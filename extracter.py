#-*- coding: utf8 -*-

#廖彧的xls文件清洗器，从xls文件提取电话号码
import xlrd
import re
import sys

if len(sys.argv)!=2:
	exit()

pattern= re.compile(r'\d{8,}')

fname = sys.argv[1]
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    pass
    #print "no sheet in %s named Sheet1" % fname
#获取行数
nrows = sh.nrows
#获取列数
ncols = sh.ncols
#print "nrows %d, ncols %d" % (nrows,ncols)
#获取第一行第一列数据 
cell_value = sh.cell_value(1,1)
#print cell_value


#获取各行数据
for i in range(1,nrows):
    row_data = sh.row_values(i)
    
    for s in row_data:
    	try:
    		#print
    		#print(str(s))    		
    		match= pattern.match(str(s))
    		if match:
    			print(match.group(0))

    	except:
    		pass
    		#sys.stderr.write('ERROR\n');
    		
    	

