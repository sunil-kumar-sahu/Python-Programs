import json
"""
d={
    'course_name':'Python',
    'fees':'15000'
}
f=json.dumps(d)
print(f)
"""
#Converting Json to Python Objects
"""
d='{"cname":"Python","fees":12000,"duration":"2 months"}'
x=json.loads(d)
print(type(x))
print(x)
for a in x:
    print(a,x[a])
"""
#Writing and Reading JSON File
file=open("posts.json","r")
x=file.read()
finaldata=json.loads(x)
for a in finaldata:
    print(a['name'],a['job'])

