from itertools import product
from math import lcm
from fractions import Fraction
from quotient_exact import C,T,P,failure,ERRORS,TRIP,PAIRS,envelope
from collections import Counter
import sys

def brute(r,J, ec, dc):
    sigs=[tuple(P[(a+j)%6] for j in J) for a in range(6)]
    a=r%6
    cache=[]
    # Independent direct formulation of H_4 evaluated as rational, not the
    # integer polynomial used in the main verifier.
    for j in J:
        q=r+j
        H=(Fraction(1,6)+Fraction(1,2*q)-Fraction(115,36*q**2)
           +Fraction(115,6*q**3)-Fraction(16315,108*q**4))
        cache.append({(e,d):108*(Fraction(q**3*(T[q]+e),C[q]+d)-q**4*H)
                      for e in ERRORS for d in ERRORS if C[q]+d>0})
    D=lcm(*(v.denominator for site in cache for v in site.values()))
    tables=[{key:int(v*D) for key,v in site.items()} for site in cache]
    sigs=[[x*D for x in sig] for sig in sigs]
    for keys in product(*[tab.keys() for tab in tables]):
        def respects(part, color):
            if part is False:
                return True
            idx = range(len(keys)) if part is True else part
            return len({keys[i][color] for i in idx}) <= 1
        if not (respects(ec,0) and respects(dc,1)): continue
        vals=[t[k] for t,k in zip(tables,keys)]
        distances=[]
        for sig in sigs:
            dif=[x-y for x,y in zip(vals,sig)]
            distances.append(max(dif)-min(dif))
        if any(d<=distances[a] for b,d in enumerate(distances) if b!=a):return True
    return False

if __name__=='__main__':
    expected = {TRIP:[38,61,441,447], PAIRS[0]:[185,257,3629,3629],PAIRS[1]:[246,300,3624,3630]}
    cnt=Counter()
    for J, Ns in expected.items():
        for (ec,dc),N in zip(((True,True),(False,True),(True,False),(False,False)),Ns):
            for r in (1,2,5,17,N-1,N,N+1,N+7):
                direct=brute(r,J,ec,dc)
                assert direct == (failure(r,J,ec,dc) is not None), (r,J,ec,dc)
                cnt[str(J)] +=1
    print('Direct exhaustive full Cartesian rational crosschecks:',cnt)
    print('Envelope endpoints:',str(envelope(1350)),str(envelope(8000)))
