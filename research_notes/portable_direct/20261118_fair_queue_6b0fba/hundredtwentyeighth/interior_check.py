"""Canonical Q repair states. Python 3 and Regina 7.4.1, no fixture downloads."""
from collections import Counter, deque
from fractions import Fraction
from importlib.metadata import version
from itertools import permutations, product
from math import gcd, prod
import json

import regina as R

def entries(A):
    return [[A.entry(i,j).pythonValue() for j in range(A.columns())] for i in range(A.rows())]

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def smith(B):
    A=R.MatrixInt(B)
    V,Vi,U,Ui=(R.MatrixInt(1) for _ in range(4))
    R.smithNormalForm(A,V,Vi,U,Ui)
    diag=[A.entry(i,i).pythonValue() for i in range(min(A.rows(),A.columns()))]
    return diag, entries(V)

def spherical(t):
    return t.isConnected() and t.isValid() and t.isClosed() and all(
        v.linkType()==R.Vertex3.Link.Sphere for v in t.vertices())

def census_one():
    perms=list(permutations(range(4)))
    seen=Counter()
    for mate in (1,2,3):
        c,d=sorted({1,2,3}-{mate})
        for f,g in product([p for p in perms if p[0]==mate], [p for p in perms if p[c]==d]):
            t=R.Triangulation3(); s=t.newTetrahedron()
            s.join(0,s,R.Perm4(*f)); s.join(c,s,R.Perm4(*g))
            seen[t.isoSig() if spherical(t) else 'excluded']+=1
    assert sum(seen.values())==108 and set(seen)-{'excluded'}=={'bkaagb','bkaagj','bkaajj','bkaajn'}
    return dict(sorted(seen.items()))

def setup(t):
    assert spherical(t)
    n=t.size()
    A=entries(R.makeMatchingEquations(t,R.NS_STANDARD))
    B=entries(R.makeMatchingEquations(t,R.NS_QUAD))
    tri=[7*i+h for i in range(n) for h in range(4)]
    qu=[7*i+4+h for i in range(n) for h in range(3)]
    groups=[[] for v in t.vertices()]
    for i in range(n):
        for v in range(4): groups[t.tetrahedron(i).vertex(v).index()].append(4*i+v)
    e=[1]*(7*n)
    for f in t.triangles():
        u=f.front(); i=u.simplex().index(); opp=u.face()
        for h in range(7): e[7*i+h]-=(h!=opp)
    for edge in t.edges():
        u=edge.front(); i=u.simplex().index(); v,w=u.vertices()[0],u.vertices()[1]
        for s in (v,w): e[7*i+s]+=1
        for h in range(3): e[7*i+4+h]+=(v in (0,h+1))!=(w in (0,h+1))
    for c in groups: assert sum(e[tri[h]] for h in c)==2
    # Independent disk checks on the native standard matrix.
    for i in range(n):
        z=[0]*(7*n); z[7*i:7*i+7]=[-1]*4+[1]*3
        assert all(dot(row,z)==0 for row in A) and dot(e,z)==-1
    for edge in t.edges():
        z=[0]*(7*n)
        for emb in edge.embeddings():
            i=emb.simplex().index(); v,w=emb.vertices()[0],emb.vertices()[1]
            z[7*i+v]-=1; z[7*i+w]-=1
            h=next(h for h in range(3) if (v in (0,h+1))==(w in (0,h+1)))
            z[7*i+4+h]+=1
        assert all(dot(row,z)==0 for row in A) and dot(e,z)==-2
    adj=[[] for j in tri]; L=[None]*len(tri)
    for row in A:
        pos=[i for i,j in enumerate(tri) if row[j]==1]; neg=[i for i,j in enumerate(tri) if row[j]==-1]
        assert len(pos)==len(neg)<=1
        if pos:
            a,b=pos[0],neg[0]; w=[row[j] for j in qu]
            adj[a].append((b,w)); adj[b].append((a,[-v for v in w]))
    for c in groups:
        L[c[0]]=[0]*len(qu); queue=deque([c[0]])
        while queue:
            a=queue.popleft()
            for b,w in adj[a]:
                if L[b] is None:
                    L[b]=[x+y for x,y in zip(L[a],w)];queue.append(b)
        assert all(L[h] is not None for h in c)
    def substitute(row):
        return [row[j]+sum(row[h]*w[a] for h,w in zip(tri,L)) for a,j in enumerate(qu)]
    closed=[substitute(row) for row in A]
    assert R.MatrixInt(B).rank()==R.MatrixInt(closed+B).rank()==R.MatrixInt(closed).rank()
    base=substitute(e)
    return groups, B, [(tau,[b-2*sum(L[i][a] for i in tau) for a,b in enumerate(base)])
                       for tau in product(*groups)], A, e, L

def polynomial(groups,U):
    # Coefficients of only the relevant box; larger exponents cannot contribute.
    counts={(0,)*len(U):1}
    for group in groups:
        next_counts=Counter(); allowed=Counter(h//4 for h in group)
        outside=len(group)-sum(allowed[s] for s in U)
        for vec,c in counts.items():
            if outside: next_counts[vec]+=outside*c
            for i,s in enumerate(U):
                if vec[i]<4 and allowed[s]:
                    key=vec[:i]+(vec[i]+1,)+vec[i+1:];next_counts[key]+=allowed[s]*c
        counts=next_counts
    return prod(map(len,groups))-sum(counts.get((k,)*len(U),0) for k in (2,3,4))

def run(t,branches):
    groups,B,states,A,e,L=setup(t); n=t.size()
    total=Counter(); sample={}; root=None
    for beta in branches:
        U=tuple(i for i,h in enumerate(beta) if h<0)
        assert U
        J=[3*i+k for i,h in enumerate(beta) for k in (range(3) if h<0 else [h])]
        sub=[[row[j] for j in J] for row in B]
        diag,V=smith(sub)
        rk=sum(bool(x) for x in diag)
        stats=Counter(); local_improvements=Counter()
        mod_dead=Counter()
        for tau,d in states:
            v=[sum(d[z]*V[i][j] for i,z in enumerate(J)) for j in range(len(J))]
            g=gcd(*v[rk:]); local=gcd(*(2*sum(x//4==s for x in tau)-1 for s in U))
            assert g>0 and local%g==0 and local in (1,3,5,7)
            if local==1: stats['witness_one']+=1
            elif g==1: local_improvements[local]+=1
            stats['g'+str(g)]+=1
            if g>1:
                if all(v[j]%g==0 for j in range(rk) if diag[j]%g==0): mod_dead[g]+=1
                if str(g) not in sample:
                    sample[str(g)]=dict(beta=beta,tau=tau,smith=diag,free_values=v[rk:])
        assert stats['witness_one']==polynomial(groups,U)
        if len(U)==n: root=dict(stats=stats,locally_inconclusive_but_survives=local_improvements)
        if n>=2:
            assert stats['witness_one']*16>=5*len(states)
            for s in U:
                assert all(any(h//4!=s for h in group) for group in groups)
        total.update(stats);total['nodes']+=1
        for p,c in mod_dead.items(): total['mod_dead_'+str(p)]+=c
    result=dict(signature=t.isoSig(),n=n,vertices=len(groups),state_count=len(states),
                vertex_degrees=[len(c) for c in groups],totals=dict(total),root=root,examples=sample)
    if t.isoSig()=='bkaagb':
        assert B==[[0,1,-1],[0,-2,2],[0,1,-1]]
        all_tau=[]
        expected=[[0,0,0,0,1,0,0],[0,0,0,0,0,1,1]]
        for tau,d in states:
            # Include two independent marking equations; rank and a unit minor
            # of the proposed null basis then certify saturation.
            rows=A+[[int(j==i) for j in range(7)] for i in tau]
            ds,_=smith(rows)
            assert sum(x!=0 for x in ds)==5 and all(dot(row,z)==0 for row in rows for z in expected)
            assert [[z[i] for i in (4,5)] for z in expected]==[[1,0],[0,1]]
            assert [dot(e,z) for z in expected]==[0,3]
            assert all(d[i]%3==0 for i in [0]) and (d[1]+d[2])%3==0
            all_tau.append(dict(tau=tau,standard_smith=ds,quad_euler=d,
                                mod3_row_multiplier_for_first_B_row=d[1]%3))
        result['exception']=dict(quad_B=B,saturated_standard_basis=expected,euler_on_basis=[0,3],
                                 all_states=all_tau,regina_is_sphere=t.isSphere(),standard_vertex_surfaces=[
                                     dict(chi=w.eulerChar().longValue(),vertex_link=w.isVertexLinking(),
                                          vector=[w.vector()[i].longValue() for i in range(7)])
                                     for w in R.NormalSurfaces(t,R.NS_STANDARD)])
    return result

def all_partial(n):
    return [b for b in product((-1,0,1,2),repeat=n) if -1 in b]

def main():
    out={'regina':version('regina'),'one_tetra_face_pairings':census_one(),'cases':{}}
    for sig in ('bkaagb','bkaagj','bkaajj','bkaajn','cPcbbbaaa','cMcabbgdv'):
        t=R.Triangulation3.fromIsoSig(sig);out['cases'][sig]=run(t,all_partial(t.size()))
    for sig in ('bkaagb','bkaagj'):
        t=R.Triangulation3.fromIsoSig(sig);assert t.pachner(t.tetrahedron(0))
        out['cases'][sig+'_1to4']=run(t,all_partial(t.size()))
    t=R.Example3.simplicialSphere()
    branches=[(-1,)*5]+[tuple(-1 if i==s else k for i in range(5)) for s in range(5) for k in (0,1,2)]
    out['cases']['boundary_4_simplex']=run(t,branches)
    # Recanonicalise once, so the listed branch and marked local corners are stable.
    t=R.Triangulation3.fromIsoSig('fvPQccdedeegovcfb')
    assert t.pachner(t.triangle(0)) and t.isoSig()=='gLLAQcedefffaavaaav'
    t=R.Triangulation3.fromIsoSig(t.isoSig())
    out['cases']['sphere_2to3']=run(t,[(-1,)*6,(-1,0,0,0,1,1)])
    row=out['cases']['sphere_2to3']['examples']['7']
    assert row['tau']==(0,1,2,3,16) and row['free_values']==[-7,7]
    probabilities={}
    for shape in ((4,), (3,1), (2,2), (2,1,1), (1,1,1,1)):
        probs=[Fraction(i,2*((i+2)//2)) for i in shape]
        p=sum(prod(q if b else 1-q for q,b in zip(probs,bits))
              for bits in product((0,1),repeat=len(shape)) if sum(bits)<=1)
        probabilities[str(shape)]=str(p)
    assert min(map(Fraction,probabilities.values()))==Fraction(5,16)
    out['single_tetra_witness_lower_bound_by_corner_partition']=probabilities
    double=out['cases']['cPcbbbaaa']['root']
    assert double['stats']['g1']==16 and double['stats']['witness_one']==10
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
