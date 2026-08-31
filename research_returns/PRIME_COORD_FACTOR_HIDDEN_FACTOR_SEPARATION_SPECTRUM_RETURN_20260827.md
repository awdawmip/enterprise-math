# Prime Coordinate Hidden-Factor Separation Spectrum — Research Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-HIDDEN-FACTOR-SEPARATION-SPECTRUM`  
Publication-ID: `TP2-FC3E7A11955B41A7F002`  
Researcher-ID: `EM-PCF3-DCEC44`  
Claim-ID: `chatgpt-pcf3-20260828-0736-dcec44`  
Execution record: `ER-35F18043DAFAC4E0547B`

## 1. Frozen verdict

`SEPARATOR_FOUND_WITH_EXACT_SCOPE`

Hard target `HIDDEN_FACTOR_SEPARATION_SPECTRUM_CLASSIFIED` is met at research-return strength for distinct odd semiprimes. The load-bearing result is an exact three-level factor-blind valuation-wall spectrum for the public Enterprise kernel

\[
A_s=\binom{2s}{s}^2\binom{3s}{s}=\frac{(2s)!(3s)!}{(s!)^5}.
\]

The spectrum classifies every local synchronization state while `s` lies below the hidden factors, exposes a second-wall separator that costs no new kernel index, and proves that the previously frozen two-seed square-root fallback can be tightened to one deterministic public seed after first-wall synchronization.

This is **not** a factorization-speedup theorem. The exact recurrence still materializes a kernel at index `Theta(p)` on balanced inputs; complexity compression remains open.

## 2. PCF1-admitted typed response vector

The executable task-local vector contains only N-native quantities:

\[
\Sigma_N(s)=\left(P_N(s),K_N(s)\right).
\]

### 2.1 Public polynomial layer

For the PCF1-admitted fixed probe family

\[
\mathcal F=\{x^2+1,\ x^2+x+1,\ x^6-1,\ x^6+1\},
\]

define

\[
P_N(s)=\bigl(\gcd(f(s),N)\bigr)_{f\in\mathcal F}.
\]

For squarefree `N=pq`, the proof-side CRT projection is exact:

\[
\gcd(f(s),N)=\prod_{r\in\{p,q\}:\ f(s)\equiv0\pmod r}r.
\]

A proper output is therefore already an integerized separation event. Fixed-degree root support remains the PCF1 square-root-scale public-seed baseline; no stronger probability theorem is claimed here.

### 2.2 Kernel valuation-wall layer

Put `D_0=1` and for `k=1,2,3`

\[
D_k(N,s)=\gcd(A_s,N^k),\qquad H_k(N,s)=\frac{D_k(N,s)}{D_{k-1}(N,s)}.
\]

Every `D_k` and `H_k` is constructed from `N,s` alone. Hidden primes enter only the proof/verifier view.

For `N=pq`, distinct primes `3<p<q`, and `0\le s<p`, Legendre's formula gives, for `r\in\{p,q\}`,

\[
\boxed{v_r(A_s)=\left\lfloor\frac{2s}{r}\right\rfloor+\left\lfloor\frac{3s}{r}\right\rfloor.}
\tag{V}
\]

Because `s<r` and `3s<3r<r^2`, no higher Legendre term occurs. Hence

\[
\boxed{H_k(N,s)=\prod_{r\in\{p,q\}:\ v_r(A_s)\ge k}r.}
\tag{H}
\]

Equivalently the three wall thresholds are

\[
\boxed{
H_1=\prod_{r<3s}r,\qquad
H_2=\prod_{r<2s}r,\qquad
H_3=\prod_{r<3s/2}r,
}
\tag{W}
\]

where the products range only over hidden factors of `N`. Boundary equalities are impossible for primes `r>3` and integer `s`.

Thus the local valuation spectrum has exactly four bins:

| hidden prime position | local valuation `v_r(A_s)` |
|---|---:|
| `r>3s` | 0 |
| `2s<r<3s` | 1 |
| `3s/2<r<2s` | 2 |
| `s<r<3s/2` | 3 |

Two hidden factors are fully synchronized under `K_N(s)=(H_1,H_2,H_3)` iff they lie in the same bin. If their valuations differ, some `H_k` is exactly the smaller factor `p` and is already a proper gcd-ready integer.

## 3. Separation taxonomy

The task's requested mechanisms reduce as follows on the current admitted surface.

1. **Raw inequality:** proof-side local responses differ. It is useful only when represented by one of the integer outputs below.
2. **Valuation separation:** `v_p(A_s) != v_q(A_s)`; exactly equivalent to some `H_k=p` under `s<p`.
3. **Collision-time separation:** the first public dyadic seed at which `H_1 != 1` records which hidden `3s` wall was crossed first.
4. **Rank/determinant separation:** no frozen PCF1-admitted target map `N -> M_N` currently exists for the table/rank routes, so no rank/determinant coordinate is fabricated here. Such components remain `N-BLIND_BUT_N_TARGET_MAP_UNINSTANTIATED`.
5. **Shell/filament/packet/relational-axis separation:** PCF1 admits these only when a complete N-native carrier construction and support cost are supplied. Current sources do not freeze such a target map, so they are not silently promoted into the executable vector.
6. **Phase/Prime-Fusion separation:** factor-labelled phases remain proof-only. The admitted public polynomial layer above is the exact N-only remnant.

This removes redundant descriptive components instead of treating a larger vector as stronger by default.

## 4. Exact first-dyadic spectrum

Let

\[
j_*=\min\{j\ge0:3\cdot2^j>p\},\qquad s_*=2^{j_*}.
\]

Minimality gives

\[
\frac32s_*<p<3s_*<2p,\qquad s_*<p.
\tag{D}
\]

All earlier dyadic seeds have `H_1=1`. At `s_*`, exactly four cases exist:

### A. Direct first-wall separator

If `q>3s_*`, then

\[
H_1=p.
\]

### B. First wall synchronized, second wall separates

If

\[
p<2s_*<q<3s_*,
\]

then both primes cross the `3s_*` wall but only `p` crosses `2s_*`, so

\[
(H_1,H_2,H_3)=(N,p,1).
\]

This is a genuine second-level separator requiring no new `A_s`; it only replaces `gcd(A_s,N)` by the already N-only `gcd(A_s,N^2)` and quotient `H_2`.

### C. Full synchronization in the high bin

If

\[
2s_*<p<q<3s_*,
\]

then

\[
(H_1,H_2,H_3)=(N,1,1),\qquad q/p<3/2.
\]

### D. Full synchronization in the low bin

If

\[
\frac32s_*<p<q<2s_*,
\]

then

\[
(H_1,H_2,H_3)=(N,N,1),\qquad q/p<4/3.
\]

There is no fifth case. In particular `H_3=1` at the first dyadic wall in every synchronized case, so the third wall is **provably redundant at this collision time**.

## 5. Single-seed synchronization breaker

The original PCF4 research return used the pair

\[
\left\lfloor\frac{\sqrt N}{3}\right\rfloor,
\quad
\left\lfloor\frac{\sqrt N}{3}\right\rfloor+1
\]

after a synchronized first response. The spectrum classification shows the second seed alone is sufficient.

Assume first-wall synchronization. Then already `q<2p`; in the full-spectrum collision cases above the stronger `q<3p/2` holds. Define the public seed

\[
\boxed{u=\left\lfloor\frac{\operatorname{isqrt}(N)}3\right\rfloor+1.}
\]

Since `N=pq` is nonsquare, `3u` is the least multiple of `3` strictly above `sqrt(N)`, hence

\[
p<\sqrt{pq}<3u.
\]

Also `u<p`: from `q<2p`,

\[
u<\frac{\sqrt{2}}3p+1<p\qquad(p\ge5).
\]

It remains to show `3u<q`. If `q=1 mod 3`, then `q-1` is a multiple of 3 and, because distinct odd primes give `p<=q-2`,

\[
\sqrt{pq}\le\sqrt{q(q-2)}<q-1.
\]

If `q=2 mod 3`, then `q-2` is a multiple of 3. The case `p=q-2` would make `p>3` divisible by 3, impossible, so `p<=q-4` and

\[
\sqrt{pq}\le\sqrt{q(q-4)}<q-2.
\]

Therefore the least multiple of 3 above `sqrt(N)` is below `q` in both cases:

\[
\boxed{p<3u<q,\qquad u<p.}
\]

Applying `(V)` gives

\[
\boxed{\gcd(A_u,N)=p.}
\]

So **one** public fallback seed breaks every first-wall synchronization.

## 6. Exact N-only splitter induced by the spectrum

For a distinct odd semiprime `N=pq`:

1. compute `gcd(N,6)`; this returns `3` when `p=3`;
2. otherwise probe dyadic `s=1,2,4,...` and compute `H_1=gcd(A_s,N)` until the first non-unit response;
3. if `1<H_1<N`, return it;
4. if `H_1=N`, compute `H_2=gcd(A_s,N^2)/N`; if `1<H_2<N`, return it;
5. otherwise set `u=floor(isqrt(N)/3)+1` and return `gcd(A_u,N)`.

Every constructor input is `N` plus fixed public arithmetic. On the theorem domain the output is always a proper divisor.

The second-wall check can save the fallback kernel evaluation on the exact mid-straddle family. It does not change the asymptotic boundary: the largest required kernel index remains `Theta(p)` in balanced cases.

## 7. Exact collision registry and finite regression

The checker reconstructs the frozen PCF2 corpus with the same deterministic private generator and public seed policy `0..63`.

It first replays the two PCF2 admitted polynomial baselines exactly:

- quadratic public probes: `74/89` successes;
- sixth-power public probes: `84/89` successes.

This matches the frozen PCF2 report.

Among the 89 corpus cases, 61 are distinct odd semiprimes in the theorem domain. The N-only kernel spectrum splits all 61. First-wall classes are:

- `SMALL_PRIME_PRECHECK`: 3;
- `DIRECT_W1_SEPARATOR`: 33;
- `FULL_SYNC_HIGH_BIN_2S_3S`: 24;
- `FULL_SYNC_LOW_BIN_3S2_2S`: 1;
- `W1_SYNC_W2_SEPARATOR`: 0 in this particular frozen corpus.

The absence of the second-wall class from those 61 rows is a corpus fact, not a theorem. An independent exact enumeration of every pair of distinct odd primes below 300 gives 1,830 semiprimes with zero failures and the exact class counts:

- `SMALL_PRIME_PRECHECK`: 60;
- `DIRECT_W1_SEPARATOR`: 1,370;
- `W1_SYNC_W2_SEPARATOR`: 202;
- `FULL_SYNC_HIGH_BIN_2S_3S`: 118;
- `FULL_SYNC_LOW_BIN_3S2_2S`: 80.

Explicit second-wall witnesses include `(p,q,s)=(7,11,4),(13,17,8),(29,37,16)`.

Finite enumeration is regression/falsification only; theorem closure is Sections 2–6.

Row-level proof-side collision data for all 61 PCF2-domain semiprimes is frozen at:

- `research_artifacts/PRIME_COORD_FACTOR_HIDDEN_FACTOR_SEPARATION_SPECTRUM/evidence_bundle.json`.

Authoring digest of the pretty-printed evidence generated by the primary checker:

`sha256:93f529bec612b676173c3fbb4a1858e158e7c32a130f4f83989ed73cdcceea11`.

## 8. Verification

Primary exact recurrence checker:

`python scripts/check_pcf3_hidden_factor_separation_spectrum.py --out /tmp/pcf3_evidence.json`

Authoring output:

`PCF3_SPECTRUM_CHECK_PASS corpus=89 theorem_domain=61 splits=61 classes={"DIRECT_W1_SEPARATOR": 33, "FULL_SYNC_HIGH_BIN_2S_3S": 24, "FULL_SYNC_LOW_BIN_3S2_2S": 1, "SMALL_PRIME_PRECHECK": 3}`

Independent direct-binomial checker:

`python scripts/check_pcf3_hidden_factor_separation_spectrum_independent.py`

Authoring output:

`PCF3_INDEPENDENT_CHECK_PASS semiprimes=1830 zero_failures counts={'DIRECT_W1_SEPARATOR': 1370, 'FULL_SYNC_HIGH_BIN_2S_3S': 118, 'FULL_SYNC_LOW_BIN_3S2_2S': 80, 'SMALL_PRIME_PRECHECK': 60, 'W1_SYNC_W2_SEPARATOR': 202}`

Authoring SHA256:

- primary checker: `f878ffa37420862bb18dcab7280620912ead03d23afd2b55687195de74d1beb5`;
- independent checker: `f194154c1018bc121f0d90fbacd86f4311e86418f63166f3888de27fc53d0265`.

## 9. Ranked integerizable-asymmetry handoff

For PCF4 / future complexity-compression work, the spectrum ranks the usable signals:

1. **`H_1` at first dyadic wall** — strongest/cheapest; direct proper factor whenever `q>3s_*`.
2. **`H_2` at the same seed** — strictly additional information with no new kernel index; catches `p<2s_*<q<3s_*`.
3. **single public fallback `u=floor(isqrt(N)/3)+1`** — deterministically breaks all remaining synchronization using `H_1` only.
4. **fixed public polynomial probes** — admissible and useful as baselines, but their fixed-degree root support does not supply the kernel's all-semiprime theorem.
5. **`H_3` at first dyadic collision** — exact redundancy; always `1` there.
6. **rank/shell/filament/packet coordinates without a frozen `N -> carrier` map** — do not enter an extractor until such a map and its support cost are defined.

The smallest integerizable asymmetry is therefore not a high-dimensional coordinate vector: it is the nested wall quotient `H_1`, with `H_2` as the only task-local extra wall that can add information before fallback.

## 10. Source/dependency pins and boundary

Pinned current taskbook blob: `sha1:49047f8f7950bcb15c80316ebd733af2725d5a35`.

PCF1 accepted audit:

- result `RR-B8D8679EB033E990E825`;
- return blob `sha1:650a01f59534f2652b033873cc7c4dcd8038723a`.

Disclosed downstream evidence used for comparison, not assumed as unproved authority:

- PCF4 Draft PR #715 head `1a54ecb01626f76f869841c5eaea747ef519effc`;
- PCF2 Draft PR #740 head `dce4a309f8d799030081ed82e310c26a92d8f465`.

The valuation-wall theorem and one-seed fallback are proved again in this return and independently checked; they do not depend on Driver acceptance of PCF4.

## 11. Smallest unresolved residue

`COMPLEXITY_COMPRESSION_OF_VALUATION_WALL` remains open.

The exact separation spectrum proves that hidden-factor information exists and is integerizable under the N-only model. What is not proved is that the needed kernel state can be reached in time polynomial in `log N`, sub-square-root time, or faster than strong classical factorization baselines.

Recommended Driver disposition:

1. accept PCF3 at TASK scope as `SEPARATOR_FOUND_WITH_EXACT_SCOPE`;
2. route the simplified one-seed fallback and `H_2` wall quotient back to PCF4/complexity-compression work;
3. preserve PCF2 as the sealed benchmark surface;
4. do not promote any factorization-speedup or Foundation claim from this result.
