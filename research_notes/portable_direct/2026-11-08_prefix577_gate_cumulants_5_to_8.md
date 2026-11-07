# PREFIX-577 — Exact fifth-through-eighth gate-cumulant rates from the frozen native X6-BRC quotient

**Status:** `AUTHOR_PROVED / EXACT_RATIONAL_AND_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED`  
**Date:** 2026-11-08  
**Scientific input pin:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`  
**Continuation base:** `research/prefix576-gate-cumulant-r2-20261108@aac16d053758b632b506ebe3658b9312579a0b8d`  
**Normative project snapshot:** `awdawmip/enterprise-math main@4efef1592c0e576b11478352e8ca97c835ebd3ee`  
**Global canonical snapshot:** `awdawmip/chatgpt-global-knowledge main@e59021b80d20301a16bd75cc94398fde441719d2`

## 1. Question and scope

PREFIX-576 established exact asymptotic gate-count cumulant rates through order four for the frozen four-STAR native X6-BRC kernel, with all six BRC weights specialized to one and the gate counter retained.

This continuation extends the same rank-one resolvent and mean-zero group-inverse calculation through order eight, without changing the frozen input or observer.

The model remains:

- 48 native phases and 96 ordered branch ports;
- six labeled native actions from every port;
- the exact 37-class gate-preserving quotient;
- three marked native gate edges `(7,9)`, `(29,9)`, `(31,9)`;
- observer `q1=q2=q3=q4=q5=q6=1`, with the gate count retained;
- stationary initial law `pi_i = class_size_i / 96`.

Depth `d` counts ordered native actions. It is not physical time, a heartbeat interval, or a solver iteration.

## 2. Exact BRC quotient and rank-one update

Let `C` be the 37-by-37 integer transition-count matrix of the exact gate-preserving quotient and `P=C/6`. Every row of `C` sums to six. The class-size vector is

`(8,4,2,1,1,2,2,8,4,2,4,4,2,4,1,1,1,1,2,2,4,2,4,4,2,2,2,2,2,2,2,2,2,2,2,2,2)`,

with total 96 and exact stationarity identity

`sum_i size_i * C[i,j] = 6 * size_j`.

The marked quotient edges are exactly

`4 -> 5`, `15 -> 5`, `17 -> 5`,

each with multiplicity one and zero retained `q5,q6` exponents. Thus, with `g` the indicator of source classes `{4,15,17}` and `e_5` the target-class basis vector,

\[
P(z)=P+(z-1)\frac{g e_5^{\mathsf T}}6.
\]

The stationary gate-source mass is `pi(g)=1/32`, giving

\[
a=\frac{\pi(g)}6=\frac1{192}.
\]

The quotient is strongly connected, bipartite with class sizes `(17,20)` and stationary masses `(48,48)`, and has period exactly two (the verified two-cycle `0 <-> 7`). The marked update preserves the support for real `z>0`.

The matrix determinant lemma gives the exact secular equation

\[
1=(z-1)R(\lambda(z)),\qquad
R(\lambda)=\frac16 e_5^{\mathsf T}(\lambda I-P)^{-1}g,
\]

where `lambda(1)=1` is the positive Perron branch.

## 3. Group-inverse chain through the seventh potential

Put `L=6I-C` and `q=g-(1/32)1`. Let `G=(I-P)^#` be the group inverse on the mean-zero subspace. The existing PREFIX-576 vectors `X,Y,Z` are retained and rechecked. Four additional integer vectors `U,V,W,T` were solved exactly from

\[
\begin{aligned}
LX&=2304g-72\mathbf1,\\
LY&=72X,\\
LZ&=72Y,\\
LU&=72Z,\\
LV&=72U,\\
LW&=72V,\\
LT&=72W.
\end{aligned}
\]

All seven vectors have zero class-size-weighted mean. Their exact denominators are

\[
384,\ 4608,\ 55296,\ 663552,\ 7962624,\ 95551488,\ 1146617856,
\]

so they represent, respectively,

\[
Gq,\ G^2q,\ G^3q,\ G^4q,\ G^5q,\ G^6q,\ G^7q.
\]

Every one of the seven 37-row integer systems was checked exactly. The new target-class entries are

\[
U_5=240497,\quad V_5=6434489,\quad
W_5=143140289,\quad T_5=2855382857.
\]

The complete new `U,V,W,T` integer vectors and denominators are in `PREFIX577_GATE_CUMULANT_ORDER8_RESULTS.json`; the inherited `X,Y,Z` vectors remain in the PREFIX-576 certificate and are rechecked by the new checker.

Consequently,

\[
R(1+\epsilon)=\frac{a}{\epsilon}
+r_0+r_1\epsilon+\cdots+r_6\epsilon^6+O(\epsilon^7),
\]

with

\[
\begin{aligned}
r_0&=-\frac{19}{2304},&
r_1&=\frac{79}{27648},&
r_2&=\frac{5801}{331776},\\
r_3&=-\frac{240497}{3981312},&
r_4&=\frac{6434489}{47775744},\\
r_5&=-\frac{143140289}{573308928},&
r_6&=\frac{2855382857}{6879707136}.
\end{aligned}
\]

## 4. Exact cumulant rates through order eight

Write `delta=z-1` and

\[
\lambda(z)=1+\sum_{j=1}^{8}c_j\delta^j+O(\delta^9).
\]

Substituting this series into `1=delta*R(lambda(z))` and solving coefficientwise gives

\[
\begin{aligned}
c_1&=\frac1{192},\\
c_2&=-\frac{19}{442368},\\
c_3&=\frac{55}{127401984},\\
c_4&=-\frac{5561}{2348273369088},\\
c_5&=-\frac{11483}{169075682574336},\\
c_6&=\frac{7239035}{2077601987473440768},\\
c_7&=-\frac{62030683}{598349372392350941184},\\
c_8&=\frac{53399880289}{22057551263871625095806976}.
\end{aligned}
\]

For the stationary-initial gate count `K_d`, define

\[
\psi(s)=\lim_{d\to\infty}\frac1d\log\mathbb E[e^{sK_d}]
       =\log\lambda(e^s).
\]

The quotient is finite, irreducible and period two. Its two cyclic classes have primitive squares; the positive Perron branch is simple and analytic near `z=1`, while the parity-dependent positive prefactors contribute only `O(1/d)` to the scaled logarithm and each fixed derivative. Therefore the derivatives through order eight are the asymptotic cumulant rates.

The exact result is

\[
\boxed{
\begin{aligned}
\kappa_1&=\frac1{192},\\
\kappa_2&=\frac{1127}{221184},\\
\kappa_3&=\frac{206963}{42467328},\\
\kappa_4&=\frac{434651857}{97844723712},\\
\kappa_5&=\frac{203828245435}{56358560858112},\\
\kappa_6&=\frac{9969866857747}{4809263859892224},\\
\kappa_7&=-\frac{5831243834665333}{8310407949893763072},\\
\kappa_8&=-\frac{102557264405132243707}{19147179916555230117888}.
\end{aligned}}
\]

The first four rates reproduce PREFIX-576 exactly. The new mathematical increment is the fifth through eighth rate, including the negative seventh and eighth cumulants.

Equivalently, the scaled cumulant generating function through degree eight is

\[
\begin{aligned}
\psi(s)={}&\frac{s}{192}
+\frac{1127s^2}{442368}
+\frac{206963s^3}{254803968}
+\frac{434651857s^4}{2348273369088}\\
&+\frac{40765649087s^5}{1352605460594688}
+\frac{9969866857747s^6}{3462669979122401280}\\
&-\frac{833034833523619s^7}{5983493723923509411840}
-\frac{14651037772161749101s^8}{110287756319358125479034880}
+O(s^9).
\end{aligned}
\]

## 5. Independent finite exact moment cross-check

The checker performs stationary-initial integer dynamic programming on the same 37-state gate-count multigraph, extending the raw-moment recurrence to orders one through eight and depth 128.

It verifies:

- 96 native ports, six outgoing and six incoming actions per port;
- the three exact native gate edges and all nine frozen-root marginal checks;
- quotient refinement `[1,4,13,21,33,37]`, 37 row sums and the exact stationary identity;
- the three marked quotient edges, strong connectivity, bipartition and period two;
- all seven mean-zero group-inverse Poisson systems, each across 37 rows;
- exact raw moments of orders 1–8 at depths 0 through 128;
- the depth-128 total of

`385151223796572526086245125219434606018278638823213973691750235774923749432850295860047477336478580736`

ordered native paths;
- exact agreement of the depth-128 first through fourth finite cumulant rates with the previously published PREFIX-576 result.

The new checker returned `ALL_CHECKS_PASS` in a source-derived local harness using the exact `edge`, `marginal_gate_rows` and `weighted_quotient` definitions fetched from the immutable PREFIX-565/566 blobs, the published PREFIX-576 `X,Y,Z` vectors, and the exact depth-128 first-four rates read from the immutable PREFIX-576 result JSON. This was not a full repository checkout run; the published script imports those existing branch-local files when run from the research directory.

The finite DP is an independent integer cross-check of the recurrence and higher-moment implementation. The asymptotic limits follow from the exact rank-one secular equation, the seven group-inverse certificates and the finite irreducible period-two Perron argument—not from finite-depth convergence alone.

## 6. BRC reuse and evidence boundary

`COMPOSE_APPLIED`:

- `PREFIX565_positive_marginal_certificate.py`: frozen native 48-phase/96-port X6-BRC edge and signed-axis marginal definition;
- `PREFIX566_gate_quotient_certificate.py`: exact 37-class quotient retaining the gate mark and `q5,q6` marginal exponents;
- `PREFIX575_gate_count_poisson_certificate.py`: existing first/second Poisson potentials and variance identity;
- `PREFIX576_gate_cumulant_rank_one_certificate.py`: existing first through third group-inverse potentials and order-four cumulant result;
- exact Fraction/integer group-inverse extension and moment DP in the new PREFIX-577 checker.

No new top-level BRC family is claimed. No classical trigonometry, pi expansion, Taylor/Padé/Cayley propagation, floating-point scientific update or physical-time interpretation is used. The exact rational algebra is a derived observer on the actual typed native BRC transition table.

The theorem is restricted to the frozen `q1=...=q6=1` gate-count observer. It does not prove the parameterized `x=q5,y=q6` gate-sensitive positivity problem, a physical gate law, physical-time calibration, instantaneous transmission or Shor speedup.

## 7. Provenance and actual control state

- Global entries read at `chatgpt-global-knowledge main@e59021b80d20301a16bd75cc94398fde441719d2`: bootstrap blob `bc9e1b3065eae7947850a0aa2261dc201a43265c`; operating-manual blob `9ce8584221f83f3de369af7239b029e4b36621c4`; sync-marker contract blob `b9292a6a34b415e4c875fd4fddd0e864d718c826`; ACTIVE worldview blob `99238c3466eb0805748bae01fd1a20868a5a351e`; conclusion policy blob `4f864c98094a0ebcfe335ac3019ed343dba94bcc`; mathematical evidence policy blob `dac8160a7e99e1a25ff8815c59ee007f9452832b`; global P000 startup projection blob `c6d4d2d79b09537bdae55253baef9c28583e44dc` (V4 projection only).
- Current project source read at `enterprise-math main@4efef1592c0e576b11478352e8ca97c835ebd3ee`: continuation protocol blob `79002ab20e30abb464837dc4c980cf5b5b68e001`; portable research protocol blob `5633f5fa72097fb4d6afcf7ff23a0df3797fd4d0`; researcher startup-context protocol blob `fa596bc1fcaa3c9b304201490c3def422d035c4e`; research-method record blob `b1c3555220bccce46db84363af94e4a3e0d0df9c`; activity-registration protocol blob `1511d9b1d99ae7e785496a94528d0729c684b7b1`; foundation-startup package blob `16b0658a5c4effdaa9b4be62d3d813c0b08a69e0`.
- Source P000 V5 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488` (the global V4 projection does not replace it); joint-relation observer-preservation blob `3923890d77a02d84b772f789e6912dd14f220d14`; heartbeat-world contract blob `94a02d067be2b039ca4c0f7ffedb5ebde8430e08`; residual-fidelity contract blob `de980f972de840c55d2535dbf4e40be7e03659ed`.
- BRC-only arithmetic route was read in both project and global forms; global BRC-only markdown blob `929b159f5fffc3d293ba6954aaa76354ca33a556`; identical global/project machine mirror blob `62ffa6bbdafd54496e27284a26a2aeaf2d04df99`; BRC priority policy blob `721ea6b559ca8a4ac11c7ed90e715219581d319b`.
- Frozen science pin `f42f2906d77f24085c123f3ccfe9667d41caa96d` is unchanged. Existing PREFIX-565/566/575/576 source blobs at the continuation branch are `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`, `7b6613193847e4123cd0ac11107eb9b9c70290c8`, `f80228126d1f015615d7324bbde36f13c5b4e84b`, `d1ba22145e7c38afbda26469f23dc10849285cc0`, and prior result blob `852cf01f83c5bbf54c5ea087d41c2d77bae2d7fe`.
- Existing author branch base, refreshed immediately before publication: `research/prefix576-gate-cumulant-r2-20261108@aac16d053758b632b506ebe3658b9312579a0b8d`.
- New checker SHA-256 `9926a76fb948c7f11feb35f52670ed47b882a9cececc73243d9276048e7b6bef`; result JSON SHA-256 `63f50cd39d8b8cbeb3388bfe9bc10461d7554a3b4198846e5ce8001a42f23651`.

GitHub identity `awdawmip` and repository administrator/write permission were verified. The native gateway reported `CONFIGURED_NOT_LIVE_VERIFIED` with `backend_connected=false`. `em_session_start`, `em_sources`, context-manifest lookup and `em_control_dispatch` returned no native Researcher session or active Owner; dispatch specifically returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE` with `operation_sent=false`. No credential was reused or submitted. This is an unshared author-side derivation, not a formal Task claim, live activity registration, Source Result, independent review or mathematical admission.

## 8. Next question

Derive the full exact rational secular function `R(lambda)` from the same 37-state gate-preserving quotient. This would package the entire higher-cumulant sequence into one exact rational object and provide a direct route to all-order coefficient identities. The parameterized `x=q5,y=q6` observer remains a separate subsequent question.
