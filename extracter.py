# coding: utf-8
import xlrd
import re
import sys
import getopt
import os

def Usage():
    print 'test.py usage:'
    print '-h,--help: print help message.'
    print '-v, --version: print script version'



def get_phone_number_from_file(fname):
	pattern= re.compile(r'\d{8,}')
	bk= xlrd.open_workbook(fname)
	sheets= bk.sheets()
	for sh in sheets:
		for i in range(0,sh.nrows):
			temp= sh.row_values(i)	
			ans= str(temp)
			phone_numbers=	re.findall(pattern, ans)
			for phone_number in phone_numbers:
				print(phone_number)

def get_phone_number_from_folder(foldername):
	files= os.listdir(foldername)
	for f in files:
		get_phone_number_from_file(foldername+'/'+f)


if __name__ == '__main__':
	if len(sys.argv)!=2:
		sys.stderr.write("ERROR: Please input the foldername name.\n")		
		exit()
#	get_phone_number_from_file(sys.argv[1])
	get_phone_number_from_folder(sys.argv[1])	




