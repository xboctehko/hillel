s = "barmaley"
dict = {}
for letter in s:
 if letter not in dict.keys():
  dict[letter] = 1
 else:
  dict[letter] += 1

print (dict)	
