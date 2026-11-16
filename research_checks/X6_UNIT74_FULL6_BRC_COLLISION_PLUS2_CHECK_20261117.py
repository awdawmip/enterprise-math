"""Exact six-axis native BRC shortest-collision/plus-two separation checker.
Frozen model: awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03.
No source authority, admission or native benchmark completion is implied.
"""
import hashlib
import importlib.util
import os
import sys
import itertools
import json
import math
from collections import Counter
from fractions import Fraction


def require(ok, msg):
    if not ok:
        raise AssertionError(msg)


def native_shortest(z):
    t = sum(map(abs, z))
    den = math.prod(math.factorial(abs(x)) for x in z)
    require(math.factorial(t) % den == 0, "shortest integrality")
    return math.factorial(t) // den


def independent_plus_two(z):
    t = sum(map(abs, z))
    return native_shortest(z) * (t + 1) * (t + 2) * sum((Fraction(1, abs(v) + 1) for v in z), Fraction(0))


def original_frozen_endpoint_plus_two(z):
    """Faithful K=1 specialization of frozen signed_brc.endpoint_multiplicity."""
    t = sum(map(abs, z))
    out = 0
    for i in range(6):
        denominator = 1
        for j, v in enumerate(z):
            a = max(v, 0)
            b = max(-v, 0)
            k = int(i == j)
            denominator *= math.factorial(a + k) * math.factorial(b + k)
        require(math.factorial(t + 2) % denominator == 0, "endpoint integrality")
        out += math.factorial(t + 2) // denominator
    return out


def passive(z):
    h = min(z)
    r = tuple(v-h for v in z)
    return dict(r=r, G=sum(v*v for v in z), T=sum(abs(v) for v in z), h=h)


def exact_cube_exception_census(M):
    candidates = 0
    passive_pairs = 0
    shortest_equal = 0
    exceptions = []
    for a in itertools.combinations_with_replacement(range(-M, M + 1), 6):
        s = sum(a)
        if s >= 0 or s % 3:
            continue
        c = -s // 3  # G(a+c·1)=G(a) in six axes iff c=-sum(a)/3.
        b = tuple(x+c for x in a)
        if b[-1] > M:
            continue
        candidates += 1
        if sum(map(abs, a)) != sum(map(abs, b)):
            continue
        passive_pairs += 1
        if native_shortest(a) != native_shortest(b):
            continue
        shortest_equal += 1
        if sorted(map(abs,a)) != sorted(map(abs,b)):
            exceptions.append((a,b))
    return dict(M=M, G_pair_candidates=candidates, equal_passive_pairs=passive_pairs,
                shortest_BRC_equal_pairs=shortest_equal, exceptional_pairs=exceptions)


def verify_pinned_original(path,A,B):
    if not os.path.exists(path):
        return {"executed":False,"reason":"Pinned original source not supplied; independent exact oracle only"}
    raw=open(path,"rb").read()
    pin=hashlib.sha1(f"blob {len(raw)}\0".encode()+raw).hexdigest()
    require(pin=="300a96e3dc24bf6fff73743037a0347a8bc83176","frozen original blob mismatch")
    spec=importlib.util.spec_from_file_location("unit74_frozen_brc_original",path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for z in (A,B):
        require(mod.spatial_norm_squared(z)==sum(x*x for x in z),"native G mismatch")
        require(mod.shortest_event_count(z)==sum(abs(x) for x in z),"native T mismatch")
        require(mod.shortest_path_multiplicity(z)==native_shortest(z),"original shortest mismatch")
        require(mod.endpoint_multiplicity(sum(map(abs,z))+2,z)==original_frozen_endpoint_plus_two(z),"original plus2 mismatch")
    return {"executed":True,"exact_git_blob_sha1":pin,"functions_called":["spatial_norm_squared","shortest_event_count","shortest_path_multiplicity","endpoint_multiplicity"],"witnesses_checked":2}


def main():
    A = (-6,-6,-2,2,2,7)
    B = (-5,-5,-1,3,3,8)
    pa,pb = passive(A),passive(B)
    require(pa['r']==pb['r'] and pa['G']==pb['G'] and pa['T']==pb['T'], "passive observer collision")
    require(pa['h']==-6 and pb['h']==-5, "depths")
    require(sorted(map(abs,A)) != sorted(map(abs,B)), "multiset difference")
    require(native_shortest(A)==native_shortest(B)==742096122768000, "shortest mass")
    x,y = independent_plus_two(A),independent_plus_two(B)
    u,v = original_frozen_endpoint_plus_two(A),original_frozen_endpoint_plus_two(B)
    require(x.denominator==1 and y.denominator==1 and x==u and y==v, "independent original recurrence comparison")
    require(u==734913692436924000 and v==752485468486752000, "plus two exact")
    require(v-u==17571776049828000, "plus two gap")
    census = [exact_cube_exception_census(M) for M in range(1,9)]
    require(all(not row['exceptional_pairs'] for row in census[:7]), "smaller-cube bounded minimality")
    require(len(census[-1]['exceptional_pairs'])==2, "cube 8 count")
    require((A,B) in census[-1]['exceptional_pairs'], "chosen witness in census")
    expected = {((-8,-3,-3,1,5,5),(-7,-2,-2,2,6,6)), (A,B)}
    require(set(census[-1]['exceptional_pairs'])==expected, "exhaustive exceptional pairs")
    pinned=verify_pinned_original(sys.argv[1] if len(sys.argv)>1 else "",A,B)
    out = {
      "schema":"EM_X6_UNIT74_AUTHOR_EXACT_INTEGER_CERT_V1", "researcher":"EM-X6-FB6990",
      "science_pin":"59538f585d037d09ef687b28715c4bc1a3f9fe03",
      "original_module_blob_sha1":"300a96e3dc24bf6fff73743037a0347a8bc83176",
      "scope":"all six named signed native X6 axes, selected raw coordinate chart",
      "A":A,"B":B,"passive_observer":{k:pa[k] for k in ('r','G','T')},
      "depths":[pa['h'],pb['h']], "shortest_N_BRC":native_shortest(A),
      "absolute_multisets":[sorted(map(abs,A)),sorted(map(abs,B))],
      "length_T_plus_2_masses":[u,v],"gap_B_minus_A":v-u,
      "reciprocal_sums":[str(sum((Fraction(1,abs(w)+1) for w in z),Fraction())) for z in (A,B)],
      "complete_sorted_six_axis_cube_census":census,
      "pinned_original_source_run":pinned,
      "all_tests_passed":True,
      "scientific_status":"AUTHOR_EXACT / SCOPED_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED"
    }
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True,default=list))

if __name__=='__main__':main()
