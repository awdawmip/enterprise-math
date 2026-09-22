"""Finite independent integer checks of the proved real two-mode criterion."""
import hashlib
import itertools
import json
from pathlib import Path

from check_polarization import dot, raw_vortex


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def neg(a):
    return tuple(-x for x in a)


def check(k, l, a, b):
    n = cross(k, l)
    assert any(n) and dot(k, a) == dot(l, b) == 0
    alpha, beta = dot(a, l), dot(b, k)
    scalar = ((dot(k, k)-dot(l, l))*alpha*beta == 0
              and alpha*dot(b, n) == 0 and beta*dot(a, n) == 0)
    raw, branches = raw_vortex({k:a, neg(k):a, l:b, neg(l):b})
    actual = all(all(dot(m,m)*v[j]-m[j]*dot(m,v) == 0 for j in range(3))
                 for m,v in raw.items() if any(m))
    assert actual == scalar
    return scalar


def main():
    pairs = [((1,0,0),(0,1,0)), ((1,0,0),(0,2,0)),
             ((1,1,0),(0,1,1)), ((1,1,0),(1,0,0)),
             ((1,2,1),(2,-1,1))]
    probes = [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,-1,2),(-2,1,1)]
    rows=[]
    for k,l in pairs:
        stationary=0
        for p,q in itertools.product(probes, repeat=2):
            stationary += check(k,l,cross(k,p),cross(l,q))
        rows.append({"k":k,"l":l,"cases":36,"stationary":stationary})
    # Explicit four-parameter axis family, including every zero degeneration.
    axis=0
    for A,B,C,D in itertools.product((-1,0,1), repeat=4):
        got=check((1,0,0),(0,1,0),(0,A,B),(C,0,D))
        assert got == (B*C == 0 and A*D == 0)
        axis += 1
    here=Path(__file__).resolve().parent
    result={"status":"PASS_REAL_TWO_MODE_INTEGER_IDENTITIES", "general_cases":180,
            "axis_family_cases":axis,"rows":rows,
            "arithmetic":"Integer cross multiplication only; no quotient or root materialized",
            "scope":"Finite check supports the separate universal proof; both cross frequencies retained, no alias",
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "raw_formula_checker_sha256":hashlib.sha256(here.joinpath('check_polarization.py').read_bytes()).hexdigest()}
    here.joinpath('real_family_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
