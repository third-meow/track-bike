import os
root = './train/not_bike/'

with open(os.path.join(root,'bg_description.txt'), 'w') as desc_file:
    for subdir, dirs, files in os.walk(root):
        for f in files:
            if f != 'bg_description.txt':
                desc_file.write(f'{f}\n')

