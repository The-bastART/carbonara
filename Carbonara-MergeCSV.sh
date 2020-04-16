#!/bin/bash
cd /media/tilmann/Archiv/Archiv/FHP-Kd/Semester-02/(11EG-K)_Slow_Planet/U1_Online Energy Consumption Self-Portrait/capture/csv/tmp/
for filename in $(ls *.csv); do sed 1d $filename >> Carbonara_Merged.csv; done