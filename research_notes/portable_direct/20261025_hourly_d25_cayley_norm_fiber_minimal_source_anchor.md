# D25/LIFT — exact Cayley fiber of fixed quadratic norm and a minimal source-frame repair coordinate

2026-10-25 | TASK_RESEARCH portable author proof and exact-integer checks | **AUTHOR-DERIVED / AUTHOR-CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM / NO_NEW_NATIVE_CHECKPOINT**

## Provenance and precise scientific question

Parent D25/LIFT/JT2 remains OPEN. Existing Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Last previously authenticated native checkpoint: Enterprise Math commit 220ee1ba360f21152912d0b4c1abdf867a1e4496; that historical checkpoint is not a new run authorization.

This note *consumes* the preceding rank-one Hilbert–90 norm-classification result and the full-depth semilinear square-orbit theorem in research_notes/portable_direct/20261025_hourly_d25_all_digits_semilinear_square_orbit_coprime_lift.md (first recorded at 78aa0a1f30f68ce2443ea1f1f75697f01ac2e9e2). It does not count their theorems as new. The new question is **exactly how many distinct fixed-frame coefficients share the same norm and first digit**, and what single additional source-marked observable restores them at all finite precisions. This addresses the prior warning that gauge/square-orbit classification does not reconstruct a source-fixed kappa-like coordinate.

## Theorem 1 — complete Cayley parametrization and sharp cardinality

Let p be an odd prime and r >= 2. Put A = Z/p^r Z, R=A[T]/(T^2-2), and sigma(a+bT)=a-bT. Write N(z)=z sigma(z). Fix any alpha in R^times. Define the source-framed norm fiber

  F(alpha) = { beta in R^times : beta = alpha (mod pR) and N(beta)=N(alpha) in A }.

Then the map

  x in pA  |-->  beta_x = alpha (1+xT)/(1-xT)

is a **bijection** from pA onto F(alpha). In particular

  |F(alpha)| = p^(r-1).

The equality refers to exact coefficient pairs in the **same fixed frame**, not to distinct near-identity sigma-gauge orbits: all these alpha and beta_x are gauge equivalent in rank one.

**Proof.** Because x in pA, 1-xT is a unit. The factor W_x=(1+xT)/(1-xT) reduces to one mod p and has norm one. Therefore beta_x belongs to the fiber.

Conversely beta in the fiber gives W=beta alpha^(-1) congruent to one mod p and N(W)=1. Since p is odd, W+1 is invertible. Let Y=(W-1)/(W+1); then Y belongs to pR and

  sigma(Y) = (W^(-1)-1)/(W^(-1)+1) = -Y.

Writing Y=u+vT, the equality sigma(Y)=-Y says 2u=0, so u=0 and Y=xT with a unique x in pA. Solving Y=(W-1)/(W+1) gives W=(1+xT)/(1-xT). The inverse formula xT=(W-1)/(W+1) also proves injectivity. Since pA has p^(r-1) elements, the cardinality follows. QED.

In the rank-one semilinear notation C=alpha, F_C(v)=C sigma(v), the gauge P_x=1-xT gives

  P_x^(-1) C sigma(P_x) = beta_x,

while N(beta_x)=N(alpha). Thus the norm determines the **unmarked gauge class**, but does not determine the fixed-frame coefficient alpha.

## Theorem 2 — exact top-digit tangent and minimal sufficient repair

For r=2 write alpha=a+bT and x=pu with u in F_p. The exact finite-ring transformation is

  beta_x = (a+4pbu) + (b+2pau)T  (mod p^2).

Writing a0=a mod p and b0=b mod p, the pair of second-digit differences is

  ((a_x-a)/p, (b_x-b)/p) = u (4b0, 2a0) in F_p^2.

Since alpha is a unit, (a0,b0) is not the zero pair. This is a **nonzero tangent line** satisfying the linearized norm constraint

  2a0 delta_a - 4b0 delta_b = 0.

It is the *whole* fiber, not merely a subset, by Theorem 1. Hence norm + reduction modulo p leaves exactly p possibilities, or exactly one base-field digit of unresolved fixed-frame information.

At general r the following is a minimal, constructive exact repair:

* If a0 != 0, retaining the full **odd coefficient** b_x in b+pA makes the map x |--> b_x bijective. Thus (N(alpha), alpha mod p, b_x) uniquely determines beta_x.
* If b0 != 0, retaining the full **even coefficient** a_x in a+pA makes x |--> a_x bijective. Thus (N(alpha), alpha mod p, a_x) uniquely determines beta_x.

At least one condition always holds; when both hold either coordinate works.

**Proof of all-digit coordinate sufficiency.** The Cayley factor has the exact pair expression

  W_x = ((1+2x^2)/(1-2x^2)) + (2x/(1-2x^2))T.

Hence

  a_x = [a(1+2x^2)+4bx]/(1-2x^2),
  b_x = [b(1+2x^2)+2ax]/(1-2x^2).

These are defined for all x in pA. They obey a_x=a and b_x=b modulo p, and their derivatives modulo p on the disk pA are respectively 4b0 and 2a0. If one derivative is a unit, the usual *finite* p-adic digit induction applies: knowing a solution mod p^k, changing x by p^k t changes the selected output by p^k times that unit times t modulo p^(k+1). Thus every prescribed matching coefficient has a unique solution x modulo p^r. Induction from x=0 mod p establishes bijectivity pA -> the selected coordinate coset. A cardinality lower bound says that recovering one of p^(r-1) source-frame alternatives requires at least r-1 base-p digits; this construction attains that bound. QED.

This is a **task-relative BRC observer audit**: carrier = (fixed source frame, alpha, sigma, p^r); coarse observer = (norm, mod-p source reduction); future requested operation = exact reconstruction of a chosen source-frame coefficient. The coarse observer loses a sharply measured p^(r-1)-element residual fiber. The extra selected coefficient is an observer-safe repair for that operation, not a new primitive branch, native CM basis, or universal scalar invariant. BRC resolution: COMPOSE_APPLIED (rank-one Hilbert–90 + finite local norm fiber + explicit repair).

## Exact p=373 certificate consuming the prior ordinary Hesse candidate

The previous **ordinary Hesse-derived candidate**, not a native CM Frobenius, was

  alpha = 92060 + 21788 T  (mod 373^2=139129),
  N(alpha) = 122102  (mod 139129),
  alpha mod 373 = 302 + 154T.

Both 302 and 154 are nonzero modulo 373, so either coefficient can be used for Theorem 2's repair.

Choose x=373. Then W_x=1+746T (mod 139129) and

  beta_x = 43570 + 107951T (mod 139129).

Direct exact arithmetic gives

  N(beta_x)=122102=N(alpha) (mod 139129),
  beta_x=alpha (mod 373),

but beta_x != alpha. The second-digit differences are

  (a_x-a)/373 = 243 (mod 373),
  (b_x-b)/373 = 231 (mod 373).

These equal (4*154, 2*302) mod 373. In particular, even a fully known norm and the complete first digit do **not** determine the second-digit coefficient used by a source-fixed observer. The discrepancy is legitimate sigma-gauge freedom only when the accompanying source frame transforms; a native fixed H0/B0 frame has not been supplied or identified.

## Reproducible finite-ring checks

The author executed the following exact-integer procedure for all p in {13,19,373}, r in {2,3}, and **every** x in pA (not a randomized subset). It checked the W norm, beta norm, first-digit equality, and injectivity of the complete fiber. For p=13,19 use alpha=2+T (norm 2); for p=373 use the displayed integer pair, interpreted as an arbitrary lift when r=3 (NOT a claimed source-authenticated Hesse p^3 lift).

~~~python
def mul(z, w, modulus):
    a, b = z
    c, d = w
    return ((a*c + 2*b*d) % modulus, (a*d + b*c) % modulus)

def norm(z, modulus):
    a, b = z
    return (a*a - 2*b*b) % modulus

def cayley(x, modulus):
    inv = pow((1 - 2*x*x) % modulus, -1, modulus)
    return (((1 + 2*x*x)*inv) % modulus, (2*x*inv) % modulus)

for p in (13, 19, 373):
    for r in (2, 3):
        mod = p**r
        alpha = tuple(u % mod for u in ((92060, 21788) if p == 373 else (2, 1)))
        seen = set()
        for k in range(p**(r-1)):
            w = cayley(p*k, mod)
            beta = mul(alpha, w, mod)
            assert norm(w, mod) == 1
            assert norm(beta, mod) == norm(alpha, mod)
            assert tuple(u % p for u in beta) == tuple(u % p for u in alpha)
            assert beta not in seen
            seen.add(beta)
        assert len(seen) == p**(r-1)
        print(p, r, len(seen), "PASS")
~~~

Observed outputs: (13,2,13), (13,3,169), (19,2,19), (19,3,361), (373,2,373), (373,3,139129), all PASS. This verifies the exact finite examples; the universal statement is proved algebraically above. The r=3 Hesse *integer-pair lift* is only a coefficient-ring test, not an original CM experiment or formal mathematical acceptance.

## Scientific and control boundaries; next exact action

The result is a sharpened **source-marking obstruction** for the current conditional quadratic coefficient model. It does not infer that the original kappa or Delta_p-R_p is the odd/even coefficient of the displayed Hesse alpha, nor that norm equality entails equality of source-fixed crystalline observables. The minimal retained coordinate must eventually be *selected and justified from original H0/B0 and [X]U data*; the theorem does not supply that original source.

Same-prime, same-original-class native divided-power H0/B0, [X]U mod p^2, semilinear direction and normalization remain unavailable. Native CM experiment: NOT_RUN. Parent D25/LIFT/JT2: OPEN. Frozen science Source pin is unchanged. The last authenticated native checkpoint is historical; this file is a portable GitHub evidence artifact, not an admitted Source checkpoint or independent review.

Current 2026-10-25 control observation: Enterprise Math em_status returned version 0.6.11; no separate task-bound recovery_status was exposed in this host. The one bounded fresh em_control_continuation attempt for the exact task returned **INVALID_ARGUMENT / CONTROL_QUOTA**. That is a control quota/capability failure, NOT NO_DISPATCH, NOT a current winning CLAIM, and NOT proof of absent results. Do not derive a current session/claim/run or create a new service identity from this note. Existing control support path: Enterprise Math Issue #1558.

**Next smallest scientific step:** source-read the actual CM/divided-power H0/B0 matrix or rank-one coefficient at the original p and its fixed normalization. Determine which coefficient/marked covector represents the original kappa. If the normalizing source frame only supplies a norm/square orbit, exhibit the extra selected p-adic repair coordinate under this theorem; if it supplies a complete frame, compute that source coordinate directly and test the original LIFT assertion. Do not pretend the auxiliary Hesse pair is that source.

**Next control step:** consume a fresh own recovery_status (when actually exposed) and any pre-existing original requests, then canonical continuation and actual Source authority; only the winning Research owner with a successful claim/open and current authorization can publish this proof through an authenticated native checkpoint and finish a lawful HANDOFF. Unreviewed project storage alone is not such a checkpoint.
