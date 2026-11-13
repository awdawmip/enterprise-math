# R703 — Marked-source repair of R702 BRC moments

Date: 2026-11-11 Asia/Shanghai. Evidence: author-side mathematical proof and exact `Fraction` computation. Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, immutable publication `TP2-8B7E13C5904A2D6F1142`. Frozen X6/P000 scientific input: `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Precursor R702 author evidence `f1163f26b4eff01fd20a31303381ec903667b1c3`. This is a scoped candidate positive-BRC source-gate model, not native triadic/V29/V39 mechanics.

## Statement of the problem

The 60 distinct four-step return-path source labels in R699 phase (a,b)=(0,0) are partitioned into classes `L_e,L_t,L_c,L_z` with caps `N=(24,18,6,12)`. An active mask x assigns each label a Boolean bit. Its histogram is v=(e,t,c,z). Define s=e+t+c+z, W=96e+5t+92c+47z, and the unnormalized positive BRC moments M0=s/60, M1=W/60. R702 proved these two moments uniquely decode every legal histogram and are future-sufficient under the full within-class source permutation group G = S24×S18×S6×S12.

Select one **named** source q in L_e. Let b=x_q and h=e-b. Choose q with rational probability alpha and choose any other of 59 labels with beta=(1-alpha)/59, toggling that source's active bit. Assume 0<alpha<1 and alpha≠1/60. This event is a positive rational, provenance-labeled BRC choice; alpha+59beta=1.

## Theorem A — A sharp one-event collision witness

The unmarked two-moment state (M0,M1) is **not** sufficient for future four-group count distributions under the biased gate operation. Take mask x with only q active, and mask y with only a different r∈L_e active. Both have v=(1,0,0,0), s=1, W=96 and moments (1/60,96/60). But

`P_x(e_next=0)=alpha`, while `P_y(e_next=0)=beta`.

They differ precisely when alpha≠1/60. The concrete α=1/2, β=1/118 witness has values 1/2 and 1/118, difference 29/59. Thus the same historical moment state produces different one-step future laws. The R693 candidate static private-middle-port realization permits both source masks while keeping shared end ports open, but the new biased toggle is **not** asserted to be an admitted live native port operation.

## Theorem B — Exact minimal repair and strong lumpability

Set `G_q = Sym(L_e\\{q}) × Sym(L_t) × Sym(L_c) × Sym(L_z)`. Its mask orbits are exactly the states

`(b,h,t,c,z) ∈ {0,1}×{0,…,23}×{0,…,18}×{0,…,6}×{0,…,12}`.

The biased kernel is equivariant under G_q; the sum of its next-state probabilities over any orbit depends only on the initial orbit. The usual group-orbit argument therefore proves strong lumpability, including the joint law of all finite future count histories.

The complete exact reduced transition kernel has these nonzero possibilities:

- b→1-b with α;
- h→h+1 with β(23-h), or h→h-1 with βh;
- t→t+1 with β(18-t), or t→t-1 with βt;
- c→c+1 with β(6-c), or c→c-1 with βc;
- z→z+1 with β(12-z), or z→z-1 with βz.

All terms have nonnegative rational mass, zero branches are omitted, and the total equals α+59β=1. Source identity remains in the unquotiented BRC layer.

The marked BRC moment `B_q=b/60` repairs the observer: `(M0,M1,B_q)` decodes the complete quotient state, since (s,W) decodes v by R702 and h=e-b.

**Minimality for future group counts.** States of different v are separated at horizon zero. States of the same v but different b are separated in one step, since

`D_e(v,b)=P(e_next=e-1)=αb+β(e-b)=βe+(α-β)b`.

The coefficient α−β=(60α−1)/59 is nonzero. Hence all G_q-orbits are precisely the future-observational equivalence classes, proving a *sharp* observer-minimal quotient for this operation. An exact known-rate downward transition probability recovers `b=(D_e−βe)/(α−β)`.

The number of observer states is `2×24×19×7×13=82,992`. The optimal fixed-length code requires `ceil(log2(82992))=17 bits`, exactly one more bit than R702's 43,225-state histogram quotient. The explicit rank `((((b*24+h)*19+t)*7+c)*13+z)` ranges from 0 to 82991; successive quotient/remainder operations invert it. This is a code for the declared future count observer, not an all-purpose compression of original path/port history.

## Theorem C — Exact return law and source-count expectation

From the all-off mask, return to all-off in two steps requires selecting the same label twice. Therefore

`P(X2=X0)=alpha²+59 beta²`.

At alpha=1/2 and beta=1/118 this equals `1/4+1/236=15/59`. For every integer n≥0, the parity law for independent draws gives the exact expected active count

`E[s_n]=[1−(1−2alpha)^n]/2 + (59/2)[1−(1−2beta)^n]`.

At alpha=1/2 and n≥1: `E[s_n]=1/2+(59/2)[1−(58/59)^n]`.

## Verification, inference boundary, continuation

The accompanying stdlib Python `Fraction` checker enumerates all **82,992** five-tuple states, verifies rank/unrank, unique (s,W,b) signatures, exact normalization of every reduced transition row, and the two-mask future-law witness. An independent sparse exact rational dynamic program checks times n=0..8 against the analytic expectation and verifies P(return at two)=15/59. The script prints `R703_MARKED_BRC_LUMPABILITY_EXACT_PASS`; the JSON evidence retains exact results and the coverage.

This theorem applies to R702's **candidate** labeled source Boolean gate dynamics. It does not prove genuine X6 Link/Port occupancy transitions, P000 TRIADIC_CLOSURE_E, V29 PASS/TRANSFER, V39 loop current j, primitive rotation transport, or a physical heartbeat interval; no Source Result/Driver acceptance is presumed.

Next distinguishing experiment: read an exact frozen legal decorated X6 Cell/Link/Port occupancy event and find two packets with the same (M0,M1) but distinct next class/triadic observations. Determine whether one marked port suffices, or whether correlated port plus V29/V39 interaction data are necessary. Transport the label q along the allowed axis action before testing covariance; retain full ordered path provenance upstream.
