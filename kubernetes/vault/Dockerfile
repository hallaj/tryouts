FROM consul:latest AS consul
FROM vault:latest AS vault

COPY --from=consul /bin/consul /bin/consul
COPY startup.sh /startup.sh
