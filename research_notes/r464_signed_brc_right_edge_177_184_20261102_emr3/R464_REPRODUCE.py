#!/usr/bin/env python3
"""Exact R464 signed BRC certificates via the immutable R463 proof kernel.

Run in an Enterprise Math checkout containing the sibling R463_VERIFY.py.
Kronecker substitution changes computation cost, not the Z[u] polynomial.
Use s=175 as a pinned SHA256 regression; then certify 177..184.
"""
import sys, json, importlib.util
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PREV = BASE/'r463_signed_brc_right_edge_175_176_20261101_emr3'/'R463_VERIFY.py'
if not PREV.exists():
    # Existing local evidence package (not the default publication path).
    PREV = Path(__file__).resolve().parent/'_R462_VERIFY.py'
assert PREV.exists(), f'Missing previous exact proof kernel: {PREV}'
spec = importlib.util.spec_from_file_location('signed_brc_r463', PREV)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)

OLD_MUL = core.mul

def mul(a,b):
    """Exact fast multiplication of Z[u] polynomials.
    Unsigned Kronecker for nonnegative coefficients; original exact
    schoolbook multiplication for any signed input.
    """
    if min(a)<0 or min(b)<0 or len(a)*len(b)<1600:
        return OLD_MUL(a,b)
    width = sum(a).bit_length() + sum(b).bit_length() + 1
    mask = (1 << width) - 1
    def encode(p):
        n=0
        for coeff in reversed(p):n=(n<<width)+coeff
        return n
    n = encode(a)*encode(b)
    out = []
    for _ in range(len(a)+len(b)-1):
        out.append(n & mask)
        n >>= width
    assert n==0
    return out

core.mul=mul

def main():
    lo=int(sys.argv[1]) if len(sys.argv)>1 else 177
    hi=int(sys.argv[2]) if len(sys.argv)>2 else 184
    regression=core.s_certificate(175,detail=True)
    assert regression['sha256']=='5a68b3d2ced114ee7744e5a75b8553717314a3d0ea1b5b497b0739ba09847239'
    print('R464_FROZEN_R463_REGRESSION_PASS',regression['sha256'],flush=True)
    rows=[]
    for s in range(lo,hi+1):
        row=core.s_certificate(s,detail=True)
        rows.append(row)
        print('R464_CERTIFICATE',json.dumps(row,sort_keys=True),flush=True)
    result={'result':'R464_REPRODUCE_PASS',
            'regression':'s175 R463 original coefficient-stream SHA256 matched',
            's_range':[lo,hi],
            'positive_coefficients':sum(row['strict_positive_coefficients'] for row in rows),
            'exact_poly_condensation_checks':len(rows),
            'original_signed_checks':10*len(rows),
            'catalan_checks':10*len(rows),'rows':rows}
    outfile=Path(f'R464_REPRODUCE_{lo}_{hi}.json')
    outfile.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print('R464_REPRODUCE_PASS',json.dumps({k:v for k,v in result.items() if k!='rows'},sort_keys=True),flush=True)
if __name__=='__main__': main()
