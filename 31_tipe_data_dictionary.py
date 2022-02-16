# List = [1,2,3,4]
# Tuple = (1,2,3,4) 
# Set = {1,2,3,4}

# print(type(List))
# print(type(Tuple))
# print(type(Set))


#  dictionary
# dictionary = {key:value, key:value}

member1 = {"ID":101,
            "Nama":"Muhammad Ayyub Ramli",
            "Pekerjaan":"Backend Developer",
            "Umur":19
            }

member2 = {"ID":101,
            "Nama":"Gugun",
            "Pekerjaan":"MC",
            "Umur":22
            }

memberlist = {101:member1, 102:member2}

print(member1)
print(member1["ID"])
print(member1.keys())
print(member1.values())

print(memberlist[101])