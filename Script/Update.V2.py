#!/usr/bin/env python
import os
import sys
import time
import shutil
import zipfile
import ConfigParser

# change workspace 
# the path to the folder where the script is located
WorkSpace = sys.path[0]
os.chdir(WorkSpace)

# input configure file
# configure's path "$WorkSpace/config.py"
Config = ConfigParser.ConfigParser()
Config.read('config.py')

# invoking ItemList from configure file
ItemList = Config.get('Server','ItemList')

# parameter quantity judgment
try:
    ProjectList = sys.argv[1]
except IndexError, e:
    print "No parameters are found when running the program."
    sys.exit()

# Parameter content judgment
ProjectName = sys.argv[1]
if ProjectName not in ItemList:
    print "%s not in this server! Please input '%s'" % (ProjectName,ItemList)
    sys.exit()

# software lock
LockFile = "/tmp/%s.lock" % ProjectName
if os.path.exists(LockFile) is True:
    print "The Script was running!"
    sys.exit()

os.mknod("/tmp/%s.lock" % ProjectName)
 
# invoking parameter
Time = time.strftime("%y%m%d-%H%M",time.localtime())
Platforms = Config.get('Server','Platforms')
SoftName = Config.get('Server','SoftName')
WarRootPath = Config.get('Server','WarPath')
ItemRoot = Config.get('Server','ItemRoot')
ConfigPath = Config.get('Server','ConfigPath')
ItemConfigPath = Config.get('Server','ItemConfigPath')
Backup = Config.get('Server','BackupPath')
Project = Config.get('Server','ProjectHome')
War = Config.get(ProjectName,'War')

WarFullPath = "%s/%s" % (WarRootPath,War)
BackupPath = "%s/%s" % (Backup,Time)

if os.path.exists(BackupPath) is True:
    print "Do not repeat the operation in a short time, please wait for 1 minutes to run again."
    os.remove(WarFullPath)
    os.remove(LockFile)
    sys.exit()

# make backup folder
if os.path.exists(BackupPath) is False:
    os.mkdir(BackupPath)

# make project folder to update 
ProjectPath = "%s/%s/%s" % (Project,ProjectName,Time)
if os.path.exists(ProjectPath) is False:
    os.mkdir(ProjectPath)

# unzip war file
WarRead = zipfile.ZipFile(WarFullPath,'r')
for File in WarRead.namelist():
    WarRead.extract(File,ProjectPath)

# update project configure file
shutil.move(WarFullPath,BackupPath)
ItemPath = "%s/%s_%s_%s/webapps" % (ItemRoot,SoftName,ProjectName,Platforms)
if os.path.exists(ItemPath) is False:
    os.mkdir(ItemPath)

ItemFullPath = '%s/ROOT' % ItemPath
ItemConfig = '%s/%s' % (ItemFullPath,ItemConfigPath)
ItemConfigBackup = '%s.bak' % (ItemConfig)
ConfigSource = '%s/%s/properties' % (ConfigPath,ProjectName)

os.system("systemctl stop %s_%s.service" % (SoftName,ProjectName))
os.remove(ItemFullPath)
os.symlink(ProjectPath,ItemFullPath)

try:
    shutil.move(ItemConfig,ItemConfigBackup)
except IOError, error:
    print error
    sys.exit()

shutil.copytree(ConfigSource,ItemConfig)
os.system("systemctl start %s_%s.service" % (SoftName,ProjectName))
os.remove(LockFile)
