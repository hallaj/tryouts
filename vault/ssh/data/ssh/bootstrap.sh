#!/bin/sh

set -m

apk add openssh-client openssh-server

. /etc/init.d/sshd
generate_host_keys

adduser -D default
passwd -u default

adduser -D nondefault
passwd -u nondefault

passwd -u root

sed -i 's/#PermitRootLogin.*/PermitRootLogin without-password/g' /etc/ssh/sshd_config
sed -i 's/^#PasswordAuthentication.*/PasswordAuthentication no/g' /etc/ssh/sshd_config
echo "TrustedUserCAKeys /etc/ssh/vault-ca.pem" >> /etc/ssh/sshd_config

ssh-keygen -t rsa -b 2048 -N '' -f ~/.ssh/id_rsa
ln -s ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys

chmod 700 ~/.ssh

cat <<eof > /root/.ssh/config
UserKnownHostsFile /dev/null
StrictHostKeyChecking no
eof

/usr/sbin/sshd -D -E /proc/1/fd/1
