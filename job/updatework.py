import os
import time
import datetime
#切换至mywork目录
os.chdir(r'D:\mywork\job')
print('pwd1:',os.getcwd())
result1 = os.popen('git add --all').read()
print('result1:',result1)
time.sleep(2)
commit_str = "git commit  -m '{}'".format(time.time())
os.system(commit_str)
time.sleep(2)
os.system('git push origin master')
with open('work_update.log','a+',encoding='utf-8') as f:
    f.write(str(datetime.datetime.now()))