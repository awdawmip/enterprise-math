#!/usr/bin/env python3
"""Exact all-endpoint S23/AV auxiliary capacity plateaux 20..200 certificate.
All decisions use integer arithmetic or stdlib Fraction with rigorous remainder.
The soundness of the finite critical-cell reduction is proved in PLATEAUX20_200.md.
"""
from fractions import Fraction as F
Q=10**26
LO=545569623581288298975349314
HI=LO+1

def logarithm_bounds(z):
  s=F(0); p=z
  for m in range(45):
    s+=2*p/(2*m+1);p*=z*z
  return s,s+2*p/(91*(1-z*z))
a,b=logarithm_bounds(F(1,3));c,d=logarithm_bounds(F(1,9));e,f=logarithm_bounds(F(1,15))
assert F(LO,Q)<(3*a-f)/(d+f)
assert (3*b-e)/(c+e)<F(HI,Q)
def enc(A,B):return (A*Q+B*(LO if B>=0 else HI),A*Q+B*(HI if B>=0 else LO))
EL,EU=enc(-431,79); TL,TU=enc(-60,11); GL,GU=enc(371,-68);DL,DU=enc(2074774,-380295)
assert 0<DL<DU<EL<EU and TL>4800*EU and GL>6*EU

def get_witnesses(n):
  ww=[]
  for i in range(1,n+1):
    ai=i*DL//EU
    assert ai*EU<i*DL and i*DU<(ai+1)*EL
    L=380295*i+79*ai; K=2074774*i+431*ai
    dl,du=enc(K,-L)
    assert 0<dl<du<EL
    ww.append((i,ai,L,K,dl,du))
  return ww

def cuts(raw,upper):return sorted({0,upper+1}|{x for x in raw if 0<x<=upper})

def check(i):
  w=get_witnesses(i); V,K=w[-1][2:4];prev=w[-2][2];H=V+510;M=K+V-prev-1
  assert EU*(H+79)<( (EU*(H+79)//Q)+1)*Q
  bmax=EU*(H+79)//Q + 1
  narrow=[]
  for beta in range(-bmax+1,bmax):
    if not beta:continue
    qlo=abs(beta)*TL//EU;qhi=abs(beta)*TU//EL
    assert qlo==qhi,(i,beta,qlo,qhi)
    aa=-qlo if beta>0 else qlo+1
    dv,dj=79*aa+11*beta,431*aa+60*beta
    wl,wu=enc(-dj,dv)
    assert 0<wl<wu<EL
    cost=max(max(dv,0)+max(dj,0),max(-dv,0)+max(-dj,0))
    if cost<=H:
      if not ((dv>0 and dj>0) or (dv<0 and dj<0)):
        print('MIXED_SIGN',i,beta,dv,dj,cost)
        return None
      narrow.append((beta,aa,dv,dj,cost,wl,wu))
  blocked={}
  for ix,ai,L,K,dl,du in w:
    items=[]
    for beta,aa,dv,dj,cost,wl,wu in narrow:
      if K == -dj and L == -dv:items.append((beta,dv,dj,cost))
      else:
        assert du<wl or wu<dl,(i,ix,beta)
        if wu<dl:items.append((beta,dv,dj,cost))
    blocked[ix]=items
  vc=cuts([L+1 for ix,ai,L,K,dl,du in w]+[-dv for _,_,dv,dj,cost,wl,wu in narrow if dv<0],V)
  jc=cuts([K+1 for ix,ai,L,K,dl,du in w]+[-dj for _,_,dv,dj,cost,wl,wu in narrow if dj<0],H)
  sc=cuts([K+L-M for ix,ai,L,K,dl,du in w]+[H-cost+1 for _,_,dv,dj,cost,wl,wu in narrow if dv>0],H)
  feasible=0;usage=set()
  for a0,b0 in zip(vc,vc[1:]):
    vl,vh=a0,b0-1
    for a1,b1 in zip(jc,jc[1:]):
      jl,jh=a1,b1-1
      for a2,b2 in zip(sc,sc[1:]):
        sl,sh=a2,b2-1
        if max(vl+jl,sl)>min(vh+jh,sh):continue
        feasible+=1
        found=False
        for ix,ai,L,K,dl,du in w:
          if vh>L or jh>K or sl<K+L-M:continue
          if any((sh<=H-cost if dv>0 else vl>=-dv and jl>=-dj) for beta,dv,dj,cost in blocked[ix]):continue
          usage.add(ix);found=True;break
        if not found:
          print('UNCOVERED',i,vl,vh,jl,jh,sl,sh,'H',H,'M',M,'narrow',len(narrow))
          return None
  for m in range(1,7):
    L=V+68+79*m;KK=K+371+431*m
    al,au=enc(KK,-L)
    assert 0<al<au<GL and KK>H and KK+L-(V+1)<=M
  assert V+68+79*6>=H
  left=H*Q//LO+1;right=HI*H//Q+1
  assert LO*left>H*Q and right*Q>HI*H and max(left,right)<=M
  return (i,H,M,len(narrow),bmax,feasible,len(usage),[e[:5] for e in narrow])

if __name__=='__main__':
 count=0
 max_cells=0
 max_narrow=0
 for i in range(20,201):
   ret=check(i)
   assert ret is not None, ("coverage_failed", i)
   ix,H,M,n,bmax,cells,usage,items=ret
   assert ix == i
   count+=1; max_cells=max(max_cells,cells); max_narrow=max(max_narrow,n)
   if i<=23 or i%10==0:
     print("CERTIFIED_PLATEAU", ix, "H", H, "M", M, "narrow", n, "beta_bound", bmax, "critical_cells", cells, "witnesses_used", usage, flush=True)
 assert count==181 and H==76068753 and M==415385600
 print("PASS_S23_AV_ANALYTIC_PLATEAUX_20_TO_200", "certified",count,"last_H",H,"last_N",M,"max_critical_cells",max_cells,"max_narrow_types",max_narrow)
