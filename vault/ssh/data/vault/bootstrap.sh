#!/bin/sh

set -m

apk add openssh-client

vault server \
  -dev \
  -dev-root-token-id=root \
  -dev-listen-address=0.0.0.0:8200 &

while ! vault operator init -status; do
  sleep 1
  echo "Waiting for vault to come online.."
done

vault secrets enable ssh
vault write ssh/config/ca generate_signing_key=true

vault read -field=public_key ssh/config/ca > /tmp/vault.pem

while [ ! -e /root/.ssh/authorized_keys ]; do
  sleep 1
done

scp /tmp/vault.pem sshd:/etc/ssh/vault-ca.pem
ssh sshd pkill -HUP sshd

vault write ssh/roles/default - <<eof
{
  "algorithm_signer": "rsa-sha2-256",
  "allow_user_certificates": true,
  "allowed_users": "*",
  "allowed_extensions": "permit-pty",
  "default_extensions": [{
    "permit-pty": ""
  }],
  "default_user": "default",
  "key_type": "ca",
  "max_ttl": "1h",
  "ttl": "1h"
}
eof

vault write -field=signed_key ssh/sign/default \
  public_key=@$HOME/.ssh/id_rsa.pub \
  > $HOME/.ssh/id_rsa-cert.pub

if [ "$(ssh default@sshd whoami)" != "default" ]; then
  echo "vault SSH authentication failed!"
  exit 1
fi

if ssh nondefault@sshd whoami >/dev/null 2>&1; then
  echo "We shouldn't have been able to login without the new principal"
  exit 1
fi

vault write -field=signed_key ssh/sign/default \
  public_key=@$HOME/.ssh/id_rsa.pub \
  valid_principals="nondefault" \
  > $HOME/.ssh/id_rsa-cert.pub

if [ "$(ssh nondefault@sshd whoami)" != "nondefault" ]; then
  echo "We shouldn't have been able to login without the new principal"
  exit 1
fi

fg
