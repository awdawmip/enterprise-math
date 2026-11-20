# X6 R48 — Exact finite-resolution BRC tomography and sharp Port-count separation

Date: 2026-11-20 (Asia/Shanghai). Task: RS-X6-NATIVE-TIME-DYNAMICS. Continuation R44 → R47 → R48. Scientific status: CONDITIONAL_AUTHOR_PROOF / EXACT_RATIONAL_INTERVAL_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.

## Fixed model and observation

Work on the *unchanged conditional R44 graph*: two named once-only whole-triad sources A,B, each with p≥1 Port choices. Port 0 shares a Cell; candidate R releases occupancy; once-only candidate T may reoccupy from stored source/Port information. The coarse observer maps each named source transfer to F, leaving R and T distinct. Transfer weights α,β are positive, and R,T have weight one. Z(w) adds weights of all successful named, ordered histories projecting to w: exact positive weighted BRC, with source/Port provenance and path multiplicity retained internally. This is neither a probability-normalized observer nor a signed-amplitude observer.

R47 proved the root word coefficients, with S=α+β>0, P=αβ>0 and 4P≤S²:

\[
X=Z(F)=pS,\qquad Y=Z(FT)=(p-1)S,\qquad D=Z(FF)=2(p^2-1)P,\qquad H=Z(FRF)=2pP.
\]

Fix reported rational readings (x,y,d,h) with known nonnegative absolute error budgets (εX,εY,εD,εH). Each actual nonnegative coefficient belongs to I(z,ε)=[max(0,z−ε),z+ε]; if z+ε<0 that interval is empty. No stochastic independence, distribution, physical calibration or relative-error hypothesis is made.

## R48.1 — Necessary and sufficient exact inverse certificate

For each candidate integer q≥1 define interval Aq and Bq. For q≥2,

\[
A_q=(I_X/q)\cap(I_Y/(q-1)),\qquad
B_q=(I_H/(2q))\cap(I_D/[2(q^2-1)]).
\]

For q=1, require 0∈IY and 0∈ID, and use A1=IX and B1=IH/2. Reject a candidate if either interval is empty. For nonempty Aq=[a,b] and Bq=[c,d], **there exist α,β>0 with exactly q Ports whose four root BRC masses fit all measurement intervals if and only if**

\[
\boxed{b>0,\quad d>0,\quad c\le b^2/4.}
\]

The complete set of admissible parameters for this q is

\[
\mathcal F_q=\{(S,P): S\in A_q,\ P\in B_q,\ S>0,\ P>0,\ 4P\le S^2\}.
\]

The unordered source weights for each member are roots of t²−St+P=0, i.e. (S±√(S²−4P))/2. A unique feasible q certifies the Port count for this observer and resolution; multiple feasible q give an exact finite-resolution ambiguity set. Nonzero error intervals ordinarily leave a set of possible weights rather than identifying their exact values.

**Proof.** Substituting the four R47 identities turns the four error enclosures into exactly the two independent interval intersections for S and P. Every positive pair α,β satisfies S>0, P>0 and 4P≤S². Conversely, any such S,P has two positive roots, which generate precisely the four required masses. With nonempty Aq,Bq, the largest permitted S is b. If c>0, the smallest P is c; thus a solution exists exactly when b>0 and c≤b²/4. If c=0<d, any sufficiently small P>0 not exceeding min(d,b²/4) works with S=b. This proves both directions, including the positive-boundary cases. QED.

**Finite integer candidate bound.** Write IX=[x−,x+], IY=[y−,y+], ID=[d−,d+], IH=[h−,h+]. If x−−y+>0, every feasible q satisfies q≤x+/(x−−y+). If h−>0, then D/H=q−1/q≤d+/h−, bounding q by the positive root of q²−(d+/h−)q−1=0. Either condition gives a mathematically justified finite exhaustive scan. Without either condition the feasibility test still characterizes candidates; an arbitrary finite scan is not claimed exhaustive.

**Weight-asymmetry diagnostic.** For Aq=[a,b], Bq=[c,d], the discriminant Δ=S²−4P obeys max(0,a²−4d)≤Δ≤b²−4c. A strictly positive lower bound certifies unequal weights; an upper bound of zero certifies equal weights; otherwise equality is unresolved by this enclosure. The discriminant bounds need not be sharp because S,P are coupled.

## R48.2 — Sharp worst-case resolution threshold for just X,Y

Fix a true model (p,S), p≥1, S>0, with two-coordinate mass vector v(p,S)=(pS,(p−1)S). A competing integer q≠p is allowed to select any total mass S'>0. Then

\[
\inf_{S'>0}\|v(p,S)-v(q,S')\|_\infty=\frac{|q-p|S}{2q-1}.
\]

To prove this, the two coordinate differences have opposite signs at the optimum, and their absolute values are equal when S'=(2p−1)S/(2q−1)>0. Moving S' from that point increases their maximum. For q>p, |q−p|/(2q−1) increases with q; for q<p, its minimum is attained at q=p−1 and is larger than the value for q=p+1. Consequently,

\[
\boxed{\inf_{q\ne p,\ S'>0}\|v(p,S)-v(q,S')\|_\infty=\frac{S}{2p+1}}
\]

and the nearest alternative is q=p+1, S'=S(2p−1)/(2p+1). The two independent bounded-error boxes of common radius η cannot overlap for any alternative integer count precisely when 2η<S/(2p+1). At equality their midpoint is shared, so the strict inequality is sharp under the X,Y-only worst-case-error model. Choose positive equal source weights within both models to realize this witness. **This sharp threshold is not the four-mass threshold:** D,H can reject competing q even when X,Y alone would be ambiguous.

## Example and executable verification

At p=3, α=1, β=2, R47 gives (X,Y,D,H)=(9,6,32,12). With the same absolute error η for all four coefficients, the exact R48.1 certificate yields only p=3 for η=0,1/20,1/5,1/2,1,2, while η=4 allows p∈{3,4} (verified over p=1..14; all cases have the strict finite-enumeration bound above). The separate sharp X,Y-only minimax η is S/[2(2p+1)]=3/14.

The accompanying standard-library Python 3 Fraction verifier implements this exact interval certificate and the integer bound. Tested 896 distinct exact p,α,β,η combinations with p=1..8, α,β∈{1/2,1,2,3}, seven η values; it checks all 16 independent sign-corner readout perturbations, totalling 14,336 readout enclosures. A further 120 rational X,Y separation checks pass. The general theorems rest on the proofs above, not the finite tests.

## Provenance, scientific boundaries and next problem

- Source R44 labelled conditional graph: research_notes/portable_direct/x6_r44_rotation_reoccupation_brc_verify.js, Git blob 9e6e7f25d0f1430ab054adb298887ae42b79f1f0.
- R47 exact positive BRC root identity: research_notes/portable_direct/2026-11-20_x6_r47_blind_source_port_weight_tomography.md, Git blob c75903fc4f4516a243cf619d3e7ff8995610ed85.
- Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Retain the six native spatial axes, triadic force closure, independent time, source/Port and complete joint relations. R,T remain conditional and are not established TRIADIC_CLOSURE_E native updates.
- Mathematical type: source-labelled positive weighted BRC mass, then exact rational interval readout. It uses no π, classical trigonometric propagation, ordinary wave solver or signed cancellation. No calibration, physics measurement, independent review, native Result/Review or formal PROGRESS is asserted.

Next: construct an actually admitted native Cell/Link/Port source-event map and test whether its four observable root masses satisfy R47 at all. A separate continuation is exact correlated-error or source-specific-gain tomography; replacing independent interval boxes requires new feasibility conditions.
