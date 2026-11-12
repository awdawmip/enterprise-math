"""PREFIX-720: exact Gamma local transverse J and diagonal Theta curvature.
Science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json,hashlib
from pathlib import Path
N,D,W=189,768,1<<18
@lru_cache(None)
def inside(m,k,x):
    return 40*(m+1)*comb(m,k)*x**k*(W-x)**(m-k)>W**m
@lru_cache(None)
def wide(m,k):
    if k>m//2:return wide(m,m-k)
    mid=k*W//m
    assert inside(m,k,mid)
    if k==0: l0=l1=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            x=(lo+hi)//2
            if inside(m,k,x):hi=x
            else:lo=x
        l0,l1=lo,hi
    lo,hi=mid,W
    while hi-lo>1:
        x=(lo+hi)//2
        if inside(m,k,x):lo=x
        else:hi=x
    if 4*(lo-l1)>W:return True
    if 4*(hi-l0)<W:return False
    raise ValueError('ambiguous frozen width predicate')
rows=[{0:1}]
for m in range(1,N+1):
    new=defaultdict(int)
    for k,v in rows[-1].items():new[k]+=v;new[k+1]+=v
    rows.append({k:v for k,v in new.items() if wide(m,k)})
assert not rows[-1] and sum(map(len,rows[:N]))==9529
assert rows[25]=={k:comb(25,k) for k in range(1,25)}
L,Z=D**(N-1),2**(2*N-1)
R=L*L*Z
@lru_cache(None)
def tail(i):
    a,b=i,D-i; pa=[1];pb=[1]
    for _ in range(N):pa.append(pa[-1]*a);pb.append(pb[-1]*b)
    return tuple(sum(v*pa[k]*pb[n-k] for k,v in row.items())*D**(N-1-n)
                 for n,row in enumerate(rows[:N]))
@lru_cache(None)
def dtail(i):
    a,b=i,D-i;pa=[1];pb=[1]
    for _ in range(N):pa.append(pa[-1]*a);pb.append(pb[-1]*b)
    return tuple(sum(v*((k*pa[k-1]*pb[n-k] if k else 0)-
                        ((n-k)*pa[k]*pb[n-k-1] if n>k else 0))
                     for k,v in row.items())*D**(N-n)
                 for n,row in enumerate(rows[:N]))
@lru_cache(None)
def influence(j):
    terms=[(m,v) for m,v in enumerate(tail(j)) if v]
    a=[];h=[]
    for n in range(N):
        cs=[(m,v,comb(n+m,n)*2**(2*N-2-n-m)) for m,v in terms]
        a.append(L*Z-sum(v*c for m,v,c in cs))
        h.append(2*(n+1)*L*Z-sum((n+m+1)*v*c for m,v,c in cs))
    assert min(a)>0 and min(h)>0
    return a,h
@lru_cache(None)
def mu(i,j):
    ai,_=influence(j)
    return F(sum(tail(i))+sum(tail(j)),L)-F(sum(x*(L*Z-y) for x,y in zip(tail(i),ai)),R)
@lru_cache(None)
def ratio(i,j):
    a,h=influence(j);s=dtail(i)
    den=sum(x*y for x,y in zip(s,a))
    num=sum(x*y for x,y in zip(s,h))
    assert den>0
    return F(num,den)

@lru_cache(None)
def second_dtail(i):
    """Exact second derivative of s_n(p), scaled by L=D^(N-1)."""
    a,b=i,D-i
    pa=[1];pb=[1]
    for _ in range(N):
        pa.append(pa[-1]*a);pb.append(pb[-1]*b)
    return tuple(
        sum(v*((k*(k-1)*pa[k-2]*pb[n-k] if k>=2 else 0)
               -(2*k*(n-k)*pa[k-1]*pb[n-k-1] if 0<k<n else 0)
               +((n-k)*(n-k-1)*pa[k]*pb[n-k-2] if n-k>=2 else 0))
            for k,v in row.items())*D**(N+1-n)
        for n,row in enumerate(rows[:N])
    )

def run():
    x=88  # exactly p=z=11/96, interior to PREFIX719's (43/384,91/768)
    s, ds, dds=tail(x),dtail(x),second_dtail(x)
    a,h=influence(x)
    cross0=cross1=0
    for n in range(N):
        v0=v1=0
        for m in range(N):
            c=comb(n+m,n)*2**(2*N-2-n-m)
            v0+=ds[m]*c
            v1+=(n+m+1)*ds[m]*c
        cross0+=ds[n]*v0
        cross1+=ds[n]*v1
    P=sum(v*w for v,w in zip(ds,a))
    Q=sum(v*w for v,w in zip(ds,h))
    PP=sum(v*w for v,w in zip(dds,a))
    QQ=sum(v*w for v,w in zip(dds,h))
    assert P>0
    # All derivative numerators have the common scale L^2*Z.
    # mu_p=P/(L^2Z), M2_p=Q/(L^2Z).
    # mu_pp=PP/(L^2Z), M2_pp=QQ/(L^2Z).
    # mu_pz=-cross0/(L^2Z), M2_pz=-cross1/(L^2Z).
    j_num=P*(QQ+cross1)-Q*(PP+cross0)
    theta_num=(P*(QQ-cross1)-Q*(PP-cross0))*(L*L*Z)-4*P**3
    j_sha=hashlib.sha256(str(j_num).encode()).hexdigest()
    theta_sha=hashlib.sha256(str(theta_num).encode()).hexdigest()
    assert j_num>0
    assert theta_num<0
    den=L*L*Z
    assert j_num>=10_000_000*den*den
    assert -theta_num>=100*P*P*den
    # General Bernstein-derivative bounds on the 189 survivor rows:
    # |partial^r mu|<=N*376^r and |partial^r M2|<=N*(N+1)*376^r.
    # Hence |J_zp|,|J_zz|<=8*N*N*(N+1)*376^4.
    B=16*N*N*(N+1)*376**4
    assert B<3_000_000*10**12
    assert j_sha=='f9eab864317b8b68e16940ed539733265725445e8108de8c7075d4d18adc95d2'
    assert theta_sha=='c3cb0b08933d50689c97613e80cc6b53820dc8820e1c7f084cb6ec64e6d0e0b1'
    result={
      'schema':'PREFIX720_R6_LOCAL_TRANSVERSALITY_V1',
      'date':'2026-11-12',
      'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'model':'189-level frozen survivor plus independent Gamma maximum',
      'x':'11/96','diagonal_J_z_sign':'+',
      'diagonal_theta_prime_sign':'-',
      'J_z_certified_at_least':'10000000',
      'Theta_prime_certified_at_most':'-100',
      'explicit_square_radius':'1/1000000000000',
      'K_explicit_lower_in_square':'7000000',
      'exact_J_numerator_sha256':j_sha,
      'exact_theta_numerator_sha256':theta_sha,
      'J_numerator_digits':len(str(j_num)),
      'survivor_nonzero_coefficient_count':sum(map(len,rows[:N])),
      'mathematical_consequence':'There exists eps>0 with J(11/96,z)>0 for 11/96<z<11/96+eps, by continuity.',
      'scope':'One rational diagonal location and non-effective open wedge, not the entire surviving region',
      'status':'AUTHOR_EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED',
      'checker':'ALL_CHECKS_PASS PREFIX720-R6'
    }
    assert result['survivor_nonzero_coefficient_count']==9529
    Path(__file__).with_name('PREFIX720_R6_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ALL_CHECKS_PASS PREFIX720-R6',result['x'],result['J_numerator_digits'])

if __name__=='__main__':
    run()
