import os
import glob
import pandas as pd
os.chdir("/media/tilmann/Archiv/Archiv/FHP-Kd/Semester-02/(11EG-K)_Slow_Planet/U1_Online Energy Consumption Self-Portrait/capture/csv/tmp/test/")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ], axis=0, ignore_index=1)
combined_csv.to_csv( "Carbonara-Merged.csv", index=False, encoding='utf-8-sig')
