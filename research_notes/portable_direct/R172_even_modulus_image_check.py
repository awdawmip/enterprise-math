"""R172 finite exhaustive validation of modular signed-axis path image theorem.
Independent from R171 check script; exact finite group enumeration.
"""
from collections import deque
import itertools
import json


def mul(s, t, q):
    a, b, c = s
    d, e, f = t
    return ((a+d) % q,
            tuple((x+y) % q for x,y in zip(b,e)),
            tuple((x+y+d*z) % q for x,y,z in zip(c,f,b)))


def generated(q,dim):
    zero=(0,)*dim
    identity=(0,zero,zero)
    generators=[]
    for i in range(dim):
        for sign in (-1,1):
            v=list(zero)
            v[i]=sign % q
            generators.append((1,tuple(v),tuple(v)))
    reached={identity}
    queue=deque([identity])
    while queue:
        s=queue.popleft()
        for g in generators:
            t=mul(s,g,q)
            if t not in reached:
                reached.add(t)
                queue.append(t)
    return reached


def invariant(s,q):
    a,b,c=s
    if q % 2 == 0:
        if (a-sum(b)) % 2: return False
        if q % 4 == 0 and (sum(c)-a*(a+1)//2)%2: return False
    return True


def main():
    cases=((2,1),(2,3),(2,6),(3,2),(4,1),(4,3),(6,2),(8,2),(10,2),(12,1))
    report={}
    exhaustive_state_count=0
    for q,d in cases:
        reachable=generated(q,d)
        expected=q**(2*d+1)//__import__('math').gcd(q,4)
        assert len(reachable)==expected,(q,d,len(reachable),expected)
        predicted=set()
        for a in range(q):
            for b in itertools.product(range(q), repeat=d):
                for c in itertools.product(range(q), repeat=d):
                    s=(a,b,c)
                    if invariant(s,q): predicted.add(s)
        assert reachable==predicted,(q,d,'missing',len(predicted-reachable),'extra',len(reachable-predicted))
        full=q**(2*d+1)
        exhaustive_state_count+=full
        report[f'q{q}_d{d}']={"full_states":full,"reachable":len(reachable),"index":full//len(reachable),"prediction_exact":True}
    print(json.dumps({"marker":"R172_ALL_MODULI_IMAGE_CERTIFICATE_EXACT_PASS",
                      "full_states_tested":exhaustive_state_count,
                      "verified_cases":report,
                      "formula":"q^(2d+1)/gcd(q,4)",
                      "invariants":"even q: a=sum(b) mod 2; q divisible by 4 also sum(c)=a(a+1)/2 mod 2",
                      "mathematical_status":"AUTHOR_PROVED; INDEPENDENT_REVIEW_NOT_RUN"},
                     sort_keys=True,indent=2))


if __name__=='__main__':
    main()
