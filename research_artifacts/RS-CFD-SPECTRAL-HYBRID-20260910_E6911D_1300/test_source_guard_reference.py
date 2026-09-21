from source_guard_reference import (
    StaticSourceSupportContract, StickyDenseSourceGuard, dense_rk4_step,
    exact_support, guarded_rk4_step, guarded_stage_rhs, inspect_source,
)

P=(1,0,0); Q=(0,1,0); R=(1,1,0)


def dense_rhs(y, source):
    # Finite-mode witness: source is part of RHS, and once p,q coexist the true
    # nonlinear operator emits r. This encodes the proved p+q escape mechanism.
    out = dict(source)
    if y.get(P,0j) != 0j and y.get(Q,0j) != 0j:
        out[R] = out.get(R,0j) - 2j*y[P]*y[Q]
    return out


def sparse_rhs(y, source):
    # Witness carrier contains P only; guard must prevent use after escape.
    return {k:v for k,v in source.items() if k == P}


def test_zero_source_accepted_sparse():
    g=StickyDenseSourceGuard.from_carrier({P})
    rhs, route, inspection = guarded_stage_rhs(stage=1, stage_state={P:1+2j}, source={},
        sparse_rhs=sparse_rhs, dense_rhs=dense_rhs, guard=g)
    assert route == 'SPARSE' and inspection.safe and not g.dense_sticky and rhs == {}


def test_static_declared_support_accepts_changing_coefficients():
    c=StaticSourceSupportContract.from_labels({Q})
    assert c.validate({Q: 1+0j}).safe
    assert c.validate({Q: -3+7j}).safe
    assert c.validate({Q: 0j}).safe
    assert c.seed({P}) == frozenset({P,Q})


def test_static_declared_support_rejects_label_escape():
    c=StaticSourceSupportContract.from_labels({Q})
    x=c.validate({Q:1j, R:2j})
    assert x.escape == frozenset({R})


def test_dynamic_escape_forces_dense_replay_and_preserves_mode():
    g=StickyDenseSourceGuard.from_carrier({P})
    rhs, route, inspection = guarded_stage_rhs(stage=2, stage_state={P:1+0j}, source={Q:3-4j},
        sparse_rhs=sparse_rhs, dense_rhs=dense_rhs, guard=g)
    assert route == 'DENSE'
    assert inspection.escape == frozenset({Q})
    assert rhs[Q] == 3-4j
    assert g.first_escape_stage == 2 and g.dense_sticky


def test_stage2_escape_is_precommit_and_guarded_rk4_matches_all_dense():
    y0={P:1+0j}
    def source(stage, _state):
        return {} if stage == 1 else ({Q:2+0j} if stage == 2 else {})
    g=StickyDenseSourceGuard.from_carrier({P})
    guarded, routes = guarded_rk4_step(y0, 0.1, source_for_stage=source,
        sparse_rhs=sparse_rhs, dense_rhs=dense_rhs, guard=g)
    dense = dense_rk4_step(y0, 0.1, source_for_stage=source, dense_rhs=dense_rhs)
    assert routes == ('SPARSE','DENSE','DENSE','DENSE')
    assert guarded == dense
    assert g.first_escape_stage == 2


def test_exact_support_counts_arbitrarily_small_nonzero():
    tiny=complex(1e-300, -1e-300)
    assert exact_support({Q:tiny}) == frozenset({Q})
    exact=inspect_source({Q:tiny}, {P})
    approx=inspect_source({Q:tiny}, {P}, tolerance=1e-250)
    assert exact.exact and exact.escape == frozenset({Q})
    assert not approx.exact and approx.safe
