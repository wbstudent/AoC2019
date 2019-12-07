import itertools

def readList():
    list = []
    with open('./ex1Input.txt') as input:
        for value in input:
            list = [int(x) for x in value.split(',')]
    return list

class Amplifier:
  def __init__(self, phase, inputtt, posInChain):
    self.phase = phase
    self.inputtt = inputtt
    self.inputCounter = 0
    self.instr = readList()
    self.pos = 0
    self.posInChain = posInChain

  def work(self):
      # if self.inputCounter != 0:
      #     self.inputCounter += 1
      runn = True
      while self.instr[self.pos] != 99 and runn:
          commandStr = str(self.instr[self.pos])
          for i in range(0, 5 - len(commandStr)):
              commandStr = "0" + commandStr
          command = int(commandStr[-2:])
          if command == 99:
              command = 100
              return False
          modesStr = commandStr[0:3]
          modes = [int(char) for char in modesStr]
          if command == 1:
              val1 = self.instr[self.instr[self.pos + 1]] if modes[2] == 0 else self.instr[self.pos + 1]
              val2 = self.instr[self.instr[self.pos + 2]] if modes[1] == 0 else self.instr[self.pos + 2]
              self.instr[self.instr[self.pos + 3]] = val1 + val2
              self.pos += 4
          elif command == 2:
              val1 = self.instr[self.instr[self.pos + 1]] if modes[2] == 0 else self.instr[self.pos + 1]
              val2 = self.instr[self.instr[self.pos + 2]] if modes[1] == 0 else self.instr[self.pos + 2]
              self.instr[self.instr[self.pos + 3]] = val1 * val2
              self.pos += 4
          elif command == 3:
              self.pose = self.instr[self.pos + 1]
              self.instr[self.pose] = self.inputtt[self.inputCounter]
              self.inputCounter += 1
              self.pos += 2
          elif command == 4:
                self.pose = self.instr[self.pos + 1]
                # print(self.instr[self.pose])
                prevOutput = self.instr[self.pose]
                if len(amplis) < 5:
                    amplis.append(Amplifier(givPerm[(self.posInChain + 1)], [givPerm[(self.posInChain + 1)]], (self.posInChain + 1)))
                amplis[(self.posInChain + 1) % 5].addInput(prevOutput)
              # runn = False
                self.pos += 2
                return True
              # amplis[(self.posInChain + 1) % 5].work()
          elif command == 5:
              param = self.instr[self.instr[self.pos + 1]] if modes[2] == 0 else self.instr[self.pos + 1]
              if param != 0:
                  self.pos = self.instr[self.instr[self.pos + 2]] if modes[1] == 0 else self.instr[self.pos + 2]
              else:
                  self.pos += 3
          elif command == 6:
              param = self.instr[self.instr[self.pos + 1]] if modes[2] == 0 else self.instr[self.pos + 1]
              if param == 0:
                  self.pos = self.instr[self.instr[self.pos + 2]] if modes[1] == 0 else self.instr[self.pos + 2]
              else:
                  self.pos += 3
          elif command == 7:
              param1 = self.instr[self.instr[self.pos + 1]] if modes[2] == 0 else self.instr[self.pos + 1]
              param2 = self.instr[self.instr[self.pos + 2]] if modes[1] == 0 else self.instr[self.pos + 2]
              val3 = self.instr[self.pos + 3]
              if param1 < param2:
                  self.instr[val3] = 1
              else:
                  self.instr[val3] = 0
              self.pos += 4
          elif command == 8:
              param1 = self.instr[self.instr[self.pos + 1]] if modes[2] == 0 else self.instr[self.pos + 1]
              param2 = self.instr[self.instr[self.pos + 2]] if modes[1] == 0 else self.instr[self.pos + 2]
              val3 = self.instr[self.pos + 3]
              if param1 == param2:
                  self.instr[val3] = 1
              else:
                  self.instr[val3] = 0
              self.pos += 4
  def addInput(self, param):
      self.inputtt.append(param)


perm = list(itertools.permutations([5, 6, 7, 8, 9]))
maxOutput = 0
# for givPerm in perm:
pos = 0
# prevOutput = 0
# self.inputtt = []
for givPerm in perm:
# givPerm = [9,7,8,5,6]
    amplis = []
    # for indx, phase in enumerate(givPerm):
    amplis.append(Amplifier(givPerm[0], [givPerm[0], 0], 0))
    c = 0
    cond = True
    while cond:
        for i in range(0, 5):
            cond = amplis[i].work()

    outt = amplis[0].inputtt[len(amplis[0].inputtt)-1]
    if outt > maxOutput:
        maxOutput = outt
print(maxOutput)
# amplis[0].startWork(3)
    
    # # inputCounter = 0
    # # self.inputtt = [phase, prevOutput]
    # mylist2 = readList()
    # pos = 0
    # runn = True
    # mylist2[1] = phase
    # mylist2[2] = prevOutput
    # self.inputtt = prevOutput
    
    # if prevOutput > maxOutput:
    #     maxOutput = prevOutput
    # print("\n\n" + str(maxOutput))