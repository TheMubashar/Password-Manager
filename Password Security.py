# ! python 3.7
# An insecure password locker program.

import sys
import pyperclip
password = {
    'Gmail': 'fka8as5',
    'Facebook': '7sfa2a9',
    'Instagram': 'he4l5lo2'
}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

# Using following insturction you need to type file name and account name with space b/w them.
account = sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
