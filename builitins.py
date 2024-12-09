name_length = len(given_name)
if name_length == 1:
    put_success(f'Strange name with length {name_length}')
elif name_length > 50:
    put_success(f'your name contains more 50 symbols {name_length}')
elif name_length > 20:
    put_success(f'your name contains more 20 symbols {name_length}')
elif name_length < 5:
    put_success(f'your name contains less than 5 symbols {name_length}')
else:
    put_success(f'Name with length {name_length}')