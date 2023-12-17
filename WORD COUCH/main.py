'''
question

we need a file to create list of question(5)

we need the input the ans of questions(5)

there shoudl be 2 variables 
1.correct ans 
2.wrong and

finally the ans we are answering will add to correct and worng accordingly and return us back how much ans was correct and how much was wrong 
'''

from questions import Animal, Bird, Laptop, Mouse, Keyboard 
correct_ans = 0
wrong_ans = 0 

class main:
  def answers(self):
    self.question1 = Animal()
    self.user_input = input("write your ans here: ")
    self.question1 = Bird()
    self.user_input2 = input("write your ans here: ")
    self.question1 = Laptop()
    self.user_input3 = input("write your ans here: ")
    self.question1 = Mouse()
    self.user_input4 = input("write your ans here: ")
    self.question1 = Keyboard()
    self.user_input5 = input("write your ans here: ")

  def animal(self):
      global correct_ans
      global wrong_ans
      if self.user_input == 'tiger':
         correct_ans+=1   
      else:
         wrong_ans+=1
         print("Wrong answer. The correct ans is tiger")
        
  def birds(self):
      global correct_ans
      global wrong_ans
      if self.user_input2 == 'peacock':
         correct_ans+=1   
      else:
         wrong_ans+=1     
         print("Wrong answer. The correct ans is peacock")

  def laptop(self):
      global correct_ans
      global wrong_ans
      if self.user_input3 == 'msi':
         correct_ans+=1   
      else:
         wrong_ans+=1     
         print("Wrong answer. The correct ans is msi")

  def mouse(self):
      global correct_ans
      global wrong_ans
      if self.user_input4 == 'logitech':
         correct_ans+=1   
      else:
         wrong_ans+=1     
         print("Wrong answer. The correct ans is logitech")

  def keyboard(self):
      global correct_ans
      global wrong_ans
      if self.user_input5 == 'keychron':
         correct_ans+=1   
      else:
         wrong_ans+=1     
         print("Wrong answer. The correct ans is keychron")
         
obj = main()
obj.answers()
obj.animal()    
obj.birds()
obj.laptop()
obj.mouse()
obj.keyboard()

print(f'\nCorrect answer: {correct_ans}    Wrong answer:{wrong_ans}')

if correct_ans == 5:
   print('\nCongragulation you scored 5/5.')
elif correct_ans >=3 and correct_ans <5:
   print(f'\nyou scored {correct_ans}/5. Better luck next time.')
else:
   print(f'\nyou scored {correct_ans}/5. Try more harder next time.')
    

  
