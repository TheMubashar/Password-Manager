# ! python 3.7
# An insecure password locker program.

import sys
import pyperclip
import re

password = {
    'Gmail': 'Firefighter125',
    'Facebook': 'Omer125',
	'Upwork': 'S825ajkfa2',
	'JetBrain':'Hx2539yh',
    'wisdomjobsgulf':'X8cskds5'
}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

# Using following insturction you need to type file name and account name with space b/w them.
account = sys.argv[1]

        
if account in password:
    pyperclip.copy(password[account])
    print('Password for ' + account + ' copied to clipboard.\n')
    account=pyperclip.paste()
    SmallLetterRegex = re.compile(r'[a-z]')
    sletter = SmallLetterRegex.findall(account)

    CapitalLetterRegex = re.compile(r'[A-Z]')
    cletter=CapitalLetterRegex.findall(account)

    NumberRegex = re.compile(r'\d+')
    number = NumberRegex.findall(account)

    LengthRegex= re.compile(r'[a-zA-Z0-9]{8}')
    length = LengthRegex.findall(account)

    errors=[]
    if (len(sletter) == 0 ):
        errors.append('Add-a-small-letter')
    if (len(cletter) == 0):
        errors.append('Add-a-capital-letter')
    if (len(number) == 0):
        errors.append('Add-a-number')
    if (len(length) == 0):
        errors.append('Password-length-is-short')
        
    if (len(errors) != 0):
        print('Please make following changes in your password:')
        for error in errors:
            print(error)
    else:
        print('Your password is strong')

else:
    print('There is no account named ' + account)

close=input('\nPress enter to close it:')