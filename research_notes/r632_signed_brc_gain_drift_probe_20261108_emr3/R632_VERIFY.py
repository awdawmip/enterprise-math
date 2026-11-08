#!/usr/bin/env python3
"""R632 frozen signed BRC: exact modular two-probe with axis-wise gain drift.
Inputs: R462 original K generator, theta=0; no native heartbeat evolution assumed.
Only Python integers and integer polynomials; no network, floating, or third-party packages.
"""
import json
import itertools
from math import comb
from pathlib import Path

def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def add(a, b):
    z = [0] * max(len(a), len(b))
    for j, v in enumerate(a): z[j] += v
    for j, v in enumerate(b): z[j] += v
    return z

def mul(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i+j] += x*y
    return z

def K(i):
    ds = (-C(4, i) + C(2, i-1), C(5, i-1)-C(5, i-2), C(7, i-2), -C(9, i-3))
    z = [0]
    for j, v in enumerate(ds, 1):
        n = i+1-j
        if n >= 0 and v:
            z = add(z, [0]*(i-1) + [-v*C(n, q) for q in range(n+1)])
    return z

def nu(a, p):
    return next((i for i, v in enumerate(a) if v % p), None)

def ppow_over(h, p):
    L=1
    while L <= h: L *= p
    return L

def H_at(B, k):
    z=[0]
    for l, row in enumerate(B):
        z=add(z, [C(k,l)*v for v in row])
    return z

def jet(a, d):
    return a[:d+1] + [0]*max(0,d+1-len(a))

def make_gain(a, x, j, is_second):
    # Nonzero gains, independent across native axes and between probes;
    # the second gain valuation can increase by 0, 1, or 3.
    delta = ((x+2*j) % 3) if is_second else 0
    if delta == 2: delta = 3
    lead = 1 + ((x+j+int(is_second)) % 3)
    return [0]*(a+delta) + [lead, x+1 if is_second else -j-1, 2+j]

def evaluate():
    k=[K(i) for i in range(1,13)]
    P=k[0::2]
    M=k[1::2]
    pval=[nu(v, 0x7fffffff) for v in P]
    mval=[next(i for i,v in enumerate(row) if v) for row in M]
    p_lead=[next(v for v in row if v) for row in P]
    m_lead=[next(v for v in row if v) for row in M]
    assert pval == [0,2,4,6,8,10], pval
    assert mval == [1,3,5,7,9,11], mval
    assert p_lead == [2,-8,6,106,83,9], p_lead
    assert m_lead == [-1,-11,53,119,36,1], m_lead
    perms=list(itertools.permutations(range(6)))
    assert len(perms)==720
    counts={'frozen_lead_checks':24, 'lucas_two_timestamp_pairs':0, 'axis_gains_and_nuisance_cases':0,
            'six_axis_orientations':0, 'sharpness_witnesses':0}
    prime_drift=[5,7,11,13]
    for p in prime_drift:
        assert len({nu(P[j],p) for j in range(6)})==6
        for h in (0,1,3,4,9,24):
            L=ppow_over(h,p)
            k0=2*((h+p)//3)
            k1=k0+L
            assert L%2==1
            for a in (0,2):
                d=a+8
                labels={}
                for x in range(6):
                    for j in range(6):
                        gain0=make_gain(a,x,j,False)
                        gain1=make_gain(a,x,j,True)
                        assert nu(gain0,p)==a
                        ig=nu(gain1,p)
                        assert ig is None or ig>=a
                        B=[[2+x+j+l, x-2*l, j+l+1] for l in range(h+1)]
                        y0=add(mul(gain0,P[j]), H_at(B,k0))
                        y1=add(mul(gain1,M[j]), H_at(B,k1))
                        diff=jet(add(y1,[-z for z in y0]),d)
                        idx=nu(diff,p)
                        actual=5 if idx is None else idx-a
                        expected=5 if j==5 else 2*j
                        assert actual==expected,(p,h,a,x,j,idx,expected)
                        labels[x,j]=actual
                        counts['axis_gains_and_nuisance_cases']+=1
                for perm in perms:
                    predicted=[5 if labels[x,perm[x]]==5 else labels[x,perm[x]]//2 for x in range(6)]
                    assert predicted==list(perm)
                    counts['six_axis_orientations']+=1
    for p in (3,5,7,11):
        for h in range(0,20):
            L=ppow_over(h,p)
            rows=[tuple(C(k,l)%p for l in range(h+1)) for k in range(84)]
            for u in range(84):
                for v in range(u+1,84):
                    assert (rows[u]==rows[v])==((v-u)%L==0),(p,h,u,v,L)
                    counts['lucas_two_timestamp_pairs']+=1
    for a in (1,2,4):
        d=a+8
        g0_5=[0]*a+[36]; g1_5=[0]*(a-1)+[83]
        g0_6=[0]*a+[1];g1_6=[0]*(a-1)+[1]
        for j,g0,g1 in ((4,g0_5,g1_5),(5,g0_6,g1_6)):
            constant=[-v for v in mul(g0,P[j])]
            y0=add(mul(g0,P[j]),constant)
            y1=add(mul(g1,M[j]),constant)
            assert jet(y0,d)==[0]*(d+1)
            assert jet(y1,d)==[0]*(d+1),(j,jet(y1,d))
            assert g0[a]%5 != 0
            counts['sharpness_witnesses']+=1
    total=sum(counts.values())
    return {
        'schema':'EM_R632_GAIN_DRIFT_AND_ARBITRARY_INDEX_SPARSE_PROBE_V1',
        'date':'2026-11-08',
        'science_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
        'frozen_K_generator_git_blob':'7fa7a762f758b30c6090468ac43487daa34abad8',
        'R631_parent':'3ac5cbaedeac11a28fa4e5bfe12dd59b53a35f1e',
        'P_leading_degrees':pval,'M_leading_degrees':mval,
        'P_first_nonzero_coefficients':p_lead,'M_first_nonzero_coefficients':m_lead,
        'safe_primes_tested':prime_drift,
        'lucas_primes_tested':[3,5,7,11],
        'lucas_h_range':[0,19],
        'two_timestamp_integer_domain':[0,83],
        'gain_conditions':'A_plus has known t-order a and p-unit lead; A_minus is any nonzero integer series of t-order >= a',
        'sampling':'k0 even arbitrary; k1=k0+p^s where p^s least > h; odd p>=5 with p!=53,83',
        'precision':'d=a+8 optimal uniform guarantee within the declared two-probe model',
        'counts':counts, 'total_exact_checks':total,
        'status':'AUTHOR_SIDE_EXACT_UNREVIEWED',
        'marker':'R632_GAIN_DRIFT_AND_LUCAS_PERIOD_EXACT_PASS'
    }

if __name__=='__main__':
    e=evaluate()
    target=Path(__file__).with_name('R632_EVIDENCE.json')
    target.write_text(json.dumps(e,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps({'marker':e['marker'],'total_exact_checks':e['total_exact_checks'],'counts':e['counts'],'evidence_file':target.name},sort_keys=True))
