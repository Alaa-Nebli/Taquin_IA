
from copy import deepcopy
from collections import deque

class taquin(object) : 
  t = [] 
  tf =[[1,2,3],[4,5,6],[7,8,0]]
  def __init__(self,tab):
      self.t = tab
 
  def etat_finale(self,t) : 
    for i in range(3) :
      for j in range(3):
        if (t[i][j] != self.tf[i][j]):
          return False
    return True 
 
  def position_case_vide(self,tb):
    for i in range(3) :
      for j in range(3):
        if (tb[i][j] == 0):
            return i,j
    return -1
 
  def permuter(self,t,c1,c2):
    i,j =c1 
    ii,jj=c2
    aux=t[i][j]
    t[i][j] = t[ii][jj]
    t[ii][jj] = aux 
    return t
 
 
  def affiche(self,t):
    j=0
    for i in range(7):
      if(i%2==0):
        print("|__|")
      else:
        print("|",t[j][0],"|",t[j][1],"|",t[j][2]," |")
        j=j+1

  def numero(self,x,y):
    return self.t[x][y]
 
  def transition(self,arr):
    tb=[]
    x,y=self.position_case_vide(arr)
    l=[]
    
    if(x-1>=0):
      l.append(((x-1),y))
    if(y-1>=0):
      l.append((x,(y-1)))
    if(x+1<3):
      l.append(((x+1),y))
    if(y+1<3):
      l.append((x,(y+1)))

    for i in range(len(l)):
      t1=deepcopy(arr)
      self.permuter(t1,self.position_case_vide(t1),l[i])
      tb.append(t1)
    return tb

  def dfs(self):
      freeNodes = []
      closed = []
      success = False 
      freeNodes.append(self.t)
      l=0
      lenGeneratedState = len(self.transition(freeNodes[0]))
      while (success == False and len(freeNodes) != 0) and l<9:
      
        generatedStates= self.transition(freeNodes[0])
        #print('Free Node 1  = ',freeNodes)
        closed.append(freeNodes[0])
        freeNodes.pop(0)
        #print('first Node after del =  ',freeNodes)
        #print('Generated state  =  ',generatedStates)
        moved = False
        for i in generatedStates:
          if ( i not in closed) or (i not in freeNodes) :
            #print(i in closed)  
            freeNodes.insert(0,i)
            moved = True
        if moved==True: 
          l+=1 
          lenGeneratedState = len(generatedStates)
        else:
          if (lenGeneratedState <= 1 ):
            l-=1 ; 
          else:
            lenGeneratedState-= 1 
        
        #print('free Node after insert generated =  ',freeNodes)
        if(self.etat_finale(closed[-1])):
          success=True
          for i in closed:
            self.affiche(i)
          print(l)
        
        
      
  def bfs(self):
      freeNodes = []
      closed = []
      success = False 
      freeNodes.append(self.t)
      while (success == False and len(freeNodes) != 0) :
        generatedStates= self.transition( freeNodes[0])
        closed.append(freeNodes[0])
        freeNodes.pop(0)
        for i in generatedStates:
          if ( i not in closed) or (i not in freeNodes) :
            freeNodes.append(i)   
        if(self.etat_finale(closed[-1])):
          success=True
          for i in closed:
            self.affiche(i)
 
  def G(self,n):
    nodeX,nodeY = self.position_case_vide(n)
    goalX,goalY=self.position_case_vide(self.tf)
    dx = abs(nodeX - goalX);
    dy = abs(nodeY - goalY);
    return 1 * (dx + dy);
  
  def H(self,n):
    nodeX,nodeY = self.position_case_vide(n)
    goalX,goalY=self.position_case_vide(self.t)
    dx = abs(nodeX - goalX);
    dy = abs(nodeY - goalY);
    return 1 * (dx + dy);   
  
  def Best(self,arr):
    min=self.H(arr[0])+self.G(arr[0])
    node=arr[0]
    for i in arr:
      curr=self.H(i)+self.G(i)
      if (curr<min):
        node=i
        min=curr
    return node
  
  def aStar(self):
    freeNodes = []
    closed = []
    success = False 
    freeNodes.append(self.t)
    while (success == False and len(freeNodes) != 0) :
        
        generatedStates= self.transition(freeNodes[0])
        bestNoued = self.Best(generatedStates)
        closed.append(bestNoued)
        
        if(self.etat_finale(closed[-1])):
          success=True
          for i in closed:
            self.affiche(i)   
    
        freeNodes.pop(0)
        for i in generatedStates:
          if ( i not in closed) or (i not in freeNodes) :
            freeNodes.append(i)



