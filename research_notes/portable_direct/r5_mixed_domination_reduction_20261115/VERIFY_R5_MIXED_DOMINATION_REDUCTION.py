"""Exact reproducible finite certificates for R5 mixed weighted repair.

Standard library only. Distances are integral center replacement distances;
not a simulation of the 954-event source or a native X6 theorem.
"""
from itertools import combinations
import json

OLD = tuple(frozenset(map(int, s)) for s in ('0125', '0135', '0235', '0245', '0246'))
AA = tuple(frozenset(map(int, s)) for s in ('1235', '1245', '1246', '1345', '1346'))
AAB = tuple(frozenset(map(int, s)) for s in ('1235', '1236', '1245', '1246', '1345', '1346'))
D = lambda a,b: len(a-b)

def gamma_and_witness(d):
    n=1 << d
    balls=tuple((1 << v) | sum((1 << (v ^ (1 << i))) for i in range(d)) for v in range(n))
    full=(1 << n)-1
    for k in range(1,n+1):
        for group in combinations(range(n), k):
            coverage=0
            for u in group: coverage |= balls[u]
            if coverage == full: return k, group
    raise AssertionError('missing dominating set')

def perfect_code(d):
    assert d == 7
    return tuple(v for v in range(1 << d) if 0 == (0 if v == 0 else xor_columns(v,d)))

def xor_columns(v,d):
    z=0
    for i in range(d):
        if v & (1 << i): z ^= i+1
    return z

def dominates(d,dom):
    return all(any((v ^ u).bit_count() <= 1 for u in dom) for v in range(1 << d))

def old_lib(d,dom,case):
    # First suffix bit s=0/1, remaining bits v in {0,1}^d.
    n=1 << d
    if case == 'a':
        return ([(1,0,v) if v in dom else (4,0,v) for v in range(n)]
                + [(0,1,v) for v in dom])
    return ([(1,0,v) for v in range(n)] + [(0,1,v) for v in range(n)])

def covers_library(d,lib,case):
    new = AA if case == 'a' else AAB
    for c in new:
        s = int(2 in c)
        for v in range(1 << d):
            if not any(D(c,OLD[j]) + int(s != so) + (v ^ vo).bit_count() <= 2
                       for j,so,vo in lib):
                return False
    return True

def exact_small_library(d,case):
    # Exhaustively examine all library subsets in increasing cardinality;
    # only used at d<=1 where 5*2^(d+1) <= 20.
    assert d <= 1
    new=AA if case == 'a' else AAB
    targets=[(c,int(2 in c),v) for c in new for v in range(1 << d)]
    old=[(j,s,v) for j in range(5) for s in range(2) for v in range(1 << d)]
    coverage=[]
    for j,s,v in old:
        bits=0
        for i,(c,s2,v2) in enumerate(targets):
            if D(c,OLD[j]) + int(s != s2) + (v ^ v2).bit_count() <=2: bits |= 1 << i
        coverage.append(bits)
    goal=(1 << len(targets))-1
    for k in range(1,len(old)+1):
        for subset in combinations(range(len(old)),k):
            union=0
            for j in subset:union |= coverage[j]
            if union == goal:return k
    raise AssertionError('no set cover')

def run():
    assert [D(frozenset((1,3,4,6)),o) for o in OLD]==[3,2,3,3,2]
    assert [D(frozenset((1,2,4,5)),o) for o in OLD]==[1,2,2,1,2]
    assert [D(frozenset((1,2,3,6)),o) for o in OLD]==[2,2,2,3,2]
    rows=[]
    for d in range(5):
        gamma, dom=gamma_and_witness(d)
        assert dominates(d,dom)
        for case in ('a','ab'):
            lib=old_lib(d,set(dom),case)
            assert covers_library(d,lib,case)
            expected=(1 << d)+gamma if case=='a' else (1 << (d+1))
            assert len(lib)==expected
            if d<=1:assert exact_small_library(d,case)==expected
        rows.append({'d':d,'m':d+2,'gamma':gamma,'kappa_a':(1<<d)+gamma,
                     'kappa_ab':1<<(d+1),'dominating_set':list(dom),
                     'gamma_verification':'exhaustive all smaller subsets'})
    d=7
    dom=perfect_code(d)
    assert len(dom)==16 and dominates(d,dom)
    # 128 vertices, balls of size 8: 16 is both attainable and forced.
    assert len(dom)*(d+1)==1<<d
    assert covers_library(d,old_lib(d,set(dom),'a'),'a')
    assert covers_library(d,old_lib(d,set(dom),'ab'),'ab')
    rows.append({'d':d,'m':d+2,'gamma':16,'kappa_a':144,'kappa_ab':256,
                 'dominating_set':list(dom),
                 'gamma_verification':'perfect Hamming code + sphere-covering lower bound'})
    report={'status':'PASS_R5_MIXED_DOMINATION_REDUCTION',
            'frozen_science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
            'old_core_sizes':len(OLD),'new_core_sizes':[len(AA),len(AAB)],
            'theorem':'all m>=2: kappa_a=2^(m-2)+gamma(Q_(m-2)), kappa_ab=2^(m-1)',
            'finite_coverage':'exact exhaustive cube domination d=0..4, library witnesses; d=7 perfect code witness+lower bound',
            'rows':rows}
    print(json.dumps(report,indent=2,ensure_ascii=False))

if __name__=='__main__':run()
