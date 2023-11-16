#!/bin/bash
dir=$(dirname "$0")
"$dir/baas_original" > "$dir/baas_log.txt" 2>&1