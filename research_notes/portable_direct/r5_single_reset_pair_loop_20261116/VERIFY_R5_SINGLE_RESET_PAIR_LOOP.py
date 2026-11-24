#!/usr/bin/env python3
"""Source-labelled one-bit Set control: exact pair-loop certificates.
Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Standard library checks always run; --milp invokes SciPy/HiGHS for optima.
"""
import argparse
import json

PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
PAIR8 = [(87,87),(93,93),(107,107),(111,111),(117,117),(123,123),
         (127,127),(173,173),(174,175),(182,183),(189,189),(213,213),
         (218,219),(222,223),(237,237),(246,247),(250,251),(254,255)]
STATIC8 = [91,95,109,111,123,125,171,174,181,183,186,189,191,
           213,214,219,222,223,234,237,246,247,251,254,255]
STATIC9 = [119,171,183,189,191,205,213,219,229,235,247,254,255,
           347,349,351,362,365,367,372,374,379,381,427,430,437,439,
           442,446,447,462,463,466,470,475,477,491,493,502,503,505,510,511]
PAIR9 = [(127,127),(151,151),(175,175),(187,187),(215,215),(221,221),
         (223,223),(233,233),(235,235),(245,245),(247,247),(251,251),
         (341,341),(346,347),(350,351),(365,365),(366,367),(373,373),
         (378,379),(421,421),(426,427),(429,429),(438,439),(445,445),
         (446,447),(469,469),(474,475),(493,493),(494,495),(502,503),
         (508,509),(510,511)]


def q(x, k):
    return sum(((x >> i) & 1) * ((x >> ((i+1) % k)) & 1)
               for i in range(k))


def feasible(r, u, k, slack=2):
    return (u & ~r) == 0 and 0 <= q(r,k) - q(u,k) <= slack


def check_static(k, centers):
    raw = 1 << k
    assert all(0 <= r < raw for r in centers)
    assert len(set(centers)) == len(centers)
    assert all(any(feasible(r,u,k) for r in centers) for u in range(raw))
    return {'k': k, 'centers': len(centers), 'masks_checked': raw,
            'all_cover': True, 'source_library_cost': '5*k+q(center)'}


def check_pair_loop(k, pairs):
    """Each pair has one state when centres equal; otherwise two reset-linked states."""
    half = 1 << (k-1)
    assigned = [[] for _ in pairs]
    for y in range(half):
        choices = [i for i,(a,b) in enumerate(pairs)
                   if feasible(a,2*y,k) and feasible(b,2*y+1,k)]
        assert choices, ('uncovered fiber', k, y)
        assigned[choices[0]].append(y)
    # Empty candidate pairs are harmless but should not be part of the witness.
    assert all(assigned)
    check_count = reset_check_count = 0
    states = []
    for i, ((a,b),ys) in enumerate(zip(pairs,assigned)):
        if a == b:
            for y in ys:
                for v in (2*y,2*y+1):
                    assert feasible(a,v,k)
                    check_count += 1
                    for bit in (0,1):
                        assert feasible(a,(v & ~1)|bit,k)
                        reset_check_count += 1
            states.append({'pair':i,'centers':[a], 'fibers':len(ys),
                           'transitions':{'set0':i,'set1':i}})
        else:
            for y in ys:
                for bit,r in ((0,a),(1,b)):
                    assert feasible(r,2*y+bit,k)
                    check_count += 1
                    for new_bit,new_r in ((0,a),(1,b)):
                        assert feasible(new_r,2*y+new_bit,k)
                        reset_check_count += 1
            states.append({'pair':i,'centers':[a,b], 'fibers':len(ys),
                           'transitions':'set_b maps both states to its pair state b'})
    count = sum(1 if a == b else 2 for a,b in pairs)
    assert sum(map(len,assigned)) == half
    assert count == (25 if k==8 else 44 if k==9 else count)
    return {'k':k,'raw_masks':2*half,'fibers':half,'pairs':len(pairs),
            'controller_states':count,'inert_states':sum(a==b for a,b in pairs),
            'reset_linked_pairs':sum(a!=b for a,b in pairs),
            'source_checks':check_count,'reset_checks':reset_check_count,
            'complete_cover':True,'transition_closed':True,
            'pair_fiber_counts':[len(x) for x in assigned]}


def solve(k, mode):
    import numpy as np
    from scipy.optimize import milp, Bounds, LinearConstraint
    from scipy.sparse import lil_matrix
    n = 1 << k
    size = n if mode == 'static' else n//2
    covers = {}
    if mode == 'static':
        for r in range(n):
            cover = sum(1 << u for u in range(n) if feasible(r,u,k))
            covers[cover] = min(covers.get(cover,(2,r)), (1,r))
    elif mode == 'paired-loop':
        lo = [sum(1 << y for y in range(size) if feasible(r,2*y,k)) for r in range(n)]
        hi = [sum(1 << y for y in range(size) if feasible(r,2*y+1,k)) for r in range(n)]
        for a in range(n):
            if not lo[a]: continue
            for b in range(n):
                cover = lo[a] & hi[b]
                if cover:
                    cost = 1 if a == b else 2
                    covers[cover] = min(covers.get(cover,(3,a,b)),(cost,a,b))
    else: raise ValueError(mode)
    candidates = [(v,w) for v,w in covers.items() if v]
    # Dominance with costs: a smaller covered subset is unnecessary if a
    # superset candidate costs no more. This preserves exact optimum.
    candidates = [(v,w) for v,w in candidates
                  if not any(v != t and v & t == v and w[0] >= z[0]
                             for t,z in covers.items())]
    A = lil_matrix((size,len(candidates)),dtype=float)
    for j,(v,w) in enumerate(candidates):
        for i in range(size):
            if v >> i & 1: A[i,j]=1.0
    opt = milp(c=np.array([w[0] for v,w in candidates],dtype=float),
               integrality=np.ones(len(candidates),dtype=int),
               bounds=Bounds(np.zeros(len(candidates)),np.ones(len(candidates))),
               constraints=LinearConstraint(A.tocsr(),np.ones(size),np.inf),
               options={'mip_rel_gap':0.0,'time_limit':120.0})
    if opt.x is None: raise RuntimeError(str(opt.message))
    chosen = [candidates[i][1] for i,x in enumerate(opt.x) if x > 0.5]
    assert sum(c[0] for c in chosen) == round(opt.fun)
    union = 0
    for i,x in enumerate(opt.x):
        if x > 0.5: union |= candidates[i][0]
    assert union == (1<<size)-1
    assert opt.status == 0 and opt.mip_gap == 0
    return {'k':k,'kind':mode,'candidate_count':len(candidates),
            'optimal_integer':round(opt.fun),'solver_status':int(opt.status),
            'solver_gap':float(opt.mip_gap),'dual_bound':float(opt.mip_dual_bound),
            'selected_count':len(chosen)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--milp',action='store_true')
    args = p.parse_args()
    result = {'status':'PASS_R5_SINGLE_RESET_PAIRED_LOOP',
              'frozen_science_pin':PIN,
              'assumptions':{'q':'sum cyclic adjacent unavailable pairs',
                             'slack':2,'commands':['Set_0(0)','Set_0(1)'],
                             'source_library':'canonical genuine source-labelled L(r)'},
              'verified_upper':[check_pair_loop(8,PAIR8),check_pair_loop(9,PAIR9)],
              'verified_static_upper':[check_static(8,STATIC8),check_static(9,STATIC9)],
              'selected_static8':STATIC8,'selected_pairs8':PAIR8,
              'selected_static9':STATIC9,'selected_pairs9':PAIR9}
    if args.milp:
        result['solver']=[solve(k,mode) for k in (8,9)
                          for mode in ('static','paired-loop')]
        assert [s['optimal_integer'] for s in result['solver']] == [25,25,43,44]
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__ == '__main__':main()
