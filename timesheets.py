#!/opt/virtual_environments/timesheets/bin/python

###############
### Imports ###
###############
import csv
import os
import sys
import datetime
from pprint import pprint
from fdfgen import forge_fdf

###################
### Global Vars ###
###################
sys.path.insert(0, os.getcwd())
filename_prefix = "timesheets"
# csv_file = "timesheets.csv"
csv_file = []
pdf_file = "timesheets.pdf"
tmp_file = "tmp.fdf"
output_folder = './output/'
temp_folder = './temp/'
pdf_pages = ""
timesheet_file = ""

Department = ''
PayPeriodTitle = 'BS'
PayPeriodNumber = ''
StartDate = ''
EndDate = ''
DueByDate = ''
Days = []
UserList = ''
# Day1 = ''
# Day2 = ''
# Day3 = ''
# Day4 = ''
# Day5 = ''
# Day6 = ''
# Day7 = ''
# Day8 = ''
# Day9 = ''
# Day10 = ''
# Day11 = ''
# Day12 = ''
# Day13 = ''
# Day14 = ''

###############
### Classes ###
###############

#################
### Functions ###
#################
def build_csv():
	buildDates()

	# print "1:",PayPeriodNumber
	# print "2:",StartDate
	# print "3:",EndDate
	# print "4:",DueByDate
	# print "5:",UserList

	csv_data = csv.reader(open(UserList))
	user_data = []
	
	for i,row in enumerate(csv_data):
		user_data.append(row)
	# pprint(user_data)

	# print "Length:",len(user_data)
	pages = len(user_data)/4
	if len(user_data)%4 > 0:
		pages+=1
	# print pages

	for i in range(pages):
		header = "Pages,DeptNumber,PayPeriodTitle,PayPeriodNumber,StartDate,EndDate,DueByDate,Day1,Day2,Day3,Day4,Day5,Day6,Day7,Day8,Day9,Day10,Day11,Day12,Day13,Day14,Name1,ID1,Assignment1,Name2,ID2,Assignment2,Name3,ID3,Assignment3,Name4,ID4,Assignment4\n"
		data = str(i)+","+Department+","+"BS,"+PayPeriodNumber+","+StartDate+","+EndDate+","+DueByDate+","+Days[0]+","+Days[1]+","+Days[2]+","+Days[3]+","+Days[4]+","+Days[5]+","+Days[6]+","+Days[7]+","+Days[8]+","+Days[9]+","+Days[10]+","+Days[11]+","+Days[12]+","+Days[13]
		Name1 = ID1 = Assignment1 = Name2 = ID2 = Assignment2 = Name3 = ID3 = Assignment3 = Name4 = ID4 = Assignment4 = ""
		for j in range(4):
			if j == 0:
				if j+4*i < len(user_data):
					Name1 = '"'+user_data[j+4*i][0]+", "+user_data[j+4*i][1]+'"'
					ID1 = user_data[j+4*i][2]
					Assignment1 = user_data[j+4*i][3]
			if j == 1:
				if j+4*i < len(user_data):
					Name2 = '"'+user_data[j+4*i][0]+", "+user_data[j+4*i][1]+'"'
					ID2 = user_data[j+4*i][2]
					Assignment2 = user_data[j+4*i][3]
			if j == 2:
				if j+4*i < len(user_data):
					Name3 = '"'+user_data[j+4*i][0]+", "+user_data[j+4*i][1]+'"'
					ID3 = user_data[j+4*i][2]
					Assignment3 = user_data[j+4*i][3]
			if j == 3:
				if j+4*i < len(user_data):
					Name4 = '"'+user_data[j+4*i][0]+", "+user_data[j+4*i][1]+'"'
					ID4 = user_data[j+4*i][2]
					Assignment4 = user_data[j+4*i][3]
		data = data+","+Name1+","+ID1+","+Assignment1+","+Name2+","+ID2+","+Assignment2+","+Name3+","+ID3+","+Assignment3+","+Name4+","+ID4+","+Assignment4+"\n"
		f = open(temp_folder+'timesheets_'+str(i)+'.csv', 'w')
		f.write(header)
		f.write(data)
		csv_file.append(temp_folder+'timesheets_'+str(i)+'.csv')

def buildDates():
	global StartDate
	global EndDate
	global DueByDate
	#start = datetime.datetime.strptime(StartDate, "%m/%d/%y")
	start = datetime.datetime.strptime(sys.argv[3], "%Y-%m-%d")
	StartDate = start.strftime("%m/%d/%y") 
	end = start + datetime.timedelta(days=13)
	EndDate = end.strftime("%m/%d/%y")
	due = end + datetime.timedelta(days=3)
	DueByDate = due.strftime("%m/%d/%y")

	current = start
	while current <= end:
		Days.append(current.strftime("%m/%d"))
		current += datetime.timedelta(days=1)
	# pprint(Days)

def checkArgs():
	global PayPeriodNumber
	global UserList
	global Department
	if len(sys.argv) < 5:
		print "Missing Arguments"
		return -1
	elif not os.path.isfile(sys.argv[4]):
		print "File Not Found"
		return -1
	else:
		Department = sys.argv[1]
		PayPeriodNumber = sys.argv[2]
		UserList = sys.argv[4]
		return 0
def combinePDF():
	global pdf_pages
	global timesheet_file
	print("<BR>Creating Timesheet...<BR><BR>")
	cmd = 'pdftk {0} cat output {1}'.format(pdf_pages, output_folder+"timesheets_BS"+PayPeriodNumber+".pdf")
	os.system(cmd)
	timesheet_file = output_folder+"timesheets_BS"+PayPeriodNumber+".pdf"

def form_fill(fields):
	global pdf_pages
	# pprint(fields)
	fdf = forge_fdf("",fields,[],[],[])
	fdf_file = open(tmp_file,"w")
	fdf_file.write(fdf)
	fdf_file.close()
	output_file = '{0}{1}_{2}.pdf'.format(temp_folder, filename_prefix, fields[0][1])
	
	if pdf_pages == "":
		pdf_pages = output_file
	else:
		pdf_pages = pdf_pages + " " + output_file

	cmd = 'pdftk "{0}" fill_form "{1}" output "{2}" dont_ask'.format(pdf_file, tmp_file, output_file)
	os.system(cmd)
	os.remove(tmp_file)

def generatePDFs():
	print("Generating Forms:<BR>")
	print("----------------<BR>")
	for csv in csv_file:
		data = process_csv(csv)	
		for i in data:
			if i[0][1] == 'Yes':
				continue
			print("{0}_{1}.pdf created...<BR>".format(filename_prefix, i[0][1]))
			form_fill(i)
	combinePDF()

def main():
	if checkArgs() != 0:
		print "Exiting.....<BR>"
	else:
		print "Running.....<BR>"
		build_csv()
		generatePDFs()
		print timesheet_file

def process_csv(file):
	headers = []
	data =  []
	csv_data = csv.reader(open(file))
	for i, row in enumerate(csv_data):
		if i == 0:
			headers = row
			continue;
		field = []
		for i in range(len(headers)):
			field.append((headers[i], row[i]))
		data.append(field)
	return data

############
### Main ###
############
if __name__ == '__main__':
 	main()
