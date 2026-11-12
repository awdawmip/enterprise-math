"""PREFIX-722-R6: rational continuation of the published PREFIX-721 Gamma wedge.
Scientific input remains f42f2906d77f24085c123f3ccfe9667d41caa96d.
This verifies arithmetic conditional on PREFIX-721's author-certified kernel bounds;
it does not recompute the frozen 189-row Gamma kernel or establish review admission.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
N = 189
B = 4*N*N*(N+1)*376**4
J0 = 40_800_000
r_old = Q(1,14_000_000_000)
r_new = Q(1,13_300_000_000)
K_new_lower = Q(J0) - B*r_new
assert B == 542610983324712960
assert r_new > r_old and K_new_lower > 2_000
assert r_new < Q(11,96) and r_new < Q(1,2)-Q(11,96)
# For any positive-order partial of order k <=3, use the previously
# certified Bernstein bounds for mu and second raw moment M2.
# Along (x+s,x-s), the k-th directional derivative adds 2**k.
mu_p_upper = Q(N*376, 2)
assert mu_p_upper == 35532
C = N*(4*N+1)*752**3  # |(M2-mu**2-t*mu)'''| for 0<=t<=1/2
assert C == 60_843_082_051_584 and C < 66*10**12
h = Q(1,10**12)
assert h < r_old
# At a diagonal stationary point inside the old square, PREFIX-721
# gives J_z = K >2e6, mu_p>0, and F''(0)=2*J_z/mu_p.
# Taylor gives F(h)-F(0) > [2e6/35532 - C*h/6] h**2.
gain_coefficient = Q(2_000_000)/mu_p_upper - Q(C,6)*h
assert gain_coefficient > 40
assert Q(2_000_000)/mu_p_upper - 11 > 40
# q >=2, q^2 >=4: a constructive absolute objective gain.
assert 4*40*h*h == Q(160,10**24)
result = {
    'schema':'PREFIX722_R6_EXACT_RATIONAL_ESCAPE_V1',
    'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'parent':'PREFIX-721',
    'scope':'auxiliary two-parameter Gamma clock, D=[0,1/2]^2',
    'published_assumptions':{
        'J_z_at_11_over_96_strict_lower':'40800000',
        'K_Lipschitz_bound':str(B),
        'old_square_K_strict_lower':'2000000',
        'mu_p_positive':'on int(D)',
        'derivative_bounds':'PREFIX-721, orders 1..3'
    },
    'new_square_radius':str(r_new),
    'new_K_lower_exact_rational':str(K_new_lower),
    'new_K_strict_lower_integer':'2000',
    'old_square_radius':str(r_old),
    'directional_third_derivative_bound':str(C),
    'mu_p_upper':str(mu_p_upper),
    'constructive_offset':str(h),
    'gain_coefficient_lower':str(gain_coefficient),
    'gain_for_diagonal_stationary_f_t_strict_lower':str(40*h*h),
    'gain_for_diagonal_stationary_V_q_strict_lower_q_ge_2':str(160*h*h),
    'verification':'EXACT_FRACTION_ARITHMETIC_PASS; inherited kernel not rerun',
    'admission':'AUTHOR_DERIVATION / UNREVIEWED / NOT_ADMITTED'
}
if __name__=='__main__':
    p = Path(__file__).with_name('PREFIX722_R6_RESULTS.json')
    p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('ALL_CHECKS_PASS PREFIX722-R6', 'K_margin='+str(K_new_lower),
          'gain_coefficient='+str(gain_coefficient), 'C='+str(C))
