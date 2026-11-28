# PREFIX-1149 — Refined joint section and observer-adapted unimodular coordinates

2026-11-28. EM-DIRECT-780BBE / TASK_RESEARCH, author analytic argument and exact rational auxiliary computation, conditional Stage46 application, NOT_REVIEWED. Independent unclaimed research; no shared task mutation. Retain the frozen Source P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d; this is auxiliary spectral algebra, not a native spatial coordinate system. Global entries verified against canonical main 18d1b87e1639ac6765bdcb00d8a909658f0aba49. Original own session status and recovery metadata confirmed active custody and no runs, owner read r6-20261128-1159-owner-read consumed by its original receipt (still running at this note's drafting). Prior 249-entry evidence manifest verified locally.

## Exact input and scope
Predecessor: 4d1a6dcf25ba4920f56a185337de1803e42a82f9:research_notes/portable_direct/2026-11-28_r6_prefix1148_raw_resolution_refinement.md (blob 14c5e52aa4d24acbabe2db3cec1553e903e43536). Reuse its verified raw-resolution refined 15 rows, 12 shared generators, signed error payments and Stage46 constants, and PREFIX-1147 section f0d630b278e0c72be9841adc0f6df9f705eeaf52. Exact input files are in the PREFIX-1148 execution archive (249-item manifest); no new raw moments or anchor computation. The independent verifier also reconstructs the 13 refined rows from previous exact coefficients and raw integers, confirming the 12 payments of 14 and one of 466, with all common generators unchanged. The inherited analytic anchor exit and independent mathematical review remain pending.

## Global section
For m,C,e and n as in PREFIX-1148, put a=-G(n[0]aj+n[1]dj), b=G n[1]am, z=n.m, S=sum_j |n.C_j|+sum_i |n_i|e_i. True shifted parameters x=rho-r,y=c-u must satisfy |a x+b y-z|<=S. The new section P is the intersection of the previous certified outer section and all selected inequalities. This does not require rounded outer models to be nested. Apply the predecessor separation normal and every nonzero sparse cofactor normal from seven coordinates including 0 or 1, cancelling the first six columns; pay every other generator and every error. 4552 applications including duplicate, 39 effective cuts, 25 final vertices. Widths 6.529117480054215e-110 and 3.1579443554981587e-109 (about 2342 and 2323 times narrower than PREFIX-1147). The 39 active supports alone reproduce the same exact polygon via all boundary-pair intersections and recursive determinants rather than Bareiss clipping.

At L>=10^114 the possible (p/q,h/q) lies in HP=P+(r,u)+[-K/L0^2,0]x[0,H/L0], L0=10^114. Monotonicity is componentwise in the signed payments. The previous coordinate basis yields 0 integer points at Q=10^72, 3*10^72 and 10^73 after 17430,159488,1774185 outer slices respectively.

## Observer-adapted coordinate lemma
Let HP be a nondegenerate convex polygon of rational parameter pairs. Choose three vertices t1,t2,t3 maximizing the absolute triangle determinant. For any point t of HP, the barycentric coordinates lambda_i of t relative to this triangle satisfy |lambda_i|<=1: replacing vertex i with t multiplies the determinant by lambda_i, and the maximum over a polygon of the absolute affine function is attained at a vertex. Thus for any integer linear form f(t)=a+b*t[0]+c*t[1], |f(t)|<=sum_i |f(t_i)|. This gives an exact positive-definite auxiliary Gram form sum_i f(t_i)^2 on integer coefficient triples, with max_{HP}|f|<=sqrt(3)*sqrt(sum_i f(t_i)^2); the inverse bound sqrt(sum_i f(t_i)^2)<=sqrt(3)*max_{HP}|f| also follows. No real/native spatial identification is used.

Use exact rational Gram-Schmidt and LLL row operations (delta=3/4, round nearest, subtract integral multiples and swap) on the prior integer basis, under this embedding. After 16 iterations the new integer V is in the compact fixture. Because every row operation is unimodular and the computed exact inverse W is integral with VW=I, no arithmetic information is lost. LLL is a selection heuristic for a useful basis; proof of completeness depends only on the actual verified V,W, not on any LLL quality bound. No floating decisions. The exact coordinate box follows by extremizing q*(a+b*x+c*y) over the vertices and q endpoints [q0,Q]; this is sufficient because it is affine separately in q and (x,y). Transform every edge inequality to a linear inequality in n=V(q,p,h). Integer interval slicing is exact, or simply exhaust the final small box. All coordinates retained. The old basis required 1,774,185 outer slices at Q=10^73, new basis has one outer slice at that Q; this counts outer iterations, not wall-clock speed, and excludes preprocessing. The 16 iterations use exact arithmetic and maximal triangle search among the polygon vertices.

## Results
New basis at Q=10^73: box [(0,0),(0,0),(0,1)], 1 outer slice, no points. Q=3*10^73: [(0,0),(0,2),(-2,3)], 3 outer slices, no points. Q=10^74: [(0,2),(-2,6),(-8,11)], 27 outer slices, 39 integer points and 30 primitive relations (gcd(q,p)=1). Independently exhaust all 540 coordinate triples with exact rational support edges, obtaining identical points and primitive relations. Hence under inherited Stage46 and anchor assumptions, for L>=10^114:
b-a >= q >= 53102590994133180630926292345110267863622958364367639094454561109869586225.
First not-excluded dyadic window starts (same inherited curvature formula): 1.8170968107390172e142 triple; 4.763410263543689e147 sqrt pair. Continuous integer endpoint 4.72478e43 unchanged.

## Full bounded fiber
All 30 primitive candidates have exact rational witnesses for the refined 15-row affine outer model at zero scale error. For U=[C,diag(e)], use the 15 pivot indices and 12 free indices in the verifier. Free numerators in the compact fixture are in ascending (q,p,h) order, denominator 10^12, found with floating LP only to propose witnesses. Solve the pivot equations exactly and verify all 15 identities and all 27 coefficient bounds. Minimum slack 1-max|z_i|=0.017424661288406626 displayed, exactly >17/1000 for all 30. Smallest candidate slack 0.3444890948869193. Positive diagonal implies full row rank, so all 30 are strictly interior. This establishes an information limit of the refined affine model alone; it does not establish membership in the old fiber at zero scale error or actual nonlinear realizability. Further directions in the same model alone cannot exclude these candidates. Next: compare the actual final grid error (13 units of rounding) to structural remainder; increase G independently with exact recomputation of row centers and generators, scale point rows rigorously, test the 30 candidates before another global scan. Alternative: target the full shared coefficient relation. Mother target B_fix,odd(32) and unbounded final separation remain open.

## Compact exact certificate and reproduction
Use the prior execution archive, put the following decoded fixture in fixture1149_compact.json. Its SHA256 is 8b3efa6c817b49be83a3e413fbe045fc400995fd757607e9caab5099d1f6ca23. It contains only the 39 cofactor index patterns, new integer basis and 30 sets of free witness numerators. No credentials. The independent compact verifier below uses only the Python standard library and the already verified prior inputs. The full execution archive also includes the Bareiss clipping, exact LLL, full independent row reconstruction, LP witness proposal, exact witnesses, and logs. Reproduce the predecessor section/row certificates first if their author check is not being reused.

```python
import base64,zlib,hashlib
b64="eNqdmMuuGDcIht8l6xnJBgy4D9JNlEUXXTaqellVffd+THqZmXSsUXKk6PzGeDCGHzh/fPj5h99++/GXz79++O7jx7bpNjbfcut96/JpY6VvwqrV+gnXrrjhvOF5w73dF/p94b9P2l3F7ip2VzlsOu/4e+G6I+8L877Q2/2QWrntOflH78bq3Vi9G6v/2NbuC/2+cFXJu0reVfKuMu875n3H+Xr6P9cbt4DQr0LEvjrHvjrnnwteV/KrlfnvSr+F46ftw/cVpuLSJMaMpjJnb008NHv2pmluM6YpGruOGOKqOaZENpvZRjTXIc3FTdTTfWxhHjaH6BiWbU4LbWxoZqVorWs0w5xdbZr1IX0Y+9WadwuO62bOB6IN62qbe6SwKWfHlp5i0kIke+9uno1/0sa2d2uJfGrDZksVNW/Rh/LF1tN0Ttd67R0LJHMOG4h6n9mnzO45xbOO5+tdot7Vm04fPgWbsnPkTBzD5bWOiFTD7m2XkVg0uYSGmfDJZtLnCDQy+DLX9FEO//z7Twc17NiY5SHu0zYfY/Q220DtCva3oiUKfFE38748UNznVJWuQ8tPvHHrPKuI6XZF3yZaIq/3aE2tTHk+8QzKyKExkuAIvLxd0TPY34p2G0S5BT7J3IwAmjgpZK00CEFi30bw6mUjAeCVFXO27Yq+TbREuJHQlN4J4cWJZ4CRkyQgezxZIBRI2h6kx/Dc9qvsgl6LgoclL6CIxEOp3smTkKkrrTMoRxKvjcQi8eJLkP+HnsH+VrTDCiEtVSGebXgM4/7QzFLJZXyhIIli2d16kFSQGpS3PYP9rWiJSNlB/hJ9vjoRzpZULjbzsBFRXZN4rRi5oGewvxVBxbz1zOmQKr7zyg6qiS2VArYlJgJ2rtZoLwKFeUfI2KhILkX2wCvY34qWKHJQh0TGXB5oVJ2gQHWvFoBnp0zwY3Lk/Ev0WqTwsnY/2I5vO6WNHKJKrbTO4PCiUcMpUpTTCpczegb7WxGltGozbGGUYHKAooqLxlqJajqiHp0eAhu5VRAh3LaC+DV6LYJnOh0FvUjyhhR8zKSYt1xpnUGxY5A5TeuCdaJE1GXpNTjxKrugtyKKCs1TEfKgROeET8pkWyudACZW++JWkTy5mdDSkEFKxapKe5Fd0GuROo9ILXTCkI1daN5Mj0h91jqDCsdZNwyaLxuyXdEz2N+KEjZxKgvFjz6hkadEZs+Vyp78wmVg8x5HV0rPR6wkT1w97xk9g/2taBeNaK06TVgZbxrOqdxZ6SjdeRuEA3SKiTBkpzIjcylOgiDpUqH66vQusgt6LaLLVXoXskWPtgxedmaC4sZnrTM4HjphTPphoroq/Bk9g/2tqNM7p3ea7cE0NTKZWMT7UmefpLJXLZp6NBO0donTjtlnu6JnsL8VBb30mD6bQyY4lBLMhJErFd6Sgofb40tvy3hg6dyBsQjO50mYcWCGXugqO6PXoi5JCjPctWrJKGv0DJULfaV1BkdvW4WJ20Fe1W6e0TPY34roUBUmq250bBaNdtXCUlY63GQwOCp1c36JRUwW2H8qTn4G+1vREuHGyaxwjKSLA+HS6jQHpFpuZEJj3g5CWLc3v++vBB7M37wyzddmk16C0B/5vH+v4V6EdjYq/mo4nzYbI28RzVv0WsS7FhdC2FWXk1l68m6uK6UzqKJHenurRoL42CFUmIBksnLxVXZBr0VV5aLe88jPqL+R8AXTWGmdwTG10IwptAP/jO2KnsH+ViTVKIi4MnCSFo2OMWC9WOkwFuLrWbNBHiZS/LCX/yZdunQmB4a/Xm9xkVz3LUQrpNrp9YMmaiwPdMZnhobwOFJEZiP/U4zBrGLnJXorYnz3+tOVakVmMEIPonPISucMjiT24iGpv6Ad05jA7swvxa5X2QW9Fqn0qDo3ennHzapEG+PRQukMjlicRiPnrRry7Yqewf5WpPV25GAVso2mgZbfheZ2pVM3iX4UcFL6059/AY9+xLM="
raw=zlib.decompress(base64.b64decode(b64))
assert hashlib.sha256(raw).hexdigest()=="8b3efa6c817b49be83a3e413fbe045fc400995fd757607e9caab5099d1f6ca23"
open("fixture1149_compact.json","wb").write(raw)
```

Save following as verify1149_compact.py. Locally executed SHA256 b11648310360d8a647d911d064b316fa9383ad48799ea5420bd51a237f87ebe4.
```python
from fractions import Fraction as F
from itertools import combinations,product
from math import ceil,floor,gcd
import json,runpy
R=runpy.run_path('verify1141_compact.py')
G,L,K,H,aj,am,dj,r,u,q0,hull,d0,solve,dot=[R[k] for k in ('G','L','K','H','aj','am','dj','r','u','q0','hull','d0','solve','dot')]
E=json.load(open('refine1148.json'));m,e,C=[E[k] for k in ('m','e','cols')]
B=json.load(open('fixture1149_compact.json'))
def edges(P):
 E=[(v-y,x-w,(v-y)*x+(x-w)*y) for (x,y),(w,v) in zip(P,P[1:]+P[:1])];assert all(a*x+b*y<=z for a,b,z in E for x,y in P);return E
def det(M):
 if not M:return 1
 return sum((-1)**i*x*det([row[:i]+row[i+1:] for row in M[1:]]) for i,x in enumerate(M[0]) if x)
I=edges([tuple(map(F,v)) for v in json.load(open('section1147.json'))['vertices']])
for p in B['patterns']:
 M=[[c[i] for i in p] for c in C[:6]];v=[(-1)**j*det([row[:j]+row[j+1:] for row in M]) for j in range(7)];g=gcd(*v);assert g
 n=[0]*15
 for i,x in zip(p,v):n[i]=x//g
 assert all(dot(n,c)==0 for c in C[:6]);a=-G*(n[0]*aj+n[1]*dj);b=G*n[1]*am;t=dot(n,m);s=sum(abs(dot(n,c)) for c in C)+sum(abs(x)*y for x,y in zip(n,e));I.extend([(a,b,t+s),(-a,-b,s-t)])
P=set()
for (a,b,c),(x,y,z) in combinations(I,2):
 d=a*y-b*x
 if d:
  v,w=(c*y-b*z)/d,(a*z-c*x)/d
  if all(i*v+j*w<=k for i,j,k in I):P.add((v,w))
P=hull(P);assert len(P)==25
width=[max(v[i] for v in P)-min(v[i] for v in P) for i in range(2)];assert width[0]<F(653,10**112) and width[1]<F(316,10**111)
HP=hull([(x+r-a,y+u+b) for (x,y),a,b in product(P,(0,K/L**2),(0,H/L))]);J=edges(HP)
V=B['V'];W=list(zip(*(solve(V,[int(j==i) for j in range(3)]) for i in range(3))));assert all(v.denominator==1 for w in W for v in w);assert all(dot(v,w)==(i==j) for i,v in enumerate(V) for j,w in enumerate(zip(*W)));W=[list(map(int,w)) for w in W]
Q=10**74;box=[]
for a,b,c in V:
 vals=[q*(a+b*x+c*y) for q,(x,y) in product((q0,Q),HP)];box.append((ceil(min(vals)),floor(max(vals))))
assert box==[(0,2),(-2,6),(-8,11)];pts=[];tested=0
for n in product(*(range(a,b+1) for a,b in box)):
 tested+=1;q,p,h=[dot(w,n) for w in W]
 if q0<=q<=Q and all(a*p+b*h<=z*q for a,b,z in J):pts.append((q,p,h))
lines=sorted(v for v in pts if gcd(v[0],v[1])==1);assert tested==540 and len(pts)==39 and len(lines)==30
q=lines[0][0];assert q==53102590994133180630926292345110267863622958364367639094454561109869586225
L3=L2=10**8
while L3<=d0*q*q/(4*400000):L3*=2
while L2<=q*q:L2*=2
U=C+[[e[i] if i==j else 0 for i in range(15)] for j in range(15)];piv=[0,1,2,3,4,5,15,16,19,20,22,23,24,25,26];free=[i for i in range(27) if i not in piv];A=[[U[j][i] for j in piv] for i in range(15)];assert len(B['nums'])==len(lines);slacks=[]
for (q,p,h),v in zip(lines,B['nums']):
 x,y=F(p,q)-r,F(h,q)-u;T=[-G*aj*x,G*(am*y-dj*x)]+[F(0)]*13;z=[F(0)]*27
 for i,j in zip(free,v):z[i]=F(j,10**12)
 rhs=[T[i]-m[i]-sum(z[j]*U[j][i] for j in free) for i in range(15)]
 for i,j in zip(piv,solve(A,rhs)):z[i]=j
 assert all(m[i]+sum(z[j]*U[j][i] for j in range(27))==T[i] for i in range(15));slack=1-max(map(abs,z));assert slack>F(17,1000);slacks.append(slack)
print('PASS compact',len(P),*[float(v) for v in width],tested,len(pts),len(lines),lines[0][0],float(min(slacks)),float(L3),float(L2))
```

Actual executed terminal output:
```
PASS compact 25 6.529117480054215e-110 3.1579443554981587e-109 540 39 30 53102590994133180630926292345110267863622958364367639094454561109869586225 0.017424661288406626 1.8170968107390172e+142 4.763410263543689e+147
```
