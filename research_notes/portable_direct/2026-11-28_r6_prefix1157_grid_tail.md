# PREFIX-1157: representation-grid refinement and common signed-scale separator

Date 2026-11-28. EM-DIRECT-780BBE / TASK_RESEARCH; own managed session metadata recovered (not a formal CLAIM). AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Scope and source
Continue PREFIX-1156 at 4952a6267c51206f59400bd4c229d99003afdadb:research_notes/portable_direct/2026-11-28_r6_prefix1156_scale_tail.md; frozen P000 V5 and companions f42f2906d77f24085c123f3ccfe9667d41caa96d. Current global entry snapshot 46607ca52b542354a2f47d37f29f7790be5cd7a9; project control snapshot 46aa221e08785c5812b81d9fff9c5f01f3007ada. Owner observation request r6-20261128-1950-owner-read was RUNNING at the last poll before scientific publication. No shared Task mutation. Prior Stage46, anchor, affine transfer and primitive relation reduction hypotheses remain in force. This is auxiliary parameter-space arithmetic on frozen derived observations, not a new native Heartbeat computation or a new physical claim.

## 1. Targeted representation refinement
The minimum PREFIX-1156 candidate is feasible even at zero scale. Changed-budget experiments showed that shrinking point-row errors by 10^6 did not remove it, whereas shrinking rows 8..14 by ten (with center/columns fixed) produced an exact zero-scale support ratio 4.027765. This is diagnostic only. Reconstruct the actual thirteen moment rows from the retained exact row coefficients and the raw 10^150 floors; increase their final grid from G0=10^140 to G=10^145. Keep the point rows unchanged in normalized units, by exact integer scaling. No new raw moment or anchor evaluation.

For a moment row with exact reconstructed center M and 12 coefficients B_j, set m=floor(G M), C_j=floor(G B_j), e=ceil(G delta)+13, where delta is the previously established analytic tail + raw half-grid + Frobenius basis + internal arithmetic payment:
delta=(6^(j+1)/(j+1) if channel j>0 else 1)*(35/36)^k + 1/(2*10^150)+10^-180+1205/10^155.
The center and 12 coefficient floors each contribute <1 in scaled units; each shared coefficient is bounded by one, so the formula pays all errors. Reconstructed old center, column and error integers agree in all 13 rows with PREFIX-1153. Six of the seven high-order rows (9..14) improve their normalized error by 100000; row 8 improves by 1150.36976; the six lower-order moment rows are largely analytic-tail limited. Preserve all 12 shared columns and 15 independent error columns.

## 2. Single separator for all 34374 primitive relations
At L*=10^130, let U=[C,diag(e)], A,B be the inherited affine transfer columns at G=10^145. For a candidate line, d_n=n dot (A*(p/q-r)+B*(h/q-u)-m). Define S=sum_j |n dot U_j|, a=n dot A, b=n dot B. Positive and negative supports are sp=S+max(0,-a)*K/L*^2+max(0,b)*H/L*, sm=S+max(0,a)*K/L*^2+max(0,-b)*H/L*. Here L*^2 denotes (L*) squared. A ratio max(d_n/sp,-d_n/sm)>1 is a strict separation certificate. These supports decrease as L increases, so a strict separation is valid uniformly for all L>=L*. We use the same normal for every candidate, rather than assigning a separate witness. The normal is inverse-pivot row 11 (zero-based), with pivot indices [5,0,14,15,16,17,18,19,20,3,28,23,1,4,2] in U plus the two signed-scale columns. Its validity is independently established by exact rational elimination and checking the resulting dual row against the pivot matrix.

Use the old PREFIX-1154 polygon with signed rectangle at L* as a necessary domain (and original PREFIX-1156 unimodular integer coordinates). For q0<=q<=3*10^85, exact box is [0,33] x [-33,62] x [-24,74]. All 323136 points were enumerated in the independent integer checker, giving 56554 points satisfying the inherited support constraints and 34374 primitive gcd(q,p)=1 lines. The interval elimination search used 3264 outer pairs and returned exactly the same sorted population. All 34374 violate the new signed support pair. Min ratio 2.395426698659215, exact lower certificate >2395/1000. This proves L>=10^130 => b-a>=q>3*10^85 under the inherited hypotheses. The previous 40 candidates at Q=3*10^84 were all excluded with the common normal; min ratio 376.399592441736. No floating arithmetic is used for acceptance.

## 3. Dyadic consequences
Stitch with the prior smaller-scale certificate. Using the inherited triple necessary inequality q^2<4*E*L/dlo and close-pair threshold gap<=sqrt(L), exact dyadic comparison gives first not excluded windows (for the certificate, not asserted actual exceptions):
triple 5491838128104487771985520639265114573815548240114644327515570767348434546718124841698047712529163643981837049113184686429697590399773315050059222632892045721600000000
near pair 1439652414253822842499372322459514194838303077856613322592241783235788025814876118502093019553245074287974691402726686439426645137758175900482724857876852433643110400000000
Factors over PREFIX-1156: 512 and 1024. Continuous-scale uniform small-L bound and consecutive integer endpoint unchanged.

## 4. Reproduction
Use the verified PREFIX-1156-execution-evidence.zip, SHA256 1730a3ce2fe4217003ed02a50c259260a2d54c93bdb27c87cf0eb5779f2025ae. Its manifest was checked. Extract into a directory and save the following program as compact1157.py. It uses only stdlib and frozen input files; compact1156.py and compact1155.py supply the inherited support domain and unimodular coordinates. Independently constructs the search box and tests all integer points, not a sample. Locally executed program SHA256 aee1ad5f1ad9df4d74fd6a41d83b477341d07de190c28d034c11b20d765db76d; log SHA256 8c69983b19d2ed432800a591d48e1cd4078c1f79c494de6a8b448a4c94d71291. Source files fixture1141.json cb38649b5a98a767b9658c9792af8d21f66b1c2f9290d1e7160b6cc602b6481a; section1154.json 178472aba386cc14ae500acfc70eb7e3b5aa5ccc31601e399c0c8ae3aa8ee885; point1153.json e63d78a63e887a1fb1dee9e53366c9bebc92ce2d4ded717d963672fe5d605280; refine1148.json 835df78001601b914376f122820ec7b34a47e2beed7849be4e901fbd30036a6b; anchor_compact.json 90d2891844e2db432af6efb66be7325f914f1934ad553d7d6e61cf9182cc88ff; compact1155.py a9a767589bc4aa3ea84c7cdf0177eda1be3b2e4af7d5635d4753a75186aa61a0; compact1156.py dbe38199ffa736a10b70bcc838611df4cd09b93963b28a260601018f971e8332. New grid1157.json SHA256 37e90cd079e8b6b9dfb1c103bc007e99ff905caefe4f9cde8b51e1cc938d3d76.

```python
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import ceil,floor,gcd,lcm,prod
import json
exec(Path('compact1156.py').read_text().split('for k,Q,count,firstq in ')[0])
G0=10**140; G=10**145; scale=G//G0
old=json.load(open('point1153.json')); raw=json.load(open('refine1148.json'))['rows']; pkt=json.load(open('anchor_compact.json'))
cc=[F(int(v),10**120) for v in pkt['center']]; Wc=[[F(int(v),10**140) for v in row] for row in pkt['weighted_columns_rows']]; dr=[F(int(v),10**140) for v in pkt['rounding_radii']]
assert max(abs(cc[i])+sum(map(abs,Wc[i]))+dr[i] for i in range(6))<1
m=[v*scale for v in old['m'][:2]]; e=[v*scale for v in old['e'][:2]]; C=[[v*scale for v in c[:2]] for c in old['cols']]
rows=sum([json.load(open(p)) for p in ['radial1146_low.json','coupled1146.json','radial1146_high.json','extra_radial1144_tight.json','extra_coupled1144_tight.json']],[])
assert len(rows)==len(raw)==13
for i,(rec,R) in enumerate(zip(rows,raw),2):
    k,j=rec['k'],rec.get('channel',0); assert (k,j)==(R['k'],R['channel']); row=list(map(F,rec['row']))
    center=dot(row,cc)-F(2*int(R['raw'])+1,2*10**150)
    cols=[sum(row[i]*Wc[i][l] for i in range(6)) for l in range(6)]+[row[i]*dr[i] for i in range(6)]
    err=(F(6**(j+1),j+1) if j else F(1))*F(35,36)**k+F(1,2*10**150)+F(1,10**180)+F(1205,10**155)
    assert floor(center*G0)==old['m'][i] and [floor(x*G0) for x in cols]==[c[i] for c in old['cols']] and ceil(err*G0)+13==old['e'][i]
    m.append(floor(center*G)); e.append(ceil(err*G)+13)
    for c,x in zip(C,cols):c.append(floor(x*G))
N=len(m); U=C+[[e[i] if i==j else 0 for i in range(N)] for j in range(N)]
aj,am,dj=map(F,(D['aj'],D['am'],D['dj'])); A=[-G*aj,-G*dj]+[0]*(N-2); B=[0,G*am]+[0]*(N-2)
k=10**16; Q=3*10**85; s=[-a*K/(2*(L*k)**2) for a in A]; t=[b*H/(2*L*k) for b in B]
U1=U+[s,t]; piv=[5,0,14,15,16,17,18,19,20,3,28,23,1,4,2]
# Solve transpose of pivot matrix for a single row of its inverse.
M=[[F(v) for v in U1[j]]+[F(i==11)] for i,j in enumerate(piv)]
for i in range(N):
    j=next(j for j in range(i,N) if M[j][i]); M[i],M[j]=M[j],M[i]; x=M[i][i]; M[i]=[a/x for a in M[i]]
    for j in range(N):
        if i!=j:
            x=M[j][i]; M[j]=[a-x*b for a,b in zip(M[j],M[i])]
n=[row[-1] for row in M]; assert all(dot(n,U1[j])==(i==11) for i,j in enumerate(piv))
S=sum(abs(dot(n,c)) for c in U); a=dot(n,A); b=dot(n,B); z=dot(n,m)
sp=S+max(0,-a)*K/(L*k)**2+max(0,b)*H/(L*k); sm=S+max(0,a)*K/(L*k)**2+max(0,-b)*H/(L*k)
# First search uses inherited integer interval elimination; second tests every point of an independently built integer box.
box,outer,pts,ls=search(k,Q,V1,W1); assert (box,outer,pts,len(ls))==([(0,33),(-33,62),(-24,74)],3264,56554,34374)
box2=[]
for aa,bb,cc1 in V1:
    vals=[q*(aa+bb*(x-d)+cc1*(y+ee)) for q,(x,y),d,ee in product((q0,Q),P,(0,K/(k*L)**2),(0,H/(k*L)))]; box2.append((ceil(min(vals)),floor(max(vals))))
assert box2==box
def ints(row):
    den=lcm(*(F(x).denominator for x in row)); v=[int(x*den) for x in row]; g=gcd(*v); return [x//g for x in v] if g else v
ineq=[ints([aa*W1[1][i]+bb*W1[2][i]-zz*W1[0][i] for i in range(3)]) for aa,bb,zz in supports(F(k))]
# Signed support constraints in the old integer coordinate system; violation of either is sufficient.
base=[a*W1[1][i]+b*W1[2][i]-(a*r+b*u+z)*W1[0][i] for i in range(3)]
pos=ints([v-sp*w for v,w in zip(base,W1[0])]); neg=ints([-v-sm*w for v,w in zip(base,W1[0])])
found=[]; np=0
for v in product(*(range(x,y+1) for x,y in box2)):
    q=dot(W1[0],v)
    if not q0<=q<=Q or any(dot(row,v)>0 for row in ineq):continue
    np+=1; p,h=dot(W1[1],v),dot(W1[2],v)
    if gcd(q,p)!=1:continue
    assert dot(pos,v)>0 or dot(neg,v)>0
    found.append((q,p,h))
assert np==pts and sorted(found)==ls
rat=[]
for q,p,h in ls:
    d=a*(F(p,q)-r)+b*(F(h,q)-u)-z; rat.append(max(d/sp,-d/sm))
assert min(rat)>F(2395,1000)
print('PASS',k,Q,box,prod(y-x+1 for x,y in box),outer,pts,len(ls),'min ratio',float(min(rat)))
# Stitch the inherited smaller-scale proof to the new bound.
oldq=1139688307034066686122654499404718613400485815666141431682213091323282338737490244883
old3=old2=new3=new2=10**8
while old3<=Dlo*oldq**2/(4*E):old3*=2
while old2<oldq**2:old2*=2
assert min(old3,old2)>L*k
while new3<=Dlo*Q**2/(4*E):new3*=2
while new2<Q**2:new2*=2
print('windows',new3,new2,'factors',new3//old3,new2//old2)
```

## 5. Next
Rebuild a tighter polygon using refined observer supports (start with the common dual normal), rebase integer coordinates and quantify the next obstruction instead of enumerating exponentially growing old-coordinate boxes. Reuse raw and anchor inputs. Global unbounded separation, mother target B_fix,odd(32), inherited anchor exit and independent review remain open.
