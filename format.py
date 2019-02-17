import glob
import os

path = 'C:/Users/ADMIN/Desktop/CU Project/labels/*'


file_names = glob.glob(path)
for f in file_names:
    output = []
    
    with open(f, 'r+') as open_file:
        data = list(open_file.read())

        
        output.append('0'); output.append(' ')

        for d in data:
            output.append(d)
            if d == '\n':
                output.append('0'); output.append(' ')  
        open_file.truncate(0)
        output.pop(len(output)-1); output.pop(len(output)-1)
        for val in output:
            open_file.write(val)

    with open(f, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(f, 'w') as fout:
        fout.writelines(data[1:])
        
