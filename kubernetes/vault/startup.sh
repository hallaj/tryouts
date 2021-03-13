#!/bin/sh

consul agent -config-file=/etc/consul.d/config.json -join=consul.consul &
vault server -config /etc/vault/config.hcl
