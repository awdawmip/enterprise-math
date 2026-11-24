"""Exact finite checks for a two-language mixed R5 center-repair theorem.
Only integer set differences, bit-count Hamming distances and exhaustive finite covering.
Scientific parent frozen at 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
from itertools import combinations
from functools import lru_cache
import json

OLD = tuple(frozenset(map(int, s)) for s in ('0125','0135','0235','0245','0246'))
A = tuple(frozenset(map(int, s)) for s in ('1235','1245','1246','1345','1346'))
AB = tuple(frozenset(map(int, s)) for s in ('1235','1236','1245','1246','1345','1346'))

def distance(new_core, old_index, ss, old_ss, v, u):
    return len(new_core - OLD[old_index]) + int(ss != old_ss) + (v ^ u).bit_count()

def library_ok(Y, library, case):
    new = A if case == 'a' else AB
    for core in new:
        ss = int(2 in core)
        for v in Y:
            if not any(distance(core,j,ss,old_ss,v,u) <= 2 for j,old_ss,u in library):
                return False
    return True

def exact_min_cover(d, X, Y, case):
    """Exhaustive branch-and-bound set cover; only called for d<=3."""
    assert d <= 3
    new = A if case == 'a' else AB
    targets = [(c,int(2 in c),v) for c in new for v in Y]
    old = [(j,ss,u) for j in range(5) for ss in range(2) for u in X]
    coverage = {}
    for row in old:
        j,old_ss,u = row
        mask = sum(1 << i for i,(c,ss,v) in enumerate(targets)
                   if distance(c,j,ss,old_ss,v,u) <= 2)
        if mask:coverage.setdefault(mask,row)
    masks = [mask for mask in coverage
             if not any(mask != nxt and mask & nxt == mask for nxt in coverage)]
    goal=(1 << len(targets))-1
    assert (sum([0]) | (0 if not masks else __import__('functools').reduce(lambda x,y:x|y,masks)))==goal
    target_to_masks = [tuple(i for i,m in enumerate(masks) if (m >> t)&1)
                       for t in range(len(targets))]
    best = [len(masks)+1,()]
    seen = {}
    def rec(done, chosen):
        if done == goal:
            if len(chosen)<best[0]:best[:]=len(chosen),tuple(coverage[masks[i]] for i in chosen)
            return
        if len(chosen)>=best[0] or seen.get(done,1<<30)<=len(chosen):return
        seen[done]=len(chosen)
        t=min((t for t in range(len(targets)) if not done>>t&1),
              key=lambda t:len(target_to_masks[t]))
        for i in sorted(target_to_masks[t],key=lambda j:-((masks[j]&~done).bit_count())):
            rec(done|masks[i],chosen+[i])
    rec(0,[])
    assert library_ok(Y,best[1],case)
    return best[0], [list(row) for row in best[1]]

def run():
    # Suffix vertex e_i is the length-d binary unit vector 1<<i.
    matrix = [[len(c-o) for o in OLD] for c in AB]
    assert matrix == [[1,1,1,2,3],[2,2,2,3,2],[1,2,2,1,2],
                      [2,3,3,2,1],[2,1,2,2,3],[3,2,3,3,2]]
    rows=[]
    for r in range(3,9):
        d=r
        Y=[1<<i for i in range(r)]
        old_restricted=[(1,0,v) for v in Y]+[(0,1,v) for v in Y]
        old_ambient=[(1,0,v) for v in Y]+[(0,1,0),(4,1,0)]
        assert library_ok(Y,old_restricted,'a')
        assert library_ok(Y,old_restricted,'ab')
        assert library_ok(Y,old_ambient,'a')
        # Forced E=1346 core at each target has only O1/O4 with s0 same v.
        E=frozenset((1,3,4,6)); B=frozenset((1,2,4,5))
        for v in Y:
            eligible=[(j,s,u) for j in range(5) for s in (0,1)
                      for u in (range(1<<d) if d<=5 else [0,*Y])
                      if distance(E,j,0,s,v,u)<=2]
            assert set(eligible)=={(1,0,v),(4,0,v)}
            assert all(distance(B,j,1,0,v,v)>2 for j in (1,4))
        # For r>=3, the unique suffix within distance <=1 of every e_i is 0.
        if d <= 5:
            assert [u for u in range(1<<d) if all((u^v).bit_count()<=1 for v in Y)]==[0]
        rows.append({'r':r,'d':d,'restricted_a':2*r,'ambient_a':r+2,'ambient_ab':2*r,
                     'restricted_witness':len(old_restricted),
                     'ambient_witness':len(old_ambient),'witness_checks':'PASS'})
    d=3;Y=[1,2,4]
    exact={}
    for X_name,X in [('restricted',Y),('ambient',list(range(1<<d)))]:
        for case in ('a','ab'):
            size,witness=exact_min_cover(d,X,Y,case)
            exact[f'{X_name}_{case}']={'size':size,'witness':witness}
    assert [exact[f'{x}_{t}']['size'] for x,t in
            [('restricted','a'),('ambient','a'),('restricted','ab'),('ambient','ab')]]==[6,5,6,6]
    report={'status':'PASS_R5_AMBIENT_OLD_HELPER_GAP',
            'frozen_science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
            'model':'auxiliary mixed weighted optimizer languages; exact indexed-center replacement metric',
            'theorem':'r>=3, d>=r: kappa_a(X=Y)=2r; kappa_a(X=Q_d)=r+2; kappa_ab both=2r, Y={unit vectors e_i:i<r}',
            'core_distance_matrix_ab':matrix,
            'exact_3bit_full_set_cover':exact,
            'constructive_witness_r_3_to_8':rows,
            'proof_scope':'universal r>=3,d>=r via forced-baseline and one-helper contradiction; finite checks are not universal proof',
            'next_question':'characterize general old X/new Y with graph-annotated states and a future-observer-preserving quotient'}
    print(json.dumps(report,indent=2,sort_keys=True,ensure_ascii=False))
if __name__=='__main__':run()
