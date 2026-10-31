"""EC49CO independent modular rank check, native X6 A/B DFA, no imports from other research."""
from collections import defaultdict
P=1000003
Q=[(a,b) for a in range(3) for b in range(3) if (a,b)!=(1,1)]
S={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1)}
def step(q,x):
 a,b=q
 if a!=2:a=2 if a==1 and x==2 else (1 if x==1 else 0)
 if b!=2:b=2 if b==1 and x==1 else (1 if x==2 else 0)
 return a,b
def run(q,s):
 for x in s:q=step(q,x)
 return q
M={x:tuple(Q.index(run(q,w)) for q in Q) for x,w in S.items()}
def expand(m,x):return tuple(M[x][i] for i in m)
def rank(rows):
 piv={}
 for row in rows:
  r=[x%P for x in row]
  for j,p in sorted(piv.items()):
   if r[j]:
    c=r[j];r=[(x-c*y)%P for x,y in zip(r,p)]
  j=next((k for k,x in enumerate(r) if x),None)
  if j is not None:
   c=pow(r[j],-1,P);piv[j]=[(c*x)%P for x in r]
 return len(piv)
def total(maps):
 groups=defaultdict(set)
 for i,j,m in maps:
  labels=[(Q[k][0]==2)*2+(Q[k][1]==2) for k in m]
  for tag in range(4):groups[i,j].add(tuple(int(x==tag) for x in labels))
 return 3*sum(rank(g) for g in groups.values())
L=[{(0,0,tuple(range(8)))}]
for h in range(1,17):
 L.append({(i+(x=='a'),j+(x=='b'),expand(m,x)) for i,j,m in L[-1] for x in S})
 if h<2:continue
 k=h-1;N=(k+1)*(k+2)//2
 allmaps=set().union(*L[1:h+1]); one={}
 for x in S:
  i0=int(x=='a');j0=int(x=='b');m0=M[x]
  one[x]={(i+i0,j+j0,tuple(m[m0[z]] for z in range(8)))
          for l in L[1:h] for i,j,m in l}
 future=set().union(*one.values())
 D=3*(3*h*h+7*h+1)
 assert total(allmaps)==D
 assert (total(one['a']),total(one['b']),total(one['c']),total(one['d']),total(future))==(
          3*(4*N-1),3*(4*N-1),6*N,6*N,D-6)
 print(k,D,total(one['a']),total(one['c']),total(future),D-total(future))
