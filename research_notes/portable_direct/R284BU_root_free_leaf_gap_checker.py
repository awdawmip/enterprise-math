#!/usr/bin/env python3
"""R284BU: exact endpoint scan of the constant star-Port gap, Python standard library.

The structural proof is in R284BU_SHARP_ROOT_FREE_LEAF_CONSTANT_GAP_20261120.md.
This checker verifies the formula on specified finite alphabet/parameter families;
it does not replace the proof for all H,t,s.
"""
import itertools
import json


def gap(t, s, a, e, b, d, g, h, u1, u2, u3):
    return (u3 * ((t-a)*(s-e)-b*d)
            + u2 * ((t-a)*h+b*g)
            + u1 * (d*h+(s-e)*g))


def det4(mat):
    """Integer determinant by Leibniz, independent of the 3x3 cofactor formula."""
    ans = 0
    for perm in itertools.permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1,4))
        v = (-1) ** inversions
        for i,j in enumerate(perm):
            v *= mat[i][j]
        ans += v
    return ans


def make_matrix(H, cfg, c03):
    a,e,b,d,g,h,u1,u2,u3 = cfg
    C = [[1 for _ in range(4)] for _ in range(4)]
    C[1][1]=a; C[2][2]=e; C[1][2]=b; C[2][1]=d
    C[3][1]=g; C[3][2]=h
    C[1][0]=u1; C[2][0]=u2; C[3][0]=u3
    C[0][3]=c03
    return C


def response(C,t,s,d0,x,z):
    # D-C-sum z_i E_0i
    M=[[-C[i][j] + (d0 if i==0 else t if i==1 else s if i==2 else x) * (i==j)
        for j in range(4)] for i in range(4)]
    for i in range(1,4):
        M[0][i] -= z[i-1]
    return det4(M)


def evaluate(H, t, s, crosscheck=False):
    assert H>=2 and t>=H*H+1 and s>=H*H+1
    expected_min = t*s - (H-1)*(t+s)
    expected_max = H*(t+H-1)*(s+H-1)
    low, high = 10**100, -10**100
    low_count, high_count = 0, 0
    low_witness, high_witness = None, None
    tested = 0
    for cfg in itertools.product(range(1,H+1),repeat=9):
        q=gap(t,s,*cfg)
        tested+=1
        if q<low: low,low_witness,low_count=q,cfg,1
        elif q==low: low_count+=1
        if q>high: high,high_witness,high_count=q,cfg,1
        elif q==high: high_count+=1
    assert low==expected_min,(H,t,s,low,expected_min)
    assert high==expected_max,(H,t,s,high,expected_max)
    checks=0
    if crosscheck:
        # The exact constant response difference is independent of all free controls.
        samples = [tuple(1 if k%2==0 else H for k in range(9)),low_witness,high_witness]
        for cfg in samples:
            for d0,x,z in [(0,0,(0,0,0)),(7,-4,(3,-5,11)),(-23,89,(-1,-2,5))]:
                C=make_matrix(H,cfg,1)
                D=make_matrix(H,cfg,2)
                diff=response(D,t,s,d0,x,z)-response(C,t,s,d0,x,z)
                assert diff == -gap(t,s,*cfg),(H,t,s,cfg,diff)
                checks+=1
    return {
        "H": H, "t":t, "s":s, "scan_size":tested,
        "min_gap":low,"max_gap":high,
        "min_gap_formula":"t*s-(H-1)*(t+s)",
        "max_gap_formula":"H*(t+H-1)*(s+H-1)",
        "min_count":low_count,"max_count":high_count,
        "min_witness_order":"a,e,b,d,g,h,u1,u2,u3",
        "min_witness":list(low_witness),"max_witness":list(high_witness),
        "independent_full_determinant_crosschecks":checks,
    }


def main():
    cases=[(2,5,50),(2,5,5),(2,7,10),(3,10,13),(3,19,37),(4,17,35)]
    items=[evaluate(*case,crosscheck=True) for case in cases]
    out={
        "result":"R284BU",
        "scope":"finite exhaustive checks of the stated cases; universal claim depends on algebraic proof",
        "arithmetic":"Python integers, exact",
        "run_command":"python3 R284BU_root_free_leaf_gap_checker.py",
        "finite_scans":sum(q["scan_size"] for q in items),
        "independent_full_determinant_crosschecks":sum(q["independent_full_determinant_crosschecks"] for q in items),
        "cases":items,
    }
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
