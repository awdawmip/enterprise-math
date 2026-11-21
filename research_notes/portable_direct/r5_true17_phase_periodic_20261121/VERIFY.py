#!/usr/bin/env python3
"""Exact primitive-17 R5 genuine-event residue and next derivative.
No floating point. Independently decomposes three overlap events into
(a214,b215,u216-218,v219-221) grouped complete homogeneous polynomials.
Scientific model: frozen price range p=214..314, S0,S1,S2,S3,S4.
"""
import json, sys
P=17
Z=(0,)*P
ONE=(1,)+(0,)*(P-1)
def plus(*xs):return tuple(sum(row[i] for row in xs) for i in range(P))
def scale(a,k):return tuple(x*k for x in a)
def shift(a,n):
 n%=P
 return a[-n:]+a[:-n] if n else a
def mul(a,b):
 c=[0]*P
 for i,ai in enumerate(a):
  if ai:
   for j,bj in enumerate(b):
    if bj:c[(i+j)%P]+=ai*bj
 return tuple(c)
def red(a):return [x-a[-1] for x in a[:-1]]
def root_factor(prices):
 w,d=ONE,Z
 for p in prices:
  w,d=plus(w,scale(shift(w,p),-1)),plus(d,scale(shift(d,p),-1),scale(shift(w,p),-p))
 return w,d
def h_groups(prices,m):
 h=[ONE]+[Z]*(m-1);dh=[Z]*m
 for p in prices:
  hh=[ONE]+[Z]*(m-1);dd=[Z]*m
  for k in range(1,m):
   hh[k]=plus(h[k],shift(hh[k-1],p))
   dd[k]=plus(dh[k],shift(dd[k-1],p),scale(shift(hh[k-1],p),p))
  h,dh=hh,dd
 return h,dh

def leading_period_certificate():
    # (1-t^17)/[(1-t) prod_{r=10..14}(1-z^r t)]
    # = prod_{r in 1..16 excluding 10..14}(1-z^r t), degree 11.
    coeff=[ONE]+[Z]*11
    degree=0
    for residue in [r for r in range(1,17) if r not in {10,11,12,13,14}]:
        for j in range(degree+1,0,-1):
            coeff[j]=plus(coeff[j],scale(shift(coeff[j-1],residue),-1))
        degree+=1
    W0,_=root_factor(range(214,219))
    vals=[red(mul(W0,c)) for c in coeff]+[[0]*16]*5
    assert len(vals)==17 and all(any(v) for v in vals[:12]) and all(not any(v) for v in vals[12:])
    return vals

def compute(m):
 assert m>=1
 h,dh=h_groups([216,217,218],m);v,_=h_groups([219,220,221],m)
 hprod=[[mul(h[u],v[j]) for j in range(m)] for u in range(m)]
 P0=DP0=P1=P2=P01=P02=P12=P012=Z
 # E0 alone: 214,215,216,217,218
 for u in range(m):
  for a in range(m-u):
   for b in range(m-u-a):
    powq=214*a+215*b
    term=shift(h[u],powq)
    P0=plus(P0,term)
    DP0=plus(DP0,shift(dh[u],powq),scale(term,powq))
 # E1,E2 alone (215 or 214 absent)
 for u in range(m):
  for j in range(m-u):
   for a in range(m-u-j):
    x=hprod[u][j]
    P1=plus(P1,shift(x,214*a))
    P2=plus(P2,shift(x,215*a))
 # 2- and 3-mask genuine intersections across 8 variable prices
 for u in range(m):
  for a in range(m-u):
   for b in range(m-u):
    c0=(a+b+u < m)
    q=214*a+215*b
    for j in range(m-u):
     c1=a+u+j < m
     c2=b+u+j < m
     if not ((c0 and c1) or (c0 and c2) or (c1 and c2)):
      continue
     x=shift(hprod[u][j],q)
     if c0 and c1:P01=plus(P01,x)
     if c0 and c2:P02=plus(P02,x)
     if c1 and c2:P12=plus(P12,x)
     if c0 and c1 and c2:P012=plus(P012,x)
 S0=set(range(214,219));S1={214,216,217,218,219,220,221};S2=set(range(215,222))
 W0,DW0=root_factor(sorted(S0));W1,_=root_factor(sorted(S1-{221}));W2,_=root_factor(sorted(S2-{221}));W,_=root_factor(sorted((S0|S1|S2)-{221}))
 r0=mul(W0,P0);dr0=plus(mul(W0,DP0),mul(DW0,P0))
 bracket=plus(mul(W1,P1),mul(W2,P2),scale(mul(W,plus(P01,P02,P12)),-1),mul(W,P012))
 dra=plus(dr0,scale(bracket,-221))
 # Other group E4 is independent; E3 has >=4 factors vanishing at primitive17.
 # S4=296..312: all 17 residues, unique multiple of17 is p306.
 # P4(zeta17)=ceil(m/17), R4(zeta17)=0, DR4(zeta17)=-5202 ceil(m/17).
 d4=-5202*((m+16)//17)
 rtotal=r0
 drtotal=plus(dra,scale(plus(ONE,scale(r0,-1)),d4))
 return {'m':m,'R_A':red(r0),'DR_A':red(dra),'DR_total':red(drtotal),'P4_at_zeta':(m+16)//17,'R_total_is_zero':all(x==0 for x in red(rtotal)), 'DR_total_is_zero':all(x==0 for x in red(drtotal))}
if __name__=='__main__':
 vals=[int(x) for x in sys.argv[1:]] or list(range(13,18))+list(range(30,35))
 rows=[compute(m) for m in vals]
 leading=leading_period_certificate()
 for row in rows:
  assert row['R_A']==leading[(row['m']-1)%17]
 if vals[:5]==list(range(13,18)):
  assert rows[0]['DR_total']==[-13328,-8840,-11084,-13073,-15062,-17442,-15691,-13872,-4845,5763,12614,19448,22287,19431,12818,8160]
 print(json.dumps({'status':'PASS','basis':'Z[z]/Phi17, z^17=1','model':'genuine individual event incidence','algorithm':'grouped h_u/h_v; no scalar union collapse','leading_period_certificate_m1_17':leading,'result':rows,'review':'NOT_REVIEWED'},indent=2))
