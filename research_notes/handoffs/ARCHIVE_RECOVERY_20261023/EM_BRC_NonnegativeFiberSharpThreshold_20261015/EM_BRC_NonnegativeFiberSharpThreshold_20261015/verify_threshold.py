#!/usr/bin/env python3
"""Exact independent checks for the external affine-incidence BRC observation model.
No floating point. p=5 exhaustive census through total mass 5; p=7 targeted witness.
"""
from itertools import combinations_with_replacement
from collections import defaultdict
import json
from pathlib import Path


def model(p):
    X=[(x,y) for x in range(p) for y in range(p) if (x,y)!=(0,0)]
    idx={pt:i for i,pt in enumerate(X)}
    # Each direction is represented by the nonzero linear functional x + m y,
    # plus the vertical one y. Legal non-origin affine lines have t != 0.
    dfn=[lambda a,b,m=m:(a+m*b)%p for m in range(p)]
    dfn.append(lambda a,b:b)
    ports=[]; kernels=[]
    for d,fun in enumerate(dfn):
        K=set(i for i,(a,b) in enumerate(X) if fun(a,b)==0)
        for t in range(1,p):
            L=set(i for i,(a,b) in enumerate(X) if fun(a,b)==t)
            assert len(K)==p-1 and len(L)==p and not K.intersection(L)
            ports.append((d,t,L));kernels.append(K)
    n=len(X)
    assert n==len(ports)==p*p-1
    Y=[[int(x in L) for x in range(n)] for _,_,L in ports]
    B=[[int(x in ports[j][2])-int(x in kernels[j]) for j in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            assert sum(Y[i][k]*B[k][j] for k in range(n))==(p if i==j else 0)
    return X,ports,kernels,Y,B


def residue_for_points(points,Y,p):
    return bytes(sum(row[i] for i in points)%p for row in Y)


def check_isolated(F, B):
    n=len(F)
    for j in range(n):
        for k in range(n):
            if j==k:continue
            if all(F[i]-B[i][j]+B[i][k]>=0 for i in range(n)):
                return False,(j,k)
    return True,None


def execute():
    out={'schema':'EM_BRC_NONNEGATIVE_FIBER_SHARP_THRESHOLD_EXACT_V1',
         'meaning':'external finite-field integer-incidence auxiliary model only',
         'completed_checks':[]}
    p=5; X,ports,ks,Y,B=model(p);n=len(X)
    counts=[]
    for N in range(0,p+1):
        seen={}; total=0; collisions=0; zero=[]; collided_groups={}
        for choices in combinations_with_replacement(range(n),N):
            residue=residue_for_points(choices,Y,p)
            if residue in seen:
                collisions+=1
                if residue not in collided_groups:collided_groups[residue]=[seen[residue]]
                collided_groups[residue].append(choices)
            else: seen[residue]=choices
            if all(a==0 for a in residue):zero.append(choices)
            total+=1
        if N<p: assert collisions==0,(N,collisions)
        if N==p:
            predicted={tuple([x]*p) for x in range(n)}
            assert set(zero)==predicted,(len(zero),len(predicted))
            expected_groups=[predicted]
            for direction in range(p+1):
                group={tuple(sorted(L)) for d,t,L in ports if d==direction}
                assert len(group)==p-1
                expected_groups.append(group)
            got={frozenset(v) for v in collided_groups.values()}
            expected={frozenset(v) for v in expected_groups}
            assert got==expected, (len(got),len(expected))
            assert sorted(len(v) for v in collided_groups.values())==[p-1]*(p+1)+[p*p-1]
            # Classify every move by its exact negative integer mass.
            by_direction={}
            for i in range(n):
                for j in range(n):
                    if i==j: continue
                    direction_type='same' if ports[i][0]==ports[j][0] else 'cross'
                    budget=sum(max(0,B[x][i]-B[x][j]) for x in range(n))
                    by_direction.setdefault(direction_type,set()).add(budget)
            assert by_direction=={'same':{p},'cross':{2*p-2}},by_direction
            out['p5_nonnegative_graph_classification']={
                'mass':p,'move_negative_mass_by_type':{k:sorted(v) for k,v in by_direction.items()},
                'nontrivial_residue_fibers':len(collided_groups),
                'fiber_cardinalities':sorted(len(v) for v in collided_groups.values()),
                'nonnegative_components':total-(p+1)*(p-2),
                'isolated_single_point_condensates':p*p-1,
                'excess_components_over_residue_fibers':p*p-2
            }
        counts.append({'mass':N,'states_exhaustively_checked':total,'distinct_residues':len(seen),'duplicate_residue_state_count':collisions,'zero_residue_states':len(zero)})
    out['p5_exhaustive_mass_layers']=counts
    assert counts[-1]['zero_residue_states']==p*p-1
    out['completed_checks'].append('p5: every multiset state for mass N=0..5, exact full-port residue census')
    out['completed_checks'].append('p5: all mass-5 collision fibers: one size 24 atomic fiber and six size 4 parallel-line fibers, exhaustive')
    witness=[]
    for p,N in ((5,5),(5,16),(7,7),(7,24)):
        X,ports,ks,Y,B=model(p);n=len(X)
        z=X.index((1,0));w=X.index((0,1));assert z!=w
        F=[0]*n;G=[0]*n; F[z]=N;G[z]=N-p;G[w]=p
        assert all(a>=0 for a in G)
        assert all(sum(Y[i][x]*(F[x]-G[x]) for x in range(n))%p==0 for i in range(n))
        iso, move=check_isolated(F,B)
        assert iso and move is None
        c=[sum(Y[i][x]*(F[x]-G[x]) for x in range(n))//p for i in range(n)]
        assert all(sum(Y[i][x]*(F[x]-G[x]) for x in range(n))==p*c[i] for i in range(n))
        assert sum(c)==0
        assert all(sum(B[x][i]*c[i] for i in range(n))==F[x]-G[x] for x in range(n))
        d=sum(max(v,0) for v in c)
        assert d==p-1
        witness.append({'p':p,'mass':N,'z':X[z],'w':X[w],
                        'formal_shortest_length':d,'nonnegative_outdegree_from_F':0,
                        'nonnegative_path_exists':False,
                        'residue_equal':True})
    out['witness_checks']=witness
    out['completed_checks'].append('p5,p7: full incidence identity YB=pI and nonnegative reachability obstruction for explicit witnesses')
    return out

if __name__=='__main__':
    result=execute(); dest=Path(__file__).with_name('certificate.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
