#!/usr/bin/env python3
"""Independent exact finite resonance audit; no old W21/W23 binaries used."""
import json
K=21; TARG=23
J=18; MOD=1<<(J+1)
Q_LO=262145; Q_HI=524287
terms=[(i,j,s,(1<<i)-s*(1<<j)) for i in range(J+1) for j in range(J+1) for s in (-1,1)]
compatible=[(u,v) for u in terms for v in terms if K*v[3]==TARG*u[3]]
assert len(compatible)==361
assert all(u[3]==v[3]==0 and u[0]==u[1] and u[2]==1 and v[0]==v[1] and v[2]==1 for u,v in compatible)
# There are precisely two positive resonant quotient pairs in bounds.
resonant=[(t,t+m) for t in range(1,43) for m in range(7) if t+m<=46 and 2*t==K*m]
assert resonant==[(21,23),(42,46)]
exceptions={str(k):(-pow(k,-1,MOD)) % MOD for k in (K,TARG)}
assert exceptions=={'21':274627,'23':182361}
Q=range(Q_LO,Q_HI+1,2)
resonant_diag=[a for a in Q if (K*a)%MOD!=MOD-1 and (TARG*a)%MOD!=MOD-1]
assert len(resonant_diag)==131071
print(json.dumps({"compatible_index_sign_pairs":len(compatible),"nonzero_compatible_c":0,"resonant_quotient_pairs":resonant,"all_ones_unique_a_mod_2pow19":exceptions,"resonant_diagonal_count":len(resonant_diag),"excluded_diagonal_modulus":274627,"status":"ALL_EXACT_ASSERTIONS_PASSED"},sort_keys=True))
