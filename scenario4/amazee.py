import csv, wget,urllib,shutil

fileurl='https://raw.githubusercontent.com/bryangruneberg/gsm-assessment-data/master/kafka.csv'
imgfolder = 'img/'
csvfile=wget.download(fileurl)
html_file = "<!doctype html> <html lang='en'> <head> <meta charset='utf-8'> </head> <body>"
html_footer = "</body></html>"
img_table = "<table>"
img_table_footer = "</table>"
print('\n')

counter = 0
tblcolcounter = 0
txtfile = open(csvfile,'r')
tblrow  = "<tr>"

for row in txtfile:
	if counter==0:
		print('skip the file header')
		print('\n')
		## do nothing (skips the header row)
	else:
		item = row.split(',')
		imgurl  = item[6]
		imgname = item[0]+'.png'
		img_w = item[1]
		img_h = item[2]

		imgcontent=urllib.request.urlretrieve(imgurl,imgname)
		# move the image to the img folder
		shutil.move(imgname,imgfolder)
		print(imgcontent)

		if tblcolcounter == 0:
			tblrow += '<td><img src="img/'+imgname+'"/></td>'	
		elif tblcolcounter == 4:
			tblrow += '<td><img src="img/'+imgname+'"/></td></tr>'
			tblrow += "<tr>"
			tblcolcounter = 0
		else:
			tblrow += '<td><img src="img/'+imgname+'"/></td>'		
		print(tblcolcounter)

	tblcolcounter += 1
	counter +=1

html_file += img_table
html_file += tblrow
html_file += img_table_footer
html_file += html_footer

## WRITE THE HTML OUT PUT FILE
snippet_file = open('output.html','w')
snippet_file.write(html_file)
snippet_file.close();

#print(html_file)
print('hello')

