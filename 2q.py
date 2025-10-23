class Employee:
    def __init__(s,name,EmpID):
        s.name = name
        s.EmpID = EmpID
    def show(s):
        print("name is",s.name)
        print("EmpID is",s.EmpID)
class Skill:
    def __init__(s,programming_language):
        s.programming_language = programming_language
    def show(s):
        print("programming_language is",s.programming_language)
class Developer(Employee,Skill):
    def __init__(s,name,EmpID,programming_language):
        Employee.__init__(s,name,EmpID)
        Skill.__init__(s,programming_language)
    def show(s):
         print("name is",s.name)
         print("EmpID is",s.EmpID)
         print("programming_language is",s.programming_language)
        
obj = Developer("Sandeep",101,"Python")
obj.show()
