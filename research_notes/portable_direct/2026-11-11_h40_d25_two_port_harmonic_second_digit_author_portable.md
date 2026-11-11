# D25/LIFT: universal exact two-port harmonic expansion modulo p²

2026-11-11. Status: \`AUTHOR_PROVED / EXACT_1227_PRIME_CHECK / UNREVIEWED / NOT_ADMITTED\`. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Author-only portable mathematics; no native H0/B0 Task checkpoint, Result or review authority is claimed.

For **every prime p≥5**, write \`p=6m+1+4e\`, \`e=0 or 1\`. Let

\`K_p(X)=Σ_{k=0}^m binom(m,k) binom(2m+e,k) X^k\`,
\`A_p=K_p(1/2)\`,
\`B_p=(1−6e) K_p(1/2)+6 K'_p(1/2)\`.

Introduce \`alpha=−(1+4e)/6\`, \`beta=−(1+e)/3\`, and for \`0≤k≤m\`,
\`t_k=binom(alpha,k)binom(beta,k)2^{-k}\`,
\`H_k=Σ_{j=0}^{k−1} (1/(6j+1+4e)+1/(3j+1+e))\`, \`H_0=0\`,
\`w_k=1−6e+12k\`.
All rational denominators are p-adic units because \`p≥5\`, \`k≤m<p\` and \`j<m\`.

**Theorem (exact mod-p² two-port second digit):** put
\`S_A=Σt_k\`, \`E_A=Σt_k H_k\`,
\`S_B=Σw_k t_k\`, \`E_B=Σw_k t_k H_k\`.
Then in \`Z_(p)/p²\`,

\`A_p ≡ S_A−p E_A (mod p²)\`, \`B_p ≡ S_B−p E_B (mod p²)\`.

If a port \`P=A\` or \`B\` is zero mod p, its base sum \`S_P\` is also zero mod p, and the next digit is

\`P/p ≡ (S_P/p)−E_P (mod p)\`.

**Thus an already p-vanishing port is zero mod p² exactly when its base quotient and harmonic correction coincide modulo p.** Retain these separate base/harmonic observations, branch e and port label until the final subtraction.

### Proof (all primes)

Use exact rational equalities \`m=alpha+p/6\`, \`2m+e=beta+p/3\`. For every \`k≤m\` each \`alpha-j\` and \`beta-j\` with \`j<k\` is a p-unit. Consequently

\`binom(alpha+p/6,k) = binom(alpha,k)∏_{j<k}(1+p/[6(alpha-j)])\`
\`≡ binom(alpha,k)[1−pΣ_{j<k}(6j+1+4e)^{-1}] (mod p²)\`.

Likewise,
\`binom(beta+p/3,k) ≡ binom(beta,k)[1−pΣ_{j<k}(3j+1+e)^{-1}] (mod p²)\`.

Multiplying and applying the weight \`w_k\` gives
\`binom(m,k)binom(2m+e,k)2^{-k} ≡ t_k(1−pH_k) (mod p²)\`.
Sum for A and B; divide the p-vanishing port by p for the next-digit statement. QED.

The exact recurrences
\`t_{k+1}=t_k(6k+1+4e)(3k+1+e)/[36(k+1)^2]\` and
\`H_{k+1}=H_k+(6k+1+4e)^{-1}+(3k+1+e)^{-1}\`
allow one-pass explicit computation of the preserved port/harmonic observer.

### Exact exceptional-cancellation certificates

| p | e | m | zero port | \`S_P/p mod p\` | \`E_P mod p\` | \`P/p mod p\` |
|---:|---:|---:|:---:|---:|---:|---:|
|149|1|24|B|26|26|0|
|211|0|35|A|183|183|0|
|101419|0|16903|A|20094|20094|0|

For the newly found p=101419 (19 mod24), \`S_A mod p²=2037913386=20094p\` and \`E_A mod p=20094\`; the prior independent higher-digit computation gives \`v_p(A)=2\`, \`A/p² mod p=73632\`. The distinct original weighted observation remains \`W_p≡p+56544p³ (mod p⁴)\` at this prime.

The companion independent Python verifier checks both formulas against a direct factorial/binomial method for **all 1227 primes 5≤p≤10000**, plus the three p² exceptional cancellations. These finite checks supplement the universal p-adic product proof; they do not establish the still-open all-prime Legendre selector.

The native frozen D25/LIFT completion target is \`Delta_p=(G_p h−1)/p ≡ R_p (mod p)\` for all \`p≡13,19 (mod24)\`, requiring original-class H0/B0 rank, semilinear direction and normalization eta. The auxiliary two-port harmonic observation is a proposed comparison interface, not a native equivalence theorem or substitute execution. Earlier UR first-digit results remain settled; authentic V2 four-file source remains unresolved at 94,687 bytes, SHA-256 \`4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76\`.
