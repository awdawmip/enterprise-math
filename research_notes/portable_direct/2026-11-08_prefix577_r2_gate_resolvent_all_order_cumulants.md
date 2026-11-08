# PREFIX-577-R2-GC — Exact rational gate resolvent and all-order BRC gate cumulants

**Date:** 2026-11-08 (Asia/Shanghai)  
**Status:** AUTHOR_PROVED / EXACT_INTEGER_AND_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED  
**Frozen scientific pin:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`  
**Current control read:** EM `main@792d9e54e09bee091bdec4e6a4c89fc67e14d38c`; global `main@bda71b82cb1a9709f30db658d1468ab107446e1a`.

## 1. Scientific question and exact native carrier

Compute the *full rational gate response* of the frozen four-STAR native X6-BRC kernel and extract its gate-count cumulants to arbitrary finite order. This extends the PREFIX-575 first/second-order Poisson result and the independent PREFIX-576-R2 third/fourth cumulant branch `aac16d053758b632b506ebe3658b9312579a0b8d`. Concurrent EM `main` includes another PREFIX-576 (axis 5/6 and gate covariance), which is a distinct three-observer study.

The immutable native model has 48 phases, 96 ordered branch ports and six labeled actions at every port. The original gate marks occur *exactly* at native edges `7→9, 29→9, 31→9`. The PREFIX-566 quotient preserves the future `(q5,q6,gate)` observation at all ordered depths for the nine permitted frozen roots (`r5=r6=0`): refinement growth `1,4,13,21,33,37`. In this note specialize *observer weights* `q1=...=q6=1` but retain the native gate mark, edge multiplicities, original source carrier and ordered action semantics. The state representation is still the native six-axis kernel; the quotient is observer-typed, not a new physical state space. Depth means ordered action count, **not physical time**.

Let `C` denote the integer 37×37 transition-count matrix (every row sums to six), `P=C/6`. The gate-source indicator `g` is supported on classes `4,15,17` and the common target is class `5`. The actual gate-marked operator is the exact BRC-derived rank-one update

```text
P(z) = P + (z-1) g e_5^T / 6.
```

Uniform choice of each labeled action induces class weights `pi_i=class_size_i/96`, not a uniform 37-state prior.

## 2. Theorem: the exact rational function

**Theorem 577-R2.1.** Define

```text
R(lambda) = (1/6) e_5^T (lambda I - P)^(-1) g .
```

Then, as an equality of rational functions,

```text
R(lambda) = N(36 lambda^2) / Q(36 lambda^2)
N(w) = 20w^3 + 48w^2 + 1728w - 62208
     = 4(w-12)(5w^2 + 72w + 1296)
Q(w) = w^5 - 20w^4 - 416w^3 - 4992w^2 - 34560w + 248832
     = (w-36)(w-4)(w+12)(w^2+8w+144).
```

The reduced transfer denominator has degree **five** in `w=lambda²` and degree **ten** in `lambda`.

**Proof.** The 37-state graph is irreducible and bipartite. The target class lies in the 17-state block and the three marked sources in the opposite 20-state block. With this ordering write `C=[[0,A],[B,0]]`, where `A` is 17×20 and `B` is 20×17; `g=(0,g_S)`. Set `D=AB`, `b=A g_S`, and let `e` select class 5 within the target block. By exact block inversion,

```text
R(lambda) = e^T ((6 lambda)^2 I - D)^(-1) b.
```

The attached pure-integer certificate reconstructs `D` from the original PREFIX-565 `edge` and PREFIX-566 `weighted_quotient` interfaces. It verifies all **289 entries** of the exact matrix annihilation identity

```text
Q(D) = 0_(17×17).
```

It independently computes the five observable Markov parameters

```text
m_k = e^T D^k b,  k=0,...,4
(m0,m1,m2,m3,m4) = (0,20,448,19008,604160).
```

Since `Q(D)=0`, the formal Laurent series `F(w)=sum_{k>=0}m_k w^(-k-1)` satisfies `Q(w)F(w)=N_*(w)` for a polynomial `N_*` of degree at most four. Its nonnegative-power coefficients depend only on the displayed first five moments, and integer multiplication gives precisely `N_*=20w³+48w²+1728w-62208`. Thus `F=N/Q`. The certificate also executes exact rational polynomial Euclidean division to check `gcd(N,Q)=1`, which proves the reduced denominator degrees. This identity concerns the *declared future gate observer*, not preservation of unrelated native axis/source readouts. ∎

## 3. All-order theorem, exact rates and sign change

**Theorem 577-R2.2.** Let `lambda(z)` be the positive simple Perron eigenvalue of `P(z)` near `z=1`, with `lambda(1)=1`. The rank-one determinant lemma gives its exact local algebraic equation

```text
Q(36 lambda(z)^2) = (z-1) N(36 lambda(z)^2).
```

Set `u=lambda-1`, `delta=z-1`, and

```text
A(t) = t N(36(1+t)^2) / Q(36(1+t)^2),    A(0)=1/192.
```

The local equation becomes `u=delta A(u)`; hence the formal Lagrange inversion identity yields, for every `n>=1`,

```text
[delta^n] (lambda(1+delta)-1) = (1/n) [t^(n-1)] A(t)^n.
```

For `psi(s)=log lambda(exp(s))`, define `kappa_n=psi^(n)(0)`. The exact finite BRC transition graph is irreducible and period two. On the even/odd classes its squared transfer is primitive; for the strictly positive stationary-initial path-count functional, the corresponding Perron prefactors for each parity remain positive near zero and contribute only bounded terms to `log E exp(s K_d)`. Therefore, for each fixed `n`,

```text
lim_(d→infinity) Cum_n(K_d)/d = kappa_n.
```

This yields an **all-order algorithm** from one rational function, without new Poisson equations at each order. Formal rational series here are a derived observer on the actual typed BRC operator; no classical propagator or physical-time series is substituted. ∎

All coefficients below are exact rational numbers produced by integer/Fraction polynomial operations, and orders 1–4 agree with the pre-existing Poisson certificates.

| order | exact asymptotic gate cumulant rate | provenance |
|---:|---|---|
| 1 | `1/192` | PREFIX-575 |
| 2 | `1127/221184` | PREFIX-575 |
| 3 | `206963/42467328` | PREFIX-576-R2 |
| 4 | `434651857/97844723712` | PREFIX-576-R2 |
| **5** | **`203828245435/56358560858112`** | **new** |
| **6** | **`9969866857747/4809263859892224`** | **new** |
| **7** | **`-5831243834665333/8310407949893763072`** | **new** |
| **8** | **`-102557264405132243707/19147179916555230117888`** | **new** |

Thus the seventh and eighth asymptotic gate cumulants are strictly **negative**, whereas orders one through six are positive. The exact Laurent expansion provides independent agreement with the previous Poisson chain:

```text
R(1+t) = 1/(192t) - 19/2304 + (79/27648)t
         + (5801/331776)t² + O(t³).
```

The certificate also checks all coefficients of the implicit equation through `(z-1)^8`.

## 4. Finite verification and reproducibility

The companion executable `PREFIX577_R2_gate_resolvent_certificate.py` uses standard-library exact integer / Fraction arithmetic and the actual PREFIX-565/566 source interfaces. It checks the native three gate edges, all nine root projections, 37 quotient rows, stationary class weights, exact bipartition `17+20`, all 289 annihilation entries, the five Markov values, coprimality, and the full rank-one implicit relation through eighth order.

Separately, a **forward integer DP** over all gate-marked quotient transitions tracks `sum_paths binomial(K_d,k)` for orders `0..8` at depths `0,1,2,5,10,20,40,80,128`. Raw moments and cumulants are reconstructed via Stirling-number identities. This independent implementation confirms the trends without serving as the asymptotic proof:

| depth | Cum5/d | Cum6/d | Cum8/d |
|---:|---:|---:|---:|
| 20 | 0.00363458 | 0.00211749 | -0.00509531 |
| 40 | 0.00362561 | 0.00209529 | -0.00522562 |
| 80 | 0.00362112 | 0.00208417 | -0.00529094 |
| 128 | 0.00361944 | 0.00208000 | -0.00531543 |
| **exact limit** | **0.00361663** | **0.00207305** | **-0.00535626** |

All plotted decimals are displays of exact fractions, not floating-point scientific inputs. Exact fractions, source-derived 17×17 matrix and other outputs appear in `PREFIX577_R2_GATE_RESOLVENT_RESULTS.json`. At depth 128 the count is exactly `96*6^128` labeled ordered paths.

**Actual local execution boundary:** the saved script was executed with small local interface shims transcribed from GitHub-read definitions of PREFIX-565 `edge` and PREFIX-566 `weighted_quotient`. Its original-module imports are directly compatible with the repository files, but this turn did not independently execute the full repository-native import path. This boundary is recorded rather than converting a local shim run into a claimed remote execution.

## 5. Information scope and next research

The reduction retains the full native six-axis BRC carrier as its source, the distinct marked edges and branch multiplicity, and exactly preserves *all future ordered gate-count generating functions*. Its specialized scalar readout does not retain individual axis-5/axis-6 rewards or arbitrary source-fiber queries. The concurrent canonical joint Poisson/covariance result is preserved separately.

Next executable study: form the exact three-parameter BRC gate transfer `P(x,y,z)` and calculate the first **mixed third-order axis/gate cumulants**, testing the axis-5/axis-6 exchange symmetry. Then identify the algebraic specialization locus where the generic parameterized gate-channel denominator decreases to the five-degree squared-spectral transfer computed here. Keep the same frozen input, source fiber and independent-review boundary.

## 6. Authority, publication and source status

GitHub authenticated login: `awdawmip`, admin access to both projects. Native Enterprise Math `em_status` and `em_session_start` both returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE` with `operation_sent=false`. Thus live native owner, Source Researcher-ID, formal CLAIM, Result and independent Driver review were **not** established. This is a self-contained author-side research artifact, not canonically admitted mathematical truth.

Exact source files: `PREFIX565_positive_marginal_certificate.py` (Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`), `PREFIX566_gate_quotient_certificate.py` (`7b6613193847e4123cd0ac11107eb9b9c70290c8`), prior PREFIX-575/576 proofs and current normative sources. All reused results retain their original source/admission status.
