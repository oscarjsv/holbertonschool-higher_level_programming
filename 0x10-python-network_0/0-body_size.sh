#!/bin/bash
#display size 
curl -s "$1" | wc -c
