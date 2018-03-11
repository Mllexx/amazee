import csv, wget,urllib,shutil

fileurl='https://raw.githubusercontent.com/bryangruneberg/gsm-assessment-data/master/kafka.csv'
imgfolder = '/opt/amazee/img/'
csvfile=wget.download(fileurl)
html = "<!doctype html> <html lang='en'> <head> <meta charset='utf-8'> </head> <body>"
html_footer = "</body></html>"
img_table = "<table>"
img_table_footer = "</table>"

print('\n')

#response = urllib.request.urlopen(fileurl)
#dd = response.read();
#tt = dd.decode('utf-8')

counter = 0
tblcolcounter = 0
txtfile=open(csvfile,'r')
tblrow=""
for row in txtfile:
	if counter==0:
		print('skip the file header')
		print('\n')
		## do nothing (skips the header row)
	else:
		item = row.split(',')
		imgurl = item[6]
		imgname = item[0]+'.png'
		img_w = item[1]
		img_h = item[2]

		imgcontent=urllib.request.urlretrieve(imgurl,imgname)
		# move the image to the img folder
		shutil.move(imgname,imgfolder)
		print(imgcontent)

	if tblcolcounter==0 and counter!=0:
		tblrow += '<tr><td>'+imgname+'</td>'	
	elif tblcolcounter==3 and counter!=0:
		tblcounter=0
		tblrow += '<td>'+imgname+'</td>/tr>'
	else:
		tblrow += '<td>'+imgname+'</td>'
		counter += 1

	print(tblrow)
	tblcolcounter += 1


print('hello')

