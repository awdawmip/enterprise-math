# Stage213 — full-real optimal segment in external ternary IID N=14

**2026-10-28 classification: PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.** This author result is for a finite IID model; it is neither a P000 native-X6 Cell theorem nor an independently accepted Source Result, Driver review or Lean proof.

## Exact statement

Observe any ordered ternary history up to N=14 under P=(3,1,20)/24 or Q=(2,2,20)/24. Allow arbitrary full-history stopping and P/Q decisions with real randomization. Let eP=P(declare Q), eQ=Q(declare P), tP=E_P τ, tQ=E_Q τ, V14(α)=inf max(tP,tQ) subject to eP,eQ≤α.

Predecessor Stage212 supplies the proven left endpoint α212=3740051857643324945/10517860061584293888 and V212=2098901961222753173/219122084616339456. Put

\[
K_{213}=\frac{36993328266365208}{365083984886815},\qquad
H_{213}=\frac{326557453975807110989706851827603}{3999898191421953578095588933632}.
\]

**Theorem:** for **every real** 0≤δ≤1825419924434075/2629465015396073472, including irrational values,

\[
\boxed{V_{14}(\alpha_{212}+\delta)=V_{212}-\frac{73986656532730416}{365083984886815}\delta}.
\]

New right endpoint:

\[
\boxed{\alpha_{213}=\frac{3747353537341061245}{10517860061584293888}},\qquad
\boxed{V_{213}=\frac{2068074187667448833}{219122084616339456}}.
\]

## Universal lower bound (all ordered histories)

At ordered history h let s=(n,a,b) denote length, zero count and one count. IID positivity gives exact ρ(s)=Q(h)/P(h)=2^(a+b)/3^a. Under P-normalization of tP+K(eP+eQ), the Bellman equation is

\[
B(s)=\min\{K\rho(s)\ [P],\ K\ [Q],\ 1+\sum_j P_j B(\operatorname{child}(s,j))\ [\text{continue}]\},
\]

omitting continue at n=14. For any full-history randomized competitor, condition on each actual ordered history. The same IID suffix and likelihood ratio applies, and randomization cannot improve on the minimum. The exact 680-state recursion yields B(root)=H213, exactly 1238 strictly positive action gaps (minimum 3314488625691065/141944653323993672), and exactly two tied states: W=(2,0,1) Q/continue and Z=(14,0,0) terminal P/Q. Therefore V14(α)≥H213−2K213α universally.

## Primal equality on the entire real interval

At W declare Q with probability u∈[0,1], otherwise continue; at Z declare P with probability z∈[0,1], otherwise Q. Elsewhere take the unique Bellman-minimizing action. Define O=(eP,eQ,tP,tQ). The exact four-corner computations imply

\[
O(u,z)=O_0+uD_W+zD_Z+uzM
\]

with components:

    O0 = (667518608447166299/1752976676930715648,
          106048341815297/320979616137216,
          2098901961222753173/219122084616339456,
          235093231565585/26748301344768)
    DW = (680646679824515/146081389744226304,
          -524951195555/160489808068608,
          -2568981129608695/18260173718028288,
          -2967572847565/13374150672384)
    DZ = (-6103515625/78364164096,
          6103515625/78364164096, 0, 0)
    M = (0,0,0,0)

M vanishes structurally: W has one symbol-1 occurrence, Z has zero, and counts are monotone. W cannot reach Z; Z is terminal and cannot reach W. The two coins cannot interact on a single live ordered path. Independent exact Fraction suffix DP and unmerged ordered integer-P/Q-mass DFS agreed on all four deterministic corners with 39451, 39451, 32779 and 32779 visits respectively, total **144460**.

Solving eP=eQ gives the exact affine error-balancing law

\[
\boxed{z(u)=\frac{265059793039672849}{819200000000000000}
 +\frac{2085244062481439}{40960000000000000}u}.
\]

For all real u∈[0,1], 0<z(0)<z(1)=306764674289301629/819200000000000000<1. The common error increases affinely from α212 to α213, and endpoint expected-time gaps are exactly

    (tP−tQ)|u=0 = 173018208237480853/219122084616339456
    (tP−tQ)|u=1 = 190811148216681473/219122084616339456

both strictly positive. Affinity gives tP>tQ throughout. Since all selected actions attain the Bellman minimum, tP+K213(eP+eQ)=H213, and hence max(tP,tQ)=tP=H213−2K213α. The universal lower bound is reached at each real α in the closed interval, completing the claimed exact theorem.

## First-switch dual-only candidate Stage214

A separate exhaustive first-switch scan yields K214=265549752/2687315 and H214=2351021677817497415171339/29442503241037913260032, new Q/continue tie at (7,2,2) and terminal P/Q tie Z. There are 680 states and 1238 strictly positive gaps, minimum 1026961/348276024, and the exact contact identity

\[
H_{214}=H_{213}+2\alpha_{213}(K_{214}-K_{213}),\quad K_{214}<K_{213}.
\]

For every α>α213, this new dual bound exceeds the **fixed Stage213 supporting line** by

\[
\frac{985905721704699046656}{196219133769222250345}(\alpha-\alpha_{213})>0.
\]

This does **not** prove Stage214 primal optimality.

## Executions, source pins, typing and remaining obligations

Actual author execution: verify_stage213.py → STAGE213_AUTHOR_EXACT_FULL_REAL_PASS 144460; standalone compact REPRO_STAGE213.py → STAGE213_REFERENCE_EXACT_PASS 144460, published Git Blob 7f04c12e3f44a000c97e3bc72f005af8e4f91654. Independent certificate-only algebra audit (not independent mathematical review) → STAGE213_INDEPENDENT_CERTIFICATE_ALGEBRA_PASS. scan_stage214.py → STAGE214_DUAL_SCAN_PASS, Git Blob bd088dd8daae710f7e083e87ae3f603fb7c1217c. Original executed sources, full corner certificates, logs and SHA256 manifest are in portable evidence archive EM_STAGE213_AUTHOR_EXACT_PORTABLE_20261028.tar.xz, SHA256 631b0954cf36855791f8e50a118f6f43d790da6624f3627489f0b7aebe4ec172. All arithmetic is exact rational/integer, not grid sampling; no GitHub-hosted execution is inferred from storage.

P000 and ACTIVE Heartbeat World remain a six-dimensional discrete native X6 Cell space plus separately typed time, not reinterpreted by this external IID model. The typed BRC contribution is provenance-preserving positive rational mass with separate P/Q measures and a justified IID count suffix observer. There is no native-X6 embedding/readout/operation-preservation theorem, physical claim, phase cancellation, independent Driver acceptance or Lean formalization.

Frozen canonical reads for this author scope: GLOBAL_KNOWLEDGE_V1 main@6b3e7a6520898c41e063db04e82b1d3c2c9c3a4b; Enterprise Math main@d42136a33bab42ab25e6d4318774708be2544d62; P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matching startup projection. Stage212 predecessor author proof commit c84a8e5c9752fe1d938e51923cce2799638eab28. Native active-owner query returned CONTROL_QUOTA; em_status advertised research_authority_granted=false; no formal CLAIM/Result or mathematical admission is implied.

**Next math:** establish Stage214 primal four-corner full-real witness or exact rational obstruction for ties (7,2,2) Q/continue and Z terminal P/Q. Preserve branch/P-Q mass identity, exact coin feasibility and time dominance; do not replay Stage213.
