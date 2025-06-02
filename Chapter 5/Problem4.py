# What will be the length of following set s
s = set()
s.add(14)
s.add(14.0)
s.add('14') # length of s after these operations?

#print(s)  #Treats 14 (int) and 14.0 (float) as same
print(len(s))