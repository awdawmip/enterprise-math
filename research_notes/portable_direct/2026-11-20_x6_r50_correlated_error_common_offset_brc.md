# X6 R50 — Correlated bounded readout error and offset-invariant BRC tomography

Date: 2026-11-20 (Asia/Shanghai). Line: RS-X6-NATIVE-TIME-DYNAMICS / independently publishable portable research. Predecessor: R44–R49. Status: CONDITIONAL_AUTHOR_PROOF / EXACT_NAMED_BRC_FINITE_CHECK / NOT_INDEPENDENTLY_REVIEWED.

## 1. Frozen object, observer and error model

Reuse **without alteration** the R44 once-only, whole-triad, two-named-source, p-Port conditional transition grammar: named paths A_i/B_i, shared Cell at Port 0, public release R and candidate reoccupation T. The root BRC observer sums positive branch weights after the **specified** projection of each A_i/B_i to F, retaining R/T. A-transfer weight α>0; B-transfer weight β>0; R/T weight 1. Neither the physical admission of R/T under native P000 nor signed/phase cancellation is presumed. Time is the order of events, not a phase counter.

Set p ∈ Z_{>=1}, S=α+β>0, P=αβ>0 with 4P≤S², and let the four BRC masses (R47) be

    A_p(S,P) = (pS, (p−1)S, 2(p²−1)P, 2pP)

in channel order (F, FT, FF, FRF), conventionally (X,Y,D,H). The R49 observation with unknown **common additive offset** b is now perturbed by four separate real errors:

    z=(x,y,d,h)=A_p(S,P)+b(1,1,1,1)+ε,  |ε_i|≤η.

The error radius η≥0 is known; the four errors may be different, but their common-offset nuisance parameter is exactly the same. No probabilistic independence is assumed. Any weights and b are parameters of this conditional model only.

## 2. R50.1 — Exact elimination of the common offset and error correlations

For fixed candidate integer q≥1 and candidate S>0, P>0, 4P≤S², write a=A_q(S,P) and residual r_i=z_i−a_i.

**Theorem (exact simultaneous consistency).** A common b and errors ε_i with |ε_i|≤η exist if and only if

    max_i r_i − min_i r_i ≤ 2η.

Equivalently, the **six** inequalities

    |(z_i−z_j) − (a_i−a_j)| ≤ 2η   for every i<j

hold simultaneously.

**Proof.** For each channel b must belong to the interval [r_i−η,r_i+η]. The four intervals share a common point exactly when max_i(r_i−η)≤min_i(r_i+η); rearrange. The pair inequalities are the same condition. Choosing any b in their common intersection gives ε_i=r_i−b. QED.

This is an exact correlated-error certificate; checking independently inferred ranges for s=x−y, k=x−h and e=d−h is only necessary in general, since these three errors share ε_x and ε_h. For any fixed q, the six strips are linear in (S,P), and the remaining exact positivity/discriminant constraint is P>0 and 4P≤S². Thus feasibility is a well-defined two-variable semialgebraic question, with no guessed bias or floating-point optimizer required. The six pairs must be checked together.

## 3. R50.2 — A tight offset-free linear exclusion certificate

Let C_q=q²−q−1 and define the null contrast

    L_q(z)=(d−h)−C_q[(x−y)−(x−h)/q].

For **every** exact q-model, L_q(A_q(S,P)+b1)=0.

The sum of absolute values of its four coefficients is exactly

    N_q = 2 if q=1; 3 if q=2; 2(q²−q−1) if q≥3.

Consequently every feasible q must satisfy

    |L_q(z)| ≤ η N_q.                                         (1)

The constant N_q is sharp for this contrast, since independent errors with signs of the four coefficients attain ηN_q; the bound is not an equivalence to the full six-pair consistency test.

**Proof.** Expand
L_q(z) = d + C_q y − C_q(1−1/q)x + (C_q/q−1)h.
Its coefficients sum to zero (the common b cancels). Their absolute sum is the stated N_q (for q=1, L_1=d−y). Bound the ε-inner product by its exact ℓ¹ norm, and choose coordinate signs to attain equality. QED.

For a true p-model z⁰=A_p(S,P)+b1, direct cancellation and factoring yield, for every q≥1,

    L_q(z⁰) = (p−q)/q × [ S C_q + 2P(pq+1) ].               (2)

For q≥2, C_q>0, so (2) has the sign of p−q and is nonzero when p≠q. This gives an explicit source-weight-aware **integer Port separator**.

If observations are within η of the exact true z⁰ and some competing q also fits them with error ≤η, then triangle inequality and (1) force |L_q(z⁰)|≤2ηN_q. Its violation is a rigorous, uniform-in-error exclusion of q.

## 4. R50.3 — An explicit worst-case Port-identifiability radius

**Theorem (constructive sufficient radius).** Let actual p,S,P,b satisfy the above positive-weight assumptions. If

    p=1:  0≤η<P/2;
    p≥2: 0≤η<min{ S/[4(p+1)], (p²−p−1)P/2 },

then **every** possible four-channel observation within η of the actual exact vector is compatible with no other integer Port count q≠p, regardless of the competitor's positive source weights and unknown common offset.

**Proof.**
For p=1 the exact e=d−h equals −2P; under four-channel error it is less than −2η whenever η<P/2. Every q≥2 has exact e_q=2C_qP_q>0, and any η-perturbation of it is greater than −2η. The two observation sets are disjoint.

For p≥2 the actual e=2C_pP>0. The second threshold makes measured e>2η, whereas every q=1 observation has e<2η, excluding q=1.

For rival q≥3, q≠p, equation (2) gives
|L_q(z⁰)| ≥ S C_q |p−q|/q ≥ S C_q/(p+1).
Here |p−q|/q≥1/(p+1) for positive integer p≠q. The first threshold gives S C_q/(p+1)>4ηC_q=2ηN_q, excluding every such q. The sole remaining rival q=2 (possible only if p≥3) satisfies |L_2(z⁰)|≥(p−2)S/2≥S/2; while 2ηN_2=6η<3S/[2(p+1)]≤3S/8<S/2. Hence q=2 is excluded too. QED.

These are **sufficient** rather than claimed optimal radii. They are uniform over all admissible perturbations, unlike determining a candidate set at one fixed measured central vector. Exact R49 uniqueness is the η=0 limit.

## 5. R50.4 — Finite candidate search in the resolved-difference regime

For observed s=x−y, k=x−h, e=d−h, assume s>2η and put m=s−2η>0 and E=max{0,e+2η}.

Every feasible q≥2 necessarily has positive P_q, e_q=2C_qP_q≤E and S_q≥m. Because q/C_q≤2 for q≥2,

    k+2η ≥ q(S_q−2P_q) ≥ qm−qE/C_q ≥ qm−2E.

Thus

    q ≤ (k+2η+2E)/m.                                     (3)

If e+2η≤0 there is no q≥2; q=1 is checked separately. Otherwise (3) supplies a **finite, explicit integer candidate range**, and R50.1 decides each remaining q by exact two-variable feasibility. When s≤2η, bound (3) is not asserted; R50.2–R50.3 remain valid where their premises hold, and unrestricted finite-enumeration claims would need a separate argument.

Worked data: (p,α,β,b)=(3,1,2,0) yield z⁰=(9,6,32,12). At η=1/10, m=14/5, E=101/5, and (3) gives q≤94/7; therefore only q=1,...,13 need consideration. R50.3 independently guarantees p=3, since η<3/16.

## 6. Verification, reproducibility, boundaries and frontier

Executable source: x6_r50_correlated_error_brc_verify.py; result: x6_r50_correlated_error_brc_results.json. The script implements the **named R44 transition carrier**, enumerates all BRC branch histories before projecting to F, and uses Fraction only as the exact positive weight coefficient ring. The finite test covers p=1,...,8; four ordered positive weight pairs; three offsets; all 16 error-box vertices per case; q=1,...,40. It checks 384 directly enumerated short-word masses, 1,536 error vertices and 59,904 rival-Port exclusions, plus formula (3) on the worked case. It is a finite exact check of the stated implementation; the universal parameter result is the algebraic proof above, not the test count.

Provenance:
- Frozen P000 science maintained separately; this proof changes no axiom or taskbook pin.
- Conditional R44 named-branch law: research_notes/portable_direct/x6_r44_rotation_reoccupation_brc_verify.js (Git blob 9e6e7f25d0f1430ab054adb298887ae42b79f1f0).
- R47 root BRC coefficients: research_notes/portable_direct/2026-11-20_x6_r47_blind_source_port_weight_tomography.md.
- R49 exact common-offset inversion: research_notes/portable_direct/2026-11-20_x6_r49_common_offset_tomography.md.
- Researcher historical record: EM-X6-214D9C; Activity RA-545183ADD4EF71C3E4698AEE. No new CLAIM, RUN, formal PROGRESS, Result or independent review is claimed by this note.

Next mathematical opportunities: compute exact **instance-specific** minimal ambiguity radius using R50.1 and the correct common-bias projection; classify boundary behavior s≤2η; obtain an actual frozen-P000 native whole-triad Cell/Link/Port R/T mapping before attributing these conditional short-word results to physical time dynamics. Preserve provenance, signed/phase/type residuals and every operation actually permitted by the declared observer.
