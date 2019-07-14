#!/usr/bin/env python3
# An insecure password locker program.

import sys
import pyperclip
import re

from generate_pass import generate_password

password = {
    'Gmail': 'fjy5gjkj',
    'Facebook': 'mek8hxxhhgr',
	'Upwork': 'shhdddd',
	'JetBrain':'2dgg3477989yh',
    'wisdomjobsgulf':'Xchhg2kds5'
}

if len(sys.argv) < 2:
    print("""
                 +-+
    =============| |
                `:_;'

    Usage: python main.py [account] - copy account password
    To generate password: python main.py -g [length of the password]
    """)
    sys.exit()

# Using following insturction you need to type file name and account name with space b/w them.
if sys.argv[1] == '-g':
    if len(sys.argv) < 3:
        print("""
        Please specify the password length.
        python main.py -g [length of the password]
        """)
    else:
        print(generate_password(int(sys.argv[2])))

else:
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
        if (len(sletter) == 0):
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