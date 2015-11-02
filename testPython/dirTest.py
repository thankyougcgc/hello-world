#!/usr/bin/python2.7
# -*- coding:utf-8 -*- 
import os,sys
import ConfigParser
defaultPath = "/home/gaochao/GitHub/hello-world"
#print os.listdir
def pathWalk(path,filename):
	print "pathWalk exec","path=",path,"filename=",filename
	fileOpened = open(filename,"a")
	for root,dirs,files in os.walk(path):
		fileOpened.write("%s,%s,%s \n" % (root,dirs,files))

if __name__ == '__main__':
	if "-p" == sys.argv[1]:
		print "not default"
		pathWalk(sys.argv[2],"testNotDefault.txt")
	elif "-c" == sys.argv[1]:
		cf = ConfigParser.ConfigParser()  
		cf.read("dirTest.conf") 
		#s = cf.sections()
		#print 'section:', s
		#path = cf.options("path")
		pathName = cf.get("path","pathName")
		kvs = cf.items("path")
		print type("pathName")
		print type(defaultPath)
		print kvs
		if pathName == defaultPath:
			print "equal"
		else:
			print "not equal"
		#file = cf.options("file")
		fileName = cf.get("file","fileName")
		print pathName,fileName
		pathWalk(pathName,fileName)
	else:
		pathWalk(defaultPath,"test.txt")