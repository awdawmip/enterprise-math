# D25 AF4: CM(-24) uniformly proves the short Pfaff root and simplicity

Date: 2026-11-09. TASK_RESEARCH author-side mathematical proof: UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.

Frozen parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, scientific input c47e13e4aba0e006366f989d6334d443f6333ae3. Native Source frontier b58330b74576153cdadde5d80a3d92df3a819a0e remains unmodified. Research conversation chatgpt-research-onhour-enterprise-math-20260923; maintenance excluded.

## All-prime theorem

For every prime p=8m-3 ≡13 (mod24), set a=5m-2, b=7m-3, q=(p-1)/2=4m-2; work in F_p. Set

P(z)=Σ_{k=0}^a binom(a,k)binom(b,k)z^k;
R(z)=Σ_{k=0}^{m-1} (-1)^k binom(a,k)binom(m-1,k) z^k (1-z)^(m-1-k);
Q0=Σ_{k=0}^{m-1} (-1)^k binom(a,k)binom(m-1,k)8^(-k);
H(X)=[T^q](T²+2T+X)^q.

Then the following are exact:

(1) H(X)=2^q(1-2X)R(4X(1-X)) in F_p[X].
(2) Q0=0, and P(1/9)=R(1/9)=0 in F_p.
(3) P'(1/9) and R'(1/9) are both nonzero in F_p.

These discharge the two all-prime assertions left as finite observations in 20261109_onhour_d25_Gauss_Pfaff_short_root_signed_band.md.

## Polynomial identity proof

Use the classical Gauss quadratic hypergeometric identity, as formal power series over Z_(p) through degree p-1:

  2F1(1/8,3/8;1;4X(1-X)) = 2F1(1/4,3/4;1;X).

For k<p, -a≡1/8 and -b≡3/8 modp, and the first numerator zero in the left series occurs at index a+1. Thus its truncation modulo (p,X^p) is P(4X(1-X)). The normalized coefficient polynomial H(X)/2^q has coefficients q! 2^(q-2k)/(k!²(q-2k)!) for 0<=k<=2m-1; consecutive ratios (q-2k)(q-2k-1)/[4(k+1)²] agree with (1/4+k)(3/4+k)/(k+1)² modulo p. Hence the right series reduces to H(X)/2^q modulo X^p.

The predecessor's exact terminating Pfaff identity is P(z)=(1-z)^((p+1)/2) R(z) modulo p. Put z=4X(1-X), so 1-z=(1-2X)² and P(4X(1-X))=(1-2X)^(p+1) R(4X(1-X)). Because (1-2X)^p≡1 modulo X^p and both H/2^q and (1-2X)R(4X(1-X)) have degree <=2m-1<p, the truncated series equality is the exact polynomial identity (1).

## CM(-24) and uniform vanishing

Choose s=(3-2 sqrt(2))/6, which satisfies 36s²-36s+1=0, 4s(1-s)=1/9. The curve E_s: y²=T³+2T²+sT has discriminant 64s²(1-s), a p-unit, and

j(E_s)=64(4-3s)^3/[s²(1-s)]=2417472+1707264 sqrt(2).

This root belongs to the Hilbert class polynomial for discriminant -24:
J²-4834944 J+14670139392,
so the curve has CM by the full order of K=Q(sqrt(-6)). For every p≡13 mod24, (-6/p)=-1, so p is inert in K. By Deuring's good-reduction criterion E_s is supersingular. Consequently its Hasse invariant H(s)=0. Since 1-2s and 8/9 are units, (1) gives R(1/9)=0; predecessor Pfaff gives P(1/9)=0; and R(1/9)=(8/9)^(m-1)Q0 gives Q0=0.

The supersingular reduction takes place over the residue field containing sqrt(2), and the proof is intrinsic to this scalar Hasse observer.

## Simple root proof

H(X)/2^q is the mod-p terminating Gauss polynomial 2F1(1/4,3/4;1;X), so it satisfies
X(1-X)H''+(1-2X)H'-(3/16)H=0.
At s, s(1-s)=1/36 is a unit. If H(s)=H'(s)=0, this ODE and its successive derivatives imply that every derivative through degree 2m-1<p vanishes at s. The polynomial must then be zero, contradicting H(0)=2^q≠0. Thus H'(s)≠0. Differentiate (1) at s where R=0:
H'(s)=4*2^q*(1-2s)^2*R'(1/9)≠0.
The Pfaff unit factor implies P'(1/9)≠0.

External published inputs are classical Gauss/Pfaff transformations, Deuring's CM inert-prime criterion, Hasse invariant criterion and the Hilbert class polynomial of discriminant -24; see
https://dlmf.nist.gov/15.8
https://link.springer.com/article/10.1007/s10231-024-01528-x (Theorem 4.1)
https://numberdb.org/Hilbert_class_polynomials
https://www.cambridge.org/core/journals/lms-journal-of-computation-and-mathematics/article/on-the-equations-a22b6cp-and-a22cp/3F32A9CD47048F8EE8C82F98D05A7C56

## Reproducible exact checks

Companion standalone script d25_pfaff_cm24_short_root_20261109.py executes exact modular arithmetic only (no floats/no external libraries). Verified all 157 primes p<=10000, p≡13 mod24: Q0=0, P(1/9)=0, P'(1/9) !=0, and reduction of H mod (36s²-36s+1) is zero. For all 11 eligible p<=400, full pullback polynomial equality is certified by degree+1 distinct exact field evaluations. For p=373: m=47, Q0=0, P'(1/9)=45 mod373, and both Hasse remainder coefficients vanish.

## Source preservation / next exact unit

BRC applied to the signed bands: keep Q0 (now uniformly proven divisible by p), Q0/p, Q1, Qedge, and predecessor affine L,T distinct. Nothing in this scalar CM proof supplies the original native crystalline Frobenius or odd Green/Hesse port. The remaining p² target is a genuine signed five-band identity
(8/9)^a [Q0/p+Q1+Qedge] + L + T ≡0 mod p
for all p≡13 mod24. Find the first-jet CM/WZ relation retaining the p² edge and carry, then connect to original 216/2304 AF4.

Separately, original native same-class p=373 H0/B0 divided-power [X]U modulo 139129, rank, Frobenius/eta, κ, Δ-R, independent reproduction remain pending under GitHub Issue #1559 with no verified executor. This author-side proof makes no native CLAIM/run/checkpoint, Result, review or admission assertion.