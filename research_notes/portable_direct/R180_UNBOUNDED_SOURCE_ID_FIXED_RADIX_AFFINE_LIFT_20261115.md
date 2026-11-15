# R180 — Fixed-radix lossless affine representation for unbounded source and branch IDs

Date: 2026-11-15. Proof status: AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED.

## Sources and scope

R179 predecessor at 763d6886f34e55944ed02b1f548bb74e87c86d70; R178 at b6b1f661422ade1329a9401797b6d4833c0b8e70. Frozen scientific input pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34 unchanged. P000 native six-dimensional signed X6 space; branch/source metadata are separate typed data, not spatial axes or heartbeat time. Current native target source: src/enterprise_math/brc_transport.py, blob be1debe367263931bd5e93fd750be3ed54624fe1.

## R180A — uniform 17-symbol embedding

Define a fixed tagged alphabet of 17 symbols: 0–11 are the 12 signed X6 primitive steps, 12/13 are binary digits 0/1, 14 is atom START, 15 atom END, and 16 the ID/SOURCE separator. For nonnegative integer n, BIN(n) is the canonical nonempty binary expansion (BIN(0) is one zero symbol). Encode an atom with arbitrary nonnegative integer branch identifier i, source identifier s, and finite ordered signed native spatial path P as

tau(i,s,P)=START BIN(i) SEP BIN(s) STEPS(P) END.

Concatenated atom words parse uniquely: the digit symbols are disjoint from step symbols and the delimiter symbols, and BIN is canonical. This represents unbounded nonnegative integer identifiers over a fixed alphabet without renaming older histories.

For every finite tagged word w, let m(w) be its number of native direction tokens, D(w) its six-axis displacement, and J(w) its sum of native-step prefix displacements; metadata tokens do not count as native movement. Let L(w) be the total number of tagged tokens and h(w) the positional base-17 code:

\[
h(w)=\sum_{r=1}^{L(w)}c(w_r)17^{L(w)-r}.
\]

Define the 13-dimensional rational affine map on Q^6 x Q^6 x Q:

\[
T_w(x,j,z)=(x+D(w),\ j+m(w)x+J(w),\ 17^{L(w)}z+h(w)).
\]

**Theorem:** for all finite tagged words u and v,

\[
T_u.\mathrm{then}(T_v)=T_{uv},\qquad T_u=T_v\iff u=v.
\]

**Proof:** metadata erasure is a monoid homomorphism, so m(uv)=m(u)+m(v), D(uv)=D(u)+D(v) and J(uv)=J(u)+J(v)+m(v)D(u). For the positional register, L(uv)=L(u)+L(v) and h(uv)=17^{L(v)}h(u)+h(v). Substitution proves the chronological affine composition formula. Equality of two affine actions forces equality of the z-linear coefficients 17^{L}, hence equal tagged lengths. Equality of z-translations implies the same fixed-length base-17 digit sequence, including possible leading zero symbols. Thus u=v. The reverse direction is trivial. Unique atom parsing then recovers every source ID, branch ID and spatial step. QED.

## R180B — exact positive BRC histogram transport

In the source EffectHistogram API, a term comprises positive rational weight, affine action and positive integer multiplicity. Since T_u=T_v iff u=v, native equal-(weight,effect) coalescence preserves exact typed-history identity: independent branches with distinct IDs remain distinct; identical complete history and weight merge by adding multiplicity. Alternatives are multiset sum and chronological serial composition is the Cauchy product with word concatenation. Thus the full tagged histories are sufficient for their exact source-sensitive, branch-sensitive, path-sensitive future observations. Signed-amplitude cancellation or physical heartbeat evolution is outside this positive-weight carrier.

Witness: two atoms of the same source 2^65+17, same native path (+E1,-E1), same positive rational weight 1/3, but IDs 2^65+3 versus 32 produce different effects despite identical native D and J.

## R180C — bit complexity

One encoded atom has exactly length |P|+bitlen(i)+bitlen(s)+3, using bitlen(0)=1. Its tagged-history positional code and affine z-slope use O(L log_2 17) bits for total token length L. At fixed length L, 17^L words need at least ceil(L log_2 17) bits of injective binary information. The encoded integers achieve this bit-size order; constant affine dimension is not constant machine-word storage or a proof of superior runtime.

## Exact reproduction and remaining work

Run R180_unbounded_ids_affine_check.py with Python integer and Fraction arithmetic; compare output with R180_verification.json. Tests passed:
- 5220 distinct positional codes over all tagged words length 0 to 3;
- 252 atomic ID/source/path combinations, including integer identifiers exceeding 2^65;
- 63,504 exhaustive ordered atomic pair parsing/statistics checks;
- 240 full 13 by 13 affine composition checks;
- a same-source/same-path different-ID witness.

The standalone reference checks passed. Native project module import is unavailable in the local sandbox (No module named enterprise_math); the script contains optional native Affine and EffectHistogram assertions for an installed project runtime. Actual native integration is LOCAL_VALIDATION_PENDING. Independent mathematical review NOT_REVIEWED.

This is independent portable research. Historical research identity EM-DIRECT-BF4AD7, session MCP-46f202db13e64ad6b4c8860e06908245, activity RA-7A118452894D2600AE7DE5A2; no formal CLAIM or authorized source execution. Activity semantic checkpoint association remains pending.

Next: native BRC integration, exact operation/bit-cost comparison with source-specific minimal observer quotients, selective provenance query correctness and recurrence conditions.
