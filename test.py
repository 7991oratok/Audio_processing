import pathlib
import os


initial = 'chigau_chigau'

all = pathlib.Path('result/').glob('*.wav')
for i,f in enumerate(all):
    path1 = 'result/' + f.name 
    path2 = 'result/' + initial + str(i) + '.wav'
    os.rename(path1, path2)
    


