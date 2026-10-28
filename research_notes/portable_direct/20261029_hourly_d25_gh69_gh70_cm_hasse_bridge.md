# D25/LIFT GH-69–GH-70: Hasse–Legendre transfer, CM discriminant −24, and Frobenius–2-isogeny

2026-10-29 Asia/Hong_Kong. **SOURCE-GROUNDED / AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** Mother `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` OPEN; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` and P000 ACTIVE unchanged. Portable author evidence, not a Source checkpoint or authorized native run.

## Input / exact observer

For prime p=8m+3 >=11, n=2m=(p-3)/4, N=(p-1)/2, k=F_p, D=binom(3m+1,m) (a p-unit), inherit from project GH-55/65:

F_m(z) = sum_{r=0}^m ((-m)_r)^2 z^r/((2m+2)_r r!),
G_m(z) = (16z d/dz + 5)F_m(z).

At t²=8/9 in F_{p²}, the inherited GH-55 identity is
D F_m(9)=9^m P_n(t), and D G_m(9)=9^m(tP'_n(t)-P_n(t)).
GH-55 source: enterprise-math@9cceb3e48c0a7fca2d36918814cd9cefe00e8db3. This is input, not new credit.

## GH-69: extension-safe Hasse invariant and an exact G observer

Define A(T)=−3(3T+5)/2, B(T)=−(9T+7), E_T: y²=x³+A(T)x+B(T), and
H_p(T)=[x^(p−1)](x³+A(T)x+B(T))^N in F_p[T].

**Theorem.** For every prime p=8m+3>=11,

H_p(T) = chi_p(−6) P_n(T) in F_p[T].

Proof (explicit dependence on published prior art): Zhi-Hong Sun's 2010 theorem (arXiv:1012.3898, *Congruences concerning Legendre polynomials II*) states for s in F_p
P_floor(p/4)(s) = −chi_p(−6) sum_{x in F_p} chi_p(x³+A(s)x+B(s)).
By Euler's criterion the sum is sum_x (x³+Ax+B)^N. Its x-degree is 3N<2(p−1); among nonconstant powers only x^(p−1) contributes, with sum −1. The constant contribution is p=0. Thus the character sum is −H_p(s), so P_n(s)=chi_p(−6)H_p(s). To lift the identity from F_p-values to polynomials, each contributing monomial has 3i+j=2N and i+j+k=N, hence j=2N−3i, k=2i−N, and j+k=N−i<=n. Thus deg_T H_p<=n<p, while deg P_n=n<p. Agreement at all p elements gives polynomial equality. Since chi_p(−6)=±1, the orientation above follows. No extension-valued character sum is asserted. QED.

Now t0=2sqrt(2)/3 lies in F_{p²} for p≡3(mod8) with t0^p=−t0. Differentiating the polynomial identity in F_p[T] is legitimate, so

D G_m(9)=chi_p(−6) 9^m [t0 H'_p(t0) − H_p(t0)].

Since n is even, the bracket is in F_p. For all p≡11(mod24), the desired G_m(9)=0 is *equivalent* to a vanishing Euler–Hasse derivative at t0; that arithmetic vanishing remains OPEN. For p≡19(mod24), the inherited F channel statement is equivalent to H_p(t0)=0. Equality of observers is established; neither unproved vanishing is inferred from the equality.

## GH-70: explicit discriminant −24 CM chart and a 2-isogeny to Frobenius conjugation

Direct exact invariants of E_T:

4A(T)^3+27B(T)^2=−729(T−1)^2(T+1)/2,
Delta(E_T)=5832(T−1)^2(T+1),
j(E_T)=64(3T+5)^3/((T−1)^2(T+1)).

At t0=2sqrt(2)/3:

Delta(E_t0)=648−432sqrt(2),
J=j(E_t0)=2417472+1707264sqrt(2),
J²−4834944J+14670139392=0.

The last polynomial is the established Hilbert class polynomial H_{−24}, the maximal order of Q(sqrt(−6)), class number two (NumberDB and Fungrim cited below). The characteristic-zero elliptic family point is therefore a CM chart. This is source-grounded identification, not a newly proved CM classification.

For a constructive modular relation, set
u(T)=64(1−T)/(1+T),
C_T: y²=x³+x²+((1+T)/8)x.
The rational 2-torsion point (0,0) gives the degree-two isogeny
(x,y) ↦ (x+1+b/x, y(1−b/x²)), b=(1+T)/8,
onto C'_T: y²=x³−2x²+((1−T)/2)x.

By direct invariants,
j(C_T)=(u+16)^3/u=j(E_{−T}),
j(C'_T)=(u+256)^3/u²=j(E_T).

The exact model isomorphisms also hold: removing the quadratic term of C'_T yields short coefficients A'=−(3T+5)/6, B'=−(9T+7)/27. Scaling by a factor whose square is 3 changes these to (9A',27B')=(A(T),B(T)). Removing the quadratic term of C_T yields A_c=(3T−5)/24, B_c=(7−9T)/216. Scaling by a factor whose square is −6 changes these to (36A_c,−216B_c)=(A(−T),B(−T)). Thus E_T and E_{−T} are genuinely 2-isogenous over a field containing sqrt(3),sqrt(−6), not merely j-equal.

For any prime p≡3(mod8), t0 belongs to F_{p²}, t0^p=−t0. Every F_p^× element is a square in F_{p²}, so the model isomorphisms and 2-isogeny are defined over F_{p²}. Therefore E_{t0}^{(p)}=E_{−t0} is 2-isogenous over F_{p²} to E_{t0}. Composition with relative p-Frobenius gives a degree-2p endomorphism over F_{p²}. It supplies a concrete Frobenius-isogeny path; the differential/eigenvalue scalar required to infer the Euler–Hasse special value remains unproved.

Quadratic reciprocity gives chi_p(−6)=+1 for p≡11(mod24) (split in Q(sqrt−6)), and −1 for p≡19(mod24) (inert). Both are p≡3(mod8), so their two CM j-roots are swapped by p-Frobenius. The split/inert distinction cannot be substituted for the still-open G observer derivative.

## Exact finite verification and BRC

Companion author Python standard-library program computes F_p² elements as pairs (a,b) with (a+b sqrt2)(c+d sqrt2)=(ac+2bd,ad+bc), the Hasse multinomial coefficient and parameter derivative, Legendre recurrence and derivative, F/G coefficients, CM j polynomial, u-parametrized 2-isogeny invariants and Frobenius conjugation. All 76 primes 11<=p<2000, p≡3(mod8), passed. It additionally observed G_m(9)=0 for 39 p≡11(mod24), and F_m(9)=0 for 37 p≡19(mod24). These are finite checks, not proofs of all-prime vanishing. The valid algebraic identities follow from the displayed arguments and the cited Sun theorem; independent review is pending.

BRC COMPOSE_APPLIED: coefficient rank, F/G port, parameter T, elliptic source, t0↔−t0 Frobenius chart, quadratic field, isogeny direction and differentiation-before-readout remain distinct. These are auxiliary arithmetic observers, not an asserted native X6 transfer, and do not discharge W/S, Hasse-six, Green R23/R36, GH-20/21 second digits or native p=373 H0/B0. The other Research lanes' work is not recredited.

## Next

Determine the *scalar-normalized* action of the explicit CM/Frobenius–2-isogeny on the Gauss–Manin/Hasse differential, retaining an invariant differential on each model. Then prove or refute t0 H'_p(t0)=H_p(t0) for every split prime p≡11(mod24), independently of the observed G_m(9)=0. Preserve the Source checkpoint native continuation fault as a separate control dependency; do not force a CLAIM.

## References

- Zhi-Hong Sun (2010), *Congruences concerning Legendre polynomials II*: https://arxiv.org/abs/1012.3898
- Hilbert class polynomial table H_{−24}: https://numberdb.org/Hilbert_class_polynomials ; https://fungrim.org/entry/20b6d2/
- Inherited exact project inputs: enterprise-math@9cceb3e48c0a7fca2d36918814cd9cefe00e8db3 (GH-55), enterprise-math@810dbc66168cb3cd5cfd2f5521bd20abec6ac203 (GH-65).
