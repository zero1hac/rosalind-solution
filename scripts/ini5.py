import sys
file1 = sys.argv[1]
opened_file = open(file1,"rb")
list_lines = opened_file.readlines()
modified_list_lines = [list_lines[i-1] if i%2 == 0 else '' for i in range(1,len(list_lines)+1)]
output_text = ''.join(modified_list_lines)
outputfile = open("output_ini5.txt","wb")
outputfile.write(output_text)
outputfile.close()
opened_file.close()
