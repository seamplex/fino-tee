#!/bin/sh

for i in `cat deps-run`; do
  if [ -z "`which $i`" ]; then
    echo "error: $i not installed (or not found)"
    exit 1
  fi
done

# run fino parametrically and save the results into data
fino tee.fin | tee data
