"""R5 activated-L gate: exact minimax support-gap certificate (Python stdlib only)."""
from fractions import Fraction as F
from itertools import product

R = (F(1), F(3, 2), F(2), F(3))

def kernel(ell):
    return (F(1, 4), ell, F(1, 2) - F(3, 2)*ell,
            F(1, 4) + ell/2)

def observer(bits, ell, stop_error, continue_error, lr=False):
    if lr:
        x,u,z,v = bits
        bits=(x,x,u,u,u,z,z,v,v)
    x0,x1,u0,u1,ub,z0,z1,v0,v1 = bits
    l0,l1=ell
    x,z=F(x0+x1,2),F(z0+z1,2)
    w=F(x0*u0+x1*u1,2)
    s=F(ub,4)+w/16
    E=l0*x0*v0+l1*x1*v1
    # Previous immutable R5 observer for equal 1/8 L error at both L actions.
    eP=F(1,8)+F(ub,8)+(1-z)/8
    eQ=F(1,8)+F(ub,8)+(1-z)/4
    TP=F(3,2)+x+z/2-s+F(3,16)*E
    TQ=F(3,2)+x/2+z-s+E/8
    # New L error corrections, Q-flow ell_i*x_i/8, P-flow 3*ell_i*x_i/16.
    for xi,vi,li,ai,bi in zip((x0,x1),(v0,v1),ell,stop_error,continue_error):
        correction=li*xi*(ai-F(1,8)+vi*(bi-ai))
        eP+=F(3,16)*correction
        eQ+=F(1,8)*correction
    return (eP,eQ,TP,TQ)

def J(point):
    eP,eQ,TP,TQ=point
    return 14*eP-19*eQ+2*TP-4*TQ

def positive(x):
    return max(F(0),x)

def support_formula(ell,a,b):
    A=[2*(ai-F(1,8)) for ai in a]
    B=[2*(bi-ai)-1 for ai,bi in zip(a,b)]
    C=sum((li*Ai for li,Ai in zip(ell,A)),F(0))
    D=sum((li*Bi for li,Bi in zip(ell,B)),F(0))
    P=sum((li*positive(Bi) for li,Bi in zip(ell,B)),F(0))
    full=(-53 + 1 + C + P)/8
    lr=(-53 + positive(C+positive(D)))/8
    return full,lr,C,D,P


cases=[
    ("inherited", (F(1,12),F(1,6)), (F(1,8),F(1,8)), (F(1,8),F(1,8))),
    ("worst_closed_errors",(F(1,12),F(1,6)),(F(0),F(0)),(F(0),F(0))),
    ("worst_close_boundary",(F(333,1000),F(333,1000)),(F(0),F(0)),(F(0),F(0))),
    ("signed_source_sensitive",(F(1,12),F(1,6)),(F(1,8),F(3,4)),(F(7,8),F(1,4))),
    ("positive_source_sensitive",(F(1,10),F(1,5)),(F(1,20),F(9,10)),(F(19,20),F(1,10))),
    ("offset_source_sensitive",(F(1,100),F(3,10)),(F(1,3),F(1,10)),(F(1,5),F(4,5))),
    ("all_ones",(F(1,12),F(1,6)),(F(1),F(1)),(F(1),F(1))),
]
for name,ell,a,b in cases:
    for li in ell:
        k=kernel(li)
        assert 0<li<F(1,3)
        assert all(z>0 for z in k)
        assert sum(k)==1
        assert sum(ri*ki for ri,ki in zip(R,k))==2
        assert sum(ri*ki/2 for ri,ki in zip(R,k))==1
    assert all(0<=t<=1 for t in a+b)
    fullpoints=[observer(bits,ell,a,b) for bits in product((0,1), repeat=9)]
    lrpoints=[observer(bits,ell,a,b,True) for bits in product((0,1), repeat=4)]
    assert len(fullpoints)==512 and len(lrpoints)==16
    assert all(all(F(0)<=ep<=1 for ep in point[:2]) for point in fullpoints+lrpoints)
    fmax=max(map(J,fullpoints)); lmax=max(map(J,lrpoints))
    fformula,lformula,C,D,P=support_formula(ell,a,b)
    assert (fmax,lmax)==(fformula,lformula),(name,fmax,lmax,fformula,lformula)
    delta=fmax-lmax
    lower=(1-sum(ell)/4)/8
    assert delta>=lower>F(5,48)
    if name.startswith('worst_'):
        assert delta==lower
    # Explicit deterministic witness: x_i=1, u_i=1, uB=0, z_i=1;
    # v_i=1 exactly when B_i>0.
    v=[int(2*(bi-ai)-1>0) for ai,bi in zip(a,b)]
    witness=observer((1,1,1,1,0,1,1,v[0],v[1]),ell,a,b)
    assert J(witness)==fmax
    assert delta/F(39)>F(5,1872)
    print(f"{name}: full={fmax} lr={lmax} gap={delta} sharp_parameter_min={lower} "
          f"source_ell={tuple(map(str,ell))}; 512/16 deterministic policies")

# Finite deterministic support = all-real support because the policy observer
# is multi-affine in each per-information-set Bernoulli choice in this DAG.
# Exact formulas + closed-domain 0<=errors<=1 prove the universal assertion.
print("PASS_EXACT_R5_ACTIVATED_L_ALL_ERROR_KERNEL_MINIMAX_NO_GO")
