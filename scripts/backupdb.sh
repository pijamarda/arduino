#!/bin/bash
/usr/lib/postgresql/9.5/bin/pg_dump -p 5433 arduino | gzip > arduino.gz
