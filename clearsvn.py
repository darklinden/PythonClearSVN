# -*- coding: cp936 -*-
# 注明字符集
# file:clearsvn.py 删除svn目录下的所有svn文件

import os,win32con,win32api

#清除文件名头尾的引号
def trimpath(pathin):
  #如果头部存在引号
  if pathin[0] == '\"':
    pathin = pathin[1:]
    
  #如果尾部存在引号
  if pathin[(len(pathin)-1)] == '\"':
    pathin = pathin[:(len(pathin)-1)]
  
  #返回清理首尾后的字串  
  return pathin


def clearsvn(path):
  #列出子目录
  filenames = os.listdir(path)
  
  for singlefile in filenames:
    
    pathfile = path + '\\' + singlefile
    #子目录判断是否为svn文件夹
    if os.path.isdir(pathfile):
      
      if singlefile.find('.svn') != -1:
        #是的话清理文件夹后删除文件夹
        deltree(pathfile)
        
        print "清理目录:" + pathfile
        
        #修改属性，同linux下chmod
        win32api.SetFileAttributes(pathfile, win32con.FILE_ATTRIBUTE_NORMAL)
        #api删除空文件夹
        os.rmdir(pathfile)
      else:
        #不是的话递归到下一层
        clearsvn(pathfile)
        
        
def deltree(path):
  
  filenames = os.listdir(path)
  #遍历所有子目录和文件夹
  for singlefile in filenames:
    
    pathfile = path + '\\' + singlefile
    #如果是文件夹的话递归清理
    if os.path.isdir(pathfile):
      
      print "清理目录:" + pathfile
      #修改属性，同linux下chmod
      win32api.SetFileAttributes(pathfile, win32con.FILE_ATTRIBUTE_NORMAL)
      #递归到下一层
      deltree(pathfile)
      #api删除空文件夹
      os.rmdir(pathfile)
    #如果是文件的话则删除  
    if os.path.isfile(pathfile):
      
      print "删除文件:" + pathfile
      #修改属性，同linux下chmod
      win32api.SetFileAttributes(pathfile, win32con.FILE_ATTRIBUTE_NORMAL)
      #api删除文件
      os.remove(pathfile)

        
if __name__=="__main__":
  #提示用户输入目录路径
  pathin = raw_input("拖放要删除文件所在目录到此：")
  
  #清理字串首尾的引号
  path = trimpath(pathin)
  
  #确认文件夹
  choose = raw_input("需要清理的文件夹为 [ " + path + " ] y/n?:")
  
  if choose == 'y' or choose == 'Y':
    #检查用户输入的目录是否存在，如果不存在则退出程序
    if os.path.exists(path)==False:
      print "输入的目录不存在！"
      os._exit(1)

    #遍历子文件夹进行删除
    clearsvn(path)
    
    print "清理完成!"
    #运行结束暂停，显示友好信息
    os.system('pause')
  
  
  

