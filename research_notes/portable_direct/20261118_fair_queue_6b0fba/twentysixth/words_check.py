"""Exact word-jet, exterior-power and formula-graph checks. No dependencies."""
from collections import defaultdict, Counter
from fractions import Fraction as Q
from functools import cache
from itertools import combinations, product
from math import prod
import json


def add_rows(v, w, t=1):
    return tuple(a+t*b for a,b in zip(v,w))


def poles_for_grade(n, grade):
    # Partial fractions for n! z^(grade-1) / product(z+i).
    return tuple(Q(prod(range(1,n+1))*(-i)**(grade-1),
                   prod(j-i for j in range(1,n+1) if j != i))
                 for i in range(1,n+1))


def symbol(grades):
    return prod(Q(a-b,a+b) for a,b in combinations(grades,2)) / Q(prod(grades))


def jet(form, d):
    return [sum(c*Q((-1)**r, i**(r+1)) for i,c in enumerate(form,1)) for r in range(d)]


def alternating(forms, d, q=0):
    # Recursion by first letter of the signed permutation. Each J acts by its Taylor integrand.
    zero = tuple(Q(0) for _ in range(d))
    jets = [jet(f,d) for f in forms]
    @cache
    def build(ids):
        if not ids:
            return tuple(Q(i==q) for i in range(d))
        out = list(zero)
        for pos,i in enumerate(ids):
            v = build(ids[:pos]+ids[pos+1:])
            g = jets[i]
            sign = (-1)**pos
            for r in range(1,d):
                out[r] += Q(sign,r)*sum(g[t]*v[r-1-t] for t in range(r))
        return tuple(out)
    return build(tuple(range(len(forms))))


def order(series):
    return next((i for i,v in enumerate(series) if v), None)


def exterior_checks():
    checked = 0
    for n in range(1,6):
        for k in range(1,min(4,n)+1):
            for gs in combinations(range(1,n+1),k):
                forms = [poles_for_grade(n,g) for g in gs]
                w = sum(gs)
                s = alternating(forms, w+2)
                assert order(s) == w and s[w] == symbol(gs)
                checked += 1
    basis = [(1,0,2,1), (0,2,-1,3), (1,0,0,1)]
    def det(m):
        if not m:
            return 1
        return sum((-1)**j*c*det([r[:j]+r[j+1:] for r in m[1:]]) for j,c in enumerate(m[0]))
    jets = [jet(f,4) for f in basis]
    # Greedy independent-column tuple is the lexicographically first nonzero maximal minor.
    es, delta = next((es,d) for es in combinations(range(4),3)
                     if (d:=det([[r[i] for i in es] for r in jets])))
    w = sum(es)+3
    a = alternating(basis,w+3)
    assert order(a)==w and a[w]==delta*symbol(tuple(i+1 for i in es))
    for q in range(w+1):
        b = alternating(basis,w+1,q)
        assert b == a[:w+1] if q==0 else not any(b)
    checked_input_orders = 0
    for grades in ((1,3),(1,2,4),(2,4,5),(1,3,4,5)):
        fs = [poles_for_grade(5,g) for g in grades]
        for q in range(7):
            wq = q+sum(grades)
            val = alternating(fs,wq+1,q)
            assert order(val)==wq and val[wq]*symbol(grades)>0
            checked_input_orders += 1
    return {"nonzero_successive_columns":checked_input_orders,"distinct_grade_sets":checked,
            "mixed_rows":{"pivot_columns":es,"jet_minor":str(delta),
                          "order":w,"first":str(a[w]),"all_columns_tested":w+1}}


def two_form_space():
    n, d = 4, 12
    forms = [poles_for_grade(n,g) for g in range(1,n+1)]
    names = list(combinations(range(n),2))
    columns = [alternating([forms[i],forms[j]],d) for i,j in names]
    echelon = {}
    for j, col in enumerate(columns):
        coef = tuple(Q(i==j) for i in range(len(names)))
        for pivot, (row, comb) in sorted(echelon.items()):
            t = col[pivot]
            col, coef = add_rows(col,row,-t), add_rows(coef,comb,-t)
        p = order(col)
        assert p is not None
        pivot_q = col[p]
        echelon[p] = tuple(x/pivot_q for x in col), tuple(c/pivot_q for c in coef)
    highest = max(echelon)
    a = echelon[highest][1]
    # The 2-form is decomposable iff its Pfaffian vanishes, in dimension four.
    pf = a[0]*a[5]-a[1]*a[4]+a[2]*a[3]
    assert pf != 0
    assert add_rows((0,)*d,tuple(sum(a[j]*columns[j][i] for j in range(6)) for i in range(d))) == echelon[highest][0]
    primitive = (0,0,-288,1296,180,19)
    assert tuple(16*t for t in primitive)==a
    degree_six = sum(c*alternating([forms[i],forms[j]],7,1)[6] for c,(i,j) in zip(primitive,names))
    assert degree_six==Q(-18,5)
    return {"primitive_witness":primitive,"witness_first_column_leading":"1/16",
            "witness_input_z_coeff_z6":str(degree_six),"pole_labels":[1,2,3,4],"grade_pairs":[[i+1,j+1] for i,j in names],
            "pivot_orders":sorted(echelon),"unit_leading_vector":[str(x) for x in a],
            "pfaffian":str(pf),"highest_order":highest}


def plus(f,g):
    h = Counter(f)
    h.update(g)
    return {w:c for w,c in h.items() if c}


def times(f,g):
    h = Counter()
    for u, a in f.items():
        for v, b in g.items():
            h[u+v] += a*b
    return {w:c for w,c in h.items() if c}


def formula_checks():
    def trees(labels):
        if len(labels)==1:
            yield labels[0]
        for i in range(1,len(labels)):
            for u,v,op in product(trees(labels[:i]),trees(labels[i:]),('+','*')):
                yield op,u,v

    def algebra(t):
        if isinstance(t,str):
            return {(t,):1} if t.startswith('x') else {():int(t)}
        op,u,v=t
        return (plus if op=='+' else times)(algebra(u),algebra(v))

    tests = 0
    zeros = 0
    for labels in [('x1','x2','x1','x3'), ('-1','x1','x1','0'), ('2','x2','-2','x2')]:
        for tree in trees(labels):
            edges = defaultdict(list)
            next_node = 2
            def build(t, a, b):
                nonlocal next_node
                if isinstance(t,str):
                    edges[a].append((b,algebra(t)))
                    return 0
                op,u,v = t
                if op == '+':
                    return build(u,a,b)+build(v,a,b)
                c=next_node
                next_node+=1
                return 1+build(u,a,c)+build(v,c,b)
            mults = build(tree,0,1)
            assert next_node == mults+2
            @cache
            def paths(a):
                if a==1:
                    return {():1}
                f={}
                for b,l in edges[a]:
                    f=plus(f,times(l,paths(b)))
                return f
            expected = algebra(tree)
            assert expected == paths(0)
            zeros += not expected
            tests += 1
    return {"four_leaf_formulas":tests,"zero_polynomials":zeros}


def universal_quadratic_check():
    p=1009
    def rank(cols, d):
        piv={}
        for vec in cols:
            v=[vec[r][q] for r in range(d) for q in range(r+1)]
            for i in sorted(piv):
                if v[i]:
                    t=v[i]
                    v=[(a-t*b)%p for a,b in zip(v,piv[i])]
            i=next((j for j,a in enumerate(v) if a),None)
            if i is not None:
                inv=pow(v[i],-1,p)
                piv[i]=[(a*inv)%p for a in v]
        return len(piv)
    out=[]
    for n in range(1,9):
        d=2*n+1
        eye=[[int(q==r) for q in range(d)] for r in range(d)]
        ts=[[[(-1)**(r-q-1)*pow(r*i**(r-q),-1,p)%p if q<r else 0
              for q in range(d)] for r in range(d)] for i in range(1,n+1)]
        products=[[[sum(l[r][a]*h[a][q] for a in range(q+1,r))%p
                    for q in range(d)] for r in range(d)] for l in ts for h in ts]
        anti=[[[ (products[i*n+j][r][q]-products[j*n+i][r][q])%p
                for q in range(d)] for r in range(d)] for i,j in combinations(range(n),2)]
        cols=[eye]+ts+products
        pair_weights = Counter(i+j for i in range(1,n+1) for j in range(1,n+1))
        pair_weights.update([0]+list(range(1,n+1)))
        antisym_weights = Counter(i+j for i,j in combinations(range(1,n+1),2))
        for size in range(1,d+1):
            def predicted(weights):
                return sum(min(count,max(0,size-w)) for w,count in weights.items())
            assert rank(cols,size)==predicted(pair_weights)
            assert rank(anti,size)==predicted(antisym_weights)
        ranks=[rank(cols,d-1),rank(cols,d),rank(anti,d-2),rank(anti,d-1)]
        assert ranks[0]<len(cols) and ranks[1]==len(cols)
        if n>1:
            assert ranks[2]<len(anti) and ranks[3]==len(anti)
        out.append([n]+ranks)
    return {"field":p, "truncations_per_space_checked":sum(2*n+1 for n in range(1,9)),
            "columns":["n","all_d=2n","all_d=2n+1","alternating_d=2n-1","alternating_d=2n"],
            "n_and_ranks_at_two_neighboring_cutoffs":out}


def modular_boundary():
    # Truncated p-by-p matrices are defined through degree p-1.
    p=3
    def apply(i,v):
        return tuple(sum((-1)**(r-q-1)*pow(r*i**(r-q),-1,p)*v[q] for q in range(r))%p
                     for r in range(p))
    for j in range(p):
        v=tuple(int(j==i) for i in range(p))
        assert apply(1,apply(2,v))==apply(2,apply(1,v))
    fs = [poles_for_grade(4,g) for g in (1,2,4)]
    q2 = alternating(fs,10,2)[9]
    assert q2 == Q(-11,30240) and q2.denominator%11 != 0
    rank_columns = []
    for q in range(3):
        v = alternating(fs,10,q)
        rank_columns.append([a.numerator*pow(a.denominator,-1,11)%11 for a in v])
    assert all(c==0 for c in rank_columns[2])
    assert rank_columns[0][7] != 0 and rank_columns[1][8] != 0
    return {"p":p,"d":p,"commutator_zero_columns":p,"degree_p_integrand_obstruction":1,
            "rank_counterexample":{"p":11,"d":10,"grades":[1,2,4],"q":2,
                                   "rational_coeff_z9":str(q2),"rank_over_F11":2,"rank_over_Q":3}}


if __name__=="__main__":
    print(json.dumps({"alternating":exterior_checks(),"full_exterior_square":two_form_space(),
                      "quadratic_full_matrices":universal_quadratic_check(),"formula_graphs":formula_checks(),"positive_characteristic":modular_boundary()}, indent=2))
