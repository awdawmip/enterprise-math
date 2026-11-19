#!/usr/bin/env python3
"""Exact native checks for the ingress-feedback implementation contract.

Usage: python check_native_realization.py SOURCE_ROOT PRIOR_FEEDBACK_ROOT
The two roots are an exact EM source cache/checkout and the prior contribution.
No external numerical reference is used. The new oriented III action retains
the prior named BRC tokens, primitive branches, source names and event history.
"""

from collections import Counter, defaultdict
from contextlib import redirect_stdout
from dataclasses import dataclass
from hashlib import sha1, sha256
from io import StringIO
from itertools import product
import importlib.util
import json
from pathlib import Path
import runpy
import sys


REVISION = "ef720decf4a35a276e509964250571a55421b9f8"
V5 = "experiments/x6_signed_internal_q_correction_v5_20260906/check_signed_internal_q_correction.py"
ATOMIC = "experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py"
SIGNED_BRC = "experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py"
PINS = {V5: "0104cf5cedd40831a94eec746394f977402ac36f",
        ATOMIC: "cf5bc031b90b26d82216925d2768583db4e10f57",
        SIGNED_BRC: "300a96e3dc24bf6fff73743037a0347a8bc83176"}
PRIOR_SHA256 = "83175b298bb8d18b43e2936043cf42f73efb476fa8b6581d4c9cdcd147af2ee0"
AXES = (0, 2, 5)


@dataclass(frozen=True)
class OrientedAtomicScatter:
    orientation: int
    generator: tuple
    joint_branches: tuple


@dataclass(frozen=True)
class State:
    carrier: object
    twist: tuple
    orientation: int = 1


def install_inputs(source_root, prior_root):
    for path, expected in PINS.items():
        data = (source_root / path).read_bytes()
        assert sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == expected
    prior = prior_root / "check_relation_updates.py"
    assert sha256(prior.read_bytes()).hexdigest() == PRIOR_SHA256
    spec = importlib.util.spec_from_file_location("prior_named_triad", prior)
    rel = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = rel
    spec.loader.exec_module(rel)
    with redirect_stdout(StringIO()):
        gauge = runpy.run_path(str(source_root / V5))
        atomic = runpy.run_path(str(source_root / ATOMIC))
    return rel, gauge, atomic


def macro(x, rel):
    """Append one source-preserving oriented III event and ingress feedback."""
    s = x.carrier.read_signs()
    tokens, branches = [], []
    for token in x.carrier.tokens:
        target = (token.axis + x.orientation) % 3
        sign = x.twist[token.axis] * token.sign
        tokens.append(rel.Token(token.source, target, sign))
        branches.append(rel.TokenBranch(
            token.source, (token.axis, token.sign), (target, sign),
            ((token.axis, -token.sign), (target, sign))))
    event = OrientedAtomicScatter(x.orientation, x.twist, tuple(branches))
    carrier = rel.NamedTriadBRC(
        x.carrier.anchor, x.carrier.sources, tuple(tokens),
        x.carrier.history + (event,))
    b = tuple(-s[i] * s[(i + x.orientation) % 3] for i in range(3))
    assert b in rel.TWISTS
    return State(carrier, b, x.orientation)


def reverse_state(x):
    """Internal path-reversal involution; it does not erase event history."""
    s = x.carrier.read_signs()
    p = s[0] * s[1] * s[2]
    return State(x.carrier, tuple(p * s[i] * x.twist[i] for i in range(3)),
                 -x.orientation)


def internal_key(x):
    return x.carrier.tokens, x.twist, x.orientation


def inverse_key(x, rel):
    u = x.carrier.read_signs()
    p = u[0] * u[1] * u[2]
    s = tuple(p * x.twist[(i + x.orientation) % 3] for i in range(3))
    a = tuple(u[(i + x.orientation) % 3] * s[i] for i in range(3))
    tokens = tuple(rel.Token(t.source, (t.axis - x.orientation) % 3,
                             s[(t.axis - x.orientation) % 3])
                   for t in x.carrier.tokens)
    return tokens, a, x.orientation


def position(port, anchor):
    axis, sign = port
    return tuple(c + (sign if k == AXES[axis] else 0)
                 for k, c in enumerate(anchor))


def token_feedback(frame, alpha, gauge):
    signs = tuple(1 if t > 0 else -1 for t in frame)
    outgoing = gauge["twisted_step"](frame, alpha)
    beta = tuple(-signs[(r + 1) % 3] * signs[(r + 2) % 3] for r in range(3))
    return outgoing, beta


def run(source_root, prior_root):
    rel, gauge, atomic = install_inputs(source_root, prior_root)
    counts = Counter()
    relation_fibers = defaultdict(list)
    fixed_fibers = defaultdict(list)
    full_fibers = defaultdict(list)
    for s, a in product(rel.SIGNS, rel.TWISTS):
        frame = tuple(s[r] * (AXES[r] + 1) for r in range(3))
        outgoing, beta = token_feedback(frame, a, gauge)
        base = State(rel.NamedTriadBRC.lift(s), a)
        first = macro(base, rel)
        by_source = tuple(t.sign * (AXES[t.axis] + 1) for t in first.carrier.tokens)
        assert outgoing == by_source
        assert beta == tuple(first.twist[t.axis] for t in first.carrier.tokens)
        counts["token_index_transport_cases"] += 1
        for local_eps in rel.SIGNS:
            eps = [1] * 6
            for axis, e in zip(AXES, local_eps):
                eps[axis] = e
            eps = tuple(eps)
            gf = gauge["gauge_frame"](frame, eps)
            ga = gauge["gauge_alpha"](frame, a, eps)
            gu, gb = token_feedback(gf, ga, gauge)
            assert gu == gauge["gauge_frame"](outgoing, eps)
            assert gb == gauge["gauge_alpha"](outgoing, beta, eps)
            counts["token_index_gauge_cases"] += 1

        for o in (-1, 1):
            x = State(rel.NamedTriadBRC.lift(s), a, o)
            assert internal_key(reverse_state(reverse_state(x))) == internal_key(x)
            assert internal_key(reverse_state(macro(reverse_state(x), rel))) == inverse_key(x, rel)
            forward = macro(x, rel)
            backward = macro(reverse_state(forward), rel)
            assert internal_key(reverse_state(backward)) == internal_key(x)
            assert len(backward.carrier.history) == 2
            f_event, b_event = backward.carrier.history
            for f, b in zip(f_event.joint_branches, b_event.joint_branches):
                assert f.source == b.source
                assert f.ingress == b.egress and f.egress == b.ingress
                assert b.primitive_steps == tuple((axis, -sign)
                                                 for axis, sign in reversed(f.primitive_steps))
                assert f.multiplicity == b.multiplicity == 1
                for anchor in ((0,) * 6, (3, -2, 1, 0, -4, 7)):
                    assert anchor in atomic["midpoint_options"](
                        position(f.ingress, anchor), position(f.egress, anchor))
                    assert anchor in atomic["midpoint_options"](
                        position(b.ingress, anchor), position(b.egress, anchor))
                    counts["native_reversed_branch_checks"] += 1
            counts["path_reversal_states"] += 1
            # This checks the retained internal projection at each half phase.
            # The macro calls evaluate T on the named carrier; this is not a
            # request to erase or physically replay the stored event history.
            def half_step(pair):
                z, phase = pair
                return (z, 1) if phase == 0 else (macro(z, rel), 0)

            def half_reverse(pair):
                z, phase = pair
                return (reverse_state(z if phase == 0 else macro(z, rel)), phase)

            for phase in (0, 1):
                left, left_phase = half_reverse(half_step(half_reverse((x, phase))))
                right_key = inverse_key(x, rel) if phase == 0 else internal_key(x)
                assert internal_key(left) == right_key and left_phase == 1 - phase
                counts["shell_closure_reversal_projections"] += 1

        r = rel.relations(s, a)
        relation_fibers[r].append((s, a))
        second = macro(first, rel)
        full_fibers[(first.carrier.read_signs(), second.carrier.read_signs())].append((s, a))
        for j in range(3):
            q = (r, s[j])
            q_next = (tuple(r[(i + 1) % 3] for i in range(3)), s[j] * r[(j - 1) % 3])
            actual_q_next = (rel.relations(first.carrier.read_signs(), first.twist),
                             first.carrier.read_signs()[j])
            assert q_next == actual_q_next
            # The exact transition descent proves arbitrary horizons by induction.
            third = macro(second, rel)
            trace = tuple(y.carrier.read_signs()[j] for y in (first, second, third))
            fixed_fibers[(j, trace)].append((q, s, a))
            counts["fixed_port_future_descent_cases"] += 1

    assert len(relation_fibers) == 4 and {len(v) for v in relation_fibers.values()} == {8}
    assert len(full_fibers) == 32 and {len(v) for v in full_fibers.values()} == {1}
    assert len(fixed_fibers) == 24 and {len(v) for v in fixed_fibers.values()} == {4}
    assert all(len({row[0] for row in rows}) == 1 for rows in fixed_fibers.values())

    witness_frame = (1, 3, -6)
    witness_a = (-1, -1, -1)
    u, correct_beta = token_feedback(witness_frame, witness_a, gauge)
    naive_beta = gauge["alpha_state"](witness_frame)
    correct_second = gauge["twisted_step"](u, correct_beta)
    naive_second = gauge["twisted_step"](u, naive_beta)
    assert correct_beta == (1, 1, -1) and naive_beta == (-1, 1, 1)
    assert correct_second == (-6, -1, -3) and naive_second == (6, -1, 3)
    eps = (-1, 1, 1, 1, 1, 1)
    naive_recomputed = gauge["alpha_state"](gauge["gauge_frame"](witness_frame, eps))
    naive_transported = gauge["gauge_alpha"](u, naive_beta, eps)
    assert naive_recomputed != naive_transported

    return {
        "schema": "X6_INGRESS_FEEDBACK_NATIVE_REALIZATION_V1",
        "status": "PASS_AUTHOR_CHECK",
        "source_revision": REVISION,
        "source_git_blobs": PINS,
        "prior_named_carrier_sha256": PRIOR_SHA256,
        "entrypoint": "check_native_realization.py:run",
        "carrier": "Three named unit tokens, retained signed ports and primitive III path history, embedded on X6 axes (0,2,5); two declared cyclic passage orientations",
        "arithmetic_operation": "OrientedAtomicScatter via the prior named BRC token/path types; original V5 tokenwise kernel and original signed_brc midpoint kernel",
        "observer_future_scope": "Exact finite-state reversal and all repeated ingress-feedback futures for the explicitly listed relation/port observers",
        "history_policy": "Both forward and reverse path events retained; no timeline erasure and no physical time interval claim",
        "counts": dict(counts),
        "closure_memory_state_counts": {
            "relation_future": 4,
            "one_fixed_port_raw_future": 8,
            "all_three_ports_next_two_shells": 32},
        "closure_memory_bits": {
            "relation_future": 2,
            "one_fixed_port_raw_future": 3,
            "all_three_ports_next_two_shells": 5},
        "indexing_witness": {
            "ingress_frame": witness_frame, "ingress_twist": witness_a,
            "first_egress": u, "correct_next_twist_in_token_order": correct_beta,
            "untransported_next_twist": naive_beta,
            "correct_second_egress": correct_second, "untransported_second_egress": naive_second,
            "naive_gauge_recomputed": naive_recomputed,
            "naive_gauge_transported": naive_transported},
        "native_permission": "A concrete covariant finite event-law extension is constructed. Selection of this law by actual TRIADIC_CLOSURE_E dynamics is not inferred from path admissibility alone.",
        "residual_certificate": "Zero mismatch against the typed native kernels; exact observer fibers. The wrong-index witness is an implementation error, not a physical residual."}


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: check_native_realization.py SOURCE_ROOT PRIOR_FEEDBACK_ROOT")
    result = run(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())
    Path(__file__).with_name("native_realization_results.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], **result["counts"],
                      "closure_memory_state_counts": result["closure_memory_state_counts"]}))
