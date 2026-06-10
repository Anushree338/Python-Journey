#what will be the length of following set s

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after this operation = 2 because python takes 1==1.0 as a same number

print(len(s))