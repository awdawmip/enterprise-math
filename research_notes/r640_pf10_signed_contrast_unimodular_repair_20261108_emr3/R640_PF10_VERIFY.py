"""R640 PF-10 four-port signed-contrast map; exact integer proof checks."""
from itertools import combinations
from random import Random

n=4
labels=[f'I{i}' for i in range(n)]+[f'O{i}' for i in range(n)]+[f'M{i}{j}' for i in range(n) for j in range(n)]
idx={name:k for k,name in enumerate(labels)}
assert len(labels)==24

def row(**coeff):
 r=[0]*24
 for name,v in coeff.items(): r[idx[name]]+=v
 return r

u=[row(**{f'I{i}':1,f'O{i}':-1}) for i in range(n)]
pairs=list(combinations(range(n),2))
om=[row(**{f'M{i}{j}':1,f'M{j}{i}':-1}) for i,j in pairs]
A=u+om
anchors=[row(**{f'O{i}':1}) for i in range(n)]
anchors += [row(**{f'M{j}{i}':1}) for i,j in pairs]
anchors += [row(**{f'M{i}{i}':1}) for i in range(n)]
B=A+anchors
assert (len(A),len(anchors),len(B))==(10,14,24)

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def observe(x):return [dot(r,x) for r in B]

def decode(y):
 assert len(y)==24
 x=[0]*24
 for i in range(n):
  x[idx[f'O{i}']]=y[10+i]
  x[idx[f'I{i}']]=y[i]+y[10+i]
 for k,(i,j) in enumerate(pairs):
  x[idx[f'M{j}{i}']]=y[14+k]
  x[idx[f'M{i}{j}']]=y[4+k]+y[14+k]
 for i in range(n): x[idx[f'M{i}{i}']]=y[20+i]
 return x

def det(M):
 A=[list(row) for row in M];sgn=1;prev=1;size=len(A)
 for k in range(size-1):
  if not A[k][k]:
   nxt=next((r for r in range(k+1,size) if A[r][k]),None)
   if nxt is None:return 0
   A[k],A[nxt]=A[nxt],A[k];sgn=-sgn
  pivot=A[k][k]
  for i in range(k+1,size):
   for j in range(k+1,size):
    a=A[i][j]*pivot-A[i][k]*A[k][j]
    assert a%prev==0
    A[i][j]=a//prev
   A[i][k]=0
  prev=pivot
 return sgn*A[-1][-1]

D=det(B)
assert abs(D)==1
checks=0
for i in range(24):
 for k in (-5,-1,0,1,7):
  x=[0]*24;x[i]=k
  assert decode(observe(x))==x
  checks+=1
for i,j in combinations(range(24),2):
 x=[0]*24;x[i]=3;x[j]=11
 assert decode(observe(x))==x
 checks+=1
rng=Random(640)
for _ in range(1000):
 x=[rng.randrange(0,10**5) for i in range(24)]
 assert decode(observe(x))==x
 checks+=1
# Four I/O common shifts; six symmetric off-diagonal flows; four loops are a Z basis of ker(A).
kernel=[]
for i in range(n):
 k=[0]*24;k[idx[f'I{i}']]=k[idx[f'O{i}']]=1;kernel.append(k)
for i,j in pairs:
 k=[0]*24;k[idx[f'M{i}{j}']]=k[idx[f'M{j}{i}']]=1;kernel.append(k)
for i in range(n):
 k=[0]*24;k[idx[f'M{i}{i}']]=1;kernel.append(k)
assert len(kernel)==14
assert all([dot(r,k) for r in A]==[0]*10 for k in kernel)
assert all([dot(r,k) for r in anchors] !=[0]*14 for k in kernel)
# True PF-10 V26 witness.
x=[0]*24
for i,v in enumerate((0,0,2,1)):x[idx[f'I{i}']]=v
for i,v in enumerate((3,4,0,0)):x[idx[f'O{i}']]=v
x[idx['M10']]=x[idx['M20']]=1
v=[dot(r,x) for r in A]
assert v[:4]==[-3,-4,2,1]
assert v[4:]==[-1,-1,0,0,0,0]
assert decode(observe(x))==x
print('R640_PF10_UNIMODULAR_SOURCE_REPAIR_PASS',
      'source_columns',len(labels),'contrast_rows',len(A),'anchors',len(anchors),
      'determinant',D,'basis_kernel',len(kernel),'reconstruction_checks',checks,
      'source_example',v)
