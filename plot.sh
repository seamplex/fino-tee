#!/bin/sh

for i in `cat deps-plot`; do
  if [ -z "`which $i`" ]; then
    echo "error: $i not installed (or not found)"
    exit 1
  fi
done

if [ ! -e data ]; then
  echo "error: data file not found, first run the case with ./run.sh"
  exit 1
fi

pyxplot plot.ppl

for i in `seq 1 11`; do
  # create VTKs with the location of the SCLs
  m4 -Dd=$i scls.vtk.m4 > scls-$i.vtk
  python tee-post.py $i
  python tee-scls.py $i
done
