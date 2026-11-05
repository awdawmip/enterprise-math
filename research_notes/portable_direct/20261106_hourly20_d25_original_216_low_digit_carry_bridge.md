# D25: exact original-216 / low-digit signed-carry bridge modulo q^2

Date: 2026-11-06. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Current publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific input: c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane logical conversation: chatgpt-research-hourly-enterprise-math-20260923.

Author-side portable result. Classification: exact algebraic congruence with independent finite modular verification; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT. The prior q^2 two-moment Lucas theorem and diagonal palindrome reduction are reused as prior inputs, not recredited.

## Claim (all primes q >= 5, with no first-digit vanishing hypothesis)

Set n0=(q^2-1)/6, and write n0=qN+r, 0<=r<q. For i=2,3,4, write i*n0=q*M_i+s_i, 0<=s_i<q. The three s_i are pairwise distinct. Let a=-1/2 in Z_(q), J=min(s_2,s_3,s_4), and let

  u_j=a^j prod_{i=2,3,4} binom(s_i,j),  0<=j<=J,
  L=sum_{j=0}^J (6j+1)u_j  (mod q^2).

All following U_i, K_i, A are the *same* signed harmonic/one-carry quantities as in the inherited theorem, namely

  U_i=sum_{j=0}^J (6j+1)u_j (H_{s_i}-H_{s_i-j}) (mod q),
  K_i=sum_{s_i<j<=min_{h!=i}s_h} (6j+1)a^j tau(s_i,j) prod_{h!=i} binom(s_h,j) (mod q),
  tau(s,j)=(-1)^(j-s+1) s!(j-s-1)!/j! (mod q),
  phi_q(2)=(2^(q-1)-1)/q (mod q),
  A=2N phi_q(2) L + sum_i M_i (U_i+K_i) (mod q).

Define the original terminated 216 observer independently of the shadow C_n:

  W_q=sum_{j=0}^{q-1} (6j+1) (1/2)_j (1/3)_j (2/3)_j / [2^j (j!)^3]
     =sum_{j=0}^{q-1}(6j+1)a^j prod_{i=2,3,4} binom(-i/6,j).

Every denominator is a q-adic unit since j<q and q>=5. Then

  BOX: W_q = L + q [A-2N phi_q(2)L] (mod q^2).                 (BRIDGE)

The equality is between signed, source-labeled original-216 coefficients and the low-index signed Lucas carrier; it preserves the three individual one-carry contributions K_i, their M_i high-digit weights and the low-index source.

## Direct proof

For i=2,3,4 the exact identity i*n0=(i*q^2-i)/6 shows

  i*n0 = -i/6 (mod q^2) in Z_(q).

For any 0<=j<q, all denominators in the binomial polynomial binom(x,j) are units, so

  binom(i*n0,j) = binom(-i/6,j) (mod q^2).

Use i*n0=q*M_i+s_i. For j<=s_i, multiplication of the finite descending factors gives

  binom(qM_i+s_i,j)
  = binom(s_i,j)[1+q M_i(H_{s_i}-H_{s_i-j})] (mod q^2).

For j>s_i, precisely one q-divisible factor occurs within j<q, and

  binom(qM_i+s_i,j) = q M_i tau(s_i,j) (mod q^2).

At q>=5 the three residues s_i are distinct: whenever j exceeds two of them, the three-factor product is divisible by q^2. Consequently, contributions without borrow give L and q sum_i M_i U_i; the single-borrow channels give q sum_i M_i K_i; all multiple-borrow channels vanish modulo q^2. Multiplying by the original signed weight (6j+1)a^j and summing gives

  W_q = L+q sum_i M_i(U_i+K_i) (mod q^2).

Substitute the inherited definition of A to obtain (BRIDGE). This argument holds for *every* prime q>=5, independently of the previously observed first-digit cancellation.

## New composed scalar certificate (conditional on first-digit L=0 mod q)

If L=0 mod q, set lambda=L/q mod q, using its canonical representative modulo q^2. Then W_q=0 mod q and (BRIDGE) gives the exact equality

  BOX: lambda+A = W_q/q (mod q).                             (QUOTIENT)

The previously proved diagonal q^2 palindrome lemma states (under the same premise)

  C_n0/q = 2^(2(N+r)) Z (lambda+A-B/6) (mod q),

with Z=sum_j u_j mod q and the inherited signed coefficient B. Therefore the *prime-square shadow base* admits the reduced exact criterion

  BOX: q^2 divides C_n0  iff  Z [W_q/q-B/6] = 0 (mod q).     (ONE-PORT)

This is useful even when the proposed epsilon-evaluation is unknown. It identifies the earlier observed congruence lambda+A=epsilon_q with the separate ordinary original-216 quotient W_q/q; it does *not* prove that this quotient always equals epsilon_q, or that B=6 epsilon_q always holds. A uniform solution needs the remaining B cancellation on Z!=0, or an alternative vanishing of Z, with full sign/carry provenance retained.

## Reproducibility and explicit verification scope

Companion file: research_notes/portable_direct/d25_low_digit_original_216_bridge_20261106.py.

The independent standard-library integer verifier forms W_q by the (1/2),(1/3),(2/3) Pochhammer coefficient recurrence modulo q^2, then independently computes L and U_i/K_i from the low-digit binomial harmonic and carry definitions. For all 194 primes 5<=q<=1200, it asserts (BRIDGE) and, when first-digit cancellation holds, (QUOTIENT). Result: 194/194 PASS.

Selected exact data (q, W_q mod q^2, lambda=L/q mod q, A mod q):
  (5,20,1,3), (7,7,0,1), (11,110,3,7),
  (13,13,8,6), (19,19,4,16), (373,373,209,165).

194 exact checks support the implementation, not universal first-digit or epsilon conjectures. The general algebraic BRIDGE is proved above under ordinary q-local finite arithmetic.

## BRC reuse and remaining mother objective

COMPOSE_APPLIED: retained signed source weights, prime valuation, three separately labeled carry channels, low/high Lucas digits, and their exact observer transport to W_q/q. Quotienting to the total happens only *after* the source-aware identity. This ordinary integer-shadow observation is distinct from the frozen native X6 H0/B0 / original Frobenius observer.

Next independent unit: find an exact evaluation of B in the Z!=0 branch, preferably a finite contiguity/telescoping certificate relating B to the Pochhammer quotient W_q/q, then return to frozen D25 F,H p^3 cancellation. The native p373 [X]U mod 139129, rank, Frobenius eta/kappa, odd branch, and independent review remain open. Never replace these native measurements with author-side shadow computations.