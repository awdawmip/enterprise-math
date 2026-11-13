"""EC49AR parameter extension: exact rational endpoint certificate and sharp failure witness.

Run beside EC49AQ's VERIFY.py (which exhausts 1365+3003 supports):
    python3 VERIFY_PARAMETER.py > PARAMETER_REPORT.json
No floating arithmetic or grid extrapolation. Analytic extension relies on convexity in eta.
"""
from fractions import Fraction as F
from itertools import product
import contextlib
import io
import json

with contextlib.redirect_stdout(io.StringIO()):
    from VERIFY import v_high, v5, paid_cost

K = F(177, 172)
ETA_STAR = F(175, 674)
TARGET = F(77, 688)
WITNESS = (
    (F(0), F(3, 16), F(1, 4), F(0), F(9, 16)),
    (F(1), F(0), F(0), F(0), F(0)),
    (F(0), F(1), F(0), F(0), F(0)),
)
ORIGINAL_ACCEPT = {(0, 1), (1, 2), (2, 0)}
EXTRA_ACCEPT = (1, 1, 0)


def t(w, u, eta):
    return F(1, 2) + (2*u-1)*(1-w)*eta


def purchased_pq(x, eta, c, u, z):
    pp = qq = F(0)
    for w in range(3):
        pp += x[w][c] * t(w, u, eta) * (F(1, 6) if z == w else F(1, 12))
        qq += x[w][c] * t(w, u, eta) / 9
    return pp, qq


def full_purchase_support(x, eta):
    return sum((max(F(0), pp-K*qq)
                for c, u, z in product(range(4), range(2), range(3))
                for pp, qq in [purchased_pq(x, eta, c, u, z)]), F(0))


def accept_value(x, eta, with_extra=False):
    a = b = F(0)
    for c, u, z in product(range(4), range(2), range(3)):
        if (c, z) in ORIGINAL_ACCEPT or (with_extra and (c, u, z) == EXTRA_ACCEPT):
            pp, qq = purchased_pq(x, eta, c, u, z)
            a += pp
            b += qq
    return a, b, a - K*b


assert len(v_high) == 24 and len(v5) == 144
assert paid_cost(WITNESS) == F(13, 16)
assert sum((F((1, 1, 2, 2, 0)[c])*WITNESS[w][c]
            for w, c in product(range(3), range(5))), F(0)) == F(43, 16)

endpoints = []
for eta, high_expected in [(F(0), F(243, 2752)), (ETA_STAR, F(36, 337))]:
    high_scores = [full_purchase_support(x, eta) for x in v_high]
    boundary_scores = [full_purchase_support(x, eta) for x in v5]
    assert max(high_scores) == high_expected
    assert max(boundary_scores) == TARGET
    assert sum(v == TARGET for v in boundary_scores) == 24
    assert accept_value(WITNESS, eta) == (F(25, 64), F(13, 48), TARGET)
    endpoints.append({
        'eta': str(eta),
        'high_max_F': str(max(high_scores)),
        'boundary_max_F': str(max(boundary_scores)),
        'boundary_argmax_count': sum(v == TARGET for v in boundary_scores),
        'checked_vertices': len(high_scores)+len(boundary_scores),
    })

# The extra leaf is exactly the first positive new observation for the witness.
for eta in (ETA_STAR, F(13, 50), F(499, 1000)):
    pp, qq = purchased_pq(WITNESS, eta, *EXTRA_ACCEPT)
    assert pp-K*qq == (674*eta-175)/16512
    a, b, h = accept_value(WITNESS, eta, with_extra=True)
    assert h == TARGET + (674*eta-175)/16512
    assert a >= 0 and b >= 0

assert accept_value(WITNESS, F(13, 50), with_extra=True)[2] == F(7701, 68800)
assert F(7701, 68800)-TARGET == F(1, 68800)

report = {
    'schema': 'EC49AR_SHARP_ETA_PLATEAU_CERT_V1',
    'status': 'AUTHOR_PROVED_EXACT_FRACTION_CHECK_PASS_UNREVIEWED',
    'global_knowledge_scope': 'auxiliary positive BRC, not signed/native X6/heartbeat',
    'C1': '43/48', 'C2': '13/16', 'k': '177/172',
    'eta_constant_optimum_interval': '0 <= eta <= 175/674',
    'eta_sharp_threshold': str(ETA_STAR),
    'global_Hmax_on_interval': str(TARGET),
    'proof_extension': 'F_eta(x) convex in eta on a fixed truncated 168-vertex polytope; endpoint certificates imply every real intermediate eta',
    'endpoint_certificates': endpoints,
    'original_witness_alpha': '25/64', 'original_witness_beta': '13/48',
    'sharp_failure_interval': '175/674 < eta < 1/2',
    'extra_legal_acceptance_observation': '(A1,u=1,z=0)',
    'witness_improvement_H': '(674*eta-175)/16512',
    'test_eta': '13/50',
    'test_improved_legal_H': '7701/68800',
    'test_improvement': '1/68800',
    'independent_review': 'pending',
}
print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
