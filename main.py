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

def a():
	sprint('You go to Walmart for some shopping')
	print('|||SHOPPING LIST|||')
	print('pringles')
	print('rubber gloves')
	print('bread')
	print('soap')
	print('milk')
	print('lotion')
	print('paper towels')
	sleep(1)
	print('1: Buy all')
	print('2: Buy one at a time')
	if a == '1':
		sleep(1)
		sprint('you bought all your groceries')
	if a == '2':
		sleep(1)
		sprint('you buy all your groceries but at one at a time. The people of Dallas TX accuse you of being a witch for choosing such an option in a game where you can buy all at once.')
		sleep(1)
		die()
