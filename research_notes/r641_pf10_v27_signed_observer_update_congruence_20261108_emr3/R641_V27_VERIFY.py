"""R641: V26/V27 PF10 signed observer is update-congruence for frozen-count active triads."""
from itertools import combinations
n=4
TRIADS=tuple(combinations(range(6),3))
NEIGH={S:tuple(T for T in TRIADS if len(set(S)&set(T))==2) for S in TRIADS}
MATCHINGS=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
def vmatch(M,S):
 S=set(S);bits=[]
 for a,b in M:
  if (a in S)+(b in S)!=1:return 0
  bits.append(1 if b in S else 0)
 return 1 if sum(bits)%2==0 else -1
CODES={S:tuple(vmatch(M,S) for M in MATCHINGS) for S in TRIADS}
assert len(set(CODES.values()))==20

def observable(I,O,M):
 u=tuple(I[i]-O[i] for i in range(4))
 om=tuple(tuple(M[i][j]-M[j][i] for j in range(4)) for i in range(4))
 return u,om
def score(S,T,I,O,M):
 u,om=observable(I,O,M);cs=CODES[S];ct=CODES[T]
 return sum(u[i]*ct[i] for i in range(4))+sum(cs[i]*om[i][j]*ct[j] for i in range(4) for j in range(4))
def successor(S,I,O,M):
 vals=sorted(((score(S,T,I,O,M),T) for T in NEIGH[S]),reverse=True)
 assert vals[0][0]>vals[1][0]
 return vals[0][1]

I=(0,0,0,10);O=(2,4,3,0)
M=[[0]*4 for _ in range(4)]
M[0][1]=M[1][2]=M[2][0]=1
M=tuple(tuple(z) for z in M)
base=observable(I,O,M)
assert base[0]==(-2,-4,-3,10)
assert base[1]==((0,1,-1,0),(-1,0,1,0),(1,-1,0,0),(0,0,0,0))
F={S:successor(S,I,O,M) for S in TRIADS}
ODD=((0,1,2),(1,2,3),(2,3,4),(0,3,4),(0,3,5),(0,2,5))
FLAT=((1,4,5),(2,4,5))
assert all(F[ODD[i]]==ODD[(i+1)%6] for i in range(6))
assert all(F[FLAT[i]]==FLAT[(i+1)%2] for i in range(2))
def holonomy(cycle):
 base=cycle[0];slots={a:i for i,a in enumerate(base)}
 for ix,S in enumerate(cycle):
  T=cycle[(ix+1)%len(cycle)]
  common=set(S)&set(T)
  leave=next(iter(set(S)-common));enter=next(iter(set(T)-common))
  nxt={a:slots[a] for a in common};nxt[enter]=slots[leave];slots=nxt
 return tuple(slots[a] for a in base)
assert holonomy(ODD)==(2,1,0)
assert holonomy(FLAT)==(0,1,2)
perturbations=[]
for i in range(n):
 ip=list(I);op=list(O);ip[i]+=1;op[i]+=1
 perturbations.append((tuple(ip),tuple(op),M))
for i,j in combinations(range(n),2):
 mp=[list(r) for r in M];mp[i][j]+=1;mp[j][i]+=1
 perturbations.append((I,O,tuple(tuple(z) for z in mp)))
for i in range(n):
 mp=[list(r) for r in M];mp[i][i]+=1
 perturbations.append((I,O,tuple(tuple(z) for z in mp)))
assert len(perturbations)==14
assert all(observable(*X)==base for X in perturbations)
checks=0
for X in perturbations:
 for S in TRIADS:
  assert successor(S,*X)==F[S]
  checks+=1
  a=b=S
  for k in range(12):
   a=successor(a,*X);b=F[b]
   assert a==b
   checks+=1
assert all(X!=(I,O,M) for X in perturbations)
print('R641_PF10_V27_UPDATE_CONGRUENCE_EXACT_PASS',
      'source_states',1+len(perturbations),'triads',len(TRIADS),
      'steps_per_start',12,'transition_checks',checks,
      'signed_contrast_kernel_basis',len(perturbations),
      'odd_cycle_length',len(ODD),'odd_holonomy',holonomy(ODD),
      'flat_cycle_length',len(FLAT),'flat_holonomy',holonomy(FLAT))
