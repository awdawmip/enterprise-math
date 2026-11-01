# D25 on-hour — a finite harmonic formula for the second digit of the terminal Green normalization

**2026-10-31; AUTHOR-SIDE / EXACT PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** Own logical Research lane: chatgpt-research-onhour-enterprise-math-20260923. Separate from the hourly Research lane chatgpt-research-hourly-enterprise-math-20260923 and control maintenance chatgpt-hourly-enterprise-math-20260921. Parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3; P000 ACTIVE unchanged.

## Reused source

The **other hourly lane** proved the exact source identity \(\Gamma_\ell=(-1)^\ell/(18S_\ell)\), \(S_\ell=\sum_{i=0}^{\ell}\binom{\ell}{i}\binom{2\ell}{i}\binom{6\ell+i}{3\ell}\), and \(\Gamma_\ell\equiv1/18\pmod p\) in research_notes/portable_direct/20261031_hourly_d25_split_green_log_residue_18.md (commit 5a19591c6841efd21acd1bba1b123d2d90ab66ff). These are CONSUMED, not reattributed or reproved. The original on-hour finite Green source is research_notes/portable_direct/20261031_onhour_d25_finite_rational_green_eval_terminal_punit.md; its exact zero-residue input remains unchanged.

## Theorem A — the next p-adic terminal digit

For every prime \(p=6\ell+1\ge7\), set \(M=3\ell\), \(H_M=\sum_{j=1}^{M}j^{-1}\), and define
\[
\mathcal H_\ell=-H_M+
\sum_{i=1}^{\ell}(-1)^i
\frac{\binom{\ell}{i}\binom{2\ell}{i}}{i\binom{M}{i}}\in\mathbb Z_{(p)}.
\]
All denominators are p-units since \(M<p\). Then
\[
\boxed{S_\ell\equiv(-1)^\ell(1+p\mathcal H_\ell)\pmod{p^2}},\qquad
\boxed{\Gamma_\ell\equiv18^{-1}(1-p\mathcal H_\ell)\pmod{p^2}}. \tag{A}
\]

**Exact proof.** The \(i=0\) term satisfies \(\binom{p-1}{M}=(-1)^M\prod_{j=1}^{M}(1-p/j)\equiv(-1)^M(1-pH_M)\pmod{p^2}\). For each \(1\le i\le\ell\), the numerator of \(\binom{p-1+i}{M}\) has exactly one factor \(p\), located at offset \(i-1\); all other factors reduce to \((i-1)!(-1)^{M-i}(M-i)!\). Thus
\[
\frac1p\binom{p-1+i}{M}\equiv
\frac{(-1)^{M-i}}{i\binom{M}{i}}\pmod p.
\]
Summing and using \((-1)^M=(-1)^\ell\) proves the first identity in (A). Substitution into the inherited **exact** \(\Gamma_\ell=(-1)^\ell/(18S_\ell)\) proves the second. These formulas hold for EVERY prime in the claimed class; checking examples is not the argument.

## Theorem B — safe mod-p Green scalar compression, with quantified failure at mod-p² source level

Preserve the actual original zero/first-jet polynomials \(J_0,J_1\), the operator \(\theta=z\partial_z\), and the distinct signed reflector \(R_p\). Define
\[
F_{\rm low}=J_0[(\theta/2-2\ell/3)J_1+J_0/18],\quad
F_{\rm exact}=F_{\rm low}-\Gamma_\ell z^{p-1}J_0,\quad
F_\sharp=F_{\rm low}-z^{p-1}J_0/18 .
\]
Write \(f_k=[y^k]F_{\rm exact}(1-y)\), \(f_k^\sharp=[y^k]F_\sharp(1-y)\) for \(0\le k\le7\ell\); the previously PROVED exact original source has \(f_M=0\) as a rational number. Define finite readouts \(E=\sum_{k\ne M}f_k(1-2^{M-k})/(k-M)\) and \(E^\sharp=\sum_{k\ne M}f_k^\sharp(1-2^{M-k})/(k-M)\). Since \(0<|k-M|\le4\ell<p\) and (A) shows \(\Gamma_\ell-1/18\in p\mathbb Z_{(p)}\),
\[
\boxed{E^\sharp\equiv E\pmod p}. \tag{B}
\]
This is a legitimate precision-typed shortcut for the *finite E readout* needed in the remaining LIFT scalar, not an equivalence of full sources.

The omitted logarithmic/residue port is nontrivial:
\[
\boxed{f_M^\sharp=\frac{1-(-1)^\ell S_\ell}{18}
\equiv-\frac{p\mathcal H_\ell}{18}\pmod{p^2}}. \tag{C}
\]
**Proof.** The source difference is \((\Gamma_\ell-1/18)z^{p-1}J_0\), proving (B) by p-local finite summation. The exact coefficient \([y^M](1-y)^{p-1}J_0(1-y)=(-1)^M S_\ell\), by the existing terminal binomial source. Hence \(f_M^\sharp=(\Gamma_\ell-1/18)(-1)^M S_\ell=(1-(-1)^\ell S_\ell)/18\), and (A) proves (C). A rational derivative has no \(dy/y\) residue: wherever (C) is nonzero, \(F_\sharp(1-y)y^{-M-1}dy\) has no rational primitive, whereas the **complete original source** has zero residue exactly. Mod-p scalar equality does not license exact Green integration or mod-p² source-level replacement.

## Exact executed checker and witnesses

The standard-library integer program d25_terminal_gamma_second_digit_20261031.py executed all **94** primes \(7\le p\le1200\) with \(p\equiv1\bmod6\); it independently constructed \(S_\ell\) by integer binomial sums and \(\Gamma_\ell=20\ell^2w_{p-1}\) from the inherited factorial expression, verifying both (A) and (C), no floating-point computation. Selected \((p,\ell,\mathcal H_\ell\bmod p,\Gamma_\ell\bmod p^2,f_M^\sharp\bmod p^2,f_M^\sharp/p\bmod p)\):
- \((13,2,4,138,91,7)\);
- \((19,3,3,37,57,3)\);
- \((67,11,65,2252,1005,15)\);
- \((373,62,192,127421,88774,238)\).

At \(p=373\), the scalar shortcut is valid mod 373, but its source contains a nonzero log residue \(88774=373\cdot238\bmod139129\). This is a concrete higher-precision information-loss witness. The finite check is not an all-prime LIFT proof, a formal admission, or native H0/B0 execution.

## Current mathematical frontier and real control boundary

The frozen original objective remains to prove \(A_p=\sum_{n=0}^{p-1}(6n+1)\binom{2n}n^2\binom{3n}n216^{-n}\equiv p\bmod p^3\) for every \(p\equiv13,19\bmod24\), or provide an exact counterexample. Previously derived, source-sensitive residual:
\[
(A_p-p)/p^2\equiv(L_0N_0-1)/p+L_0N_1-12\,2^{-3\ell}E_p-R_p\pmod p.
\]
Only E may be replaced by E-sharp mod p; the carry, first-jet and signed reflector remain distinct. Next decisive unit: a JOINT finite WZ/CM cancellation (not another separate Green or R auxiliary lemma), with nonzero source checks at p=19,67,373.

Original-class native benchmark enterprise-math#1559 is **NOT_EXECUTED/PENDING_OWNER**: fixed373 H0/B0 divided-power [X]U mod139129, actual rank, semilinear Frobenius/eta, signed Green/Hesse, κ and independent replication remain with the existing support intake. Research-onhour read-only recovery kimi-query-bridge#6632 reported active session pointer but no own CLAIM/run; existing request #6633 FAILED UPSTREAM_CODE_REVIEW_REQUIRED and must not be replayed. Gateway status in this research run: research_authority_granted=false, executor_binding_configured=false. No native checkpoint/Result/review, research activity registration or official task admission is claimed by this author-side document. Frozen scientific source pin, current task schedule and notifications unchanged.
