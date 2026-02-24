#7. write a programme that stores 3 students details in a dictionary and list of their marks and average marks

students = {"sathwik":[55,66,78],"reddy":[44,55,22],"komala":[55,33,90]}
s1 =round(sum(students["sathwik"])/3,2)
s2 = round(sum(students["reddy"])/3,2)
s3 = round(sum(students["komala"])/3,2)
s1,s2,s3
print("name: sathwik\n""marks uptained: ",students["sathwik"],"\nAverage:", s1)

print("\nname: reddy\n""marks uptained: ",students["reddy"],"\nAverage:", s2)

print("\nname: komala\n""marks uptained: ",students["komala"],"\nAverage:", s3)
