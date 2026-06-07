# object
# class
# attribute
# method


class results:
    def __init__(self,student, marks):
        self.student= student
        self.marks= marks
# mantiq =results("",100)
# masael =results("",98)
# qatar= results("",99)
# print (qatar.student,qatar.marks)
# print (masael.student,masael.marks)
# print (mantiq.student ,":",mantiq.marks)


class finals (results):
    def __init__(self, student, marks,finalMarks):
        super().__init__(student, marks)
        self.finalMarks= finalMarks
    def show(self):
        print ("your final mark is")
        print(self.finalMarks)
meow= finals("taqi",55,33)
meow.show()