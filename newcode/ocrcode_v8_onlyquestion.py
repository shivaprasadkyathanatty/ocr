# to upload files from local to s3 and mark them public: $aws s3 cp /home/shivaprasad/Downloads/iClicker_OCR/new_code/images/raw_image/ s3://iclicker-ocr/raw_image/ --acl public-read --recursive
# refer: https://medium.freecodecamp.org/getting-started-with-tesseract-part-i-2a6a6b1cf75e
import cv2
import os
import numpy as np
import pytesseract
import mysql.connector
import time
import sys
from tesserocr import PyTessBaseAPI
import filetype
# from importlib import reload
import codecs


def mysql_conn():
	cnx = mysql.connector.connect(user='root', password='aceuser123',
								  host='localhost',
								  database='central',autocommit=True)
	return cnx


def pattern_A_dot(tmp,img_file_name,low_confidence_score_count,high_confidence_score_count):
	file=img_file_name
	qA=tmp.find(" A. ")
	qB=tmp.find(" B. ")
	qC=tmp.find(" C. ")
	qD=tmp.find(" D. ")
	qE=tmp.find(" E. ")
	qF=tmp.find(" F. ")
	qG=tmp.find(" G. ")
	qH=tmp.find(" H. ")

	if qA != -1:
		qApos=tmp.find(" A. ")
	else:
		qApos="NA"
		qAcont="NULL"
		qcont=tmp[:]
	
	if qB != -1:
		qBpos=tmp.find(" B. ")
	else:
		qBpos="NA"
		qBcont="NULL"

	if qC != -1:
		qCpos=tmp.find(" C. ")
	else:
		qCpos="NA"
		qCcont="NULL"

	if qD != -1:
		qDpos=tmp.find(" D. ")
	else:
		qDpos="NA"
		qDcont="NULL"

	if qE != -1:
		qEpos=tmp.find(" E. ")
	else:
		qEpos="NA"
		qEcont="NULL"

	if qF != -1:
		qFpos=tmp.find(" F. ")
	else:
		qFpos="NA"
		qFcont="NULL"

	if qG != -1:
		qGpos=tmp.find(" G. ")
	else:
		qGpos="NA"
		qGcont="NULL"

	if qH != -1:
		qHpos=tmp.find(" H. ")
	else:
		qHpos="NA"
		qHcont="NULL"

	if qHpos!="NA":
		qHcont=tmp[qHpos+4:]
	
	if qGpos!="NA":
		if qHpos=="NA":
			qGcont=tmp[qGpos+4:]		
		else:
			qGcont=tmp[qGpos+4:qHpos]		

	if qFpos!="NA":
		if qGpos=="NA":
			qFcont=tmp[qFpos+4:]		
		else:
			qFcont=tmp[qFpos+4:qGpos]		

	if qEpos!="NA":
		if qFpos=="NA":
			qEcont=tmp[qEpos+4:]		
		else:
			qEcont=tmp[qEpos+4:qFpos]		

	if qDpos!="NA":
		if qEpos=="NA":
			qDcont=tmp[qDpos+4:]		
		else:
			qDcont=tmp[qDpos+4:qEpos]		

	if qCpos!="NA":
		if qDpos=="NA":
			qCcont=tmp[qCpos+4:]		
		else:
			qCcont=tmp[qCpos+4:qDpos]		

	if qBpos!="NA":
		if qCpos=="NA":
			qBcont=tmp[qBpos+4:]		
		else:
			qBcont=tmp[qBpos+4:qCpos]		

	if qApos!="NA":
		qcont=tmp[:qApos]
		if qBpos=="NA":
			qAcont=tmp[qApos+4:]		
	
		else:
			qAcont=tmp[qApos+4:qBpos]		

	qcont=qcont.strip()
	qAcont=""
	qBcont=""
	qCcont=""
	qDcont=""
	qEcont=""
	qFcont=""
	qGcont=""
	qHcont=""

	print ("Question:\t"+qcont.strip())
	print ("Option 1:\t"+qAcont.strip())
	print ("Option 2:\t"+qBcont.strip())
	print ("Option 3:\t"+qCcont.strip())
	print ("Option 4:\t"+qDcont.strip())
	print ("Option 5:\t"+qEcont.strip())
	print ("Option 6:\t"+qFcont.strip())
	print ("Option 7:\t"+qGcont.strip())
	print ("Option 8:\t"+qHcont.strip())

	insert_data(file,qcont,qAcont,qBcont,qCcont,qDcont,qEcont,qFcont,qGcont,qHcont,low_confidence_score_count,high_confidence_score_count)


def pattern_a_dot(tmp,img_file_name,low_confidence_score_count,high_confidence_score_count):
	file=img_file_name
	
	qA=tmp.find(" a. ")
	qB=tmp.find(" b. ")
	qC=tmp.find(" c. ")
	qD=tmp.find(" d. ")
	qE=tmp.find(" e. ")
	qF=tmp.find(" f. ")
	qG=tmp.find(" g. ")
	qH=tmp.find(" h. ")

	if qA != -1:
		qApos=tmp.find(" a. ")
	else:
		qApos="NA"
		qAcont="NULL"
		qcont=tmp[:]
	
	if qB != -1:
		qBpos=tmp.find(" b. ")
	else:
		qBpos="NA"
		qBcont="NULL"

	if qC != -1:
		qCpos=tmp.find(" c. ")
	else:
		qCpos="NA"
		qCcont="NULL"

	if qD != -1:
		qDpos=tmp.find(" d. ")
	else:
		qDpos="NA"
		qDcont="NULL"

	if qE != -1:
		qEpos=tmp.find(" e. ")
	else:
		qEpos="NA"
		qEcont="NULL"

	if qF != -1:
		qFpos=tmp.find(" f. ")
	else:
		qFpos="NA"
		qFcont="NULL"

	if qG != -1:
		qGpos=tmp.find(" g. ")
	else:
		qGpos="NA"
		qGcont="NULL"

	if qH != -1:
		qHpos=tmp.find(" h. ")
	else:
		qHpos="NA"
		qHcont="NULL"

	if qHpos!="NA":
		qHcont=tmp[qHpos+4:]
	
	if qGpos!="NA":
		if qHpos=="NA":
			qGcont=tmp[qGpos+4:]		
		else:
			qGcont=tmp[qGpos+4:qHpos]		

	if qFpos!="NA":
		if qGpos=="NA":
			qFcont=tmp[qFpos+4:]		
		else:
			qFcont=tmp[qFpos+4:qGpos]		

	if qEpos!="NA":
		if qFpos=="NA":
			qEcont=tmp[qEpos+4:]		
		else:
			qEcont=tmp[qEpos+4:qFpos]		

	if qDpos!="NA":
		if qEpos=="NA":
			qDcont=tmp[qDpos+4:]		
		else:
			qDcont=tmp[qDpos+4:qEpos]		

	if qCpos!="NA":
		if qDpos=="NA":
			qCcont=tmp[qCpos+4:]		
		else:
			qCcont=tmp[qCpos+4:qDpos]		

	if qBpos!="NA":
		if qCpos=="NA":
			qBcont=tmp[qBpos+4:]		
		else:
			qBcont=tmp[qBpos+4:qCpos]		

	if qApos!="NA":
		qcont=tmp[:qApos]
		if qBpos=="NA":
			qAcont=tmp[qApos+4:]		
	
		else:
			qAcont=tmp[qApos+4:qBpos]		


	
	qcont=qcont.strip()
	qAcont=""
	qBcont=""
	qCcont=""
	qDcont=""
	qEcont=""
	qFcont=""
	qGcont=""
	qHcont=""

	print ("Question:\t"+qcont.strip())
	print ("Option 1:\t"+qAcont.strip())
	print ("Option 2:\t"+qBcont.strip())
	print ("Option 3:\t"+qCcont.strip())
	print ("Option 4:\t"+qDcont.strip())
	print ("Option 5:\t"+qEcont.strip())
	print ("Option 6:\t"+qFcont.strip())
	print ("Option 7:\t"+qGcont.strip())
	print ("Option 8:\t"+qHcont.strip())

	insert_data(file,qcont,qAcont,qBcont,qCcont,qDcont,qEcont,qFcont,qGcont,qHcont,low_confidence_score_count,high_confidence_score_count)



def pattern_A_bracket(tmp,img_file_name,low_confidence_score_count,high_confidence_score_count):
	file=img_file_name
	
	qA=tmp.find(" A) ")
	qB=tmp.find(" B) ")
	qC=tmp.find(" C) ")
	qD=tmp.find(" D) ")
	qE=tmp.find(" E) ")
	qF=tmp.find(" F) ")
	qG=tmp.find(" G) ")
	qH=tmp.find(" H) ")

	if qA != -1:
		qApos=tmp.find(" A) ")
	else:
		qApos="NA"
		qAcont="NULL"
		qcont=tmp[:]
	
	if qB != -1:
		qBpos=tmp.find(" B) ")
	else:
		qBpos="NA"
		qBcont="NULL"

	if qC != -1:
		qCpos=tmp.find(" C) ")
	else:
		qCpos="NA"
		qCcont="NULL"

	if qD != -1:
		qDpos=tmp.find(" D) ")
	else:
		qDpos="NA"
		qDcont="NULL"

	if qE != -1:
		qEpos=tmp.find(" E) ")
	else:
		qEpos="NA"
		qEcont="NULL"

	if qF != -1:
		qFpos=tmp.find(" F) ")
	else:
		qFpos="NA"
		qFcont="NULL"

	if qG != -1:
		qGpos=tmp.find(" G) ")
	else:
		qGpos="NA"
		qGcont="NULL"

	if qH != -1:
		qHpos=tmp.find(" H) ")
	else:
		qHpos="NA"
		qHcont="NULL"

	if qHpos!="NA":
		qHcont=tmp[qHpos+4:]
	
	if qGpos!="NA":
		if qHpos=="NA":
			qGcont=tmp[qGpos+4:]		
		else:
			qGcont=tmp[qGpos+4:qHpos]		

	if qFpos!="NA":
		if qGpos=="NA":
			qFcont=tmp[qFpos+4:]		
		else:
			qFcont=tmp[qFpos+4:qGpos]		

	if qEpos!="NA":
		if qFpos=="NA":
			qEcont=tmp[qEpos+4:]		
		else:
			qEcont=tmp[qEpos+4:qFpos]		

	if qDpos!="NA":
		if qEpos=="NA":
			qDcont=tmp[qDpos+4:]		
		else:
			qDcont=tmp[qDpos+4:qEpos]		

	if qCpos!="NA":
		if qDpos=="NA":
			qCcont=tmp[qCpos+4:]		
		else:
			qCcont=tmp[qCpos+4:qDpos]		

	if qBpos!="NA":
		if qCpos=="NA":
			qBcont=tmp[qBpos+4:]		
		else:
			qBcont=tmp[qBpos+4:qCpos]		

	if qApos!="NA":
		qcont=tmp[:qApos]
		if qBpos=="NA":
			qAcont=tmp[qApos+4:]		
	
		else:
			qAcont=tmp[qApos+4:qBpos]		

	
	qcont=qcont.strip()
	qAcont=""
	qBcont=""
	qCcont=""
	qDcont=""
	qEcont=""
	qFcont=""
	qGcont=""
	qHcont=""

	print ("Question:\t"+qcont.strip())
	print ("Option 1:\t"+qAcont.strip())
	print ("Option 2:\t"+qBcont.strip())
	print ("Option 3:\t"+qCcont.strip())
	print ("Option 4:\t"+qDcont.strip())
	print ("Option 5:\t"+qEcont.strip())
	print ("Option 6:\t"+qFcont.strip())
	print ("Option 7:\t"+qGcont.strip())
	print ("Option 8:\t"+qHcont.strip())


	insert_data(file,qcont,qAcont,qBcont,qCcont,qDcont,qEcont,qFcont,qGcont,qHcont,low_confidence_score_count,high_confidence_score_count)

def insert_data(file,qcont,qAcont,qBcont,qCcont,qDcont,qEcont,qFcont,qGcont,qHcont,low_confidence_score_count,high_confidence_score_count):
	mysqlcon=mysql_conn()
	cursor=mysqlcon.cursor()
	cursor.execute('insert into central.iclicker (file,question,optionA,optionB,optionC,optionD,optionE,optionF,optionG,optionH,low_confidence_score_count,high_confidence_score_count) values ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}","{10}","{11}");'.format(file,qcont,qAcont,qBcont,qCcont,qDcont,qEcont,qFcont,qGcont,qHcont,low_confidence_score_count,high_confidence_score_count))
	time.sleep(1)

def get_options():
	mysqlcon=mysql_conn()
	cursor=mysqlcon.cursor()
	cursor.execute('select * from central.iclicker;')
	options=cursor.fetchall()
	return options

def get_file():
	mysqlcon=mysql_conn()
	cursor=mysqlcon.cursor()
	cursor.execute('select distinct file from central.iclicker;')
	file_names = cursor.fetchall()
	return file_names

def guessfiletype(file_name):
	kind = filetype.guess(file_name)
	if kind is None:
		print('Cannot guess file type!')
		return
	return kind.extension
	#print('File extension: %s' % kind.extension)
	#print('File MIME type: %s' % kind.mime)

def main():
	#ipdb = Pdb()
	#ipdb.set_trace()
	#setup system
	reload(sys)
	sys.setdefaultencoding("utf-8")
	# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
	mysqlcon=mysql_conn()
	cursor=mysqlcon.cursor()
	#clean the mysql table
	cursor.execute('delete from central.iclicker;')
		
	# define raw input image file path
	raw_image_path_folder = "/home/shivaprasad/Downloads/iClicker_OCR/new_code/images/raw_image/"
	# define formatted input file path
	format_image_path = "/home/shivaprasad/Downloads/iClicker_OCR/new_code/images/formatted_image/"
	# delete all files from format_image_path
	for f in os.listdir(format_image_path):
		os.remove(os.path.join(format_image_path,f))
	# define output text file path
	text_file_path="/home/shivaprasad/Downloads/iClicker_OCR/new_code/extracted_text/"
	# delete all files from text_file_path
	for f in os.listdir(text_file_path):
		os.remove(os.path.join(text_file_path,f))
	for img in os.listdir(raw_image_path_folder):
		print (img)
	
	for imge in os.listdir(raw_image_path_folder):
		# retain raw_image_path for str manipulation
		#raw_image_path=imge
		#img=imge
		# Read image using opencv
		img=cv2.imread(raw_image_path_folder+imge)
		# Rescale the image, if needed. Tesseract works best on images that are 300 dpi, or more.
		img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
		# Noise removal
		# Convert to gray
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		# Apply dilation and erosion to remove some noise
		kernel = np.ones((1, 1), np.uint8)
		img = cv2.dilate(img, kernel, iterations=1)
		img = cv2.erode(img, kernel, iterations=1)
		# Apply blur to smooth out the edges
		img = cv2.GaussianBlur(img, (5, 5), 0)
		# Binarization
		# Apply threshold to get image with only b&w (binarization)
		img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
		# Extract the file name without the file extension
		img_file_name = imge
		print ("image file that is getting processed is: " + img_file_name)
		# Create a directory for outputs
		# Find file type for missing file extension
		full_raw_image_file_path = raw_image_path_folder + img_file_name
		file_type = os.path.splitext(full_raw_image_file_path)[1]
		if (file_type) == '':
			file_type = guessfiletype(full_raw_image_file_path)
			img_save_path = format_image_path+img_file_name + "." + file_type
		else:
			img_save_path = format_image_path+img_file_name
		# Write the file to output file
		cv2.imwrite(img_save_path, img)
		# Recognize text with tesseract for python
		extracted_text = pytesseract.image_to_string(img_save_path, lang="eng")
		print (extracted_text)
		# insert extracted text into a file
		extract_file=text_file_path+img_file_name+".txt"
		# open text file to insert extracted text
		with open(extract_file,"wb") as f:
			f.write(extracted_text.encode('utf-8'))
		# remove new lines from the text file
		fd=tmp=None
		fd=file(extract_file,"rb").read()
		tmp=fd.replace("\n"," ").replace("\x0C"," ").replace("iClicker"," ").replace("Question @"," ").replace("%"," ")
		tmp=" ".join([e for e in tmp.split(" ")if e.strip()])
		file(extract_file,"wb").write(tmp)

		# find confidence score of ocr text and send it to sql table
		confidence_score=[]
		with PyTessBaseAPI() as api:
			api.SetImageFile(img_save_path)
			confidence_score=api.AllWordConfidences()
		low_confidence_score=[]
		high_confidence_score=[]
		for score in confidence_score:
			if score < 90:
				low_confidence_score.append(score)
			else:
				high_confidence_score.append(score)
		low_confidence_score_count=len(low_confidence_score)
		high_confidence_score_count=len(high_confidence_score)

		if low_confidence_score_count < 10:
			# find pattern of multiple choice questions and send them for respective functions to parsing
			pattern=tmp.find(" A. ")
			if pattern !=-1:
				pattern_A_dot(tmp,img_file_name,low_confidence_score_count,high_confidence_score_count)

			pattern=tmp.find(" a. ")
			if pattern !=-1:
				pattern_a_dot(tmp,img_file_name,low_confidence_score_count,high_confidence_score_count)

			pattern=tmp.find(" A) ")
			if pattern !=-1:
				pattern_A_bracket(tmp,img_file_name,low_confidence_score_count,high_confidence_score_count)


	# removing records from sql table if they produced only one option in sql result or if they produced infrequent values for options
	options=get_options()
	for option in options:
		if option[3]== "NULL":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))		
		elif option[9]!="NULL" and option[8]=="NULL":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[8]!="NULL" and option[7]=="NULL":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[7]!="NULL" and option[6]=="NULL":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[6]!="NULL" and option[5]=="NULL":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[5]!="NULL" and option[4]=="NULL":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[4]!="NULL" and option[3]=="NULL":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[3]!="NULL" and option[2]=="NULL":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[2]!="NULL" and option[1]=="NULL":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[9]!="" and option[8]=="":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[8]!="" and option[7]=="":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[7]!="" and option[6]=="":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[6]!="" and option[5]=="":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[5]!="" and option[4]=="":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[4]!="" and option[3]=="":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[3]!="" and option[2]=="":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))
		elif option[2]!="" and option[1]=="":
			cursor.execute('delete from central.iclicker where file="{0}";'.format(option[0]))

	# get names of all files that produced result
	sql_file_names=get_file()
	sql_file_names=list(sql_file_names)
	#print 'files that produced result:\n',sql_file_names
	sql_file_names_list=[]
	
	for f in sql_file_names:
		sql_file_names_list.append(f[0])
	# get names of all files that were used as input files
	print (sql_file_names_list)
	extract_file_names=[]
	for f in os.listdir(text_file_path):
		extract_file_names.append(os.path.splitext(f)[0])
	print (extract_file_names)
	
	# files that didnt produce result
	diff_list=list(set(extract_file_names)-set(sql_file_names_list))
	#print 'files that didnt produce result\n',diff_list[0]
	print (diff_list)

	
if __name__ == '__main__':
	main()