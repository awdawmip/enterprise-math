#!/usr/bin/env python3
"""Independent exact checks for unfiltered endpoint coefficient and H=S3 observers."""
import json
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from pathlib import Path
from signed_brc import endpoint_weight,endpoint_multiplicity
from VERIFY_EC49BV import analyze,attainable_atoms,compositions,signature_patterns,WP,WM,ID


def coefficient_dp(n,wp,wm):
    d={(0,)*6:Fraction(1)}
    for _ in range(n):
        t=defaultdict(Fraction)
        for loc,weight in d.items():
            for axis in range(6):
                up=list(loc); up[axis]+=1
                dn=list(loc); dn[axis]-=1
                t[tuple(up)] += weight*wp[axis]
                t[tuple(dn)] += weight*wm[axis]
        d=t
    return d


def S3_brute_support():
    H=tuple(tuple(p)+tuple(range(3,6)) for p in permutations(range(3)))
    patterns=((0,1),(1,0))
    pmap=signature_patterns(H,patterns)
    all_ok=True; total_words=0; atom_signatures=set()
    for k in compositions(2,6):
        items=[]
        for i,c in enumerate(k):items += [i]*c+[6+i]*c
        brute=set()
        for w in set(permutations(items)):
            total_words+=1
            bits=0
            for j in range(3):bits |= pmap.get(w[j:j+2],0)
            brute.add((w[0],w[-1],bits))
        dp,_=attainable_atoms(k,H,patterns)
        if brute != dp:all_ok=False
        atom_signatures.update(brute)
    assert total_words==396 and all_ok
    return H,{"S3_direct_words":total_words,"all_signatures_identical":True,"S3_reachable_atoms":len(atom_signatures)}


def main():
    cases=[(0,(0,)*6),(2,(0,)*6),(4,(1,-1,0,0,0,0)),(5,(1,-1,1,0,0,0)),(6,(0,)*6)]
    results=[]
    for n,disp in cases:
        value=coefficient_dp(n,WP,WM).get(disp,Fraction(0))
        native=endpoint_weight(n,disp,WP,WM)
        assert value==native
        results.append({"n":n,"d":list(disp),"coefficient":str(value),"native":str(native)})
    H,brute=S3_brute_support()
    s=analyze(4,H=H,wp=(2,3,5,7,11,13),wm=(1,)*6)
    assert s['fixed_instrument_rank']==198 and s['covariant_instrument_rank']==174
    # Covariant instrument: (h.w)_{h(i)}=w_i, so every word has preserved product.
    word=(0,1,7,6) # signed four-step closed native path
    w=(Fraction(2),Fraction(3),Fraction(5),Fraction(7),Fraction(11),Fraction(13))
    for h in H:
        transformed=tuple(h[a] if a<6 else 6+h[a-6] for a in word)
        forward_wp=tuple(w[h.index(j)] for j in range(6))
        def chi(path,weight_positive):
            out=Fraction(1)
            for a in path:out*=weight_positive[a] if a<6 else Fraction(1)
            return out
        assert chi(word,w)==chi(transformed,forward_wp)
    out={"schema":"EC49BV_BRIDGE_CHECK_V1","native_endpoint_coefficients":results,
        "S3_result":s,"S3_brute":brute,"covariant_identity_checked_for_all_S3":True}
    Path(__file__).with_name('BRIDGE_REPORT_EC49BV.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))
if __name__=='__main__':main()
