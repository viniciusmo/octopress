import os
import subprocess
from datetime import date
msg_commit = "git commit -am 'Atualizando meu blog'"+ str(date.today())

os.system("rm -rf ../viniciusmo.github.com/*")
subprocess.call("cp public/* -r ../viniciusmo.github.com/", shell=True)
os.chdir("../viniciusmo.github.com/")
os.system("git add .")
os.system(msg_commit)
os.system("git push origin master")
os.chdir("../octopress/")
os.system("git add .")
os.system(msg_commit)
os.system("git push origin master")
print "Finish deploy..."
