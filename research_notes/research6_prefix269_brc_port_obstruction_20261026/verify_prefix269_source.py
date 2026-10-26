#!/usr/bin/env python3
"""PREFIX-269: exact Source-package verification, NOT executed in the publishing session.

Run from a checkout of Enterprise Math at:
  PYTHONPATH=src python research_notes/research6_prefix269_brc_port_obstruction_20261026/verify_prefix269_source.py

This uses canonical nonnegative-rational CWM, recurrent-port and recurrent-mass
interfaces, without phase substitution or physical heartbeat claims.
"""
from fractions import Fraction as F

from enterprise_math.brc_weighted import cwm_edge, cwm_propagate
from enterprise_math.brc_recurrent_ports import (
    recurrent_port_signature,
    recurrent_port_context_matrix,
)
from enterprise_math.brc_weighted_recurrent import (
    finite_recurrent_mass_analysis,
    verify_recurrent_integer_stable_certificate,
)

zero = F(0)
half = F(1, 2)
quarter = F(1, 4)

# Full state order: (p, hidden, q).  Visible labeled port indices are (0,2).
module_a = ((zero, half, zero),
            (zero, zero, half),
            (zero, zero, zero))
module_b = ((zero, half, zero),
            (half, zero, zero),
            (zero, zero, zero))
port_a = recurrent_port_signature(module_a, [1])
port_b = recurrent_port_signature(module_b, [1])
assert port_a.boundary_indices == port_b.boundary_indices == (0, 2)
assert port_a.effective_matrix == ((zero, quarter), (zero, zero))
assert port_b.effective_matrix == ((quarter, zero), (zero, zero))
assert port_a.hidden_loop_zeta == port_b.hidden_loop_zeta == F(1)

# Forget output-port label; the two branches collapse to the same CWM triple.
aggregate = cwm_propagate(cwm_edge(half), cwm_edge(half))
assert (aggregate.count, aggregate.total, aggregate.dominant) == (1, quarter, quarter)

# One future positive-rational port context, permitted by WBRC-T31.
update = ((zero, zero), (F(4), zero))
def apply_port_context(signature):
    return recurrent_port_context_matrix(signature, update, ((), ()), (), ())

a_next = apply_port_context(port_a)
b_next = apply_port_context(port_b)
assert a_next == ((zero, quarter), (F(4), zero))
assert b_next == ((quarter, zero), (F(4), zero))
assert a_next[0][1] * a_next[1][0] == 1  # unit-mass repeated closed path

check_a = finite_recurrent_mass_analysis(a_next)
check_b = finite_recurrent_mass_analysis(b_next)
assert not check_a.stable
assert check_b.stable
assert check_b.star == ((F(4, 3), zero), (F(16, 3), F(1)))
assert verify_recurrent_integer_stable_certificate(b_next, (1, 5))

print("PREFIX269_SOURCE_IMPORT_BRC_PASS")
