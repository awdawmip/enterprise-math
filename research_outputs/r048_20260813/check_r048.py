#!/usr/bin/env python3
import argparse
import hashlib
import itertools
import json
import math
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def canonical_hash(obj, excluded_field):
    x = dict(obj)
    x.pop(excluded_field, None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

def compositions(total, n):
    if n == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for rest in compositions(total-a, n-1):
            yield (a,) + rest

def path_edges(n):
    return [(i, i+1) for i in range(n-1)]

# G2-M1
def m1_moves(x, edges):
    x = tuple(x)
    out = []
    for u,v in edges:
        d = x[u]-x[v]
        if d >= 2:
            y=list(x); y[u]-=1; y[v]+=1; out.append(tuple(y))
        elif d <= -2:
            y=list(x); y[v]-=1; y[u]+=1; out.append(tuple(y))
    return out

def m1_P(x):
    return sum(a*a for a in x)

def test_m1():
    checks=0
    for n in range(2,5):
        edges=path_edges(n)
        for M in range(0,7):
            for x in compositions(M,n):
                for y in m1_moves(x,edges):
                    assert sum(y)==sum(x)
                    assert m1_P(y) <= m1_P(x)-2
                    checks += 1
    return checks

# G2-M2
def m2_moves(state):
    p,n=state
    out=[]
    for i,(a,b) in enumerate(zip(p,n)):
        if a>0 and b>0:
            pp=list(p); nn=list(n)
            pp[i]-=1; nn[i]-=1
            out.append((tuple(pp),tuple(nn)))
    return out

def m2_q(state):
    p,n=state
    return tuple(a-b for a,b in zip(p,n))

def m2_nf_from_q(q):
    return (tuple(max(v,0) for v in q), tuple(max(-v,0) for v in q))

def m2_terminals(state):
    seen=set()
    terms=set()
    stack=[state]
    while stack:
        s=stack.pop()
        if s in seen: continue
        seen.add(s)
        nxt=m2_moves(s)
        if not nxt:
            terms.add(s)
        else:
            stack.extend(nxt)
    return terms

def test_m2():
    checks=0
    vals=range(0,4)
    for p in itertools.product(vals, repeat=2):
        for n in itertools.product(vals, repeat=2):
            s=(p,n)
            q=m2_q(s)
            terms=m2_terminals(s)
            assert terms == {m2_nf_from_q(q)}
            for t in m2_moves(s):
                assert m2_q(t)==q
                assert sum(t[0])+sum(t[1]) == sum(p)+sum(n)-2
                checks += 1
    # raw normal-form non-monoidality counterexample
    plus=((1,),(0,))
    minus=((0,),(1,))
    lhs=(tuple(plus[0][i]+minus[0][i] for i in range(1)),
         tuple(plus[1][i]+minus[1][i] for i in range(1)))
    assert m2_nf_from_q(m2_q(lhs)) == ((0,),(0,))
    assert (plus[0][0]+minus[0][0], plus[1][0]+minus[1][0]) == (1,1)
    return checks

# G2-M3
def m3_step(bits):
    b=list(bits)
    for i in range(len(b)):
        if b[i]==0:
            b[i]=1
            for j in range(i):
                b[j]=0
            return tuple(b)
    return tuple(0 for _ in b)

def test_m3():
    checks=0
    for L in range(1,9):
        z=tuple(0 for _ in range(L))
        cur=z
        seen=[]
        carry_counts=[0]*L
        for step in range(2**L):
            assert cur not in seen
            seen.append(cur)
            for k in range(1,L):
                if all(cur[j]==1 for j in range(k)):
                    carry_counts[k]+=1
            cur=m3_step(cur)
            checks+=1
        assert cur==z
        assert len(seen)==2**L
        for k in range(1,L):
            assert carry_counts[k]==2**(L-k)
        for k in range(1,L+1):
            cur=z
            pref=cur[:k]
            period=None
            for t in range(1,2**k+1):
                cur=m3_step(cur)
                if cur[:k]==pref:
                    period=t
                    break
            assert period==2**k
    return checks

# G2-M4
def m4_union(state):
    u=0
    for s in state: u |= s
    return u

def popcount(x):
    return x.bit_count()

def m4_P(state):
    U=m4_union(state)
    return sum(popcount(U)-popcount(s) for s in state)

def m4_update(state,e):
    u,v=e
    st=list(state)
    z=st[u] | st[v]
    st[u]=z; st[v]=z
    return tuple(st)

def test_m4():
    checks=0
    for n in range(2,5):
        edges=path_edges(n)
        for A in range(1,4):
            allsets=range(2**A)
            for st in itertools.product(allsets, repeat=n):
                U=m4_union(st); P=m4_P(st)
                for e in edges:
                    y=m4_update(st,e)
                    assert m4_union(y)==U
                    if y!=st:
                        assert m4_P(y) < P
                    checks+=1
                terminal=all(m4_update(st,e)==st for e in edges)
                if terminal:
                    assert len(set(st))==1
    return checks

# G2-M5
def compose_maps(f,g):
    # f after g
    return tuple(f[g[i]] for i in range(len(f)))

def semigroup_closure(gens,n):
    ident=tuple(range(n))
    seen={ident}
    q=deque([ident])
    gens=list(gens)
    while q:
        a=q.popleft()
        for g in gens:
            for h in (compose_maps(g,a), compose_maps(a,g)):
                if h not in seen:
                    seen.add(h); q.append(h)
    return seen

def orbit(x, semigroup):
    return {m[x] for m in semigroup}

def reachable_graph(gens,n):
    return [[g[x] for g in gens] for x in range(n)]

def reach_sets(gens,n):
    adj=reachable_graph(gens,n)
    out=[]
    for x in range(n):
        seen={x}; q=[x]
        while q:
            a=q.pop()
            for b in adj[a]:
                if b not in seen:
                    seen.add(b); q.append(b)
        out.append(seen)
    return out

def test_m5():
    checks=0
    n=3
    funcs=list(itertools.product(range(n), repeat=n))
    for idx,f in enumerate(funcs):
        # all single-generator systems, and a bounded but deterministic set of pairs
        gen_sets=[(f,)]
        gen_sets.append((f, funcs[(idx*7+5)%len(funcs)]))
        for gens in gen_sets:
            sg=semigroup_closure(gens,n)
            rs=reach_sets(gens,n)
            for x in range(n):
                Ox=orbit(x,sg)
                assert Ox==rs[x]
                for g in gens:
                    y=g[x]
                    Oy=orbit(y,sg)
                    assert Oy <= Ox
                    checks+=1
            for x in range(n):
                for y in range(n):
                    if y in rs[x] and x in rs[y]:
                        assert rs[x]==rs[y]
    # exact product orbit-size law on two example actions
    gens1=[(1,0)] # swap on 2
    gens2=[(1,2,0)] # 3-cycle
    sg1=semigroup_closure(gens1,2)
    sg2=semigroup_closure(gens2,3)
    assert len(orbit(0,sg1))*len(orbit(0,sg2)) == 2*3
    return checks

# G2-M6
def swap_state(st,e):
    u,v=e
    s=list(st); s[u],s[v]=s[v],s[u]
    return tuple(s)

def bfs_swap_orbit(st,edges):
    seen={st}; q=[st]
    while q:
        s=q.pop()
        for e in edges:
            t=swap_state(s,e)
            if t not in seen:
                seen.add(t); q.append(t)
    return seen

def test_m6():
    checks=0
    for n in range(2,6):
        edges=path_edges(n)
        for st in itertools.product((0,1), repeat=n):
            orb=bfs_swap_orbit(st,edges)
            m=sum(st)
            expected=math.comb(n,m)
            assert len(orb)==expected
            for e in edges:
                t=swap_state(st,e)
                assert sorted(t)==sorted(st)
                assert swap_state(t,e)==st
                checks+=1
    return checks

def test_hashes():
    basis=load("R048_INDEPENDENT_DEBT_BASIS.json")
    fact=load("R048_DEBT_FACTORIZATION.json")
    cset=load("R048_G2_CANDIDATE_SET.json")
    led=load("R048_NATIVE_DERIVATION_LEDGER.json")
    mat=load("R048_INTERNAL_STRUCTURE_MATRIX.json")
    pf=load("R048_PRODUCTIVE_FAILURES.json")
    aud=load("R048_CONTAMINATION_AUDIT.json")
    res=load("R048_EXACT_CHECK_RESULTS.json")
    assert canonical_hash(basis,"stage_a_freeze_sha256")==basis["stage_a_freeze_sha256"]
    assert canonical_hash(fact,"stage_a_factorization_freeze_sha256")==fact["stage_a_factorization_freeze_sha256"]
    for c in cset["candidates"]:
        assert canonical_hash(c,"candidate_freeze_sha256")==c["candidate_freeze_sha256"]
    assert canonical_hash(cset,"candidate_set_freeze_sha256")==cset["candidate_set_freeze_sha256"]
    assert canonical_hash(led,"ledger_freeze_sha256")==led["ledger_freeze_sha256"]
    assert canonical_hash(mat,"matrix_freeze_sha256")==mat["matrix_freeze_sha256"]
    assert canonical_hash(pf,"productive_failures_freeze_sha256")==pf["productive_failures_freeze_sha256"]
    assert canonical_hash(aud,"audit_freeze_sha256")==aud["audit_freeze_sha256"]
    assert canonical_hash(res,"results_freeze_sha256")==res["results_freeze_sha256"]
    assert cset["stage_a_basis_sha256"]==basis["stage_a_freeze_sha256"]
    assert len(cset["candidates"])==6
    assert len({c["candidate_id"] for c in cset["candidates"]})==6
    assert aud["selection_signal_audit"]["winner_selected"] is False
    return 9+6

def main():
    tests=[
        ("hash/schema freeze", test_hashes),
        ("G2-M1 pairwise equalization", test_m1),
        ("G2-M2 signed cancellation", test_m2),
        ("G2-M3 binary carry", test_m3),
        ("G2-M4 finite union", test_m4),
        ("G2-M5 rewrite action quotient", test_m5),
        ("G2-M6 conservative swaps", test_m6),
    ]
    total=0
    for name,fn in tests:
        n=fn()
        total+=n
        print(f"PASS {name}: {n} checks")
    print(f"R048_EXACT_CHECKER_PASS total_checks={total}")
if __name__=="__main__":
    main()
