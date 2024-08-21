class Dept:
    def __init__(self):
        self.dept = {
            "hr": "Human resource",
            "acc": "accounts and finance",
            "sd": "sales and distribution",
            "mft": "manufacturing department"
        }

    def __call__(self,dept):
        return self.dept[dept]


def Depts():
    depts = {
        "hr": "Human resource",
        "acc": "accounts and finance",
        "sd": "sales and distribution",
        "mft": "manufacturing department"
    }

    def dname(dept):
        return depts[dept]

    return dname


d = Depts()
print(d.__call__("hr"))
s = d("hr")
print(s)