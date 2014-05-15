import subprocess
import sys
import re

startLength = 1
maxPasswordLength = 10
matchRE = re.compile('.*(\w{32}\:\S+@.*)$',re.MULTILINE)

hashcatBin = "C:\\temp\\hashcat\\oclHashcat-1.20\\oclHashcat64.exe"

emailProviders = [
	"gmail.com",
#	"aol.com",
#	"yahoo.com",
#	"hotmail.com",
]

for i in range(startLength,maxPasswordLength+1):
	for email in emailProviders:
		email = "@" + email
		maskPattern = "?1" * i

		mask = maskPattern + email
		print "\n\nCracking length %s using mask %s" % (i,mask)

		commandLine = [
					hashcatBin,
					'-m',
					'0',
					'-a',
					'3',
					'--status-timer=5',
					'-o',
					'/tmp/crackatar.pot'
					'-1',
					'?l?u?d_.',
		  			'hash.txt',
					str(mask)
				]
		proc = subprocess.Popen(commandLine, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print "Ran %s\n\n" % " ".join(commandLine)
		
		for line in iter(proc.stdout.readline, ""):
			if matchRE.match(line):
				print "\n\n==============="
				print "Hash found! %s" % matchRE.match(line).groups()[0]
				print "==============="
				sys.exit(0)
			else:
				print line,

		import time
		#time.sleep(1)
