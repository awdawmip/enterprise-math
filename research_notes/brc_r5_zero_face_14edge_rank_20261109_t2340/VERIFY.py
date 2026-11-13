"""Exact rational certificate for the R5 14-edge zero-marginal face theorem."""
from fractions import Fraction as Q
r=list(map(Q,'1/10 1/2 3/4 1 5/4 3/2 19/10'.split()))
mu=list(map(Q,('1776436/17038625 0 8901809/21809440 '
 '4095218743/29442744000 14797213/81785400 '
 '219439/545236000 4921555313/29442744000').split()))
nu=list(map(Q,('320280178677571/4128019922520000 '
 '43263964872863/2704970319600000 28207726175297/67624257990000 '
 '92699828728925827/474722291089800000 0 '
 '185998525907381/901656773200000 8330190867389003/94944458217960000').split()))
S=tuple(sorted(((0,0),(6,6))+tuple((i,j) for j in (1,2,3,5)
                                     for i in (0,2,3,4,5,6))))
w=list(map(Q,"""320280178677571/4128019922520000
259836587175363479/28483337465388000000
4163939580528917851/237361145544900000000
1/100000000
904888979/121892960160000
1/100000000
140050277696678373889/395601909241500000000
385435293745742857153/7120834366347000000000
904888979/52996939200000
1149346606791753413/178020859158675000000
162178355977236369389/3560417183173500000000
77483719314294687619/890104295793375000000
904888979/26498469600000
1/100000000
1/100000000
77019742865112790241/1424166873269400000000
180650920135742744371/1424166873269400000000
5485566073/13630900000000
1/100000000
1/100000000
1/100000000
56572122731/4306001310000000
904888979/68896020960000
904888979/68896020960000
942085121417421013/11868057277245000000
8330190867389003/94944458217960000""".split()))
assert len(S)==len(w)==26 and min(w)==Q(1,100000000)
def col(e):
 i,j=e; x=[Q(0)]*21;x[i]=1;x[7+j]=1;x[14+j]=r[i];return x
def rank(A):
 a=[list(map(Q,row)) for row in A]; k=0
 for j in range(len(a[0])):
  p=next((i for i in range(k,len(a)) if a[i][j]),None)
  if p is None: continue
  a[k],a[p]=a[p],a[k]
  v=a[k][j]; a[k]=[u/v for u in a[k]]
  for i in range(k+1,len(a)):
   if a[i][j]:
    v=a[i][j]; a[i]=[u-v*t for u,t in zip(a[i],a[k])]
  k+=1
  if k==len(a):break
 return k
assert mu[1]==nu[4]==0 and sum(mu)==sum(nu)==sum(w)==1
M=[[col(e)[i] for e in S] for i in range(21)]
assert [sum(M[i][j]*w[j] for j in range(26)) for i in range(21)]==mu+nu+[r[j]*nu[j] for j in range(7)]
assert rank(M)==14
B=((0,0),(0,1),(3,1),(5,1),(0,2),(2,2),(3,2),
   (2,3),(3,3),(4,3),(4,5),(6,5),(6,6),(6,1))
assert rank([[col(e)[i] for e in B] for i in range(21)])==14
print('PASS_26_STRICT_POSITIVE_EDGES min=1/100000000')
print('PASS_21_EXACT_BLACKWELL_EQUALITIES')
print('PASS_RANK_14_NULLITY_12')
print('PASS_INDEPENDENT_14_COLUMNS')
print('ZERO_FACE_UNIVERSAL_VERTEX_SUPPORT_BOUND 14')
