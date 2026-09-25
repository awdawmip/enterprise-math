#!/usr/bin/env python3
"""Exact H0M controls. Does NOT assert algebraicity or execute an unavailable Ext solver.
Run from anywhere: python this_file.py [--output result.json]
Dependency: sympy. All mathematical arithmetic is rational/integer, never floating-point.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, factorial
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'research_artifacts/HODGE_H0M_WEIL_SIXFOLD'

def gp(z:tuple[int,int], n:int)->tuple[int,int]:
    out=(1,0)
    for _ in range(n): out=(out[0]*z[0]-out[1]*z[1],out[0]*z[1]+out[1]*z[0])
    return out

def mul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])

def D(k:int):
    M=S.zeros(2**k)
    for col in range(2**k):
        for j in range(k):
            M[col^(1<<j),col] += 1 if (col>>j)&1 else -1
    return M

def sparse_derivation(v:dict[tuple[int,...],S.Rational]):
    out=Counter()
    for ids,c in v.items():
        for p,j in enumerate(ids):
            q=j^1
            if q in ids: continue
            new=list(ids); new[p]=q
            inversions=sum(new[a]>new[b] for a in range(6) for b in range(a+1,6))
            out[tuple(sorted(new))]+=c*((-1)**inversions)*(1 if j%2 else -1)
    return {k:v for k,v in out.items() if v}

def main():
    model_path=A/'HODGE_H0M_WEIL_SIXFOLD_MODEL_SPEC.json'
    model=json.loads(model_path.read_text())
    ledger=json.loads((A/'HODGE_H0M_LITERATURE_FRONTIER_LEDGER.json').read_text())
    assert sha256(model_path.read_bytes()).hexdigest()==ledger['model_sha256']
    assert model['candidate_cycle'] is None and model['cycle_search_started_before_freeze'] is False
    ds=model['homology_hermitian_form']['diagonal']
    H=S.diag(*ds); assert H.det()==-3
    I2=S.Matrix([[0,-1],[1,0]])
    Ih=S.diag(*([I2]*6))
    E=S.diag(*[S.Matrix([[0,d],[-d,0]]) for d in ds])
    J0=S.diag(*[I2*(1 if d>0 else -1) for d in ds])
    assert J0*J0==-S.eye(12) and J0*Ih==Ih*J0
    assert J0.T*E*J0==E
    assert E*J0==S.diag(*[abs(d) for d in ds for _ in range(2)])
    assert E.det()==9 and Ih.T*E*Ih==E
    assert sorted(abs(d) for d in ds)==[1,1,1,1,1,3]

    # 924-dimensional exterior algebra broken into exact occupancy-invariant blocks.
    occupancy=Counter()
    for ids in combinations(range(12),6):
        n=[int(2*j in ids)+int(2*j+1 in ids) for j in range(6)]
        occupancy[n.count(1)]+=1
    block_counts={0:20,2:90,4:30,6:1}
    block_ranks={k:int(DomainMatrix.from_Matrix(D(k)**2+36*S.eye(2**k)).rank()) for k in block_counts}
    assert block_ranks=={0:1,2:4,4:16,6:62}
    assert occupancy==Counter({k:v*2**k for k,v in block_counts.items()})
    total=sum(block_counts[k]*2**k for k in block_counts)
    rank=sum(block_counts[k]*block_ranks[k] for k in block_counts)
    assert (total,rank,total-rank)==(924,922,2)
    r=S.Matrix([0 if b.bit_count()%2 else (-1)**(b.bit_count()//2) for b in range(64)])
    s=S.Matrix([0 if b.bit_count()%2==0 else (-1)**((b.bit_count()-1)//2) for b in range(64)])
    assert D(6)*r==-6*s and D(6)*s==6*r
    assert S.Matrix.hstack(r,s).rank()==2
    # Polarization cube (unnormalized) has only double-occupancy terms.
    theta3={tuple(t for j in js for t in [2*j,2*j+1]):6*S.prod(ds[j] for j in js) for js in combinations(range(6),3)}
    assert theta3 and not sparse_derivation(theta3)
    signature=(sum(d>0 for d in ds),sum(d<0 for d in ds))
    assert signature==(3,3) and signature[::-1]==(3,3)  # determinant-line Hodge counts, not a cycle-existence test
    weights=[comb(6,a)**2 for a in range(7)]
    assert weights==[1,36,225,400,225,36,1] and sum(weights)==924

    # Full rational algebraic projector from the isogeny [1+2i]^* on H^6.
    x=S.symbols('x'); eigen=[mul(gp((1,2),a),gp((1,-2),6-a)) for a in range(7)]
    assert eigen[6]==(117,44) and eigen[3]==(125,0)
    q=S.Poly(x*x-234*x+15625,x,domain=S.QQ)
    other=S.Poly(x-125,x,domain=S.QQ)
    for a in (1,2):
        re,im=eigen[a]
        other*=S.Poly(x*x-2*re*x+re*re+im*im,x,domain=S.QQ)
    inverse=S.invert(other,q)
    projector=other*inverse
    minimum=other*q
    assert (projector*projector-projector).rem(minimum).is_zero
    assert projector.rem(q).as_expr()==1 and projector.rem(other).is_zero
    for a,(re,im) in enumerate(eigen):
        assert S.expand(projector.as_expr().subs(x,re+S.I*im))==int(a in (0,6))
    TW=S.Matrix([[117,44],[-44,117]])
    assert TW*TW-234*TW+15625*S.eye(2)==S.zeros(2)
    aa,bb=S.symbols('a b',real=True)
    assert S.Matrix.hstack(S.Matrix([aa,bb]),TW*S.Matrix([aa,bb])).det()==-44*(aa*aa+bb*bb)
    # Conditional arithmetic only: these vectors are NOT asserted to be cycle classes.
    rational_tests=0
    for seed in ([1,0],[S.Rational(2,3),S.Rational(-5,7)],[-3,2]):
        v=S.Matrix(seed); basis=S.Matrix.hstack(v,TW*v)
        for target in ([S.Rational(-2,3),S.Rational(5,7)],[0,0],[1,S.Rational(-1,11)]):
            w=S.Matrix(target); coeff=basis.inv()*w
            assert basis*coeff==w; rational_tests+=1

    # Universal norm obstruction has an exact modulo-p descent proof in the return;
    # these residue enumerations check the only possible first obstruction step.
    local_norm_certificates={}
    for p in [3,7]:
        zeros=[(a,b) for a,b in product(range(p),repeat=2) if (a*a+b*b)%p==0]
        assert zeros==[(0,0)]
        local_norm_certificates[str(p)]=zeros
    valuation_classes={"1":[0,0],"3":[1,0],"7":[0,1],"21":[1,1]}
    assert len({tuple(v) for v in valuation_classes.values()})==4
    # determinant law is proved universally by multiplicativity; exact instances check conventions.
    transport_tests=0
    for c in [S.Rational(1,3),S.Rational(2),S.Rational(7,5)]:
        for z in [1+2*S.I,S.Rational(2,3)+S.Rational(5,7)*S.I,3+S.I]:
            M=S.eye(6); M[0,0]=z; M[1,4]=S.Rational(1,3)+S.I
            dest=c*S.conjugate(M).T*H*M
            norm=S.expand(S.conjugate(M.det())*M.det())
            assert S.simplify(dest.det()/H.det()-c**6*norm)==0
            assert S.simplify(c**6*norm-(c**3*M.det())*S.conjugate(c**3*M.det()))==0
            transport_tests+=1
    assert H.inv().det()/H.det()==S.Rational(1,9)

    # Actual first-order bundle deformation of O_A^2 with nonzero quadratic obstruction.
    X=S.Matrix([[0,1],[0,0]]); Y=S.Matrix([[0,0],[1,0]])
    bracket=X*Y-Y*X
    assert bracket==S.diag(1,-1) and bracket.trace()==0 and bracket!=S.zeros(2)
    ext2=comb(6,2)*4; trace_rank=comb(6,2)
    assert (ext2,trace_rank,ext2-trace_rank)==(60,15,45)

    # Exact boundary witnesses for surfaced unverified generalization claims.
    torsion_degree=3**12; assert torsion_degree==531441 and torsion_degree!=3**2
    data={'schema':'HODGE_H0M_EXACT_CHECK_V1','status':'PASS','sympy_version':S.__version__,
      'model_sha256':ledger['model_sha256'],'ambient_H6_dimension':total,'D2_plus_36_rank':rank,
      'Weil_Q_dimension':2,'Weil_Hodge_type':[3,3],'block_counts':block_counts,'block_ranks':block_ranks,
      'signature':[3,3],'hermitian_determinant':-3,'polarization_type':[1,1,1,1,1,3],
      'eigenvalues_T_as_Gaussian_pairs':eigen,'weight_multiplicities':weights,
      'Weil_minimal_polynomial':str(q.as_expr()),'other_minimal_factor':str(other.as_expr()),
      'full_Weil_projector':str(projector.as_expr()),'projector_coefficients_descending':[str(t) for t in projector.all_coeffs()],
      'projector_full_H6_idempotent':True,'conditional_rational_lift_tests':rational_tests,
      'norm_residue_certificates':local_norm_certificates,'independent_3_7_parity_classes':valuation_classes,
      'determinant_transport_exact_instances':transport_tests,'null_control':{'object':'O_A^2','Ext2_dimension':ext2,'semiregularity_rank':trace_rank,'kernel_dimension':ext2-trace_rank,'quadratic_obstruction_matrix':[[1,0],[0,-1]],'interpretation':'u wedge v tensor [X,Y] is nonzero for independent invariant (0,1)-forms u,v; its semiregularity image is zero.'},
      'degree_of_A_to_A_mod_A3':torsion_degree,
      'actual_frontier_cycle_found':False,'algebraicity_asserted':False,'global_derived_transport_no_go_asserted':False,
      'finite_check_limit':'Finite matrices and polynomial identities only. The infinite norm-parity proof, period-domain existence, and generic divisor input are stated/proven or attributed separately. No checker assertion certifies an open cycle-existence statement.'}
    parser=argparse.ArgumentParser(); parser.add_argument('--output'); args=parser.parse_args()
    text=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    if args.output: Path(args.output).write_text(text)
    print(text,end='')

if __name__=='__main__': main()
