#!/usr/bin/env python3
"""Exact finite centered-mask verifier for the frozen 189-row killed Pascal
recursion. Uses the published PREFIX755 companion checker, same directory.
Theorem 756.1 proves the all-orders continuum implication from these
finite integer mask checks. Standard Python library only.
"""
from pathlib import Path
import runpy
import json

upstream = runpy.run_path(str(Path(__file__).with_name(
    "PREFIX755_R6_BERNSTEIN_MONOTONE_GAMMA_CHECK.py")))
wide, N = upstream["wide"], upstream["N"]
assert N == 189
checked = 0
nonempty_rows = 0
empty_rows = []
first_edges = {}

for n in range(1, N + 1):
    accepted = [k for k in range(n + 1) if wide(n, k)]
    checked += n + 1
    if not accepted:
        empty_rows.append(n)
        continue
    left = accepted[0]
    assert 0 <= left <= n // 2
    assert accepted == list(range(left, n - left + 1)), (
        "not symmetric and centered", n, accepted)
    first_edges[n] = left
    nonempty_rows += 1

assert checked == 18144, checked
assert nonempty_rows == 188, nonempty_rows
assert empty_rows == [189], empty_rows
assert first_edges[25] == 1, first_edges[25]
assert first_edges[188] == 89, first_edges[188]
result = {
    "schema": "PREFIX756_R6_CENTERED_KILLED_PASCAL_V1",
    "scientific_pin": "awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "comparison": "exact integer frozen width predicate; no floating point",
    "row_domain": "1<=n<=189; 0<=k<=n",
    "mask_memberships_checked": checked,
    "nonempty_centered_symmetric_rows": nonempty_rows,
    "empty_mask_rows": empty_rows,
    "left_edge_n25": first_edges[25],
    "left_edge_n188": first_edges[188],
    "global_theorem": "symmetric centered killed Pascal masks preserve normalized Bernstein central unimodality at arbitrary finite levels",
    "continuum_consequence": "S_n(p) nondecreasing for all real p in [0,1/2]",
    "status": "AUTHOR_EXACT_INTEGER_CHECK / UNREVIEWED / NOT_ADMITTED"
}
print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
print("ALL_CHECKS_PASS PREFIX756-R6")
