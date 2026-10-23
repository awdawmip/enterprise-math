# D25/LIFT — Three-band exact hypergeometric-base expansion through p^3

2026-10-24 | TASK_RESEARCH, **portable author-side arithmetic**. **AUTHOR-PROVED ALL-TARGET-PRIME CONGRUENCES; BOUNDED EXACT SELF-CHECK; UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**. No native benchmark, winning CLAIM, open/resume authorization, Result, or independent review is claimed here.

Parent Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. **Frozen task/source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` remains unchanged.** Provenance: Research logical lane `chatgpt-research-hourly-enterprise-math-20260923`, **not** control-maintenance `chatgpt-hourly-enterprise-math-20260921`. The previously Source-registered `EM-DIRECT-211CEB / MCP-cf39e84761fa4092a3600450d8aad3ab` is a historical service identity reference; this paper grants it no new claim/run. Existing support route: [#1558](https://github.com/awdawmip/enterprise-math/issues/1558).

Compared with current repository source at main `0f60695147d861c2f40448e46ef3adebab78c1c1` and the distinct immutable task pin. Global Knowledge main `bdc4c6b8927afbdf4d031565b3bec53d95936bbc`, P000 ACTIVE_LOCKED. The original [two-seam Gosper identity](20261024_onhour_d25_original_endpoint_gosper_two_seam_p2.md), [seam-to-target normalization](20261024_hourly_d25_T2_Gm_normalization_p2.md), and the other Research lane's [low first jet / high p-unit sectors](20261024_onhour_d25_regular_low_jet_high_unit_two_sector.md) are **inherited work, not newly claimed here**. The unique new contribution below is a full termwise `p^3` bridge, including **the next high-sector digit**, which those `p^2`/`p` interfaces do not provide.

## Exact original problem and fixed comparison carrier

For every prime `p=6m+1>=7` (`m>=1`), retain the **unchanged original** rational hypergeometric sequence

\[
R_0=1,\quad
\frac{R_{n+1}}{R_n}=
\frac{(6n+2p+1)(3n+1)(3n+2)}
{12(n+1)(3n+p+2)(3n+2p+1)}.
\]

Introduce the simple, *non-native auxiliary* hypergeometric base

\[
a_n=\frac{(1/6)_n}{2^n n!}
=\frac{\prod_{j=0}^{n-1}(6j+1)}{12^n n!},
\quad a_0=1,\quad
\frac{a_{n+1}}{a_n}=\frac{6n+1}{12(n+1)}.
\]

Every term is an exact rational number, with fixed, labeled index `n`. This is not an assertion that the auxiliary base is a native-X6 primitive or that a p-adic scalar observer forgets branch provenance.

For `j\notin\{m,2m\}` and `0<=j<4m`, define p-integral terms

\[
\ell_j=\frac2{6j+1}-\frac1{3j+2}-\frac2{3j+1},\qquad
u_j=\frac4{(6j+1)^2}-\frac1{(3j+2)^2}-\frac4{(3j+1)^2},
\]

\[
E_n^*=\sum_{\substack{0\le j<n\\j\ne m,2m}}\ell_j,
\qquad U_n^*=\sum_{\substack{0\le j<n\\j\ne m,2m}}u_j.
\]

The star omits *only* the two exceptional indices, never an entire tail. For `n<=m`, it omits nothing.

## Theorem: a full three-band p^3 termwise certificate

For each `0<=n<=4m`, in `\mathbb Z_{(p)}` the following holds:

\[
\boxed{
R_n\equiv
\begin{cases}
a_n\left[1+pE_n^*+\frac{p^2}{2}\bigl((E_n^*)^2-U_n^*\bigr)\right],
&0\le n\le m,\\[2mm]
3a_n\left[1+p\left(E_n^*-\frac{14}{3}\right)\right],
&m<n\le2m,\\[2mm]
a_n\left[1+p\left(E_n^*-\frac{23}{3}\right)\right],
&2m<n\le4m,
\end{cases}
\pmod{p^3}.}
\tag{BAND-3}
\]

**Proof.** Divide the exact adjacent ratios of `R_n` and `a_n`:

\[
\frac{R_{n+1}/a_{n+1}}{R_n/a_n}
=F_n(p):=
\frac{6n+2p+1}{6n+1}
\frac{3n+1}{3n+2p+1}
\frac{3n+2}{3n+p+2}.\tag{F}
\]

For the stated range `0<=j<4m`, the only exceptional p-bearing linear factors in `F_j` are at `j=m` and `j=2m`. The cancellations must be performed exactly, *before* reduction:

\[
F_m(p)=\frac{p+3}{5p+1}
\equiv3\left(1-\frac{14p}{3}\right)\pmod{p^2},\tag{J1}
\]

\[
F_{2m}(p)=\frac{(4p-1)(p+1)}{3(2p-1)(2p+1)}
\equiv\frac13(1-3p)\pmod{p^2}.\tag{J2}
\]

Their product is `F_mF_{2m}\equiv1-23p/3\pmod{p^2}`. At every **other** `j`, all displayed denominators are p-units, and direct finite-product expansion gives

\[
F_j(p)\equiv
1+p\ell_j+\frac{p^2}{2}(\ell_j^2-u_j)
\pmod{p^3}.\tag{REG}
\]

Therefore, before either exceptional index, multiplying (REG) yields
`R_n/a_n\equiv1+pE_n^*+p^2((E_n^*)^2-U_n^*)/2\pmod{p^3}`.
After `j=m`, the first jump gives
`R_n/a_n\equiv3[1+p(E_n^*-14/3)]\pmod{p^2}`;
after `j=2m`, the two exceptional factors give
`R_n/a_n\equiv1+p(E_n^*-23/3)\pmod{p^2}`.

Finally `4m<p`; all denominators of `a_n` are p-units, and among `6j+1` for `0<=j<4m` the *only* multiple of p occurs at `j=m`, exactly once. Hence

\[
v_p(a_n)=
\begin{cases}0,&0\le n\le m,\\1,&m<n\le4m.\end{cases}
\tag{VAL}
\]

Thus the lower band needs the coefficient ratio to precision `p^3`; each upper band needs it only to `p^2`, because its `a_n` already contains one p. Substitution proves (BAND-3) for **every** target prime, without numerical interpolation, illegal p division or seam deletion. QED.

## Corollary: an explicit original-endpoint p^3 replacement

Let `Q_n` be the **corresponding complete right-hand expression** in (BAND-3), not its reduction to a coarse total. The original endpoint remains

\[
S_{4m}(2m)=\mathcal A_m
\sum_{n=0}^{4m}(6n+2p-1)R_n,
\qquad
\mathcal A_m=\frac{(p-1)!}{3^{p-1}((2m)!)^3},
\]
where `\mathcal A_m` is a p-unit. Consequently the **complete original** sum, with its true terminal `n=4m`, satisfies

\[
\boxed{
S_{4m}(2m)\equiv
\mathcal A_m\sum_{n=0}^{4m}(6n+2p-1)Q_n\pmod{p^3}.
}\tag{END-3}
\]

No `K_{p,2m}` or `K_{p,4m}` is individually inverted: the endpoint is expanded *before* the Gosper divided-forcing decomposition. In particular (END-3) is a separate **proved equivalence/reduction**, **not** a proof that its right side equals the still-open desired `p(4/3)^{p-1}\pmod{p^3}`.

The p³ interface provides a previously absent **second p-adic digit of both upper p-unit sectors** and an independent exact-precision audit of the original endpoint. The other lane's LOW-JET/HIGH finite obstruction `\mathcal D_m^{\mathrm{finite}}\) remains the smaller obligation for the second-digit LIFT; this paper neither replaces that obligation nor claims to have proved its vanishing. The unrecovered source-specific CM representative/comparison/normalization is still separately required for the native D25 task frontier.

## Exact author-side checks and boundaries

Using Python `fractions.Fraction`, exact rational recurrence `R_0=1`, exact rational `a_n`, explicit `E_n^*,U_n^*`, and p-factor-stripped modular reduction (checking numerator/denominator valuations before modular inverse), **every term `0<=n<=4m` and the full (END-3) sum** was checked modulo `p^3` for all 18 primes `p=6m+1` with `1<=m<=29`:

`7,13,19,31,37,43,61,67,73,79,97,103,109,127,139,151,157,163`.

All author checks passed. Witnesses `p : (original weighted sum mod p^3, BAND-3 rebuilt sum mod p^3)`:

`7:(189,189)`; `13:(1963,1963)`; `19:(2679,2679)`; `31:(6479,6479)`; `37:(46176,46176)`; `61:(141337,141337)`.

These are exact finite **self-checks**, not an independent proof for infinitely many primes; the all-prime result follows from the displayed rational product proof. No native experiment or independent review was executed. The original LIFT, Source CM companion, Researcher authorization and checkpoint remain unverified/not completed.

**Typed BRC use:** `COMPOSE_APPLIED / REUSE_APPLIED`. Carrier = branch-labeled original `n`, rational signed weight `R_n`, explicit p-adic valuation and unit, exact special jump labels `m`/`2m`; observer = mod `p^3` of the entire original weighted scalar, and permissible operation = summation up to the exact `4m` endpoint. Equations (F), (J1), (J2) preserve the omitted fine information for a future observer; (BAND-3) is *not* an unrestricted branch-level equality at higher precision, and not a positive-mass conservation theorem.

**Smallest next scientific unit:** use the already derived binomial LOW-JET/HIGH decomposition to prove or refute the exact finite obstruction `\mathcal D_m^{\mathrm{finite}}\equiv0\pmod p` uniformly in the selected prime classes, potentially via terminating contiguous/WZ integration by parts. The new BAND-3 representation is an independent p³-precision consistency/alternative route, not a reason to replay the first-digit or finite prime scans. No Source pin, active owner, claim, result, scheduler or notification setting is changed.
