userName = input('Enter username')
passWord  = input('Enter password')
codedPass = '*' * passWord.len()
print(f'Hi {userName}, your password {codedPass} is {passWord.len()} long' )