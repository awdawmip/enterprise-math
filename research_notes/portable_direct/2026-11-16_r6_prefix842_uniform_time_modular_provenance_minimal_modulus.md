# PREFIX-842 — Minimal time-uniform modular readout for named BRC sources

Date 2026-11-16. Status: AUTHOR_PROVED / EXACT_MODULAR_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Scientific-input pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged). Predecessor: PREFIX-841, 5d2c9675d8e0c4b67f64b5b1ea882aa71feab727.

## Declared scope

Use PREFIX-841's auxiliary positive-integer Q-only BRC system: p=q>=1 original named sources of weights 1<=w_i<=W, one marked source with positive integer addition/removal weights a,b. Formal step t>=1 is a Q-operation count, not physical X6 heartbeat duration. Tagged one-deletion mass is D_i(t)=c_t w_i, with c_t=a^floor(t/2)b^floor((t-1)/2)>0. Names are publicly ordered and the observer has a provenance-sensitive linear output

$$
Z_W(t)=\sum_{i=1}^{p}W^{i-1}D_i(t)
=c_t(S_{p,W}+U),\quad
S_{p,W}=\sum_{i=1}^p W^{i-1},\quad U\in\{0,\dots,W^p-1\}.
$$

For a fixed positive integer modulus m, the receiver sees only Z_W(t) mod m and knows p,W,a,b,t. Here W>=2; the case W=1 is predetermined. Put N=W^p, C=ab, and define the C-free part of m by

$$
m_{\perp C}=\frac{m}{\prod_{\ell\mid C}\ell^{v_\ell(m)}}.
$$

The product ranges over distinct prime divisors of C (an empty product is one). Thus gcd(m_{\perp C},C)=1. All divisibility is exact positive-integer arithmetic.

## Theorem 842.1 — Sharp arbitrarily long observation criterion

The *same* fixed modular readout Z_W(t) modulo m uniquely distinguishes all N labeled assignments for every integer t>=1 if and only if

$$
\boxed{m_{\perp (ab)}\ge W^p.}
$$

**Proof.** PREFIX-841 proved that at any fixed t the map is injective exactly when m/gcd(m,c_t)>=N. Since a,b are positive integers, c_t divides c_(t+1), so gcd(m,c_t) increases by divisibility and m/gcd(m,c_t) is nonincreasing in t. For each prime ell dividing C=ab, v_ell(c_t)=floor(t/2)v_ell(a)+floor((t-1)/2)v_ell(b) tends to infinity. For primes not dividing C this valuation stays zero. Consequently gcd(m,c_t) eventually equals the full C-primary divisor of m, and m/gcd(m,c_t) eventually equals m_perpC. It is never smaller than m_perpC. Applying the fixed-time criterion proves both directions. QED.

## Theorem 842.2 — Exact smallest uniform modulus and a constructive bound

Among all fixed moduli m>=1 with uniform-time label injectivity, the minimum is

$$
\boxed{m_\infty^\star=\min\{m\in\mathbb Z_{\ge N}:\gcd(m,ab)=1\}.}
$$

It always exists. Writing rad(C) for the product of distinct prime divisors of C, with rad(1)=1, gives the explicit finite bound

$$
N\le m_\infty^\star\le N+\operatorname{rad}(ab)-1.
$$

**Proof.** If m is admissible, its C-free part d=m_perpC satisfies d>=N by Theorem 842.1, d<=m and gcd(d,C)=1. Replacing m by d therefore preserves admissibility while not increasing the modulus. Conversely any m>=N coprime to C has m_perpC=m and is admissible. This proves the exact minimum. In any rad(C) consecutive integers there is one congruent to 1 modulo rad(C). That integer is coprime to C and lies in [N,N+rad(C)-1], giving the bound. QED.

Examples: for N=4, a=2, b=1 the minimum fixed modulus is 5, and modulus 4 fails from t=2. For N=9, a=2, b=3 the minimum is 11. For N=64, a=2, b=3 the minimum is 65. If gcd(W,ab)=1, m_infty_star=N, so the information-theoretically minimal normalized alphabet is realized by the raw modulo-N observer for every t.

## Theorem 842.3 — Exact finite-horizon minimum and stabilization

For a specified nonempty finite horizon t=1,...,T, let c_T=a^floor(T/2)b^floor((T-1)/2). The same fixed modulus m is lossless at **all** times in the horizon if and only if

$$
\boxed{\frac{m}{\gcd(m,c_T)}\ge N.}
$$

Hence the exact minimum is

$$
m_T^\star=\min\{m\ge1:m/\gcd(m,c_T)\ge N\}.
$$

The sequence m_T_star is nondecreasing in T, bounded above by m_infty_star, and equals m_infty_star for all sufficiently large T.

**Proof.** Because c_t divides c_T for t<=T, the fixed-time injectivity condition is weakest at T. This proves the equivalence. Its feasible sets shrink monotonically with T, yielding monotonicity of the minima; m_infty_star is feasible at every T. For finite stabilization put K=m_infty_star-1. For each prime ell dividing ab require v_ell(c_T)>=floor(log_ell K). At such T, for every m<=K the whole C-primary divisor of m divides c_T, so m/gcd(m,c_T)=m_perpC<N by minimality of m_infty_star. All smaller moduli fail, and m_infty_star succeeds. Since each listed valuation grows indefinitely, such a T exists. QED.

For N=4, a=2, b=1 the optimal finite-horizon moduli are m_1_star=4 and m_T_star=5 for every T>=2. For N=9,a=2,b=3 the sequence starts 9,9,11 and remains 11 thereafter.

## Proposition 842.4 — Bounded-register exact modular propagation

Let v_t be the complete vector of named-subset/marked-bit positive weighted masses under the BRC Q transition. For any modulus m, let bar-v_t denote reduction of every component modulo m. Computing the same weighted Q transitions directly over Z/mZ gives exactly bar-v_t at every t, because the quotient map from nonnegative integers to Z/mZ preserves addition and multiplication.

Accordingly, the tagged output Z_W(t) mod m can be evaluated by carrying only modular state masses and powers W^(i-1) mod m. For a fixed uniformly admissible m=m_infty_star, gcd(c_t,m)=1 for all t, so the receiver computes

$$
U\equiv (Z_W(t)\bmod m)c_t^{-1}-S_{p,W}\pmod m,
$$

takes its unique representative in [0,N-1], and decodes the p base-W digits of U. Thus the **per-state mass register and one output register** can use ceil(log2 m_infty_star) bits independently of t. This is an exact residue computation, not an interpretation of residues as positive masses, and the separate named-state count/transition work remains. In an explicit subset DP the state space can have up to 2^(p+1) typed keys and O(t p 2^p) modular transition operations.

## Exact independent tests

An accompanying Node/JavaScript BigInt program checks all p=1..4, W=2..4, a,b=1..4 (192 parameter families). For T=1..12 it exhaustively finds each least finite modulus and checks the stated monotonicity and uniform bound (2,304 horizons; 93,413 failed smaller-modulus candidates). It evaluates the C-free part of every modulus through m_infty_star+7 (9,340 checks) and confirms its equality to m/gcd(m,c_100) on the enumerated parameter range. It independently enumerates residues in small domains (5,780 comparisons).

More strongly, for p=1..3, W=2..3, **every ordered weight tuple** in [1,W]^p, a,b=1..3 and t=1..6, the checker propagates the full legal named-state Q graph **directly modulo the computed minimum uniform modulus**, obtains the tagged output and recovers every weight via modular inverse and positional digits. This checks 477 configurations, 2,862 time frames and 7,344 recovered digits without using the closed D_i formula to generate the state masses. All exact assertions returned ALL_EXACT_ASSERTIONS_PASSED.

## Meaning and frontier

PREFIX-841 established a single-time exact modular criterion; PREFIX-842 identifies **the least constant-size modulus across arbitrary time**, an exact finite-horizon alternative, a computable stabilization certificate, and an implementation that avoids time-growing integer mass registers under the explicitly stronger tagged observer. This is a BRC typed modular quotient for a specified output, not an unrestricted quotient for arbitrary observers or native physical coupling.

Next discriminating unit: identify whether a permitted native Cell/Link/Port event provides the required named one-deletion output, with provenance, resource and time semantics. Then compare the mathematical constant-width residue observer with the actual native observation contract. Preserve the separate q>=5 minimal nonnegative Q carrier and the uniform even-T recollision bound questions.

Research provenance: independent auxiliary publication. Shared X6 Task CLAIM, formal Result, independent Review and Foundation admission are separate.
