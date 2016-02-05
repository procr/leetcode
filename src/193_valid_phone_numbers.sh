#!/bin/bash
# Read from the file file.txt and output all valid phone numbers to stdout.

# method 1
sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}/p' file.txt

# method 2
grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt

grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt

# method 3
awk '{if ($0 ~ /^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/) print $0}' file.txt
