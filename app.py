import os
import datetime
from pathlib import Path
import time
p = Path('D:\\test2')
os.chdir('D:\\test2')
#p = Path('\\\\192.168.0.106\\diskn\\DOCX\\RESULT\\2022\\')
#os.chdir('\\\\192.168.0.106\\diskn\\DOCX\\RESULT\\2022\\')



for x in p.rglob("*"):
    if x.is_file():
        timestamp = os.path.getmtime(x)
        datestamp = datetime.datetime.fromtimestamp(timestamp)
        t = os.path.getmtime(x)
        t_str = time.ctime(t)
        t_obj = time.strptime(t_str)
        form_t = time.strftime("%Y-%m-%d_%H:%M:%S", t_obj)
        form_t = form_t.replace(":", "")
        if 'ПротОпер' not in os.path.split(x)[1][0:]:
            try:
                os.rename(x, os.path.split(x)[0] + '/' + form_t + '_ПротОпер_' + os.path.split(x)[1][18:])
            except FileExistsError:
                os.rename(x, os.path.split(x)[0] + '/' + form_t + '_ПротОпер_' + os.path.split(x)[1][18:] + '_(1)')
                pass







'''
for root, dir, files in os.walk("."):
    for filename in files:

        if 'ПротОпер' not in filename:
            os.rename((root + '/' + filename), (root + '/' + filename[:18] + 'ПротОпер' + filename[17:]))
'''