class student:
    def get_data(self):
        self.roll_no=input("enter the roll_no")
        self.student_name=input("enter the name")
    def out_data(self):
     return(self.roll_no,self.student_name)
class marks:
   def __init__(self):
      self.marks=[]
   def get_mark(self):
      for _ in range(6):
         mark=input("enter the six subjects marks")
         self.marks.append(mark)
   def total_mark(self):
      total=self.marks.sum()
      print(total)
   
      
     
obj1 = student()
obj1.get_data()
obj2=marks()
obj2.get_mark()
print(obj1.out_data() )
print(obj2.total_mark)
