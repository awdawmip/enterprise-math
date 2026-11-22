#!/usr/bin/env python3
"""Exact p17 vertical-order-6 split (3,3) exact affine-kernel exclusion (author computation).

Frozen scientific carrier: T6 exponent-mass <=2331, reciprocal moments S1..S6,
p17 valuation one and 17-adic necessary congruences.  The 16x16 q0 lattice
basis below is copied byte-for-number from the pinned 2026-09-20 certificate
`research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json`
(Git blob SHA1 d9ac014355a6a1058cc8a0cf2141a01082628881).

Proof-side executable: every exact rational ball search is exhaustive because
Dmin > Rmax^2 for the order-six symmetric split (3,3). It is not a test of lower-prime
completion; a surviving 17-adic kernel would require further work.
Runtime: Python 3.12, sympy 1.14 (rational matrix inversion only).
"""
import hashlib
import json
import math
from fractions import Fraction
from itertools import combinations_with_replacement, product
from pathlib import Path
from sympy import Matrix

P = 17
BUDGET = 2331
W = [P*r-1 for r in range(1,P)]
U=[[47,44,-50,30,-3,1,2,18,-9,-5,0,10,-5,6,-4,-2],[76,87,-16,-2,-18,17,-13,13,-3,10,12,4,-11,-4,-3,-1],[-89,-26,23,10,-3,8,13,13,7,-8,-16,11,1,3,-13,-4],[-139,-1,31,52,7,17,0,-2,12,-21,-10,2,-1,0,-1,-1],[116,7,-33,10,-26,8,-7,21,-4,16,-14,4,-1,-11,-9,-4],[0,22,-14,3,-28,-18,-10,3,1,0,-9,15,3,-11,-9,-2],[28,-65,2,-35,-18,9,16,15,4,-3,-5,-5,-3,-13,1,-1],[188,51,-20,23,24,27,-14,4,0,1,-6,2,4,-1,1,6],[64,15,12,-1,-8,-1,-14,12,-1,-9,-21,-4,-4,3,-8,5],[86,24,24,19,-48,11,0,7,-7,10,4,15,5,1,1,-4],[48,-10,41,0,-16,-32,22,19,-21,1,-4,-5,-1,-5,1,0],[187,-8,-3,31,-1,29,-3,-26,-2,-7,9,-4,0,14,0,4],[143,-36,-7,11,18,-30,-20,8,-16,-11,7,-10,-2,-7,-4,-1],[95,117,-48,0,14,-18,15,2,-12,0,4,-9,2,0,-6,-7],[-56,-48,2,-5,-30,9,-12,36,-2,11,1,-3,4,-4,-9,6],[179,-20,26,-4,2,-24,7,-8,20,-4,9,14,1,7,3,0]]

assert len(U)==16 and all(len(row)==16 for row in U)
assert abs(int(Matrix(U).det()))==P**21
for k in range(1,7):
    mod=P**k
    assert all(sum(x*pow(r,-k,mod) for r,x in enumerate(row,1))%mod==0 for row in U)

# Exact Gram-Schmidt of the weighted, saturated homogeneous q0 lattice.
B=[[x*w for x,w in zip(row,W)] for row in U]
G=Matrix(B)*Matrix(B).T
mu=[[Fraction(0)]*16 for _ in range(16)]
D=[]
for i in range(16):
    for j in range(i):
        mu[i][j]=(Fraction(int(G[i,j]))-sum(mu[i][k]*mu[j][k]*D[k] for k in range(j)))/D[j]
    D.append(Fraction(int(G[i,i]))-sum(mu[i][j]*mu[i][j]*D[j] for j in range(i)))
Dmin=min(D)
Minv=Matrix(U).inv()
Q=math.lcm(*(int(x.q) for x in Minv))
N=[[int(Minv[i,j]*Q) for j in range(16)] for i in range(16)]


def particular_atom(q,r):
    """One exact integral q0 representative compensating vertical (q,r)."""
    u=[0]*16
    A=[[int(i==j) for j in range(16)] for i in range(16)]
    for k in range(1,7):
        mod=P**k
        coeff=[pow(j,-k,mod) for j in range(1,P)]
        residual=(-pow(P*q+r,-k,mod)-sum(a*c for a,c in zip(u,coeff)))%mod
        values=[sum(a*c for a,c in zip(row,coeff))%mod for row in A]
        piv=next(i for i,val in enumerate(values) if val%P)
        inv=pow(values[piv],-1,mod)
        u=[a+((residual*inv)%mod)*b for a,b in zip(u,A[piv])]
        pivot=A[piv]
        A=[[mod*x for x in row] if i==piv else
           [a-((values[i]*inv)%mod)*b for a,b in zip(row,pivot)]
           for i,row in enumerate(A)]
    for k in range(1,7):
        mod=P**k
        assert (sum(v*pow(r,-k,mod) for r,v in enumerate(u,1))+
                pow(P*q+r,-k,mod))%mod==0
    return u

ATOMS={}
for q in range(1,7):
    for r in range(1,17):
        u=particular_atom(q,r)
        ATOMS[q,r]=(tuple(sum(u[j]*N[j][i] for j in range(16)) for i in range(16)),
                    P*(P*q+r)-1)


def partitions(s,least=1):
    if s==0:
        yield ()
    else:
        for q in range(least,s+1):
            for rest in partitions(s-q,q):
                yield (q,)+rest


def vertical_states(s):
    for pt in partitions(s):
        grouped=[[(q,res) for res in combinations_with_replacement(range(1,17),pt.count(q))]
                 for q in sorted(set(pt))]
        for grp in product(*grouped):
            atoms=tuple((q,r) for q,rs in grp for r in rs)
            cost=sum(ATOMS[a][1] for a in atoms)
            if cost>BUDGET:
                continue
            coord=[0]*16
            for a in atoms:
                v=ATOMS[a][0]
                for i in range(16):coord[i]+=v[i]
            yield (atoms,cost,tuple(coord))

STATES={i:list(vertical_states(i)) for i in range(7)}
assert [len(STATES[i]) for i in range(7)]==[1,16,152,1088,6460,30040,47628]
RMAX={}
for a,b in ((3,3),):
    ca=min(x[1] for x in STATES[a]);cb=min(x[1] for x in STATES[b])
    RMAX[f'{a},{b}']=(BUDGET-ca)**2+(BUDGET-cb)**2
assert max(RMAX.values())<Dmin  # at most floor and ceil at every coordinate


def ball_search(pos,neg):
    """Return (visited GS nodes, sphere leaves, budget-valid q0 solution).
    Every potential solution is included. The full rational sphere bound is a
    necessary relaxation of two separate signed exponent-mass constraints.
    """
    _,cp,pp=pos
    _,cn,nn=neg
    c=[Fraction(a-b,Q) for a,b in zip(pp,nn)]
    radius=(BUDGET-cp)**2+(BUDGET-cn)**2
    z=c[:]
    n=[0]*16
    count=0
    leaves=0
    def go(i,spent):
        nonlocal count,leaves
        if i<0:
            leaves+=1
            u=[sum((c[j]+n[j])*U[j][r] for j in range(16)) for r in range(16)]
            assert all(x.denominator==1 for x in u)
            u=[int(x) for x in u]
            plus=sum(w*max(0,x) for w,x in zip(W,u))
            minus=sum(w*max(0,-x) for w,x in zip(W,u))
            if cp+plus<=BUDGET and cn+minus<=BUDGET:return u
            return None
        count+=1
        center=c[i]+sum(z[j]*mu[j][i] for j in range(i+1,16))
        floor=math.floor(-center)
        for ni in (floor,floor+1):
            nex=spent+D[i]*(center+ni)**2
            if nex<=radius:
                z[i]=c[i]+ni;n[i]=ni
                found=go(i-1,nex)
                if found is not None:return found
        z[i]=c[i]
        return None
    sol=go(15,Fraction(0))
    return count,leaves,sol


def main():
    out={'schema':'T6_P17_VERTICAL_ORDER6_SPLIT3_3_AUTHOR_EXACT_EXCLUSION_V1',
         'source_p17_q0_basis_blob_sha1':'d9ac014355a6a1058cc8a0cf2141a01082628881',
         'source_task_pin':'d84bd940cfb093cdc60e569f15cad58772a51dca',
         'mass_per_side':BUDGET,
         'basis_determinant_abs':str(abs(int(Matrix(U).det()))),
         'minimum_exact_GS_squared':[str(Dmin.numerator),str(Dmin.denominator)],
         'maximum_split_squared_radius':RMAX,'states_by_order':{str(k):len(v) for k,v in STATES.items()},
         'split_counts':{},'survivors':[],'state':'AUTHOR_EXACT_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED'}
    for a,b in ((3,3),):
        stats={'raw_pairs':0,'shared_named_vertical_pairs':0,
               'primitive_pairs_checked':0,'full_sphere_leaves':0,'budget_valid_kernels':0,
               'recursion_nodes_by_depth':{}}
        for index,pos in enumerate(STATES[a]):
            for neg in STATES[b][index+1:]:  # unordered distinct pairs up to overall sign
                stats['raw_pairs']+=1
                if set(pos[0])&set(neg[0]):
                    stats['shared_named_vertical_pairs']+=1;continue
                stats['primitive_pairs_checked']+=1
                nodes,leaves,sol=ball_search(pos,neg)
                stats['full_sphere_leaves']+=leaves
                stats['recursion_nodes_by_depth'][str(nodes)]=stats['recursion_nodes_by_depth'].get(str(nodes),0)+1
                if sol is not None:
                    stats['budget_valid_kernels']+=1
                    out['survivors'].append({'positive_vertical':pos[0],
                                            'negative_vertical':neg[0],'q0_signed':sol})
        out['split_counts'][f'{a},{b}']=stats
        print('split',a,b,'checked',stats['primitive_pairs_checked'],
              'survivors',stats['budget_valid_kernels'],flush=True)
    assert out['split_counts']['3,3']['raw_pairs']==591328
    assert out['split_counts']['3,3']['shared_named_vertical_pairs']==171136
    assert out['split_counts']['3,3']['primitive_pairs_checked']==420192
    assert out['split_counts']['3,3']['full_sphere_leaves']==0
    assert not out['survivors']
    path=Path('T6_P17_Q6_SPLIT3_3_REPRODUCER_CERT_20261123.json')
    path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('certificate',str(path),'sha256',hashlib.sha256(path.read_bytes()).hexdigest())
    return out

if __name__=='__main__':main()
