# R100 — Exact dynamic gcd-period profile updates and cross-version witnesses

Date: 2026-11-12. Status: **author-side mathematical proof with exact finite implementation audit**; independent review pending.

Researcher: `EM-DIRECT-C1F646`; Activity: `RA-F1FCB0CBA8ECD3A606E6A30A` (registration independently verified).
Frozen scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: R99 scientific commit `53782564e40714c2bf5121a3c6bc84585e70e1f8`, specifically its exact rational circle-arc semantics and safe gcd period. The result is in the **auxiliary finite rational circular-source model**, not an alteration of P000 or native X6 geometry.

## Exact setting and typed source identity

A finite source set `E` contains complete identities `u=(t,branch)` with integer `t` and totally ordered integer branch, ordered lexicographically. Fix an observer signature `sigma=(j,x,a,b)` with `j,a,b in Z`, `x in Q`. At a real parameter `theta`, put
`s_t={x+(t-j)theta}`, `A={a theta}`, `B={b theta}`, where braces mean fractional part in [0,1).

`M_t(theta)` holds precisely when `s_t` lies on the directed **half-open** circular arc [A,B). The arc is empty if A=B. If A<B, membership means `A<=s_t<B`; if A>B, it means `s_t>=A or s_t<B`. Define `W_E(theta)=max_lex{u in E : M_{time(u)}(theta)}`, with `NONE` for empty selection. Branches sharing a time have equal membership but retain distinct identity and rank.

Let `g_E=gcd(|a|,|b|, {|t-j| : (t,branch) in E})`, taking an all-zero gcd as zero. For `g_E>0`, `P_E=1/g_E` is R99's certified period; for `g_E=0`, `W_E` is constant.

## R100.1 — Exact one-identity insertion, including a change of period

For `u=(t,b) not in E`, define `F=E union {u}`. For **all real theta**,
```
W_F(theta) = max_lex( W_E(theta), u if M_t(theta) else NONE ).
```
This is a pointwise identity: the eligible set for F is the union of the previously eligible set and (possibly) one identity. Therefore an **exact cached profile** of W_E and one exact membership profile for u suffice to build the complete W_F profile with no recalculation of the other old source memberships.

Moreover
`g_F=gcd(g_E,|t-j|)`.
If `g_E,g_F>0`, then `g_F divides g_E` and `P_F/P_E=g_E/g_F=:m` is a positive integer. On `[0,P_F]`, the cached W_E profile is periodically tiled exactly m times, then overlaid with u's membership. If g_E=0, W_E is constant and can be overlaid without tiling. If g_F=0 as well, both winner functions are constant.

Write `C_E` for the complete rational cut set (including endpoints) of a cached exact W_E profile on [0,P_E], and `C_u` for a complete exact membership cut set for u on [0,P_F]. When g_E,g_F>0, the updated profile is representable on the union of these cuts and uses no more than
```
m * (|C_E|-1) + 1 + |C_u|
```
distinct cuts. Overlap only improves the bound. At each cut and each intervening rational midpoint the max formula is exact. This is a structural **profile-size** bound, not an unmeasured wall-clock improvement.

## R100.2 — Exact single deletion using a cached top-two profile

Let `u in E`. Write `W_E^(1)(theta)` and `W_E^(2)(theta)` for the largest and second-largest *distinct complete* eligible identities, padding with NONE. Then, for every real theta,
```
W_{E\{u}}(theta) =
    W_E^(2)(theta)  if W_E^(1)(theta)=u,
    W_E^(1)(theta)  otherwise.
```
Proof: removing a nonwinner leaves the maximum unchanged; removing the current winner exposes the second identity. The identity statement includes duplicate times, including a lower-ranked branch at the same time.

The new `g_{E\{u}}` is recomputed from the remaining source times. When both gcds are positive, `g_E` divides `g_{E\{u}}`, so the new safe period is no longer than the old safe period. Consequently, restricting the old top-two profile to the new period and applying the formula yields an exact new winner profile. The top-two certificate is sufficient for **one** removal; an additional deletion may require a cached top-three profile or a rebuilding operation.

An ordered persistent gcd aggregation, maintaining `|t-j|` plus the fixed `|a|,|b|`, can compute version-specific g without losing branch provenance. The signed representation of the underlying source identity is never reduced to its gcd.

## R100.3 — Exact cross-version equality and rational discrepancy witness

For arbitrary finite versions E,F at the same observer sigma, define `h=gcd(g_E,g_F)`. If `h>0`, both `W_E` and `W_F` have common certified period `Q=1/h`, since `Q/P_E=g_E/h` and `Q/P_F=g_F/h` are positive integers whenever their individual gcds are nonzero. If either gcd is zero, that winner is constant. If h=0, both winners are constant.

On [0,Q], obtain the finite union of the two exact rational critical cut sets from R97/R99. The functions are constant on each open cut gap, and their exact values are defined at every cut. Hence:

* W_E equals W_F for every real theta **iff** their complete identities agree at every union cut and at one rational midpoint of each open gap.
* Otherwise a union cut or a rational midpoint supplies an exact rational witness of the mismatch.
* For any closed rational query interval I=[L,U], an exact discrepancy witness inside I is found by querying the translated interval when its width is smaller than Q; when its width is at least Q, take a witness z on [0,Q] and lift by `z + Q*ceil((L-z)/Q)`. This belongs to [L,L+Q] within I and preserves both winners.

For a short interval the translated critical partition must be recomputed (or restricted from a complete tiled profile); a discrepancy elsewhere in the full period alone does not prove a discrepancy on the short interval. Closed endpoints, isolated point changes, the empty-arc case and complete branch identities are included.

## Exact computation, scope and result

The Python standard-library `Fraction` checker generated 220 deterministic source histories with additions, exact observer signatures (including negative slopes and zero-slopes), duplicate-time branches and rational query intervals. For each version it built two exact **stored** periodic cut/midpoint profiles (top one and top two), compared the cached insertion/deletion algorithms with independent direct full-identity evaluation, and tested cross-version equality using the complete six-family cut union.

Results (seed 10020261112): 21,378 pointwise cached insertion checks passed; 21,378 cached deletion checks passed; 21,378 periodicity checks passed; 220 full-period version comparisons (146 changed; 74 unchanged) passed; 132 witnessed interval discrepancies were checked directly; 42 sampled histories contained same-time branch duplication. The direct rational critical partition independently checked the absence of an interval mismatch whenever no witness was returned. No floating point entered the mathematical assertions.

Reproduce: `base64 -d check_r100.py.gz.b64 | gzip -dc > check_r100.py`, then `python3 check_r100.py` from this directory. Expected banner begins `R100_PASS` and outputs `verification_r100.json`. This is a finite exact implementation audit of the all-real algebraic propositions, not an independent formal proof review.

## Next scientific frontier R101

Develop a persistent **top-k** circular profile and version-aware incremental certificate index (OUT rectangles) with an explicit amortized operation/bit complexity budget. Compare full rebuild versus tiled insertion or top-two removal over the same source-edit/query workload, including the gcd-period expansion factor, exact rational cut lengths, retained history memory, and witness recovery. In particular characterize when an inserted source enlarges the certified period so much that tiling is more costly than reconstruction. Retain R99's safe period as an upper-layer certificate rather than asserting it is minimal.

Formal source task `RS-S23-AV` returned `NO_CURRENT_IMMUTABLE_PUBLICATION` at this run's current exact control query. This work is durable author-side research only; no shared CLAIM or Result/review is asserted.
