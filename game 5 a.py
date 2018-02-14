import random
z=['A','B','c','D','E','F','G','H','I','J','A','B','C','D','E','F','G','H','I','J']
random.shuffle(z)
y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print ("welcome:",y)
p1=0
p2=0
while(y!=['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']):
      print("p1 turns")
      n1=int(input())
      n2=int(input())
      y[n1-1]=z[n1-1]
      y[n2-1]=z[n2-1]
      print(y)
      if(y[n1-1]==y[n2-1]):
        y[n1-1]=y[n2-1]=z[n1-1]=z[n2-1]='*'
        p1=p1+1
        print(p1,1)
      else:
        y[n1-1]=n1
        y[n2-1]=n2
        print(p1,y)
        print("p2 turns")
        n3=int(input())
        n4=int(input())
        y[n3-1]=z[n3-1]
        y[n4-1]=z[n4-1]
        print(y)
      if(y[n3-1]==y[n4-1]):
        y[n3-1]=y[n4-1]=z[n3-1]=z[n4-1]='*'
        p2=p2+1
        print(p2,y)
      else:
        y[n3-1]=n3
        y[n4-1]=n4
        print(p2,y)
      if(p2>p1):
        print("p2 win")
      else:
        print("p1 win")
      
      
      
      
      
      
      
      
      
