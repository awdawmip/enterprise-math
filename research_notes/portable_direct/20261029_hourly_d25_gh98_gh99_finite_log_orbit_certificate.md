# D25/LIFT GH-98/GH-99 — finite-logarithm trace and anharmonic-orbit certificate

2026-10-29 · Research lane: chatgpt-research-hourly-enterprise-math-20260923. Status: **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is an original *application* of standard finite-logarithm identities, not a claim that those classical identities are new. No native Source CLAIM, authorized run, checkpoint, Result, or independent review is inferred. D25/LIFT/JT2 and original GH-3 remain OPEN. Frozen scientific source pin c47e13e4aba0e006366f989d6333ae3 unchanged.

## Exact source and separation

Fix prime p=4d+3 >=7 and work in F_p. Let h_0=1 and h_(j+1)=h_j*(4j+3)^3/[(4j+4)(4j+5)(4j+6)] for 0<=j<d. Every denominator is a p-unit. Define U(z)=sum_(j=0)^d h_j z^j; H(z)=(8 theta+5)U(z), theta=z*d/dz; and the reflected finite tail

  R_p(z) = sum_(j=0)^d (8j+5)h_j*z^(d+1+j)/(d+1+j).

H is the *reflected Laurent observer*, NOT the elliptic Hasse invariant. The original-source GH-3 target T_(p,z)=(8 theta+1)S_d(z) is a different object. The previously verified R_p'(z)=z^d H(z) is reused, not presented as a new discovery.

## GH-98: universal finite-log and Fermat-quotient trace

Define the classical finite logarithm L_p(t)=sum_(n=1)^(p-1) t^n/n in F_p[t]. It has the integer polynomial representation

  L_p(t) = [1-t^p-(1-t)^p]/p (mod p),                       (98.1)

where division is performed in Z[t] *before* reduction. Thus L_p(1-t)=L_p(t), t L_p(1/t)=-L_p(t) for t!=0, and L_p(0)=L_p(1)=0.

**Theorem 98.1.** For every prime p=4d+3>=7 and every a in F_p^*,

  R_p(a) = a sum_(x in F_p^*) x^d H(x) L_p(x/a).           (98.2)

Hence R_p(a)=0 iff the right-hand finite-field logarithmic trace vanishes. The trace is a *noncircular source-faithful alternate certificate* as its right side contains neither R_p nor its derivatives.

**Proof.** Write Q(x)=x^(d+1)H(x)=sum_(j=0)^d b_j x^(d+1+j), b_j=(8j+5)h_j. Multiplicative orthogonality sum_(x!=0)x^k=-1 if (p-1)|k and 0 otherwise gives

  sum_(x!=0) Q(x)L_p(a/x)
    = -sum_(j=0)^d b_j a^(d+1+j)/(d+1+j) = -R_p(a).

Indeed d+1+j belongs to [d+1,2d+1]=(p+1)/4,...,(p-1)/2, so no other exponents collide modulo p-1 with n in [1,p-1]. Apply L_p(a/x)=-(a/x)L_p(x/a). The binomial identity binom(p,n)/p=(-1)^(n-1)/n (mod p) proves (98.1), and its exact integer numerator gives both functional equations. This proof does not assume CM, previous H(9) vanishing, or GH-3.

Let q_p(u)=(u^(p-1)-1)/p mod p for p-unit integer u. With the term u q_p(u) defined as zero when p|u, any integer representative r of t satisfies

  L_p(t) = -r q_p(r) -(1-r) q_p(1-r) mod p.                (98.3)

This gives a second, independently executable *weighted Fermat-quotient trace* for R. The formula follows from u^p=u+p*u*q_p(u) mod p^2, and is independent of representative by (98.1). Calling this a Wieferich or CM classification would be premature.

## GH-99: six-transform weighted source projection

Put X=F_p\{0,1}, F_a(t)=(a*t)^d H(a*t). The anharmonic S3 is generated on X by s(t)=1-t and i(t)=1/t. Its six transforms g(t) and finite-log weights w_g(t), defined by L_p(g(t))=w_g(t)L_p(t), are:

| g(t) | w_g(t) |
|---|---|
| t | 1 |
| 1-t | 1 |
| 1/t | -1/t |
| 1-1/t | -1/t |
| 1/(1-t) | -1/(1-t) |
| t/(t-1) | 1/(t-1) |

**Theorem 99.1.** Define the weighted projection

  (P F)(t) = [F(t)+F(1-t) -{F(1/t)+F(1-1/t)}/t
    -F(1/(1-t))/(1-t) +F(t/(t-1))/(t-1)]/6.

Then for every p,a as above,

  R_p(a) = a sum_(t in X) (P F_a)(t) L_p(t).               (99.1)

If P F_a is identically zero, R_p(a)=0. Conversely, the trace may vanish through inter-orbit signed cancellations even if every orbit contributes nonzero. Thus P is a lossy *observer quotient*, not permission to discard original source coefficients.

**Proof.** Each g permutes X. Substitute u=g(t) in sum_(u in X)F_a(u)L_p(u), use the weight relation, and average the six equal sums. Since p>=7, 6 is a unit. No inferred CM or GH-3 identity is needed.

**Theorem 99.2 (exact orbit sizes).** The orbit {-1,2,1/2} always has size 3. For p=7 mod12, the two roots of t^2-t+1=0 form one size-2 orbit and the remaining (p-7)/6 orbits have size 6. For p=11 mod12 there is no size-2 orbit and the remaining (p-5)/6 orbits have size 6. Proof: order-3 fixed points solve t^2-t+1=0, whose discriminant -3 is a square precisely when p=1 mod3 for p>3. Other points have trivial stabilizer. Count all p-2 elements.

**Exact 3347 witness.** For p=3347 (p=11 mod12), the Fermat-quotient implementation decomposes X into **one size-3 and 557 size-6 orbits**. Each of the **558** uniquely represented orbit contributions at a=9 is nonzero modulo 3347, yet their modular sum is **zero**, independently matching GH-95's reflected-tail computation. Canonical first five (representative, size, finite log, signed source sum, orbit contribution):

  (2,3,3255,2138,299)
  (3,6,2518,1956,2551)
  (4,6,553,825,2603)
  (5,6,2493,421,743)
  (6,6,2451,3311,2462)

Therefore this zero is a *global signed cancellation in the chosen source/observer chart*, not the disappearance of a single local orbit contribution. No uniqueness beyond the GH-97 finite bound or explanation of the arithmetic cause is asserted.

## Verification, BRC, next frontier

Actually executed integer-only Python standard-library programs:
- d25_gh98_finite_log_trace_check.py: 14 distinct primes, **453** parameter specializations; direct tail, integer-binomial finite-log trace, Fermat-quotient trace, and paired symmetry agree. For p<100 every finite-field element was also checked against coefficient and integer evaluations of L_p.
- d25_gh99_anharmonic_orbit_check.py: all six transformation weights, exact orbit partition and **453** parameter specializations agree with the direct tail; the 3347 witness has 558 nonzero signed orbit contributions summing to zero.

Terminal checks: PASS_GH98_FINITE_LOG_FERMAT_AND_SYMMETRIC_TRACE and PASS_GH99_S3_ORBIT_SOURCE_PROJECTION. These support finite computations; the universal statements rest on the derivations above. Reuse: **BRC COMPOSE_APPLIED**, carrier (prime p, reflected j, x, transformed t, orbit, source/observer weight, mod-p value), preserving sign, coefficient origin, operations and valuations; the S3 quotient loses information. External arithmetic variables are not native 6D coordinates. P000 ACTIVE and Heartbeat World spatial/time semantics unchanged.

**Next minimal nonrepeated science question:** substitute a properly normalized elliptic Hasse/Legendre *finite-character-sum* representation into (98.2) and seek a CM/Jacobi/WZ simplification predicting the 3347 trace zero. Independently use GH-92's signed eigenport for original GH-3 T_(p,9)=0 mod p. Preserve Laurent B0L, GH-20/21, W/S, six Hasse ports, R23/R36 and native p=373 work.

2026-10-29 15:19 +08 native gateway 0.6.11: research_authority_granted=false; executor_binding_configured=false; CODE_REVIEW_REQUIRED, active quota 5/5. Prior 2026-10-25 recovery #6424 and continuation #6425 are historical read-only evidence, not current Source ownership. No new native CLAIM/OPEN/checkpoint was made; historical session/staging untouched. Succession issue enterprise-math#1558 remains the control owner. Research/maintenance logical IDs remain separate.
