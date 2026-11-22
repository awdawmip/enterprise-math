#!/usr/bin/env python3
"""R762JE: all remaining t<=10, z>0 46-event Port-Euler terminal histograms.

Run alongside R762JC_SEVEN_TRIPLE_46_44.py and
R762JD_THREE_FULL_SUPPORT_CLASSES.py. NumPy+SciPy/HiGHS propose witnesses;
exact integer degree, support, active-set and BFS validators check each.
"""
from itertools import combinations
from collections import Counter
from R762JD_THREE_FULL_SUPPORT_CLASSES import essential_reps
from R762JC_SEVEN_TRIPLE_46_44 import T, solve, verify_exact

def allowed_inactive(counts, inactive):
    active=set(range(15))-set(inactive)
    return all(sum(p in active for p in T[s])>=2
               for s in range(20) if counts[s]>0)

def run_case(t,z,s,expected):
    assert 3*t + s + 2*(20-t-z-s)==46
    all_essential,reps=essential_reps(t)
    tested=represented=impossible=0
    inactive_sizes=Counter();cut_rounds=Counter()
    for mask,orbit_size in reps:
        triples=[i for i in range(20) if mask>>i&1]
        unused=sorted(set(range(15))-{v for j in triples for v in T[j]})
        other=[i for i in range(20) if i not in triples]
        for zeros in combinations(other,z):
            nonzero_rest=[i for i in other if i not in zeros]
            for ones in combinations(nonzero_rest,s):
                counts=[3 if i in triples else 0 if i in zeros else
                        1 if i in ones else 2 for i in range(20)]
                assert sum(counts)==46
                for size in range(len(unused)+1):
                    for inactive in combinations(unused,size):
                        if not allowed_inactive(counts,inactive):
                            # A positive support with <2 active Ports cannot
                            # contribute an event in an original legal history.
                            impossible+=1
                            continue
                        result=None
                        # A supporting triple need not be lexicographically first.
                        for j in triples:
                            c=counts.copy();c[j]=1
                            try:
                                x,rounds=solve(c,inactive)
                            except AssertionError:
                                continue
                            verify_exact(x,c,inactive)
                            result=(j,rounds)
                            break
                        assert result is not None,(t,z,s,triples,zeros,ones,inactive)
                        tested+=1;represented+=orbit_size
                        inactive_sizes[len(inactive)]+=1
                        cut_rounds[result[1]]+=1
    observed=(all_essential,len(reps),tested,represented,impossible,
              dict(inactive_sizes),dict(cut_rounds))
    assert observed==expected,(t,z,s,observed,expected)
    print(f'PASS {(t,20-t-z-s,s,z)}: '
          f'essential={all_essential} orbits={len(reps)} '
          f'valid_witnesses={tested} labelled={represented} '
          f'locally_impossible={impossible} '
          f'inactive={dict(sorted(inactive_sizes.items()))} '
          f'cuts={dict(sorted(cut_rounds.items()))}',flush=True)

def main():
    # Full algebraic census: every length-46 histogram in {0,1,2,3}^20.
    all_histograms=[(t,d,s,z)
        for t in range(21) for d in range(21-t)
        for s in range(21-t-d) for z in [20-t-d-s]
        if 3*t+2*d+s==46]
    assert len(all_histograms)==24
    low=[h for h in all_histograms if h[0]<=10]
    assert low==[(6,14,0,0),(7,12,1,0),(8,10,2,0),
                (8,11,0,1),(9,8,3,0),(9,9,1,1),
                (10,6,4,0),(10,7,2,1),(10,8,0,2)]
    checks={
      (8,1,0):(4920,16,301,82980,11,{0:192,1:96,2:13},{0:290,1:11}),
      (9,1,1):(240,2,330,33000,0,{0:220,1:110},{0:327,1:3}),
      (10,1,2):(6,1,360,2160,0,{0:360},{0:359,1:1}),
      (10,2,0):(6,1,45,270,0,{0:45},{0:44,1:1}),
    }
    for (t,z,s),expected in checks.items():run_case(t,z,s,expected)
    print('PASS R762JE: 1036/1036 exact Euler witnesses, four missing-support classes; '
          'all 24 length-46 histograms classified by reduction dependencies')
if __name__=='__main__':main()
