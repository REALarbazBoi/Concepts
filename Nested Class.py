class customer:

    def __init__(self, id, name, bdno, bstreet, bcity, bcountry, bpin, sdno, sstreet, scity, scountry, spin):
        self.custid = id
        self.name = name
        self.baddrd = self.Address(bdno, bstreet, bcity, bcountry, bpin) #address is an inner class
        self.saddr = self.Address(sdno, sstreet, scity, scountry, spin)

    class Address:

        def __init__(self, dno, street, city, country, pin):
            self.dno = dno
            self.street = street
            self.city = city
            self.country = country
            self.pin = pin

        def display(self):
            print(self.dno)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)

c = customer(10, "John", 100, "abc", "Mumbai", "India", 400043, 200, "Vikesh", "Delhi", "India", 110024)

c.baddrd.display()
c.saddr.display()