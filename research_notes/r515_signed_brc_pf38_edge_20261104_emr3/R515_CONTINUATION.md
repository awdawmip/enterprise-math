# R515 continuation — signed BRC s=3,m=38

2026-11-04. Frozen scientific pin R462 @ 18783e01e3646c72b7aab3b16d3f565e83e6446f; predecessor R514 @ 513658f3a928ee4036cf21b060b1928bdc67afb3.

Mother objective: exact signed BRC Toeplitz s=3 right-edge sign classifications and structural explanation of sign transitions.

New author-side conditional all-integer theorem: D_38(k)>0 for 1<=k<=12 and D_38(k)<0 for all k>=13 (r=27 permanent negative tail). With R514: D_37(k)>0>D_38(k) for 13<=k<=22.

Reproduce node R515_VERIFY.js > R515_EVIDENCE.json (76 integer Newton coefficients; 229-point identity, shifted k=13 all 76 coefficients strictly negative; 12 positive finite values; 20 original 38x38 Bareiss; 760 signed BRC comparisons). Independent: python R515_INDEPENDENT.py > R515_INDEPENDENT_EVIDENCE.json (12 direct SymPy Berkowitz 38x38 determinants, including k=12/13 boundary).

Next independently executable unit: s=3,m=39 all-positive-integer sign classification via degree<=234; 78 Newton coefficients and 235 exact identity points. Additional structural problem: derive leading dominant-pole and phase explanation at k=12,13,22,23 without modifying the frozen scientific pin.

Author-side draft, not native Result/Driver acceptance. The native control endpoint was checked in this turn: em_control_tasks=CONTROL_QUOTA; em_session_start=STATIC_READONLY_SCOPE_DENIED (operation_sent=false). GitHub actor awdawmip with admin permissions; PR #1708 is project Source handoff, not research CLAIM.
