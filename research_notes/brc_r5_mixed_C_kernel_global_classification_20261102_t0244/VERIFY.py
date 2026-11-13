"""R5 exact all-real NO-GO for C_s=(1-s)*(A+B)/2+s*C.
Python 3 standard library; Fraction flow, polynomial identities and exact
32x12 tensor Bernstein certificate on (tau,s) in [0,1]^2.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

Z,H,O=F(0),F(1,2),F(1)
LR_BITS=tuple(product((0,1),repeat=5))
W_BITS=(1,0,1,0,0,0,1,0)
FACET_BITS=(1,0,0,0,1)

def lr_to_full(bits):
    p,q,r,k,l=bits
    return p,q,q,r,k,k,l,l

def observe(bits,tau,s):
    p,qn,qc,r,kn,kc,ln,lc=map(F,bits)
    tau,s=F(tau),F(s)
    assert Z<=tau<=O and Z<=s<=O
    assert all(Z<=x<=O for x in (p,qn,qc,r,kn,kc,ln,lc))
    out,mass=[Z,Z,Z,Z],[Z,Z]
    keys=0
    def key(mp,mq,ratio):
        nonlocal keys
        assert mp==ratio*mq,(mp,mq,ratio)
        keys+=1
    def end(mp,mq,a,t):
        assert mp>=Z and mq>=Z
        mass[0]+=mp;mass[1]+=mq
        if a=="P":out[0]+=mp
        else:out[1]+=mq
        out[2]+=t*mp;out[3]+=t*mq
    def L(mp,mq,l):
        key(mp,mq,F(12,5))
        end(mp*l,mq*l,"P",4)
        end(mp*(1-l),mq*(1-l),"Q",5)
    def K(mp,mq,k,l):
        key(mp,mq,F(8,5))
        end(mp*k,mq*k,"P",3)
        mp*=1-k;mq*=1-k
        end(mp/4,mq/2,"Q",4)
        L(mp*F(3,4),mq/2,l)
    def A(mp,mq,k,l):
        end(mp*F(3,5),mq/2,"Q",3)
        mp*=F(2,5);mq/=2
        end(mp/2,mq/2,"P",3)
        K(mp/2,mq/2,k,l)
    def B(mp,mq,l):
        end(mp/10,mq/8,"P",4)
        end(mp*F(3,10),mq*F(3,8),"Q",4)
        L(mp*F(3,5),mq/2,l)
    def C(mp,mq,k,l):
        end(mp*F(3,5),mq/2,"Q",3)
        K(mp*F(2,5),mq/2,k,l)
    def N(mp,mq,k,l):
        A(mp/2,mq/2,k,l)
        B(mp/2,mq/2,l)
    def JN(mp,mq):
        key(mp,mq,F(2))
        end(mp*qn,mq*qn,"P",2)
        N(mp*(1-qn),mq*(1-qn),kn,ln)
    for _ in range(2):
        mp=mq=F(1,8)
        key(mp,mq,O)
        end(mp*p,mq*p,"P",1)
        mp*=1-p;mq*=1-p
        end(mp/2,mq*F(3,4),"Q",2)
        JN(mp/2,mq/4)
    JN(F(1,4),F(1,8))
    mp,mq=F(1,2),F(5,8)
    key(mp,mq,F(4,5))
    end(mp*r,mq*r,"Q",1)
    mp*=1-r;mq*=1-r
    end(mp*(1-tau/2),mq*(1-tau/5),"Q",2)
    jp,jq=mp*tau/2,mq*tau/5
    key(jp,jq,F(2))
    end(jp*qc,jq*qc,"P",2)
    jp*=1-qc;jq*=1-qc
    N(jp*(1-s),jq*(1-s),kc,lc)
    C(jp*s,jq*s,kc,lc)
    assert mass==[O,O],mass
    assert keys>=4
    return tuple(out)

def add(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,Z)+v
    return {k:v for k,v in out.items() if v}
def neg(a):return {k:-v for k,v in a.items()}
def mul(a,b):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            ix=i+k,j+l
            out[ix]=out.get(ix,Z)+v*w
    return {k:v for k,v in out.items() if v}
def at(a,t,s):
    return sum((v*F(t)**i*F(s)**j for (i,j),v in a.items()),Z)
def interpolated(bits):
    oo,to,os,ts=[observe(bits,*v) for v in ((Z,Z),(O,Z),(Z,O),(O,O))]
    return [{(0,0):a,(1,0):b-a,(0,1):c-a,(1,1):d-b-c+a}
            for a,b,c,d in zip(oo,to,os,ts)]
# n is an integer-polynomial supporting direction for each (tau,s).
N=(
    {(2,1):F(-120),(1,1):F(-1125),(2,0):F(360),(1,0):F(2010),(0,0):F(1650)},
    {(2,1):F(-240),(1,1):F(-1656),(2,0):F(720),(1,0):F(720)},
    {(2,1):F(-75),(1,1):F(225),(2,0):F(555),(1,0):F(1380),(0,0):F(825)},
    {(2,1):F(192),(1,1):F(18),(2,0):F(-1104),(1,0):F(-1764),(0,0):F(-660)}
)
def dot(n,obs):
    ans={}
    for x,y in zip(n,obs):ans=add(ans,mul(x,y))
    return ans
def bernstein(poly):
    # 3rd degree in tau, 2nd degree in s.
    assert all(i<=3 and j<=2 for i,j in poly)
    return {(i,j):sum((v*F(comb(i,k),comb(3,k))*F(comb(j,l),comb(2,l))
                       for (k,l),v in poly.items() if k<=i and l<=j),Z)
            for i in range(4) for j in range(3)}

def verify():
    facet=dot(N,interpolated(lr_to_full(FACET_BITS)))
    witness=interpolated(W_BITS)
    assert witness==[
        {(0,0):F(61,160),(1,0):F(1,4),(0,1):Z,(1,1):Z},
        {(0,0):F(11,16),(1,0):F(-1,8),(0,1):Z,(1,1):Z},
        {(0,0):F(43,20),(1,0):Z,(0,1):Z,(1,1):Z},
        {(0,0):F(125,64),(1,0):Z,(0,1):Z,(1,1):Z}]
    assert add(dot(N,witness),neg(facet))=={(2,1):F(33,4),(1,1):F(495,4)}
    count=positive=0
    active=[]
    for bits in LR_BITS:
        slack=add(facet,neg(dot(N,interpolated(lr_to_full(bits)))))
        vals=bernstein(slack)
        assert all(v>=Z for v in vals.values()),(bits,slack,vals)
        count+=len(vals)
        positive+=sum(v>Z for v in vals.values())
        if not slack:active.append("".join(map(str,bits)))
    assert (count,positive)==(384,264),(count,positive)
    regressions=((F(1,2),F(1,100)),(F(1,2),H),(F(4,5),F(3,5)),
                 (F(3,7),F(2,3)),(F(1,17),F(1,19)),(O,O))
    for t,s in regressions:
        n=[at(p,t,s) for p in N]
        def linear(v):return sum((a*b for a,b in zip(n,v)),Z)
        maxlr=max(linear(observe(lr_to_full(b),t,s)) for b in LR_BITS)
        assert maxlr==at(facet,t,s)
        assert linear(observe(W_BITS,t,s))-maxlr==F(33,4)*s*t*(t+15)
    print("EXACT_TWO_LAW_FLOW_AND_ALL_SHARED_TIME_LR_KEYS=PASS")
    print("ALL_32_LR_VERTICES_BILINEAR_INTERPOLATION=PASS")
    print("DUAL_NORMAL_INTEGER_POLYNOMIAL_DEGREES=tau2_s1")
    print("SIGNED_WITNESS_MINUS_EXACT_LR_SUPPORT=(33/4)*s*tau*(tau+15)")
    print("NONNEGATIVE_BERNSTEIN_COEFFICIENTS=",count,
          "positive=",positive,"active_zero_slack=",",".join(active))
    print("EXTRA_EXACT_RATIONAL_OBSERVATION_CHECKS=",6*33)
    print("FOR_ALL_tau,s_IN_[0,1]_SIGN_CERTIFIED=PASS")
    print("FOR_tau*s>0_CONVEX_HULLS_ARE_SEPARATED=PASS")
    print("BOUNDARY_EQUALITY_AT_tau*s=0_IS_ANALYTIC_MARKOVIZATION_NOT_COMPUTATION")
    print("STATUS=AUTHOR_EXACT_CHECKED; UNREVIEWED; NOT_NATIVE_ADMITTED")
    print("PASS_EXACT_R5_MIXED_THIRD_KERNEL_GLOBAL_CLASSIFICATION")

if __name__=="__main__":verify()
