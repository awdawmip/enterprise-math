# PREFIX-831 exact independent reproducibility checker (Python 3, stdlib only)
from collections import Counter, defaultdict
from math import factorial
A=[-98,-82,-58,-34,13,16,69,75,99]
B=[-x for x in A]
def coeff(x):
 e=[1]+[0]*len(x)
 for v in x:
  for i in range(len(x),0,-1): e[i]+=v*e[i-1]
 return e
def lift(a,b,h):
 x=Counter(a)+Counter(v+h for v in b)
 y=Counter(b)+Counter(v+h for v in a)
 c=x&y
 return sorted((x-c).elements()),sorted((y-c).elements()),sum(c.values())
assert coeff(A)[:9]==coeff(B)[:9] and coeff(A)[9]!=coeff(B)[9]
for step,h,want in [(9,24,12),(10,53,16)]:
 before=coeff(A)[step]-coeff(B)[step]
 A,B,removed=lift(A,B,h)
 assert len(A)==len(B)==want
 assert coeff(A)[:step+1]==coeff(B)[:step+1]
 assert coeff(A)[step+1]-coeff(B)[step+1]==step*h*before
A=sorted(v+100 for v in A);B=sorted(v+100 for v in B)
assert min(A+B)>0 and len(A)==len(B)==16
assert coeff(A)[:11]==coeff(B)[:11]
delta=coeff(A)[11]-coeff(B)[11]
assert delta==386647617821617152000
def trace(w):
 p=len(w);D={((1<<p)-1,0):1};out=[];states=edges=0
 for t in range(12):
  v=[0]*(p+1)
  for (mask,mark),mass in D.items():v[mask.bit_count()+mark]+=mass
  out.append(v);states+=len(D)
  if t==11:break
  N=defaultdict(int)
  for (mask,mark),mass in D.items():
   bits=mask
   while bits:
    bit=bits&-bits;j=bit.bit_length()-1
    N[mask^bit,mark]+=mass*w[j];edges+=1;bits-=bit
   if mark:N[mask,0]+=mass*3;edges+=1
   elif mask.bit_count()<p:N[mask,1]+=mass*2;edges+=1
  D=N
 return out,states,edges
ha,sa,ea=trace(A);hb,sb,eb=trace(B)
for t in range(12):
 for k in range(17):
  expected=factorial(11)*delta if (t,k)==(11,5) else 0
  assert ha[t][k]-hb[t][k]==expected,(t,k)
print('ALL_EXACT_ASSERTIONS_PASSED')
print('A=',A,'B=',B,'delta_e11=',delta,'delta_Y5_11=',factorial(11)*delta)
print('histogram_scalar_comparisons=',12*17,'named_states=',sa+sb,'transitions=',ea+eb)
