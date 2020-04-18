#!/bin/bash
for filename in *.csv; do sed -i '1d' $filename; done