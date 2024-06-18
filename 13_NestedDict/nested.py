course={
    'php':{'duration':'2 months','fee':2000},
    'python':{'duration':'3 months','fee':30000},
    'java':{'duration':'1 month','fee':200}
}
# print(course)
# print(course['php']['fee']) #2000

course['java']['fee']=230202
print(course)

for k,v in course.items():
    print(k,v['duration'])