#!/bin/bash
set -e

influx -execute 'CREATE DATABASE horizon';
influx -execute 'CREATE RETENTION POLICY one_day ON horizon DURATION 24h REPLICATION 1 DEFAULT';
