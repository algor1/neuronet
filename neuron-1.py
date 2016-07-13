import random ,pdb
import math

AA=1#скорость обучения

# сигмоида
def sigmo(x):
 if x> 500:
  x=500
 elif x<-500:
  x=-500
 return 2/(1+math.exp(-x))-1

# производная от сигмоиды
def sigmodif(x):
 return (1+ (sigmo(x))**2)/2
# сумма листа
def listsum(list1,list2):
 return list(map(lambda x, y: x+y, list1,list2))
# округление листа
def listround(list1,num):
 return [round(x,num) for x in list1]


## распечатка весов


class neuron:
    
 def __init__(self, num):
  self.numSynapses=num+1
  self.synapses=[]
  self.output=0
  self.inputs=[]
  for I in range( self.numSynapses):
    self.synapses.append(random.random()-0.5)
    
  
# расчет выходного значения нейрона
 def calc(self,inputs):
  inputs.insert(0,1)
  self.inputs =inputs
  self.suminputs=sum(list(map(lambda x, y: x*y, self.synapses, inputs)))
  self.output=sigmo(self.suminputs)
  
 ## self.output=2/(1-math.exp(self.sumx))

 
# Изменения в весов синапсов
 def modify(self,rightoutput):
  #pdb.set_trace()
 ## print (rightoutput,self.output)
  self.neuronerror= (rightoutput-self.output)*sigmodif(self.suminputs)
 ## print(rightoutput-self.output,sigmodif(self.suminputs),self.neuronerror)
  self.rightinputs = []
  for I in range(len(self.synapses)):
   self.rightinputs.append ( self.synapses[I]*self.neuronerror*AA)
   self.synapses[I]=self.synapses[I]+self.neuronerror*self.inputs[I]*AA
  self.rightinputs.pop(0)
 ## print (111,self.rightinputs)
  return self.rightinputs 
  

class layer:
 # Класс слоя
 def __init__(self, num, num1):
  self.numNeurons=num
  self.numSynapses= num1
  self.neurons=[]
  self.outputs=[]
  for I in range( self.numNeurons):
    self.neurons.append(neuron(self.numSynapses))

# Расчет выходных значений всех нейронов слоя
 def calc(self, inputs):
  self.outputs =[]
  for n in self.neurons:
    n.calc(inputs)
    self.outputs.append(n.output)
 ## print(self.outputs)
 
# Изменение весов синапсов всех нейронов слоя
 def modify (self, rightoutputs):
  self.modyfiedinputs =[]
  for I in range(len(self.neurons)):
 ##   print("i=",I)##   print(3333, self.modyfiedinputs ,self.neurons[I], I, len(self.neurons),rightoutputs[I])
 ##   print (rightoutputs[I],self.neurons[I].output)      
    r=self.neurons[I].modify(rightoutputs[I])
    if len (self.modyfiedinputs)==0:
     self.modyfiedinputs=r
    else:
     self.modyfiedinputs=listsum(self.modyfiedinputs,r)
  return self.modyfiedinputs


class neuronet:
    def __init__(self, num, num1,num2):
        self.numlayers=num
        self.numinputs=num1
        self.numoutputs=num2
        self.layers=[]
        self.inputs=[]
        self.outputs=[]
        for I in range( self.numlayers-1):
            self.layers.append(layer(self.numinputs[I+1], self.numinputs[I]))
        self.layers.append(layer(self.numoutputs,self.numinputs[self.numlayers-1]))

    def printweights(self):
       for r in self.layers:
        print ("--------")
        for n in r.neurons:
          print (["{0:0.2f}".format(x) for x in n.synapses])
    # Расчет всех слоев
    def calc(self,layerinputs):
       self.nextlayerinputs= layerinputs
       for I in range(len(self.layers)):
      ##  print(I, self.nextlayerinputs)
        self.layers[I].calc( self.nextlayerinputs )
        self.nextlayerinputs=list(self.layers[I].outputs)
       return self.nextlayerinputs
#обучение
    def modify (self,num, num1, num2):
       self.inputs=num
       
       self.loops=num2
       for j in range(self.loops):
         self.nextrightoutputs=num1
         self.calc(self.inputs)
        
         for I in range(len(self.layers)-1,-1,-1):
        
           self.nextrightoutputs=  list(self.layers[I].modify( self.nextrightoutputs ))
    def savemindmap(self, str1):
      self.filename= str1
      f=open(self.filename, 'wt')
        

net1=neuronet(3,[4,4,8],2)
for I in range(2000):
 net1.modify([-1,-1,-1,1],[1,-1],1)
# print (net1.calc([-1,-1,1,-1]))

 net1.modify([-1,-1,1,-1],[-1,1],1)
# print (net1.calc([-1,-1,-1,1]))

# net1.modify([-1,1,-1,-1],[-1,1],2)
# print (net1.calc([1,-1,1,-1]))
    
# net1.modify([1,-1,-1,-1],[-1,1],2)    
# print (net1.calc([1,1,1,1]))
print("____________")      
print (net1.calc([-1,-1,-1,1]))
print (net1.calc([-1,-1,1,-1]))
print (net1.calc([-1,1,-1,-1]))
print (net1.calc([1,-1,-1,-1]))
net1.printweights()
##net1.savemindmap("1.txt")