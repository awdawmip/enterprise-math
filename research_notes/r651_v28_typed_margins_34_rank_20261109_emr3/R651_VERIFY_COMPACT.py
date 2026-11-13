"""R651 exact 19/27/34 ranks, V28 recovery, signed collision. Python stdlib."""
from itertools import combinations,product
from fractions import Fraction
import json
P=range(4); E=[]
for c in (0,1):
 for a,b in product(P,repeat=2):
  if a!=b:E.append(('P',c,a,b))
for c in (0,1):
 for a,b in product(P,repeat=2):E.append(('T',c,a,b))
assert len(E)==56
pairs=list(combinations(P,2))
def state(word):
 M=[[[0]*4 for _ in P] for _ in range(2)]
 ri=[[0]*4 for _ in range(2)];ro=[[0]*4 for _ in range(2)]
 for typ,c,a,b in word:
  if typ=='P':M[c][a][b]+=1
  else:ro[c][a]+=1;ri[1-c][b]+=1
 return M,ri,ro
def fields(word):
 M,ri,ro=state(word);om=[];d=[];p=[];q=[];I=[];O=[]
 for c in (0,1):
  m=M[c];p0=[sum(row) for row in m]
  q0=[sum(m[i][j] for i in P) for j in P]
  om+= [m[i][j]-m[j][i] for i,j in pairs]
  d.append([ri[c][i]-ro[c][i] for i in P])
  p.append(p0);q.append(q0)
  I.append([p0[i]+ri[c][i] for i in P]);O.append([q0[i]+ro[c][i] for i in P])
 s19=om+d[0]+d[1][:3]
 s27=s19+I[0]+I[1]
 s34=s19+p[0]+p[1]+ro[0]+ro[1][:3]
 return (s19,s27,s34),(p,q,ri,ro,I,O)
def rank(cols):
 a=[[Fraction(v) for v in row] for row in zip(*cols)];r=0
 for j in range(len(a[0])):
  k=next((k for k in range(r,len(a)) if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];pivot=a[r][j]
  for k in range(r+1,len(a)):
   if a[k][j]:
    f=a[k][j]/pivot
    for h in range(j,len(a[0])):a[k][h]-=f*a[r][h]
  r+=1
  if r==len(a):break
 return r
def recover(z):
 assert len(z)==34
 dx=z[12:16];dy=z[16:19]+[-sum(z[12:19])]
 p=[z[19:23],z[23:27]];ro=[z[27:31],z[31:34]]
 ri0=[dx[i]+ro[0][i] for i in P]
 ro[1].append(sum(ri0)-sum(ro[1]))
 ri=[ri0,[dy[i]+ro[1][i] for i in P]]
 q=[];I=[];O=[]
 for c in (0,1):
  om=[[0]*4 for _ in P]
  for (i,j),v in zip(pairs,z[c*6:c*6+6]):om[i][j]=v;om[j][i]=-v
  q0=[p[c][i]-sum(om[i]) for i in P]
  q.append(q0)
  I.append([p[c][i]+ri[c][i] for i in P])
  O.append([q0[i]+ro[c][i] for i in P])
 return (p,q,ri,ro,I,O)
cols=[fields((e,))[0] for e in E]
ranks=[rank([x[k] for x in cols]) for k in range(3)]
assert ranks==[19,27,34]
words=0
for n in range(3):
 for word in product(E,repeat=n):
  s,full=fields(word)
  assert recover(s[2])==full
  assert sum(sum(v) for v in full[4])==sum(sum(v) for v in full[5])
  words+=1
assert words==3193
empty=fields(())[0][0]
a=fields((('P',0,0,1),('P',0,1,0)))
b=fields((('P',0,2,3),('P',0,3,2)))
assert empty==a[0][0]==b[0][0]
assert a[1][0]!=b[1][0]
print(json.dumps({'marker':'R651_V28_TYPED_MARGINS_34_RANK_EXACT_PASS',
 'event_generators':56,'ranks':ranks,'exhaustive_event_words_len_le_2':words,
 'witness':'two distinct reciprocal PASS pairs share signed19 but differ in typed V28 margins',
 'status':'exact integers/rationals; author-side'}))
