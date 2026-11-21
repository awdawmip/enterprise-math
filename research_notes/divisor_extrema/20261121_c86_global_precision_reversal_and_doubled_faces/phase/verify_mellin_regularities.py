#!/usr/bin/env python3
"""Exact independent coverage/continuity audit of the C86 Mellin chambers.

All pass/fail decisions use integers or Fraction. The optional decimal displays
do not enter the checks. This does not rerun the parent cubature computation.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'smallarea' / 'mellin_chambers.json'
sys.path.insert(0, str(HERE))
from exact_phase_moment import root_bounds

P = F(41, 20)


def canonical(v):
    for x in v:
        if x:
            sign = 1 if x > 0 else -1
            return tuple(sign*y for y in v), sign
    return tuple(v), 1


def boundary_ledger(rows, q, axis):
    """Value and two derivative expressions on a fixed-r or fixed-s edge.

    Keys are the affine argument of |u|^p or sign(u)|u|^(p-1).
    Derivative coefficients are affine polynomials in the free coordinate.
    """
    value = defaultdict(F)
    normal = defaultdict(lambda: [F(0), F(0)])
    tangent = defaultdict(lambda: [F(0), F(0)])
    for a, b, c, w in rows:
        if axis == 's':
            a, b = b, a
        u, sign = canonical((a*q, b+c*q))
        if not any(u):
            continue
        value[u] += w
        normal[u][0] += w*sign*a
        normal[u][1] += w*sign*c
        tangent[u][0] += w*sign*(b+c*q)
    clean = lambda d: {k: tuple(v) for k, v in d.items() if any(v)}
    return ({k: v for k, v in value.items() if v}, clean(normal), clean(tangent))


def spline_coverage(poly, pieces, cuts):
    """Verify the affine spline on complete trapezoids, not sample points.

    Every claim on a trapezoid is affine, so its four rational vertices suffice.
    """
    differences = [(x[0]-y[0], x[1]-y[1]) for x in poly for y in poly]
    tbreaks = {-F(dx, dy) for dx, dy in differences if dy}
    minwidth = min(max(dx+dy*t for dx, dy in differences) for t in tbreaks)
    checked = 0
    for lo, hi, piece in zip(cuts, cuts[1:], pieces):
        knots = [(F(t['intercept']), F(t['slope']), F(t['jump'])) for t in piece]
        if not knots:
            assert minwidth*lo >= 1
            checked += 1
            continue
        assert sum(j for a, b, j in knots) == 0
        assert sum(a*j for a, b, j in knots) == 0
        assert sum(b*j for a, b, j in knots) == 0
        rm = (lo+hi)/2
        assert all(a+b*rm < c+d*rm for (a,b,j),(c,d,k) in zip(knots,knots[1:]))
        const = slope_r = slope_z = F(0)
        for (a,b,j),(aa,bb,jj) in zip(knots, knots[1:]):
            const -= j*a
            slope_r -= j*b
            slope_z += j
            zm = (a+aa+(b+bb)*rm)/2
            dx,dy = max(differences, key=lambda d: d[0]*rm+d[1]*zm)
            assert (const,slope_r,slope_z) == (F(1),F(-dx),F(-dy))
            for r in (lo,hi):
                for z in (a+b*r,aa+bb*r):
                    assert a+b*r <= aa+bb*r
                    assert const+slope_r*r+slope_z*z >= 0
                    assert all(dx*r+dy*z >= ex*r+ey*z for ex,ey in differences)
            checked += 1
        # The extreme support rays also have h=0. An ordered point difference
        # with outward sign certifies W>=1 throughout each unbounded ray.
        for edge, direction in ((knots[0],-1),(knots[-1],1)):
            a,b,j = edge
            possible = [(dx,dy) for dx,dy in differences if dy*direction > 0
                        and all(dx*r+dy*(a+b*r) >= 1 for r in (lo,hi))]
            assert possible
            checked += 1
    return checked


def chamber_terms_from_splines(data):
    """Regenerate all merged power terms from the verified spline atoms."""
    out = {}
    for row in data['chambers']:
        ri,si = row['r_index'],row['s_index']
        merged = defaultdict(F)
        for poly in data['scaled_splines']:
            coefficient = F(poly['coefficient'])
            for u in poly['pieces'][ri]:
                ai,bi,di = map(F,(u['intercept'],u['slope'],u['jump']))
                for v in poly['pieces'][si]:
                    aj,bj,dj = map(F,(v['intercept'],v['slope'],v['jump']))
                    arg,_ = canonical((-aj,ai,bi-bj))
                    merged[arg] += coefficient*di*dj
        merged = {k:v for k,v in merged.items() if v and any(k)}
        supplied = {tuple(F(t[k]) for k in ('a_r','b_s','c_rs')):F(t['weight'])
                    for t in row['terms']}
        assert merged == supplied
        out[ri,si] = [(*k,v) for k,v in merged.items()]
    return out


def derivative_bounds(rows, ra, rb, xa, xb):
    first_r = first_x = second_r = second_x = mixed = F(0)
    for a,b,c,w in rows:
        m = max(abs(a+b*x+c*r*x) for r in (ra,rb) for x in (xa,xb))
        q = max(F(1),m)
        dr = abs(c)*xb
        dx = max(abs(b+c*ra),abs(b+c*rb))
        first_r += P*abs(w)*m*q*dr
        first_x += P*abs(w)*m*q*dx
        second_r += P*(P-1)*abs(w)*q*dr**2
        second_x += P*(P-1)*abs(w)*q*dx**2
        mixed += abs(w)*(P*(P-1)*q*dr*dx + P*m*q*abs(c))
    return first_r,first_x,second_r,second_x,mixed


def normal_jump_interval(left, right, r, s):
    lo = hi = F(0)
    for sign,rows in ((1,left),(-1,right)):
        for a,b,c,w in rows:
            u = a*r+b*s+c*r*s
            coefficient = sign*P*w*(a+c*s)*u
            l,h = root_bounds(abs(u),power=20,bits=100)
            if coefficient >= 0:
                lo += coefficient*l
                hi += coefficient*h
            else:
                lo += coefficient*h
                hi += coefficient*l
    return lo,hi


def main():
    data = json.loads(SOURCE.read_text())
    cuts = list(map(F,data['cuts']))
    assert cuts == [F(0),F(1,3),F(1,2),F(2,3),F(1)]
    assert F(data['exponent']) == P
    assert len(data['scaled_splines']) == 15
    assert all(len(row['pieces']) == 4 for row in data['scaled_splines'])
    assert len(data['chambers']) == 10
    assert {(row['r_index'],row['s_index']) for row in data['chambers']} == {
        (ri,si) for ri in range(4) for si in range(ri+1)}
    polyhedral_checks = sum(spline_coverage(row['polygon'],row['pieces'],cuts)
                            for row in data['scaled_splines'])
    terms = chamber_terms_from_splines(data)
    edges = []
    for j,q in enumerate(cuts[1:-1],1):
        for axis, indices in (('r',range(j)),('s',range(j,4))):
            for other in indices:
                left = terms[j-1,other] if axis == 'r' else terms[other,j-1]
                right = terms[j,other] if axis == 'r' else terms[other,j]
                l = boundary_ledger(left,q,axis)
                h = boundary_ledger(right,q,axis)
                assert l[0] == h[0]
                assert l[2] == h[2]
                edges.append({'axis':axis,'fixed_coordinate':str(q),'other_index':other,
                              'value_matches':True,'tangential_derivative_matches':True,
                              'normal_derivative_ledger_matches':l[1] == h[1]})
    jump = normal_jump_interval(terms[1,0],terms[2,0],F(1,2),F(1,4))
    assert jump[0] > 0
    bounds = []
    for (ri,si), rows in sorted(terms.items()):
        vals = derivative_bounds(rows,cuts[ri],cuts[ri+1],F(1,3),F(1))
        bounds.append({'r_index':ri,'s_index':si,
                       'bounds':dict(zip(('Hr','Hx','Hrr','Hxx','Hrx'),map(str,vals))),
                       'decimal_display':list(map(float,vals))})
    certificate = HERE.parent / 'mellin_integral_certificate.json'
    cert_summary = None
    if certificate.exists():
        c = json.loads(certificate.read_text())
        assert c['chamber_source_sha256'] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
        assert c['grid'][0] % 6 == 0
        assert c['interior_cells']+c['boundary_cells'] == c['grid'][0]*c['grid'][1]
        assert int(c['weighted_integral']['lower_numerator']) > 0
        assert int(c['moment_difference']['upper_numerator']) < 0
        cert_summary = {'sha256':hashlib.sha256(certificate.read_bytes()).hexdigest(),
                        'matching_chamber_source':True,'strict_negative_endpoint':True,
                        'scope':'Endpoint/source consistency check; cubature independently reviewed, not rerun here.'}
    out = {'schema':'C86_MELLIN_REGULARITY_AUDIT_V1',
            'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'scaled_spline_pieces':sum(len(row['pieces']) for row in data['scaled_splines']),
            'polyhedral_checks':polyhedral_checks,
            'regenerated_chambers':len(terms),'edge_checks':edges,
            'strict_non_C1_witness':{'r':'1/2','s':'1/4',
                'quantity':'left S_r minus right S_r',
                'interval':list(map(str,jump)),'decimal_display':list(map(float,jump))},
            'chamber_derivative_bounds':bounds,'certificate':cert_summary}
    target = HERE / 'mellin_regularity_audit.json'
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','polyhedral_checks':polyhedral_checks,
                      'chambers':len(terms),'shared_edges':len(edges),
                      'non_C1_jump_decimal':list(map(float,jump)),
                      'certificate_endpoint_check':cert_summary is not None},indent=2))


if __name__ == '__main__':
    main()
