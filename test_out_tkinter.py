import nigga
global cor
cor = 0
def fq():
   print(nigga.read)
   x = input()
   if x == nigga.read1:
      print("Правильно")
   else:
      print("Неправильно")
   check()
def check():
   if fq() == "Правильно":
      cor = 1
   else:
      exit(0)

def sq():
   print(nigga.read2)
   y = input()
   if y == "":
      print("Правильно")
   else:
      print("Неправильно")
def mark():
   if cor > 4:
      print("Оценка 5")
   elif cor == 4:
      print("Оценка 4")
   elif cor == 3:
      print("Оценка 3")
   else:
      print("Оценка 2")
fq()