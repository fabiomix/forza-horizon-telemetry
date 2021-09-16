#!/bin/bash
set -e

influx -execute 'CREATE DATABASE horizon'
influx -execute 'CREATE RETENTION POLICY two_hours ON horizon DURATION 2h REPLICATION 1 DEFAULT';
