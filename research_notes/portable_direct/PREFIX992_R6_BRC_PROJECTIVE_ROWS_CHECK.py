"""PREFIX-992: exact positive BRC recurrent-port kernel/projective-history compression.
Python 3; Fraction, Counter; auxiliary signed-source bit-flip graph (not native X6 dynamics).
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
import json

WORDS=((6,24,6,-3),(6,24,8,40))
# Two hidden vertices: A=diag(1/2,1/2), X row by hidden node,
# Y has one nonzero entry per visible-port row, B=0.
X=((1,2,1,3,2,4),(2,1,3,1,4,2)) # actual X / 100
CLASS=(0,0,1,1,0,1)
RHO=(1,2,1,2,3,3) # actual Y[h,CLASS[h]] = RHO[h] / 100
J=tuple(range(6))
A=((Fraction(1,2),Fraction(0)),(Fraction(0),Fraction(1,2)))
def v(a): return Fraction(2 if a[3]==1 else 3)
def f(c,a):return Fraction(X[c][a[2]],5000)*v(a)
def kernel(h,j):return Fraction(RHO[h]*X[CLASS[h]][j],5000)
def graph(word):
 p=max(abs(c) for c in word).bit_length()+1
 src={q:tuple((q,i,j,sgn) for i in range(p) for j in range(1,p) for sgn in (1,-1) if (1<<i)-sgn*(1<<j)==c) for q,c in enumerate(word)}
 ports=sorted({a[2] for row in src.values() for a in row})
 starts=tuple((0,1+sum(1<<j for k,j in enumerate(ports) if mask>>k&1)) for mask in range(1<<len(ports)))
 todo=deque(starts);seen=set(starts); edges={}
 while todo:
  state=todo.popleft();q,x=state
  row=[]
  for a in src[q]:
   if (x>>a[2]&1)!=(1-a[3])//2:continue
   t=((q+1)%len(word),x^(1<<a[2]));row.append((a,t))
   if t not in seen:seen.add(t);todo.append(t)
  edges[state]=tuple(row)
 return starts,edges

def direct(starts,edges,n,h=0):
 cur=Counter({(s,h,Fraction(1)):1 for s in starts})
 for _ in range(n):
  nxt=Counter()
  for (s,k,m),count in cur.items():
   for a,t in edges[s]:nxt[(t,a[2],m*kernel(k,a[2])*v(a))]+=count
  cur=nxt
 return cur

def compressed(starts,edges,n,h=0):
 if n==0:return Counter({(s,h,Fraction(1)):1 for s in starts})
 # Intermediate representation carries previous-port *projective class* only.
 cur=Counter({(s,CLASS[h],Fraction(1)):1 for s in starts})
 for _ in range(n-1):
  nxt=Counter()
  for (s,c,m),count in cur.items():
   for a,t in edges[s]:
    j=a[2];nxt[(t,CLASS[j],m*RHO[j]*f(c,a))]+=count
  cur=nxt
 result=Counter()
 for (s,c,m),count in cur.items():
  for a,t in edges[s]:result[(t,a[2],m*RHO[h]*f(c,a))]+=count
 return result

def composition(starts,edges,n,m,h=0):
 first=compressed(starts,edges,n,h)
 out=Counter()
 cache={}
 for (state,last,weight),count in first.items():
  key=(state,last)
  if key not in cache:cache[key]=compressed((state,),edges,m,last)
  for (t,j,v2),count2 in cache[key].items():out[(t,j,weight*v2)]+=count*count2
 return out

def summary(cur):
 hist=Counter()
 for (s,j,w),cnt in cur.items():hist[w]+=cnt
 return dict(path_count=sum(hist.values()),weight_mass=str(sum((w*c for w,c in hist.items()),Fraction(0))),distinct_weights=len(hist),terminal_rows=len(cur))

def main():
 # Schur complement check and projective row obstruction.
 Y=tuple((Fraction(RHO[h],100),Fraction(0)) if CLASS[h]==0 else (Fraction(0),Fraction(RHO[h],100)) for h in J)
 x=tuple(tuple(Fraction(t,100) for t in row) for row in X)
 W=tuple(tuple(sum((Y[h][k]*2*x[k][j] for k in (0,1)),Fraction(0)) for j in J) for h in J)
 assert all(W[h][j]==kernel(h,j) for h in J for j in J)
 assert X[0][1]*X[1][2]!=X[0][2]*X[1][1]
 assert all(W[h][j]*W[k][l]==W[h][l]*W[k][j] for h in J for k in J if CLASS[h]==CLASS[k] for j in J for l in J)
 rows=[]
 for word in WORDS:
  starts,edges=graph(word)
  for h in J:
   for n in range(13):
    d=direct(starts,edges,n,h);c=compressed(starts,edges,n,h)
    assert d==c,(word,h,n,len(d),len(c))
  for n,m in ((1,1),(2,3),(3,4)):
   assert composition(starts,edges,n,m)==direct(starts,edges,n+m),(word,n,m)
  rows.append(dict(word=word,initial_states=len(starts),reachable_states=len(edges),n8=summary(direct(starts,edges,8)),n12=summary(direct(starts,edges,12))))
 cert=dict(schema="PREFIX992_R6_PROJECTIVE_BRC_PORT_HISTORY_V1",model="positive rational BRC W_eff=Y(I-A)^-1 X with A=diag(1/2,1/2), B=0",X_numerator=X,Y_row_class=CLASS,Y_row_coefficient=RHO,denominator_X_Y=100,port_count=len(J),projective_history_classes=2,full_history_ports=len(J),checked_lengths=[0,12],checked_initial_history_ports=list(J),checked_gluing=[[1,1],[2,3],[3,4]],integer_fraction_arithmetic=True,rows=rows)
 print(json.dumps(cert,indent=2))
 with open('/mnt/data/prefix992/PREFIX992_R6_EXACT_RESULTS.json','w') as fp:json.dump(cert,fp,indent=2)
 print('PASS: BRC Schur, 2 projective classes, 2 words, 6 initial histories, n=0..12, 3 gluing splits')
if __name__=='__main__':main()
