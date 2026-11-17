#!/usr/bin/env python3
"""Certified near-D4/2 minimax adaptive absolute-noise budget cost, stdlib only."""
import hashlib, itertools, json, pathlib, sys
COHORT_SHA="a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d"
TABLE_SHA="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
PIN="435e77af0d180eac32bd1f9c4c464bc4010b7551"
D4=1882951873548292168718745600000
E=range(214,222); M=range(223,292); L=range(293,315)

def get(p,sha):
    b=pathlib.Path(p).read_bytes();assert hashlib.sha256(b).hexdigest()==sha
    return json.loads(b)

def maximal_ambiguous(s, k, n):
    """Maximal common-y intersections when 2eta=D4-1, exact integer centers."""
    a=sorted((n[k][b],b) for b in s)
    subsets=set(); j=0
    for i,(v,b) in enumerate(a):
        j=max(j,i)
        while j<len(a) and a[j][0]-v<D4:j+=1
        subset=frozenset(t for _,t in a[i:j])
        if len(subset)>1:subsets.add(subset)
    return sorted((x for x in subsets if not any(x<y for y in subsets)),key=lambda x:(-len(x),tuple(sorted(x))))

def separated(s, ks, n):
    return all(any(abs(n[k][a]-n[k][b])>=D4 for k in ks) for a,b in itertools.combinations(s,2))

def run(c,t):
    assert c['scientific_input']==PIN and PIN in t['scope']
    n={}
    for k in range(214,315):
        A={int(z):int(v) for z,v in c['all_budget_coefficients'][str(k)].items()}
        n[k]=[sum(v for z,v in A.items() if z&b==z) for b in range(256)]
        assert n[k]==[int(z) for z in t['counts_and_cohorts'][str(k)]['counts']]
    # A rectangular 16x2x2 hard fibre, with disjoint readout windows.
    S=[lo|late|middle for lo in range(16) for late in (16,32) for middle in (0,64)]
    for lo in range(16):
        for k in E:
            assert len({n[k][lo|late|middle] for late in (16,32) for middle in (0,64)})==1
        for k in M:
            for middle in (0,64):
                assert len({n[k][llo|late|middle] for llo in range(16) for late in (16,32)})==1
        for k in L:
            for late in (16,32):
                assert len({n[k][llo|late|middle] for llo in range(16) for middle in (0,64)})==1
    m_first=next(k for k in M if abs(n[k][16]-n[k][80])>=D4)
    l_first=next(k for k in L if abs(n[k][16]-n[k][32])>=D4)
    assert (m_first,l_first)==(224,298)
    fibre=list(range(16));early=[]
    for first in E:
        kids=maximal_ambiguous(fibre,first,n)
        per=[(tuple(sorted(s)),next((k for k in E if separated(s,[k],n)),None)) for s in kids]
        feasible=all(k is not None for s,k in per)
        second_max=max((k for s,k in per),default=0) if feasible else None
        cost=first+second_max if second_max else (first if feasible else None)
        early.append(dict(first=first,child_count=len(kids),feasible=feasible,
                          worst_second=second_max,worst_cost=cost))
    finite=[p for p in early if p['worst_cost'] is not None]
    best=min(p['worst_cost'] for p in finite)
    assert best==433
    assert [(q['first'],q['worst_cost']) for q in finite]==[(215,433),(217,435),(218,435),(219,436)]

    full=maximal_ambiguous(list(range(256)),215,n)
    detail=[]
    for s in full:
        second=next((k for k in E if separated(s,[k,224,298],n)),None)
        assert second is not None and second<=218
        detail.append(dict(maximal_masks=sorted(s),size=len(s),second_early_budget=second))
    assert len(full)==19 and max(p['second_early_budget'] for p in detail)==218
    assert sorted([p['second_early_budget'] for p in detail])==sorted([214]*5+[216]*7+[217]*5+[218]*2)
    assert not separated(list(range(256)),[215,224,298],n)
    return dict(status='PASS_R5_SHARP_ADAPTIVE_NEAR_D4_BUDGET_COST',scientific_input=PIN,
                eta_range='(D4-1)/2 <= eta < D4/2',D4=str(D4),full_count_checks=25856,
                hard_fibre_count=len(S),hard_fibre_m_first=m_first,hard_fibre_l_first=l_first,
                early_fibre_first_budget_certificate=early,early_fibre_minimax_sum=best,
                lower_bound=best+m_first+l_first,full_256_maximal_first_response_sets=len(full),
                full_strategy=dict(first_budget=215,second_early_conditional=detail,
                                   third_and_fourth_fixed=[224,298],worst_cost=215+218+224+298),
                interpretation='zero-error adversarial real-interval observations, arbitrary adaptive order; sharp for near-D4/2 interval only')

if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit('usage: python VERIFY_R5_ADAPTIVE_COST.py compact_stdout.json EXACT_R5_ALL_101_BUDGETS.json')
    print(json.dumps(run(get(sys.argv[1],COHORT_SHA),get(sys.argv[2],TABLE_SHA)),indent=2,ensure_ascii=False))
