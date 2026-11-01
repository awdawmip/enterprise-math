# D25: rational CM lift versus Teichmüller/Frobenius coordinate (portable author proof)

Date: 2026-11-01 Asia/Hong_Kong. Research lane: `chatgpt-research-hourly-enterprise-math-20260923`. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`. Status: **AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This artifact does not assert native Source ownership, an accepted Result or an original H0/B0 experiment.

## New mathematical unit

Let p>=5, p != 3 be prime, lambda=1/9 in Z_(p), and q=(9^(p-1)-1)/p, the ordinary *integer* Fermat quotient. For **every** polynomial F in Z_(p)[z], both identities hold:

(1) lambda^p - lambda = -p lambda q + p² lambda q² (mod p³).

(2) F(lambda^p)-F(lambda) = -p lambda q F'(lambda) + p² q² [lambda F'(lambda) + lambda² F''(lambda)/2] (mod p³).

Proof: The identity lambda^p=lambda/(1+pq) is exact. Expand (1+pq)^-1 to second order, and apply polynomial Taylor expansion with increment divisible by p. Coefficients are p-integral and p is odd, so the stated divided derivative is valid; all terms of degree >=3 have valuation >=3.

If F(lambda) is divisible by p and F'(lambda) is a unit, let r be the unique Hensel root modulo p². Then

(3) (r-lambda^p)/p = -[F(lambda)/p]/F'(lambda) + lambda q (mod p).

If F(lambda) is divisible by p², with g=F(lambda)/p², the root modulo p³ satisfies

(4) r-lambda^p = p lambda q - p² [lambda q² + g/F'(lambda)] (mod p³).

**Precision rule**: the q in p lambda q needs q mod p²; the p² term needs only g and F' mod p. Formula (4) has two separate sources: rational-coordinate Fermat-quotient carry, and Gauss second-digit residue g. It is invalid to discard either before comparison.

## D25 specialization and actual obstruction

Use the existing author-side D25 interfaces (not new claims):

p=8t+5>=13; a=5t+3; h=(p-1)/2;

Q_t(z)=sum_(j=0)^t (-1)^j binom(t,j)binom(a+j,j)z^j,

F_p(z)=sum_(k=0)^(p-1) (1/8)_k(3/8)_k z^k/(k!)².

Assume the prior CM mod-p selector Q_t(lambda)=0 mod p and Q'_t(lambda) !=0 mod p. Set K=8 lambda(1-lambda) Q'_t(lambda) mod p and sigma=K F'_p(lambda) mod p. The prior p-local identity F_p(z)=(1-z)^(h+1)Q_t(z) mod p gives sigma=8 lambda(1-lambda)^(h+2) Q'_t(lambda)² !=0 mod p.

The prior CM-MOMENT observer `M_p(z)=K(F_p(z)/p)` for lifts of the fixed base root therefore satisfies the **new, explicit Fermat-quotient coordinate law**:

(5) M_p(lambda^p)-M_p(lambda) = -lambda q_p(9) sigma (mod p).

Thus, subject to the stated CM mod-p selector,

(6) F_p(1/9)=0 (mod p²) **iff**
F_p((1/9)^p)/p + lambda q_p(9) F'_p(lambda) = 0 (mod p).

This is a *reduced proof obligation*, not a proof that all primes p=13 mod 24 satisfy it. The Frobenius-side normalization must preserve q_p(9) rather than asserting that the Teichmüller-coordinate observation separately vanishes.

Because q_p(9)=2q_p(3)+p q_p(3)² exactly, for any given CM prime satisfying F_p(lambda)=0 mod p² and with unit F'_p(lambda), the **stronger** assertion F_p(lambda^p)=0 mod p² holds precisely when 3^(p-1)=1 mod p² (base-3 Wieferich). This gives a sharp arithmetic discriminator and a falsifiable shortcut.

**Exact counterexample at p=13**, independent of any infinite-prime conjecture: lambda=94 mod 169, lambda^13=146 mod 169, q_13(9)=3 mod 13, F_13(lambda)=169 mod 2197, F'_13(lambda)=8 mod 13, and F_13(lambda^13)/13=6 mod 13. Therefore F_13(1/9)=0 mod 169 but F_13((1/9)^13) !=0 mod 169. The observer has K=3, sigma=11, M(lambda)=0, M(lambda^13)=5 mod 13, matching -3*3*11=5.

## Real execution and limits

A standalone standard-library integer modulo p³ checker independently computed F,F',F'' from all original Pochhammer coefficients, Q and Q' from the original binomial polynomial, and direct Hensel roots. Run on 2026-11-01: **109** eligible primes p=5 mod 8, 13<=p<=3000, all (1)/(2) PASS; **53** p=13 mod 24, all (3)/(5) PASS, and (4) verified for the 53 observed p² zeros. No q_p(9)=0 occurred in this finite family; that does not establish nonexistence outside the tested range.

Representative (p, q9 mod p, M(lambda), M(lambda^p), sigma, (r-lambda^p)/p mod p):
(13,3,0,5,11,9), (37,36,0,5,8,4), (61,26,0,49,37,30), (109,93,0,23,47,83), (373,229,0,294,65,357).

Code companion: `research_notes/portable_direct/d25_frobenius_coordinate_defect_20261101.py`. The exact local run log and full derivation are in the 2026-11-01 author evidence package. These are **portable rational-coordinate** checks, NOT the source-mandated native p=373 H0/B0 benchmark.

## Frontier and safe next action

Mother target remains original 216-sum A_p=p mod p³ for p mod 24 in {13,19}. New precise p=13 mod 24 research step: find a source-verified Dwork/Gross–Koblitz or finite WZ expression of F_p(lambda^p)/p whose p-local normalization cancels lambda*q_p(9)*F'_p(lambda) for every eligible prime; otherwise provide a genuine counterexample. For third-digit comparison use the q² and F'' terms above, not an uncorrected Teich coordinate. Do not repeat the preceding author-side Wronskian/CM-MOMENT or the affine-fibre proof.

As observed on 2026-11-01: authenticated Gateway 0.6.11 had research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, Source CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. No new winning claim/open/run/Source-native checkpoint or research activity is asserted. Project issue #1558 owns the pending native-control recovery; #1559 the independent H0/B0 benchmark. Keep actual predecessor IDs/staging intact and do not borrow the maintenance lane. P000 ACTIVE and source pins unchanged.
