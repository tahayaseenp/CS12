import csv
def CREATE():
       f=open("Emp.csv","a",newline="")      
       obj=csv.writer(f)
       L=[]
       while True:
              eno = input("Enter employee number:")
              ename = input("Enter employee name:")
              edep = input("Enter employee department:")
              ebasic = input("Enter employee basic:")
              hra = input("Enter employee hra?:")
              sal = input("Enter employee salary:")
              L.append([eno,ename,edep,ebasic,hra,sal])
              ch=input("do you?")
              if ch.lower()!='y':
                    break
       obj.writerows(L)
       f.close()

CREATE()