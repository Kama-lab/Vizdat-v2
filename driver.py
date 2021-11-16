import os

with open('requirements.txt') as f:
    line = f.readlines()

for l in line:
    print(f"{l.strip()}")
    os.system(f'sh run.sh {l.strip()}')
