# D25/LIFT GH-150 — Sharp generic trace-square sampling lower bound

2026-10-30. Author-side portable continuation of GH-148/149, Research logical lane chatgpt-research-hourly-enterprise-math-20260923 (not maintenance). Parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. P000 ACTIVE_LOCKED and scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Exact question

GH-148 proved that the actual trace-line residue has the form J(W)=G(W)^2 with deg G<=m for p=8m+3, m=(p-3)/8, and 2m+1 distinct square parameters suffice to reconstruct a marked derivative J'(W0), W0=1/144. Does the square condition plus the signed anchor G(0)=g0!=0 let an arbitrary black-box polynomial observer recover the same derivative from 2m samples?

## GH-150 theorem and proof

Let F be a field of odd characteristic, m>=1, g0 in F^×, and T any 2m distinct nodes of F containing 0 and the nonzero target W0. Within the generic class of squares J=G^2, deg G<=m, G(0)=g0, the 2m observed values {J(w):w in T} **do not always determine** J'(W0). Hence 2m+1 samples are a sharp worst-case sufficient-and-necessary count for this particular degree-and-square-only observer model, even with a signed nonzero constant anchor.

Proof: Partition T=A disjoint-union B with |A|=|B|=m and 0 in A, and define

    P(W)=product_(a in A) (W-a),
    Q(W)=product_(b in B) (W-b),
    c=g0/Q(0),
    G_plus=c(P+Q),   G_minus=c(Q-P).

Since 0 is not in B, Q(0)!=0, and both G polynomials have degree<=m and constant g0. On A their values agree; on B their values are negatives. Consequently G_plus(w)^2=G_minus(w)^2 at all 2m observed nodes. However

    J_plus(W)-J_minus(W) = 4*c^2*P(W)*Q(W).

The target W0 is a simple root of PQ because nodes are distinct and occur exactly once. Thus J_plus'(W0)-J_minus'(W0)=4*c^2*(PQ)'(W0) !=0. QED. For m=1, W0 lies in B, and the same proof works. Any n<2m observed nodes cannot give a universal guarantee in a class where 2m do not.

This is an **information-theoretic theorem about generic polynomial observer fibers**, not a construction of two actual elliptic curves or a no-go theorem for exploiting the specific Hasse-coefficient structure of the real G_p. A future 3347 algorithm using CM, Jacobi sums or a further explicit arithmetic relation might still require fewer than 837 independently evaluated traces.

## Executed exact witnesses

A separate Python 3 standard-library checker, research_notes/portable_direct/d25_gh150_square_trace_information_lower_bound_check.py, was actually executed for p=11,19,43,59,67,83,107,3347. It constructs both degree-m polynomials on exactly 2m distinct **square-class** nodes, preserves each g0=H_p(1/8) as a signed constant, verifies equality of squares at all observed nodes, and computes a nonzero marked-derivative difference. For p=3347: m=418, g0=3233, W0=860, 836 observed nodes, and

    J_plus'(860)-J_minus'(860)=2779 (mod 3347).

Terminal log PASS_GH150_SQUARE_CLASS_JET_NONIDENTIFIABILITY. These are **formal observer witness polynomials**, not 836 independent elliptic-curve point counts and not an independent evaluation of the original S1.

## BRC reuse, boundaries and successor

Carrier = finite-field square-class labelled trace polynomial; observer = the sample-square values and signed anchor; future operation = the oriented first jet. The explicit nonconstant observer fiber is a concrete BRC information-loss witness: current equality at all measured nodes does not imply equality under the allowed future derivative. This is COMPOSE_APPLIED on GH-148 and BRC observer law, not a P000 native six-axis assertion or new axiom.

Next science: identify an **additional source-backed arithmetic constraint** on actual G_p beyond degree, squareness and signed anchor that can break the generic 837-sample bound, or independently obtain the remaining 836 distinct trace inputs from GH-149. Continue the mother D25 native H0/B0 divided-power, [X]U mod p^2, semilinear Frobenius normalization eta, and p=373 validation separately; GH-3/GH-83 are not closed. Gateway ordinary continuation returned CONTROL_QUOTA, so no new legal CLAIM/OPEN/native checkpoint/Result/review or Source admission is claimed. Source and scheduler settings remain untouched.
