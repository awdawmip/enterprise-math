"""Common labelled partitions, simultaneous erasures and coherent mark substitutions."""
from collections import defaultdict
from functools import cache
from itertools import combinations
from math import lcm
import json


def canonical(values):
    names = {}
    return tuple(names.setdefault(x,len(names)) for x in values)


def subsets(s):
    for k in range(len(s)+1):
        yield from combinations(s,k)


def signature(positions, order):
    return canonical(v % order for v in positions)


def agreement(n, orders):
    h, period = min(orders), lcm(*orders)
    q, t = divmod(n,period)
    return h*q+min(h,t)


def representatives(horizon, size):
    yield from combinations(range(1,horizon+1),size)
    for rs in combinations(range(1,horizon+1),size-1):
        base = lcm(*rs)
        yield rs+(base*(horizon//base+1),)


def all_target_consensus(n, horizon, size):
    return max(agreement(n,rs) for rs in representatives(horizon,size))


def exhaustive_common(n, periods):
    best = {}
    for marks in subsets(range(n)):
        by_signature = defaultdict(list)
        for r in periods:
            by_signature[signature(marks,r)].append(r)
        for group in by_signature.values():
            for k in range(2,min(4,len(group))+1):
                for rs in combinations(group,k):
                    best[rs] = max(best.get(rs,0),len(marks))
    return best


def partitions(k):
    if k == 0:
        yield ()
        return
    for previous in partitions(k-1):
        for label in range(max(previous,default=-1)+2):
            yield previous+(label,)


@cache
def spoiled_distance(p, q):
    # Definition using only equalities; never compare the numeric block names.
    for errors in range(len(p)+1):
        for clean in combinations(range(len(p)),len(p)-errors):
            if canonical(p[i] for i in clean) == canonical(q[i] for i in clean):
                return errors


def unique_by_reports(marks, horizon, erasures, changes):
    for deleted in combinations(marks, min(erasures,len(marks))):
        kept = tuple(x for x in marks if x not in deleted)
        all_orders = range(1,max([horizon,*marks])+2)
        patterns = [(min(r,horizon+1),signature(kept,r)) for r in all_orders]
        for report in partitions(len(kept)):
            possible = {label for label,p in patterns if spoiled_distance(p,report)<=changes}
            if len(possible)>1:
                return False
    return True


def prime(p):
    return p>=2 and all(p%d for d in range(2,int(p**0.5)+1))


def first_erasure(marks, horizon):
    A=max(marks,default=0)
    scores = []
    for r in range(1,horizon+1):
        for p in {2}|{p for p in range(2,A//r+1) if prime(p)}:
            nested = defaultdict(lambda:defaultdict(int))
            for x in marks:
                nested[x%r][x%(p*r)] += 1
            scores.append(len(marks)-sum(max(v.values()) for v in nested.values()))
    return min(scores)


def main():
    count = 0
    list_checks = 0
    for n in range(1,11):
        periods=tuple(range(1,12))
        brute = exhaustive_common(n,periods)
        for rs,z in brute.items():
            assert z == agreement(n,rs)
        count += len(brute)
        for horizon in range(1,min(n,6)+1):
            for size in range(2,min(4,horizon+1)+1):
                candidates = [z for rs,z in brute.items() if len(rs)==size and
                              len({min(r,horizon+1) for r in rs})==size]
                assert max(candidates) == all_target_consensus(n,horizon,size)
                list_checks += 1
    threshold_checks = 0
    sample_rows = []
    for horizon in range(1,16):
        for size in range(2,min(7,horizon+1)+1):
            b, rs = min((lcm(*rs)//min(rs), rs) for rs in representatives(horizon,size))
            assert (b==size) == (lcm(*range(1,size+1))<=2*horizon)
            sample_rows.append({"H":horizon,"labels":size,"B":b,"minimizing_orders":rs})
            threshold_checks += 1
    pair_checks = 0
    for n in range(1,80):
        for r in range(1,31):
            assert all(agreement(n,(r,s))<=agreement(n,(r,2*r))
                       for s in range(1,66) if s!=r)
            pair_checks+=1
    tests=0
    for marks in subsets((0,1,2,3,4,5)):
        if not marks: continue
        for horizon in range(1,5):
            d=first_erasure(marks,horizon)
            for e in range(2):
                for t in range(2):
                    assert unique_by_reports(marks,horizon,e,t) == (e+2*t<d)
                    tests += 1
    mixed=(0,1,0,2,0,1)
    r2=signature(range(6),2)
    r4=signature(range(6),4)
    assert spoiled_distance(mixed,r2)==spoiled_distance(mixed,r4)==1
    assert signature((0,1,2,3,8,9,10,11),4)==signature((0,1,2,3,8,9,10,11),8)
    assert signature((0,3,6),1)==signature((0,3,6),3)!=signature((0,3,6),2)
    assert signature(range(5),4)!=signature(range(5),5)
    print(json.dumps({"n1_to_10_order_tuple_checks":count,"list_label_exhaustive_checks":list_checks,
                      "finite_lcm_threshold_checks":threshold_checks,"nearest_double_checks":pair_checks,
                      "direct_coherent_report_checks":tests,"examples_B":sample_rows,
                      "polluted_word_example":{"positions":list(range(6)),"reported":mixed,
                                               "order2":r2,"order4":r4},
                      "three_way_example_n30":{"pair_costs":[30-agreement(30,rs) for rs in
                                                [(1,2),(1,3),(2,3)]],"common_cost":30-agreement(30,(1,2,3))}},
                      indent=2,sort_keys=True))


if __name__=="__main__":
    main()
