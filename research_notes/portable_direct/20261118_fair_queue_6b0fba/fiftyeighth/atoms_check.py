"""Replay the round-8 generator and verify signed slot counts on the actual height box."""
from array import array
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd, isqrt
from pathlib import Path
import json


HEIGHTS = (1000, 1500, 2000)
SOURCE_SHA = "398899655f04b5a50758bbb7eb2207cd19fe900b79d1ec7f84afecad8f6b54e1"


def factor_sieve(bound):
    # Store a smallest prime divisor of composites; untouched n>=2 are prime.
    factors = array("I", [0]) * (bound+1)
    for p in range(2, isqrt(bound)+1):
        if not factors[p]:
            for n in range(p*p,bound+1,p):
                if not factors[n]:
                    factors[n] = p
    # Compute the actual oriented Gaussian prime by searching integer legs.
    roots = array("I",[0]) * (bound+1)
    for u in range(2,isqrt(bound)+1):
        upper = min(u-1,isqrt(bound-u*u))
        for v in range(1,upper+1):
            n=u*u+v*v
            if n%4==1 and not factors[n]:
                assert not roots[n]
                roots[n]=v*pow(u,-1,n)%n
    return factors,roots


def pack(wp,wm,gp,gm,ram):
    assert 0<=max(wp,wm,gp,gm)<16
    return 1 + wp + 16*wm + 256*gp + 4096*gm + 65536*ram


def slot(b,a):
    return (b-1)*(b-2)//2+a-1


def from_norm(b,a,factors,roots):
    n=a*a+b*b
    ram=int(n%2==0)
    if ram:
        n//=2
    wp=wm=gp=gm=0
    while n>1:
        p=factors[n] or n
        slope=roots[p]
        assert slope>0 and p%4==1
        plus=(a-b*slope)%p==0
        assert plus!=((a+b*slope)%p==0)
        n//=p
        excess=0
        while n%p==0:
            n//=p
            excess+=1
        if plus:
            wp+=1
            gp+=excess
        else:
            wm+=1
            gm+=excess
    return wp,wm,gp,gm,ram


def row_stats(h,counts):
    total=sum(counts.values())
    wp,wm,gp,gm,ram=[sum(k[i]*v for k,v in counts.items()) for i in range(5)]
    hist=Counter()
    excess_hist=Counter()
    for (u,v,p,m,_),num in counts.items():
        hist[u+v]+=num
        excess_hist[p,m]+=num
    return dict(height=h, atoms=total, plus_slots=wp, minus_slots=wm, signed_slots=wp+wm,
                positive_excess=gp, negative_excess=gm, valuation_l1=wp+wm+gp+gm,
                odd_odd_atoms=ram, all_simple_splits=excess_hist[0,0],
                slots_by_size=dict(sorted(hist.items())),
                omega_means=[str(Fraction(num,total)) for num in (wp,wm)])


def local_residues(p,u,v):
    # Work modulo p^2. Enumerate every possible value of the unit b, test the
    # four residue lines a/b for valuation >=1 or >=2, and remove (0,0) mod p.
    m=p*p
    slope1=v*pow(u,-1,p)%p
    w,z=u*u-v*v,2*u*v
    slope2=z*pow(w,-1,m)%m
    plus1=minus1=plus2=minus2=0
    for b in range(m):
        for a in range(m):
            if a%p==0 and b%p==0:
                continue
            right=(a-b*slope1)%p==0
            left=(a+b*slope1)%p==0
            assert not (right and left)
            plus1+=right
            minus1+=left
            plus2+=(a-b*slope2)%m==0
            minus2+=(a+b*slope2)%m==0
    size=p**4-p**2
    assert plus1==minus1==size//(p+1)
    assert plus2==minus2==size//(p*(p+1))
    return dict(prime=p,primitive_classes=size,each_first_valuation=plus1,
                each_second_valuation=plus2)


def overlap_check(H):
    B=2*H*H
    factors,_=factor_sieve(B)
    pis={}
    for u in range(2,isqrt(B)+1):
        for v in range(1,min(u-1,isqrt(B-u*u))+1):
            n=u*u+v*v
            if n%4==1 and not factors[n]:
                pis[n]=(u,v)
    C=Fraction(1)
    for p in pis:
        C*=Fraction(p-1,p+1)
    # List vectors by their associated units modulo Gaussian units, both signs
    # retained; height is not used to generate them.
    catalogue=sorted(pis)
    vectors=[]
    def walk(index,n,x,y):
        if n!=1:
            out=[]
            for a,b in ((x,y),(x-y,x+y)):
                for _ in range(4):
                    if 0<b<a:
                        out.append((a,b))
                    a,b=-b,a
            assert len(out)==1
            raw=out[0]
            if 2*n<=H*H:
                assert raw[0]<=H
            vectors.append((n,raw))
        for i in range(index,len(catalogue)):
            p=catalogue[i]
            if n*p>B:
                break
            u,v=pis[p]
            for sign in (1,-1):
                xx,yy,m=x,y,n
                while m*p<=B:
                    xx,yy=xx*u-yy*sign*v,xx*sign*v+yy*u
                    m*=p
                    walk(i+1,m,xx,yy)
    walk(0,1,1,0)
    physically={coord:n for n,coord in vectors if coord[0]<=H}
    assert len(physically)==sum(c[0]<=H for _,c in vectors)
    oracle={(b,a):(a*a+b*b)//(2 if (a+b)%2==0 else 1)
            for b in range(2,H+1) for a in range(1,b) if gcd(a,b)==1}
    assert physically==oracle
    A=len(oracle)
    Y=A*C
    overlap=sum(min(Fraction(1,A),C/n) for n in physically.values())
    low=sum(n<=Y for n,_ in vectors)
    high=sum(Fraction(1,n) for n in physically.values() if n>Y)
    assert Y<=Fraction(H*H,2) and overlap==Fraction(low,A)+C*high
    return dict(height=H,product_normalizer=str(C), threshold=str(Y), vectors_le_threshold=low,
                overlap=str(overlap), total_variation=str(1-overlap))


def main():
    path=Path(__file__).resolve().parents[1]/"eighth"/"atoms_check.py"
    assert sha256(path.read_bytes()).hexdigest()==SOURCE_SHA
    spec=spec_from_file_location("round8_rational_atoms",path)
    gen=module_from_spec(spec)
    spec.loader.exec_module(gen)
    H=HEIGHTS[-1]
    slots=array("I",[0])*(H*(H-1)//2)
    def emit(b,a,eps,positive,path,sign):
        wp=wm=gp=gm=0
        product=1
        for p,k in path:
            if sign*k>0:
                wp+=1
                gp+=abs(k)-1
                product*=p**abs(k)
            else:
                wm+=1
                gm+=abs(k)-1
        assert product==positive and slots[slot(b,a)]==0
        slots[slot(b,a)]=pack(wp,wm,gp,gm,eps%2)
    raw=gen.generate(H,emit)
    factors,roots=factor_sieve(H*H+(H-1)**2)
    hist=Counter()
    samples=[]
    for b in range(2,H+1):
        for a in range(1,b):
            code=slots[slot(b,a)]
            if gcd(a,b)>1:
                assert code==0
                continue
            vals=from_norm(b,a,factors,roots)
            assert code==pack(*vals)
            hist[vals]+=1
        if b in HEIGHTS:
            samples.append(row_stats(b,hist))
    with (path.parent/"atoms_checked.json").open() as stream:
        frozen=json.load(stream)
    for row,old in zip(samples,frozen):
        assert row["atoms"]==old["atoms"]
        assert row["slots_by_size"]=={int(k):v for k,v in old["nonzero_support_sizes"].items()}
    assert samples[-1]["atoms"]==raw["odd_box_atoms"]+raw["even_box_atoms"]
    print(json.dumps(dict(generator_sha256=SOURCE_SHA, height_boxes=samples,
                          largest_free_directions=raw["free_direction_groups"],
                          largest_odd_disk_nodes=raw["odd_disk_nodes"],
                          global_overlap_checks=[overlap_check(h) for h in (6,12,24)],
                          local_prime_square_checks=[local_residues(5,2,1),local_residues(13,3,2),
                                                     local_residues(17,4,1)]),indent=2))


if __name__=="__main__":
    main()
