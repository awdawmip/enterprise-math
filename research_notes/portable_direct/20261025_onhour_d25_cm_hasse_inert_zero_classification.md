# D25 / SECOND-DIGIT-LIFT — all-prime CM/Hasse classification of the Legendre zero port

**Date** 2026-10-25. **Scope** Author-side portable mathematics; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT, not a Source-native checkpoint, native benchmark, Result, reviewer decision or completed LIFT. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`; research lane `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance lane).

## Theorem: previously missing zero and nondegenerate derivative

Let p=6m+1>=7 be prime, and define
[
L_0(p)=sum_{n=0}^{m}2^{-n}{mchoose n}{2mchoose n},
quad
D_0(p)=sum_{n=0}^{m}n,2^{-n}{mchoose n}{2mchoose n}.
]
With the standard classical CM and Deuring reduction theorems as explicitly imported below, the following is proved for **all** primes p=6m+1:
[
oxed{L_0(p)=0mod piff (2/p)=-1iff p=13,19mod24.}
]
When L_0=0 mod p, **D_0 is nonzero mod p**.

### 1. Exact finite-field polynomial bridge

Let F_m(z)=sum_{n=0}^m 2^{-n} C(m,n)C(2m,n) z^n, and let U_m(z)=P_{2m}(sqrt(1-z/2)), a polynomial because P_{2m} is even. The terminating coefficient ratio of F gives over Q:
[
z(1-z/2)F_m''+(1+(3m-1)z/2)F_m'-m^2F_m=0.
]
Transforming Legendre's differential equation along s²=1-z/2 gives:
[
z(1-z/2)U_m''+(1-3z/4)U_m'+m(2m+1)U_m/4=0.
]
The first-derivative coefficient difference is p/4 and the constant-term difference is mp/4. Mod p the equations coincide. Both values at z=0 are 1; coefficient uniqueness through degree m uses n² invertible for 1<=n<=m. Therefore in F_p[z],
[
F_m(z)=P_{2m}(sqrt{1-z/2}).
]
Choose s∈F_{p²} with s²=1/2. Then L_0=P_{2m}(s) and D_0=F_m'(1)=-P'_{2m}(s)/(4s) mod p. All square-root choices agree because the degree is even.

### 2. Legendre port equals the Hasse coefficient of a specific 3-torsion curve

Set b=(1+s)/54 and define the auxiliary elliptic curve
[
E_b: y^2+xy+by=x^3.
]
Completing the square with w=2y+x+b yields w²=4x³+(x+b)²=:f_b(x). Its mod-p Hasse coefficient is
[
mathcal H_p(b)=[x^{p-1}]f_b(x)^{(p-1)/2}
=sum_{k=0}^{2m} A_k b^k,quad
A_k={3mchoose k},4^k,{6m-2kchoose k}.
]
For 0<=k<2m, the coefficient ratio satisfies
[
A_{k+1}/A_k=
rac{4(3m-k)(6m-3k)(6m-3k-1)(6m-3k-2)}
{(k+1)^2(6m-2k)(6m-2k-1)}
=rac{3(3k+1)(3k+2)}{(k+1)^2}pmod p.
]
The coefficients B_k of P_{2m}(1-54b) are
[
B_k=(-27)^k{2mchoose k}{2m+kchoose k},
quad
B_{k+1}/B_k=-27(2m-k)(2m+k+1)/(k+1)^2,
]
which have the same reduction because 6m=-1 (mod p). All denominators used in 0<=k<2m are p-units; A_0=B_0=1. Hence the exact finite-field polynomial identity
[
oxed{mathcal H_p(b)=P_{2m}(1-54b)}.
]
At b=(1+s)/54 this equals P_{2m}(-s)=P_{2m}(s)=L_0 mod p. This constructs an explicit arithmetic witness without identifying it with the native six-dimensional Heartbeat World.

### 3. Explicit CM invariant and inert/split classification

For E_b, c4=1-24b, Δ=b³(1-27b) and j=c4³/Δ. Both b and 1-27b=(1-s)/2 are nonzero for every p>=7 since s²=1/2≠1, so reduction is good. Over characteristic zero, taking s=√2/2 gives
[
j=2417472-1707264sqrt2
]
with monic polynomial
[
oxed{H_{-24}(X)=X^2-4834944X+14670139392}.
]
**Imported established CM fact:** this is the Hilbert class polynomial for the maximal order of K=Q(√-6), discriminant -24; the class-number-two reduced forms are [1,0,6] and [2,0,3]. Do not treat this classical identification or Deuring's theorem as a newly proved Enterprise Math axiom. Exact polynomial coefficients are independently cross-checked by characteristic-zero invariant algebra; CM identification may be checked in standard tables (MIT 18.783 Lecture 20, https://math.mit.edu/classes/18.783/2023/LectureNotes20.pdf ; D=-24 class polynomial tables, https://bp3aq.github.io/Expository_Paper/Hilbert_class_polynomials_summary.pdf). The latter table has the shifted j-trace t(24)=4833456; adding 2·744 yields 4834944.

**Imported Deuring CM good-reduction theorem:** for p>=7 unramified in K, E_b is supersingular iff p is inert in K; if split, it is ordinary. Supersingularity is equivalent to Hasse coefficient zero. Here p=1 mod3, hence (-6/p)=(-3/p)(2/p)=(2/p), giving L_0=0 iff (2/p)=-1. Quadratic reciprocity then gives the exact target residues 13,19 mod24 among primes p=1 mod6.

For nondegeneracy, if also D_0=0 then P_{2m}(s)=P'_{2m}(s)=0. Legendre's equation at s²=1/2 has invertible leading coefficient; successive differentiation implies all derivatives vanish. Since 2m<p, the polynomial would be zero identically, contrary to P_{2m}(1)=1. Thus D_0 !=0 whenever L_0=0.

## Relation to existing D25 third digit; what remains unproved

The prior author-side joint certificate at commit 9713f10774d8c0a64c64fb2bd9888bec5679f40d established the original Clausen-moment three-band formula
[
M=L_0+pL_1+p^2(L_2^{low}+L_2^{mid}+V_{4m})mod p^3,quad
N=D_0+pD_1mod p^2.
]
The new theorem makes U_0=L_0/p+L_1 an **unconditional p-local integer in the two target prime classes**, and D_0 a nonzero derivative port. Conditional on the **separate admitted first-digit** W_p=p mod p², the remaining exact joint third-digit obligation is
[
mathcal E_p=(12U_0D_0-1)/p+U_0^2+
12U_0D_1+12D_0(L_2^{low}+L_2^{mid}+V_{4m})-T_p
stackrel{?}{=}0mod p.
]
Here T_p is the original signed Clausen cutoff; the numerator may be divided by p only after using its separately justified first-digit input. No all-prime proof of this equation is claimed, and the native CM/Hasse/Frobenius/kappa benchmark on the frozen original object has **not** been performed. JT2/LIFT remains OPEN.

### Actual independent finite checks

An independent local exact-modular test on 2026-10-25 computed binomial L0,D0, Hasse coefficient in F_p[s]/(s²-1/2) and Legendre split predictions for **149 primes p=1 mod6** (all p<=2000 and extra p=19963); 78 inert target primes and 71 split primes. All field identities, zero/nonzero classifications, and target-class D0 nondegeneracy checks passed. Example (p,L0,D0): (13,0,7), (19,0,1), (211,0,42), (19963,0,6798). These tests check the derivation; the all-prime claim rests on the explicit polynomial argument plus the cited classical theorems. Checker filename: `d25_cm_hasse_classification_check_20261025.py`, run output in the author-side portable research bundle; the remotely stored proof itself is sufficient to recover the mathematical derivation.

### BRC, observer and project semantics

Preserved carrier: original integer binomial coefficients, p-valuations, signed finite-field residues, distinct zero/first-derivative ports (L0,D0), Hasse arithmetic witness and separately retained high-rank/signed cutoff T_p. A boolean L0=0 quotient loses D0 and fails the future-operation fidelity test. Exact symbolic observer preservation was applied; **positive weighted BRC is not applicable** to signed F_p residue cancellation. External scalar elliptic-curve arithmetic is an auxiliary declared observer, not a proof about native 6D X6 propagation. P000, ACTIVE X6 worldview and frozen Source pin are unchanged.

**Next unfinished scientific unit:** construct a single finite-field adjoint/telescoper for the whole joint residual E_p, retaining every low/mid/high term and signed boundary; otherwise find an exact counterexample. Native benchmark, canonical Researcher session/CLAIM/run/checkpoint and independent review require their own actual authorization and results. This note is **author-side neutral preservation only**, never Source-native publication or mathematical admission.
