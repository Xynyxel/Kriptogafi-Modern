def string_to_binary(a_binary_string):
    l,m=[],[]
    for i in a_binary_string:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m