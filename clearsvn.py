# -*- coding: cp936 -*-
# ע���ַ���
# file:clearsvn.py ɾ��svnĿ¼�µ�����svn�ļ�

import os,win32con,win32api

#����ļ���ͷβ������
def trimpath(pathin):
  #���ͷ����������
  if pathin[0] == '\"':
    pathin = pathin[1:]
    
  #���β����������
  if pathin[(len(pathin)-1)] == '\"':
    pathin = pathin[:(len(pathin)-1)]
  
  #����������β����ִ�  
  return pathin


def clearsvn(path):
  #�г���Ŀ¼
  filenames = os.listdir(path)
  
  for singlefile in filenames:
    
    pathfile = path + '\\' + singlefile
    #��Ŀ¼�ж��Ƿ�Ϊsvn�ļ���
    if os.path.isdir(pathfile):
      
      if singlefile.find('.svn') != -1:
        #�ǵĻ������ļ��к�ɾ���ļ���
        deltree(pathfile)
        
        print "����Ŀ¼:" + pathfile
        
        #�޸����ԣ�ͬlinux��chmod
        win32api.SetFileAttributes(pathfile, win32con.FILE_ATTRIBUTE_NORMAL)
        #apiɾ�����ļ���
        os.rmdir(pathfile)
      else:
        #���ǵĻ��ݹ鵽��һ��
        clearsvn(pathfile)
        
        
def deltree(path):
  
  filenames = os.listdir(path)
  #����������Ŀ¼���ļ���
  for singlefile in filenames:
    
    pathfile = path + '\\' + singlefile
    #������ļ��еĻ��ݹ�����
    if os.path.isdir(pathfile):
      
      print "����Ŀ¼:" + pathfile
      #�޸����ԣ�ͬlinux��chmod
      win32api.SetFileAttributes(pathfile, win32con.FILE_ATTRIBUTE_NORMAL)
      #�ݹ鵽��һ��
      deltree(pathfile)
      #apiɾ�����ļ���
      os.rmdir(pathfile)
    #������ļ��Ļ���ɾ��  
    if os.path.isfile(pathfile):
      
      print "ɾ���ļ�:" + pathfile
      #�޸����ԣ�ͬlinux��chmod
      win32api.SetFileAttributes(pathfile, win32con.FILE_ATTRIBUTE_NORMAL)
      #apiɾ���ļ�
      os.remove(pathfile)

        
if __name__=="__main__":
  #��ʾ�û�����Ŀ¼·��
  pathin = raw_input("�Ϸ�Ҫɾ���ļ�����Ŀ¼���ˣ�")
  
  #�����ִ���β������
  path = trimpath(pathin)
  
  #ȷ���ļ���
  choose = raw_input("��Ҫ������ļ���Ϊ [ " + path + " ] y/n?:")
  
  if choose == 'y' or choose == 'Y':
    #����û������Ŀ¼�Ƿ���ڣ�������������˳�����
    if os.path.exists(path)==False:
      print "�����Ŀ¼�����ڣ�"
      os._exit(1)

    #�������ļ��н���ɾ��
    clearsvn(path)
    
    print "�������!"
    #���н�����ͣ����ʾ�Ѻ���Ϣ
    os.system('pause')
  
  
  

