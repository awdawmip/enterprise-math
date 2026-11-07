#!/usr/bin/env python3
"""R609: exact branch-provenance free-algebra fiber test.
Carrier = tagged R462 signed auxiliary coefficient factorization, not native heartbeat dynamics.
Pure Python integers, no numerical approximation.
"""
from math import comb
import json, hashlib
from pathlib import Path

# Weighted words P,A,B have respective degrees 1,1,2.
WEIGHT = {'P':1,'A':1,'B':2}

def words(r,s,orientation):
    """Finite free algebra factor expansion, with integer signed coefficients."""
    d = r-s
    assert orientation in ('PAB','PBA') and 2 <= s < r and r%2==1
    out = {}
    for p in (0,1):
        for a in range(2*s+1):
            for b in range(d+1):
                w = ('P',)*p + ((('A',)*a+('B',)*b) if orientation=='PAB' else (('B',)*b+('A',)*a))
                v = (-1 if p else 1)*comb(2*s,a)*comb(d,b)
                out[w] = out.get(w,0) + v
    return {w:v for w,v in out.items() if v != 0}

def grade(w):
    return sum(WEIGHT[x] for x in w)

def graded(t):
    out={}
    for w,v in t.items():
        n=grade(w)
        out[n]=out.get(n,0)+v
    return out

def coeff_r442(r,s):
    """Frozen R462 original signed coefficient [t^r] formula, no precalculated values."""
    d=r-s
    def cb(n,k):
        return comb(n,k) if 0<=k<=n else 0
    return sum(comb(d,q)*(cb(2*s,r-2*q)-cb(2*s,r-2*q-1)) for q in range(d+1))

def check_pair(r,s,full=True):
    k=(r-1)//2;d=r-s
    v=min(k,d);u=r-2*v
    assert 1<=v<=d and 1<=u<=2*s and u%2==1
    c=comb(2*s,u)*comb(d,v)
    wa=('A',)*u+('B',)*v
    wb=('B',)*v+('A',)*u
    assert grade(wa)==grade(wb)==r and wa != wb
    if full:
        left,right=words(r,s,'PAB'),words(r,s,'PBA')
        assert graded(left)==graded(right)
        assert graded(left).get(r,0)==coeff_r442(r,s)
        assert left.get(wa,0)==c and left.get(wb,0)==0
        assert right.get(wa,0)==0 and right.get(wb,0)==c
        assert sum(z for w,z in left.items() if grade(w)==r)==coeff_r442(r,s)
        assert sum(z for w,z in right.items() if grade(w)==r)==coeff_r442(r,s)
    return {'r':r,'s':s,'d':d,'u':u,'v':v,'joint_magnitude':str(c),'signed_scalar':str(comb(r+s,2*s)*coeff_r442(r,s))}

def main():
    checks=[check_pair(r,s) for r in range(5,26,2) for s in range(2,r)]
    assert len(checks)==sum(r-2 for r in range(5,26,2))==143
    # Exact large frozen R462 crosschecks, do not materialize enormous word dictionaries.
    large=[check_pair(r,s,full=False) for r in (195,197) for s in (171,172,173,174)]
    for row in large:
        r,s=row['r'],row['s'];u,v=row['u'],row['v'];d=r-s
        assert row['joint_magnitude']==str(comb(2*s,u)*comb(d,v))
    # A concrete smallest signed BRC coefficient (r=5,s=2): scalar may cancel,
    # whereas the witness words carry distinct signed source paths.
    small=check_pair(5,2)
    payload={'schema':'R609_SIGNED_BRC_TAGGED_FACTOR_FIBER_V1','scientific_source':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
      'full_exact_odd_r_5_to_25_pair_count':len(checks),
      'large_frozen_row_pairs':large,
      'small_witness':small,
      'full_coefficients_and_free_algebra_consistency':'PASS',
      'proof_scope':'formal signed factor provenance lifts; native BRC state realization unproved',
      'terminal_marker':'R609_TAGGED_FACTOR_FIBER_EXACT_PASS'}
    # Deterministic canonical evidence hash for pairwise witness parameters.
    stream=json.dumps(checks,sort_keys=True,separators=(',',':')).encode('utf-8')
    payload['exhaustive_pair_evidence_sha256']=hashlib.sha256(stream).hexdigest()
    dest=Path(__file__).with_name('R609_EVIDENCE.json')
    dest.write_text(json.dumps(payload,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'count':len(checks),'small':small,'large':large,'sha256':payload['exhaustive_pair_evidence_sha256'],'marker':payload['terminal_marker']},sort_keys=True))
if __name__=='__main__':main()
