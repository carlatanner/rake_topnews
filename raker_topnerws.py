


import rake
import operator
from time import mktime

def init_archivo( ):
	archivo_salida= "ik1.sql"
	try:
	
		#modo  w de escritura b binario 
		output_file=open (archivo_salida, "wb")	
	except:
		output_file = -1
	return output_file
def insert_keys(keyword, output_file):
	sql = """INSERT INTO bignews.keycount( keyword, count) 
			VALUES ('"""
	output_file.write(sql)
	output_file.write(keyword[0])
	output_file.write("', ")
	output_file.write(str(keyw[1]))
	output_file.write(""" );""")
	output_file.write("\n")
	
	
	# EXAMPLE ONE - SIMPLE
stoppath = "stopwordsspanish.txt"

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath, 5, 3, 4)

# 2. run on RAKE on a given text
sample_file = open("../../text/titles.txt", 'r')
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print "Keywords:", keywords
output_ins = init_archivo()

for keyw in keywords:
	insert_keys(keyw, output_ins)

output_ins.close()		

###################################################################
exit()

