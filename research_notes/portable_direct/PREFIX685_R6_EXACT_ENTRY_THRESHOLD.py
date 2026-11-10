#!/usr/bin/env python3
"""PREFIX685-R6: exact local entry threshold from frozen 189-level BRC observer.
Reuses original PREFIX680 module unmodified; all decisive tests use integers/Fraction.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from fractions import Fraction as Q
from math import comb
import json
from PREFIX680_R6_EXACT_THIRD_ORDER_CROSSOVER_CERTIFICATE import N, frozen_rows, dot

SCIENCE_PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"
L = Q(2663, 50000)

def survivor_at(rows, p):
    a,d=p.numerator,p.denominator
    ap=[a**i for i in range(N+1)]
    cp=[(d-a)**i for i in range(N+1)]
    dp=[d**i for i in range(N+1)]
    return [Q(sum(v*ap[k]*cp[n-k] for k,v in row.items()),dp[n])
            for n,row in enumerate(rows)]

def proof():
    rows=frozen_rows()
    S=survivor_at(rows,L)
    S0=[Q(row.get(0,0)) for row in rows]
    K=[[Q(comb(n+j,n),2**(n+j+1)) for j in range(N)] for n in range(N)]
    J=[[Q(n+j+1,2)*K[n][j] for j in range(N)] for n in range(N)]
    mu_diag=2*sum(S)-dot(S,S,K)
    mu_edge=sum(S0)+sum(S)-dot(S0,S,K)
    h_diag=2*sum((n+1)*S[n] for n in range(N))-dot(S,S,J)
    h_edge=sum((n+1)*(S0[n]+S[n]) for n in range(N))-dot(S0,S,J)
    B=mu_diag-mu_edge
    A=2*(h_diag-h_edge)-mu_diag**2+mu_edge**2
    assert A>0 and B>0
    qc=B/A
    assert Q(9816)<qc<Q(9929) and Q(9872)<qc<Q(9873)

    scale=10**12
    tick=(qc*scale).__floor__()
    assert Q(tick,scale)<qc<Q(tick+1,scale)
    assert tick==9872453419496357

    prec=10**24
    a_tick=(A*prec).__floor__()
    b_tick=(B*prec).__floor__()
    assert a_tick==803334881118283114227
    assert b_tick==7930886194096894324395803
    # Standalone small integer witness for the ratio enclosure.
    assert b_tick*scale>tick*(a_tick+1)
    assert (b_tick+1)*scale<(tick+1)*a_tick

    return {
        "result":"ALL_CHECKS_PASS PREFIX685-R6",
        "scientific_pin":SCIENCE_PIN,
        "source_kernel":"PREFIX680_R6_EXACT_THIRD_ORDER_CROSSOVER_CERTIFICATE.py",
        "kernel_source_commit":"2c91711f60aa74d93880780929f532da24140ec0",
        "prior_local_threshold_source_commit":"758f58df1f3c25377e5400747c3e19da15bea750",
        "evaluation_z":str(L),
        "survivor_levels":N,
        "survivor_nonzero_cells":sum(map(len,rows)),
        "A_positive":True,"B_positive":True,
        "A_24digit_enclosure":[f"{a_tick}/{prec}",f"{a_tick+1}/{prec}"],
        "B_24digit_enclosure":[f"{b_tick}/{prec}",f"{b_tick+1}/{prec}"],
        "smallest_integer_q_with_crossing_in_I":9873,
        "A_numerator_bits":A.numerator.bit_length(),
        "A_denominator_bits":A.denominator.bit_length(),
        "B_numerator_bits":B.numerator.bit_length(),
        "B_denominator_bits":B.denominator.bit_length(),
        "q_c_exact":"B(L)/A(L), computed from exact frozen 189-level recurrence",
        "q_c_12digit_floor":tick,
        "q_c_strict_bracket":[f"{tick}/{scale}",f"{tick+1}/{scale}"],
        "q_c_decimal_enclosure":[f"{tick//scale}.{tick%scale:012d}",f"{(tick+1)//scale}.{(tick+1)%scale:012d}"],
        "q_c_numerator_bits":qc.numerator.bit_length(),
        "q_c_denominator_bits":qc.denominator.bit_length(),
        "interpretation":"unique crossing in I iff q>=q_c for real q>=0, reusing PREFIX684 derivative proof",
        "prior_189_kernel_rerun":True,
        "arithmetic":"exact Python integer/Fraction and strict integer cross-products",
        "status":"AUTHOR_DERIVED / EXACT_INTEGER_FRACTION_RECOMPUTED / UNREVIEWED / NOT_ADMITTED"
    }

if __name__=="__main__":
    print(json.dumps(proof(),ensure_ascii=False,indent=2))
