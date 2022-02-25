from termcolor import colored
import sys
import time
import os



def c():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)



def sprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)


def die():
	sprint(colored('You kicked the bucket', 'red'))
	return start

	print('''

               
                                 
		                         
		     _______________________
        |                       |
	      | 	                    |
		     \                     /
		      \                   /
		       \                 /
		        \               /
		         \             /
		          \___________/''')
