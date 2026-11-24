#!/usr/bin/env python3
"""Exact finite arithmetic accompanying the R1/R2 prime-support lower bounds."""
from math import gcd, lcm, prod
from itertools import combinations
import hashlib,json

P=(7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417)
Q0=(5,13,19,73)
A2=9807947978443488306255509703402695727949968778703073231931137913705883712843
S2=11356718000553566643685496313583434507970452519839503606327232707476034989690
S1=S2//(433*38737)
A1=A2%S1
A3=191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3=398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
A=38737
E=(577,487824887233)
C=(181,631,23311,54001,18837001,29247661)
D=(87211,246241,262657,279073)
T=E+C+D
U9=(
29,43,1429,5419,3361,15790321,88959882481,
211,421,86171,106681,122921,152041,664441,1564921,7416361,47392381,146919792181,1041815865690181,
193,1153,6337,22253377,38941695937,278452876033,33975937,138991501037953,
61681,4562284561,168692292721,469775495062434961,
92737,649657,40388473189,77158673929,118750098349,
209924353,4261383649,24929060818265360451708193,
8369281,394783681,4278255361,46908728641,750016890283777055704738227247474485366338380663681,
3457,816769,18446744069414584321,1562985901350085709953,1422346738975853644793916289,
2017,5153,25629623713,54410972897,1538595959564161,
127681,1130641,755667361,84179842077657862011867889681,54169520413224311136354324156824071681)
assert S2==S1*433*A and S3==S2*prod(T) and A3%S2==A2
assert len(set(U9))==59 and len(set(T))==12 and gcd(prod(U9),S3)==1
assert gcd(A1,prod((3,11,61,331,37,109)))==prod((3,11,61,331,37,109))
assert A2%433==0
B=prod((1<<(420*e))-1 for e in range(33,65))
# Every 1<=e<=64 divides a maximal multiplier in 33..64.
assert all(any(m%e==0 for m in range(33,65)) for e in range(1,65))
def crt(a,m,b,n):
    return a + m*((b-a)*pow(m,-1,n)%n), m*n

def strip(b,v):
    while (g:=gcd(b,v))>1:
        b//=g
    return b

def hexsha(n):
    return hashlib.sha256(n.to_bytes((n.bit_length()+7)//8,'big')).hexdigest()

def make_pair(fiber,target,plan):
    m,a=(S1,A1) if fiber=='R1' else (S2,A2)
    a0=a1=a
    n=m
    for q,w in plan:
        assert B%q==0
        r=pow(2,-(16+18*w),q)
        a0,_=crt(a0,n,0 if q==target else r,q)
        a1,n=crt(a1,n,r,q)
    M=strip(B,n)
    a0,_=crt(a0,n,0,M)
    a1,n=crt(a1,n,0,M)
    a0+=n; a1+=n
    assert gcd(a0,M)==gcd(a1,M)==M
    assert (a0-a1)%(n//target)==0 and a0%target==0 and a1%target!=0
    assert a0%m==a1%m==a
    return a0,a1,n

def order(q):
    r=2%q; d=1
    while r!=1:
        r=2*r%q; d+=1
        assert d<=26880
    return d

def zeroes(a,q,period):
    r=pow(a,2,q); out=0
    for j in range(period):
        if r==1: out|=1<<j
        r=2*r%q
    assert r==pow(a,2,q)
    return out

def verify(fiber,target,plan):
    a0,a1,n=make_pair(fiber,target,plan)
    qs=tuple(dict.fromkeys(P+Q0+((A,) if fiber=='R2' else ())+tuple(q for q,_ in plan)))
    period=lcm(*(order(q) for q in qs))
    allmask=(1<<period)-1
    ons=offs=0
    active_on={}
    active_off={}
    for q in qs:
        active_on[q]=zeroes(a1,q,period)
        ons|=active_on[q]
        active_off[q]=zeroes(a0,q,period)
        offs|=active_off[q]
    assert ons==allmask
    on_cost=off_cost=None
    if target in HIGH:
        assert offs==allmask
        def exact(a, available):
            old=0
            for q in P: old|=a[q]
            masks=[v for q,v in a.items() if q not in P and v&~old]
            for k in range(len(masks)+1):
                for subset in combinations(masks,k):
                    u=old
                    for mask in subset: u|=mask
                    if u==allmask: return k
        on_cost=exact(active_on,len(qs)-len(P))
        off_cost=exact(active_off,len(qs)-len(P))
        assert (on_cost,off_cost)==(9,10)
        # The common observed/available repair is essential off but not on.
        assert (active_off[REPAIR]>>2048)&1
    else:
        assert offs!=allmask
    return {'fiber':fiber,'q':target,'period':period,'off_uncovered':period-offs.bit_count(),
            'finite_costs_certified_by_cutoff': [on_cost,off_cost] if target in HIGH else None,
            'modulus_bits':n.bit_length(),'on_sha256':hexsha(a1),'off_sha256':hexsha(a0)}

HIGH={870031:315,1765891:630,2521:1260}
REPAIR=1325521
def main():
    rows=[]
    for q in E: rows.append(verify('R2',q,tuple(zip(E,(0,2)))))
    for group,phases in ((C,(0,1,3)),(D,(0,1,2))):
        for q in group:
            ps=[q]+[r for r in group if r!=q][:2]
            rows.append(verify('R2',q,tuple(zip(ps,phases))))
    for q in (433,A): rows.append(verify('R1',q,((433,0),(A,1))))
    from math import isqrt
    assert all(REPAIR%p for p in range(2,isqrt(REPAIR)+1)) and order(REPAIR)==2520
    for q,d in HIGH.items():
        assert all(q%p for p in range(2,isqrt(q)+1))
        assert order(q)==d and d//gcd(d,36)==35
        rows.append(verify('R2',q,((181,0),(631,3),(29,5),(43,3),(q,21),(REPAIR,56))))
    assert gcd(prod(HIGH), S3*prod(U9))==1
    m3=prod(U9); m2=m3*prod(T)*prod(HIGH); m1=m2*433*A
    print(json.dumps({'mask_bits':B.bit_length(),'necessary_support':[(len(U9),m3.bit_length()),(len(U9)+len(T)+len(HIGH),m2.bit_length()),(len(U9)+len(T)+len(HIGH)+2,m1.bit_length())],'rows':rows},indent=2))

if __name__=='__main__':main()
