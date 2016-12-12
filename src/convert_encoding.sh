#!/bin/bash
converted="converted_"
txt=".txt"
for file in * ; do
    echo "$file"
    output=$converted$file$txt
    echo "$output"
    iconv -f SHIFT-JIS -t UTF-8 "$file" > "$output"
done
