# R5 — Third signed-eta phase coalescence (exact follow-on)

**Date:** 2026-11-12. Researcher-side exact finite proof; same frozen P/Q–BRC 28-mass auxiliary observer, 15 labeled moves, full 28-coordinate constraints and original scientific pins as `RESEARCH.md` in this folder. No P000/native-X6 change.

With `x=155682221/25142124560000000`, `eta_2^+=x/9959`, `eta_2^-=-x/9913`, the *next (third)* collisions between a moving `t_q(eta)=(x-23eta)/q` and the finite original target-0 fixed spectrum are:

| Sign | Third eta | Merged phase epsilon | Active collision |
|---|---|---|---|
| positive | `eta_3^+=x/6233=155682221/156710862382480000000` | `1401139989/3406757877880000000` | `t_15(eta)=36x/542` |
| negative | `eta_3^-=-x/6187=-155682221/155554324652720000000` | `1401139989/3381615753320000000` | `t_15(eta)=36x/538` |

The integer subset-sum collision equation `eta/x=(1-36q/k)/23` over `q∈{15,12,3}` and `k∈K` gives the initial signed ordering: for positive eta, `1/12443,1/9959,1/6233`; for negative, `-1/12397,-1/9913,-1/6187`. All six ratios lie strictly within the previously certified affine minimizing-coordinate stability radius `|eta|<x/4945`, so no other first-zero family intrudes before these events.

**Exact complete finite results:** Each third edge has 1,146 distinct interior first-zero phase values, while the open interval after the second edge and before the third has 1,147. At the merged edge the legal complete 15-atom order counts change:

| Edge | Newly zero masks | Legal before | Legal after | Loss |
|---|---:|---:|---:|---:|
| `eta_3^+` | **4,111** | 853,203,571,008 | 472,075,847,712 | **381,127,723,296** |
| `eta_3^-` | **4,110** | 849,160,117,200 | 468,299,290,272 | **380,860,826,928** |

Separately, at `eta_​inside=(999*eta_3+eta_2)/1000`, the two adjacent cuts give the exact ordered decomposition:

- Positive: fixed `k=542` first, **15** failing masks and **1,036,269,792** lost schedules; moving `q=15` second, **4,096** masks and **380,091,453,504** lost. Sum = **4,111** masks and **381,127,723,296** orders.
- Negative: moving `q=15` first, **4,096** masks and **379,627,579,392** lost; fixed `k=538` second, **14** masks and **1,233,247,536** lost. Sum = **4,110** masks and **380,860,826,928** orders.

The script `VERIFY_THIRD_COLLISION.py` imports the sibling standalone exact verifier `VERIFY_SECOND_COLLISION.py`, runs its 32,768-mask × 28-coordinate rational prefix tests and integer Boolean-lattice order-count recurrence at both signed third edges and neighboring rationals; the published local execution record is `THIRD_OUTPUT.txt`. It checks exact equality to the fixed-plus-moving phase set at the evaluated points, positivity, the unchanged maximal endpoint and the additive two-cut count. Full interval classification uses the earlier finite minimizer-switch certificate and ordered integer-collision ratios.

**Next scientific frontier:** continue to the fourth collision on each side, and audit the first genuine change of active minimizing coordinate at `|eta|=x/4945`; compare first-zero phase-value generation to the actual count of legal complete schedules. Formal Source scientific admission and independent mathematical review remain pending.
