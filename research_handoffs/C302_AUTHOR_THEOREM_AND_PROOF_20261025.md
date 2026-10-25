# C302 — Exact scalar content and primitive integer numerator for 125 frozen auxiliary paths

Date: 2026-10-25. Researcher: `EM-DIRECT-25C302`; Activity: `RA-R2C30220261025T201217CST`. Scientific classification: **AUTHOR_EXACT / SOURCE_EXPOSED / NOT_ADMITTED**. This is a result solely for the C195/H168 **79-positive-rational-branch auxiliary model**. No theorem about signed/phase GF(2)-BRC, the native Heartbeat X6 cell geometry, or dynamics is asserted.

## 1. Question, exact context, and inherited dependencies

C300 determined that the rational functions on 125 frozen C293 dyadic parameter paths have reduced denominator degree 352 (124 paths), with degree 265 on path index 28, after removing exactly two linear factors. C301 established exact integer content and positive full-strip bounds for the reduced denominator, yielding the conditional sufficient nonroot sign precision `P=352*b+13702+134`. It left the **integer scalar content of the numerator-denominator pair** undetermined.

Frozen predecessor artifacts: C275/C284/C288/C293, C298, C300, C301; C301 immutable author commit `a616a2443d9d4083c0024f3f6841e782b2e62ca8`. Global canonical source snapshot: `d69588fe0c92d1ec230ac60df6fc805e96fbf762`; Enterprise Math canonical source immediately prior to registration: `f651ea40d12cee192ecab1bc741f98f1a9e01892`. The current activity was registered and read back at `eea9b43411984e23a345c95824f3b6340481ec80`.

All constants and 125 paths are the frozen inputs bundled in C301's portable archive. C300's **no further polynomial cancellation** and C297's **uniform outward interval width** are inherited author-level dependencies; they have not been independently readmitted here.

## 2. Exact construction in the integer polynomial ring

Write path `i`'s normalized auxiliary scalar observable as

`f_i(t) = sum_{j=1}^{79} c_j prod_r (n_{jr}(t)/d_{jr}(t))`

over the frozen short parameter strip. Here all the `n,d` have **integer coefficients**, `c_j` are rational, and each oriented integer denominator has a positive integer-content decomposition `d_{jr}=h_{jr}q_{jr}` with primitive `q_{jr} in Z[t]`. Define

- `P_i(t)=prod_q q(t)^{e_i(q)}`, with `e_i(q)` the maximum multiplicity of factor `q` across the 79 terms;
- `s_i=lcm_j (denominator(c_j) prod_r h_{jr})`;
- `D_i^{shared}=s_i P_i`;
- `T_{ij}(t)=numerator(c_j) * (s_i/(denominator(c_j)prod_r h_{jr})) * prod_r n_{jr}(t) * (P_i(t)/prod_r q_{jr}(t))`.

Every quotient and scalar in `T_{ij}` belongs to `Z[t]` by construction, so

`A_i^{shared}=sum_j T_{ij} in Z[t]`, and `f_i=A_i^{shared}/(s_i P_i)`.

C300 identified two distinct primitive linear factors `q_{i,0}, q_{i,1}` with exactly zero residues and no other rational-function polynomial cancellation. In this run, we additionally performed **exact integer polynomial divisions**, with every leading coefficient division exact and every remainder identically zero:

`A_i^{red}=A_i^{shared}/(q_{i,0}q_{i,1}) in Z[t]`,

`P_i^{red}=P_i/(q_{i,0}q_{i,1}) in Z[t]`.

Thus the normalized pair has `f_i=A_i^{red}/(s_i P_i^{red})`. By C301 and Gauss's lemma, `content(P_i^{red})=1` and `content(s_i P_i^{red})=s_i`.

## 3. New exact content theorem: all 125 pairs

Define `a_i=content(A_i^{red})=gcd_k |[t^k]A_i^{red}|`, and `g_i=gcd(a_i,s_i)`.

**Exact computational theorem C302-I.** Complete integer-polynomial coefficient expansion, exact Z[t] divisions, exact coefficient gcds and full 125-path verification produced

`a_i=g_i` for **every** `i=0,...,124`.

The saved certificate carries each `g_i` as a decimal integer plus the SHA-256 of the full coefficient sequence, encoded as decimal coefficients separated by newlines with final newline. The program checks `s_i mod g_i=0`, and computes both `a_i.bit_length()` and `g_i.bit_length()`. For every index these bit lengths are equal. As `g_i | a_i`, equality of their bit lengths forces `g_i=a_i`: a strictly larger multiple is at least `2g_i` and has strictly greater bit length.

The 125 gcd bit lengths range from **273 to 418**. In particular the full integer numerator `A_i^{red}/g_i` is now **primitive** as a polynomial in `Z[t]`, and the integer pair

`(A_i^{prim},D_i^{prim})=(A_i^{red}/g_i,(s_i/g_i)P_i^{red})`

is primitive: the gcd of all coefficients across both polynomials is 1. The prior C300 rational-polynomial reducedness remains unchanged; there is no additional claimed `Q[t]` factor cancellation.

This is a 125-instance exact finite computation, *not* a universal theorem about arbitrary 79-branch input families.

## 4. Stronger continuous-strip denominator height

For each frozen short strip `I_i`, C301's exact positive rational endpoint-product majorant `U_i` satisfies `D_i^{red}(t)<=U_i` for **every real** `t in I_i`. Therefore, for the primitive pair,

`0<D_i^{prim}(t)<=U_i/g_i`.

Let `H_i^{old}` denote C301's certified exponent `U_i<2^{H_i^{old}}`, and put `m_i=bit_length(g_i)`. The elementary integer bound `g_i>=2^{m_i-1}` gives

`U_i/g_i < 2^{H_i^{old}-m_i+1}`.

For **every index except 63**, the maximum of those 124 explicit conservative exponent bounds is **13317**. For index 63 the exact rational expression was re-evaluated and found to have `H_63^{old}=13702` and

`2^{13399} <= U_63/g_63 < 2^{13400}`.

Consequently the uniform strict continuous-strip estimate is

`0<D_i^{prim}(t)<2^{13400}` for all 125 paths and all real `t in I_i`.

The exponent 13400 is the exact maximum of the explicitly used endpoint-product majorants after scalar reduction; this does **not** claim that it is the optimal upper bound on the actual function `D_i^{prim}(t)`.

Special path 28: `degree=265`, old exponent 10767, new exact endpoint-product exponent **10349**.

## 5. Improved *conditional* dyadic sign precision

For `t=k/2^b in I_i` and `f_i(t)!=1`, the polynomial `N_i=A_i^{prim}-D_i^{prim} in Z[t]` is nonzero at `t`. Since `degree(N_i)<=d_i`, the number `2^{d_i b} N_i(k/2^b)` is a nonzero integer. Thus

`|f_i(t)-1|>2^{-d_i b-13400}`.

**Conditional on the inherited C297 outward evaluator having normalized total width strictly below `2^{134-P}`, the certified sufficient uniform sign precision becomes**

`P >= 352*b + 13400 + 134`.

At `b=512`, this is **193758 bits**, compared with C301's **194060 bits**, a reduction of **302 sufficient-precision bits**. On the exceptional path 28, the individual bound is `265*512+10349+134=146163` bits. These are mathematical worst-case sufficiency bounds, not measurements of runtime, memory or algorithmic optimality. At an exact root, no finite strict-sign certificate is possible.

## 6. Reproducible computation and validation boundary

The primary script `C302_SCALAR_CONTENT_EXACT.py` expands full `Z[t]` coefficients on all 125 paths with Python integer arithmetic, using an exact polynomial long-division implementation and 79-term coefficients derived from the frozen input. For practical execution limits, the 125 complete records were computed in 7 chunks of respectively 20,20,20,20,20,20,5 paths, then checked as a continuous ordered sequence 0..124. Every path also passed two exact algebraic evaluation identities at `t=0` and `t=1` (250 checks, algebraic extension only).

An independently implemented `sympy.Poly(...,domain=ZZ)` calculation recomputed the complete coefficient vectors for indices **0 and 28** and matched the exact numerator coefficient SHA-256 and scalar gcd. This is **2/125 independent polynomial-engine checks**, not 125. A separate nine-index test `{0,8,24,28,40,63,64,96,124}` compared the original `original_F(v,W)/Q` with the separately expanded 79-term formula at valid dyadic-strip midpoints, all exact equalities. The scalar-height verifier rechecks all 125 conservative bounds and recomputes the critical strip products for indices 63 and 28 with `Fraction`.

No formal checker, independent Research Driver review or Source admission was performed. No native signed/phase BRC operations were performed. The two canceled terms retain branch identity and individually stored provenance under any future-operation or observer scope that can distinguish them: **scalar cancellation in this auxiliary readout is not a branch-information-preserving quotient**.

## 7. Sources, state and next unit

Source status: this is an **author research branch** artifact; it is not a canonical task Result, CLAIM, review, Working Truth or change to P000. The native read-only EM control endpoint returned `CONTROL_QUOTA` on task inventory and `STATIC_READONLY_SCOPE_DENIED; operation_sent=false` on new execution session; live owner was therefore **not verified**. No existing active claim was displaced.

Suggested C303: design a fast p-adic/content computation avoiding full 352-degree `Z[t]` numerator expansion, prove exact prime-adic valuation sufficiency, and quantify bit complexity against this C302 oracle. In parallel, formulate a **declared observer- and future-operation-preserving native typed BRC/X6 bridge**; the auxiliary simplification alone is not such a bridge.
