import math

def binary_to_String(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m

def string_to_binary(a_binary_string):
    l,m=[],[]
    for i in a_binary_string:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m


# print('Enter your plain Text:')
# pt = input()
# pt = string_to_binary(pt)
# print('plain text (binary), ',pt)
# pt = binary_to_String(pt)
# print('plain text (string), ',pt)

# print('Enter your key:')
# k = input()
# k = string_to_binary(k)
# print('plain text, ' + k)
