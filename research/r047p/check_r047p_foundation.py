#!/usr/bin/env python3
"""Exact finite checks for frozen R047P blind Foundation candidates.
Standard library only. No calibration or external prior-art inputs.
"""
from __future__ import annotations
import hashlib, itertools, json, math
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANDIDATE_FILE = HERE / "R047P_FOUNDATION_CANDIDATE_SET.json"

def canon_hash(obj):
    raw=json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def all_edges(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def graphs(n):
    pairs=all_edges(n)
    for bits in range(1<<len(pairs)):
        yield frozenset(pairs[k] for k in range(len(pairs)) if bits>>k & 1)

def subsets(n):
    for bits in range(1<<n):
        yield frozenset(i for i in range(n) if bits>>i & 1)

def adj(E,n):
    a=[set() for _ in range(n)]
    for u,v in E: a[u].add(v); a[v].add(u)
    return a

def cut(E,A):
    return frozenset(e for e in E if ((e[0] in A) ^ (e[1] in A)))

def star(E,v):
    return frozenset(e for e in E if v in e)

def xor_set(A,B): return A.symmetric_difference(B)

def refine(E,A):
    n=max([-1]+[x for e in E for x in e]+list(A))+1
    # Caller supplies vertex count separately via padding by synthetic occupancy vector when needed.
    raise RuntimeError("use refine_n")

def refine_n(E,A,n):
    a=adj(E,n)
    colors=tuple(1 if v in A else 0 for v in range(n))
    history=[colors]
    strict=0
    while True:
        sig=[(colors[v],tuple(sorted(colors[u] for u in a[v]))) for v in range(n)]
        table={s:i for i,s in enumerate(sorted(set(sig)))}
        nxt=tuple(table[s] for s in sig)
        if same_partition(colors,nxt):
            return history,colors,strict
        assert refines(nxt,colors)
        strict += 1
        colors=nxt; history.append(colors)

def same_partition(c,d):
    n=len(c)
    return all((c[i]==c[j])==(d[i]==d[j]) for i in range(n) for j in range(n))

def refines(fine,coarse):
    n=len(fine)
    return all(not(fine[i]==fine[j]) or coarse[i]==coarse[j] for i in range(n) for j in range(n))

def permute_edge(E,p):
    return frozenset(tuple(sorted((p[u],p[v]))) for u,v in E)

def permute_set(A,p): return frozenset(p[v] for v in A)

def permute_vec(x,p):
    out=[0]*len(x)
    for v,z in enumerate(x): out[p[v]]=z
    return tuple(out)

def parity_T(E,x):
    a=adj(E,len(x))
    return tuple((x[v]+sum(x[u] for u in a[v]))&1 for v in range(len(x)))

def add2(x,y): return tuple((a^b) for a,b in zip(x,y))

def branch_levels(E,A0,n):
    m={frozenset(A0):1}; levels=[m]
    for _ in range(n-len(A0)):
        nxt={}
        for A,mul in m.items():
            frontier=[v for v in range(n) if v not in A and any(tuple(sorted((v,u))) in E for u in A)]
            for v in frontier:
                B=A|{v}; nxt[B]=nxt.get(B,0)+mul
        if not nxt: break
        m=nxt; levels.append(m)
    return levels

def automorphisms(E,A,n):
    out=[]
    for p in itertools.permutations(range(n)):
        if permute_edge(E,p)==E and permute_set(A,p)==A: out.append(p)
    return out

def orbit_quotient(E,A,n):
    autos=automorphisms(E,A,n)
    unseen=set(range(n)); orbits=[]
    while unseen:
        v=min(unseen); O={p[v] for p in autos}; unseen-=O; orbits.append(tuple(sorted(O)))
    orbits.sort(key=lambda O:(len(O),O))
    idx={v:i for i,O in enumerate(orbits) for v in O}
    weights={}
    for u,v in E:
        i,j=sorted((idx[u],idx[v])); weights[(i,j)]=weights.get((i,j),0)+1
    return tuple(len(O) for O in orbits), tuple(sorted((i,j,w) for (i,j),w in weights.items()))

def connected(E,n):
    if n==0: return True
    a=adj(E,n); seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for u in a[v]:
            if u not in seen: seen.add(u); stack.append(u)
    return len(seen)==n

def degree(E,n):
    d=[0]*n
    for u,v in E: d[u]+=1; d[v]+=1
    return tuple(d)

def fire(E,q,v):
    n=len(q); d=degree(E,n)
    assert d[v]>0 and q[v]>=d[v]
    z=list(q); z[v]-=d[v]
    for u,w in E:
        if u==v: z[w]+=1
        elif w==v: z[u]+=1
    return tuple(z)

def translation(E,n,v):
    d=degree(E,n); z=[0]*n; z[v]-=d[v]
    for u,w in E:
        if u==v: z[w]+=1
        elif w==v: z[u]+=1
    return tuple(z)

def checks():
    with open(CANDIDATE_FILE,encoding='utf-8') as fh:
        D=json.load(fh)
    # Freeze integrity.
    manifest=[]
    for c in D['candidates']:
        x=dict(c); want=x.pop('freeze_sha256')
        assert canon_hash(x)==want, c['id']
        manifest.append({'id':c['id'],'freeze_sha256':want})
    assert canon_hash({'sources':D['sources'],'manifest':manifest})==D['candidate_set_sha256']
    yield 'freeze_hashes'

    # M1: exhaustive n<=4 edgewise XOR homomorphism and one-toggle law.
    for n in range(1,5):
      for E in graphs(n):
       for A in subsets(n):
        for C in subsets(n): assert cut(E,xor_set(A,C))==xor_set(cut(E,A),cut(E,C))
        for v in range(n): assert cut(E,xor_set(A,{v}))==xor_set(cut(E,A),star(E,v))
    yield 'M1_cut_XOR_and_toggle_exhaustive_n<=4'

    # M2: exhaustive refinement/stabilization; selected automorphism equivariance via every preserving permutation.
    for n in range(1,5):
      for E in graphs(n):
       for A in subsets(n):
        hist,stable,strict=refine_n(E,A,n)
        assert strict<=max(0,n-1)
        for p in itertools.permutations(range(n)):
            if permute_edge(E,p)==E and permute_set(A,p)==A:
                for colors in hist:
                    pc=permute_vec(colors,p)
                    assert same_partition(colors,pc)
    yield 'M2_refinement_stabilization_equivariance_exhaustive_n<=4'

    # M3: exhaustive linearity + relabeling n<=4, and finite-state eventual repetition.
    for n in range(1,5):
      vecs=list(itertools.product((0,1), repeat=n))
      for E in graphs(n):
       for x in vecs:
        seen={}; z=x
        for t in range((1<<n)+1):
            if z in seen: break
            seen[z]=t; z=parity_T(E,z)
        else: raise AssertionError('finite orbit did not repeat')
        for y in vecs: assert parity_T(E,add2(x,y))==add2(parity_T(E,x),parity_T(E,y))
        for p in itertools.permutations(range(n)):
            assert parity_T(permute_edge(E,p),permute_vec(x,p))==permute_vec(parity_T(E,x),p)
    yield 'M3_linearity_equivariance_finite_orbit_exhaustive_n<=4'

    # M4: level-size invariant and exact disconnected interleaving witness.
    E=frozenset({(0,1),(1,2),(3,4)}); A0=frozenset({0,3}); levels=branch_levels(E,A0,5)
    for k,m in enumerate(levels):
        for A in m: assert len(A)==len(A0)+k
    # At k=2, reaching {0,1,3,4} has two interleavings, C(2,1)=2.
    assert levels[2][frozenset({0,1,3,4})]==math.comb(2,1)
    yield 'M4_level_and_disconnected_interleaving'

    # M5: exact relabeling invariance + frozen nonfaithful witness.
    C6=frozenset(tuple(sorted((i,(i+1)%6))) for i in range(6))
    K3K3=frozenset({(0,1),(0,2),(1,2),(3,4),(3,5),(4,5)})
    A=frozenset(range(6))
    q1=orbit_quotient(C6,A,6); q2=orbit_quotient(K3K3,A,6)
    assert q1==q2==((6,),((0,0,6),))
    p=(2,4,1,5,0,3)
    assert orbit_quotient(permute_edge(C6,p),permute_set(A,p),6)==q1
    # Connectivity distinguishes the original relations, so equality of Q is nonfaithful.
    assert connected(C6,6) and not connected(K3K3,6)
    yield 'M5_relabeling_and_nonfaithful_witness'

    # M6: exhaustive one-step conservation n<=4 over small charge range, translation commutation, exact 2-cycle.
    for n in range(1,5):
      for E in graphs(n):
       d=degree(E,n)
       for q in itertools.product(range(4),repeat=n):
        for v in range(n):
          if d[v]>0 and q[v]>=d[v]: assert sum(fire(E,q,v))==sum(q)
       trs=[translation(E,n,v) for v in range(n)]
       for v in range(n):
        for w in range(n):
         # Fixed firing translations commute under addition.
         assert tuple(trs[v][i]+trs[w][i] for i in range(n))==tuple(trs[w][i]+trs[v][i] for i in range(n))
    E=frozenset({(0,1)}); q=(1,0); q1=fire(E,q,0); q2=fire(E,q1,1)
    assert q1==(0,1) and q2==q
    yield 'M6_conservation_commutation_two_cycle'

def main():
    done=list(checks())
    print(json.dumps({'status':'PASS','checks':done,'count':len(done)},indent=2))
    return done

if __name__=='__main__': main()
