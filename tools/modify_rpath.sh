#!/bin/bash

patchelf=third_party/patchelf-0.9/src/patchelf

files=`find $1 -name "*.so"`
for file in $files; do
    echo "Modyfing ${file}: setting RPATH to \'\$ORIGIN"
    $patchelf --set-rpath '$ORIGIN' $file
done
