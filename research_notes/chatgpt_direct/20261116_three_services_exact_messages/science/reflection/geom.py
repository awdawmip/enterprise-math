from itertools import permutations,product
from pathlib import Path
from collections import Counter
D=Path(__file__).resolve().parent
P=[(x,y,z) for x in range(3) for y in range(5) for z in range(5)]
G=set()
for t,u in product(range(5), repeat=2):
 for a,b in product((1,-1),repeat=2):
  for eps in (1,2):
   for perm in (False,True):
    r=[]
    for x,y,z in P:
     if perm:y,z=z,y
     x=min((eps*x)%5,(-eps*x)%5)
     r.append(25*x+5*((eps*a*y+t)%5)+(eps*b*z+u)%5)
    G.add(tuple(r))
def pieces(m):
 while m:
  l=m&-m;yield l.bit_length()-1;m^=l
def image(m,r):return sum(1<<r[i] for i in pieces(m))

def reps(h):
 h=set(h);res=[]
 while h:
  s=min(h);orb={image(s,r) for r in G};assert orb<=h
  res.append((s,len(orb)));h-=orb
 return res
if __name__=='__main__':
 print('group',len(G));r=reps([int(l.split()[0]) for l in open('pdecomp.txt')]);print('p11reps',r);open(D/'p11_reps.txt','w').write(''.join(f'{m} {n}\n' for m,n in r))
 masks={}
 for l in (D/'fixed_all_masks.txt').open():
  hi,lo,a,b=map(int,l.split());m=(hi<<64)+lo;p=m>>25;f=m%2**25
  if b==4:masks.setdefault(p,set()).add(f)
 print('families',Counter((max(m.bit_count()for m in t),len(t)) for t in masks.values()))
 with open(D/'fix4.txt','w')as f:
  for p,t in masks.items():
   maximal=sorted([x for x in t if not any(x!=y and x&y==x for y in t)])
   print(p,len(maximal),*maximal,file=f)
