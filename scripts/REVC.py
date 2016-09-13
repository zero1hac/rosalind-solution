import sys
file_input = open(sys.argv[1], "rb")
string_input = file_input.readline().strip()
final_output_string = ''
for i in string_input[::-1]:
    if i == 'C':
        final_output_string+='G'
    if i == 'G':
        final_output_string+='C'
    if i == 'T':
        final_output_string+='A'
    if i == 'A':
        final_output_string+='T'
print final_output_string
