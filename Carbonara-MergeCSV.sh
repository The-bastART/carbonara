#!/bin/bash
for filename in $(ls *.csv); do sed $filename >> Carbonara_Merged.csv; done