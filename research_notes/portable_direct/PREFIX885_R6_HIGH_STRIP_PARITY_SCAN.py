"""PREFIX-885 full high-strip parity scan, using exact CRT."""
from math import gcd
from collections import Counter
import json
from PREFIX885_R6_CENTRAL_FIBER_CRT import central_fiber_count

N=1<<32


def center_fast(q1,q2):
    g=gcd(q1,q2)
    L=(q1//g)*q2
    if g>1:
        h=(N-1)//L
        return 2*((h+1)//2)
    assert L>N
    r1=((N-1)*pow(2,-1,q1))%q1
    r2=((N-1)*pow(2,-1,q2))%q2
    inv=pow(q1,-1,q2)
    n=0
    for i in range(32):
        bit=1<<i
        x=r1+q1*(((r2-bit-r1)*inv)%q2)
        if x<N and (x&bit)==0:
            n+=1
        x=r1+q1*(((r2+bit-r1)*inv)%q2)
        if x<N and (x&bit)!=0:
            n+=1
    assert n%2==0,(q1,q2,n)
    return n


def exhaustive_scan():
    vals=list(range(523001,524288,2))
    groups=Counter()
    multiplicities=Counter()
    checked=0
    odd_examples=[]
    for i,q1 in enumerate(vals):
        for j in range(i,len(vals)):
            q2=vals[j]
            c=center_fast(q1,q2)
            g=gcd(q1,q2)
            category=('coprime' if g==1 else
                      'noncoprime_low_g' if g<=63 else
                      'noncoprime_high_g')
            weight=1 if i==j else 2
            groups[(category,'total')]+=weight
            groups[(category,'odd' if (c//2)%2 else 'even')]+=weight
            multiplicities[c]+=weight
            checked+=weight
            if len(odd_examples)<10 and (c//2)%2:
                odd_examples.append({'q1':q1,'q2':q2,'gcd':g,'c_star':c,
                                     'collision_parity':1})
            if (i*len(vals)+j)%9973==0:
                assert c==central_fiber_count(32,q1,q2)
    assert checked==644*644
    out={'schema':'PREFIX885_R6_HIGH_STRIP_EXHAUSTIVE_V1',
         'p':32,
         'q_domain':'odd q in [523001,524287]',
         'ordered_pairs':checked,
         'parity_by_gcd_class':{k[0]:{} for k in groups}}
    for (category,metric),v in groups.items():
        out['parity_by_gcd_class'][category][metric]=v
    out['central_multiplicity_distribution']={str(k):v for k,v in sorted(multiplicities.items())}
    out['odd_parity_examples']=odd_examples
    out['notes']='Exact arithmetic, upper triangle weighted by 2 off diagonal. Parity classification, not collision existence.'
    return out


if __name__=='__main__':
    out=exhaustive_scan()
    with open('PREFIX885_R6_HIGH_STRIP_PARITY_RESULTS.json','w') as f:
        json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))
