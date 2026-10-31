# Stage212 — exact full-real optimum segment for external ternary IID N=14

**Classification (2026-10-28): PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.** This result is for a finite external IID sequential-observer model. It asserts neither P000 native-X6 Cell dynamics nor native Source Result/CLAIM/Driver mathematical acceptance.

## Model and theorem

Observe arbitrary full ordered ternary histories, under IID laws P=(3,1,20)/24 or Q=(2,2,20)/24, stop at τ≤14, and declare P/Q, with arbitrary history-sensitive real randomized choices. Let eP=P(declare Q), eQ=Q(declare P), tP=E_P τ, tQ=E_Q τ and V14(α)=inf max(tP,tQ) subject to both errors ≤α.

From Stage211, α211=3739617835243324945/10517860061584293888 and V211=2100773454342753173/219122084616339456. Define K212=626616/6055, H212=86217082286260423009/1036550173712449536 and Δ212=3311328125/80244904034304.

**Theorem:** for every real δ∈[0,Δ212], including irrational δ,

\[
\boxed{V_{14}(\alpha_{211}+\delta)=V_{211}-\frac{1253232}{6055}\delta}.
\]

The new endpoint is

\[
\alpha_{212}=\frac{3740051857643324945}{10517860061584293888},\qquad
V_{212}=\frac{2098901961222753173}{219122084616339456}.
\]

## Universal Bellman lower bound

For each ordered history h let s=(n,a,b) with a counts of symbol 0, b counts of symbol 1, and n=length(h). Strictly positive history masses have ratio Q(h)/P(h)=ρ(s)=2^(a+b)/3^a. For objective tP+K(eP+eQ), under P-normalization the Bellman equation is

\[
B(s)=\min\{K\rho(s)\ [\text{declare P}],\quad K\ [\text{declare Q}],\quad
1+\sum_{j=0}^{2}P_jB(s+e_j)\ [\text{continue}]\},
\]

where continue is excluded at n=14. This recursion is valid for arbitrary full-history competitors, not merely count policies: condition on each actual ordered history and use the IID suffix plus the history likelihood ratio. Randomized actions are convex combinations and cannot beat the minimum. Thus B(root)=H gives V14(α)≥H−2Kα for every real α.

An exhaustive exact Fraction evaluation covers 680 count states, with 1238 strictly positive action gaps (minimum 632064308823793/15996144656056320). Exactly two states tie: T=(10,3,1) with P/continue, and Z=(14,0,0) with terminal P/Q.

## Exact real-valued primal witness and path provenance

At T declare P with real probability u∈[0,1], otherwise continue. At Z declare P with real probability z∈[0,1], otherwise Q. Everywhere else select the unique Bellman minimizer. The observation tuple O=(eP,eQ,tP,tQ) is

\[
O(u,z)=O_0+uD_T+zD_Z+uzM.
\]

Its exact rational coefficients, from the four deterministic corner policies, are:

    O0 = (667907615807166299/1752976676930715648,
          105950621815297/320979616137216,
          2100773454342753173/219122084616339456,
          235241911565585/26748301344768)
    DT = (-36640625/165112971264, 190859375/626913312768,
          -528828125/61917364224, -32265625/5804752896)
    DZ = (-6103515625/78364164096, 6103515625/78364164096, 0, 0)
    M = (0,0,0,0)

The zero bilinear interaction is not inferred from a numerical fit: T already has three symbol-0 and one symbol-1 observations whereas Z has none of either. Counts cannot decrease, so T cannot be an ancestor of Z; Z is terminal, so Z cannot be an ancestor of T. These coins never influence each other's active path.

For the four deterministic (u,z) corners in lexicographic order, an independent integer P/Q-mass DFS preserving every ordered history visited 45331, 45331, 39451, 39451 nodes, total **169564**. At each corner its exact rational outputs equal the conditional suffix-DP outputs. Branch identities and multiplicities are retained for the DFS; the IID count quotient is used only for the proved suffix sufficiency.

Set eP=eQ. Because eP−eQ has nonzero z coefficient, the unique balanced coin curve is

\[
\boxed{z(u)=\frac{267827859599672849}{819200000000000000}
          -\frac{270319}{80000000}u}.
\]

For every real u∈[0,1], both endpoints 0<z(1)=265059793039672849/819200000000000000<z(0)<1, so the entire real coin arc is feasible. Its common error increases affinely from α211 at u=0 to α212 at u=1. The endpoint time gaps are respectively

    (tP−tQ)|u=0 = 173671714797480853/219122084616339456
    (tP−tQ)|u=1 = 173018208237480853/219122084616339456

and are strictly positive. Hence their entire affine interpolation has max(tP,tQ)=tP. All actions at the two ties are Bellman-minimizing, so on the balanced arc tP+K(eP+eQ)=H exactly, i.e. tP=H−2Kα. This attains the universal lower bound for every real α in the claimed closed interval and proves the theorem.

## Strict right separation and Stage213 dual-only frontier

A separate exact first-switch scan gives Stage213 dual-only K213=36993328266365208/365083984886815, H213=326557453975807110989706851827603/3999898191421953578095588933632. The new tie is (2,0,1) Q/continue, with terminal Z P/Q, 680 states, 1238 positive gaps and minimum 3314488625691065/141944653323993672. It verifies exactly

\[
H_{213}=H_{212}+2\alpha_{212}(K_{213}-K_{212}),\quad K_{213}<K_{212}.
\]

Consequently, for α>α212, the new dual bound exceeds the **fixed** Stage212 supporting line by

\[
2(K_{212}-K_{213})(\alpha-\alpha_{212})
=\frac{381829089679610688}{88423341139586593}(\alpha-\alpha_{212})>0.
\]

This proves strict-right separation from the Stage212 support, **not** Stage213 primal optimality.

## Evidence, scope, sources and next task

Frozen global source: GLOBAL_KNOWLEDGE_V1 main@6b3e7a6520898c41e063db04e82b1d3c2c9c3a4b; Enterprise Math main@d42136a33bab42ab25e6d4318774708be2544d62; original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, matching projection. Scientific predecessor: Stage211 author commit c4b51439f30841c169435d63b66f06cacaef3c13, not independently mathematically admitted.

Actual local executions: verify_stage212.py → STAGE212_AUTHOR_EXACT_FULL_REAL_PASS 169564; a separately written standalone reference REPRO_STAGE212.py → STAGE212_REFERENCE_EXACT_PASS 169564; audit_stage212.py exact certificate algebra → STAGE212_INDEPENDENT_CERTIFICATE_ALGEBRA_PASS (not independent mathematical review); scan_stage213.py → STAGE213_DUAL_SCAN_PASS. All computations use Python Fraction/integer, no numerical grid or floating approximation. Original scripts/full corner certificate/logs/hash manifest reside in the accompanying portable evidence package EM_STAGE212_AUTHOR_EXACT_PORTABLE_20261028.tar.xz (SHA256 04c560e02a5dafe2e606e4699aca87bb54801fe0a4ccdffa1dbc8243a32118fa). The GitHub standalone REPRO_STAGE212.py is the exact locally executed source, Git blob 0d1ebe88656b67b674db75f8968999d6af94c68a.

BRC applies as typed positive rational branch mass and separate P/Q provenance; there is no signed/phase cancellation or native X6 observer claim. No Lean checker run, physical calibration, independent Driver approval or native Source Result exists. A native owner query returned CONTROL_QUOTA and native status advertised research_authority_granted=false; the present result is portable author mathematics. Next unit: solve the four Stage213 policy corners, error-balance feasibility, time dominance, mixed term and all-real interval or exact rational obstruction, under unchanged history-sensitive model.
