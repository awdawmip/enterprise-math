# D25/LIFT — exact ramified fiber counts for a tangent-blind affine observer

Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Date: 2026-10-25. This is a NEW conditional finite-ring statement, NOT an original CM/divided-power computation, an authorized native execution checkpoint, or a claim of D25/LIFT completion.

## Source and exact scope

Consumes the fixed-source Cayley norm fiber and Jacobian criterion at immutable project commit c7bc4c0b2605411cbdf34f6b8ec6b241502a622c, file research_notes/portable_direct/20261025_hourly_d25_source_frame_norm_observer_jacobian_lift.md. The previously proved criterion states that a scalar observer transverse to the norm fiber is invertible at every digit; a tangent-blind observer is not. The present independent unit computes the ENTIRE cardinality of every fiber for a tangent-blind LINEAR observer, at arbitrary finite precision, including its ramification strata. This is not a recredit of the older loss-of-injectivity proof.

Fix an odd prime p and r >= 2. Put A_r = Z/p^r Z and R_r = A_r[T]/(T^2-2), with sigma(T)=-T. Let alpha=a+bT be a unit, marked in its source frame. Fix u,v in A_r and the linear scalar observer f(a,b)=ua+vb. Define

  F = ua+vb,     L = 4ub+2va.

Assume F is a unit and L = 0 (mod p), i.e. this observer is tangent-blind modulo p. The entire fixed-norm, fixed-first-digit disk of alpha is parameterized WITHOUT quotienting source coefficients by

  beta(t) = alpha (1+tT)/(1-tT),     t in p A_r.

The map t -> beta(t) is bijective onto that disk (as established in the consumed lemma). In this note all operations are exact finite-ring operations; t is a coefficient-ring Cayley PARAMETER, not a native heartbeat/BRC propagator or a physical time coordinate.

## Theorem: exact fiber cardinalities to all finite depths

Let m = r-2. Choose the uniquely determined reduction ell = L/p modulo p^(r-1), and let y be an arbitrary element of A_m = Z/p^m Z (for m=0, the unique element of the trivial ring). Then the number of t in p A_r such that

  f(beta(t)) = F + p^2 y   (mod p^r)

is EXACTLY

  p times #{z in A_m : z^2 = Delta_y (mod p^m)},

where

  Delta_y = ell^2 + 16 F y + 8 p^2 y^2  (mod p^m).

The count is independent of representatives of F and ell at the precisions declared above. In particular, when r=2, every one of the p admissible source elements has the same observer value F modulo p^2.

For r>=3, write d=Delta_y modulo p^m. Its square-root count is determined completely as follows:

* If d=0 modulo p^m: p^floor(m/2) roots.
* If v_p(d)=2e<m and d/p^(2e) is a nonzero quadratic residue modulo p: 2p^e roots.
* Otherwise: zero roots.

Thus every nonempty observer fiber has size divisible by p; at a noncritical, quadratic-residue y the fiber has size 2p, while the highest ramification strata can have more than 2p points. Knowledge of full norm, first residue and one such tangent-blind linear observer loses a precisely computable number of marked source-frame points; a generic two-branch description alone is FALSE over finite local rings with zero divisors.

## Proof, including information-preserving calculation

In the quadratic coefficient ring,

  (1+tT)/(1-tT) = (1+2t^2+2tT)/(1-2t^2).

Therefore, without erasing the even/odd source coefficients,

  a(t)=[a(1+2t^2)+4bt]/(1-2t^2),
  b(t)=[b(1+2t^2)+2at]/(1-2t^2),

and hence the exact identity

  f(beta(t)) - F = t(L+4Ft)/(1-2t^2).

Since L=p ell and t=p x with x modulo p^(r-1), this becomes

  f(beta(px)) = F + p^2 [ell x+4F x^2]/[1-2p^2 x^2]  (mod p^r).

The denominators are units. Equality to F+p^2y modulo p^r is equivalent, modulo p^m, to

  H_y x^2 + ell x - y = 0,
  H_y := 4F+2p^2y.

H_y is a unit, since F and 2 are units. Completing the square gives an EXACT equivalence

  (2 H_y x+ell)^2 = ell^2+4H_y y
                  = ell^2+16Fy+8p^2y^2 = Delta_y  (mod p^m).

The affine transformation x -> z=2H_y x+ell is a bijection modulo p^m. Each such x class has precisely p lifts to x modulo p^(r-1), hence the claimed p times square-root count. For m=0 all t belong to one class, giving p. The square-root enumeration follows from the p-adic valuation of z and the two Hensel lifts of each nonzero square unit over an odd prime. QED.

The exact pairwise observer collision relation is also retained:

  f(beta(t))-f(beta(s))
  = (t-s)[L(1+2st)+4F(t+s)] / [(1-2t^2)(1-2s^2)].

It shows why division by t-s in the finite ring may be ILLEGAL; omitting its annihilator would yield the incorrect assertion that every fiber has at most two elements.

## Explicit p=373, r=3 certificate

Consume the earlier ordinary-Hesse marked candidate alpha=92060+21788T and the tangent-blind linear observer f(a,b)=302a-308b. Here p^3=51,895,117, the norm of alpha is 817747 modulo p^3 (reduces to 122102 modulo p^2), and

  F=21091416,    L=-30389056=373*(-81472).
  F mod 373=131,    ell mod 373=215.

The rescaled first nonconstant observer digit is

  y = 215x + 151x^2  (mod 373),    t=373x.

For y=0, its two distinct roots modulo 373 are x=0 and x=295. There are 373 lifts of each: EXACT fiber cardinality 746. For the critical x=334, y=97 modulo 373, the discriminant is zero and the EXACT fiber cardinality is 373. Direct exact coefficients include

  x=0:     beta=(92060,21788),        f=21091416 (mod 51895117).
  x=295:   beta=(24465372,50204835), f=21091416 (mod 51895117).
  x=334:   beta=(7409201,46747871),  f=34586929 (mod 51895117).

Every displayed beta has norm 817747 modulo 51895117. These are a formal lift of the ORDINARY Hesse coefficient witness into a declared abstract coefficient ring, NOT authenticated original-class CM data or a claim that the original mod p^3 coefficients equal this chosen lift.

## Actually executed exact author checks

Standard-library Python, exact modular arithmetic only. Exhaustively enumerate all t in p A_r; independently compute each marked beta(t), its norm and f, tally observer outputs; compare EVERY tally with p times a separately enumerated square-root histogram for Delta_y. The exact outputs were:

| (p,r) | t values | y values | populated y | maximum fiber | result |
| --- | ---: | ---: | ---: | ---: | --- |
| (13,2) | 13 | 1 | 1 | 13 | PASS |
| (13,3) | 169 | 13 | 7 | 26 | PASS |
| (13,4) | 2197 | 169 | 79 | 169 | PASS |
| (19,3) | 361 | 19 | 10 | 38 | PASS |
| (19,4) | 6859 | 361 | 172 | 361 | PASS |
| (373,3) | 139129 | 373 | 187 | 746 | PASS |

For p=13/19 the exact witness is alpha=2+3T, u=2, v=p-6, with L=4p, F=3p-14. For p=373 the source values are as above. All values are integers in their declared residue rings; the checks do not establish independent review or the unperformed native CM experiment. Reproducible checker lives in sibling file 20261025_hourly_d25_affine_blind_observer_ramified_fiber_check.py.

## BRC/source interface, limitations, and next nonrepeating unit

Carrier: the marked rank-2 quadratic coefficient ring with BOTH a and b preserved. Observer: (N(alpha), alpha mod p, f). Allowed future operations: finite modular arithmetic and source-frame recovery at declared precision. Exact fiber counting here certifies that projection to one tangent-blind scalar destroys branch and p-adic lift information. It is NOT a safe collapse under future coefficient-sensitive operations; retain source coefficients or a source-certified transverse observer. No transfer from this auxiliary coefficient ring to P000's native six-dimensional spatial Cell dynamics is claimed; P000, heartbeat-world X6 semantics and frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 are unchanged.

Unfinished mother D25/LIFT/JT2 requirement: authenticated same-prime/same-original-CM-class divided-power H0/B0 basis, actual [X]U mod p^2, genuine Frobenius rank/direction/normalization, and a proven original kappa / Delta_p-R_p observer. Native CM experiment remains NOT_RUN. Do NOT substitute this lift for native results. No current winning native CLAIM/open/run has been read during this portable research unit; no new native checkpoint is asserted.

Next discriminating action: once the ACTUAL source-defined kappa observation is obtained, derive its exact expression in the real marked frame; test whether it is transverse or tangent-blind. If genuinely a linear tangent-blind quadratic-ring scalar, use the above discriminant/fiber formula to compute loss at the exact prime/precision, and add a proved transverse marked port before any irreversible quotient. Otherwise this theorem does not apply. Formal admission remains with independent review and current Source authority; controller support for repeated CONTROL_QUOTA signature remains Issue #1558, not a duplicate ticket.


## Consecutive second unit: exact number of observable outputs (not just individual fibers)

A distinct finite-resolution question remains after the fiber theorem: how many DIFFERENT second-and-higher observer values can be seen at all? Here this count is independent of ell and of which source point alpha with F unit was used.

For m=r-2, the discriminant map on A_m,

  D(y)=ell^2+16Fy+8p^2y^2,

is an exact bijection. Indeed,

  D(y)-D(z)=(y-z)[16F+8p^2(y+z)],

and the bracket is a unit because p is odd and F is a unit. Thus D is injective on the finite local ring, hence bijective. By the first theorem, an output y is attained if and only if D(y) is a square in A_m, so the exact number of attained values equals the number S(p,m) of DISTINCT square residues modulo p^m:

  S(p,0)=1,
  S(p,m)=1 + (p-1)/2 * SUM_{e=0}^{floor((m-1)/2)} p^(m-2e-1)  (m>=1).

Equivalently,

  S(p,m)=1 + (p^(m+1)-1)/(2(p+1))   for odd m,
  S(p,m)=1 + p*(p^m-1)/(2(p+1))     for even m>=2.

Proof of the count: one square is zero. Every nonzero square has an EVEN valuation 2e<m; writing it p^(2e) times a unit square, it has exactly phi(p^(m-2e))/2 = (p-1)p^(m-2e-1)/2 distinct possibilities. Sum over all e.

At fixed first residue and norm there are p^(r-1) possible marked elements, but only S(p,r-2) scalar outputs of the tangent-blind affine observer. This is an exact finite-domain upper bound on the distinguishable source states, not a probability model or a loss measured in floating-point bits. The executed exhaustive observations from the previous section give, for p=13,r=4: S=79; p=19,r=4: S=172; p=373,r=3: S=187, agreeing with the formula. No independent review or original CM data is thereby supplied.

For next work on a REAL native coefficient readout, this offers a sharp observer-selection test: identify the actual coefficient ring and f from authenticated source first; only then compute the discriminant and image size or use a transverse independent marked observation. It does not supersede P000, native BRC constraints, the frozen D25 pin or the unresolved original H0/B0 experiment.
