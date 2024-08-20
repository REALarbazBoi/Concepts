import Student, pickle # type: ignore

studs = [Student.Student(10,"John","cs"), Student.Student(20,"Ajay","EC"), Student.Student(30,"Khan","ME")]

with open("students.data", "wb") as f:
    for s in studs:
        pickle.dump(s,f)