# Import required module/s
import csv

def readMarkSheet(filename):
	"""Reads the input CSV file of Mark Sheet and creates a mapping of student name with his/her marks for each subject.

	Parameters
	----------
	file_name : str
		CSV file name of Mark Sheet

	Returns
	-------
	dict
		Mapping of each student's name and his/her marks for each subject as { Key : Value } pair

	Example
	-------
	>>> csv_file_name = 'task1_sample.csv'
	>>> print( readMarkSheet( csv_file_name ) )
	{
		'Artus Syne': {'marks': [43.0, 71.0, 55.0, 16.0, 51.0]}, 'Evey Reburn': {'marks': [49.0, 7.0, 53.0, 50.0, 63.0]},
		'Giff Wickmann': {'marks': [63.0, 37.0, 21.0, 87.0, 9.0]}, 'Garrot Casetta': {'marks': [22.0, 3.0, 91.0, 75.0, 52.0]},
		'Roselle Maes': {'marks': [71.0, 90.0, 96.0, 79.0, 48.0]}, 'Torin Ziehms': {'marks': [71.0, 31.0, 83.0, 1.0, 25.0]},
		'Jaye Etock': {'marks': [92.0, 9.0, 2.0, 78.0, 55.0]}, 'Thomasina Tinkham': {'marks': [25.0, 78.0, 46.0, 46.0, 90.0]},
		'Adolphus Biernat': {'marks': [91.0, 96.0, 98.0, 94.0, 100.0]}, 'Rex Aspinell': {'marks': [34.0, 75.0, 51.0, 38.0, 99.0]}
	}
	"""

	name_marks_mapping = {}

	##############	ADD YOUR CODE HERE	##############
	filename = open('task1_sample.csv','r')
	csvreader = csv.reader(filename)
	fields = []
	fields = next(csvreader)
	rows = []
	for row in csvreader:
	    rows.append(row)
	#print(rows)
	#print(fields)
	#dk = {}
	nl = []
	marks = []
	markslist = []
	for name in rows:
	    nl.append(name[0])
	#print(rows)
	for i in rows:
	    for j in range(1,6):
	        marks.append(i[j])
	    markslist.append(marks)
	    marks = []
	fr = {}
	frlist = []
	for stuff in markslist:
	    fr["marks"] = stuff
	    frlist.append(fr)
	    fr = {}
	for i in range(len(nl)):
	    name_marks_mapping[nl[i]] = frlist[i]



	##################################################

	return name_marks_mapping


def generateGradeCard(mapping_dict):
	"""Generate the Grade Card for all students in the given mapping of student and their scores in all subjects with the grade each one has received.

	Parameters
	----------
	mapping_dict : dict
		Mapping of each student's name and his/her marks for each subject as { Key : Value } pair

	Returns
	-------
	dict
		Grade Card for all students with their scores in all subjects and the grade each one has received

	Example
	-------
	>>> name_marks_mapping = {
								'Artus Syne': {'marks': [43.0, 71.0, 55.0, 16.0, 51.0]}, 'Evey Reburn': {'marks': [49.0, 7.0, 53.0, 50.0, 63.0]},
								'Giff Wickmann': {'marks': [63.0, 37.0, 21.0, 87.0, 9.0]}, 'Garrot Casetta': {'marks': [22.0, 3.0, 91.0, 75.0, 52.0]},
								'Roselle Maes': {'marks': [71.0, 90.0, 96.0, 79.0, 48.0]}, 'Torin Ziehms': {'marks': [71.0, 31.0, 83.0, 1.0, 25.0]},
								'Jaye Etock': {'marks': [92.0, 9.0, 2.0, 78.0, 55.0]}, 'Thomasina Tinkham': {'marks': [25.0, 78.0, 46.0, 46.0, 90.0]},
								'Adolphus Biernat': {'marks': [91.0, 96.0, 98.0, 94.0, 100.0]}, 'Rex Aspinell': {'marks': [34.0, 75.0, 51.0, 38.0, 99.0]}
							}
	>>> print( generateGradeCard( name_marks_mapping ) )
	{
		'Artus Syne': {'subject_wise_marks': [43.0, 71.0, 55.0, 16.0, 51.0], 'grade_received': 'D'},
		'Evey Reburn': {'subject_wise_marks': [49.0, 7.0, 53.0, 50.0, 63.0], 'grade_received': 'D'},
		'Giff Wickmann': {'subject_wise_marks': [63.0, 37.0, 21.0, 87.0, 9.0], 'grade_received': 'D'},
		'Garrot Casetta': {'subject_wise_marks': [22.0, 3.0, 91.0, 75.0, 52.0], 'grade_received': 'D'},
		'Roselle Maes': {'subject_wise_marks': [71.0, 90.0, 96.0, 79.0, 48.0], 'grade_received': 'A'},
		'Torin Ziehms': {'subject_wise_marks': [71.0, 31.0, 83.0, 1.0, 25.0], 'grade_received': 'D'},
		'Jaye Etock': {'subject_wise_marks': [92.0, 9.0, 2.0, 78.0, 55.0], 'grade_received': 'D'},
		'Thomasina Tinkham': {'subject_wise_marks': [25.0, 78.0, 46.0, 46.0, 90.0], 'grade_received': 'C'},
		'Adolphus Biernat': {'subject_wise_marks': [91.0, 96.0, 98.0, 94.0, 100.0], 'grade_received': 'O'},
		'Rex Aspinell': {'subject_wise_marks': [34.0, 75.0, 51.0, 38.0, 99.0], 'grade_received': 'C'}
	}
	"""

	grade_card = mapping_dict

	##############	ADD YOUR CODE HERE	##############
	gradelist = []
	per = 0;
	for name in grade_card:
	    for num in grade_card[name]["marks"]:
	        per += int(num);
	    per = per/5;
	    #print(per*5)
	    if per >= 90:
	        gradelist.append("O")
	    elif per >= 70:
	        gradelist.append("A")
	    elif per >= 60:
	        gradelist.append("B")
	    elif per >= 50:
	        gradelist.append("C")
	    elif per >= 40:
	        gradelist.append("D")
	    else:
	        gradelist.append("FAIL")
	    per = 0;
	print(gradelist)
	new_k = "subject_wise_marks"
	old_k = "marks"
	for name in grade_card:
		grade_card[name][new_k] =  grade_card[name].pop(old_k)
	i = 0;
	for name in grade_card:
	    grade_card[name]["grade_received"] = gradelist[i]
	    i+=1


	##################################################

	return grade_card


if __name__ == "__main__":
	"""Main function, code begins here.
	"""
	csv_file_name = 'task1_sample.csv'
	name_marks_mapping = readMarkSheet(csv_file_name)
	print(name_marks_mapping)
	grade_card = generateGradeCard(name_marks_mapping)
	print(grade_card)
