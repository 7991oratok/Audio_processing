import pathlib
import os


initial = 'chigau_chigau'

all = pathlib.Path('2019_12_MFCC_DATA/').glob('*.txt')
for i,f in enumerate(all):
    print(f.name.replace('.txt', ''))
    


