#!/usr/bin/env python3
"""R749SPI: exact rational sanity checks for a human-proved upper-fiber homothety.
No finite sample is used as the universal proof; see companion theorem note.
"""
import json
from fractions import Fraction as Q
M=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if ((k&m).bit_count()&1)==0 else -1 for m in M) for k in range(16))

def law(t,s,h=0,u=0,v=0,w=0,z=0):
    return tuple((1+sum((a*b for a,b in zip((t,s,h,u,v,w,z),r)),Q(0)))/16 for r in W)

def tv(p,q):return sum((abs(x-y) for x,y in zip(p,q)),Q(0))/2

def check():
    # Universal polynomial kernel of the (++ fixed-mass subtraction) proof.
    # M++ - 4(t+s-1) - (M+-+M-+) = 3(h-(t+s-1)).
    for t,s,h in [(Q(1,2),Q(1,2),Q(0)),(Q(3,5),Q(3,5),Q(9,25)),(Q(4,5),Q(3,5),Q(3,5))]:
        Mpp=1+t+s+h;Mpm=1+t-s-h;Mmp=1-t+s-h
        assert Mpp-4*(t+s-1)-Mpm-Mmp==3*(h-(t+s-1))
    Pstar=law(Q(1),Q(1),Q(1))
    assert sum(Pstar)==1 and min(Pstar)>=0
    tests=0
    for tp,sp in [(Q(1,2),Q(1,2)),(Q(3,5),Q(2,5)),(Q(4,5),Q(1,5)),(Q(1),Q(0))]:
      # Strict boundary t'+s'=1; the pair sources P+, P- and midpoint are legal.
      p0=law(tp,sp)
      pplus=law(tp,sp,Q(0),1-sp,1-sp,1-tp,1-tp)
      pminus=law(tp,sp,Q(0),sp-1,sp-1,tp-1,tp-1)
      # H has the other allowed h extremum when tp>=sp.
      H=law(tp,sp,1-tp+sp)
      for p in [p0,pplus,pminus,H]:
        assert sum(p)==1 and min(p)>=0
        for alpha in [Q(1),Q(4,5),Q(1,2),Q(1,10)]:
          nu=1-alpha
          t=nu+alpha*tp;s=nu+alpha*sp
          mix=tuple(nu*a+alpha*b for a,b in zip(Pstar,p))
          assert sum(mix)==1 and min(mix)>=0
          # Recover the boundary moments and complete source from its full law.
          assert sum(x*W[k][0] for k,x in enumerate(mix))==t
          assert sum(x*W[k][1] for k,x in enumerate(mix))==s
          pulled=tuple((x-nu*y)/alpha for x,y in zip(mix,Pstar))
          assert pulled==p
          tests+=1
    # Exact scale identity obtained from the R749SPF point (3/5,3/5):
    # rho=8/25, rho_cal=18/55. At the boundary midpoint these
    # divide by alpha=4/5 to rho=2/5, rho_cal=9/22.
    assert Q(4,5)*Q(2,5)==Q(8,25)
    assert Q(4,5)*Q(9,22)==Q(18,55)
    assert Q(9,22)-Q(2,5)==Q(1,110)
    diagonal={}
    for r in (Q(1,2),Q(3,5),Q(3,4),Q(1)):
      a=2*(1-r);rho=4*(1-r)/5;rcal=9*(1-r)/11
      assert rho==a*Q(2,5) and rcal==a*Q(9,22)
      assert rcal-rho==(1-r)/55
      diagonal[str(r)]={'rho':str(rho),'rho_cal':str(rcal),'gap':str(rcal-rho)}
    return {'schema':'R749SPI_UPPER_FIBER_HOMOTHETY_V1','status':'PASS',
      'method':'exact rational law mixing and inverse; polynomial identity; prior exact point substitution',
      'exact_mix_cases':tests,'diagonal':diagonal,
      'universal_proof':'separate algebraic inequalities and simplex retraction in theorem note',
      'source_point':'R749SPF @ (3/5,3/5), free=8/25, calibrated=18/55',
      'native_transfer':'OPEN','review':'AUTHOR_EXACT_NOT_REVIEWED'}

if __name__=='__main__':print(json.dumps(check(),sort_keys=True,indent=2))
