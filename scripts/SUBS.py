string = raw_input().strip()
import re
substr = raw_input().strip()
print ' '.join([str(i.start()+1) for i in re.finditer('(?='+substr+')', string)])
