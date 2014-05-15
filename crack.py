import subprocess
import sys

passwordLength = 8

emailProviders = [
	"aol.com",
	"gmail.com",
	"yahoo.com",
	"baidu.com",
	"hotmail.com",
	"yahoo.com",
]

for i in range(1,passwordLength + 1):
	for email in emailProviders:
		maskPattern = "?l" * i

		mask = "%s@%s" % (maskPattern, email)
		print "Cracking length %s using mask %s" % (i,mask)

		#import ipdb; ipdb.set_trace()

		  #--pw-min=10 /tmp/hash.txt ?l?l?l?l?l?lp@gmail.com --quiet
		proc = subprocess.Popen([
					'/tmp/hashcat-0.47/hashcat-cli64.app',
					'-m',
					'0',
					'-a',
					'3',
					'--quiet',
					'--pw-min=%d' % ((len(maskPattern) / 2) + len("@" + email)),
					'/tmp/hash.txt',
					'"' + mask +'"'
				], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print "Ran %s" % " ".join([
					'/tmp/hashcat-0.47/hashcat-cli64.app',
					'-m',
					'0',
					'-a',
					'3',
					'--quiet',
					'--pw-min=%d' % ((len(maskPattern) / 2) + len("@" + email)),
					'/tmp/hash.txt',
					'"' + mask +'"'
				])

		(out, err) = proc.communicate()
		if len(out) > 1:
			print out
			sys.exit(0)