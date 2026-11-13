#!/usr/bin/env python3
"""Exact Fraction evidence: Stage311-B, finite checks only."""
from fractions import Fraction as F
from itertools import product

p0,p1=F(1,4),F(3,4)
p=(p0,p1)
r=F(9,400)
c=3*(F(3,4)-r)**2
ubar=F(51,5000)
M={
 (0,0,0):(63,1),(0,0,1):(21,3),(0,1,0):(21,3),(0,1,1):(7,9),
 (1,0,0):(9,7),(1,0,1):(3,21),(1,1,0):(3,21),(1,1,1):(1,63)
}
assert sum(a+b for a,b in M.values())==256
assert all(a>0 and b>0 for a,b in M.values())
def q(u): return F(9,128)*u+F(3,32)*u*u-F(1,8)*u**3
def g(u): return F(117,4096)*u-F(123,1024)*u*u+F(23,256)*u**3
E=q(ubar)
B=c*r/128
assert ubar<r
assert q(r)>E>F(9,20800)
assert g(ubar)<B
assert F(13,32)*E>B
L=[F(286443,160000),F(39243,160000),F(51557,160000),F(35643,160000)]
residual=[F(13,1024),F(3,1024),F(3,1024),F(13,1024)]
margin=[residual[k]-F(5,16)*r*L[k] for k in range(4)]
assert all(v>0 for v in margin)
BITS=list(product((0,1),repeat=3))
def bernpath(x,bits):
 k=sum(bits)
 return x**k*(1-x)**(3-k)
def tv(D,E):
 return sum(abs(D.get(k,F(0))-E.get(k,F(0))) for k in D.keys()|E.keys())/2
def path_distributions(changed=None):
 target_public={};comp_public={};target_tagged={};comp_tagged={}
 for h,(a,b) in M.items():
  j,w,y=h;t=(p0 if a>b else p1)
  if changed is not None and h==(1,0,0): t=p0+changed
  for s,weight in enumerate((a,b)):
   initial=F(weight,256)
   for bits in BITS:
    gkey=(w,y)+bits;tkey=(s,j,w,y)+bits
    tar=initial*bernpath(p[s],bits);cmp=initial*bernpath(t,bits)
    target_public[gkey]=target_public.get(gkey,F(0))+tar
    comp_public[gkey]=comp_public.get(gkey,F(0))+cmp
    target_tagged[tkey]=target_tagged.get(tkey,F(0))+tar
    comp_tagged[tkey]=comp_tagged.get(tkey,F(0))+cmp
 assert sum(target_public.values())==sum(comp_public.values())==1
 assert sum(target_tagged.values())==sum(comp_tagged.values())==1
 return tv(target_public,comp_public),tv(target_tagged,comp_tagged)
P0,Tstar=path_distributions()
assert P0==F(11,256)
assert Tstar==F(77,1024)
for u in (F(0),F(1,10000),F(1,100),F(51,5000)):
 pub,tag=path_distributions(u)
 assert pub==P0-q(u),(u,pub,P0-q(u))
 assert tag==Tstar+g(u),(u,tag,Tstar+g(u))
print('SOURCE_PAIRS=8; ORIGINAL_SOURCE_PATH_ATOMS=128; EXACT_FRACTION')
print('r=',r,'c_r=',c,'u_bar=',ubar)
print('epsilon_new=',E,'decimal=',format(float(E),'.15f'))
print('epsilon_old=',F(9,20800),'increase_ratio=',E/F(9,20800))
print('candidate_tagged_cost=',g(ubar))
print('universal_outside_radius_barrier=',B)
print('strict_barrier_gap=',B-g(ubar))
print('q(r)=',q(r),'all_four_public_sign_margins=',','.join(map(str,margin)))
print('MAP_PUBLIC=',P0,'MAP_TAGGED=',Tstar)
print('STAGE311B_NONLINEAR_TV_LOCALIZATION_EXACT_PASS')
