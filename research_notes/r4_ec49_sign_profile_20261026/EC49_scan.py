#!/usr/bin/env python3
"""Exact ratio-event scan for two-stage positive BRC K-memory ROC convex-hull preservation.
Uses only Python integers and Fraction.  Not a native X6 simulation.
"""
import itertools
import json
import random
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


def check_counts(P, Q):
    assert len(P) == len(Q) and len(P) > 0
    Y = len(P[0]); assert Y > 0
    assert all(len(a) == Y for a in P+Q)
    assert all(isinstance(x, int) and x > 0 for a in P+Q for x in a)
    M = sum(map(sum, P)); assert M == sum(map(sum, Q))
    return len(P), Y, M


def scan(P, Q):
    H, Y, M = check_counts(P, Q)
    group = defaultdict(dict)
    for h in range(H):
        for y in range(Y):
            r = Fraction(P[h][y], Q[h][y])
            group[r][h] = group[r].get(h, 0) | (1 << y)
    ratios = sorted(group)
    profiles = [0] * H
    freq = Counter(profiles)
    values = [len(freq)]
    for ratio in ratios:
        # Simultaneous updates within one tied ratio; never sample fake subchambers.
        for h, mask in group[ratio].items():
            old = profiles[h]
            new = old | mask
            if old == new:
                continue
            freq[old] -= 1
            if freq[old] == 0:
                del freq[old]
            freq[new] += 1
            profiles[h] = new
        values.append(len(freq))
    maximum = max(values)
    peak_chambers = [i for i, x in enumerate(values) if x == maximum]
    def fmt(x): return str(x.numerator) + '/' + str(x.denominator)
    return {
        'H':H, 'Y':Y,'M':str(M),'ratio_events':len(ratios),
        'max_distinct_profiles':maximum,
        'thresholds':[fmt(x) for x in ratios],
        'chamber_counts':values,
        'peak_chamber_indices':peak_chambers,
    }


def distinct_profiles(P, Q, lam):
    return len(set(tuple(P[h][y]*lam.denominator > Q[h][y]*lam.numerator for y in range(len(P[0]))) for h in range(len(P))))


def chromatic_conflict(P, Q, lam):
    H, Y, _ = check_counts(P,Q)
    signs = [[(P[h][y]*lam.denominator>Q[h][y]*lam.numerator) for y in range(Y)] for h in range(H)]
    edges = [(i,j) for i in range(H) for j in range(i+1,H) if any(signs[i][y]!=signs[j][y] for y in range(Y))]
    for K in range(1,H+1):
        for coloring in itertools.product(range(K), repeat=H):
            if all(coloring[i]!=coloring[j] for i,j in edges):
                return K
    assert False


def scan_chamber_samples(P, Q):
    r=sorted(set(Fraction(a,b) for pa,qa in zip(P,Q) for a,b in zip(pa,qa)))
    samples=[r[0]/2]+[(a+b)/2 for a,b in zip(r,r[1:])]+[r[-1]+1]
    return samples


def sharpness(r):
    H=1<<r
    P=[[2 if (h>>y)&1 else 1 for y in range(r)] for h in range(H)]
    Q=[[1 if (h>>y)&1 else 2 for y in range(r)] for h in range(H)]
    res=scan(P,Q)
    assert res['M']==str(3*r*(1<<(r-1)))
    assert distinct_profiles(P,Q,Fraction(1))==H
    assert res['max_distinct_profiles']==H
    return {'future_labels':r,'histories':H,'source_mass':res['M'],'convex_hull_memory':H,'full_region_memory':H, 'chamber_counts':res['chamber_counts']}


def tests():
    rng=random.Random(480049)
    regressions=0
    exact_chamber_comparisons=0
    brute_chromatic_comparisons=0
    for H in range(1,6):
      for Y in range(1,4):
        for trial in range(25):
          A=[[rng.randint(1,9) for _ in range(Y)] for _ in range(H)]
          B=[[rng.randint(1,9) for _ in range(Y)] for _ in range(H)]
          Sa=sum(map(sum,A));Sb=sum(map(sum,B))
          P=[[x*Sb for x in row] for row in A]
          Q=[[x*Sa for x in row] for row in B]
          result=scan(P,Q)
          samples=scan_chamber_samples(P,Q)
          counts=[distinct_profiles(P,Q,lam) for lam in samples]
          assert counts==result['chamber_counts']
          assert len(result['thresholds'])==len(samples)-1
          exact_chamber_comparisons+=len(samples)
          if H<=4:
            for lam in samples:
              assert chromatic_conflict(P,Q,lam)==distinct_profiles(P,Q,lam)
              brute_chromatic_comparisons+=1
          assert max(counts)==result['max_distinct_profiles']
          regressions+=1
    witness_P=[[3,12],[12,3],[6,6]]
    witness_Q=[[7,7],[7,7],[7,7]]
    witness=scan(witness_P,witness_Q)
    assert witness['M']=='42' and witness['max_distinct_profiles']==3
    assert witness['chamber_counts']==[1,3,3,1]
    sharp=[sharpness(r) for r in range(1,9)]
    return {
      'schema':'EM_R4_EC49_SIGN_PROFILE_SCAN_V1',
      'arithmetic':'positive integers, exact Fraction, simultaneous tied-ratio events',
      'random_seed':480049,
      'random_models':regressions,
      'exact_chamber_comparisons':exact_chamber_comparisons,
      'bruteforce_graph_chromatic_checks':brute_chromatic_comparisons,
      'nonmonotone_witness':{'P':witness_P,'Q':witness_Q,'scan':witness},
      'sharpness_instances':sharp,
      'all_checks':'PASS',
      'mathematics_status':'author-side proof; finite checks corroborate implementations only',
      'native_scope':'auxiliary two-stage positive BRC; no original X6 heartbeat update'
    }

if __name__=='__main__':
    result=tests()
    out=Path(__file__).with_name('EC49_REPORT.json')
    out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps({'all_checks':result['all_checks'],'random_models':result['random_models'],'chamber_comparisons':result['exact_chamber_comparisons'],'chromatic':result['bruteforce_graph_chromatic_checks'],'sharpness_r':len(result['sharpness_instances'])},ensure_ascii=False))
