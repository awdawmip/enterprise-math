from fractions import Fraction as F
from pathlib import Path
import json
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
CERTIFICATE = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parents[1] / "divisor_extrema" / "20261121_c87_global_position_ordering_and_complete_triangle_integral" / "integrated_kernel_certificate.json"
_certificate_bytes = CERTIFICATE.read_bytes()
_certificate_git_blob = hashlib.sha1(
    b"blob " + str(len(_certificate_bytes)).encode("ascii") + b"\0" + _certificate_bytes
).hexdigest()
if _certificate_git_blob != "4269238343a4eb5815fb048ffd0dd59b9e4fc280":
    raise ValueError("C87 certificate differs from the pinned source Git blob")
SOURCE = json.loads(_certificate_bytes)
BETA = F(1, 200)

def interval_data(row, name):
    q = row[name]
    return F(q["lower_numerator"]) / int(q["denominator"]), F(q["upper_numerator"]) / int(q["denominator"])

# Reuse the existing whole-cell certificates; do not regenerate their kernel quadrature.
cells = [(F(0), F(1, 8), F(1, 40), F(1, 2))]
previous = F(1, 8)
for row in SOURCE["intervals"]:
    lo, hi = map(F, row["x_interval"])
    alo, ahi = interval_data(row, "A_interval")
    assert lo == previous and lo < hi
    lower, upper = alo / hi**2, ahi / lo**2
    assert lower > BETA and upper >= lower
    cells.append((lo, hi, lower, upper))
    previous = hi
assert previous == 1 and len(cells) == 61

# Pure-integer root comparisons establish the crude axis bound B <= 1/2.
assert 2 * 97**20 > 100**20       # 2^(-1/20) < 97/100
assert 4 * 93**20 < 100**20       # 4^(-1/20) > 93/100
axis_a_upper = F(211,244)*F(97,100)-F(101,122)*F(93,100)+F(23,61)
axis_remainder = F(9318931,47520000) / 8
assert axis_a_upper + axis_remainder < F(1,2)

# zeta(2) is bounded by telescoping rational tails. N controls only this scalar.
N = 64
s = sum((F(1,k*k) for k in range(1,N+1)), F(0))
zlo, zhi = s + F(1,N+1), s + F(1,N)
clo, chi = F(16000,16359) / zhi, F(16000,16359) / zlo
cmid = (clo+chi)/2
crad = (chi-clo)/2

def positive(q):
    return max(F(0),q)

def area(lo, hi, theta):
    """Exact trapezoid/triangle area of the rational piecewise-affine hinge."""
    m = min(theta, 1-theta)
    a = 1-m
    q = m/a
    return a * (positive(hi-q)**2-positive(lo-q)**2)/2

def hinge(x, theta):
    return max((1-theta)*x-theta, theta*x-(1-theta), F(0))

def area_by_knots(lo, hi, theta):
    """Independent exact common-knot trapezoid evaluation."""
    points = {lo, hi}
    for q in [theta/(1-theta) if theta != 1 else F(2),
              (1-theta)/theta if theta != 0 else F(2)]:
        if lo < q < hi:
            points.add(q)
    points = sorted(points)
    return sum(((b-a)*(hinge(a,theta)+hinge(b,theta))/2
                for a,b in zip(points,points[1:])), F(0))

def j0(theta):
    return (1-2*theta)**2 / (2*max(theta,1-theta))

def proxy(theta):
    return -cmid*sum((((l+u)/2)*area(a,b,theta) for a,b,l,u in cells),F(0))

def value_enclosure(theta):
    lo = clo*sum((l*area(a,b,theta) for a,b,l,u in cells),F(0))
    hi = chi*sum((u*area(a,b,theta) for a,b,l,u in cells),F(0))
    # centered I(theta) = -(I(1/2)-I(theta))
    return -hi,-lo

def pair_enclosure(left,right):
    assert 0 <= left < right <= F(1,2)
    total_lo,total_hi=F(0),F(0)
    for a,b,l,u in cells:
        d=area(a,b,left)-area(a,b,right)
        assert d >= 0
        total_lo += l*d
        total_hi += u*d
    return clo*total_lo,chi*total_hi

def pack(x):
    return {"exact":str(x),"decimal":float(x)}

# Covers both symmetric halves, endpoints, and cell/kink changes.
thetas = [F(0), F(1,20), F(1,10), F(1,4), F(1,3), F(1,2),
          F(2,3), F(3,4), F(9,10), F(1)]
for t in thetas:
    assert sum((area(a,b,t) for a,b,l,u in cells),F(0)) == j0(t)
    for a,b,l,u in cells:
        assert area(a,b,t) == area_by_knots(a,b,t)
    vlo,vhi=value_enclosure(t)
    assert vlo <= proxy(t) <= vhi
    assert proxy(t)==proxy(1-t)

pairs={}
for left,right in [(F(1,10),F(1,2)),(F(1,4),F(1,2)),(F(1,10),F(1,4)),(F(0),F(1,2))]:
    lo,hi=pair_enclosure(left,right)
    simple=clo*BETA*(j0(left)-j0(right))
    assert 0 < simple <= lo <= hi
    pairs[f"{left},{right}"]={"I_right_minus_I_left":[pack(lo),pack(hi)],
                             "universal_rational_lower":pack(simple)}

jensen=[]
for a,b,w in [(F(1,10),F(9,10),F(1,2)),(F(0),F(1,2),F(1,3)),
              (F(1,5),F(7,10),F(2,5)),(F(1,20),F(1,4),F(3,7))]:
    z=w*a+(1-w)*b
    gap=proxy(z)-w*proxy(a)-(1-w)*proxy(b)
    bound=cmid*BETA*w*(1-w)*(b-a)**2/2
    assert gap >= bound > 0
    jensen.append({"a":str(a),"b":str(b),"lambda":str(w),"gap":pack(gap),"lower":pack(bound)})

uniform_error = chi*sum((((u-l)/2)*(b*b-a*a)/2 for a,b,l,u in cells),F(0))
uniform_error += crad*sum((((u+l)/2)*(b*b-a*a)/2 for a,b,l,u in cells),F(0))
result={
    "scope":"Author-side rational compilation of existing whole-cell B bounds; no original-inventory bridge rerun.",
    "source_commit":"63eec225728612d1df6c178b516b5ecf4687ee06",
    "source_blob":"4269238343a4eb5815fb048ffd0dd59b9e4fc280",
    "rational_cells":len(cells),"zeta_tail_N":N,
    "C_interval":[pack(clo),pack(chi)],
    "axis_B_upper_proved":pack(axis_a_upper+axis_remainder),
    "uniform_centered_proxy_error":pack(uniform_error),
    "pairs":pairs,"jensen_checks":jensen,
    "finite_exact_checks":{"trapezoid_cases":len(thetas)*len(cells),"value_symmetry_cases":len(thetas),"jensen_cases":len(jensen)}
}
(ROOT/"rational_position_results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k not in ["jensen_checks"]},ensure_ascii=False,indent=2))

