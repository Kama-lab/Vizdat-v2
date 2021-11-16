import os

f = open('ignored_packs.txt','w')

with open('requirements.txt') as f:
    line = f.readlines()

for l in line:
    print(f"{l.strip()}")
    strg = l + os.popen(f'sh run.sh {l.strip()}').read() + "\n" + "======================================================="
    f.write(strg)

f.close()
