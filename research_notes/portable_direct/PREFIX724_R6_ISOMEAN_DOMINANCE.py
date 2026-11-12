"""PREFIX-724-R6: exact rational checks for mean-fiber outward dominance.
The Gamma kernel input is the author-level PREFIX-721/722 certificate, not rerun here.
Science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from fractions import Fraction as F
from pathlib import Path
import json

N = 189
M = F(N * 376, 2)
B = 4 * N * N * (N + 1) * 376 ** 4
x0 = F(11, 96)
r = F(1, 13_300_000_000)
kappa = F(40_800_000) - B * r
coefficient = kappa / M
old_radius = F(1, 14_000_000_000)
old_coefficient = F(2_000_000) / M
assert M == 35_532
assert B == 542_610_983_324_712_960
assert kappa == F(170_445_696, 78_125) > 2000
assert coefficient == F(14_203_808, 231_328_125)
assert 4 * coefficient == F(56_815_232, 231_328_125)
assert old_coefficient == F(500_000, 8_883)
assert coefficient/4 == F(3_550_952, 231_328_125)
assert r > old_radius and x0 - r > 0 and x0 + r < F(1, 2)

# Exact, independent polynomial sanity model: m=p+z,
# second moment m2=(z-p)^2+12*m.  J=4(z-p), K=4, m_p=m_z=1.
def mu(p, z):
    return p + z

def m2(p, z):
    return (z-p)**2 + 12*mu(p, z)

def obj(p, z, q):
    return q*q*(m2(p,z)-mu(p,z)**2)-q*mu(p,z)

# On a mean fiber: p -> p-h, z -> z+h. The exact gain is
# 4*d*h + 4*h*h in m2 and q^2 times that in obj, independent of t.
checks = 0
for i in range(0, 21):
    for j in range(i, 21):
        p, z = F(i, 100), F(j, 100)
        h = F(1, 1000)
        if p-h < 0 or z+h > F(1,2):
            continue
        d = z-p
        old_mu, new_mu = mu(p,z), mu(p-h,z+h)
        assert old_mu == new_mu
        gain = m2(p-h,z+h)-m2(p,z)
        v0, v1 = z-p, (z+h)-(p-h)
        assert gain == v1*v1-v0*v0
        assert gain > F(3,4)*(v1*v1-v0*v0)
        assert gain == 4*d*h+4*h*h
        assert gain > 4*(d*h+h*h/2)
        for q in (F(1,3),F(2),F(13,5),F(17)):
            assert obj(p-h,z+h,q)-obj(p,z,q) == q*q*gain
        checks += 1
assert checks > 100

result = {
    "schema": "PREFIX724_R6_MEAN_FIBER_DOMINANCE_V1",
    "date": "2026-11-12",
    "science_pin": "f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "parent": "PREFIX-675",
    "predecessor": "PREFIX-723-R6",
    "domain": "auxiliary Gamma 2-parameter square D=[0,1/2]^2; mean-fiber paths inside certified S_r",
    "center": str(x0), "radius": str(r),
    "inherited_K_strict_lower": str(kappa),
    "inherited_mu_partial_upper": str(M),
    "exact_gain_coefficient_kappa_over_M": str(coefficient),
    "exact_gain_coefficient_q_ge_2": str(4*coefficient),
    "old_square_K_over_M": str(old_coefficient),
    "mean_contrast_quadratic_gain_coefficient": str(coefficient/4),
    "mean_contrast_identity": "At fixed u=mu and v=z-p, dV_q/dv=q^2*v*K/(mu_p+mu_z); for |v1|>|v0| on one side, gain > q^2*kappa/(4*M)*(v1^2-v0^2).",
    "proof": "Along mu=c, dp/dz=-mu_z/mu_p; dM2/dz=J/mu_p=(z-p)K/mu_p. Thus M2 and every V_q strictly increase outward, with gain > q^2*(kappa/M)*(d0*h+h^2/2).",
    "checked_polynomial_example": "mu=p+z; M2=(z-p)^2+12mu; J=4(z-p)",
    "exact_rational_example_pairs": checks,
    "exact_rational_q_values_per_pair": 4,
    "reused_dependency": "PREFIX-721/722 author-level 189-row kernel K and derivative inequalities; no independent gamma-kernel rerun",
    "scope_limit": "The theorem on S_r is conditional on inherited K>kappa and mu_j>0; no additional 384x384 cells certified",
    "status": "AUTHOR_PROVED_RELATIVE_TO_INHERITED_CERTIFICATE / EXACT_FRACTION_TOY_CHECKED / UNREVIEWED / NOT_ADMITTED",
    "next": "Build certified mean-level boundary dominance on larger surviving rectangles using frozen Gamma kernel and exact Bernstein positivity for K and mu_j."
}
if __name__ == '__main__':
    Path(__file__).with_name('PREFIX724_R6_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('ALL_CHECKS_PASS PREFIX724-R6')
    print('r=', r, 'K>', kappa, 'K/M=', coefficient, 'q>=2 gain coeff=',4*coefficient)
    print('exact polynomial points=',checks)
