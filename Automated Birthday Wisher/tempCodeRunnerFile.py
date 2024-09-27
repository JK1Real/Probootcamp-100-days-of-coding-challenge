    pattern =re.compile(r'\[Name\]')
    new_data = re.sub(pattern,"hello",data,count=1)
    print(new_data)