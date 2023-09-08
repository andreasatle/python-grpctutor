#!/usr/bin/env bash
find . -depth -type d -name '__pycache__' -exec rm -rf {} \;
