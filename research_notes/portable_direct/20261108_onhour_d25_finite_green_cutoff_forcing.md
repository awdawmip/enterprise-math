# D25 — Exact finite Green–Wronskian with nonzero truncation source

Date: 2026-11-08 Asia/Hong_Kong. Research lane \`chatgpt-research-onhour-enterprise-math-20260923\`, not maintenance \`chatgpt-hourly-enterprise-math-20260921\`. TASK_RESEARCH author-side external rational-function model: PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`.

This unit consumes the full-power Green identity of independent Research20 commit \`47c8de70adfae20dd99a47eb804bb2dd72f87716\` and our immediately previous residue-cutoff theorem \`de8535d04ddc62ff5661dbfadefb999be7c6ec24\`. The mathematical change is replacing the infinite forced kernel by the **actual degree-m finite kernel used in the original reflected R_p**, and computing its exact terminal forcing.

## Exact all-m finite cutoff theorem

For every positive integer m let P=6m+1 and D=t d/dt. Let

\[
\mathcal L=(6D-1)(3D-1)-36tD^2
=18(1-2t)D^2-9D+1.
\]

Set C_1=1/10 and C_(r+1)/C_r=36r²/((6r+5)(3r+2)), with F_m(t)=sum_(r=1)^m C_r t^r. Let Q_m(z)=sum_(i=0)^m binom(m,i)binom(2m,i)z^i and W_m(t)=Q_m(1/(2t)). The previous reciprocal Gauss identity gives

\[
\mathcal L W_m=-P(9D-2)W_m-P^2W_m.
\]

**New finite forcing identity, valid exactly over Q[t] for any m>=1:**

\[
\boxed{\mathcal L F_m=t-36m^2 C_m t^{m+1}.}\tag{FINITE-FORCING}
\]

Proof: degree one has coefficient (6-1)(3-1)C_1=10C_1=1; degrees 2..m cancel by the exact C_r recurrence. The sole uncancelled term is the t^(m+1) coefficient from -36t D² F_m, equal to -36m²C_m. No other degree appears.

Define the source-preserving Laurent Wronskian J_m(t)=W_m D F_m-F_m D W_m. Then the exact **finite Green equation** is

\[
\boxed{
18(1-2t)D J_m-9J_m
=t W_m-36m^2 C_m\,t^{m+1}W_m
+P F_m(9D-2)W_m+P^2 F_mW_m.
}\tag{FINITE-GREEN}
\]

Proof: W_m L F_m -F_m L W_m
=18(1-2t)D(W_m D F_m-F_mD W_m)-9(W_m D F_m-F_mD W_m) by the product rule. Substitute FINITE-FORCING and the previously proved reciprocal Gauss defect. This is a Laurent-polynomial identity, no convergence issue.

## Nonzero Frobenius-cutoff source for the frozen target

Let p=P=6m+1 be prime. All q_i=2^(-i)binom(m,i)binom(2m,i) and C_r for 1<=r<=m are p-integral and C_m is a p-unit. Since 36m²=(p-1)²=1 mod p, the exact equation reduces to

\[
18(1-2t)D J_m-9J_m
\equiv tW_m-C_m t^{m+1}W_m\pmod p.
\tag{FINITE-GREEN-MOD-P}
\]

The **terminal cutoff source** is a nonzero polynomial of degrees 1..m+1:
\[
-C_m t^{m+1}W_m=-C_m\sum_{i=0}^m q_i\,t^{m+1-i}.
\]
Its coefficient at t is \(-C_m q_m\ne0\bmod p\), since q_m=2^(-m)binom(2m,m) is a p-unit (2m<p). Its highest coefficient at t^(m+1) is \(-C_m\ne0\). Hence the finite source term survives reduction for every prime p=6m+1, including both frozen target classes p=13,19 (mod24). This is an exact local statement about the finite Green operator, not a conclusion that R_p or Delta_p is nonzero.

| p | m | C_m mod p | q_m mod p | coefficient of t in cutoff | coefficient of t^(m+1) |
|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 9 | 8 | 6 | 4 |
| 19 | 3 | 1 | 12 | 7 | 18 |
| 43 | 7 | 41 | 8 | 16 | 2 |
| 67 | 11 | 36 | 5 | 21 | 31 |
| 373 | 62 | 37 | 13 | 265 | 336 |

The accompanying standard-library exact Fraction checker verifies the original reciprocal Gauss defect, the new FINITE-FORCING, and both sides of FINITE-GREEN for m=1,2,3,7,11,62 (p=7,13,19,43,67,373 where P is prime). All full Laurent coefficient vectors PASS. The theorem itself is proved by coefficient recurrence and the Wronskian product rule.

## Next scientific step

Combine the nonzero terminal source \(-C_m t^{m+1}W_m\) with the previous three-residue decomposition of the original reflected R_p into CM tangent and infinity cutoff. Seek a **finite**, not infinite-kernel, weighted adjoint/Green boundary certificate that converts the terminal t^(m+1) forcing into the original cutoff-sensitive \(\Phi_{xx}\) and the rational divided \((ZH_0-1)/p\), alongside SH0 and ZH1. Check p=19 and 373 first; preserve signed/odd original source terms. This is a specifically testable route, not a claim that all proof routes need this representation.

The original same-class H0/B0/divided-power/Frobenius/Hesse κ benchmark at p=373 (support #1559) remains unexecuted, with no assigned operator observed in this run. Native request \`onhour11-20261106-1400-exact-research-lane-continuation\` retained, native status/receipt yielded BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE with operation_sent=false. Site CONFIGURED_NOT_LIVE_VERIFIED; no native Researcher session/CLAIM/open/Result/checkpoint was established. Mother Delta_p=R_p and W_p mod p³ remain OPEN.