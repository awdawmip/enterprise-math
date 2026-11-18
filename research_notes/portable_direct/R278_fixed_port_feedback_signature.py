#!/usr/bin/env python3
"""R278 exact finite rational certificate: determinant/cofactor probe signatures.

Python >=3.10, stdlib only; all arithmetic is fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import permutations, product
from json import dumps

def det(M):
    n=len(M)
    if n==0: return F(1)
    total=F(0)
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=F(-1 if inv%2 else 1)
        for i,j in enumerate(p): term *= M[i][j]
        total+=term
    return total

def star(A,r):
    assert 0<=r<len(A)
    minor=[[A[i][j] for j in range(len(A)) if j!=r] for i in range(len(A)) if i!=r]
    return det(minor)/det(A)

def baseline(W):
    return [[(F(1) if i==j else F(0))-W[i][j] for j in range(len(W))] for i in range(len(W))]

def after_edits(A,edges,values):
    B=[row.copy() for row in A]
    for (u,v),x in zip(edges,values): B[u][v]-=x
    return B

def signature(A,r,edges):
    """Return multiaffine coefficient dicts for D(x),N(x)=D(x)*S'_rr."""
    m=len(edges); denom=det(A)
    D_values={};N_values={}
    for mask in range(1<<m):
        xs=[F(bool(mask & (1<<i))) for i in range(m)]
        B=after_edits(A,edges,xs)
        D_values[mask]=det(B)/denom
        minor=[[B[i][j] for j in range(len(B)) if j!=r] for i in range(len(B)) if i!=r]
        N_values[mask]=det(minor)/denom
    def mobius(vals):
        result={}
        for mask in range(1<<m):
            total=F(0);s=mask
            while True:
                total+=(-1 if ((mask^s).bit_count()%2) else 1)*vals[s]
                if s==0:break
                s=(s-1)&mask
            result[mask]=total
        return result
    D=mobius(D_values);N=mobius(N_values)
    assert D[0]==1
    return D,N

def evaluate(poly,xs):
    y=F(0)
    for mask,c in poly.items():
        term=c
        for i,x in enumerate(xs):
            if mask>>i&1:term*=x
        y+=term
    return y

def q(x):
    return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def calculate():
    witness=[]
    for c in [F(0),F(1,2)]:
        W=[[F(0),F(0)],[F(0),c]]
        A=baseline(W)
        edges=[(0,1),(1,0)]
        D,N=signature(A,0,edges)
        assert N=={0:F(1),1:F(0),2:F(0),3:F(0)}
        assert D=={0:F(1),1:F(0),2:F(0),3:-1/(1-c)}
        singleton=[]
        for xx,yy in [(F(0),F(0)),(F(1,4),F(0)),(F(0),F(1,4))]:
            singleton.append(star(after_edits(A,edges,[xx,yy]),0))
        assert singleton==[1,1,1]
        joint=star(after_edits(A,edges,[F(1,4),F(1,4)]),0)
        expected=F(1)/(F(1)-F(1,16)/(F(1)-c))
        assert joint==expected
        witness.append({'internal_port_loop':q(c),'baseline_and_both_singletons':[q(z) for z in singleton],
                        'both_edges_weight_1_4':q(joint),'denominator_mixed_coefficient':q(D[3])})
    assert [x['both_edges_weight_1_4'] for x in witness]==['16/15','8/7']

    test_cases=[
      ('symmetric_triangle',[[F(0),F(1,8),F(1,8)],[F(1,8),F(0),F(1,8)],[F(1,8),F(1,8),F(0)]],[(0,1),(1,0),(1,2)]),
      ('asymmetric_triangle',[[F(0),F(1,6),F(1,9)],[F(1,8),F(0),F(1,10)],[F(1,7),F(1,12),F(0)]],[(0,1),(1,2),(2,0)]),
      ('looped_chain',[[F(1,9),F(1,10),F(0)],[F(0),F(1,11),F(1,8)],[F(1,12),F(0),F(1,13)]],[(0,2),(1,0),(2,1)])
    ]
    counts=[]
    for name,W,edges in test_cases:
        A=baseline(W)
        assert det(A)>0
        D,N=signature(A,0,edges)
        count=0
        for xs in product([F(0),F(1,8),F(1,4)],repeat=3):
            B=after_edits(A,edges,xs)
            assert det(B)>0
            for i,row in enumerate(W):
                total=sum(row)+sum(x for (u,v),x in zip(edges,xs) if u==i)
                assert total<1
            left=star(B,0)
            right=evaluate(N,xs)/evaluate(D,xs)
            assert left==right
            count+=1
        counts.append({'case':name,'tests':count,'D':[q(D[i]) for i in range(8)],'N':[q(N[i]) for i in range(8)]})
    return {'schema':'R278_EXACT_FRACTION_CERTIFICATE_V1','status':'PASS','number_witness_systems':len(witness),
            'singletons_per_system':2,'joint_witnesses':witness,
            'three_port_models':counts,'three_port_full_direct_checks':sum(x['tests'] for x in counts),
            'arithmetic':'Python fractions.Fraction; determinant via permutation expansion; multiaffine coefficients via Boolean-subset Mobius inversion'}

if __name__=='__main__':
    print(dumps(calculate(),ensure_ascii=False,indent=2))
