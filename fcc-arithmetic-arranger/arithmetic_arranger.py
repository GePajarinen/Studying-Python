def arithmetic_arranger(problems, withAnswer = False):
    
  if len(problems) >5:
    print("Error: Too many problems.")

  line1= []
  line2=[]
  line3=[]
  line4= []

  for i, prob in enumerate(problems):
    op1, sign, op2 = prob.split(" ")

    #Situations that will return an error:
    if sign != '+' and sign != '-' :
      print("Error: Operator must be '+' or '-'.")
    
    else:
      if sign == '+':
        answ = str(int(op1) + int(op2))
      elif sign == '-':
        answ = str(int(op1) - int(op2))

    if len(op1) > 4 or len(op2) > 4:
      print("Error: Numbers cannot be more than four digits.")

    if not op1.isdigit() or not op2.isdigit():
      print("Error: Numbers must only contain digits.")


    if op1 > op2:
      part1= (" "*2)+ op1
      part2= sign+(' '* (len(part1)-1-len(op2)))+op2
      part3 = "-" * int(len(part1))
      part4 = " " * (len(part3)-len(answ)) + answ

    else:
      part1 = " "* ((len(op2)+2)-len(op1)) + op1
      part2 = sign + ' ' + op2
      part3= "-"* len(part2)
      part4 = " " * (len(part3)-len(answ)) + answ

    line1.append(part1)
    line2.append(part2)
    line3.append(part3)
    line4.append(part4)

  total = []
  total.append('    '.join(line1))
  total.append('    '.join(line2))
  total.append('    '.join(line3))
  total.append('    '.join(line4))

  if withAnswer == True:
    arranged_problems = '\n'.join(total)
  else:
    arranged_problems = '\n'.join(total[:-1])

  return arranged_problems
