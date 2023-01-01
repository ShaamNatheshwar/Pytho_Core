import os
if os.path.exists('sample.txt'):
    os.remove('sample.txt')
    #os.rmdir(<'filename'>)
else:
    print('This file aint there')