# D25 / SECOND-DIGIT-LIFT — exact two-zone p-adic jet for original A216 lower port

Date: 2026-10-30 Asia/Hong_Kong. Research lane: chatgpt-research-onhour-enterprise-math-20260923 (separate from maintenance). Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).

Status: AUTHOR-SIDE / PROVED EXACT REPARAMETERIZATION AND p-ADIC JET / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

## Proved rational-polynomial identity

Fix any prime p=6m+1 >=7. The original signed A216 coefficient is

\[
 a_n={\binom{2n}{n}^2\binom{3n}{n}\over216^n}
 ={(1/2)_n(1/3)_n(2/3)_n\over 2^n(n!)^3},\qquad
 A_{\rm low}=\sum_{n=0}^{3m}(6n+1)a_n.
\]

Use x=(-3m,-2m,-4m), lambda=(1/2,1/3,2/3), and define the finite rational polynomial

\[
P_m(T)=\sum_{n=0}^{3m}{6n+1\over2^n(n!)^3}\prod_{i=1}^{3}(x_i+\lambda_iT)_n
 =U_0+T U_1+T^2U_2+\cdots.\tag{J1}
\]

Since x+lambda*p=(1/2,1/3,2/3) *exactly*, P_m(p)=A_low in Q. Since n<=3m<p, every coefficient is p-integral, so

\[
 A_{\rm low}\equiv U_0+pU_1+p^2U_2\pmod {p^3}.\tag{J2}
\]

For 0<=n<=2m put
\[
 t_n={\prod_i(x_i)_n\over2^n(n!)^3},\
 L_n=\sum_{i,j<n}{\lambda_i\over x_i+j},\
 V_n=\sum_{i,j<n}{\lambda_i^2\over(x_i+j)^2}.
\]
For 2m<n<=3m remove just the factor (i=2,j=2m) from the product and sums (a star denotes that exclusion), and put
\[
 b_n={\prod^*_{i,j<n}(x_i+j)\over3\,2^n(n!)^3},\
 L_n^*=\sum^*_{i,j<n}{\lambda_i\over x_i+j}.
\]
Product differentiation gives, *as exact rational identities*,
\[
\begin{aligned}
U_0&=\sum_{n=0}^{2m}(6n+1)t_n,\\
U_1&=\sum_{n=0}^{2m}(6n+1)t_nL_n+
       \sum_{n=2m+1}^{3m}(6n+1)b_n,\\
U_2&=\underbrace{\sum_{n=0}^{2m}(6n+1)t_n(L_n^2-V_n)/2}_{U_{2,\rm int}}+
       \underbrace{\sum_{n=2m+1}^{3m}(6n+1)b_nL_n^*}_{U_{2,\rm cross}}.
\end{aligned}\tag{J3}
\]
Proof: all base factors for n<=2m are nonzero, so logarithmic product derivatives yield (L^2-V)/2. For n>2m exactly one base factor vanishes, (-2m+T/3) at j=2m, so this summand contains T/3 and its next coefficient is b_n L_n^*. No other base factor can vanish before n=3m. Every denominator retained after excluding the single zero is a p-unit (absolute base factor <p); thus reduction and exact quotient operations are valid.

## Application to the frozen LIFT (still open)

For target primes p=13 or 19 (mod24), consume accepted D24 first-digit A_low=p (mod p^2). By (J2), the quotient K=(U0+p U1-p)/p^2 is p-integral. Then
\[
 J=(A_{\rm low}-p)/p^2\equiv K+U_{2,\rm int}+U_{2,\rm cross}\pmod p.\tag{J4}
\]
Reuse the earlier middle-port reflection Q=C_m H_m from project commit 80e8d88d9cf1d1acab2ccd808fe18facfa003395. The remaining **paired** LIFT obligation is precisely
\[
 \boxed{K+U_{2,\rm int}+U_{2,\rm cross}+C_mH_m\equiv0\pmod p,\quad p=13,19\ (mod24).}\tag{J5}
\]
J5 has finite exact evidence below but has **not** been proved for every target prime. This new reduction exposes both original low-port second-jet sources as a terminating polynomial, rather than discarding either zone or extending the already singular middle kernel through its p-boundary.

## Executed exact evidence

Companion project Python guard d25_a216_low_two_zone_padic_jet_20261030.py was executed for all 115 primes 7<=p<1500, p=1 (mod6): term-by-term original 216 recurrence and polynomial jets agree modulo p^3, including the factor-zero threshold. J4/J5 pass for the 60 frozen-class primes. Independent raw integer-binomial recomputation agrees at p=7,13,19,31,37,373.

| p | K | U2 interior | U2 crossed | U2 total | J | C_m | H_m | Q |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 3 | 5 | 8 | 0 | 3 | 9 | 4 | 10 |
| 19 | 11 | 1 | 17 | 18 | 10 | 13 | 8 | 9 |
| 373 | 240 | 82 | 158 | 240 | 107 | 203 | 310 | 266 |

At p=373 the distinct second-jet sources contribute 82 and 158; 240+240=480=107 (mod373), while 203*310=266, so J+Q=373. Both second-jet zones matter even though the total happens to vanish at p=13. Finite regressions are not all-prime proof of J5.

BRC COMPOSE_APPLIED: carrier includes original n, signed 6n+1, valuation-zone label, parameter-jet degree 0/1/2 and source provenance; future operations are specialization T=p, addition, and p^2 quotient only after first-digit divisibility. Observer is the p-local scalar modulo p^3, then quotient modulo p. No claim of native X6/H0/B0 equivalence.

## Recovery / next science

Previously frozen D24, Guo-Zudilin B2304, B2 elimination, the reflected middle kernel, and the factor-three singular boundary result (b22324e4deaa6fd0f443d753237446af180a10f1) are consumed, not re-proved. Next exact action: build a two-source parameter-contiguous/WZ certificate on P_m(T) pairing U2 interior, U2 crossed and C_m H_m with K. Preserve the n=2m zero-factor boundary and the earlier s=m-1 pole residue ratio three. Prove J5 for all target primes or exhibit a verified original-integer counterexample.

Native priority #1559 remains fixed p373 original H0/B0 divided-power [X]U mod139129, rank, Frobenius/eta, signed Green/Hesse and kappa with independent reproduction. At 2026-10-30 Site gateway showed research_authority_granted=false, write_relay_enabled=false; checkpoint_list read returned ACCESS_DENIED. Actual native continuation/owner/session/CLAIM/run/original request IDs remain UNKNOWN in this Site context; no new formal operation or reattempt was issued. Support issue is intake, with no verified assigned executor. This is author-side evidence, not an admitted Result, not a Source checkpoint, and not a replacement native benchmark. P000, ACTIVE worldview, frozen scientific pin and Research/maintenance ownership are unchanged.
