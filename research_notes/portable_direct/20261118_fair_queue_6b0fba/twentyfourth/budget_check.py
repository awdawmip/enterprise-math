"""Exact prime-log entropy arithmetic on a compressed, monotone Gaussian walk."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import log, prod
import json

PRIMES=(137,149,157,173)
CUTS=(1,2,4,8)


@lru_cache(None)
def factors(n):
    out=[]
    d=2
    while d*d<=n:
        while n%d==0:
            out.append(d)
            n//=d
        d+=1
    if n>1: out.append(n)
    return out


def combine(*terms):
    value=Counter()
    for scale, expr in terms:
        for p,q in expr.items(): value[p]+=scale*q
    return {p:q for p,q in value.items() if q}


def entropy(keys):
    counts=Counter(keys)
    n=sum(counts.values())
    value=Counter(factors(n))
    for k in counts.values():
        for p in factors(k): value[p]-=Fraction(k,n)
    return {p:q for p,q in value.items() if q}


def magnitude(expr):
    return sum(log(p)*float(q) for p,q in expr.items())


def brief(expr):
    # A short exact signature also works for samples with many count factors.
    return {str(p):str(q) for p,q in sorted(expr.items())}


def build_walk():
    mod=prod(PRIMES)
    roots=[next(i for i in range(1,p) if i*i%p==p-1) for p in PRIMES]
    old=0
    enc=[]
    for p,r,last in zip(PRIMES,roots,CUTS):
        forbidden={(-x-sign*r*y)%p for y in range(9) for x in range(9-y) for sign in (-1,1)}
        alphabet=[a for a in range(1,p) if a not in forbidden][:2**(last-old)]
        assert len(alphabet)==2**(last-old)
        enc.append(alphabet)
        old=last
    anchors=[]; previous_end=(-200,-1)
    for j,bits in enumerate(product((0,1),repeat=8)):
        labels=[]; first=0
        for alphabet,last in zip(enc,CUTS):
            index=0
            for bit in bits[first:last]: index=2*index+bit
            labels.append(alphabet[index])
            first=last
        x=sum(a*(mod//p)*pow(mod//p,-1,p) for a,p in zip(labels,PRIMES))%mod
        while x<previous_end[0]+129: x+=mod
        y=j*mod
        assert x>=previous_end[0]+129 and y>previous_end[1]
        positions=[(x,y)]
        for bit in bits:
            x+=1-bit; y+=bit
            assert all((x+sign*r*y)%p for p,r in zip(PRIMES,roots) for sign in (-1,1))
            positions.append((x,y))
        previous_end=x,y
        anchors.append((positions,bits))
    return anchors,roots,enc


def experiment(anchors,roots,width,lengths):
    # Equal weights on (chosen anchor, uniform terminal offset). The next 128 steps are east.
    @lru_cache(None)
    def h(qcount,offset,length,at):
        conditioning=[]; joint=[]
        for pos,bits in anchors:
            for u in range(width):
                m=u+at
                x,y=pos[min(m,8)]
                if m>8: x+=m-8
                q=tuple((x+r*y)%p for r,p in zip(roots[:qcount],PRIMES[:qcount]))
                word=(bits+(0,)*128)[m:m+offset+length]
                history=word[:offset]
                conditioning.append((q,history))
                joint.append((q,history,word[offset:]))
        return combine((1,entropy(joint)),(-1,entropy(conditioning)))

    charges=[]
    gaps=[]
    dsum=drift=0.0
    for j,L in enumerate(lengths):
        charge=combine((Fraction(1,L),h(j,0,L,0)),(Fraction(-1,L),h(j+1,0,L,0)))
        charges.append(charge)
        if j+1 == len(lengths):
            continue
        B=lengths[j+1]
        g=h(j+1,0,L,0); g2=h(j+1,0,B,0)
        target=combine((Fraction(1,L),g),(Fraction(-1,B),g2))
        decomposed={}
        for i in range(1,B):
            weight=Fraction(B-i,B)-max(Fraction(L-i,L),0)
            prev=h(j+1,i-1,1,0)
            moved=h(j+1,i-1,1,1)
            cur=h(j+1,i,1,0)
            info=combine((1,moved),(-1,cur))
            shift=combine((1,moved),(-1,prev))
            assert magnitude(info)>=-1e-12
            dsum+=float(weight)*magnitude(info)
            drift+=float(weight)*magnitude(shift)
            decomposed=combine((1,decomposed),(weight,info),(-weight,shift))
        assert decomposed==target
        gaps.append(target)
    total=combine(*[(1,c) for c in charges])
    start=combine((Fraction(1,lengths[0]),h(0,0,lengths[0],0)))
    end=combine((Fraction(1,lengths[-1]),h(len(lengths),0,lengths[-1],0)))
    assert combine((1,start),(-1,end),*[( -1,g) for g in gaps])==total
    return {'width':width,'lengths':lengths,'charges_prime_logs':[brief(c) for c in charges],
            'total_prime_logs':brief(total),'total_bits_display':round(magnitude(total)/log(2),12),
            'weighted_discarded_information_nats_display':round(dsum,12),
            'weighted_signed_shift_nats_display':round(drift,12)}


def main():
    anchors,roots,enc=build_walk()
    unsmoothed=experiment(anchors,roots,1,CUTS)
    assert unsmoothed['total_prime_logs']=={'2':'5/2'} and 2**5>5**2
    assert all(v=={'2':str(q)} for v,q in zip(unsmoothed['charges_prime_logs'],
                                               (1,Fraction(1,2),Fraction(1,2),Fraction(1,2))))
    smooth=[experiment(anchors,roots,w,(1,3,5,8)) for w in (1,5,19)]
    for entry in smooth[1:]:
        d=1/entry['width']
        modulus=-d*log(d)-(1-d)*log(1-d)+d*log(2)
        assert entry['total_bits_display']*log(2) < log(2)+3.5*modulus
    print(json.dumps({'actual_step_vectors':[[1,0],[0,1]],'D1_alphabet_size_in_source':5,
                      'signed_split_primes':PRIMES,'sqrt_minus_one':roots,
                      'residues_encoding_new_bits':enc,'disjoint_anchors':len(anchors),
                      'both_signs_zero_avoiding_on_observed_eight_steps':True,
                      'unsmoothed':unsmoothed,'nondivisible_lengths':smooth},indent=2))


if __name__=='__main__':
    main()
