"""Canonical-Q observer on public Regina controls. Requires the PyPI package regina==7.4.1."""
import argparse
from collections import Counter, deque
from functools import reduce
import json
from pathlib import Path
from math import gcd
from time import perf_counter
import regina as R

PRIMES = (3,5,7)
CASES = {
    "S3":("threeSphere",()), "Bing-S3":("bingsHouse",()),
    "L(3,1)":("lens",(3,1)), "L(5,2)":("lens",(5,2)),
    "L(8,3)":("lens",(8,3)), "S2xS1":("s2xs1",()),
    "Poincare":("poincare",()), "Weeks-A":("weeks",()),
    "Weeks-B":("smallClosedOrblHyperbolic",()),
    "Figure8(5,1)":("fromIsoSig",("jLLvQPQcdfhghigiihshhgfifme",)),
}


def entries(m):
    return [[m.entry(i,j).pythonValue() for j in range(m.columns())] for i in range(m.rows())]


def add(u,v,k=1):
    return [x+k*y for x,y in zip(u,v)]


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def build(t):
    n=t.size()
    assert t.isClosed() and t.isOrientable() and t.countVertices()==1 and t.isValid()
    a=entries(R.makeMatchingEquations(t,R.NS_STANDARD))
    b=entries(R.makeMatchingEquations(t,R.NS_QUAD))
    tr=[7*i+j for i in range(n) for j in range(4)]
    qu=[7*i+j for i in range(n) for j in range(4,7)]
    # Each local Euler coefficient counts disk faces, arcs in a chosen global face
    # occurrence, and intersections in a chosen global edge occurrence.
    e=[1]*(7*n)
    for face in t.triangles():
        emb=face.front(); i=emb.simplex().index(); opp=emb.face()
        for j in range(7):
            if j!=opp: e[7*i+j]-=1
    for edge in t.edges():
        emb=edge.front(); i=emb.simplex().index()
        v,w=emb.vertices()[0],emb.vertices()[1]
        e[7*i+v]+=1; e[7*i+w]+=1
        for j in range(3):
            if (v in (0,j+1)) != (w in (0,j+1)): e[7*i+4+j]+=1
    assert sum(e[k] for k in tr)==2
    adj=[[] for _ in tr]
    for row in a:
        plus=[i for i,j in enumerate(tr) if row[j]==1]
        minus=[i for i,j in enumerate(tr) if row[j]==-1]
        assert len(plus)==len(minus)<=1 and all(abs(row[j])<=1 for j in tr)
        if plus:
            u,v=plus[0],minus[0]
            dq=[row[k] for k in qu] # t_v = t_u + Q_r q
            adj[u].append((v,dq)); adj[v].append((u,[-x for x in dq]))
    p=[None]*len(tr); p[0]=[0]*len(qu); queue=deque([0])
    while queue:
        u=queue.popleft()
        for v,row in adj[u]:
            if p[v] is None:
                p[v]=add(p[u],row);queue.append(v)
    assert all(z is not None for z in p)
    base=[e[k] for k in qu]
    for j,h in zip(tr,p): base=add(base,h,e[j])
    d=[add(base,h,-2) for h in p]
    # Check integral cycle consistency on the Q-space, not just at test vectors.
    checks=[]
    for row in a:
        relation=[row[j] for j in qu]
        for j,h in zip(tr,p):
            if row[j]: relation=add(relation,h,row[j])
        checks.append(relation)
    assert R.MatrixInt(b+checks).rank()==R.MatrixInt(b).rank()
    assert R.MatrixInt(checks+b).rank()==R.MatrixInt(checks).rank()
    # Signed tetrahedral matching solutions give Euler -1 (or +1 after gauge repair).
    for i in range(n):
        z=[0]*(7*n)
        for k in range(7): z[7*i+k]=-1 if k<4 else 1
        assert all(dot(row,z)==0 for row in a) and dot(e,z)==-1
        qz=[z[j] for j in qu]
        assert all(dot(row,qz)==0 for row in b)
        assert all(dot(row,qz)==(1 if tau//4==i else -1) for tau,row in enumerate(d))
    return b,d,e


def restrict(rows,jj):
    return [[row[j] for j in jj] for row in rows]


def row_coefficients(b,d,p):
    """Return explicit lambda with lambda B = d mod p, or None."""
    rows = len(b); cols=len(d)
    tab=[[b[i][j]%p for i in range(rows)]+[d[j]%p] for j in range(cols)]
    piv=[]; k=0
    for c in range(rows):
        s=next((u for u in range(k,cols) if tab[u][c]),None)
        if s is None: continue
        tab[k],tab[s]=tab[s],tab[k]; inv=pow(tab[k][c],-1,p)
        tab[k]=[x*inv%p for x in tab[k]]
        for u in range(cols):
            if u!=k and tab[u][c]:
                z=tab[u][c];tab[u]=[(x-z*y)%p for x,y in zip(tab[u],tab[k])]
        piv.append(c);k+=1
    if any(row[-1] for row in tab[k:]): return None
    coeff=[0]*rows
    for i,c in enumerate(piv): coeff[c]=tab[i][-1]
    assert all(sum(coeff[i]*b[i][j] for i in range(rows))%p==d[j]%p for j in range(cols))
    return coeff


def census(t):
    start=perf_counter()
    b,d,e=build(t); n=t.size(); size=4*n
    native_start=perf_counter(); sphere=t.nonTrivialSphereOrDisc()
    native_elapsed=perf_counter()-native_start
    # All standard vertex surfaces: the type constraints and t_tau=0 cut coordinate faces.
    rays=R.NormalSurfaces(t,R.NS_STANDARD); positive=[]
    for s in rays:
        v=[s.vector()[j].pythonValue() for j in range(7*n)]
        assert dot(e,v)==s.eulerChar().pythonValue()
        if s.eulerChar()>0 and not s.isVertexLinking():
            assert s.eulerChar().pythonValue() in (1,2)
            types=tuple(next((k for k in range(3) if v[7*i+4+k]),-1) for i in range(n))
            zeros=tuple(j for j in range(size) if v[7*(j//4)+j%4]==0)
            assert zeros and any(k!=-1 for k in types)
            positive.append((types,zeros))
    assert bool(positive)==bool(sphere)
    setup=perf_counter()-start
    stages=("mod","exact")
    stats={name:{'visited':0,'first':Counter(),'survivors':Counter(),'mass':0,'pass':0} for name in stages}
    examples={}; expected_positive=0; extra_leaves=[]; leaf_ranks=Counter(); full_mod=0; begin=perf_counter(); nodes_snf=0

    def visit(prefix,mod_states,int_states):
        nonlocal nodes_snf,expected_positive,full_mod
        h=len(prefix)
        jj=[3*i+k for i in range(n) for k in ([prefix[i]] if i<h else range(3))]
        bb=restrict(b,jj); dd=restrict(d,jj)
        smith=R.MatrixInt(bb); v=R.MatrixInt(1); vi=R.MatrixInt(1); u=R.MatrixInt(1); ui=R.MatrixInt(1)
        R.smithNormalForm(smith,v,vi,u,ui); nodes_snf+=1
        diag=[smith.entry(i,i).pythonValue() for i in range(min(len(bb),len(jj)))]
        rank=sum(bool(x) for x in diag)
        if h==n:
            leaf_ranks[rank]+=1
            if rank==n and any(diag[-1]%p for p in PRIMES):
                full_mod+=1
        # Unimodular SNF gives integral kernel, plus extra columns for p|invariant.
        extra={p:[i for i in range(rank) if diag[i]%p==0] for p in PRIMES}
        vals=R.MatrixInt(dd)*v
        keep=[]; ints=[]; exact_alive=set(int_states) if int_states is not None else set()
        for tau in mod_states:
            free=[vals.entry(tau,j).pythonValue() for j in range(rank,len(jj))]
            g=reduce(gcd,free,0)
            killed=None
            for prime in PRIMES:
                if g%prime==0 and all(vals.entry(tau,i).pythonValue()%prime==0 for i in extra[prime]):
                    killed=prime;break
            if killed is None: keep.append(tau)
            if tau in exact_alive and g in (1,2): ints.append(tau); assert killed is None
            if killed is not None and 'row' not in examples:
                lam=row_coefficients(bb,dd[tau],killed); assert lam is not None
                examples['row']={'prefix':prefix,'tau':tau,'p':killed,'lambda':lam,'d':dd[tau]}
            if g>2 and ('gcd' not in examples or (g==4 and examples['gcd']['g']!=4)):
                examples['gcd']={'prefix':prefix,'tau':tau,'g':g,'d':dd[tau],
                                 'free_values':free,'kernel':[[v.entry(i,j).pythonValue() for i in range(len(jj))]
                                                               for j in range(rank,len(jj))]}
        if h<n:
            assert len(keep)==len(ints)==size
        if h==n and keep and not ints:
            extra_leaves.append(dict(branch=prefix,mod_survivors=keep,
                                      primitive_kernel=[[v.entry(i,j).pythonValue() for i in range(len(jj))]
                                                        for j in range(rank,len(jj))],
                                      exact_images=[reduce(gcd,(vals.entry(i,j).pythonValue()
                                                 for j in range(rank,len(jj))),0) for i in range(size)]))
        for stage,orig,surviv in [('mod',mod_states,keep),('exact',int_states,ints)]:
            if orig is None: continue
            s=stats[stage];s['visited']+=1;s['survivors'][len(surviv)]+=1
            if not surviv:
                s['first'][h]+=1;s['mass']+=3**(n-h)
            elif h==n: s['pass']+=1
        # Any compatible positive vertex-ray certificate must survive in its zero-triangle states.
        for types,zeros in positive:
            if all(types[i] in (-1,k) for i,k in enumerate(prefix)):
                assert set(zeros)<=set(keep)
                if int_states is not None: assert set(zeros)<=set(ints)
                if h==n: expected_positive+=1
        if h<n and keep:
            for choice in range(3): visit(prefix+(choice,),keep,ints if ints else None)
    visit((),list(range(size)),list(range(size)))
    elapsed=perf_counter()-begin
    for s in stats.values(): assert s['mass']+s['pass']==3**n
    # Baseline runs the same ordered tree, consulting the precomputed exact geometric certificates.
    count=0; off_positive=0
    def off(prefix):
        nonlocal count,off_positive
        count+=1
        if len(prefix)==n:
            off_positive+=sum(all(k in (-1,j) for k,j in zip(types,prefix)) for types,zeros in positive)
        else:
            for j in range(3): off(prefix+(j,))
    tick=perf_counter();off(());off_elapsed=perf_counter()-tick
    assert count==(3**(n+1)-1)//2 and expected_positive==off_positive
    return dict(n=n,vertices=1,tau=size,sig=t.isoSig(),finite_primes=PRIMES,stats=stats,baseline_nodes=count,
                positive_rays=len(positive),positive_ray_leaf_pairs=off_positive,native_positive=bool(sphere),
                standard_rays=rays.size(),examples=examples,extra_leaves=extra_leaves,leaf_ranks=leaf_ranks,full_rank_mod_any=full_mod,seconds=dict(setup=setup,observer=elapsed,
                    baseline=off_elapsed,regina_native=native_elapsed),smith_calls=nodes_snf)


def main():
    cli=argparse.ArgumentParser();cli.add_argument('names',nargs='*');cli.add_argument('--out');cli.add_argument('--verify',action='store_true')
    args=cli.parse_args();out={}
    for tag in args.names or CASES:
        name,par=CASES[tag]
        t=R.Triangulation3.fromIsoSig(*par) if name=="fromIsoSig" else getattr(R.Example3,name)(*par)
        out[tag]=census(t)
        z=out[tag];print(tag,z['n'],z['baseline_nodes'],[(k,s['visited'],s['mass'],s['first']) for k,s in z['stats'].items()],z['seconds'],flush=True)
        if args.verify:
            expected=json.loads(Path(__file__).with_name("normal_census.json").read_text())[tag]
            observed=json.loads(json.dumps({k:v for k,v in z.items() if k!='seconds'}))
            assert observed=={k:v for k,v in expected.items() if k!='seconds'}
        if args.out:
            with open(args.out,'w') as fp:json.dump(out,fp,indent=2);fp.write('\n')


if __name__=='__main__': main()
