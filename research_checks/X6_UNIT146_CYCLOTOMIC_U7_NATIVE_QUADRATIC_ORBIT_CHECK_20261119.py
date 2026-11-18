#!/usr/bin/env python3
"""Unit146: exact original-U seven-phase/native-X6 metric and path/BRC audit.

Source transcription: experiments/x6_cyclotomic_compatibility_20260910/verify.py
Git blob 0d4ea1d29281236c80ae8502de7d75a5d76c39e9.
This checks the literal integer U operator, not that original SymPy program.
"""
from collections import Counter
from itertools import product
from math import factorial, prod
import json


def ensure(condition, message):
    if not condition:
        raise ValueError(message)


def U(z):
    ensure(len(z) == 6 and all(type(x) is int for x in z), "six native integer coordinates required")
    b = z[5]
    return (-b, z[0]-b, z[1]-b, z[2]-b, z[3]-b, z[4]-b)


def Q(z):
    return sum(x*x for x in z)


def H(z):
    return 7*Q(z) - sum(z)**2


def T(z):
    return sum(abs(x) for x in z)


def M(z):
    return factorial(T(z))//prod(factorial(abs(x)) for x in z)


def cycle(z):
    a=[z]
    for _ in range(7): a.append(U(a[-1]))
    ensure(a[-1]==z, "seven-cycle fails")
    return a[:-1]


def certificate():
    zero=(0,)*6
    e0=(1,0,0,0,0,0)
    e5=(0,0,0,0,0,1)
    orbit0=cycle(e0)
    ensure([Q(w) for w in orbit0]==[1,1,1,1,1,1,6], "basis orbit norm vector")
    ensure([T(w) for w in orbit0]==[1,1,1,1,1,1,6], "basis orbit primitive length vector")
    ensure([M(w) for w in orbit0]==[1,1,1,1,1,1,720], "basis orbit N-BRC vector")
    ensure(U(e5)==(-1,)*6, "last basis vector image")
    count=0; all_constant=0; one_step_equal=0; one_step_nonzero_equal=0
    one_step_nonzero_later_different=0
    
    for z in product(range(-2,3),repeat=6):
        z=tuple(z)
        p=cycle(z)
        q=[Q(w) for w in p]
        hz=H(z)
        ensure(all(H(w)==hz for w in p), "derived H fails to be invariant")
        ensure(sum(q)==2*hz, "seven-phase native Q orbit sum fails")
        ensure(q[1]-q[0]==z[5]*(5*z[5]-2*sum(z[:5])), "one-step defect formula")
        if len(set(q))==1:
            all_constant+=1
            ensure(z==zero, "nonzero equal-native-norm orbit, obstruction false")
        if q[1]==q[0]:
            one_step_equal+=1
            if z!=zero:
                one_step_nonzero_equal+=1
                if len(set(q))>1:one_step_nonzero_later_different+=1
        count+=1
    ensure(all_constant==1, "global rigidity count mismatch")
    ensure(one_step_nonzero_equal==one_step_nonzero_later_different,"one-step preservation has no full seven-phase exception")
    return {
        "schema":"X6_UNIT146_CYCLOTOMIC_U7_NATIVE_Q_ORBIT_CERT_V1",
        "task_id":"RS-X6-LEGACY-PLANE-RECONCILIATION",
        "scientific_pin":"59538f585d037d09ef687b28715c4bc1a3f9fe03",
        "historical_pin":"fd2bcff10ca6e147348b6c1236027fc0d2877df3",
        "consumer_path":"experiments/x6_cyclotomic_compatibility_20260910/verify.py",
        "consumer_blob":"0d4ea1d29281236c80ae8502de7d75a5d76c39e9",
        "coverage":{"box":"[-2,2]^6","vectors":count,"U_iterations_per_vector":7,"integer_exact":True,"source_program_executed":False},
        "findings":{"constant_native_norm_orbits":all_constant,
                    "single_step_norm_equal":one_step_equal,
                    "nonzero_single_step_norm_equal":one_step_nonzero_equal,
                    "nonzero_single_step_equal_but_later_differs":one_step_nonzero_later_different,
                    "basis_e0_Q_orbit":[Q(w) for w in orbit0],
                    "basis_e0_T_orbit":[T(w) for w in orbit0],
                    "basis_e0_shortest_positive_N_BRC_orbit":[M(w) for w in orbit0],
                    "basis_e5_U_image":list(U(e5))},
        "proved_identites":["U^7=I", "sum_{r=0}^{6} Q(U^r z)=2(7Q(z)-(sum z)^2)", "all_r Q(U^r z)=Q(z) iff z=0", "Q(Uz)-Q(z)=z5(5 z5-2sum_{i<5} z_i)", "H(Uz)=H(z)"],
        "status":"AUTHOR_PROVED_EXACT_INTEGER_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED"
    }

if __name__=='__main__':
    x=certificate()
    s=json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False)
    print(s)
