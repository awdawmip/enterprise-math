#!/usr/bin/env python3
"""R762EX: exact full-three-coordinate q9 second-trit period certificate.
Only Python standard library and exact integer group-ring convolution.
"""
import hashlib
import json

Q = 9
BRANCHES = ((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
START, WINDOW, PERIOD = 9, 127, 54
LAST = START + WINDOW - 1 + PERIOD  # 189
MOD = 3 ** (LAST // 3)  # 3^63

def ix(x,y,z):
    return (x * Q + y) * Q + z

SHIFT = [tuple(ix((x-dx)%Q,(y-dy)%Q,(z-dz)%Q)
               for x in range(Q) for y in range(Q) for z in range(Q))
         for dx,dy,dz in BRANCHES]

def f(n):
    return max(0, n//3-2)

def shadow(vector, n):
    unit = 3**f(n)
    assert all(c % unit == 0 for c in vector), ('content_lower_bound',n)
    return bytes((c//unit)%9 for c in vector)

def compute():
    v = [0]*(Q**3)
    v[0] = 1
    s = {}
    mass_checks = 0
    for n in range(LAST+1):
        assert sum(v)%MOD == pow(6,n,MOD), ('mass',n)
        mass_checks += 1
        if n >= 8:
            s[n] = shadow(v,n)
        if n < LAST:
            v = [sum(v[p[i]] for p in SHIFT)%MOD for i in range(Q**3)]
    assert len(s[9]) == Q**3
    for n in range(START,START+WINDOW):
        assert s[n] == s[n+PERIOD], ('period',n)
    assert s[8][1] == 8 and s[62][1] == 5 and s[8]!=s[62]
    assert s[9][1] == 6 and s[27][1] == 0 and s[9]!=s[27]
    union_hash = hashlib.sha256(b''.join(s[n] for n in range(START, START+WINDOW))).hexdigest()
    pair_hash = hashlib.sha256(b''.join(s[n]+s[n+PERIOD] for n in range(START,START+WINDOW))).hexdigest()
    return {
      'schema':'R762EX_EXACT_INTEGER_CERT_V1',
      'model':'positive named six-branch P_9 in Z[(Z/9Z)^3], all coordinates retained',
      'q':Q, 'period':PERIOD, 'candidate_exact_preperiod':START,
      'recurrence_order_from_R762EM':WINDOW,
      'initial_window_first':START, 'initial_window_last':START+WINDOW-1,
      'last_power':LAST, 'fixed_modulus':'3^63',
      'full_terminal_positions':Q**3,
      'period_vector_equalities':WINDOW,
      'period_coefficient_equalities':WINDOW*(Q**3),
      'mass_invariant_checks':mass_checks,
      'normalization_integrality_checks':len(s)*(Q**3),
      'coordinate_order':'index=(x*9+y)*9+z, so index 1=(0,0,1)',
      'witness_not_period_18': {'n':9,'compare_n':27,'index':1,'first_residue_mod9':s[9][1],'second_residue_mod9':s[27][1]},
      'witness_preperiod_8_fails':{'n':8,'compare_n':62,'index':1,'first_residue_mod9':s[8][1],'second_residue_mod9':s[62][1]},
      'initial_window_concat_sha256':union_hash,
      'initial_window_pairs_concat_sha256':pair_hash,
      'scope':'finite exact certificate; universal extension uses 127-degree monic annihilator and coefficient 3-adic bounds from R762EM/R762EO',
      'independence':'author-side calculation; prior spectral inputs NOT_REVIEWED',
      'status':'PASS'
    }

if __name__=='__main__':
    print(json.dumps(compute(),indent=2,ensure_ascii=False,sort_keys=True))
