#!/bin/sh
ls /data/src | entr -r /data/executor.sh
