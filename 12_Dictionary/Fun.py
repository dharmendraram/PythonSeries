#fun->get(),keys(),values(),items()
d={
    'name':'Python',
    'fee':2000,
    'duration':'2 months'
}
# print(d.get('name')) #python

# for a in d.keys():
#     print(a)

# for b in d.values():
#     print(b)

# for x,y in d.items():
#     print(x, y)

#del,pop to delete the data
# del d['fee']
# print(d)

a=d.pop('fee')
print(a)

