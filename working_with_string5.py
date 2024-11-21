



import messages

firstname = "Alex"
# print(id(firstname))
lastname = "Obama"

# firstname = "Mr " + firstname
# print(id(firstname))
fullname = firstname + " " + lastname
welcome_message = "Welcome, Mr." + " "+ fullname

alternative_welcome_message = f'Welcome, Mr. {fullname}!'
print(alternative_welcome_message)
alternative_welcome_message2 = messages.MSG_WELCOME_MISTER.format(name='George', other='Other data')
print(alternative_welcome_message2)

# v

print (welcome_message)

reverted_fullname = lastname + firstname



print (fullname)
print(reverted_fullname)

print(firstname, lastname, lastname, fullname)


multy_lines1 = ('vhbs'
                ' ufvo'
                ' uwb '
                'revb')
print(multy_lines1)

multy_lines2 = 'vhbfdvaou rrgqer rgegrae ra\n\nrag '

print(multy_lines2)

multy_lines3 = """
dgag
garg
gfag
gag

"""
print(multy_lines3)



