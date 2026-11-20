# R762HK — Exact positive-BRC flip-block transfer and a 14-event obstruction

**Task**: `RS-X6-TRIADIC-CLOSURE-DYNAMICS` / `TP2-8B7E13C5904A2D6F1142`. Historical Researcher `EM-X6-3050F6`, own session `MCP-4b2d70a97f594366a7c94a0f8b45df38`. This is author-derived and independently executable exact evidence, **NOT_REVIEWED**. The signed three-support Port transition remains a **composite candidate**, not a native primitive `TRIADIC_CLOSURE_E` event.

**Frozen science**: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`: `p000_reality_foundation.json`, `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, and joint-relation-preservation contract. **Predecessor**: R762HJ, `enterprise-math@2cc5ef6fb10f1d30d70738e9b6ddb9c563e3aa23`.

## HK1 — Universal two-state positive-source flip-block transfer

Let `m` be even and let `P_0,P_1,...,P_m=P_0` be a time-ordered, labelled closed walk of two-axis Ports in `X={0,...,5}`, with `|P_t ∩ P_{t+1}|=1`. Define `h_t=1_{P_t ∪ P_{t+1}}∈{0,1}^6`, `α_t=(-1)^t`, and `V=Σ_t α_t h_t`. Every signed history is specified uniquely by a bit word `b=(b_0,...,b_{m-1})∈{0,1}^m`, giving `ε_t=α_t(-1)^{b_t}`.

Define the **disjoint flip-block count** `k(b)=Σ_{t=0}^{m-1}(1-b_{t-1})b_t`, with the external initial bit `b_{-1}=0`. Thus a block is a maximal nonempty interval of consecutive ones, with *no cyclic wrapping*; this convention fixes a starting Port/event-time seam.

In the six-variable Laurent polynomial ring over nonnegative integers, write `x^w=∏_{i=0}^5 x_i^{w_i}`. Set the 2×2 transfer at event index `t` to

```
T_t(p,q) = u^((1-p)q) * x^(q α_t h_t),    p,q ∈ {0,1}.
G_m(u,x) = (1,0) · T_0 T_1 ... T_{m-1} · (1,1)^T.
B_m(u) = [x^(V/2)] G_m(u,x).
```

If some coordinate of `V` is odd, define `B_m(u)=0`. For all even `m` and all such named closed Port walks,

```
B_m(u) = Σ_{b : Σ ε_t h_t = 0} u^(k(b)).
```

In particular, `B_m(1)` is the **exact positive-source signed zero-Cell completion multiplicity**, and the least exponent with positive coefficient is the minimum number of alternating-sign flip blocks. This is a complete algorithm for the *fixed unsigned source history*; it is not a certificate for Port walks omitted by a later native permission rule.

**Proof**: In the product, a unique sequence of intermediate binary states `q=b_t` is chosen, starting with previous state zero. Its scalar weight is `u^k(b)` and its monomial weight is `x^(Σ b_t α_t h_t)`. All coefficients are nonnegative and no distinct source words cancel. Its completed signed displacement equals `Σ α_t(1-2b_t)h_t = V-2Σ b_t α_t h_t`. Hence exactly the required zero-displacement histories contribute to the indicated coefficient, with their exact block counts. QED.

An exact map-based dynamic program stores `(W,p)` where `W=Σ_{t<j} b_t α_t h_t ∈ Z^6`, `p=b_{j-1}`, and either the least block cost or the polynomial of block-count multiplicities. At `j` there are at most `2(2j+1)^6` such states. Therefore computing **minimum flip-block count and existence** takes at most `O(m^7)` exact small-integer transitions and `O(m^6)` active states, treating the six-axis dimension as fixed. Computing the **whole histogram** can be done within `O(m^8)` exact coefficient operations and `O(m^7)` coefficient slots. These are conservative combinatorial bounds; exact integer bit complexity is additional. This supplies a polynomial-in-length existence method for each fixed six-axis source word, versus testing all `2^m` signed words.

For odd `m`, zero displacement is impossible in this declared three-support model: summing the six coordinate equations gives `3 Σ ε_t=0`, so equal numbers of positive and negative signs are necessary.

## HK2 — A 14-event closed-Port two-block obstruction

Take the time-ordered walk, with seam `P_0=P_{14}=01`:

```
01 → 15 → 12 → 25 → 24 → 04 → 05 → 03 → 04 → 24 → 23 → 25 → 35 → 05 → 01.
```

Each consecutive Port pair shares exactly one axis, so all 14 three-support composite candidate events are legal under the *declared Port adjacency rule*. All six support-incidence counts are even:

```
d = (8,4,8,6,6,10),    V = (2,0,0,0,-2,0).
```

For the one-interval HJ2 repair, the required prefix difference is `V/2=(1,0,0,0,-1,0)`. An exhaustive check of the exactly `14·15/2=105` nonempty intervals gives zero matches. However, flipping the two disjoint blocks `[3,5)` and `[6,8)` from alternating signs (least-significant-bit-first mask `216`) yields six-coordinate displacement exactly zero.

Complete independent enumeration of all `2^14=16,384` signed source histories gives the zero-Cell completion **positive multiplicity** `104`, with exact block-count generating polynomial

```
B_14(u) = 20 u^2 + 46 u^3 + 36 u^4 + 2 u^5.
```

Thus the **minimum** is exactly two disjoint blocks; this improves R762HJ's previously exhibited 18-event obstruction to a 14-event explicit obstruction. No global minimal-length claim is made: the open range 10–12 requires exhaustive proof before the 14-event example could be called globally shortest. The 14-event walk is also a *subwalk shortening of the previously certified 18-event example*, not a separate physical force experiment.

## Verification and BRC scope

`R762HK_CHECK.cpp`, compiled with C++17, checks all 14 Port incidences, exact six-axis parity and alternating residual, all 105 one-interval candidates, all 16,384 signed-source words, the full flip-block histogram and a second, independently implemented positive-coefficient dynamic transfer. Both methods agree on `B_14(u)`; the explicit two-block signing directly sums to zero. The machine-generated JSON evidence is `R762HK_EVIDENCE.json`.

This BRC transfer retains the full 0/1 ordered source word, phase sign and positive branch multiplicity. It uses formal signed **Cell displacement**, not subtraction of positive BRC masses. Keeping `u` and the monomial residue preserves the distinctions needed for future block-aware queries. Summing `u` or projecting spatial coordinates is only an explicitly scoped current observer.

## Open continuation

1. Certify or disprove the one-block property at lengths 10 and 12 across all named closed Port walks; random sampling is not an exhaustive certificate. Search for an actual parity-valid **unsignable** Port history, rather than conflating failure of one-block repair with failure of all signings.
2. Study the growth of worst-case minimum flip-block cost under Port concatenation and seam changes.
3. Independently obtain a typed P000-native primitive force incidence, Cell/Link/Port/time update and triadic rotation permission. This composite candidate is not promoted to primitive dynamics.
4. Preserve existing owner and only associate this exact committed evidence with the existing Research Activity when authorized, retaining `NOT_REVIEWED` and authentic Source/CAS readback.

**End status**: author-proved HK1, explicit finite certificate HK2; general parity sufficiency unresolved; independent review `NOT_REVIEWED`.
