# D25 — original 216-weighted 3F2 terminal source and resonant-seam repair

Date: 2026-11-01. Author-side portable mathematics, Research lane chatgpt-research-hourly-enterprise-math-20260923. Original task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_RUN / SOURCE_CHECKPOINT_PENDING.

## Exact target/source

Consume (without recrediting) the original signed Clausen source-port identity in research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md at 2d7bdfd7821d3afac8eaefb4b88bfedca8ff46be: the frozen original 216 scalar is

W_p = sum_{n=0}^{p-1} (6n+1) (1/2)_n (1/3)_n (2/3)_n / [ 2^n (n!)^3 ].

Write a_n=(1/2)_n(1/3)_n(2/3)_n/(n!)^3, w_n=(6n+1)a_n and W_p(z)=sum_{n<p}w_n z^n. Thus W_p=W_p(1/2). The following statements hold for every prime p>=7, p≡1 (mod 6), hence for both original 216 target classes p≡13,19 (mod 24). They are external auxiliary p-adic algebra, not a claim about native X6 or H0/B0.

## Theorem I — a polynomial operator for the original weighted sum

Let theta=z*d/dz, P(theta)=(theta+1/2)(theta+1/3)(theta+2/3), and

D_W=(6theta-5)theta^3 - (6theta+1) z P(theta).

The operator order is literal: (6theta+1) applies AFTER multiplication by z, so the second term is not z(6theta+1)P(theta).

An exact identity over rational polynomials is

D_W W_p(z) = -(6p+1)(6p-5)(p-1/2)(p-2/3)(p-1/3)a_{p-1} z^p.  (1)

Moreover, v_p(a_{p-1})=3 and a_{p-1}/p^3≡-1 (mod p). Hence, coefficientwise,

D_W W_p(z) ≡ (5/9)p^3 z^p (mod p^4),                  (2)

and in the actual original evaluation coordinate,

D_W W_p(1/2)/p^3 ≡ 5/18 (mod p).                     (3)

In particular the normalized terminal source is nonzero. Unlike the previously derived terminal sources -35/64 (p≡13 mod24) and -3/64 (p≡19 mod24) for a *different* 2304 finite Gauss operator, this weighted original-216 source has the SAME 5/9 in both classes. A transfer between the two operators must exhibit explicit signed quadratic cutoff/port contributions; no identification of terminal coefficients by analogy is justified. Neither (2) nor (3) proves W_p≡p (mod p^3).

Proof of (1). The rising-factorial recurrence says n^3 a_n=P(n-1)a_{n-1} for n>=1. The coefficient of z^n in D_W W_p for 1<=n<p is

(6n-5)n^3 w_n - (6n+1)P(n-1)w_{n-1}
=(6n+1)(6n-5)[n^3a_n-P(n-1)a_{n-1}]=0.

The constant coefficient vanishes. The only remaining coefficient is z^p from the second term at index p-1, giving (1) exactly. This operator has no division by the potentially nonunit factor 6n+1.

Proof of normalized top coefficient. Write

a_{p-1} = prod_{j=0}^{p-2} (2j+1)(3j+1)(3j+2) /
          [18^(p-1)((p-1)!)^3].

Three and only three numerator factors are p-divisible: p at j=(p-1)/2, p at j=(p-1)/3, and 2p at j=2(p-1)/3. Each is exactly once divisible by p; none of the denominators is divisible by p. By Wilson, the products of the other residues in the three affine-permutation families are 1, 1/2 and 1 modulo p: remove the zero and the j=p-1 residues -1, -2, -1 from the complete nonzero product -1. The numerator divided by p^3 is therefore 2*(1)*(1/2)*(1)=1 modulo p. The denominator is 18^(p-1)((p-1)!)^3≡-1 modulo p. Thus a_{p-1}/p^3≡-1. Since P(p-1)≡-1/9 and (6p+1)(6p-5)≡-5 mod p, (1) gives (2). Fermat at z=1/2 gives (3).

## Theorem II — valuation bands and sharp local carry

Let r=(p-1)/6 and three cutoff indices j1=(p-1)/3, j2=(p-1)/2, j3=2(p-1)/3. For ALL 0<=n<p,

v_p(a_n)=1_{n>j1}+1_{n>j2}+1_{n>j3},               (4)
v_p(w_n)=v_p(a_n)+1_{n=r}.                           (5)

The last term in (5) is an additional LOW-BAND weight resonance: 6r+1=p. It is not one of the three Pochhammer numerator crossings. The exact seam-carry law is

w_{r+1} ≡ (36/125) (w_r/p) (mod p), with w_r/p=a_r a p-unit.  (6)

Proof. The three zero-residue numerator factors enter at n>j1, n>j2, n>j3 respectively, each exactly once; n! stays a p-unit. Among 6n+1 for 0<=n<p, exactly one is a multiple of p when p≡1 mod6, at n=r; it is exactly p. For the seam, the hypergeometric ratio a_{r+1}/a_r at r≡-1/6 modulo p equals ((1/3)(1/6)(1/2))/(5/6)^3=6/125. Since 6(r+1)+1=p+6, multiply by 6 to obtain (6).

Observer-fiber consequence, with restricted quantifiers: in the family of unit scalar multiples of this recurrence, w_r mod p is always zero but w_{r+1} mod p varies with the upstream unit. Therefore a LOCAL propagation observer carrying only w_r mod p cannot determine the successor; retaining the repair coordinate w_r/p mod p is sufficient for this one seam. For the specifically normalized sequence a_0=1 one could also recompute from the full defining formula. No native spatial embedding or general information-minimality theorem follows.

## Exact checks and evidence strength

A Python standard-library checker constructs original rational coefficients in Z/(p^4), verifies (4)-(6) for EVERY coefficient, the INTERNAL cancellation of (1) coefficientwise, the top coefficient (2), and independent evaluations at z=1/2 and z=1/9. Nine sample primes independently reconstruct a_{p-1} from the original factorial product. Actual execution: 207/207 primes 7<=p<=3000, p≡1 mod6 PASS, including 53 p≡13 mod24, 54 p≡19 mod24 and 100 other primes.

p=13: r=2, w_r/p=11, w_(r+1)=4, normalized D_W terminal=2 (all mod13).
p=19: r=3, w_r/p=7, w_(r+1)=16, terminal=9 (mod19).
p=37: r=6, w_r/p=11, w_(r+1)=23, terminal=17 (mod37).
p=373: r=62, w_r/p=81, w_(r+1)=271, terminal=42 (mod373).

Theorems are algebraic; finite tests corroborate but do not establish infinity. This is not the native H0/B0 [X]U benchmark, not an original 216 p^3 congruence proof, not a mathematical acceptance, and not a Source-native Research checkpoint.

## Carry and next scientific unit

BRC method: COMPOSE_APPLIED to frozen original W_p and to the prior source-aligned W_p-p ↔ Delta_p-R_p equivalence. Preserve four coefficient strata, the additional resonance p-valuation, original positive/negative signed cutoff Q/p^2=R_p, residue-class tags, observer derivative order and precision horizon. The genuinely next obligation is to derive (or disprove by a discriminating coefficient counterexample) an exact source-preserving intertwiner from this original weighted 3F2 operator to the 2304 quadratic Gauss/Frobenius ports, INCLUDING the signed high-index cutoff and p-dependent normalization; only then try proving all-prime Delta_p-R_p=0 mod p.

Prior exact Research continuation request #6638 terminated UPSTREAM_CODE_REVIEW_REQUIRED. Production/deployment owner is #1558; original same-class native H0/B0 p373 is #1559, NOT_RUN. No new CLAIM, OPEN, session close, native checkpoint, independent review or Result was performed here. P000/ACTIVE and frozen scientific source pin unchanged.