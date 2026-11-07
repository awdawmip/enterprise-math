#!/usr/bin/env python3
"""Exact rational certification of R5 K3 homogeneous-source observer equality.
The universal real theorem is proved separately in RESEARCH.md.
"""
from fractions import Fraction as F
from itertools import product

CAP = (F(1, 8), F(1, 6), F(1, 16), F(3, 32))
ZERO = F(0)
ONE = F(1)

def observer(x, y, i, z, t, u, r, v, p, q):
    """All inputs rational; FULL has individual z,t,u, LR has common ones."""
    w = (CAP[0], (1-x)*CAP[1], y*CAP[2], i*CAP[3])
    d = w[2] + w[3]
    M = [w[s]*z[s] for s in range(4)]
    Z = [F(2,3)*M[s]*t[s] for s in range(4)]
    U = [Z[s]*u[s] for s in range(4)]
    sm, sz, su = sum(M), sum(Z), sum(U)
    ep = F(107,128)-F(21,128)*x+d/4-(F(1,2)-p/8)*sz
    eq = F(13,64)+F(3,64)*x-d/2+(F(1,8)+q/32)*sz
    tp = 3+sm+F(3,2)*sz+r*su
    tq = 3+sm/2+F(3,8)*sz+v*su/4
    return (ep, eq, tp, tq), (w, d, sm, sz, su)

def common_policy(x,y,i,z,t,u):
    w = (CAP[0], (1-x)*CAP[1], y*CAP[2], i*CAP[3])
    d = w[2]+w[3]
    weight = sum(w)
    M = sum(w[s]*z[s] for s in range(4))
    Z = sum(F(2,3)*w[s]*z[s]*t[s] for s in range(4))
    U = sum(F(2,3)*w[s]*z[s]*t[s]*u[s] for s in range(4))
    yl = d/(CAP[2]+CAP[3]*(1-x))
    zl = M/weight
    tl = F(3,2)*Z/M if M else ZERO
    ul = U/Z if Z else ZERO
    assert all(ZERO <= a <= ONE for a in (yl,zl,tl,ul))
    return yl,zl,tl,ul

def stage_bits(j):
    return (int(j>=1),int(j>=2),int(j==3))

def full_det_observer(x,y,i,st,pars):
    bits=[stage_bits(j) for j in st]
    return observer(x,y,i,tuple(a[0] for a in bits),tuple(a[1] for a in bits),tuple(a[2] for a in bits),*pars)[0]

def lr_det_observer(x,y,j,pars):
    a,b,c=stage_bits(j)
    return observer(x,y,(1-x)*y,(a,)*4,(b,)*4,(c,)*4,*pars)[0]

def sum_vectors(points):
    return tuple(sum(pt[k]*weight for pt,weight in points) for k in range(4))

def verify(pars):
    full_count=0
    bound_eight=0
    four_stage_support=0
    for x,i in ((ZERO,ZERO),(ZERO,ONE),(ONE,ZERO)):
      for y in (ZERO,ONE):
        for stages in product(range(4), repeat=4):
          full_count+=1
          target=full_det_observer(x,y,i,stages,pars)
          z=tuple(F(int(j>=1)) for j in stages)
          t=tuple(F(int(j>=2)) for j in stages)
          u=tuple(F(int(j==3)) for j in stages)
          yl,zl,tl,ul=common_policy(x,y,i,z,t,u)
          own,_=observer(x,yl,(1-x)*yl,(zl,)*4,(tl,)*4,(ul,)*4,*pars)
          assert target==own,(x,y,i,stages,target,own)
          w=(CAP[0],(1-x)*CAP[1],y*CAP[2],i*CAP[3]); wt=sum(w)
          points=[]
          for j in range(4):
            pi=sum(w[s] for s in range(4) if stages[s]==j)/wt
            if pi:
              four_stage_support+=1
              for ycorner,frac in ((ZERO,ONE-yl),(ONE,yl)):
                if frac:
                  points.append((lr_det_observer(x,ycorner,j,pars), pi*frac))
          assert 1 <= len(points) <= 8
          assert sum(weight for _,weight in points)==ONE
          assert all(weight>=ZERO for _,weight in points)
          assert sum_vectors(points)==target,(x,y,i,stages)
          bound_eight=max(bound_eight,len(points))
    assert full_count==1536
    sample_count=0
    samples=[
      (F(1,3),F(2,5),F(1,4),(F(1,5),F(2,3),F(3,4),F(1,3)),(F(3,5),F(1,4),F(2,5),F(7,8)),(F(1,7),F(1,2),F(2,3),F(4,5))),
      (F(3,5),F(1,7),F(2,5),(ZERO,ONE,F(3,4),F(1,3)),(ONE,ZERO,F(2,5),F(1,4)),(ZERO,ONE,F(1,2),F(3,4))),
      (ONE,ONE,ZERO,(ONE,ONE,ONE,ONE),(ONE,ONE,ONE,ONE),(ONE,ONE,ONE,ONE)),
      (ZERO,ZERO,ZERO,(ZERO,)*4,(ZERO,)*4,(ZERO,)*4),
      (ZERO,ONE,ONE,(ONE,)*4,(ONE,)*4,(ONE,)*4),
    ]
    for x,y,i,z,t,u in samples:
      assert ZERO<=i<=ONE-x
      full,_=observer(x,y,i,z,t,u,*pars)
      yl,zl,tl,ul=common_policy(x,y,i,z,t,u)
      lr,_=observer(x,yl,(ONE-x)*yl,(zl,)*4,(tl,)*4,(ul,)*4,*pars)
      assert full==lr
      sample_count+=1
    print('parameters',tuple(str(x) for x in pars),'full_det',full_count,'max_nonzero_vertices',bound_eight,'behavioral_nonvertex',sample_count,'stage_terms',four_stage_support,'PASS')
    return full_count,sample_count

if __name__=='__main__':
    examples=[
      (F(1,5),F(2,5),F(1,2),F(1,2)),
      (F(2,5),F(4,5),F(1,3),F(2,3)),
      (F(1,3),F(1,3),F(1,2),F(1,2)),
      (F(4,5),F(1,5),F(2,3),F(1,4)),
      (F(2,3),F(3,4),F(7,10),F(1,4)),
      (F(1,7),F(6,7),F(1,9),F(8,9)),
    ]
    totals=[verify(row) for row in examples]
    print('TOTAL_FULL_DETERMINISTIC_CERTIFICATES',sum(x for x,_ in totals))
    print('TOTAL_NONVERTEX_POLICY_CHECKS',sum(y for _,y in totals))
    print('PASS_EXACT_R5_K3_HOMOGENEOUS_REAL_IMAGE_EQUALITY')
