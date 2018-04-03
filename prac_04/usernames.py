"""
Checks whether user is in Username
"""

user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Please Enter User Name : >> ")
if user_input in user_names:
    print("Access Granted")
else:
    print("Access Denied")