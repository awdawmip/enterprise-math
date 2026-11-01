# D25 / SECOND-DIGIT-LIFT: original A216 two-moment source split (2026-10-30)

**Status:** AUTHOR-SIDE RESEARCH / PROVED CONDITIONAL TRANSFER AND EXACT FIXED-PRIME COUNTEREXAMPLES / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED. This document is not a canonical Source checkpoint, claim, freeze, Result, or native H0/B0 experiment.

**Lane:** `chatgpt-research-onhour-enterprise-math-20260923` (TASK_RESEARCH), separate from maintenance. **Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. **Mother:** `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Immutable scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Preserve P000 and ACTIVE HEARTBEAT_WORLD; this is ordinary scalar arithmetic only, not an indigenous H0/B0 operator result.

## Exact original source and a new moment-port decomposition

For each prime p>3 set

\[
a_n=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\qquad
S_{0,p}=\sum_{n=0}^{p-1}a_n,\qquad
S_{1,p}=\sum_{n=0}^{p-1}n a_n.
\]

All denominators are p-units. Keep the original n and coefficient, as distinct *zeroth moment* and *first moment* ports. The previously fixed weighted A216 observable is **exactly**

\[
A_p=\sum_{n=0}^{p-1}(6n+1)a_n=S_{0,p}+6S_{1,p}.
\]

Termwise binomial arithmetic gives the precise interface to an already published, otherwise differently packaged p-adic theorem:

\[
a_n=\frac{\binom{2n}{n}\binom{-1/3}{n}\binom{-2/3}{n}}{8^n}.\tag{1}
\]

This holds in \(\mathbb Z_{(p)}\) for p>3, term by term; it is not a redefinition of A216. The 2015 result of Zhi-Hong Sun, *Note on super congruences modulo p²*, arXiv:1503.03418, proves for an odd prime p, p-integral a, and unit m:

\[
\sum_{n=0}^{p-1}\binom{2n}{n}\binom a n\binom{-1-a}n/m^n\equiv0\pmod p
\quad\Longrightarrow\quad\equiv0\pmod{p^2}.
\]

Specializing the **exact** source (1) to \(a=-1/3,m=8\), we obtain the all-prime **conditional theorem**

\[
\boxed{S_{0,p}\equiv0\pmod p\quad\Longrightarrow\quad S_{0,p}\equiv0\pmod{p^2}.}\tag{2}
\]

This implication is proved by a published theorem. The antecedent for **every** p in the frozen residue classes requires its own uniform CM/Hasse proof or exact accepted Source certificate; finite checks do not supply that infinite-quantifier proof. Historic discussion of this \(216\) unweighted supercongruence appears, e.g., Zhi-Hong Sun's 2013 Legendre-polynomial research, and a residue-class \(p^3\) strengthening is explicitly formulated as *Conjecture 5.28* in the 2022 AIMS Mathematics survey, not used here as a theorem.

For p≡13,19 mod24, reuse the already accepted D24 first-digit relation \(A_p\equiv p\pmod{p^2}\). Combining it with (2), **conditional only on the mod-p antecedent**, rigorously proves the first-moment lift

\[
\boxed{S_{1,p}\equiv\frac p6\pmod{p^2}.}\tag{3}
\]

More generally with a prior certified \(A_p\equiv p\chi_p\pmod{p^2}\), the consequent is \(S_{1,p}\equiv p\chi_p/6\pmod{p^2}\). Note that \(p/6\) denotes a p-adic integer (multiplication by the inverse of 6 modulo the stated modulus).

If the antecedent holds, define **separately sourced, integral** second-digit ports

\[
U_p=\frac{S_{0,p}}{p^2}\bmod p,\qquad
V_p=\frac{S_{1,p}-p/6}{p^2}\bmod p.
\]

These two values remain attached to their original n-indexed summands and weighting operators \(1\) and \(n\). The original frozen second-digit assertion admits a second exact pair-port formulation

\[
\boxed{A_p\equiv p\pmod{p^3}\iff U_p+6V_p\equiv0\pmod p.}\tag{4}
\]

This is a proven conditional equivalence, **not** a new proof of the target all-prime cancellation. It complements the previously established original cutoff-based \(J_p+C_mH_m^{reg}\) target and does not replace its frozen source/observer contract.

## Strict finite counterexamples to independent second-digit zero

Direct original integer binomial sums with modulus p³ give:

| p | S0 (mod p³) | S1 (mod p³) | p/6 (mod p³) | U=S0/p² (mod p) | V=(S1-p/6)/p² (mod p) |
|---:|---:|---:|---:|---:|---:|
| 13 | 1859 | 1157 | 1833 | 11 | 9 |
| 19 | 2888 | 665 | 5719 | 8 | 5 |
| 373 | 9878159 | 32950447 | 43245993 | 71 | 299 |

Every row has \(U\ne0\), \(V\ne0\), but \(U+6V=0\pmod p\). In particular at p=13,

\[
S_{0,13}=11\cdot13^2\pmod{13^3},\quad
S_{1,13}-13/6=9\cdot13^2\pmod{13^3},\quad
11+6\cdot9=65=5\cdot13.
\]

Therefore both candidate shortcuts \(S_0\equiv0\pmod{p^3}\) and \(S_1\equiv p/6\pmod{p^3}\) **fail already at p=13**; the original LIFT requires their signed source cancellation. This is a mathematically rigorous fixed-prime counterexample against those two **stronger** claims, not a counterexample to LIFT.

## Executed finite regression (not an infinite-prime proof)

The companion Python standard-library checker uses the exact modular ratio

\[
\frac{a_{n+1}}{a_n}=\frac{(2n+1)(3n+1)(3n+2)}{36(n+1)^3}\qquad(0\le n<p-1),
\]

whose denominator is invertible modulo p³. For p=13,19,373, a second independent \(\binom{2n}{n}^2\binom{3n}{n}\) integer route was compared coefficient-sum-wise. Executed on **all 667 primes 5≤p<5000**: **334** in p mod24 ∈{13,17,19,23} satisfied \(S_0=0\pmod{p^2}\) and \(6S_1=p\chi_p\pmod{p^2}\); **166** in the frozen p mod24 ∈{13,19} satisfied \(A_p=p\pmod{p^3}\). No exceptions in these finite ranges. These checks certify precisely the enumerated cases; the published transfer handles (2), the remaining all-prime antecedent and third-digit cancellation remain proof obligations.

## Reuse / next exact action

First, locate a current accepted CM/Hasse proof for \(S_{0,p}\equiv0\pmod p\) in both frozen classes, or prove that statement without importing a conjectural p³ form. Then construct a **paired finite p³ WZ/parameter identity** for \(U_p+6V_p\), preserving 1 and n source weights. Compare it to the previously frozen low-vs-middle regular-tail certificate before claiming anything new; keep the signed/odd observer. Use the first-principles n-recurrence above for portable reproductions.

**Highest native benchmark gap:** Enterprise Math issue #1559, `https://github.com/awdawmip/enterprise-math/issues/1559`, remains the original-class fixed p=373 H0/B0 divided-power [X]U modulo 139129, native rank, semilinear F/eta, signed odd Green/Hesse, κ, Delta-R, independently reproduced and reviewed by a legitimate native executor. This author-side scalar result is not evidence for that experiment. Observed Site client 2026-10-30 01:05Z reports static read-only identity / Researcher writes disabled. No Source request, claim, run, checkpoint, Result, HANDOFF or independent acceptance is asserted.

**External source:** Zhi-Hong Sun, *Note on super congruences modulo p²*, arXiv:1503.03418 (2015; theorem as abstracted). Related but not substituted: Zhi-Hong Sun, *Congruences for sums involving products of three binomial coefficients*, arXiv:2202.05077 (2022), whose main displayed generalized weight results have a **4^-k** denominator, not the **8^-k** in (1). Do not confuse the two.
