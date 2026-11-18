"""Independent integer verification in normal coordinates and common-frame ports."""
from collections import Counter, defaultdict
from math import gcd, isqrt
import json


def h(q,r):
    return max(abs(2*q+r),abs(q+2*r),abs(q-r))


def norm(q,r):
    return q*q+q*r+r*r


def rotate(p):
    q,r=p
    return -r,q+r


def points(s):
    # Normal coordinates x=q-r, y=q+2r, x == y (mod 3).
    for x in range(-s,s+1):
        lo=max(-s,-s-x)
        hi=min(s,s-x)
        for y in range(lo+(x-lo)%3,hi+1,3):
            yield (2*x+y)//3,(y-x)//3


def ell(z,m):
    return (z[0]+m*z[1])%(m*m-m+1)


def prime(n):
    return n>1 and all(n%d for d in range(2,isqrt(n)+1))


def original_label(q,r,k):
    n=0
    for j in range(k):
        a,b=q%2,r%2
        n+=(a+2*b)*4**j
        u,v=(q-a)//2,(r-b)//2
        q,r=u+v,-u
    return n


def check_ports(m, expected_outer=None):
    a=(m-1)//3; K=m*m-m+1
    outer=set(); inner=set(); old=defaultdict(list)
    for q in range(a+1,2*a+1):
        z=(q,m-2*q)
        y=(z[0]-m,z[1]+1)
        for _ in range(6):
            assert h(*z)==m and h(*y)==m-1
            assert ell(z,m)==ell(y,m)
            assert z not in outer and y not in inner
            outer.add(z);inner.add(y)
            old[z[0]%m,z[1]%m].append((z,y))
            z,y=rotate(z),rotate(y)
    if expected_outer is not None: assert outer==expected_outer
    assert len(inner)==len(outer)==2*(m-1)
    assert len(old)==m-1
    units={1,-1,m,-m,m-1,1-m}
    for pair in old.values():
        assert len(pair)==2
        (z,y),(t,v)=pair
        assert norm(*z)==norm(*t)
        assert (ell(y,m)-ell(v,m))%K in {u%K for u in units}
        assert gcd(ell(y,m)-ell(v,m),K)==1
    return old


def main():
    sites=0
    for s in range(81):
        states=set(points(s))
        assert len(states)==s*s+s+1-2*(s%3==1)
        for q,r in states:
            Q=norm(q,r); H=h(q,r)
            assert H*H==4*Q-3*min(q*q,r*r,(q+r)**2)
            assert 3*Q<=H*H<=4*Q
        if s:
            assert sum(h(*z)==s for z in states)==2*s+{-1:0,0:0,1:-2,2:2}[s%3]
        sites+=len(states)
    assert set(points(0))==set(points(1))=={(0,0)}
    for m in range(2,81):
        K=m*m-m+1; reps={ell(z,m) for z in points(m-1)}
        assert len(reps)==sum(1 for _ in points(m-1))
        assert set(range(K))-reps==({K//3,2*K//3} if m%3==2 else set())
        if m%3==1:
            check_ports(m,{z for z in points(m) if h(*z)==m})
        for u in range(-4,5):
            for v in range(-4,5):
                if not(u or v):continue
                q,r=m*u+v,-u+(m-1)*v
                assert norm(q,r)==K*norm(u,v) and h(q,r)>=2*m-1
                assert (h(q,r)==2*m-1)==(norm(u,v)==1)
    details={}
    for m in (4,16,64,256,1024,4096,16384,65536):
        old=check_ports(m)
        details[str(m)]=len(old)
    # Preserve original labels alongside norm and capacity readouts.
    odd_pairs=check_ports(256)
    raw=sorted({original_label(q,r,8) for q,r in odd_pairs})
    labels=[n for n in raw if prime(n)]
    assert len(labels)==14
    witness=[(z,y) for pair in odd_pairs.values() for z,y in pair if original_label(*z,8)==15017]
    assert len(witness)==2 and all(norm(*z)==17707 for z,y in witness)
    contrast=[]
    for pair in odd_pairs.values():
        z,y=pair[0]
        n=original_label(*z,8); Q=norm(*z)
        if prime(n)!=prime(Q):contrast.append([n,Q])
    assert contrast
    return {'normal_coordinate_site_visits':sites,'count_s_range':[0,80],
            'quotient_m_range':[2,80],'missing_classes_m8':[19,38],
            'port_matching_edges':details,'matching_edges_sum':sum(details.values()),
            'original_prime_labels_m256':labels,'label_norm_opposite_primality_example':min(contrast),
            'result':'PASS'}


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
