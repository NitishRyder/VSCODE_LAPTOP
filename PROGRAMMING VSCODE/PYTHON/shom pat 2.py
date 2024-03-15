movetolast = lambda l, e: [x for x in l if x != e] + [e] + [e] 

a = ['a', 'v', 'a', 'i', 't']
print(movetolast(a, 'a'))
