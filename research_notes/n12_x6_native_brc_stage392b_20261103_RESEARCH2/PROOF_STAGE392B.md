# Stage392-B — Source-defined native X6 signed steps expose future hidden BRC state

**Date:** 2026-11-03. **Lane:** Research2 author-side portable research, continuing Stage391-B in Draft PR #1736. **Evidence class:** exact algebraic proof plus executed Python integer/Fraction checker; UNREVIEWED / NOT_ADMITTED. No Task/CLAIM/Result/Review mutation or P000/worldview change.

## 1. Source and scientific pins

Frozen scientific context inherited without rebasing:
- Enterprise Math: 2af3fc484eb11060b69e0afc1b562bcaf5ad1419
- Global scientific context: bf84bd7c61a2444b59b1da96be57df0e9ae47e53
- P000 V5 immutable blob: bcc2590d3168a28f72e8b9f0f9b1f76faadcd488

At the frozen EM revision, the **actually defined** native operation is in definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md §§2–3: twelve primitive signed-axis steps \(T_i^\pm(a)=a\pm e_i\), \(a\in\mathbb Z^6\), in a chosen Cell-anchored raw chart of the native affine torsor. Section 5 defines twenty three-component min-zero observers. Section 6 establishes the relative quotient by the diagonal direction and its integer common-depth reconstruction.

The actual **typed BRC** law is in research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md §§1–3: the shortest native signed-axis word length \(N(a)=\sum_i|a_i|\) and its ordered branch multiplicity \(M(a)=N(a)!/\prod_i|a_i|!\). These are combinatorial path measures, not the P000 spatial quadratic length, signed amplitude, physical clock, or final Cell address.

Also applied: frozen definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.json and definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json. Behavioral rules separately read at current global main e693993599de367f0f27c3da8821e8838eadc848 and EM main dff5390aa240f3ff3cba47a31348a3de317a14ca; those do not replace frozen scientific pins.

## 2. Precisely typed observer and future alphabet

Let \(D=(1,1,1,1,1,1)\). For each of the twenty three-axis selections \(S=\{i,j,k\}\), define
\[
C_S(a)=(a_i-m_S,a_j-m_S,a_k-m_S),\qquad m_S=\min(a_i,a_j,a_k).
\]
Each observer retains its third component. Set \(R(a)=(C_S(a))_{|S|=3}\), the **complete collection** of twenty selected-three-component readouts, not a declaration of native slice membership. Define the enriched observation
\[
O(a,n,\sigma)=(R(a),N(a),M(a),n,\sigma,A_\sigma,Q_\sigma).
\]
Here \(\sigma\in\{P,Q\}\) is a separately typed source label. The arrays \(A_\sigma\) (16 signed auxiliary Bernoulli comparisons) and \(Q_\sigma\) (four rational auxiliary residuals) retain exactly the Stage391-B test sidecars: \(B_k(z)=z^k(1-z)^{3-k}\); \((u_P,v_P)=(1/4,3/4)\), \((u_Q,v_Q)=(1/3,2/3)\); comparison anchors \(1/4,3/4\), \(k=0,\ldots,3\); and residuals \([4B_k(u_\sigma)+B_k(v_\sigma)]/5-m_k/160\) for \(m=(61,21,9,9)\). These test sidecars depend on the source label, not the native spatial chart.

The future language consists of every finite word in the **source-defined** twelve \(T_i^+,T_i^-\). Each step moves the target Cell in its fixed-anchor raw chart, increments a separately typed abstract operation index, and keeps its source label unchanged. In particular, these are not the invented symbolic \(H,J_m\) operators of Stage391-B.

## 3. Theorem A: infinite family and strict one-step BRC separation

For arbitrary integers \(t\ge0,k\ge1\), let
\[
a_{t,k}=(-(t+k),-(t+k),-(t+k),t,t,t),
\quad
b_{t,k}=(-t,-t,-t,t+k,t+k,t+k)=a_{t,k}+kD.
\]
They have **identical current observations** \(O(a,n,\sigma)=O(b,n,\sigma)\) for the same source/index. Every three-component min-zero selection is invariant under adding \(kD\). Both shortest-path multisets have three entries \(t\) and three entries \(t+k\); hence
\[
N(a)=N(b)=6t+3k,\qquad
M(a)=M(b)=\frac{(6t+3k)!}{t!^3(t+k)!^3}.
\]

Apply the actual native operation \(T_1^+\). If \(t=0\), their new \(N\) differ by exactly 2: \(N(T_1^+a)=3k-1\), \(N(T_1^+b)=3k+1\). For **every \(t\ge1\)**, both new lengths equal \(6t+3k-1\), while
\[
\boxed{\frac{M(T_1^+b)}{M(T_1^+a)}=\frac{t}{t+k}<1}.
\]
This is exact for unbounded integer parameters, not a sampled estimate.

**Proof.** At \(t\ge1\), the two post-step absolute axis-count arrays are
\[
(t+k-1,t+k,t+k,t,t,t)
\quad\text{and}\quad
(t-1,t,t,t+k,t+k,t+k).
\]
The multinomial numerators are equal. The ratio of denominator products is
\[
\frac{(t+k-1)!(t+k)!^2t!^3}{(t-1)!t!^2(t+k)!^3}
=\frac{t}{t+k}.
\]
For \(t=0\), the primitive step reduces one negative coordinate of \(a\) and increases a zero coordinate of \(b\), giving the stated exact length difference. QED.

**Executed representative \(t=1,k=2\):** \(a=(-3,-3,-3,1,1,1)\), \(b=(-1,-1,-1,3,3,3)\). Both begin with \((N,M)=(12,2217600)\) and identical twenty relative triples. After \(+E_1\), the values become \((11,554400)\) and \((11,184800)\), respectively; the ratio is \(1/3\).

**Corollary (all fixed residue moduli).** For any integer \(m\ge1\), take \(k=m,t\ge1\). The common depths \(h(a)=-(t+k)\) and \(h(b)=-t\) also agree modulo \(m\), while one native step separates their BRC multiplicities. Therefore adding only a **fixed modular common-depth residue** cannot universally repair this observer. It does not settle arbitrary context-dependent encodings.

## 4. Theorem B: exact all-word fiber classification

For any \(a,b\in\mathbb Z^6\),
\[
R(a)=R(b)\quad\Longleftrightarrow\quad b=a+kD
\ \text{ for some } k\in\mathbb Z.
\]
Proof: equality of every three-component min-zero readout yields all pairwise differences \(a_i-a_j=b_i-b_j\), since every pair belongs to a triple. Conversely all differences are invariant under a common diagonal shift. Native steps preserve such fibers, as \((a+kD)\pm e_i=(a\pm e_i)+kD\). Consequently \(R\) by itself is an exact future-safe quotient for *all* finite native-step words, with its source/index sidecars carried identically.

When the observer includes anchored shortest BRC \(N\), the **all-word future-observation equivalence is equality of the full native raw six-coordinate state**. Indeed for any \(a\ne b\), a finite word whose net signed-axis displacement is \(-a\) brings the first Cell to the chosen anchor, with future \(N=0\); the other ends at \(b-a\ne0\), with future \(N>0\). Identical states clearly agree along every identical word. This is a complete all-integers, arbitrary-finite-word proof.

A canonical sufficient repair is \(R(a)\) plus the **full integer common depth** \(h=\min_i a_i\): recover all coordinate differences from overlapping triples, construct the unique min-zero six-coordinate representative \(r=\operatorname{can6}(a)\), and restore \(a=r+hD\). Thus all native-step and BRC future outputs are determined. Any equally future-safe repair must distinguish distinct native states. The sharp **additional coding size** relative to the already enriched \(O=(R,N,M,\ldots)\) is a different open question.

This pair of theorems identifies exactly when relative information is sufficient and how anchored BRC observables change the necessary state distinction. The chosen anchor is a Cell, not a distinguished ontological origin. The index \(n\) is operation order, not a physical heartbeat tick.

## 5. Exact implementation evidence

The self-contained REPRO_STAGE392B_NATIVE_BRC.py reimplements the **published** signed-step and shortest-path BRC equations over native integers, and uses exact Fraction arithmetic for the retained Bernoulli sidecars. It checks:
- 264 parameter/source pairs, including 24 boundary \(t=0\) cases and 240 strict rational \(t/(t+k)\) comparisons;
- complete grid \(\{-1,0,1\}^6\): 729 reconstruction checks and 26,244 signed-step relative descent comparisons with diagonal shifts \(-2,1,3\);
- twenty sample moduli, with the all-moduli result separately proved above.

Program executed twice, stdout byte-identical: **STAGE392B_NATIVE_T_BRC_FIBER_PASS**. Output and the exact JSON certificate are supplied with the runnable script; JSON size 1988 bytes, SHA256 b1ba9fee897ab4d3dfcad587906d0f4fd88eda17f3950b0264307e2bea1040e2; source SHA256 c527baf9b697d925bb9a79ea92ed7b37334fe5ddc71c567f79b37ecb653c7efe; actual stdout SHA256 cb75b21b8c735c410ecdd9823a4501e8b6a894b57f0805cfa6890be1faa1ba0c. The symbolic claims are established by algebra and reachability, not extrapolated from the finite checks. Native service/physical heartbeat execution was not performed.

## 6. Remaining science and status

Next Stage393-B: select the frozen signed all-length endpoint BRC \(N_M(z)\), or a genuinely source-defined typed path/branch update, with future observation of ordered branch identity, source and provenance. Determine whether full X6 reconstruction from \((R,h)\) is sufficient for that *decorated* state. Either prove generator descent and all-word conservation or construct an exact equal-current/different-future witness plus typed repair. Also consider the sharp incremental encoding cost for enriched \(O\).

This is a durable **portable author-side proof**, not native CLAIM, formal Source Result, Driver acceptance, verified physical law, or modification of P000.
