import os
import glob
    
oldFiles = glob.glob('*.png')
for count, x in enumerate(oldFiles):
    os.rename(oldFiles[count], 'Pic(' + str(count+0) + ').png')