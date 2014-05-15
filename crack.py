import subprocess
import sys
import re

startLength = 1
maxPasswordLength = 8
matchRE = re.compile('^\w{32}\:.*$')

emailProviders = [
	"gmail.com",
	"aol.com",
	"yahoo.com",
	"hotmail.com",
]

for i in range(startLength,maxPasswordLength+1):
	for email in emailProviders:
		email = "@" + email
		maskPattern = "?l" * i

		mask = maskPattern + email
		print "Cracking length %s using mask %s" % (i,mask)

		commandLine = [
					'/tmp/hashcat-0.47/hashcat-cli64.app',
					'-m',
					'0',
					'-a',
					'3',
					'--quiet',
					'--pw-min=%d' % (i + len(email)),
					'/tmp/hash.txt',
					str(mask)
				]

		proc = subprocess.Popen(commandLine, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		#print "Ran %s" % " ".join(commandLine)
		
		for line in iter(proc.stdout.readline, ""):
		    if matchRE.match(line):
		    	print "Hash found! %s" % line
		    	sys.exit(0)
		    elif line.startswith('Progress') or line.startswith('Estimated'):
		    	print line,