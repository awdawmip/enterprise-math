#!/usr/bin/env python3
"""PREFIX-282: original Stage50 typed C4-BRC observation-scope split.
Run inside the pinned Stage50 bundle checkout with:
    PYTHONPATH=<checkout> python -S verify_prefix282.py
Only original stage50/stage49b/stage46 C4-BRC operations evaluate scientific data.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from stage50 import interference as h
from stage49b import gauss_brc as g
from stage46 import brc_port_update as port

EXPECTED = {
    "stage50/interference.py": "43b23d47e5d3da191aeaeefefe4f378fea2166eefd228ae77475f7196ceca853",
    "stage49b/gauss_brc.py": "a2a16cee4d9e851aa8c676d1ab68491c7a8954f7ff9232e4cb57424f6fd31ccf",
    "stage46/brc_port_update.py": "a6bc156c789859d1aabefdef5db56b9d313565c5684d744e591e3371687baee4",
}


def enc(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, tuple):
        return [enc(v) for v in x]
    if isinstance(x, list):
        return [enc(v) for v in x]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    return x


def verify():
    root = Path(h.__file__).resolve().parents[1]
    for path, expected in EXPECTED.items():
        actual = hashlib.sha256((root / path).read_bytes()).hexdigest()
        assert actual == expected, (path, actual)
    assert len(port.coin(12)) == 12
    packets = {
        "f": {0: h.ONE, 1: (F(4), F(0)), 2: (F(4), F(0))},
        "g": {0: (F(2), F(0)), 1: (F(5), F(0)), 2: (F(2), F(0))},
    }
    masses = {name: h.packet_z(packet) for name, packet in packets.items()}
    assert masses == {"f": F(33), "g": F(33)}
    moments = {
        name: [h.moment(packet, r) for r in range(5)]
        for name, packet in packets.items()
    }
    assert moments["f"] == moments["g"]
    assert moments["f"] == [(F(1), F(0)), (F(20, 33), F(0)), (F(4, 33), F(0)),
                            (F(0), F(0)), (F(0), F(0))]
    ports = {}
    port_calls = 0
    for name, packet in packets.items():
        records = []
        for r in range(5):
            row = []
            for phase in range(4):
                out = h.local(packet, r, phase)
                assert out["norm_in"] == out["norm_out"] == 2 * masses[name]
                assert out["compatible"]
                model = F(5, 18) * (1 - h.cmul(h.PHASE[phase], moments[name][r])[0])
                assert out["probability"] == model
                row.append(out["probability"])
                port_calls += 1
            records.append(row)
        ports[name] = records
    assert ports["f"] == ports["g"]
    masks = {name: h.three_masks(packet) for name, packet in packets.items()}
    assert masks["f"] == masks["g"]
    assert masks["f"]["I3"] == F(0)
    diag = {}
    for name, packet in packets.items():
        variance, twice_second, probs = h.packet_variance(packet)
        assert probs == {j: h.pair_observer(h.field_packet({j: a})) / masses[name]
                         for j, a in packet.items()}
        assert sum(probs.values(), F(0)) == 1
        mean = sum((j * prob for j, prob in probs.items()), F(0))
        second = sum((j*j * prob for j, prob in probs.items()), F(0))
        assert variance == second - mean*mean
        assert twice_second == 2*second
        cost = sum((g.energy(g.add((), g.CYCLE, j))*prob
                    for j, prob in probs.items()), F(0))
        assert cost == twice_second
        diag[name] = {"probs": probs, "mean_source_index": mean,
                      "second_source_moment": second,
                      "variance": variance, "loop_link_cost": cost}
    assert diag["f"]["probs"] == {0: F(1,33), 1: F(16,33), 2: F(16,33)}
    assert diag["g"]["probs"] == {0: F(4,33), 1: F(25,33), 2: F(4,33)}
    assert diag["f"]["loop_link_cost"] - diag["g"]["loop_link_cost"] == F(26, 11)
    assert diag["f"]["variance"] - diag["g"]["variance"] == F(8, 121)
    assert diag["f"]["mean_source_index"] - diag["g"]["mean_source_index"] == F(5,11)
    return enc({
        "schema": "PREFIX282_ORIGINAL_STAGE50_OBSERVER_SPLIT_V1",
        "status": "EXACT_SOURCE_MODEL_CHECK_PASS__NOT_NATIVE_HEARTBEAT_ADMITTED",
        "original_source_commit": "318f47839d6bc7c850a3b7cc0fcb22d48febd9ba",
        "original_source_sha256": EXPECTED,
        "source_functions": ["stage50.interference.local", "stage50.interference.moment",
                             "stage50.interference.three_masks", "stage50.interference.packet_variance",
                             "stage50.interference.pair_observer", "stage49b.gauss_brc.energy"],
        "input_packets": {"f": [1,4,4], "g": [2,5,2]},
        "norms": masses, "normalized_moments_r0_to_r4": moments,
        "stage50_external_probability_r0_to_r4_by_C4_phase": ports,
        "original_stage50_local_calls": port_calls,
        "original_stage50_three_input_port_masks": masks,
        "field_load_diagonal": diag,
        "differences_f_minus_g": {
            "variance": F(8,121), "loop_link_cost": F(26,11),
            "mean_source_index": F(5,11)},
        "verification_scope": "Original C4-BRC kernel, declared packet/load readouts; no native heartbeat model_law_id or detector calibration.",
    })


if __name__ == "__main__":
    result = verify()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
