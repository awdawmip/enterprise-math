# R762DD — Integral open X6 path-area cocycle and sharp parity repair

Date: 2026-11-17. Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`; author identity `EM-X6-3050F6` with own existing SID `MCP-4b2d70a97f594366a7c94a0f8b45df38`. Independent review: `NOT_REVIEWED`.

## Frozen scientific sources and typed scope

Taskbook `awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md`; frozen P000 V5 `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; R762CH full signed X6 **closed** path area at PR #2575@1c860018c4399e1b7497192ef818e3567390d2e2; R762DC bounded passive frame diagnostics PR #2641. P000 keeps six native spatial axes, native three-force stability, PERP_E/120-degree relation and Cell torsor. The ordered pair-area numbers below are path-provenance relations; their 15 coordinates are not additional spatial axes or native two-dimensional planes. No authentic `TRIADIC_CLOSURE_E` event licensing is assumed.

## Definition — native signed unit-step paths without closing hypothesis

Fix a chosen native chart anchor. An arbitrary (possibly open) primitive X6 path is a finite word (H=(d_1,\ldots,d_m)) with each (d_t\in\{\pm e_1,\ldots,\pm e_6\}\subset\mathbb Z^6). Let

\[
v_i(H)=\sum_t d_{t,i},\qquad
B_{ij}(H)=\sum_{p<t} d_{p,i}d_{t,j}\quad(i\ne j),
\]
\[
A_{ij}(H)=B_{ij}(H)-B_{ji}(H)\quad(i<j).
\]

The (A\)-array is an alternating 15-coordinate history relation. In a closed path, (B_{ij}) for (i<j) is precisely the R762CH path-area (C_{ij}), while (A_{ij}=2C_{ij}).

## Theorem 1 — integral 2-step central extension of signed X6 path concatenation

For every pair of signed unit-step paths H,K (open or closed),

\[
\boxed{v(HK)=v(H)+v(K),\quad
A(HK)=A(H)+A(K)+v(H)\wedge v(K).}
\]

Here ((v\wedge w)_{ij}=v_iw_j-v_jw_i). Therefore the image of the path map (Phi(H)=(v(H),A(H))) lies in the integral two-step nilpotent group
\[
(v,a)\star(w,b)=(v+w,a+b+v\wedge w).
\]
This operation is associative, has identity ((0,0)), inverse ((-v,-a)), and central subgroup ((0,a)). It transforms under signed native-axis permutations via (v\mapsto Pv, A\mapsto(\wedge^2P)A).

**Proof.** Splitting the sum defining (B_{ij}(HK)) into within-H, within-K and cross-boundary ordered pairs gives (B_{ij}(HK)=B_{ij}(H)+B_{ij}(K)+v_i(H)v_j(K)). Subtract the reversed (j,i) expression to get the boxed law. The associator's extra terms on both sides are ((v\wedge w)+(v\wedge z)+(w\wedge z)), by bilinearity. Antisymmetry gives (v\wedge(-v)=0). Covariance follows from relabeling the underlying signed steps. QED.

## Theorem 2 — exact parity image, reconstruction, and realization

For **every** signed primitive path and every i<j,
\[
\boxed{A_{ij}(H)\equiv v_i(H)v_j(H)\pmod 2,\qquad
B_{ij}(H)=\frac{A_{ij}(H)+v_i(H)v_j(H)}2.}
\]

Moreover, **every** pair ((v,A)\in\mathbb Z^6\times\mathbb Z^{15}) satisfying the displayed 15 parity congruences is represented by some signed unit-step path.

**Proof of parity and reconstruction.** Because one native unit step has only one nonzero axis coordinate, (d_{t,i}d_{t,j}=0) for (i\ne j). Hence (v_iv_j=\sum_{p\ne t}d_{p,i}d_{t,j}=B_{ij}+B_{ji}). Subtraction gives (A=B_{ij}-B_{ji}=2B_{ij}-v_iv_j), proving both assertions.

**Proof of surjectivity onto the parity lattice.** Construct a signed coordinate walk (H_0) from 0 to any prescribed (v\in\mathbb Z^6); its area (A^0) has the required parity. For any target A having the same parity, ((A_{ij}-A^0_{ij})/2) are integers. Append signed four-step closed loops (L_{ij}=(+e_i,+e_j,-e_i,-e_j)), each of which has v=0 and (A=+2e_{ij}), and their reverse-oriented analogues, which have (A=-2e_{ij}). Additivity in Theorem 1 when one factor is closed shows independent adjustment of every pair coordinate without changing v. Thus all admissible parity tuples occur. QED.

**Immediate implication.** The signed-X6 path algebra is an index-(2^{15}) parity-constrained sublattice of the naive (mathbb Z^6\times\mathbb Z^{15}) coordinate set (as a set; the parity constraints are nonlinear in v). Unlike R762CH, the open-path (A) is not simply additive: omitting (v\wedge w) yields an incorrect update for open fragments.

## Theorem 3 — sharp modulus for lossless recovery of ordered pair residues

Fix (q\ge2), and suppose the signed endpoint (v(H)) is retained exactly. An observer retaining only (A(H)\bmod m) for some positive integer (m) can reconstruct the complete **ordered** (B_{ij}(H)\bmod q) for all signed unit-step histories if and only if

\[
\boxed{q\mid m/\gcd(m,2).}
\]

The smallest admissible modulus is
\[
\boxed{m_{\min}(q)=\begin{cases}q,&q\text{ odd},\\2q,&q\text{ even}.\end{cases}}
\]

**Sufficiency.** Fix v, so all valid A have the parity of (v_iv_j). If two such arrays agree mod m, their coordinate differences are divisible by both m and 2, hence by (operatorname{lcm}(m,2)=2m/\gcd(m,2)). By Theorem 2, their B differences equal half their A differences and are multiples of (m/\gcd(m,2)), hence vanish modulo q under the stated condition.

**Necessity, with concrete equal-coarse-data counterexample.** If (q\nmid m/\gcd(m,2)), set (t=m/\gcd(m,2)). For any fixed pair i<j, compare the two open histories (H=B_{ij}^{t}) and (K=L_{ij}^{t}), where (B_{ij}=(+e_i,-e_i,+e_j,-e_j)) and L is the oriented loop above. Both are actually closed; they have identical Cell endpoint 0, length 4t, and full signed-direction step histogram. But (A(K)-A(H)=2t e_{ij}\equiv0\pmod m), whereas (B_{ij}(K)-B_{ij}(H)=t\not\equiv0\pmod q). Thus the proposed quotient loses an observable phase even on the strongest common coarse fibre. The least m meeting the divisibility condition is q if q odd, and 2q if q even. QED.

**Information nuance.** On any fixed v, exactly q distinct (A_{ij}\bmod m_{\min}) values are parity-admissible; the necessary 2q modulus for even q is a *congruence repair*, not an additional bit per pair over the actual parity-constrained population. If v itself is discarded, the reconstruction formula no longer applies and future signed Cell updates must be assessed separately.

## Exact executable author verification

Run `node R762DD_VERIFY.js > R762DD_EVIDENCE.json`. Uses JavaScript Number only with bounded integers here; no floating point error arises in the enumerated ranges. The checker exhaustively enumerates all (1+12+12^2+12^3+12^4=22621) signed X6 words of lengths 0..4 and checks parity and B reconstruction on each, all 145²=21025 ordered concatenations of empty/two-step words for the cocycle, all 15 loop edge generators, and 75 exact equal-coarse-history failure witnesses for every smaller modulus than the sharp bound at q=2,...,10. Author execution PASS. General theorems have the proofs above; independent review NOT_REVIEWED.

## Research continuation

This open-path integral update is a candidate *carrier* for legal Cell/Link/Port path provenance. Obtain the authentic `TRIADIC_CLOSURE_E` signed incidence/update predicate and V17/V29/V39 transport, identify which future operations consult B, A, Port/source sequence and other joint residuals, and certify a scope-typed minimal quotient or native separating suffix. Preserve the frozen task science and joint-relation observer contract.