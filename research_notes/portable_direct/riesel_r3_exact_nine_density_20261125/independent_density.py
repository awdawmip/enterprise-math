from itertools import combinations,product
from math import prod
from fractions import Fraction
from decimal import Decimal,getcontext
from functools import lru_cache
import json

A=(1,2,10,11,12,16,17,22,25,26,30,31,32)
Z=(29,43,1429,5419)
G=(92737,649657,40388473189,77158673929,118750098349)
B=(193,1153,6337,22253377,38941695937,278452876033)
D=(33975937,138991501037953)
C=(61681,4562284561,168692292721,469775495062434961)
R=(209924353,4261383649,24929060818265360451708193)
H=(8369281,394783681,4278255361,46908728641,750016890283777055704738227247474485366338380663681)
F=(3457,816769,18446744069414584321,1562985901350085709953,1422346738975853644793916289)
J=(3361,15790321,88959882481)
U=(211,421,86171,106681,122921,152041,664441,1564921,7416361,47392381,146919792181,1041815865690181)
L=(2017,5153,25629623713,54410972897,1538595959564161)
V=(127681,1130641,755667361,84179842077657862011867889681,54169520413224311136354324156824071681)
T=C[:2]
C2=C[2:]
allgroups=(Z,G,B,D,C,R,H,F,J,U,L,V)
assert len(set(q for xs in allgroups for q in xs))==59

@lru_cache(None)
def ord2(q):
 p=1
 for d in range(1,841):
  p=2*p%q
  if p==1:return d
 raise ValueError(q)
from math import gcd
def f_of(q):
 d=ord2(q)
 return d//gcd(d,12)
def h_of(q):
 d=ord2(q)
 return d//gcd(d,36)

@lru_cache(None)
def common_counts(G,k):
 return masks_group(G,k)

def masks_group(G,k):
 d={0:1}
 for q in G:
  nxt={}
  for z,w in d.items():
   if q>2*k:nxt[z]=nxt.get(z,0)+(q-2*k)*w
   for j in range(k):
    a=z|(1<<j)
    nxt[a]=nxt.get(a,0)+2*w
  d=nxt
 assert sum(d.values())==prod(G)
 return d

def occ(G,k):
 return common_counts(G,k).get((1<<k)-1,0)
def rprob(u,gp):
 return Fraction(u,prod(gp))

def point(c):
 return tuple(a for a in A if a%7==c)
def phase(b,mod,sm):
 return tuple(i for i,a in enumerate(sm) if (a-b)%mod==0)
def class_mask(P,p,b):
 # Four lifts of each point, enough for all geometric zero-common templates.
 return sum(1<<(4*i+k) for i,a in enumerate(P) for k in range(4) if (a+35*k-b)%p==0)

def geom_terms(P,groups,bud):
 # Each group entry: (type name, period, max distinct primes).
 # Geometric term = needed distinct class-presence bits in each group.
 a=[(k,b,class_mask(P,p,b)) for k,p,lim in groups for b in range(p) if class_mask(P,p,b)]
 grouped={k:sorted(b for l,b,m in a if l==k) for k,p,lim in groups}
 ix={(k,b):i for k,p,lim in groups for i,b in enumerate(grouped[k])}
 lims={k:lim for k,p,lim in groups}
 X=(1<<(4*len(P)))-1
 terms=[]
 for cs in combinations(a,bud):
  v=0;ct={};s={}
  for k,b,m in cs:
   v|=m;ct[k]=ct.get(k,0)+1;s[k]=s.get(k,0)|(1<<ix[k,b])
  if v!=X or any(ct[k]>lims[k] for k in ct):continue
  if any((m&~sum_mask([x[2] for x in cs if x!=(k,b,m)]))==0 for k,b,m in cs):continue
  terms.append(tuple(s.get(k,0) for k,p,lim in groups))
 return grouped,terms

def sum_mask(vals):
 x=0
 for a in vals:x|=a
 return x

# Under budget8 exclusion, S=4 implies Type II (with one Z ignored) is impossible:
# whichever row is missing already triggers Z8 by its U-pair or J-pair.
# Type III survives when both small rows are usable and needs these phase bits.
small=point(1)+point(5)
cube_g,cube_terms=geom_terms(small,(('J',14,3),('U',35,12),('T',10,2)),4)
assert len(cube_terms)==7, cube_terms
cube_d={k:common_counts({'J':J,'U':U,'T':T}[k],len(bs)) for k,bs in cube_g.items()}

def indicator(terms,bits):
 return any(all(u&v==u for u,v in zip(a,bits)) for a in terms)
def reindex_mask(M,l1,l2):
 return sum(1<<i for i,b in enumerate(l2) if b in l1 and (M>>l1.index(b))&1)

@lru_cache(None)
def zero_kernel(S,ct):
 # returns Pr(no Z8), Pr(no Z8 and no Z9_common).
 # ct is witnessed T-presence mask over all 10 v phases.
 S=set(S)
 s=len(S)
 if s<=2:return Fraction(1),Fraction(1)
 miss=sorted(set(range(1,6))-S)
 if s==3 and all(m in (1,5) for m in miss):
  z=0
  t=reindex_mask(ct,list(range(10)),cube_g['T'])
  for j,x in cube_d['J'].items():
   for u,y in cube_d['U'].items():
    if indicator(cube_terms,(j,u,t)):z+=x*y
  return Fraction(1),1-rprob(z,J+U)
 if s==3 and sum(m in (1,5) for m in miss)==1:
  return Fraction(1),1-rprob(occ(J,2)*occ(U,2),J+U)
 if s==3:return Fraction(1),Fraction(1)
 c,=miss
 small_c=c in (1,5)
 P=point(c)
 gs,terms=geom_terms(P,(('J',14,3),('U',35,12),('T',10,2),('L',28,5),('V',70,5)),3)
 # Type IV–VIII only; T or V are allowed only on small row.
 if not small_c:terms=[s for s in terms if not s[2] and not s[4]]
 # Four-Z common geometry does not admit two T slots in same phase, etc.
 # Type III with one Z ignored if missing small (other small may be ignored).
 jph=cube_g['J'] if small_c else gs['J']
 uph=cube_g['U'] if small_c else gs['U']
 t=reindex_mask(ct,list(range(10)),gs['T'])
 tc=reindex_mask(ct,list(range(10)),cube_g['T'])
 j0=reindex_mask((1<<len(gs['J']))-1,gs['J'],jph)
 u0=reindex_mask((1<<len(gs['U']))-1,gs['U'],uph)
 jl=common_counts(J,len(jph));ul=common_counts(U,len(uph))
 ml=common_counts(L,len(gs['L']))
 mv=(common_counts(V,len(gs['V'])) if small_c else {0:prod(V)})
 noir=noir_no9=0
 for j,x in jl.items():
  for u,y in ul.items():
   if j&j0==j0 or (small_c and u&u0==u0):continue
   noir+=x*y
   if small_c and indicator(cube_terms,(j,u,tc)):continue
   jr=reindex_mask(j,jph,gs['J'])
   ur=reindex_mask(u,uph,gs['U'])
   cnt=sum(zl*zv for bl,zl in ml.items() for bv,zv in mv.items() if not indicator(terms,(jr,ur,t,bl,bv)))
   noir_no9+=x*y*cnt
 return rprob(noir,J+U),rprob(noir_no9,J+U+L+V)

def cover_pair(g1,g2,k):
 # D or E group; g1 and g2 all equally weighted inside phase categories.
 total=prod(g1+g2)
 no8=(prod(g1)-occ(g1,k))*prod(g2)
 no9=total-occ(g1+g2,k)
 return Fraction(no8,total),Fraction(no9,total)

@lru_cache(None)
def no_col(t):
 # selected T phases in v -> w mod h (h=10). Old and new require
 # w=0,6,8 for C10; H20 permits w=0,8,16.
 flags=0
 for i,b in enumerate((0,6,8)):
  if t>>( (2+3*b)%10 )&1:flags|=1<<i
 # Actual coefficient cardinalities are 2 per allowed phase at every q.
 d=common_counts(C2,3);e=common_counts(H,3)
 a=sum(w for c,w in d.items() if c|flags!=7)
 b=sum(w*z for c,w in d.items() for h,z in e.items() if c|h|flags!=7)
 return rprob(a,C2),rprob(b,C2+H)

def sums():
 # Budget8 binary vs augmented binary refinement. B supports old t parities.
 # F supports four t phases. New if B has both parities OR one B parity and
 # both F slots of the opposite parity.
 b0=prod(B)-occ(B,2)
 b1=sum(x*y for b,x in common_counts(B,2).items() for f,y in common_counts(F,4).items()
        if b!=3 and not (b&1 and f&10==10) and not (b&2 and f&5==5))
 bb=(rprob(b0,B),rprob(b1,B+F))
 dd=cover_pair(D,R,2)
 total0=total1=Fraction(0)
 zstates=common_counts(Z,5)
 tstates=common_counts(T,10)
 comp_8=Fraction(0)
 for sm,zw in zstates.items():
  sset=tuple(i+1 for i in range(5) if sm>>i&1)
  gz=1-rprob(occ(G,5-len(sset)),G)
  for tm,tw in tstates.items():
   z0,z1=zero_kernel(sset,tm & sum(1<<b for b in cube_g["T"]) if (1 not in sset or 5 not in sset) else 0)
   c0,c1=no_col(tm)
   w=rprob(zw*tw,Z+T)
   total0+=w*z0*c0*bb[0]*dd[0]
   total1+=w*z1*c1*bb[1]*dd[1]*gz
 assert 0<total1<total0<1
 return total0,total1

if __name__=='__main__':
 n0,n1=sums()
 getcontext().prec=75
 value=n0-n1
 def js(x):
  return {'n':str(x.numerator),'d':str(x.denominator),'decimal':str(Decimal(x.numerator)/Decimal(x.denominator))}
 print(json.dumps({'no8':js(n0),'no8_no9':js(n1),'exact9':js(value),'cache':str(zero_kernel.cache_info())},indent=2))
