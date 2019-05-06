from teacher import *
s=student()
s.set_details(124,"prasad","tirupati")
s1=s.get_details()
for x in s1:
    print(x)
t=teacher()
t.set_student_details(125)
t1=t.get_student_details()
print(t1)
# for x in t1:
#     print(x)
