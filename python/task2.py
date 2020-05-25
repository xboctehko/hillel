s = ' ненормальную'
morph = ''.join([e.upper() if i%2==0 else e for i, e in enumerate(s)])
print(morph)
