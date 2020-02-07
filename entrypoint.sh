#!/bin/sh -l

variables=$(printf $INPUT_VARIABLES | sed 's/\n+/,/g')

jinja2 --strict=$INPUT_STRICT $INPUT_TEMPLATE -D $variables > $INPUT_FILE