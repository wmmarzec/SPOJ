import sys

def is_number(i):
	try:
		int(i)
		return True
	except ValueError:
		return False
try:
    for lines in sys.stdin:
        line = lines.split()
        numbers = 0
        words = 0
        for i in range (0, len(line)):
            if is_number(line[i]):
                numbers+=1
            else:
                words+=1
        print (numbers, words)

except:
      sys.exit(0)