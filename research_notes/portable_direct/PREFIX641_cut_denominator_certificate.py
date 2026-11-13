#!/usr/bin/env python3
"""Exact native BRC prefix-window cut denominator proof witness (PREFIX641)."""
import sys,hashlib,json
from pathlib import Path
from fractions import Fraction as Q
from math import prod
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from PREFIX641_native_rolling_pipeline import initial_integer,integer_port_step,integer_vec_apply,gates_for,ff,native,ZERO

def raw_moments(v,d,gg):
    M=None
    for g in gg:
        st=ff.fstep(g)
        M=st if M is None else ff.fprod(M,st)
    z={s*native.S:(x,0,0,0,0,0) for s,x in enumerate(v) if x}
    z=integer_vec_apply(z,M)
    total=ZERO
    for x in z.values():total=ff.add(total,x)
    return total,d*M.den

def check():
    rows=[]
    for kind in ('one','rational','zeros'):
        gates=gates_for(kind,20)
        for t in range(0,5):
            v,d=initial_integer();rt=native.embed()
            for g in gates[:t]:v,d=integer_port_step(v,d,g);rt=native.native_step(rt,g)
            for L in (1,2,4,8):
                num,den=raw_moments(v,d,gates[t:t+L])
                assert den==4*prod(g.denominator for g in gates[:t+L]),(kind,t,L,'denom')
                exact=tuple(Q(a,den) for a in num)
                assert exact==native.oracle(rt,gates[t:t+L]),(kind,t,L,'moments')
                rows.append(dict(kind=kind,t=t,L=L,denominator_bits=den.bit_length(),max_numerator_bits=max(x.bit_length() for x in num)))
    out={'schema':'PREFIX641_PREFIX_CUT_COMMON_DENOMINATOR_CERTIFICATE_V1','checks':len(rows),'gate_families':['one','rational','zeros'],'domain':'native 96-port positive-branch labelled BRC, two motif six-jets, original 576 actions','checks_detail':rows,'status':'ALL_ASSERTIONS_PASS','role':'AUTHOR_UNREVIEWED'}
    p=HERE/'PREFIX641_cut_denominator_results.json';p.write_text(json.dumps(out,indent=2)+'\n')
    print('ALL_ASSERTIONS_PASS',len(rows),'prefix/window cut denominator and six-jet exact tuple checks')
    print('JSON_SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':check()
