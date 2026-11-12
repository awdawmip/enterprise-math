"""PREFIX-723-R6: exact rational outward-ascent certificate.
Frozen science: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Conditional on published PREFIX-721/722 author-level kernel bounds;
does not rerun the survivor recurrence or grant independent review.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

N=189
M=Q(N*376,2)
MU2=Q(N*376**2,2)
M2_2=Q(N*(N+1)*376**2,2)
MAX_MEAN=2*N
T_MAX=Q(1,2)
H=M2_2+(2*MAX_MEAN+T_MAX)*MU2+2*M**2
x0=Q(11,96)
r=Q(1,13_300_000_000)
B=4*N*N*(N+1)*376**4
K_BOUND=Q(40_800_000)-B*r
g=Q(2_000)/(2*M)
max_step=g*(2*r)/H
margin=min(x0-r,Q(1,2)-x0-r)
f_gain=g*g/(2*H)
v_gain=4*f_gain
assert M==35_532 and MU2==13_360_032 and M2_2==2_538_406_080
assert H==15_170_316_336
assert B==542_610_983_324_712_960
assert K_BOUND==Q(170_445_696,78_125)>2_000
assert g==Q(250,8_883)
assert max_step==Q(1,3_584_560_672_337_500_800_000)<margin
assert g/H<1
assert f_gain==Q(15_625,598_527_301_736_353_752)
assert v_gain==Q(15_625,149_631_825_434_088_438)
for a in range(1,41):
    for b in range(1,51):
        u,v=Q(a),Q(b)
        A,C=Q(a-b,13),Q(2*b-a,17)
        weighted=u*A+v*C
        if weighted>0:
            assert max(A,C)>=weighted/(u+v)
result={
 "schema":"PREFIX723_R6_OUTWARD_ASCENT_CERTIFICATE_V1",
 "date":"2026-11-12",
 "science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "parent":"PREFIX-675",
 "predecessor":"PREFIX-722-R6",
 "scope":"auxiliary BRC/independent-Gamma observer; D=[0,1/2]^2; real q>=2",
 "inherited_certificate":"PREFIX-721/722 author-level K and Bernstein derivative bounds; 189-row kernel not rerun",
 "center":"11/96", "square_radius":str(r),
 "strict_K_lower_rational":str(K_BOUND),
 "uniform_second_coordinate_derivative_bound":str(H),
 "outward_derivative_gap_coefficient":str(g),
 "max_outward_step":str(max_step),
 "minimum_domain_boundary_margin":str(margin),
 "strict_f_t_gain_per_separation_squared":str(f_gain),
 "strict_V_q_gain_per_separation_squared_q_ge_2":str(v_gain),
 "test":"EXACT_FRACTION_ASSERTIONS_PASS; 2000 weighted-average cases; parent kernel not rerun",
 "admission":"AUTHOR_DERIVED / UNREVIEWED / NOT_ADMITTED",
 "next_problem":"Local Bernstein outward ascent on surviving fine-grid rectangles with genuine disjoint area certification"
}
if __name__=="__main__":
    Path(__file__).with_name("PREFIX723_R6_RESULTS.json").write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS PREFIX723-R6")
    print("H=",H,"g=",g,"max_step=",max_step)
    print("V_gain_coefficient_gt=",v_gain)
