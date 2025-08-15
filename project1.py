3
student={}
n=int(input("enter a number of students"))
for i in range(n):
    print("\n enter details for students")
    name=(input("name"))
    age=int(input("age"))
    english=int(input("english marks"))
    maths=int(input("maths marks"))
    science=int(input("science marks"))
    hindi=int(input("hindi marks"))
    student[name]={
        "age":age,
        "english":english,
        "maths":maths,
        "science":science,
        "hindi":hindi
    }
while True:
    print("\n menu")
    print("1.view student report")
    print("2.view all students")
    print("3.exit")
    choice=input("enter your choice(1:search student,2:all student,3:exit)")

    if choice=="1":
        search_name=input("enter student name to view report:")
        if search_name in student:
            data=student[search_name]
            print("\n report card")
            print("name:",search_name)
            print("age:",data["age"])
            print("english:",data["english"])
            print("maths:",data["maths"])
            print("science:",data["science"])
            print("hindi:",data["hindi"])
            avg=(data["english"]+data["maths"]+data["science"]+data["hindi"])/4
            print("average:",round(avg,2))
        else:
            print("student not found")
    elif choice=="2":
        print("all student:")
        for name,data in student.items():
            print(f"{name}-age:{data['age']},english:{data['english']},maths:{data['maths']},science:{data['science']},hindi:{data['hindi']}")
            avg=(data["english"]+data["maths"]+data["science"]+data["hindi"])/4
            print("average:",round(avg,2))   

    elif choice=="3":
        print("exit program")
        break
    else:
        print("invalid choice")        



 