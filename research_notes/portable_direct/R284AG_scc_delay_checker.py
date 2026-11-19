#!/usr/bin/env python3
"""R284AG: exact auxiliary graph-pencil certificate checks (not a native BRC run)."""
from itertools import combinations, product
from random import Random
import json
import sympy as s

SEED = 284017

def determinant(A):
    return A.det(method='bareiss') if A.rows else s.Integer(1)

def sccs(A):
    n=A.rows
    # Reachability closure, then mutual reachability partition.
    reach=[[bool(A[i,j]) for j in range(n)] for i in range(n)]
    for i in range(n): reach[i][i]=True
    for k in range(n):
        for i in range(n):
            for j in range(n): reach[i][j] |= reach[i][k] and reach[k][j]
    remain=set(range(n)); blocks=[]
    while remain:
        i=min(remain)
        block=tuple(j for j in sorted(remain) if reach[i][j] and reach[j][i])
        blocks.append(block)
        remain.difference_update(block)
    return blocks

def principal(A, idx):
    return A.extract(list(idx),list(idx))

def pencil(A, t):
    return A + s.diag(*t)

def sum_minor_expansion(A,t):
    n=A.rows
    ans=0
    for mask in range(1<<n):
        S=[i for i in range(n) if mask>>i&1]
        T=[i for i in range(n) if not mask>>i&1]
        ans += determinant(principal(A,T))*s.prod(t[i] for i in S)
    return s.expand(ans)

def earliest_degree(A):
    n=A.rows
    for d in range(n+1):
        for S in combinations(range(n),d):
            T=[i for i in range(n) if i not in S]
            if determinant(principal(A,T)) != 0:
                return d
    raise AssertionError('highest-degree monomial always present')

def make_family(q, d):
    """rank(N)=q-1; attainable d=1..q-2 or d=q."""
    if d!=q and not 1<=d<=q-2: raise ValueError((q,d))
    N=s.zeros(q)
    if d==q:
        for i in range(q-1): N[i,i+1]=s.Rational(1,i+2)
        cycle_weight=s.Integer(0)
    else:
        ell=q-d
        weights=[s.Rational(1,j+2) for j in range(ell)]
        for j,w in enumerate(weights): N[j,(j+1)%ell]=w
        for j in range(ell,q-1): N[j,j+1]=s.Rational(1,j+2)
        cycle_weight=s.prod(weights)
    return N,cycle_weight

def check():
    rng=Random(SEED)
    random_graph_cases=minor_coeff_checks=scc_checks=full_rank_baselines=family_evals=0
    cycle_witness_checks=forbidden_gap_checks=0
    for q in range(2,7):
        for case in range(5):
            A=s.zeros(q)
            for i in range(q):
                for j in range(q):
                    if i!=j and rng.randrange(4)<2:
                        A[i,j]=s.Rational(rng.choice((-3,-2,-1,1,2,3)),rng.choice((4,5,7)))
            block=sccs(A)
            values=[determinant(pencil(A, [s.Integer((mask>>i)&1) for i in range(q)])) for mask in range(1<<q)]
            coeffs=list(values)
            for bit in range(q):
                for mask in range(1<<q):
                    if mask & (1<<bit): coeffs[mask] -= coeffs[mask ^ (1<<bit)]
            for mask in range(1<<q):
                T=[i for i in range(q) if not (mask>>i&1)]
                assert coeffs[mask]==determinant(principal(A,T))
                minor_coeff_checks += 1
            for k in range(3):
                t=[s.Rational(rng.randrange(0,4),7) for _ in range(q)]
                assert determinant(pencil(A,t))==sum_minor_expansion(A,t)
                assert determinant(pencil(A,t))==s.prod(determinant(pencil(principal(A,B),[t[i] for i in B])) for B in block)
                scc_checks+=1
            dag=all(len(B)==1 for B in block) # zero diagonal
            assert (earliest_degree(A)==q)==dag
            assert earliest_degree(A)!=q-1
            forbidden_gap_checks+=1
            # Minimum cycle: no chord contributes another permutation.
            cycles=[]
            for length in range(2,q+1):
                for seq in product(range(q),repeat=length):
                    if len(set(seq))==length and seq[0]==min(seq) and all(A[seq[i],seq[(i+1)%length]]!=0 for i in range(length)):
                        cycles.append(seq)
                if cycles: break
            if cycles:
                C=cycles[0]
                expected=(-1)**(len(C)-1)*s.prod(A[C[i],C[(i+1)%len(C)]] for i in range(len(C)))
                assert determinant(principal(A,C))==expected
                cycle_witness_checks+=1
            random_graph_cases+=1
        for d in list(range(1,q-1))+[q]:
            N,w=make_family(q,d)
            assert N.rank()==q-1
            assert earliest_degree(N)==d
            full_rank_baselines+=1
            ell=q-d
            for _ in range(18):
                t=[s.Rational(rng.randrange(4),11) for _ in range(q)]
                if d==q:
                    formula=s.prod(t)
                else:
                    formula=s.prod(t[ell:])*(s.prod(t[:ell])+(-1)**(ell-1)*w)
                assert determinant(pencil(N,t))==formula
                family_evals+=1
    # Zero-diagonal exclusion is tight: a self-loop recovers degree q-1.
    loop=s.zeros(5);loop[0,0]=1
    for i in range(1,4):loop[i,i+1]=1
    assert loop.rank()==4 and earliest_degree(loop)==4
    # Stable positive embedding of SCC+chain family, q=6,d=3.
    q,d=6,3; N,w=make_family(q,d); k=q+1; c=s.Rational(1,16*k)
    ts=[c*s.Rational(1,2) for i in range(q)]
    C=c*s.ones(k,k)
    for i in range(q):
        for j in range(q):C[i,j]+=c*N[i,j]
        C[i,i]+=ts[i]
    assert min(C)>0
    assert max(sum(C[i,j] for j in range(k)) for i in range(k))<1
    target=c*(s.prod(ts[3:])*(s.prod(ts[:3])+c**3*w)) # 3-cycle has + sign
    assert determinant(C)==target and target!=0
    C0=C.copy()
    for i in range(q): C0[i,i]-=ts[i]
    assert C0.rank()==k-1
    # Complete Port determinant tested on smaller nontrivial cycle+chain member.
    qp,dp=3,1
    Np,wp=make_family(qp,dp);kp=qp+1;cp=s.Rational(1,16*kp)
    tp=[cp/2]*qp
    Cp=cp*s.ones(kp,kp)
    for i in range(qp):
        for j in range(qp):Cp[i,j]+=cp*Np[i,j]
        Cp[i,i]+=tp[i]
    gate=s.Rational(1,16);delta=s.Rational(1,256*kp)
    I=s.eye(kp);D=delta*s.ones(kp,kp);O=s.zeros(kp,kp)
    Port=s.BlockMatrix([[I-D,-Cp,O],[-D,I-D,-gate*I],[-gate*I,O,O]]).as_explicit()
    assert determinant(Port)==(-1)**kp*gate**(2*kp)*determinant(Cp)
    assert Port.rank()==3*kp
    Cp0=Cp.copy()
    for i in range(qp): Cp0[i,i]-=tp[i]
    Port0=s.BlockMatrix([[I-D,-Cp0,O],[-D,I-D,-gate*I],[-gate*I,O,O]]).as_explicit()
    assert determinant(Port0)==0 and Port0.rank()==3*kp-1
    result={"schema":"R284AG_GRAPH_DELAY_EXACT_CHECK_V1","status":"PASS", "date":"2026-11-19",
       "seed":SEED,"arithmetic":"SymPy exact Rational/Bareiss, no floating-point; auxiliary matrix algebra, no native BRC dynamics",
       "random_graph_cases":random_graph_cases,"principal_minor_coefficient_enumerations":minor_coeff_checks,
       "scc_factorization_numeric_checks":scc_checks,"shortest_cycle_minor_witness_checks":cycle_witness_checks,
       "missing_degree_q_minus_1_checks":forbidden_gap_checks,"corank_one_constructed_families":full_rank_baselines,
       "family_polynomial_evaluations":family_evals,"loop_gap_counterexample":"q=5 corank=1 first-degree=4",
       "positive_core_scc_example":{"q":q,"d":d,"c":str(c),"det":str(determinant(C)),"rank_0":1+N.rank(),"example_q3_full_port_det":str(determinant(Port)),"example_q3_full_port_rank":Port.rank(),"example_q3_baseline_port_rank":Port0.rank()},
       "scope":"Finite exact cross-checks; general theorem supplied by independent algebraic proof; NOT_REVIEWED"}
    return result
if __name__=='__main__':print(json.dumps(check(),indent=2,sort_keys=True))
