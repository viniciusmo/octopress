import os
os.system("rm -rf ../viniciusmo.github.com/*")
os.system("cd public/")
os.system("cp *  ../viniciusmo.github.com/")
os.system("cd ../")
os.system("cd ../viniciusmo.github.com/")
os.system("git add .")
os.system("git commit -am 'Atulizando meu blog'")
os.system("git push origin master")
os.system("cd ../octopress/")
print "Finish deploy..."
