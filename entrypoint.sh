#!/bin/sh -l

variables=$(printf $INPUT_VARIABLES | sed 's/\n+/,/g')

if [ $INPUT_STRICT = true ]; then
    jinja2 --strict $INPUT_TEMPLATE -D $variables -o $INPUT_OUTPUT_FILE
fi

jinja2 $INPUT_TEMPLATE -D $variables -o $INPUT_OUTPUT_FILE
