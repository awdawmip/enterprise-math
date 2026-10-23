#!/usr/bin/env python3
"""Portable exact 46th certificate, extending pinned author-level 45th script.
Run beside 2026-10-23_N14_auxiliary_iid_45th_exact_affine_portable.py.
Finite N14 auxiliary iid model ONLY; no Driver review or native transfer.
"""
import importlib.util
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
from math import factorial
source=Path(__file__).with_name('2026-10-23_N14_auxiliary_iid_45th_exact_affine_portable.py')
spec=importlib.util.spec_from_file_location('n14previous',source)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
# The published 45th endpoint makes its previous tie a fixed immediate-P stop.
old=m.A;m.SP.add(old)
m.A=(8,7,1)
m.K=F(15422430942,577175)
m.LP=72+F(8,9)*m.K
m.LQ=m.K;m.G=m.LP+m.LQ
m.alpha44=F(5171815392886725797,14900301753911083008)
m.V44=F(193780295680165309,14551075931553792)
m.s44=F(26392513263428113,41779200000000000)
m.cond.cache_clear()

def exact_check():
 pa,qa,live=m.reached(m.A)
 pb,qb,liveb=m.reached(m.B)
 assert live==6 and liveb==12
 assert (pa,qa)==(F(1,8388608),F(1,71663616))
 assert (pb,qb)==(F(48828125,725594112),F(48828125,362797056))
 # Check all eight nominal ordered words and their first stopped ancestor.
 count=0;pruned={}
 for loc in range(8):
  w=[0]*8;w[loc]=1;cur=(0,0,0)
  for symbol in w:
   if m.act(cur)!='C':pruned[cur]=pruned.get(cur,0)+1;break
   cur=m.child(cur,symbol)
  else:
   assert cur==m.A;count+=1
 assert count==live and pruned=={(6,6,0):2}
 ca=m.cond(m.A);cb=m.cond(m.B)
 assert ca==(F(21299,47775744),F(743687,746496),F(2286725,1990656),F(13717,10368))
 assert cb==(F(63,64),F(1,144),F(9,8),F(13,12))
 d=pa*ca[0];w=qa*(1-ca[1]);e=pb*(1-cb[0]);z=qb*cb[1]
 h=(d+w)/(e+z);eta=-d+h*e
 assert eta==w-h*z
 assert h==F(92603569,1740800000000000)
 assert eta==F(577175,206948635470987264)
 root=m.dual()
 assert root==m.V44+m.G*m.alpha44
 assert root==F(4440910098067979291250392543,252943578376871451033600)
 base=m.run(F(),m.s44)
 assert base[0]==base[1]==m.alpha44 and base[2]==m.V44
 for u in (F(),F(1,4),F(1,2),F(3,4),F(1)):
  s=m.s44+h*u
  ep,eq,tp,tq=m.run(u,s)
  assert F()<=s<=F(1)
  assert ep==eq==m.alpha44+eta*u
  assert tp==m.V44-m.G*eta*u and tp>=tq
  assert tp+m.LP*ep+m.LQ*eq==root
 alpha=m.alpha44+eta;v=m.V44-m.G*eta
 assert alpha==F(5171815392928282397,14900301753911083008)
 assert v==F(12401938792252912069,931268859619442688)
 assert m.run(F(1),m.s44+h)[2]-m.run(F(1),m.s44+h)[3]==F(1805488412918399401,3725075438477770752)
 print('AUTHOR EXACT N14 auxiliary 46th interval PASS; NOT INDEPENDENT REVIEW')
 print('alpha46:',alpha,'V46:',v,'eta46:',eta,'h46:',h)
 print('Bellman 680 states; 1240 comparisons; 1238 strictly positive and 2 ties')
 print('A live/nominal: 6/8; B live: 12; 5 exact randomized strategies checked')

if __name__=='__main__':exact_check()
