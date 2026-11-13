"""Exact rational regression for supercritical K3 clock hull rigidity.
Uses only the Python standard library, enumerates genuine deterministic policies.
"""
from fractions import Fraction as F
from itertools import product

S = ('C', 'I', 'BJ', 'IJ')
C = (F(1,8),F(1,6),F(1,16),F(3,32))
P = (F(1,3),F(1,2),F(3,5),F(4,5))
Q = (F(2,3),F(1,4),F(3,7),F(5,8))


def observer(x, y, i, stages, r, v):
    weights = (C[0],(1-x)*C[1],y*C[2],i*C[3])
    d = weights[2]+weights[3]
    m = tuple(weights[j] if stages[j]>=1 else F(0) for j in range(4))
    s = tuple(F(2,3)*m[j] if stages[j]>=2 else F(0) for j in range(4))
    u = tuple(s[j] if stages[j]==3 else F(0) for j in range(4))
    ep = F(107,128)-F(21,128)*x+d/4-sum(s)/2+sum(P[j]*s[j] for j in range(4))/8
    eq = F(13,64)+F(3,64)*x-d/2+sum(s)/8+sum(Q[j]*s[j] for j in range(4))/32
    tp = 3+sum(m)+F(3,2)*sum(s)+sum(r[j]*u[j] for j in range(4))
    tq = 3+sum(m)/2+F(3,8)*sum(s)+sum(v[j]*u[j] for j in range(4))/4
    return (ep,eq,tp,tq)


def enumerate_full(r,v):
    for x in (F(0),F(1)):
        for y in (F(0),F(1)):
            for i in sorted({F(0),1-x}):
                # dedup x=1,i=0 duplicate without changing extrema
                if x == 1 and i != 0:
                    continue
                for stages in product(range(4),repeat=4):
                    yield observer(x,y,i,stages,r,v),(x,y,i,stages)


def enumerate_lr(r,v):
    for x,y in product((F(0),F(1)),repeat=2):
        for stage in range(4):
            yield observer(x,y,(1-x)*y,(stage,)*4,r,v),(x,y,(1-x)*y,(stage,)*4)


def support(vec, n):
    return sum(vec[j]*n[j] for j in range(4))


def analytic_full(r,v,n):
    a,b=n[2:]
    g1=a+b/2
    g2=2*a+3*b/4
    g3=[(2+F(2,3)*r[j])*a+(F(3,4)+v[j]/6)*b for j in range(4)]
    return 3*(a+b)+sum(C[j]*max(0,g1,g2,g3[j]) for j in range(4))


def trial(title,r,v,n,expected_stage):
    assert all(0 < z < 1 for z in (*r,*v))
    assert all(v[j] >= F(3,2)*r[j] for j in range(4))
    thresholds_mu=tuple((9+2*v[j])/(8*(3+r[j])) for j in range(4))
    alpha=tuple(v[j]/(4*r[j]) for j in range(4))
    nu=tuple((3+2*v[j])/(4*(3+2*r[j])) for j in range(4))
    assert all(m >= F(3,8) for m in thresholds_mu)
    assert len(set(alpha if expected_stage=='alpha' else nu))>1
    full=list(enumerate_full(r,v))
    lr=list(enumerate_lr(r,v))
    assert len(full)==1536 and len(lr)==16
    hF=max(support(z,n) for z,_ in full)
    hL=max(support(z,n) for z,_ in lr)
    assert hF==analytic_full(r,v,n)
    assert hF>hL
    witness, strategy = next((z,pol) for z,pol in full if support(z,n)==hF)
    gap=hF-hL
    dist=gap/sum(abs(q) for q in n)
    assert support(witness,n)-hL==gap
    assert dist>0
    print(f'{title}: mu={thresholds_mu}; alpha={alpha}; nu={nu}')
    print(f'  n={n}; h_FULL={hF}; h_LR={hL}; gap={gap}; ||n||_1={sum(abs(q) for q in n)}; dist_inf_lower={dist}')
    print(f'  FULL witness={witness}; policy={strategy}; FULL_count={len(full)} LR_count={len(lr)}')
    return gap,dist

if __name__=='__main__':
    print('R5 K3 supercritical clock hull rigidity: exact Fraction enumeration')
    r=(F(1,10),F(1,5),F(3,10),F(2,5))
    # Fixed alpha=1/2, distinct nu. Source 2x change under positive b normal.
    trial('COMMON_ALPHA_DISTINCT_NU',r,tuple(2*x for x in r),(F(0),F(0),-F(2,7),F(1)),'nu')
    # Fixed nu=3/10, distinct alpha. Source 2x change under positive a normal.
    trial('COMMON_NU_DISTINCT_ALPHA',r,tuple(F(3,10)+F(6,5)*x for x in r),(F(0),F(0),F(3,5),-F(1)),'alpha')
    # Fully uniform reference, where every clock normal supports equally.
    uniform_r=(F(1,5),)*4; uniform_v=(F(2,5),)*4
    all_full=list(enumerate_full(uniform_r,uniform_v)); all_lr=list(enumerate_lr(uniform_r,uniform_v))
    normals=((F(0),F(0),F(1),F(0)),(F(0),F(0),-F(2,7),F(1)),
             (F(0),F(0),F(3,5),-F(1)),(F(0),F(0),-F(1),-F(1)))
    for n in normals:
        assert max(support(z,n) for z,_ in all_full)==max(support(z,n) for z,_ in all_lr)
    print('UNIFORM_REFERENCE: 4 selected signed clock directions PASS (not a full 2D hull computation)')
    print('PASS_EXACT_R5_K3_SUPERCRITICAL_ALPHA_NU_RIGIDITY')
