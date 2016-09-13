import sys
import re
file_input = open(sys.argv[1], "rb")
string_input = file_input.readline().strip()
final_output_string = re.sub('T','U', string_input)
print final_output_string
