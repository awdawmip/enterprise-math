#!/usr/bin/env python3
"""R135 exact verification; rational/integer arithmetic only, no dependencies."""
from fractions import Fraction as Q
from math import gcd
from time import monotonic
from json import dump

def farey(m):
    return sorted(Q(a,b) for b in range(1,m+1)
                  for a in range(b+1) if gcd(a,b)==1)

def ceil(x):
    return -(-x.numerator//x.denominator)

def direct_word(K,m,theta):
    a,b=theta.numerator,theta.denominator
    assert 0<a<b
    return tuple(int(((K+i)*a)%b < a) for i in range(m))

def mechanical(m,alpha,rho):
    return tuple((rho+(i+1)*alpha).__floor__()-(rho+i*alpha).__floor__()
                 for i in range(m))

def phi(n):
    return sum(gcd(i,n)==1 for i in range(1,n+1))

def mignosi(m):
    return 1+sum((m+1-q)*phi(q) for q in range(1,m+1))

def midpoint_lift(K,m):
    L=K-1; assert L>=max(1,m*(m-1))
    f=farey(m)
    found={}; checks=0; min_excess=None; max_den=0
    for a,b in zip(f,f[1:]):
        mid=(a+b)/2
        assert b-a==Q(1,a.denominator*b.denominator)
        cuts=[(Q(0),0,0),(Q(1),1,0)]
        cuts.extend((Q(ceil(j*mid))-j*mid,ceil(j*mid),j) for j in range(1,m+1))
        cuts.sort()
        assert all(cuts[j][0]<cuts[j+1][0] for j in range(len(cuts)-1))
        for lower,upper in zip(cuts,cuts[1:]):
            (vl,p,j),(vu,q,k)=lower,upper
            C=Q(p+q,2); T=Q(j+k,2)
            assert T>=Q(1,2)
            left=(L+T)*a-C
            right=(L+T)*b-C
            assert right-left>1
            n=left.__floor__()+1
            theta=(n+C)/(L+T)
            assert a<theta<b and Q(0)<theta<Q(1)
            rho=(L*theta)%1
            assert rho==C-T*theta
            assert p-j*theta<rho<q-k*theta
            w=mechanical(m,mid,(vl+vu)/2)
            assert direct_word(K,m,theta)==w
            found.setdefault(w,theta)
            checks+=1
            max_den=max(max_den,theta.denominator)
            excess=right-left-1
            min_excess=excess if min_excess is None else min(min_excess,excess)
    assert len(found)==mignosi(m)
    return found,checks,min_excess,max_den

def full_atoms(K,m):
    # Complete phase partition for every floor n*theta used in the observer.
    cuts={Q(0),Q(1)}
    for n in range(max(1,K-1),K+m):
        cuts.update(Q(p,n) for p in range(1,n))
    cuts=sorted(cuts)
    words={}
    for i in range(len(cuts)-1):
        theta=(cuts[i]+cuts[i+1])/2
        words.setdefault(direct_word(K,m,theta),theta)
        if i:
            theta=cuts[i]
            words.setdefault(direct_word(K,m,theta),theta)
    assert all(direct_word(K,m,t)==w for w,t in words.items())
    return words,len(cuts)-2,2*len(cuts)-3

def run():
    start=monotonic(); rows=[];total=0
    for m in range(1,31):
        bound=max(1,m*(m-1))+1
        a,ct,exc,den=midpoint_lift(bound,m)
        huge=10**80+bound
        b,ct2,exc2,den2=midpoint_lift(huge,m)
        assert set(a)==set(b)
        total+=ct+ct2
        rows.append({'m':m,'sufficient_K':bound,'F_m':len(a),
                     'certificates_per_K':ct,'min_excess_at_bound':str(exc),
                     'max_denominator_at_bound':str(den),
                     'max_denominator_bits_huge_K':den2.bit_length()})
    ref=midpoint_lift(43,7)[0]
    example=[]; full_checks=0
    for K in range(10,20):
        w,c,atoms=full_atoms(K,7)
        full_checks+=atoms
        missing=[''.join(map(str,ww)) for ww in sorted(ref.keys()-w.keys())]
        example.append({'K':K,'patterns':len(w),'interior_cut_count':c,
                        'parameter_atoms_checked':atoms,'missing_words':missing})
    assert example[1]['patterns']==54 and example[5]['patterns']==52
    assert example[5]['missing_words']==['0111110','1000001']
    result={'status':'R135_QUADRATIC_MIDPOINT_LIFT_PASS',
            'scientific_input_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
            'method':'Exact rational Farey gap midpoint alignment, independent direct modular observer, all floor-crossing singleton and open atoms',
            'm_range_inclusive':[1,30],
            'huge_K_offset':str(10**80),
            'lift_certificates_verified':total,
            'nonmonotone_example_m7':example,
            'nonmonotone_atoms_verified':full_checks,
            'rows':rows,
            'elapsed_seconds':round(monotonic()-start,3)}
    with open('verification_r135.json','w') as handle:
        dump(result,handle,indent=2,ensure_ascii=False)
    print(result['status'],'lift_certificates',total,
          'atoms',full_checks,'time',result['elapsed_seconds'])

if __name__=='__main__':
    run()
