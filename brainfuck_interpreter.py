instruction = ".+[.+]"

tape = [0]*40

dataPointer = 0
instructionPointer = 0

out = ""

def add(i):
  global dataPointer
  tape[dataPointer]=(tape[dataPointer]+i)%255

def right(i):
  global dataPointer
  dataPointer+=i

def output(i):
  global dataPointer
  global out
  out+=chr(tape[dataPointer])

def ask(i):
  global dataPointer
  tape[dataPointer] = ord(str(input())[0])

def beg(i):
  global instructionPointer
  if not tape[dataPointer] and i>0 or tape[dataPointer] and i<0:
    next = 1
    while next:
      instructionPointer+=i
      if instruction[instructionPointer]=='[':
        next+=i
      elif instruction[instructionPointer]==']':
        next-=i

commands = {
'+' : (add,1),
'-' : (add,-1),
'>' : (right,1),
'<' : (right,-1),
'.' : (output,1),
',' : (ask,1),
'[' : (beg,1),
']' : (beg,-1)
}

def read(instruction):
  global instructionPointer
  a = len(instruction)
  while instructionPointer>=0 and instructionPointer<a:
    couple = commands[instruction[instructionPointer]]
    couple[0](couple[1])
    instructionPointer+=1
    print(tape)
  print(out)
