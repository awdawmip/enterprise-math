# EC49V — exact information-strength envelope and fixed-cost separation

Status: **AUTHOR-PROVED / EXACT-FRACTION-CHECKED / UNREVIEWED / NOT-ADMITTED**. Scientific parent: EC49U, Draft PR #1668, immutable commit `b2ce9c962ffb662f31fb1166c5c2641f1eb0fa2b`. This is a portable author-side research result, not a canonical Task, CLAIM or Result.

## Frozen finite positive-weight BRC observer

Preserve `W=Z={0,1,2}`, `U={0,1}`, `sigma=(1,0,-1)`. Source laws: `Q(w,z)=1/9`; `P(w,z)=1/6` if `z=w`, otherwise `1/12`; `t_w(u)=1/2+(2u-1)*eta*sigma_w`.
The atom is `R(w,u,z)=R(w,z)t_w(u)`, so each source has 18 positive leaves for `0<=eta<1/2`. Rational eta gives strictly positive rational leaves. Difference of source **readout probabilities**: `Delta(w,u,z)=t_w(u)(3*1[z=w]-1)/36`. Do not identify it with native signed BRC amplitude.

Compressed observer knows W only before choosing STOP or action A (cost 1) / B (cost 2), and a one-bit memory D. W is then forgotten, while the observer remembers (A/B,D), sees U, may buy S (cost 1) and see Z, and accepts/rejects using retained state and observation. The full-history observer retains W. Both may use independent, source-blind, real-valued behavioral randomization; **no retained shared seed**. Define alpha=P(accept), beta=Q(accept), and two stage costs C1,C2, identical for both sources because P(W,U)=Q(W,U). `H=alpha-beta-(C1+C2)/18`.

## Theorem 1: exact H support for every real 0<=eta<1/2

\[
\boxed{\sup_{\mathrm{compressed}} H = \max\{1/27,\;\eta/6-1/36\}.}
\]
The sole interior crossover is **eta=7/18**. For `eta<=7/18` the optimum is `1/27`; for `7/18<=eta<1/2` it is `eta/6-1/36`. Both values are attained by deterministic admissible controllers. In particular `h(1/200)=1/27` and `h(5/12)=1/24`.

**Proof.** For a fixed finite acyclic protocol, H is separately affine in each behavioral decision probability; a maximum exists at a deterministic vertex. Before S, P and Q agree, so early acceptance has zero discrimination advantage and paid actions that never buy S can be replaced by STOP without decreasing H. A deterministic prefix maps each W into exactly one of `STOP,A0,A1,B0,B1` (125 choices).

For a nonempty fiber F of histories producing the same action/memory code and U=u set
\[
D_{F,u,z}=\sum_{w\in F}t_w(u)(3\mathbf1_{z=w}-1)/36,quad M_{F,u}=\sum_{w\in F}t_w(u)/3.
\]
The exact optimal post-U surplus from S and terminal acceptance is
\[
G(F)=\sum_{u=0}^1\Big[\sum_{z=0}^2[D_{F,u,z}]_+-M_{F,u}/18\Big]_+.
\]
The full fiber contribution is `V_A(F)=G(F)-|F|/54`, `V_B(F)=G(F)-|F|/27`. All seven nonempty fibers give the following **exact** table (each expression on its stated eta interval):

| F | G(F) |
|---|---|
| any singleton | 1/27 |
| {0,1} or {1,2} | 1/54 for eta<=1/4; 1/216+eta/18 for eta>=1/4 |
| {0,2} | 1/54 for eta<=1/6; eta/6-1/108 for eta>=1/6 |
| {0,1,2} | 0 for eta<=1/3; eta/6-1/18 for eta>=1/3 |

Direct derivation: singleton has positive Delta only at z=w and sum_u t_w(u)=1. Adjacent pairs have z-coefficients `(2t_a-t_b)/36`, `(2t_b-t_a)/36` with sign switch at eta=1/4. Pair {0,2} has `t_0+t_2=1` and z-coefficients `(1/2 +/- 3eta)/36`, switch at eta=1/6. The triple positive signed contribution per u is `eta/12`, while S penalty is `1/36`, giving eta=1/3. The displayed positive-part formula now gives the table exactly.

Every B fiber is nonpositive on eta<1/2 (singleton 0); A adjacent pairs and the triple are strictly negative; a singleton A gives exactly `1/54`; the only other potentially positive A fiber is {0,2}, giving `eta/6-5/108` for eta>=1/6. There are just two A memory codes. Therefore the only maximizers are two A singleton fibers (value 1/27), or A fiber {0,2} plus A singleton {1} (value `eta/6-1/36`). Both are implementable without shared seeds. Their crossover gives 7/18. This proves the all-real result; finite checks are corroboration, not extrapolation.

The executed pure-Fraction complete affine-arrangement verifier (see linked evidence archive) checked 125 prefix assignments, 14 fiber/U cases, eight independent terminal acceptance masks per local case, 9 local mask cells and 13 upper-envelope subcells; it returned exactly the two displayed segments. `REPRODUCE.py` also executes the independent parent verifier at hard rational points.

## Theorem 2: a stronger cost-face separation

For every real `0<=eta<=1/6` and every legal compressed behavioral controller:
\[
\boxed{J:=\alpha-\beta-(C_1-C_2)/6\le 1/9.}
\]
**Proof:** After paying for A or B, buying S weakly improves J: it adds a nonnegative optimally selected P-Q acceptance difference and adds the positive term C2/6. Thus assume S always follows purchases. For any nonempty fiber, its best acceptance advantage is `B(F)=sum_{u,z}[D_{F,u,z}]_+`. At eta<=1/6 every singleton and every pair has B(F)=1/18, while the triple has B(F)=eta/6<=1/36. An A fiber contributes B(F); a B fiber contributes `B(F)-|F|/18<=0`. Two A codes give at most 2/18=1/9. Deterministic vertex reduction covers all real behavioral kernels, and two A singleton fibers attain equality with unconstrained costs.

At `eta=1/200`, fix `C1=43/48`, `C2=7/8`. Then
\[
\alpha-\beta\le 1/9+(43/48-7/8)/6=\boxed{11/96}.
\]
The full-history rational witness from EC49U has `(alpha,beta,C1,C2)=(7/16,7/24,43/48,7/8)`, hence discrimination `7/48`. Thus **the fixed-cost discrimination gap is at least 1/32**, strengthening the earlier unrestricted-H certificate gap 1/96.

The bound 11/96 is **sharp for the convex hull** of compressed outcome vectors: mix deterministic all-S prefixes `(STOP,A0,A1)`, `(A0,A0,A1)`, `(A0,A1,B0)` with probabilities `3/8,9/16,1/16`. Their `(C1,C2,alpha-beta)` triples are `(2/3,2/3,1/9)`, `(1,1,1/9)`, `(4/3,1,1/6)`. The weighted mean is `(43/48,7/8,11/96)`. **This shared-seed mixture has NOT been proved implementable by the original 1-bit behavioral controller.** Convex hull and behavioral feasibility are not interchangeable.

A legal, source-blind, genuinely behavioral witness at eta=1/200 is: W0->A0; W1->A1; W2->STOP with prob 3/8, A0 with prob 9/16, B0 with prob 1/16; always buy S after A/B; A0 accepts z in {0,2}, A1 accepts z=1, B0 accepts z=2. It uses no retained W after erasure and no shared seed, and yields
\[
(C1,C2,\alpha,\beta,\alpha-\beta)=(43/48,7/8,109/192,67/144,59/576).
\]
Hence the **exact unknown behavioral cost-face maximum** lies in `[59/576,11/96]`. The full achievable (alpha,beta) section also remains OPEN. `REPRODUCE.py` checks the rational values with direct source atoms; detailed independent fraction calculations remain in the evidence archive.

## Type, authority and admission scope

Positive-weight branch BRC auxiliary observer only, not native signed/complex BRC amplitude or physical X6. Sensor cost is not heartbeat time. P000 and ACTIVE worldview were read but not modified. Any X6 translation needs typed carrier, embedding, readout, and relation-preservation proof. Native control owner query was denied `CONTROL_QUOTA`; native `session_start` was denied `STATIC_READONLY_SCOPE_DENIED`. No official session/CLAIM/Result, independent Driver review, or theorem admission is claimed.
