import sympy as s
import json
from pathlib import Path

u, v, z = s.symbols("u v z", nonzero=True)
# Only finite coefficients are used. Differentiation here is formal coefficient extraction.
nx = (1-u**9/(4*v**9))**12 * (1-4*u**15)**12 / ((1+448*u**51*v**9)**12*(1+1792*u**66*v**9)**12)
xjet = s.series(nx,u,0,16).removeO().expand()
assert s.simplify(xjet-(1-3*u**9/v**9-48*u**15)) == 0
ny = (1-4*z/u**9)**12 / ((1+448*u**51*z)**12*(1+1792*u**66*z)**12)
yc = s.factor(s.diff(ny,z).subs(z,0))
assert s.simplify(yc+48*u**(-9)*(1+112*u**60+448*u**75)) == 0
alpha,beta,R=s.symbols("alpha beta R", nonzero=True)
diag = alpha**180*beta**504*(1-4*alpha**15*R)**12-(1-4*R)**12
coeffs = [s.expand(diag).coeff(R,k) for k in [0,1]]
assert s.simplify(coeffs[0]-(alpha**180*beta**504-1)) == 0
assert s.simplify(coeffs[1]-(-48*alpha**195*beta**504+48)) == 0
result={
 "arithmetic":"exact symbolic rational-function coefficients",
 "x_normalized_jet_through_degree_15":str(xjet),
 "x_first_forbidden_power_in_u":81,
 "y_normalized_first_z_coefficient":str(yc),
 "y_first_forbidden_power_in_v":513,
 "axis_orders_in_base_coordinate":[18,126],
 "diagonal_constant_coefficient":str(coeffs[0]),
 "diagonal_R_coefficient":str(coeffs[1]),
 "status":"PASS",
 "scope":"Checks finite expansions used by the written algebraic proof; no analytic continuation or numerical sampling."
}
p=Path(__file__).with_name("algebraic_affine_rigidity_checks.json")
p.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))

