#!/usr/bin/env python3
"""Independent exact finite witness for the universal BRC rational-numerator and Newton extraction proof.
Uses original signed 12-step K/J recurrence, integer polynomial arithmetic, and one
independent rational-numerator recurrence. Does not import R330/R336 code.
"""
import argparse
import json
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def add(a, b):
    res = [0] * max(len(a), len(b))
    for i, v in enumerate(a): res[i] += v
    for i, v in enumerate(b): res[i] += v
    return trim(res)


def trim(a):
    while len(a) > 1 and not a[-1]: a.pop()
    return a


def mul(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        if v:
            for j, w in enumerate(b):
                if w: z[i+j] += v*w
    return trim(z)


def power_one_minus_two(n):
    return [(-2)**i * choose(n, i) for i in range(n+1)]


def base_monomial(n, coef, shift):
    return [0]*shift + [coef*choose(n, h) for h in range(n+1)] if n >= 0 else [0]


def kernel(i):
    d = (-choose(4,i)+choose(2,i-1),
         choose(5,i-1)-choose(5,i-2),
         choose(7,i-2), -choose(9,i-3))
    out = [0]
    for j, dj in enumerate(d, 1):
        if dj: out = add(out, base_monomial(i+1-j, -dj, i-1))
    return out


def forcing(i):
    out = [0]
    for coef, n in ((-choose(3,i-1),i),(-choose(6,i-1),i-1),(choose(8,i-2),i-2)):
        if coef: out = add(out, base_monomial(n, coef, i))
    return out


def build_B(max_s, K, J):
    out = [[1,1]]
    for s in range(1,max_s+1):
        p = J[s] if s<len(J) else [0]
        for i in range(1,min(s,12)+1): p=add(p,mul(K[i],out[s-i]))
        out.append(trim(p))
    return out


def build_rational_numerators(max_q, K, J):
    # K(x,t)=2x+sum_{h>=1} L_h(x)t^h; A=1+t+sum_{s>=1}J_s(t)x^s.
    L=[]; A=[]
    for q in range(max_q+1):
        L.append(trim([K[i][q] if q<len(K[i]) else 0 for i in range(13)]))
        a = [int(q==0) + int(q==1)]
        for s in range(1,11): a.append(J[s][q] if q<len(J[s]) else 0)
        A.append(trim(a))
    assert L[0]==[0,2], L[0]
    assert A[0]==[1], A[0]
    for q in range(1,max_q+1):
        assert len(L[q])-1 <= q+1, (q,'K degree')
        assert len(A[q])-1 <= q, (q,'A degree')
    P=[[1]]
    for q in range(1,max_q+1):
        row=mul(power_one_minus_two(q),A[q]);
        for h in range(1,q+1):
            row=add(row,mul(mul(L[h],power_one_minus_two(h-1)),P[q-h]))
        assert len(row)-1 <= 2*q,(q,len(row)-1,2*q)
        P.append(row)
    return P,L,A


def transformed_coefficients(P):
    # P_q((1-y)/2)=[y^j] ... ; use exact rational substitution.
    return [Fraction((-1)**j)*sum((Fraction(v*choose(h,j), 2**h) for h,v in enumerate(P) if h>=j), Fraction(0))
            for j in range(len(P))]


def recovered_coeff(P, s, q):
    return sum(v*2**(s-h)*choose(s-h+q,q)
               for h,v in enumerate(P) if h<=s)


def source_D(B,q,k):
    return sum((-1)**(k-v)*choose(k,v)*2**(q-v)*B[q+v][q]
               for v in range(k+1))


def extracted_D(p,q,k):
    r=q-k
    return 4**q*sum(p[j]*choose(2*q-j,r-j) for j in range(r+1))


def run(qmax=24):
    assert 1<=qmax<=64
    K=[[0]]+[kernel(i) for i in range(1,13)]
    J=[[0]]+[forcing(i) for i in range(1,11)]
    S=max(2*qmax+2, 3*min(qmax,18)+2)
    B=build_B(S,K,J)
    P,L,A=build_rational_numerators(qmax,K,J)
    poles=0; dchecks=0; interior=0; neg_outer=0; ptests=0; highest_checks=0
    digest=sha256(); samples=[]
    for s,row in enumerate(B):
        interior += sum(1 for q in range(s+1) if q<len(row) and row[q]>0)
        assert all(q<len(row) and row[q]>0 for q in range(s+1))
        neg_outer += sum(v<0 for v in row[s+1:])
    for q in range(qmax+1):
        p=transformed_coefficients(P[q]); ptests+=len(p)
        assert len(p)<=2*q+1
        for s in range(S+1):
            true=B[s][q] if q<len(B[s]) else 0
            assert recovered_coeff(P[q],s,q)==true,('pole numerator',q,s)
            poles+=1
        for k in range(q+1):
            lhs=source_D(B,q,k)
            rhs=extracted_D(p,q,k)
            assert rhs.denominator==1 and lhs==int(rhs),('Newton extraction',q,k,lhs,rhs)
            dchecks+=1
            digest.update(f'{q},{k}:{lhs}\n'.encode())
        if q in (0,1,2,3,qmax):
            samples.append({'q':q,'deg_Pq':len(P[q])-1,'p0':str(p[0]),
                'D_q_0':str(source_D(B,q,0)), 'D_q_q':str(source_D(B,q,q))})
    # The top Newton coefficient of H_r(u)=5^{-u} D_{r+u,u} is 6^r.
    for r in range(min(qmax,18)+1):
        seq=[Fraction(source_D(B,r+u,u),5**u) for u in range(r+1)]
        for order in range(r):
            seq=[seq[i+1]-seq[i] for i in range(len(seq)-1)]
        assert seq[0] == 6**r, ('universal top coefficient',r,seq[0])
        highest_checks+=1
    return {'schema':'R337_INDEPENDENT_POLE_EXTRACTION_CERT_V1',
            'status':'PASS','q_checked':[0,qmax],'B_rows':[0,S],
            'pole_numerator_coeff_reconstructions':poles,
            'Newton_extraction_equalities':dchecks,
            'top_coefficient_r_checks':highest_checks,
            'exact_rational_transformation_coefficients':ptests,
            'triangle_positive_count':interior,
            'retained_outer_negative_count':neg_outer,
            'sha256_D_qk_sequence':digest.hexdigest(),
            'samples':samples,
            'infinite_proof_basis':'finite K/J t-degree bounds plus exact rational numerator recurrence and exact coefficient algebra (see proof)',
            'scope':'ordered six-edge signed-tail BRC auxiliary combinatorial model only',
            'review':'AUTHOR_SIDE; UNREVIEWED; NOT_ADMITTED',
            'arithmetic':'Python arbitrary precision integer and Fraction; no float signs'}



# R339 new test, standalone by reusing the above exact R337 kernel and numerator helpers.
# All twelve signed K/J terms retained; no floating-point sign decisions.
def run_r339(limit=128):
    from hashlib import sha256
    from pathlib import Path
    assert 6 <= limit <= 128
    K=[[0]] + [kernel(i) for i in range(1,13)]
    J=[[0]] + [forcing(i) for i in range(1,11)]
    B=build_B(max(130,limit+2),K,J)
    b0={(5,5):219,(6,5):3163,(6,6):1258,(7,6):15466}
    for (s,q),val in b0.items(): assert B[s][q]==val,(s,q,B[s][q])
    d0={(5,0):7008,(5,1):43600,(6,0):80512,(6,1):414400}
    for (q,k),val in d0.items(): assert source_D(B,q,k)==val,(q,k,source_D(B,q,k))
    def minor(q,k):
        return source_D(B,q,k)*source_D(B,q+1,k+1)-source_D(B,q,k+1)*source_D(B,q+1,k)
    assert minor(5,0)==-606208000
    # Reconstruction from rational-numerator representation, independent of B recursion.
    P,L,A=build_rational_numerators(6,K,J)
    for s in range(8):
        for q in range(7):
            assert recovered_coeff(P[q],s,q)==(B[s][q] if q<len(B[s]) else 0)
    adj_neg=[];adj_pos=0
    for q in range(1,65):
        for k in range(q):
            v=minor(q,k)
            assert v!=0
            if v<0: adj_neg.append((q,k))
            else: adj_pos+=1
    assert adj_neg==[(q,0) for q in range(5,65)]
    assert adj_pos==2020
    edge_hash=sha256();edge_signs={}
    for q in range(1,limit+1):
        v=minor(q,0)
        assert (v>0 if q<5 else v<0)
        edge_hash.update(f"{q}:{v}\n".encode())
        if q<=5: edge_signs[str(q)]=str(v)
    tri=sum(1 for s,row in enumerate(B) for q in range(s+1) if row[q]>0)
    assert tri == len(B)*(len(B)+1)//2
    exterior=sum(z<0 for s,row in enumerate(B) for z in row[s+1:])
    assert exterior>0
    return {"schema":"EM_R339_BRC_TP2_OBSTRUCTION_EXACT_V1",
      "status":"PASS","witness_b":{str(k):v for k,v in b0.items()},
      "witness_D":{str(k):v for k,v in d0.items()},
      "M_5_0":minor(5,0),"first_negative_adjacent_minor":[5,0],
      "q_le_4_all_adjacent_minors_positive":True,
      "all_adjacent_q_1_to_64":{"total":2080,"positive":adj_pos,"negative":len(adj_neg),
         "negative_positions":"exactly (q,0) for 5<=q<=64"},
      "edge_k0":{"q_min":1,"q_max":limit,"positive":[1,4],"negative":[5,limit],
         "first_five":edge_signs,"sha256_q_colon_minor_lines":edge_hash.hexdigest()},
      "P_q_independent_reconstruction_equalities":56,
      "signed_B_rows":[0,len(B)-1],
      "B_triangle_strict_positive":tri,
      "B_exterior_negatives_retained":exterior,
      "claim":"One negative 2x2 minor refutes global TN2/TP2, not entrywise positivity",
      "method":"exact arbitrary precision integers, full signed K/J recurrence",
      "research_status":"AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED"}

if __name__=="__main__":
    import argparse
    cli=argparse.ArgumentParser()
    cli.add_argument("--limit",type=int,default=128)
    cli.add_argument("--output",default="R339_EVIDENCE.json")
    a=cli.parse_args()
    result=run_r339(a.limit)
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print("R339 EXACT PASS",result["M_5_0"],result["edge_k0"]["sha256_q_colon_minor_lines"])
