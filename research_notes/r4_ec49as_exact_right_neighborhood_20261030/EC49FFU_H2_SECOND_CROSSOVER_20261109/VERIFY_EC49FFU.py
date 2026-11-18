"""EC49FFU native signed-X6 prefix witnesses; frozen pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab."""
from collections import Counter
A={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
O='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
S=(0,0,4,1,16,32,8,2,0)
B={4:'ce',8:'ec',2:'ed',1:'de'}

def signed(w):return [n for t in w for n in A[t]]
def check(w,h,k,s):
 q=0
 for t in w:q=T[q][O.index(t)]
 assert S[q]==s
 c=Counter(w);x,y,z=k
 assert len(w)==h and (c['a'],c['e'],c['c']+c['d'],c['f'],c['g'])==(z-1,z,x+y-h-1,h+1-y-2*z,h+1-x)
 v=signed(w)
 assert len(v)==2*(sum(k)-1) and tuple(v.count(i)-v.count(-i) for i in range(1,7))==(2,0,0,0,0,0)
 return v

def count(paths):
 root={};total=0
 for p in paths:
  v=root
  for step in p:
   if step not in v:v[step]={};total+=1
   v=v[step]
 return total

def family(h,x):
 r=x-3;s=h+1-x
 return {4:'f'*r+'e'+'g'*s+'c',2:'f'*r+'e'+'g'*s+'d',8:'g'+'f'*r+'e'+'g'*(s-1)+'c',1:'g'+'f'*r+'e'+'g'*(s-1)+'d'}

def run(h):
 base=[check(w,2,(3,1,1),s) for s,w in B.items()]
 assert count(base)==28
 r=h-2
 ext={s:w+'g'*r for s,w in B.items()}
 late={4:'ce'+'g'*r,8:'e'+'g'*r+'c',2:'e'+'g'*r+'d',1:'de'+'g'*r}
 def cost(words,k):return count(base+[check(w,h,k,s) for s,w in words.items()])
 a=cost(ext,(3,h-1,1));b=cost(late,(3,h-1,1))
 assert (a,b)==(8*h+12,6*h+23)
 if h<4:return (h,a,b,None,min(a,b))
 for x in range(4,h+1):
  w=family(h,x);k=(x,h+2-x,1)
  assert cost(w,k)==4*h+42
  assert count([check(t,h,k,s) for s,t in w.items()])==4*h+16
 return (h,a,b,4*h+42,min(a,b,4*h+42))

if __name__=='__main__':
 for h in list(range(3,33))+[40,48,64,80,100]:
  print(*run(h))
 assert run(10)==(10,92,83,82,82)
