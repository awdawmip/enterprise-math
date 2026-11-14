# EC49CS — Expanded signed-X6 BRC: universal suffix rank and earliest three-operation saturation

2026-11-01 (Asia/Shanghai). **AUTHOR_ANALYTIC_PROOF / EXACT_Q_CLASS_ALGEBRA_PASS / EXACT_INTEGER_WITNESS_PASS / NATIVE_BRC_AUDIT_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED.** Author-side continuation of EC49CR in PR #1730; this research is not an admitted Result.

## Frozen inputs and exact scope

GLOBAL_KNOWLEDGE_V1 `main@92504df7f8729f0200e0a65c7b95d2a236e2efb4` (P000 and ACTIVE worldview unchanged); Enterprise Math `main@42da097851a02b96f8ff2018f5c28096eec13866`; parent EC49CR `8c1c07cc61bca7e2bcdc08a50e56bce47a832b5a`. Primitive model: ordered `±E1,…,±E6` steps with BRC positive weights `w0=(2,3,3,2,1,1)`, `w1=(3,2,3,2,1,1)`, negative weights 1, and independent path-count channel. A nine-state DFA records A=(+E1,+E2) and B=(+E2,+E1) **ordered** subword completion and four final joint tags. All six signed displacement coordinates are retained; only first two can be nonzero for targets of the selected suffix language. No physical time or slice embedding is asserted.

Complete suffix operations: `a=(-1,-1)`, `b=(-2,-2)`, `c=(1,2,-1,-2)`, `d=(2,1,-2,-1)`, `e=(3,1,1,-3)`. Their signed X6 net displacement in first two coordinates: `(-2,0),(0,-2),(0,0),(0,0),(2,0)`. Let `S'={a,b,c,d,e}`; `R_u(tag,channel)` is the exact positive BRC weighted sum over actual prefix paths which become net-zero after appending complete operation word `u` and finish at that tag. Minima below refer only to rational-linear additive exact observer states for this language.

## Theorem 1 — universal all-h minimal formal dimensions

For all **integers h ≥ 2**,

```
dim_Q O_{S'^h}       = 3*(11*h*h+15*h+8)/2
dim_Q O_{S'^{1..h}}  = 18*h*h+24*h+12
```

For `h=1`, both dimensions equal 45. Therefore at h=3 the exact-h rank is **228** from 125 suffix words and the cumulative rank is **246** from 155 suffix words (h=2 regression: 123 and 132).

**Full proof, not finite extrapolation.** Each formal readout row on a given signed target is a function on the nine possible starting DFA states. Its suffix BRC weight is a positive, nonzero scalar for a fixed channel; consequently only the rational rowspace of the four final-tag indicator functions matters. Different signed target fibers form a direct sum. Define `L_s f=f◦F_s`, where `F_s` is the exact DFA action of complete operation s. Write a target as `(2u,2v,0,0,0,0)`; `u∈Z,v≥0`. Exact-h spaces satisfy

```
V_0(0,0) = U4 (the 4-dim final tag-indicator span);
V_h(u,v) = L_a V_{h-1}(u-1,v) + L_b V_{h-1}(u,v-1)
         + L_e V_{h-1}(u+1,v) + L_c V_{h-1}(u,v) + L_d V_{h-1}(u,v);
```

where plus denotes **linear span**, and fibers outside `|u|+v≤h` vanish. The following **finite exact-Q nine-column identities** are directly computed from the five literal operations and independently checkable by rational elimination. Let
`U3=L_cU4+L_dU4`, `K3=L_aU3`, `U5=U3+K3`, `U6=U3+U4`.
Their dimensions are respectively `3,3,5,6`, with `dim U4=4`. For every `U∈{U3,U4,U5,U6}`, `L_cU+L_dU=U3`. For each `s∈{a,b,e}`, `L_sU4=L_sU6=U4` and `L_sU3=L_sU5=K3`. Finally, `U4+U5=U6`. Exact rational checker and its nine-column bases are recorded in the author's reproducible evidence.

Set `t=h-(|u|+v)`. Induction using these finite identities gives: boundary `t=0 → U4`; for `h≥2`, odd interior t → U5 and positive even interior t → U6. The sole base exception is `h=1,u=v=0 → U3`. Proof: the c/d predecessor of every interior fiber supplies U3, and for h≥2 at least one neighboring a/b/e predecessor exists; its class has the parity of t (depth t or t−2), contributing K3 for odd t and U4 for even t. Boundary nodes have only U4-valued a/b/e predecessors. Thus the exact-h fiber counts are `2h+1` boundary, `h(h+1)/2` odd interior and `h(h-1)/2` positive even interior. Their one-channel total is `4(2h+1)+5h(h+1)/2+6h(h-1)/2=(11h²+15h+8)/2`. For the cumulative horizon, every interior fiber is U6: the odd depth-1 U5 joins the previous boundary U4, and deeper odd layers join a previous even U6. Hence `4(2h+1)+6h²=6h²+8h+4` per channel. Three independent **formal** BRC channels triple these values. □

The recurrence uses only `(h+1)^2` fibers and ≤9 rational coordinates per fiber; horizons 1..H require O(H³) bounded-dimension rational row operations and O(H²) basis storage instead of enumerating `5^h` future words. Bit-cost depends on rational coefficient sizes.

## Theorem 2 — first true-path saturation at h=3

For **actual ordered signed-X6 prefixes with correlated two BRC weights and path count**, both observation languages first attain their formal ranks at even length **n=14**:

```
n=10: modulo-certified lower bounds 221 (exact h=3), 238 (cumulative ≤3)
n=12: exact-Q ranks               227 / 228,       245 / 246
n=14: genuine path integer minors 228 / 228,       246 / 246
n>=14 even: full ranks by neutral (+E3,-E3) prepend.
```

The only rank-deficient n=12 target is `(-6,0,0,0,0,0)`, short by one in both languages. The exact-Q dynamic program retains ≤3 genuine rationally independent *weight triples* per (six-component endpoint, nine-state DFA). Continuation from the same typed state acts on these triples by the same invertible diagonal map, so the retained triples span **all** possible length-n genuine path observations, not a sample. Its backwards L1/parity cone is an exact signed-axis reachability test. This proves the n=12 upper bounds. For n=14, the 15 already-full n=12 fibers have literal independent path minors extended by neutral prefix `(+E3,-E3)`, multiplying their weight triples by invertible `(3,3,1)`; a focused endpoint-cone search gives a literal 12-path full-rank minor at the exceptional target. **All 16 fiber determinants** are nonzero mod **1,000,003** for both languages; nonzero mod prime proves Q independence. Odd n have the wrong endpoint parity, and all lower even n inject under repeated neutral prefixes into the rank-deficient n=12 space. □

For the n=14 cumulative certificate, the 16 determinant residues (ascending targets) are
`753899,639851,265243,949830,135535,367516,750611,211087,445528,399539,211087,445528,399539,445528,399539,399539`.
The two n=14 certificates contain 228 and 246 genuine literal paths, independently replayed for signed endpoints, ordered A/B tag updates, both exact BRC weight products, counts and all determinants. The aggregate **native signed positive BRC endpoint** implementation independently agrees with the typed exact-integer DP at n=12 and n=14 for **155 suffixes × 3 channels = 465 comparisons each** (930 total); all four tag totals also match. The native endpoint kernel alone does not perform label filtering.

## Evidence and limits

Author-executed source scripts: exact 9-column Q class algebra, recursive horizon rowspaces checked through h=18, explicit 125/155-word h=3 enumeration, exact-Q typed-state DP through n=12, n=14 authentic-path modular minors and an independently written replay checker, plus separate native BRC comparisons. Complete original scripts, JSON, witness paths and logs are retained in the author evidence archive; a compact portable verifier/certificate is supplied in this directory. No claim about arbitrary nonlinear encodings, positive-weight signed phase cancellation, fixed-size unbounded future memory, three-dimensional native slice geometry or physical stability.

Related literature (background, not a proof of this specific result): Balle–Panangaden–Precup, *A Canonical Form for Weighted Automata and Applications to Approximate Minimization* (2015), https://arxiv.org/abs/1501.06841; Lopez, *Commutative ℕ-Rational Series of Polynomial Growth* (STACS 2025), DOI 10.4230/LIPIcs.STACS.2025.67. The latter treats commutative series; the present suffix language preserves primitive letter order.

## Next, provenance and authority

Next **EC49CT**: compute h=4 true-prefix ranks at n=14,16 using exact-Q compressed typed bases and modular genuine-path certificates, then test a uniform saturation threshold. Source-native `em_status` (2026-11-01) returned `research_authority_granted=false`, `executor_binding_configured=false`, `source_sync.control.state=CODE_REVIEW_REQUIRED`; active Owner inventory returned `CONTROL_QUOTA` (active 5/5). No CLAIM, Source Research-Activity, formal Result, independent Driver review or admission has been obtained. This is an author-side portable scientific handoff, not canonical task promotion; no credentials or sharing permissions changed.
