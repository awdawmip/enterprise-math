# PREFIX-577 / BRC-X6 — exact passive first-gate observer rank stratification

**Date:** 2026-11-08 UTC. **Frozen scientific input:** f42f2906d77f24085c123f3ccfe9667d41caa96d. **Status:** AUTHOR_PROVED / EXACT_SYMBOLIC_GCD_AND_NATIVE_MODULAR_HANKEL_VERIFIED / UNREVIEWED / NOT_ADMITTED. Author-side research note, not a native Source Task Result or checkpoint.

## Original carrier and exact theorem

Retain all original 96 native ports, six tagged actions per port (576 edges), the six native X6 reward axes, separately typed time and gate events, and the original branch and tag provenance. Starting at port 9 and frozen root 0, draw each of six actions uniformly. Let T be first gate time, U and V the accumulated rewards along axes 5 and 6. For the passive gate-return observer set

S(t,x,y) = sum_{n>=0} s_n(x,y) t^n, 
s_n(x,y) = e_9^T C(x,y)^n g(x,y),
F(z,x,y) = (z/6) S(z/6,x,y),

where C is the ungated action-count adjacency weighted by x^R5 y^R6 and g collects gated actions. Exponents are nonnegative integers.

**The exact reduced denominator degree in t, equivalently minimal scalar realization dimension/Hankel rank, is:**

| Specialized first-return observer | Coefficient field | Exact degree |
|---|---|---:|
| x,y independent; retain joint (U,V) | Q(x,y) | **28** (inherited theorem, independently rechecked) |
| x=1, y=lambda; retain V | Q(lambda) | **24** |
| x=lambda, y=1; retain U | Q(lambda) | **24** |
| x=y=lambda; retain sum U+V | Q(lambda) | **18** |
| x=0, y=lambda; filter paths with U=0 | Q(lambda) | **18** |
| x=lambda, y=0; filter paths with V=0 | Q(lambda) | **18** |
| x=y=1; time-only first-gate series | Q | **10** |
| x=y=0; filter paths with U=V=0 | Q | **4** |

The zero-variable cases are **coefficient filters**, using 0^0=1, not lossless reductions. The 1-variable cases forget the indicated reward. The diagonal case counts the **sum** of rewards; it does not erase branch provenance in the underlying native model.

## Proof of all eight exact degrees

The inherited exact 37-class passive quotient is checked against all 576 original tagged edges. Its proven 37 consecutive integer-polynomial residual identities for n=28,...,64, plus Cayley–Hamilton, prove over Z[x,y]:

Q(t,x,y) S(t,x,y) = P(t,x,y), degree_t(Q)=28, degree_t(P)<=27, Q(0,x,y)=1.

The complete 136 monomial coefficients of the explicit Q are preserved at the immutable source:
https://github.com/awdawmip/enterprise-math/blob/a3e9f095d92bd31d2ffcd6b3a40ccb733b137751/research_notes/portable_direct/2026-11-08_prefix577_r6_gate_joint_generic_degree28_exact_author_portable.md

P is determined exactly by the 28 native-equivalent original path count polynomials s_0,...,s_27, by truncating Q*S. Specialize **both** P and Q for each row; compute exact bivariate gcd in Z[t,lambda] or univariate gcd in Z[t], then divide. This gives explicit reduced denominator and numerator, proves the upper bound, and constructs the infinite-sequence recurrence. The exact gcd_t degrees are respectively (generic parent, 4,4,10,0,0,18,4), giving reduced degrees (28,24,24,18,18,18,10,4).

Two useful explicit exact cancellation factors are:

At x=1,y=lambda (or after exchange of x,y):
gcd(P,Q) = 16 t^4 - 8 t^2 + 1 = (1-4t^2)^2.

At x=y=lambda, the gcd is, up to sign:
1 + 12 lambda t^2 - 96 lambda^2 t^4 - 640 lambda^3 t^6
 + 5376 lambda^4 t^8 - 9216 lambda^5 t^10.

This cancels exactly ten degrees and yields the genuinely **18th-order total-reward recurrence**. For x=y=1 a further cancellation yields the time-only order 10.

Every upper bound is sharp by an **independent native 96-port** nonzero Hankel determinant mod 1000000007. The witnesses (x,y; d; det(H_d) mod p) are:

- (2,3; 28; 595325725)
- (1,2; 24; 205620315)
- (2,1; 24; 205620315)
- (2,2; 18; 648725615)
- (0,2; 18; 11808176)
- (2,0; 18; 11808176)
- (1,1; 10; 530286724)
- (0,0; 4; 256)

For each witness, H_d=(s_{i+j})_{0<=i,j<d}, computed from **all 576 native action choices** and no state quotient. Nonzero mod prime is a rigorous integer nonvanishing certificate; at every witness the candidate reduced denominator's constant coefficient is nonzero. Specialization cannot increase a regular family’s recurrence order; each matching lower bound therefore establishes the stated exact rational-function-field degree.

For every row of order d, normalize the reduced denominator to D(t)=1+sum_{j=1}^d d_j t^j. The exact passive scalar realization is the d-dimensional companion form xi_n=(s_n,...,s_{n+d-1})^T with top d-1 superdiagonal shifts, last row (-d_d,...,-d_1) and output the first component. The initial vector is the native sequence s_0,...,s_{d-1}. Its minimality follows from the corresponding nonzero native Hankel minor.

## Interpretation, reproducibility and boundaries

**BRC reuse:** exact native tagged branch counts, weighted joint rewards, gate-return stop and original port provenance. Allowed continuation is repeated passive uniform tagged sampling until the first gate, followed by the declared reward/time readout. This certified scalar compression does not authorize new tagged-action control, replacement of the full six-axis readout, arbitrary port starts or ordered path/provenance queries. In particular, the rank change 28 -> 18 for U+V is an observer-specific information-loss certificate, not a global statement that the joint interaction direction is redundant.

Local fully reproducible program and all exact reduced denominators/numerators are in conversation artifact **PREFIX577_R6_OBSERVER_RANK_STRATIFICATION_AUTHOR_PORTABLE_20261108.zip** (SHA-256 c33efb3a3acd12a8935c7d6b3683b48f5054657f10033c4bc274d674907c33cc). That external artifact is not claimed as published in this GitHub commit. Reproducible algorithm: load the source Q coefficients above and frozen original kernel; form s_0..s_27 from original 96-port nongated paths; compute P=[Q*S]_{<28}; specialize Q and P on the eight curves, compute Z[t,lambda] gcd, and compute the displayed native H_d determinants modulo p. The original native96 and the 37-class quotient integer residual checks n=28..64 were reexecuted successfully this turn.

**Inherited, do not recredit:** degree-28 full (U,V) theorem, 37-state passive quotient and original frozen path kernel. **New scientific unit:** exact eight-observer specialization rank stratification, 24/18/10/4 minimal realizations, complete symbolic common-factor certificates and independent native Hankel nonvanishing witnesses.

**Next independent mathematical unit:** classify readout weights x=lambda^a,y=lambda^b and exceptional parameter loci without discarding native X6 source data. The separate canonical D25 Task still requires the original H0/B0 divided-power module, [X]U mod p^2, Frobenius direction, normalization eta and native CM validation. The current author-side work has no native CLAIM, open, Source task checkpoint, Result, review or admission.

**Researcher provenance:** historical EM-DIRECT-3EE30C / registered service identity EM-ENTERPRISE-301CA6 with Research-Activity RA-E889C3B8461F5844B53CAF15; this turn does not possess the service session private capability and makes no ownership claim. Previous original session_start request h40-r11-self-researcher-session-start-20261108t1954-v1 is already SUCCEEDED and was not replayed. Exact new D25 continuation request h40-r11-d25-continuation-20261108t1512-v1 was QUEUED at last checked receipt; preserve this request ID, do not retransmit it. UR original V2 four-file bundle remains absent from the checked local workspace: expected size 94687 bytes, SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; no reconstructed file is asserted to be the original.
