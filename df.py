import commands

result = commands.getoutput('df -k').split('\n')

for line in result[1:]:
	temp = line.split()
	usage = temp[4][:-1]
	print(usage)
	if usage > 60:
		print(usage)
	else:
		pass