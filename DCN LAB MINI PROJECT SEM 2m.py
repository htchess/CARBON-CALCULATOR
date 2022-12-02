from tkinter import*

import tkinter as tk
from tkinter import RIDGE
from tkinter import messagebox
import mysql.connector as connector

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:999Htiw@rid@localhost/pythontest")

root=tk.Tk()
root.title("SAVE CARBON EMMISSION SAVE PLANET")
root.geometry("500x500+0+0")


############################################################################################################################
##################################################### carbon emitted by food    ############################################
# class DBHelper: 
#      def __init__(self) :
#          self.con=connector.connect(host='localhost',port='3306',user ='root',password='999Htiw@ri',database='pythontest')
#          query='create table if not exists carbon_dta(diet varchar(100) ,carbon_E  int)'
#          cur = self.con.cursor()
#          cur.execute(query)
#          print("Created")
#      def insert_carbon_diet_data(self,Diet,Carbon_E):
#          query= "insert into carbon_dta(diet,carbon_E ) values('{}',{})".format(Diet,Carbon_E)
#          print(query)
#          cur=self.con.cursor()
#          cur.execute(query)
#          self.con.commit()
#          print("carbon_diet_data save to db")
#      def save_data(self,Diet):
#          query= "insert into carbon_dta(diet) values('{}')".format(Diet)
#          print(query)
#          cur=self.con.cursor()
#          cur.execute(query)
#          self.con.commit()
#          print("carbon_diet_data save to db")
          
        
# helper=DBHelper()    

# helper.insert_carbon_diet_data('vegan',7)
# helper.insert_carbon_diet_data('vegetarian',4)
# helper.insert_carbon_diet_data('fish-eater',4)
# helper.insert_carbon_diet_data('low-meat eater',5)
# helper.insert_carbon_diet_data('medium meat eater',6)
# helper.insert_carbon_diet_data('high meat eater',7)

############################################################################### carbon emmited by cloth##################
# class DBHelper: 
#      def __init__(self) :
#          self.con=connector.connect(host='localhost',port='3306',user ='root',password='999Htiw@ri',database='pythontest')
#          query='create table if not exists carbon_dta2(diet varchar(100),cloth_type varchar(100) ,carbon_E  int)'
#          cur = self.con.cursor()
#          cur.execute(query)
#          print("Created")
#      def insert_carbon_cloth_data(self,cloth,Carbon_E):
#          query= "insert into carbon_dta2(cloth_type,carbon_E ) values('{}',{})".format(cloth,Carbon_E)
#          print(query)
#          cur=self.con.cursor()
#          cur.execute(query)
#          self.con.commit()
#          print("carbon_cloth_data save to db")
#      def save_data(self,cloth,diet,carbon_E):
#          query= "insert into carbon_dta2(diet,cloth_type,carbon_E) values('{}','{}','{}')".format(cloth,diet,carbon_E)
#          print(query)
#          cur=self.con.cursor()
#          cur.execute(query)
#          self.con.commit()
#          print("carbon_cloth_data save to db")
     
##############################################
############################################################################### carbon emmited by cloth##################
class DBHelper: 
     def __init__(self) :
         self.con=connector.connect(host='localhost',port='3306',user ='root',password='999Htiw@ri',database='pythontest')
         query='create table if not exists carbon_dta4(diet varchar(100),cloth_type varchar(100) ,carbon_E  int,name varchar(100),total_carbon_E float,total_plants int)'
         cur = self.con.cursor()
         cur.execute(query)
         print("Created")
     def insert_carbon_cloth_data(self,cloth,Carbon_E):
         query= "insert into carbon_dta4(cloth_type,carbon_E ) values('{}',{})".format(cloth,Carbon_E)
         print(query)
         cur=self.con.cursor()
         cur.execute(query)
         self.con.commit()
         print("carbon_cloth_data save to db")
     def save_data(self,cloth,diet,carbon_E,name,total_carb,total_plant):
         query= "insert into carbon_dta4(diet,cloth_type,carbon_E,name,total_carbon_E,total_plants) values('{}','{}','{}','{}','{}','{}')".format(cloth,diet,carbon_E,name,total_carb,total_plant)
         print(query)
         cur=self.con.cursor()
         cur.execute(query)
         self.con.commit()
         print("carbon_cloth_data save to db")
     def get_data(self,name):
         query="select * from carbon_dta4 where name = '{}'".format(name)
         print(query)
         cur=self.con.cursor()
         cur.execute(query)
         result = cur.fetchmany(size =1)
         print(result[0][2])
         show_all(result=result[0])
         self.con.commit()
         print("retrieve carbon data from db")


        
helper=DBHelper()    

# helper.insert_carbon_cloth_data('cotton',8)
# helper.insert_carbon_cloth_data('Nylon',5)
# helper.insert_carbon_cloth_data('PET',6)
# helper.insert_carbon_cloth_data('wool',5)
dict1=[{'cotton':8,'Nylon':5,'PET':6,'wool':5}]
dict2=[{'vegan':3,'vegetarian':4,'fish-eater':34,'low meat-eater':5,'medium meat-eater':6,'high meat-eater':7}]
str(dict1)
str(dict2)
for dicts in dict1:
    for keys in dicts:
        dicts[keys]=int(dicts[keys])
for dicts in dict2:
    for keys in dicts:
        dicts[keys]=int(dicts[keys])

#####################################################################################

######################################################################################
lbl1=tk.Label(root,text="CARBON EMMISSION CALCULATOR ",font=('',45,'bold'),fg='green',bd=5,relief=RIDGE)
lbl1.pack()


lbl1=tk.Label(root,text="NAME :",font=('Algerian',15,'bold'))
lbl1.place(x=540,y=100)

lbl1=tk.Label(root,text="CARBON EMITTED BY FOOD(IN KG) :",font=('Algerian',15,'bold'))
lbl1.place(x=155,y=200)

lbl1=tk.Label(root,text="CARBON EMITTED BY CLOTHS(IN KG) :",font=('Algerian',15,'bold'))
lbl1.place(x=129,y=250)

lbl1=tk.Label(root,text="DISTENCE TRAVEL BY CAR IN KM(PER DAY) :",font=('Algerian',15,'bold'))
lbl1.place(x=118,y=300)

lbl1=tk.Label(root,text="TOTAL CARBON EMISSION(IN KG) :",font=('Algerian',15,'bold'))
lbl1.place(x=168,y=350)

lbl1=tk.Label(root,text="NUMBER OF TREE PLANTED :",font=('Algerian',20,'bold'))
lbl1.place(x=140,y=400)

lbl1=tk.Label(root,text="OR",font=('Algerian',20,'bold'))
lbl1.place(x=550,y=450)

lbl1=tk.Label(root,text="IF DATA ENTERED BEFORE WRITE YOUR NAME :",font=('Algerian',15,'bold'))
lbl1.place(x=140,y=500)
#################################################################################################################

#################################################################################################################
menu= StringVar()
menu.set("Select Any Diet")
drop= tk.OptionMenu(root, menu,"vegan", "vegetarian","fish-eater","low meat-eater","medium meat-eater","high meat-eater")
drop.place(x=600,y=200)


print(menu.get())
def add_data():
    my_class=menu.get()
    helper.save_data(my_class) # insert data

#######################################################################################
menu2= StringVar()
menu2.set("Select Cloth Type")
drop1= tk.OptionMenu(root, menu2,"cotton", "Nylon","PET","wool")
drop1.place(x=600,y=250)




#######################################################################################   entry box1 CAR DATA ##################
# def get_data():
#    label.config(text= entry.get(), font= ('arial'))
entry = Entry(root, width= 10)
entry.place(relx= .5, rely= .45, anchor= CENTER)

entry2 = Entry(root, width= 40)
entry2.place(relx= .55, rely= .1555, anchor= CENTER)

entry5 = Entry(root, width= 40, )
entry5.place(relx= .55, rely= .73, anchor= CENTER)


b3=tk.Button(root, text= "Add Data", command= lambda: add_data2()).place(relx= .61, rely= .45, anchor= CENTER)
res=0
def add_data2():
    my_class=entry.get()
    my_class1=menu2.get()
    my_class3=menu.get()
    my_class4=entry2.get()
    x1=(dict2[0].get(my_class3))
    x2=(dict1[0].get(my_class1))
    print(my_class)
    x3=float(my_class)
    res=x1+x2+(0.12*x3)
    print(res)
    helper.save_data(my_class3,my_class1,my_class,my_class4,res,int(res*3.3)) # insert data
    
    
   
    show_answer(res)
    show_answer2(res)
    
    
def show_answer(res):
    label=Label(root, text=res, font=('Calibri 15'))
    
    label.place(x=650,y=350)
   
def show_answer2(res):
    label=Label(root, text=int(res*3.3), font=('Calibri 15'))
    label.place(x=650,y=400)

  ######################################################################################  entry box 2 NAME DATA 1 ############
# def get_data1(res):
#    label.config(text= res, font= ('arial'))

# tk.Button(root, text= "Add Data", command= get_data1).place(relx= .65, rely= .1555, anchor= CENTER)
    

#######################################################################################   entry box 5 NAME DATA 2 ################## 
def get_data5():
   name=entry5.get()
   helper.get_data(name=name)

tk.Button(root, text= "Get Data", command= get_data5).place(relx= .65, rely= .73, anchor= CENTER)

##############################################################
def show_all(result):
    label=Label(root, text=result[3], font=('arial'))
    label.place(x=100,y=600)
    label1=Label(root, text=result[0], font=('arial'))
    label1.place(x=200,y=600)
    label2=Label(root, text=result[1], font=('arial'))
    label2.place(x=400,y=600)
    label3=Label(root, text=result[2], font=('arial'))
    label3.place(x=500,y=600)
    label4=Label(root, text=result[4], font=('arial'))
    label4.place(x=600,y=600)
    label5=Label(root, text=result[5], font=('arial'))
    label5.place(x=700,y=600)

      


root.mainloop()
