# ABC Enterprise Adversarial Census and No-Go Audit — Research Return

Status: `FROZEN RESEARCH RETURN / EXACT_INFINITE_OBSTRUCTION_FAMILY`  
Task-ID: `RS-ABC-ENTERPRISE-ADVERSARIAL-CENSUS`  
Publication: `TP2-3132361FDFD8E30AD1F9`  
Researcher-ID: `EM-ABC4-B9841C`  
Claim: `chatgpt-abc4-20260827-1629`  
Execution branch: `research/abc-enterprise-adversarial-census-em-abc4-b9841c`  
Execution base: `17843476d63af371bd270d53bcfc9cf876cdd7bf`

## 1. Primary verdict

Primary verdict:

`EXACT_INFINITE_OBSTRUCTION_FAMILY`

Hard target disposition:

`ABC_ADVERSARIAL_CENSUS_AND_NOGO_CERTIFICATES_FROZEN / MET`

This task produces three distinct outcomes:

1. the proposed **coefficient-2 capped-core inequality is false**, with a minimal exact counterexample in the exhaustive range `c <= 4000`;
2. the recorded **boundary-payment inequality survives**, and in fact follows from a stronger elementary bound;
3. any **unqualified bounded-window carry-payment heuristic** is false: the primitive infinite family
   \[
   (a,b,c)=(1,p^k-1,p^k)
   \]
   has an exact `p`-channel first activation
   \[
   \tau_p=p^k+1,
   \]
   hence zero `p`-channel carry energy throughout every window `1 <= n <= p^k`.

The remaining potentially viable program is therefore narrower: an **interior-conditioned** carry theorem or a weakened capped-core inequality with an explicit exceptional/defect term. Boundary payment by itself cannot explain the difficult interior examples.

## 2. Provenance boundary and self-contained audit normalization

The immutable ABC1–ABC4 taskbooks persist the intended roles of `R`, `H`, `beta`, `I_cap`, boundary payment and carry activation, but the parent conversation containing the full formulas is not repository-addressable from the taskbook. To keep this return replayable, ABC4 freezes the following self-contained audit normalization, matching the persisted task descriptions and the recorded parent bound.

For a primitive positive triple
\[
a+b=c,\qquad \gcd(a,b)=1,
\]
pairwise coprimality of `a,b,c` follows. Put
\[
\rho(x)=\operatorname{rad}(x),\qquad
\rho=\rho(a)\rho(b)\rho(c)=\operatorname{rad}(abc),
\]
and
\[
u_x=\frac{x}{\rho(x)}.
\]

Define the logarithmic one-time support and repeated-prime height by
\[
R=\log\rho,\qquad
H=\log(u_a u_b u_c).
\]

Let
\[
m=\min(a,b),
\qquad
K_{\rm cap}=\prod_{x\in\{a,b,c\}}\min(u_x,m),
\]
and define
\[
I_{\rm cap}=\log K_{\rm cap},
\qquad
D_{\rm sup}=H-I_{\rm cap}.
\]

Use the balanced boundary normalization
\[
\beta=\log\frac{c^2}{4ab}\ge 0
\]
and standard abc quality
\[
q=\frac{\log c}{R}.
\]

Then the exact log identities are
\[
R+H=\log(abc)=3\log c-\beta-\log4,
\]
hence
\[
\boxed{3(q-1)R=H+\beta+\log4-2R}
\]
and
\[
\boxed{H=I_{\rm cap}+D_{\rm sup}}.
\]

All decisive no-go decisions below are reduced to integer/rational comparisons. Decimal logarithms are descriptive only.

If the unpublished parent conversation used an additive renormalization of `beta`, the raw balance ratio
\[
\frac{4ab}{c^2}
\]
and all integer capped-core/carry certificates below remain unchanged.

## 3. Global boundary theorem: the boundary-payment route survives

### Theorem 1 — stronger elementary boundary bound

For every primitive positive `a+b=c`,
\[
\boxed{D_{\rm sup}\le 2\log\frac{c}{m}}.
\]

### Proof

For each coordinate `x`, the uncapped repeated-prime quotient is
\[
u_x=\frac{x}{\operatorname{rad}(x)}\le x\le c.
\]

The contribution of coordinate `x` to `D_sup` is
\[
\log u_x-\log\min(u_x,m)
=
\max\!\left(0,\log\frac{u_x}{m}\right).
\]

The smaller addend itself is `m`, so for that coordinate `u_m <= m` and its excess contribution is zero. There are only two remaining coordinates, and each contributes at most
\[
\log(c/m).
\]
Summing gives the claim.

Now write `x=m/c <= 1/2`. Since
\[
\beta=-\log(4x(1-x)),
\]
we have
\[
\log\frac{c}{m}
=
-\log x
=
\beta+\log4+\log(1-x)
\le \beta+\log4.
\]
Therefore
\[
\boxed{D_{\rm sup}\le 2\beta+\log16}.
\]

This is exactly the boundary-payment form recorded in the ABC3 task metadata, with a stronger intermediate estimate.

The exhaustive census through `c<=4000` found zero violations of either bound, but the theorem above is global; the finite scan is regression evidence only.

## 4. Exact no-go: the coefficient-2 capped-core bound is false

The ABC1 task explicitly requested an active attempt to kill a coefficient-2 bound before any proof attempt. The natural critical statement in the audit normalization is

\[
I_{\rm cap}\le 2R,
\]
equivalently, by monotonicity of `log`,
\[
\boxed{K_{\rm cap}\le \rho^2}.
\]

This universal inequality is false.

### Minimal exact counterexample in the exhaustive range

\[
\boxed{32+49=81}.
\]

Factorization:
\[
32=2^5,\qquad 49=7^2,\qquad 81=3^4.
\]

Thus
\[
\rho=2\cdot7\cdot3=42,
\]
and
\[
(u_a,u_b,u_c)=(16,7,27).
\]

Here `m=32`, so no component is capped:
\[
K_{\rm cap}=16\cdot7\cdot27=3024,
\qquad
D_{\rm sup}=0.
\]

But
\[
3024>42^2=1764,
\]
indeed
\[
\frac{K_{\rm cap}}{\rho^2}=\frac{12}{7}.
\]

Therefore
\[
\boxed{I_{\rm cap}>2R}
\]
with **zero boundary excess**.

The same triple is genuinely interior in the raw geometric sense:
\[
\frac{4ab}{c^2}=\frac{6272}{6561},
\]
so under the audit normalization
\[
\beta=\log\frac{6561}{6272}\approx0.0450477473.
\]

Its quality is
\[
q=\frac{\log81}{\log42}\approx1.1757189916.
\]

This kills simultaneously:

- the universal coefficient-2 capped-core inequality;
- the heuristic that every `q>1` excess must be carried by `D_sup`;
- a boundary-only explanation of high-quality triples.

### Stronger low-beta witness

A sharper interior witness in the same census is
\[
\boxed{1024+1377=2401}
\]
with
\[
1024=2^{10},\quad 1377=3^4\cdot17,\quad 2401=7^4.
\]

Here
\[
\rho=714,\qquad
(u_a,u_b,u_c)=(512,27,343),\qquad
m=1024,
\]
so again
\[
D_{\rm sup}=0,
\qquad
K_{\rm cap}=4\,741\,632.
\]

Exactly,
\[
\frac{K_{\rm cap}}{\rho^2}
=
\frac{2688}{289}
\approx9.301038.
\]

The balance ratio is
\[
\frac{4ab}{c^2}
=
\frac{5\,640\,192}{5\,764\,801},
\]
equivalently
\[
\beta
=
\log\frac{5\,764\,801}{5\,640\,192}
\approx0.0218525270,
\]
while
\[
q\approx1.1845653987.
\]

Thus the failure is not a thin-boundary artifact.

## 5. Exhaustive exact census through c <= 4000

The checker enumerates unordered primitive triples with
\[
1\le a\le b,\qquad a+b=c\le4000.
\]

Total exact corpus size:
\[
\boxed{2\,431\,800}
\]
primitive triples.

Exactly seven triples in this range violate `K_cap <= rho^2`:

| a | b | c | rho | K_cap/rho^2 | q (descriptive) | beta (descriptive) |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 49 | 81 | 42 | 12/7 | 1.175719 | 0.045048 |
| 169 | 343 | 512 | 182 | 13/4 | 1.198754 | 0.122726 |
| 81 | 1250 | 1331 | 330 | 19683/12100 | 1.240485 | 1.475729 |
| 243 | 1805 | 2048 | 570 | 2187/1900 | 1.201553 | 0.871566 |
| 1024 | 1377 | 2401 | 714 | 2688/289 | 1.184565 | 0.021853 |
| 625 | 2048 | 2673 | 330 | 28125/484 | 1.360723 | 0.333248 |
| 1024 | 2187 | 3211 | 1482 | 10368/4693 | 1.105900 | 0.140623 |

The first row is minimal by `c` within the exhaustive range.

The strongest `I_cap/R` violation in the range is
\[
625+2048=2673,
\]
with
\[
I_{\rm cap}/R\approx2.700511,
\qquad
H/R\approx2.785649,
\qquad
D_{\rm sup}/R\approx0.085137.
\]

The best low-beta adversarial score used by the checker is attained by
\[
1024+1377=2401.
\]

These decimal rankings are descriptive; the universal kill certificates are the exact integer comparisons above.

## 6. Exact infinite carry obstruction

For a prime `p` and integer `k>=1`, set
\[
P=p^k,
\qquad
(a,b,c)=(1,P-1,P).
\]

This is primitive. For the `p`-channel, the ABC2/ABC3 carry statistic is
\[
h_p(n)
=
v_p\!\left(\frac1P\binom{nP}{n}\right).
\]

Using
\[
\binom{nP}{n}
=
P\binom{nP-1}{n-1},
\]
we get the exact simplification
\[
h_p(n)
=
v_p\binom{nP-1}{n-1}.
\]

### Theorem 2 — exact first activation

\[
\boxed{\tau_p=P+1=p^k+1}.
\]

### Proof

For `1<=n<=P`,
\[
nP-1=(n-1)P+(P-1).
\]

In base `p`, the lower `k` digits of `nP-1` are all `p-1`; the higher block is the base-`p` expansion of `n-1`. Since `n-1<P`, every base-`p` digit of the bottom index `n-1` fits beneath the corresponding lower digit `p-1`, and all higher bottom digits vanish. Lucas' theorem therefore gives
\[
\binom{nP-1}{n-1}\not\equiv0\pmod p.
\]
Hence
\[
h_p(n)=0
\qquad(1\le n\le P).
\]

At `n=P+1`, the bottom index is `P=p^k`, which has digit `1` in position `k`. But
\[
(P+1)P-1=P^2+P-1
\]
has digit `0` in position `k` and the lower `k` digits equal to `p-1`. Lucas' criterion fails in position `k`, so the binomial is divisible by `p`. Thus
\[
h_p(P+1)>0.
\]

Therefore `tau_p=P+1`.

### Consequence

For the controlled-window energy
\[
E_p(W)=\sum_{n=1}^{W}h_p(n),
\]
we have
\[
\boxed{E_p(W)=0\quad\text{for every }W\le p^k}.
\]

Hence no universal carry-payment theorem can require positive `p`-channel energy in a window bounded only by a fixed power `p^A` independent of `v_p(c)`: choose `k>A`.

This obstruction is boundary-heavy, so it does **not** kill a future theorem with a genuine interior hypothesis such as a quantitative beta restriction. It does kill unqualified carry-payment heuristics.

The checker independently replays the theorem for `p in {2,3,5,7,11}` and `1<=k<=4`; that computation is regression only, not the proof.

## 7. Carry profiles of the principal adversarial witnesses

Using the deterministic window `1<=n<=64`:

- `32+49=81`: `tau_2=1`, `tau_3=4`, `tau_7=5`.
- `1024+1377=2401`: `tau_2=1`, `tau_3=1`, `tau_7=8`, `tau_17=1`.
- `625+2048=2673`: `tau_2=5`, `tau_3=1`, `tau_5=3`, `tau_11=1`.
- `1+80=81`: `tau_3=82`, so the `p=3` channel has no activation in the 64-window.
- `1+2400=2401`: `tau_7=2402`, so the `p=7` channel has no activation in the 64-window.

The full per-prime energy sums and maxima are frozen in `census_summary.json`.

## 8. Disposition of the ABC1–ABC3 routes

| Route | Candidate audited | Disposition |
|---|---|---|
| ABC1 capped core | `I_cap <= 2R` | **KILLED** exactly; minimal `c<=4000` witness `32+49=81` |
| ABC1 boundary-only payment | `q>1` must force positive `D_sup` | **KILLED**; `32+49=81` and `1024+1377=2401` have `D_sup=0` |
| ABC3 boundary escape | `D_sup <= 2 beta + log 16` | **SURVIVES GLOBALLY**; stronger `D_sup <= 2 log(c/m)` proved |
| ABC2 carry activation | universal short-window positive carry payment | **KILLED** by `(1,p^k-1,p^k)` with `tau_p=p^k+1` |
| ABC2 interior carry activation | beta-restricted carry-energy lower bound | **OPEN**; not refuted by the boundary family |
| combined program | boundary payment + universal coefficient-2 core | **KILLED AS STATED** |
| combined program | boundary payment + weakened core + interior carry term | **STILL VIABLE** |

This is the main program-level conclusion: the difficult mass is not an unbounded tower tail; the boundary theorem already controls that. The failure lives in a **balanced capped core**.

## 9. Reproducibility

Checker / corpus generator:

`scripts/check_abc_enterprise_adversarial_census.py`

Frozen machine-readable output:

`research_artifacts/ABC_ENTERPRISE_ADVERSARIAL_CENSUS/census_summary.json`

Default replay:

`python scripts/check_abc_enterprise_adversarial_census.py --max-c 4000 --carry-window 64 --output /tmp/abc4.json`

Authoring-time verified facts:

- primitive triples scanned: `2,431,800`;
- coefficient-2 counterexamples: `7`;
- minimal counterexample: `(32,49,81)`;
- strong boundary violations: `0`;
- parent boundary violations: `0`;
- exact carry-family regression cases: `20`;
- all carry-family regression cases passed.

The universal boundary and carry-family statements are proved in this return. Enumeration is used only to establish bounded minimality/rankings and to supply regression evidence.

Universal tool reuse gate: `NOT_APPLICABLE`. The required checker is task-local and introduces no new general-purpose repository mechanism.

## 10. Smallest unresolved unit

The smallest mathematically live successor is **not** “try coefficient 2 again.”

It is one of:

1. characterize the exceptional balanced capped-core set and seek the best weakened inequality
   \[
   I_{\rm cap}\le (2+\delta)R + \text{typed correction};
   \]
2. condition the carry-energy problem on a genuinely interior band and ask whether the same primes responsible for large `I_cap/R` must activate with controlled cumulative energy;
3. test whether the seven capped-core failures up to `c=4000` share an exact algebraic packet that can be bounded independently of abc.

No Foundation/native-plane promotion is authorized by this task.

## 11. Driver recommendation

Driver should accept this task at `EXACT_INFINITE_OBSTRUCTION_FAMILY` strength if the audit normalization is judged consistent with the unpublished parent formulas.

On acceptance:

- mark the universal ABC1 coefficient-2 route **refuted**;
- retain the boundary-payment theorem, preferably in the stronger `2 log(c/m)` form;
- forbid unqualified bounded-window carry-payment claims;
- allow only explicitly beta/interior-conditioned carry successors;
- if the parent conversation used a different additive beta normalization, translate the boundary table before integration; do not discard the integer no-go and carry certificates.

Hard block: `NONE` for the ABC4 hard target.  
Residual provenance note: the parent conversation formulas were referenced by taskbooks but not themselves persisted as repository source; this return therefore makes its audit normalization explicit rather than silently treating conversation state as a file.
