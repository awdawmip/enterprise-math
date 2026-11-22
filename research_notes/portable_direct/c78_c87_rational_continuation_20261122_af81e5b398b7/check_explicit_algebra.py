"""Build and check actual C78 determinant polynomials and radical norms."""
from pathlib import Path
import json
from explicit_algebra import *


def main():
    c = circuit()
    reduced = {}
    cert = {'source_spectrum': 'C77 G_1/L0, signed; r^4=x,s^4=y',
            'source_commit': '07764cb22422a2710c8a329a0c67ba60013312d4',
            'arithmetic': 'Python arbitrary-precision integers and fractions.Fraction',
            'determinants': {}, 'norm_checks': {}}
    for name in ['Delta', 'Hessian']:
        quotient = exact_division(c[name], c['Q'])
        assert quotient is not None
        content, p = primitive_part(quotient)
        assert mul(scale(p, content), c['Q']) == c[name]
        reduced[name] = p
        degree, low = lowest_homogeneous_part(p)
        b, bounds, constant = characteristic_bound(p)
        cert['determinants'][name] = {
            'integer_content': content, 'removed_denominator_factor': 'Q',
            'polynomial_terms': polynomial_rows(p), 'term_count': len(p),
            'lowest_total_degree': degree, 'lowest_homogeneous_terms': polynomial_rows(low),
            'norm_leading_certificate': norm_leading_certificate(p),
            'coefficient_l1_bound_B': b,
            'characteristic_coefficient_bound_ascending': bounds,
            'positive_power_coefficient_sum_bound': constant}
    assert lowest_homogeneous_part(reduced['Delta']) == (127, {
        (44,83):35, (35,92):-310, (26,101):680})
    assert lowest_homogeneous_part(reduced['Hessian']) == (112, {
        (29,83):-3710, (20,92):-3233, (11,101):-28832})

    r, s = Q(1,2), Q(1,4)
    x, y = r**4, s**4
    q = evaluate(c['Q'], r, s)
    det_j = evaluate(c['Delta'],r,s)/(64*r**3*s**3*q**5)
    det_h = evaluate(c['Hessian'],r,s)/(256*r**7*s**7*q**6)
    assert det_j > 0 and det_h < 0
    cert['point'] = {'r': str(r), 's': str(s), 'x': str(x), 'y': str(y),
                     'R': fractions_pack(evaluate(c['N'],r,s)/q),
                     'Jacobian_determinant': fractions_pack(det_j),
                     'Hessian_determinant': fractions_pack(det_h)}

    for name, p in reduced.items():
        matrix = norm_matrix_at(p,x,y)
        d = determinant(matrix)
        assert d != 0
        coeffs = characteristic_coefficients(matrix)
        assert coeffs[-1] == d
        value = evaluate(p,r,s)
        v = Q(0)
        for coefficient in coeffs:
            v = v*value + coefficient
        assert v == 0
        b, bounds, constant = characteristic_bound(p)
        assert all(abs(coeffs[16-j]) <= bounds[j] for j in range(17))
        assert abs(d) <= abs(value)*constant  # this point also has |P| <= 1
        assert abs(value) <= 1
        cert['norm_checks'][name] = {
            'specialized_norm': fractions_pack(d),
            'specialized_charpoly_annihilates_P': True,
            'all_characteristic_coefficient_bounds_passed': True,
            'constant_coefficient_matches_independent_determinant': True,
            'norm_small_value_bound_passed': True}

    # Independent small generator norm identities, including non-monomial entries.
    examples = [({(1,0):1}, x**4), ({(0,1):1}, y**4),
                ({(0,0):1,(1,0):1}, (1-x)**4),
                ({(1,0):1,(0,1):1}, (x-y)**4)]
    for p, expected in examples:
        assert determinant(norm_matrix_at(p,x,y)) == expected
    cert['generator_norm_identities_checked'] = len(examples)
    cert['status'] = 'PASS'
    cert['scope'] = ('Exact polynomial nonzero certificates and degree-16 norm implementation; '
                     'does not establish finite-inventory C2 convergence or cross-branch counting.')
    path = Path(__file__).with_name('explicit_algebra_certificate.json')
    path.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':cert['status'],
        'terms':{k:len(p) for k,p in reduced.items()},
        'norm_grid_exponents':{k:norm_leading_certificate(p)['grid_exponent_D'] for k,p in reduced.items()},
        'point_jacobian_positive':det_j>0,'point_hessian_negative':det_h<0,
        'norm_checks':list(cert['norm_checks'])},indent=2))


if __name__ == '__main__':
    main()
