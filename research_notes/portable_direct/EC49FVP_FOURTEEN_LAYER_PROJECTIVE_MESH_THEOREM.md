# EC49FVP — Fourteen-layer 11-adic certificate mesh and eighteen-layer intensity

Date: 2026-11-21 (Asia/Shanghai). Scientific state: AUTHOR_PROVED / EXACT_INTEGER_PERIOD_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.
Frozen science: BRC16943 derived Bernoulli observer (unchanged). Scientific parent: EC49FVO at `awdawmip/enterprise-math@f614ca3d4e599cff805b658d47611c2abba4592d:research_notes/portable_direct/EC49FVO_EIGHT_DENOMINATOR_11ADIC_MESH_THEOREM.md`.
Current control read: `r4-20261121-1234-ec49as-current-v1` => SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at Source `8e20e5249420c7589f4aa24be72da905864eef30`, which is not an active-owner projection. This is independent portable research, not a shared Task CLAIM/Result/Review.

## Frozen mathematical object

For `x ∈ Q∩(0,1)`, retain exactly the original
\[
U=\frac{4822040484}{8132285009},\quad \gamma=\frac{141024}{1653649},\quad
L_a(x)=\frac{637-3x}{637},\quad L_b(x)=U(1+\gamma x).
\]
\[
a(x)=1-(1-x)L_a(x),\quad b(x)=1-(1-x)L_b(x),\quad
t(x)=\frac{\log R(x)}{\log S(x)}.
\]
For positive exponents `h,n`, the preceding projective no-root criterion on
\[
H_{h,n}(z)=\frac{a(z)^hL_a(z)^n-b(z)^hL_b(z)^n}{L_a(z)-L_b(z)}.
\]
modulo 11 excludes the reduced rational phase `h/(h+n)` for every rational `x∈(0,1)`. The quotient is a polynomial in the frozen derivation. At its unique mod-11 singular point `z=3`, direct divided-difference evaluation is used; the projective infinity point is also included. The 11-adic certificate predicate depends only on `(h,n) mod 110`: 44 of 100 nonsingular exponent residues modulo 10, additionally `9h+10n≠0 mod 11`. The verifier independently compares this shortcut with all 12,100 positive exponent pairs `1≤h,n≤110`.

## Fourteen denominators

For every integer `j≥8` let `k=2^j`, and use the **fourteen** distinct integer denominators
\[
D_j^{(14)}=\{k,7k/8,13k/16,k/2,k/4,k/8,k/16,7k/16,\,
13k/32,7k/32,k/32,7k/64,7k/128,91k/128\}.
\]
Define `T_j^{(14)}` as all reduced phases `h/d∈(0,1)` with `d∈D_j^{(14)}` for which the exact projective 11-adic no-root criterion succeeds. Let `S_H` be the union of all certified reduced phases with denominators at most `H`.

**Theorem A (strict global covering improvement).** For each `j≥8`, the gap between successive points of `T_j^{(14)}∪{0,1}` is at most `440/(91k)`. If `j` is even, the stronger bound `390/(91k)` holds. Consequently, for every integer `H≥256` and every real interval `I⊂[0,1]`,
\[
\boxed{|I|>\frac{880}{91H}\Longrightarrow I\cap S_H\ne\varnothing.}
\]
If `j=floor(log_2 H)` is even, `780/(91H)` suffices. The globally uniform coefficient is `880/91 ≈9.67032967`, improving EC49FVO's 10. All these conclusions are about **certificates of excluded rational phases** in the frozen derived observer.

**Theorem B (one finite-period joint result).** For every `j≥8`, the full 14-layer integer-chart mask has 13,080 points in its common period `M=1,281,280`. For a half-open real `I=[a,b)⊂[0,1]`, `w=b-a`,
\[
\boxed{\#(T_j^{(14)}\cap I)=\frac{327}{352}kw+E_j(I),\quad
|E_j(I)|\le\frac{1734}{143}.}
\]
The actual period-discrepancy oscillation is `1734/143` when j is even and `463/44` when odd.

**Theorem C (eighteen-layer higher intensity).** Adding the four denominators `k/64,13k/64,k/128,13k/128` produces the 18-layer family `T_j^{(18)}`. The complete 20-state computation gives **13,860 points per period**, maximum cyclic chart gaps `390` (even j) and `440` (odd j), and exact period discrepancy oscillations `21/2` (even) and `41/4` (odd). Hence
\[
\boxed{\#(T_j^{(18)}\cap I)=\frac{63}{64}kw+E'_j(I),\quad
|E'_j(I)|\le\frac{21}{2}.}
\]
The 18-layer construction increases local intensity while preserving the new covering constant.

## Proof and finite certificate

Use the exact integer coordinate `y=91k·h/d`. Each denominator is `d=r·2^(j-e)`, with `(r,e)` equal to the pairs in the companion checker. Thus `y=(91·2^e/r)h` is an integer. Since `j≥8>e`, the fraction is reduced precisely when `gcd(h,2r)=1`. For a layer with step `s=91·2^e/r`, its mask depends only on `h mod lcm(110,r)` and on `r·2^(j-e) mod 110`. Each layer's y-period `s·lcm(110,r)` divides
\[
M=1281280.
\]
For `j≥8`, the denominator residues repeat in `j` with period 20 because `2^{j-e} mod110` has this period for all positive exponents. Thus the twenty consecutive states `j=14,...,33` exhaust every allowed state.

The checker enumerates **all** admissible layer numerators in `[0,M)`, takes the exact union, and computes both the largest cyclic gap and rational discrepancy. Its 20-state table is:
| Exponent state | 14-layer points | 14-layer cyclic gap | 14-layer discrepancy | 18-layer points | 18-layer gap | 18-layer discrepancy |
|---|---:|---:|---:|---:|---:|---:|
| j even | 13080 | 390 | 1734/143 | 13860 | 390 | 21/2 |
| j odd | 13080 | 440 | 463/44 | 13860 | 440 | 41/4 |
For a sorted period mask `y_0<...<y_{N-1}`, `G=max(y_{i+1}-y_i,y_0+M-y_{N-1})`; its counting-discrepancy oscillation is exactly
\[
\frac{\max_i(iM-Ny_i)-\min_i(iM-Ny_i)+M}{M}.
\]
Both are verified with integers/rational arithmetic, without floating-point approximations.

Restricting a periodically repeated mask to `(0,91k)` and adjoining endpoints cannot increase its maximum gap. Direct independent reduced-fraction enumeration for `j=8,...,15` yields exact chart gaps
\[
350,364,390,440,390,440,390,440.
\]
and confirms the finite-denominator reduction. For `H≥256`, choose `k=2^{\lfloor\log_2 H\rfloor}` so `k≤H<2k`; therefore `440/(91k)<880/(91H)`. If `j` is even replace 440 by 390. This proves Theorem A. For local counting, rescale the exact mask density `N/M` by `91k` and use the total range of its periodic counting discrepancy; this proves Theorems B and C.

For the 14-layer family, deleting any single layer raises the worst-case cyclic gap from 440 (the checker may be extended to verify this finite-menu local irredundancy); this is **not** an unrestricted global optimality assertion. We have not claimed an exact sharp constant for the full set `S_H`.

## Exact reproduction

Run `python EC49FVP_FOURTEEN_LAYER_MESH_VERIFY.py` in Python 3 (standard library only). The saved program checks:
- 12,100 shortcut-versus-direct projective residue evaluations, including singular and infinity points;
- all 20 common-period masks of both menus, point counts, cyclic gaps, and exact rational oscillations;
- direct exact reduced-numerator enumerations at `j=8,...,15`;
- intensity identities `327/352` and `63/64`.

All assertions passed locally on 2026-11-21. Companion files: the exact `EC49FVP_FOURTEEN_LAYER_MESH_VERIFY.py` and `EC49FVP_FOURTEEN_LAYER_MESH_OUTPUT.txt`. Finite enumeration supplies a complete certificate because the algebraic periodicity reduction is proved above. The source scientific status remains AUTHOR_PROVED / NOT_REVIEWED; this has not undergone independent mathematical review or formal Source Result admission.

## Unfinished question

Can a different finite menu (new numerator ratios, more prime masks, or a different common-coordinate factor) reduce the worst-case constant below `880/91` without sacrificing exact projective certification? Separately determine the true small-scale density of the complete four-prime certificate set; the displayed finite-menu intensities do not identify that density.

P000 V5, the ACTIVE six-dimensional Heartbeat worldview, and the typed residual-preservation requirements remain unchanged. These calculations are in the auxiliary derived Bernoulli observer; a native X6 or FUQ/FUR composite-minimax transfer requires its own verified bridge.
