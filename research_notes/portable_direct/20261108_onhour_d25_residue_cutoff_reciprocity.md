# D25 — Reflected-residue reciprocity: CM tangent and complementary infinity cutoff

Date: 2026-11-08 Asia/Hong_Kong. TASK_RESEARCH author-side portable, algebraic identity PROVED; exact finite arithmetic CHECKED; UNREVIEWED / NOT_ADMITTED. Logical Research lane \`chatgpt-research-onhour-enterprise-math-20260923\`, excluding maintenance lane \`chatgpt-hourly-enterprise-math-20260921\`.

Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Consumes (does not claim authorship of) the independent reflected R_p kernel / Green source at commit \`47c8de70adfae20dd99a47eb804bb2dd72f87716\` and this lane's earlier D25 first-lift work at \`1ab363049fb298ce10c0575036d350c5a4549424\`.

## Exact all-m finite rational theorem

For any integer m>=1, define q_i=2^(-i) binom(m,i)binom(2m,i), i=0..m; C_1=1/10, C_(r+1)/C_r=36r²/[(6r+5)(3r+2)]. Let

- Q_m(z)=sum_(i=0)^m binom(m,i)binom(2m,i)z^i; F_m(t)=sum_(r=1)^m C_r t^r; W_m(t)=Q_m(1/(2t)).
- R_m=2 sum_(i=1)^m q_i sum_(r=1)^i [1+6(i-r)] C_r, the original reflected source.
- B_m=sum_(r=1)^m C_r sum_(i=0)^(r-1) [6(r-i)-1]q_i, the **complementary sector with r>i**.
- Q=Q_m(1/2)=sum q_i; J=(z Q'_m(z))_(z=1/2)=sum i q_i; U=F_m(1)=sum C_r; V=F'_m(1)=sum r C_r.

Then **exactly over Q, with no primality assumption**:

\[
\boxed{R_m=2\{B_m+(Q+6J)U-6QV\}.}\tag{R-RECIPROCITY}
\]

**Proof (global rational residue).** Put A(t)=(1+5t)/(1-t)² and H(t)=W_m(t) A(t) F_m(t)/t. By coefficient extraction, Res_(t=0) H dt=R_m/2. At t=1 write H=G(t)/(t-1)², G(t)=(t^(-1)+5)W_m(t)F_m(t). Since W_m(1)=Q and W'_m(1)=-J, its residue is

\[
\mathrm{Res}_{1}H\,dt=G'(1)=-(Q+6J)U+6QV.
\]

At infinity A(t)/t=sum_(n>=1)(6n-1)t^(-n-1), hence coefficient [t^(-1)]_infinity H equals sum_(0<=i<r<=m)q_i C_r[6(r-i)-1]=B_m and Res_infinity H dt=-B_m. The rational residue theorem yields R-RECIPROCITY. The same identity follows by splitting the total signed (i,r) pair sum into r<=i and r>i. The two proofs use identical exact rational data and do not depend on numerical fitting.

## CM specialization and exact witnesses

For p=6m+1 prime in the frozen p=13,19 (mod24) classes, all C_r denominators with r<=m are p-units. Consumption of the previously proven uniform CM/Hasse zero Q_m(1/2)=0 mod p gives

\[
\boxed{R_p\equiv2 B_m+12 J F_m(1)\pmod p.}\tag{CM-CUTOFF}
\]

This preserves two distinct observables: the local Hasse tangent J and the complementary **infinity/cutoff** pair sector B_m. Neither is silently contracted before the declared weighted-residue observation. Original source term R_p is not reconstructed from a measured Delta.

| p | m | J | F_m(1) | B_m | 2B_m | 12 J F_m(1) | original R_p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 7 | 0 | 0 | 0 | 0 | 0 |
| 19 | 3 | 1 | 5 | 14 | 9 | 3 | 12 |
| 43 | 7 | 20 | 12 | 8 | 16 | 42 | 15 |
| 67 | 11 | 40 | 9 | 28 | 56 | 32 | 21 |
| 373 | 62 | 294 | 45 | 167 | 334 | 235 | 196 |

All entries reduced mod p. In particular p=373 gives 334+235=569=196 mod373; p=19 gives 9+3=12. A route that takes only the local t=1 tangent residue misses B_19=14, an exact counterexample to that **specific projection**, not to adjoint methods in general.

The accompanying Python standard-library checker independently generates original Gauss B_i and Hasse q_i recurrences, reproduces exact rational R-RECIPROCITY for m=1..8, and tests all 77 primes p<=2000 in the two frozen classes; all pass.

## Research handoff

The complementary B_m is now an explicit, cutoff-typed boundary candidate for the unresolved original D25 congruence Delta_p=R_p. Next construct a finite adjoint/creative-telescoping certificate linking B_m to the original divided (ZH0-1)/p, SH0, ZH1 and Phi_xx cutoff terms while retaining the tangent JF_m(1); discriminate first on p=19 and p=373 with nonzero B_m. This is a proposed route, not an exclusive prerequisite. Frozen mother objectives Delta_p=R_p and W_p=p mod p^3 remain OPEN.

Native issue #1559's original-class p373 H0/B0, divided powers, Frobenius eta, signed Hesse kappa and independent replication are pending and are **not executed** by these computations. The old native request \`onhour11-20261106-1400-exact-research-lane-continuation\` is retained; this run's native status/receipt read returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE, operation_sent=false. Site CONFIGURED_NOT_LIVE_VERIFIED, no authenticated researcher session/claim/run verified, REGISTER_PENDING, native checkpoint not written. No freeze/review/admission claimed.