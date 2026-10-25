# Stage116 — exact full-real affine optimum after E saturation

**Author evidence status:** AUTHOR_EXACT_FINITE_PROOF; two separately written exact rational/integer implementations passed locally. This file does not constitute an admitted native Result, independent Research Driver review or a P000/Heartbeat X6 theorem.

**Frozen inputs:** GLOBAL_KNOWLEDGE_V1 main@3f5265ba9cb837a6d9b3ba272de8106f751e8d34; Enterprise Math main@f67a9840c8e8b0d9420366d8049e689f8f1abf1b before publication. P000 startup projection was checked against its canonical blob. Native task inventory returned CONTROL_QUOTA and native session creation returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false: active owner, CLAIM and native session are unverified.

## Exact statement

For at most N=14 independent ternary observations with laws
\[
P=(1/8,1/24,5/6),\quad Q=(1/12,1/12,5/6),
\]
allow any randomized stopping/decision rule depending on its **entire ordered history**. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and
\[
V_{14}(\alpha)=\inf_{eP,eQ\le\alpha}\max(tP,tQ).
\]
The inherited author-proved Stage115 right endpoint is
\[
\alpha_{115}=\frac{900390060440962701793}{2592933255351443128320},
\qquad
V_{115}=\frac{132635694365041929281069}{10371733021405772513280}.
\]
Put
\[
K=\frac{37550061}{41440},\qquad
L=\frac{3296576}{3885},\qquad
S=K+L=\frac{6232589}{3552},\qquad
\eta=\frac{22731875}{28581715777683456}.
\]
**Theorem (exact finite author proof).** For EVERY REAL number \(0\leq\delta\leq\eta\):
\[
\boxed{V_{14}(\alpha_{115}+\delta)=V_{115}-\frac{6232589}{3552}\delta.}
\]
The precise endpoint is
\[
\boxed{\alpha_{116}=\frac{900390062503198401793}{2592933255351443128320},\qquad
V_{116}=\frac{132635679890866772493569}{10371733021405772513280}.}
\]
The SAME supporting affine line is right-sharp: it cannot remain an equality at any larger alpha. This does not assert any formula for the next segment of V.

## Bellman proof covering all ordered-history strategies

At count state \(s=(n,a,b)\), a counts symbol 0 and b counts symbol 1; the third count is \(n-a-b\). The exact prefix likelihood ratio \(Q/P=2^{a+b}/3^a\). Conditional future iid laws are independent of the ordering of this particular prefix, even though the original policy is allowed to remember every letter. For dual loss \(tP+L\,eP+K\,eQ\), the Bellman recursion is
\[
H(s)=\min\left\{K\frac{2^{a+b}}{3^a}\ \text{(declare P)},\
L\ \text{(declare Q)},\
1+\frac18 H(n+1,a+1,b)+\frac1{24}H(n+1,a,b+1)+\frac56 H(n+1,a,b)\ \text{(continue)}\right\}
\]
with no continuation at \(n=14\).

All \(\sum_{n=0}^{14}\binom{n+2}{2}=680\) states and every available action were computed in exact fractions. There are 1,238 strictly positive nonchosen gaps, 0 negative gaps, and only TWO states with multiple minimizers:
\[
D=(9,1,2):\quad\text{declare Q}=\text{continue},
\qquad
T=(14,7,4):\quad\text{declare P}=\text{declare Q}.
\]
The exact minimum positive gap is \(200314681163/7919307325440\). The Stage115 tie E=(12,4,1) is now uniquely declare P. The exact dual root is
\[
H(0,0,0)=\frac{529581447731753074942871}{851289298734478786560}
=V_{115}+S\alpha_{115}.
\]
By backward induction **for every literal ordered prefix**, allowing any history-specific randomized action, \(H(0)\le tP+L eP+K eQ\le \max(tP,tQ)+S\alpha\) for both errors \(\le\alpha\). This certifies a global lower bound, not merely optimality among count-only competitors.

The candidate was found by following Stage115's D tie, along \(dK=-1,dL=-164096/214569\), sweeping the exact AFFINE action gaps over all 680 states. The earliest new tie appears at T when the positive parameter is \(1155167973/56648480\). This is a discovery computation; the complete Bellman pass above supplies global dual validity.

## Constructive full-real primal family and BRC path provenance

At D declare Q with probability \(w\) and otherwise continue. At terminal T declare P with probability \(z\), Q with probability \(1-z\). At every other state use the unique Bellman minimizer. The old E tie is forced to declare P.

The TRUE ordered-first-arrival cones at D and T are disjoint. D has a=1 at depth 9; T has a=7 at depth 14. Reaching T from D would need 6 new symbol-0 observations in only 5 steps; T cannot precede D by depth. Therefore no \(wz\) cross term survives. The positive integer/rational branch carrier retains the true word identity and P/Q path mass:

| state | ordered prefix count | P total mass | Q total mass |
| --- | ---: | ---: | ---: |
| D=(9,1,2) | 172 | 671875/53747712 | 671875/20155392 |
| T=(14,7,4) | 9830 | 614375/75144747810816 | 614375/80244904034304 |

For \(M(w,z)=(eP,eQ,tP,tQ)\), both exact derivatives are:
\[
\partial_w M=\left(
\frac{593265625}{5283615080448},
-\frac{430671875}{5015306502144},
-\frac{34607609375}{1981355655168},
-\frac{17355203125}{417942208512}\right),
\]
\[
\partial_z M=\left(
-\frac{614375}{75144747810816},
\frac{614375}{80244904034304},0,0\right).
\]
The known left point is \((w_{115},z)=(374236473161181/1042086080000000,0)\), with both errors alpha115 and \(tP=V115\). Solving the EXACT identity eP=eQ gives
\[
\boxed{w(z)=\frac{374236473161181}{1042086080000000}
+\frac{118943}{1488694400}z,\qquad 0\le z\le1.}
\]
Throughout this entire interval \(0<w(z)<1\) and \(0\le z\le1\). The balanced error equals \(\alpha_{115}+\eta z\), while \(tP=V_{115}-S\eta z\). The strict time-dominance differences \(tP-tQ\) at the two endpoints are, respectively,
\[
\frac{444360026883234885715}{691448868093718167552}>0,\qquad
\frac{1333084068027931219645}{2074346604281154502656}>0.
\]
As this difference is affine, \(tP>tQ\) for every real \(z\in[0,1]\). The constructed rule uses only dual minimizers and reaches the Bellman lower bound exactly, proving the stated formula for every real delta in the entire interval.

At the right endpoint \(z=1\), but \(w=w_{116}=374319733261181/1042086080000000\) remains in (0,1).

## Right-sharpness over all history-dependent randomizations

Suppose equality in the SAME support line occurred at alpha>alpha116. The finite randomized decision tree admits an optimal policy by compactness. Because \(K,L>0\), equality in the Bellman lower bound forces (i) both errors equal alpha, and (ii) every used action at positive prefix mass is Bellman minimizing. Every non-tie action is therefore forced, so mixing is restricted to the actual ordered histories reaching D and T. At a fixed count state the likelihood ratio and conditional future law are identical for all reaching words, hence the mass-weighted mixed choices over those words have the same four declared moments as a single aggregate \(w,z\in[0,1]\). This is a proved quotient **only for the declared four moment observers**, not a universal erasure of provenance.

The zero mixed term and exact error balance imply \(w=w_{115}+(118943/1488694400)z\) and \(\alpha=\alpha_{115}+\eta z\). Since z≤1, \(\alpha\le\alpha116\), contradiction. The line is right-sharp even if the competitor remembers all ordered history.

## Verification, source scope, and next problem

The accompanying CHECKER_STAGE116.py was locally executed with exact Python Fraction backward Bellman induction, 680 states, precise root moments, interval endpoints and first-hit positive weights. INDEPENDENT_ORDERED_STAGE116.py was separately implemented as literal ordered-word DFS with integer path weights over 24^14 and 12^14; all four deterministic (w,z) corners were exhaustively traversed (862459 or 854719 visited nodes each). Their four moments, both derivative vectors, zero mixed term, ordered first-hit counts and P/Q masses coincide EXACTLY. Neither result is remote execution, Lean formalization or an independent mathematical review.

BRC resolution: REUSE_APPLIED to an exact positive rational labeled-path carrier; authorized operations are iid symbol extension, stopping and final decisions through N14, and observers eP,eQ,tP,tQ. Count compression is justified for this iid likelihood-weighted Bellman recurrence and these four observers only. No P000 geometry transfer, signed/phase cancellation, infinite-horizon bound, or Foundation promotion is asserted.

**Stage117 open:** with z=1 and D still mixed, continue along the D-tie affine dual direction. Exact gap sweep finds first candidate tie at (7,5,1) at \(K=7703713039590/8727240137\), \(L=7249159245096/8727240137\). This is a candidate dual, NOT an achieved next primal interval. Verify all gaps and true first-hit cones, construct or obstruct the next balanced-error primal, and retain author/review/source distinctions.
