#!/bin/sh
elm make /data/src/Main.elm --output /data/dist/Main.js && date > /data/dist/watchme.py
