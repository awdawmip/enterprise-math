"""Replay bounded matrix/BRC/T6 evidence; does not enumerate arbitrary q."""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from channel_quotient import (
    ROOT, GEOMETRY_SOURCE, GEOMETRY_SHA256, brc_gate_observation,
    finite_gate_descent_check, gate_image, geometry,
    make_gate_witness, verify_gate_witness,
)


def main():
    x, y = (5, 0, 0, 0, 0, 0), (0, 1, 1, 1, 1, 1)
    witness = make_gate_witness(x, y)
    verification = verify_gate_witness(x, y, witness)
    assert verification.status == "VALID" and len(witness.steps) == 5
    for gate in range(6):
        matrix = geometry.kernel(gate)
        assert geometry.recurrent_mass_power(matrix, 2) == matrix
    hx = (1, 0, 0, 0, 0, 0)
    hy = (F(1, 2), F(1, 2), 0, 0, 0, 0)
    vx, cx, wx = brc_gate_observation(hx, 2)
    vy, cy, wy = brc_gate_observation(hy, 2)
    assert vx == vy and wx != wy
    inputs = ((0,) * 6, hx, hy, (2, 3, 0, 0, 0, 0))
    t6 = [finite_gate_descent_check(inputs, i, lambda v: sum(v) ** 2)
          for i in range(6)]
    assert all(t6)
    files = [Path(__file__), Path(__file__).with_name("channel_quotient.py"),
             Path(__file__).with_name("test_channel_quotient.py"), GEOMETRY_SOURCE,
             ROOT / "src/enterprise_math/operation_quotient.py",
             ROOT / "src/enterprise_math/brc_histogram.py",
             ROOT / "src/enterprise_math/brc_weighted.py",
             ROOT / "src/enterprise_math/brc_weighted_recurrent.py"]
    data = {
        "status": "FINITE_WITNESSES_VERIFIED",
        "scope": "rational six-channel mass vector; not arbitrary-q execution or microscopic quotient",
        "source_sha256": {str(p.relative_to(ROOT)).replace('\\', '/'):
                          hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
        "reused_geometry_sha256": GEOMETRY_SHA256,
        "five_step_witness": {
            "source": list(map(str, witness.source)), "target": list(map(str, witness.target)),
            "steps": [dict(before=list(map(str, s.before)), after=list(map(str, s.after)),
                           donor=s.donor, receiver=s.receiver, amount=str(s.amount), gate=s.gate,
                           common_matrix_image=list(map(str, gate_image(s.before, s.gate))))
                      for s in witness.steps]},
        "brc_boundary": {
            "inputs": [list(map(str, hx)), list(map(str, hy))], "gate": 2,
            "same_channel_mass": list(map(str, vx)), "counts": [cx.count, cy.count],
            "histograms": [[[str(w), count] for w, count in h.entries] for h in (wx, wy)]},
        "finite_single_gate_t6_checks": t6,
        "global_knowledge": "main@4fa7d7d",
    }
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
