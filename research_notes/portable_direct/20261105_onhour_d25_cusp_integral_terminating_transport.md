# D25: p-integral CM-cusp terminating triangular transport for the original 216/2304 models

**Date:** 2026-11-05. **Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. **Publication:** TP2-B6F4FC938FF94941C1B7. **Frozen science:** c47e13e4aba0e006366f989d6334d443f6333ae3. **Research lane:** chatgpt-research-onhour-enterprise-math-20260923, distinct from the maintenance lane. **Classification:** AUTHOR-SIDE EXACT DERIVATION + EXECUTED FINITE REGRESSION; UNREVIEWED / NOT_ADMITTED. No native Result or H0/B0 calculation.

## 1. Previously established input, with provenance

Consume the prior author-side high-positive-CM analytic transform in research_notes/portable_direct/20261105_onhour_d25_positive_cm_branch_exact_period_transport.md (itself UNREVIEWED/NOT_ADMITTED). Its Gauss/Clausen formulation supplies the formal-series identity

  A(z) = M(z)^2 B(t(z)),

where A(z) = 3F2(1/2,1/3,2/3;1,1;z) = sum alpha_n z^n, B(t) = 3F2(1/2,1/4,3/4;1,1;t) = sum beta_k t^k, and

  u=(1+sqrt(1-z))/2, v=(1+sqrt(1-t))/2,
  J3(u)=27(1+8u)^3/(u(1-u)^3),
  J4(v)=64(1+3v)^3/(v(1-v)^2),
  J3(u)=J4(v),
  M^2=3t sqrt(1-t)/(2z sqrt(1-z) t').

The selection is the positive high-CM branch. We do not identify this ordinary analytic transform with native H0/B0 crystalline Frobenius. The earlier exact Puiseux half-integer-coset cancellation is consumed, not reproved.

## 2. New theorem: all coefficients are p-integral without branch-discriminant division

Work in R=Z[1/6] and the formal variable s, and substitute z=s^2/3, t=s^3 U(s). Put

  G(z)=z^3 J3((1+sqrt(1-z))/2)
      =432(5+4 sqrt(1-z))^3(1+sqrt(1-z))^2,
  H(t)=t^2 J4((1+sqrt(1-t))/2)
      =64(5+3 sqrt(1-t))^3(1+sqrt(1-t)).

Both belong to R[[z]], resp. R[[t]], with G(0)=1259712=2^6*3^9, H(0)=65536=2^16. The exact algebraic equation is

  27 G(s^2/3) U(s)^2 = H(s^3 U(s)),    U(0)=32/729.

**Theorem A.** This equation has a unique solution U(s) in R[[s]] with that constant term. Moreover,

  N(s) := [3 U(s) sqrt(1-s^3 U(s))] /
          [sqrt(1-s^2/3) (3 U(s)+s U'(s))]

lies in R[[s]], has N(0)=1, and the exact *formal* identity is

  A(s^2/3) = N(s) B(s^3 U(s)).

**Proof.** In R, 2,3,G(0),H(0),U(0) are units. The normalized formal square root sqrt(1+x) exists by coefficient recursion requiring only division by 2. Rewriting the algebraic equation as

  U(s) = (32/729) sqrt( (H(s^3 U(s))/65536)
                         (G(0)/G(s^2/3)) )

specifies the positive unit root. Its dependence on U(s) inside H begins at order s^3, so successive substitution is s-adically contractive and determines each coefficient uniquely in R. Since 3U(0) and both square-root constants are units, the displayed N also lies in R[[s]]. The preceding high-CM analytic identity supplies A=N B after substitution; both sides expand as formal powers of s, so the identity is exact coefficientwise. No division by the CM conjugate difference j_+-j_-=2*1707264*sqrt(2) occurs, including at primes 13 and 19 where that difference is divisible by p.

For reproducibility the rational coefficients begin as

  U(s)=32/729 + (56/6561)s^2 - (416/531441)s^3 + ...,
  N(s)=1+(1/27)s^2-(1/243)s^3+(5/972)s^4+... .

These coefficients are formal expressions. They preserve the odd s-coset of the positive high branch rather than dropping it prematurely.

## 3. The finite triangular transport, valid for every finite index

Define for integers n,k >=0

  T[n,k] = 9^k (3/2)^n [s^(2n)] ( N(s) (s^3 U(s))^k ).

As t(s)^k is divisible by s^(3k), T[n,k]=0 whenever 3k>2n. Comparing the s^(2n) coefficient of the formal identity proves the exact rational identity

  alpha_n/2^n = sum_{k=0}^{floor(2n/3)} T[n,k] beta_k/9^k.

**Theorem B.** Every T[n,k] belongs to Z[1/6]. Consequently, for every prime p>3 this is a p-integral finite terminating identity. Its coefficients are built without p-dependent branch denominators. The first nontrivial exact rational checks include T[0,0]=1, T[1,0]=1/18, T[2,0]=5/432, T[3,1]=-64/2187, and T[3,2]=128/243. The signed odd-power contributions to N and t are included in each extraction.

For any prime p>3 set h=(p-1)/2, K=floor(2(p-1)/3), and let

  a_n=alpha_n/2^n=binom(2n,n)^2 binom(3n,n)/216^n,
  b_k=beta_k/9^k=binom(2k,k)^2 binom(4k,2k)/2304^k,
  W_p=sum_{n=0}^{p-1}(6n+1)a_n,
  V_p=sum_{k=0}^{p-1}(8k+1)b_k,
  V_h=sum_{k=0}^h(8k+1)b_k.

It follows **exactly over Q**, before taking p-adic residues, that

  W_p - V_h =
    sum_{k=0}^{K} b_k ( sum_{n=0}^{p-1}(6n+1)T[n,k]
                         - (8k+1)*1_{k<=h} ).

Call the right-hand side E_p. The previously published and independently sourced 2304 half-truncation congruence V_p ≡ V_h (mod p^3) then yields the **strict, exact-interface certificate**

  W_p - V_p ≡ E_p  (mod p^3).

The original frozen target for p ≡13 or 19 (mod24), namely Delta_p-R_p≡0 (modp), is thus equivalent, after consumption of the previously aligned scalar interface, to E_p≡0 (modp^3). This is a *finite p-integral terminating certificate*, not yet a proof that E_p vanishes for all target primes. The outer index K is strictly smaller than p-1 for p>3. No asymptotic-complexity improvement is asserted: construction of all T entries has a cost and can involve both even/odd cosets.

## 4. Exact arithmetic verification and retained signed shells

The companion checker evaluates U,N,T through polynomial arithmetic over Z/p^3Z, verifies the coefficient identity against **independent raw integer binomial coefficients** at each n<p, and checks W, V_h, V and E_p. The executed domain is p=5,7,11,13,17,19,23,31,37 (nine primes, zero assertion failures), using no floating-point arithmetic. All nine satisfy E_p ≡ W_p-V_p (modp^3); that identity has the formal proof above. Their observed E_p values happen to be 0, which is finite regression only.

At p=13, with p^3=2197, h=6, K=8 and native-2304 valuation endpoint J=floor((3p-1)/4)=9, the two signed upper contributions are 1183 and 1014, summing to 0 (mod2197), while W_p=V_p=13.

At p=19, with p^3=6859, h=9, K=12, J=14, they are 1083 and 5776, summing to 0 (mod6859), while W_p=V_p=19. Individually the contributions are not zero. This retains the 2304 signed overhang and the 216 triangular K-boundary, instead of silently identifying infinite analytic and finite p-adic truncations.

The reproducible checker is d25_cusp_integral_terminating_transport_20261105.py. Note: it only computes portable integer arithmetic; the native fixed 373 H0/B0 divided-power benchmark remains NOT_EXECUTED and PENDING_OWNER under Issue #1559.

## 4a. Second exact unit: a signed two-block witness prevents columnwise shortcuts

The scalar E_p is not a sum of individually p^3-divisible k-columns. Let

  e_{p,k}=b_k ( sum_{n<p}(6n+1)T[n,k] - (8k+1)*1_{k<=h} ),

and let c=ceil(p/4). The exact original 2304 factorial valuation v_p(b_k)=floor(4k/p) for 0<=k<p shows that k<c is the p-unit carrier, while k>=c carries at least one p. The **signed** two-block decomposition is

  E_p = sum_{k<c} e_{p,k} + sum_{c<=k<=K} e_{p,k},

without replacing a sum by an absolute value or deleting either observer.

Direct independent integer-binomial/program evaluation with the same exact T kernel gives:

| p | c | e_{p,0} mod p^3 | sum_{k<c} e_{p,k} mod p^3 | sum_{k>=c} e_{p,k} mod p^3 | E_p mod p^3 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 4 | 646 | 741 | 1456 | 0 |
| 19 | 5 | 3081 | 950 | 5909 | 0 |

Here e_{13,0}=646 is nonzero even modulo 13 and e_{19,0}=3081 is nonzero even modulo 19. This is an exact **finite counterexample** to termwise or columnwise p-divisibility as a possible shortcut. Both low and high blocks have nonzero residues modulo p^3, and their signed sum cancels. At these two test primes the low block is 13*57 and 19*50, respectively; the high block repairs the higher digits. Therefore a viable *uniform* proof of the frozen target through this T kernel must exhibit cancellation **across** k-columns, such as a telescoper with explicit k-boundary; neither a per-column divisibility claim nor a positive-mass quotient suffices. This negative conclusion is scoped only to the proposed termwise shortcut and the displayed exact witnesses, not to the target congruence.

The same checker was extended to emit c, e_{p,0}, and both block residues for all nine test primes, and was rerun with successful assertions. No larger sample is needed to refute the termwise shortcut.

## 5. Frontier, reuse and evidence scope

**Reused:** published author-side positive CM analytic transform and Puiseux signed branch; original 216/2304 arithmetic coefficients; published 2304 full-vs-half mod p^3 theorem; the accepted first-digit and previously source-aligned Delta-R interface at the exact frozen scientific scope.

**New:** all-prime p-integrality of a formal high-CM cusp change of variable and gauge; a proven finite triangular transport at every integer n, with a uniform outer truncation K=floor(2(p-1)/3); its signed mod-p^3 scalar residual E_p.

**BRC observer:** retain original model tags, integer coefficient, p-adic valuation, s-even/s-odd Puiseux provenance, high/low CM branch, Frobenius character as a separately sourced observer, signed (6n+1)/(8k+1) weights, both half endpoint h and triangular support K, and final 2304 shell ending at J. Information is collapsed only after exact coefficient extraction or the stated full-vs-half mod-p^3 theorem.

**Smallest next math action:** find a uniform finite summation/creative-telescoping law for the *specific* T[n,k] kernel proving E_p≡0 (modp^3) for p≡13,19 (mod24). The p=13/19 rational integer witness above fixes the required boundary signs; search for a recurrence in n,k and a p-divisible certificate. If this route stalls, test exact local obstruction rather than enlarging auxiliary CM identities. The parent native H0/B0 benchmark is a distinct authorized-executor requirement in Issue #1559. No formal Source CLAIM/run/Result or review/admission is asserted.
