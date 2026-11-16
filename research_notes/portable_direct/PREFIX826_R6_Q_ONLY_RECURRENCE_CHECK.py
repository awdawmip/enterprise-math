#!/usr/bin/env python3
"""PREFIX-826 reproducible exact checks; Python stdlib only, integer arithmetic."""
import json
from collections import defaultdict
from itertools import combinations
from math import comb, factorial

def moment_operator(q, a, b):
    u = [('U', k, h) for k in range(q+1) for h in range(k+1)]
    v = [('V', k, h) for k in range(q) for h in range(k+1)]
    names = u + v
    ids = {x:i for i,x in enumerate(names)}
    edges = [[] for _ in names]
    observations = [[] for _ in range(q+1)]
    for (typ,k,h),i in ids.items():
        if typ == 'U':
            if k < q:
                edges[i].extend([(ids['U',k+1,h+1],h+1), (ids['V',k,h],b)])
            if h == 0:
                observations[k].append(i)
        else:
            if k < q-1:
                edges[i].append((ids['V',k+1,h+1],h+1))
            edges[i].append((ids['U',k,h],a))
            if h == 0:
                observations[k+1].append(i)
    return names, edges, observations

def mv(edges, vec):
    return [sum(w*vec[j] for j,w in row) for row in edges]

def eval_polynomial(edges, vec, q, z, extra_x=False):
    powers = [vec]
    for _ in range(q):
        powers.append(mv(edges, mv(edges, powers[-1])))
    out = [sum(comb(q,j)*(-z)**(q-j)*powers[j][i]
               for j in range(q+1)) for i in range(len(vec))]
    return mv(edges, out) if extra_x else out

def cv(rows, v):
    return tuple(sum(v[j] for j in row) for row in rows)

def named_states(q, m):
    states = []
    for mark in (0,1):
        for k in range(q-mark+1):
            for subset in combinations(range(m), k):
                states.append((mark, subset))
    return states

def apply_named(q, beta, a, b, mass):
    out = defaultdict(int)
    for (mark, subset),weight in mass.items():
        for i in subset:
            child = (mark, tuple(j for j in subset if j != i))
            out[child] += weight*beta[i]
        if mark:
            out[(0,subset)] += weight*b
        elif len(subset) < q:
            out[(1,subset)] += weight*a
    return {s:v for s,v in out.items() if v}

def named_hist(mass,q):
    out = [0]*(q+1)
    for (mark,subset),v in mass.items():
        out[len(subset)+mark] += v
    return tuple(out)

def choose_recurrence(history,q,lam):
    for t in range(len(history)-2*q-1):
        expected = tuple(sum((-1)**(q-j)*comb(q,j)*lam**(q-j)*history[t+2*j+1][h]
                  for j in range(q+1)) for h in range(q+1))
        assert all(x == 0 for x in expected), ('recurrence',q,t,expected)

def interpolate(history,q,lam):
    for r in (1,2):
        deltas = []
        for j in range(q):
            deltas.append(tuple(sum((-1)**(j-k)*comb(j,k)*lam**(j-k)*history[r+2*k][h]
                     for k in range(j+1)) for h in range(q+1)))
        for n in range((len(history)-1-r)//2+1):
            obs = tuple(sum(comb(n,j)*lam**(n-j)*deltas[j][h]
                      for j in range(min(q,n+1))) for h in range(q+1))
            assert obs == history[r+2*n], ('interpolation',q,r,n,obs,history[r+2*n])

def main():
    summary = {
       'schema':'PREFIX826_EXACT_INTEGER_EVIDENCE_V1',
       'scope':'positive a,b; unnormalized Q=R+A; cardinality histograms; finite named subsets',
       'moment_configurations':0,'moment_basis_annihilator_checks':0,
       'moment_visible_jordan_witnesses':0,'moment_visible_zero_witnesses':0,
       'named_parameter_sets':0,'named_initial_states':0,
       'named_histogram_recurrences':0,'named_histogram_interpolations':0,
       'max_named_capacity':6,'max_moment_capacity':12,
       'status':'ALL_EXACT_ASSERTIONS_PASSED'
    }
    for q in range(1,13):
        for a,b in ((1,1),(2,3),(3,2)):
            names,L,C = moment_operator(q,a,b)
            n = len(names)
            assert n==(q+1)**2
            summary['moment_configurations']+=1
            for i in range(n):
                e = [int(j==i) for j in range(n)]
                assert not any(eval_polynomial(L,e,q,a*b,True))
                summary['moment_basis_annihilator_checks']+=1
            e = [int(s==('U',q-1,q-1)) for s in names]
            z = cv(C,eval_polynomial(L,e,q-1,a*b,True))
            expected = 2**(q-1)*factorial(q-1)
            expected *= (a*b)**(q//2) if q%2==0 else a*(a*b)**((q-1)//2)
            assert z[q%2] == expected and sum(abs(x) for x in z)==expected
            summary['moment_visible_jordan_witnesses']+=1
            e = [int(s==('U',q,0)) for s in names]
            z = cv(C,eval_polynomial(L,e,q,a*b,False))
            assert z[q]==(-a*b)**q and sum(abs(x) for x in z)==(a*b)**q
            summary['moment_visible_zero_witnesses']+=1
    for q in range(1,7):
        m=q+1
        for betas in (list(range(1,m+1)),[2*i+1 for i in range(m)]):
            states=named_states(q,m)
            for a,b in ((1,1),(2,3)):
                summary['named_parameter_sets']+=1
                for initial in states:
                    hist=[];mass={initial:1}
                    for _ in range(4*q+8):
                        hist.append(named_hist(mass,q))
                        mass=apply_named(q,betas,a,b,mass)
                    choose_recurrence(hist,q,a*b)
                    interpolate(hist,q,a*b)
                    summary['named_initial_states']+=1
                    summary['named_histogram_recurrences']+=(len(hist)-2*q-1)*(q+1)
                    summary['named_histogram_interpolations']+=(len(hist)-1)*(q+1)
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    from pathlib import Path
    Path(__file__).with_name('PREFIX826_R6_Q_ONLY_RECURRENCE_RESULTS.json').write_text(
        json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
