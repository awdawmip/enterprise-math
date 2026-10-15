# Independent exact checks, 2026-10-15 (unreviewed)
Symmetric two-belief full public-policy DP, with feedback branching and labelled positive-support sources, gives:
n=5 Q=1,T=3: first depth 5, 258 memo states.
n=5 Q=2,T=3: first depth 5, 280 memo states.
n=6 Q=1,T=3: first depth 6, 588 memo states.
n=6 Q=2,T=3: first depth 6, 667 memo states.

Independent oriented exact BFS states (X safe/Y unsafe; Y safe/X unsafe):
n5 Q1: 589 / 743
n5 Q2: 848 / 688
n6 Q1: 3139 / 4477
n6 Q2: 5549 / 4487

Spine simulation terminal paths (X safe-path total and unsafe count; Y path total and unsafe count):
n6 Q1: X 5525/0; Y 5141/24.
n6 Q2: X 3125/0; Y 3605/120.
Explicit n-step strategies checked using source-set bitmasks for n=3..12,Q1 and n=2..12,Q2.

Finite n6 checks address only two specified state pairs, not universal H6 upper bound.
Local archive SHA256: 9aafec0e47474ccc6d39434d080d33840e3e5450f6cb034a3acf1fb756ec3c2a.
