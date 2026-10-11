# J1 k=2048: global exact minimum for singleton T observations (author-side finite certificate)

Status: **AUTHOR_DRAFT / EXTERNAL_FINITE_FIELD_AUXILIARY / UNREVIEWED / NOT_ADMITTED**. No formal CLAIM, Result, Driver review, P000-native transfer, or change of owner is asserted. The native identity check returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE`; current owner was not confirmed. Local activity registration attempted but was blocked by platform safety checks.

Read pins: GLOBAL_KNOWLEDGE_V1 main@330b2c1378bf343fb35d70425573cae9aa2070f2; Enterprise Math main@3096803ff631f25bbb829d246593e35e0197c1a2.

## Statement
For `1<=j<=2048` let `D_j=(2j-1)^2+32768`. The frozen 69 pairwise disjoint odd-length square-product relations determine U (499 labels), with complement T (1549 labels). For primes with no D_j divisible by p let `P(p)=#{j:(D_j/p)=+1}`, `Y(p)=4P(p)`. `O_a` fixes exactly one positive symbol, at a in T.

New **global singleton** result:

`min_{a feasible} min_{p:O_a} Y(p) = 424`.

Exactly 1528 singleton labels are feasible. **Only a=1963 can attain Y=424**; for every feasible a!=1963 the new result proves `Y>=472`. The full character vector previously constructed for a=1963 achieves P=106, so infinitely many nondegenerate primes attain the bound by CRT/Dirichlet.

## Evidence and proof
All squarefree D rows were re-factored from the 2048 input integers (1656 odd prime features); rank(all)=1655 and rank(T)=1546. Modulo span(T), 86 of 499 U signs are forced; the other 413 U signs fall into 227 nonzero quotient classes r.

For each fixed feasible singleton a, the exact positive-branch identity is
`P=P_floor(a)+sum_r w_r e_r`, with `w_r=|n0_r-n1_r|`, `e_r=1[x_r != preferred_r]`, and `P_floor=1+forced_U_positive+sum_r min(n0_r,n1_r)`.

A parity-odd XOR cycle C has XOR of quotient classes zero and XOR of preferred bits one, so `sum_{r in C} e_r>=1`. Nonnegative rational cycle weights lambda_C satisfying `sum_{C contains r}lambda_C<=w_r` certify `P>=P_floor+ceil(sum_C lambda_C)`. **47 new exact rational certificates** have been checked for the representatives of the previously unresolved 58 exceptional singleton labels; the smallest new certified lower bound is `Y>=472` at representative a=288. The remaining 57 exceptional labels have certified lower bound >=488 via their 46 representatives and verified linear-character gauge relations.

The representative lower-bound histogram is 472:1, 488:2, 496:10, 504:18, 512:9, 520:3, 528:1, 536:1, 544:2 (47 total). Every rational cycle weight, XOR parity, positive width, and integer capacity was verified with a separate `sympy.factorint`/high-pivot checker, not trusted from the SciPy LP finder. Gauge equivalence was independently checked for all 58 labels. This leaves the prior 1466 gauge-shift+4 states (exact Ymin=496), 2 gauge-shift+12 states (exact Ymin=504), plus previously independently rechecked exceptional a=1963 (exact 424) and a=1192 (exact 536). This covers all 1528 feasible a.

## Replication and scope
Local evidence package: `em4_j1_k2048_global_singleton_min_20261012.zip`, SHA-256 `fda185154a5650a57174935b6d59c136bb2a867196afd31155607bb99453495c`. Includes `PROOF.md`, `LP_47_CERTIFICATE.json` (all selected rational XOR cycles), original input relation and witness files, `verify_lp47.py`, `prior_shift_verifier.py`, independent audit and manifest. Both local verification programs PASS. ZIP not fully persisted in Source by this note; local exact bytes remain the source of its certificate.

This concerns external finite-field observer Y, with labeled positive branches and algebraic phase constraints. The original J1 `E=Y` mapping is inherited, not re-proved; the unconditional J1 escape lower bound 276 is unchanged. This does NOT imply a theorem in native P000 six-dimensional Cell space.

Next smallest scientific unit: close the exact per-observer minimum for a=288 (new certified Y>=472), by constructing a matching 1656-bit attainable character or stronger parity dual. Only then approach double-positive T observations to seek unrestricted bounds.
