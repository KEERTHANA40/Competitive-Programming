def find(s1, s2):
     
    if(sorted(s1.lower().replace(" ",""))== sorted(s2.lower().replace(" ",""))):
        print("True") 
    else:
        print("False")       


find("anagram","nagaram")           
find("Keep","Peek")
find("Mother In Law","Hitler Woman")
find("School Master","The Classroom")
find("ASTRONOMERS","NO MORE STARS")
find("Toss","Shot")
find("joy","enjoy")
find("Debit Card","Bad Credit")
find("SiLeNt CAT","LisTen AcT")
find("Dormitory","Dirty Room")  
         