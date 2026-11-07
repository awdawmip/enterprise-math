# Stage370-B — exact two-sided vertical-coordinate strip exclusion at fixed two-source budget

2026-11-02 · Research2 **portable author-side theorem**, not native Result/Review/admission.

**Mother question.** Determine (or refute) unrestricted four-parameter global cost optimality in the frozen original 16-label, four-audit-port Bernoulli/BRC two-source auxiliary model. This stage excludes two new *nonlocal, positive-area* candidate regions; it does not assert global optimality.

**Scientific provenance and freeze.** Carry forward GLOBAL_KNOWLEDGE_V1 scientific input `main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math scientific input `main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, project P000 V5 original source locator `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488` as reported by Stage369-B. This paper uses the unchanged **external auxiliary model** defined there; no native X6/Cell semantics are inferred. Current operational rules were separately read from GLOBAL_KNOWLEDGE_V1 `main@7dc7476f70d300b0e36b37260f0c7a9d446c2a82` and Enterprise Math `main@55477da6580c35f18c2c48600fee5b76a1b2bc25`. Parent verified scientific frontier: Stage369-B, commit `c93f99a4b0fb88c0989979636a4e79688046a23e` and exact 1304-leaf cost-exclusion certificate.

## Definitions and precise statement

For `k=0,1,2,3`, define

\[
 B_k(z)=z^k(1-z)^{3-k},\quad w=(1,3,3,1),\quad m=(61,21,9,9),
\]
\[
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\qquad
 b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|,
\]
\[
 D_3(a,z)=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,
\]
\[
 c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

The four `D_3` terms remain **independent audit ports** and all 16 `(port,k)` comparison labels are retained. Let `q_star` be the root `r_0=r_1=0` isolated in the rational intervals in Stage369-B, `beta_star=b(q_star)`, and let `P,Q in [0,1]^2` be feasible when

\[
 b(P)+b(Q)\le 2\beta_*+\frac{11}{5000}.
\]

The objective is `T(P,Q)=33/1024+c(P)+c(Q)`.

**Theorem (Stage370-B, universal over real inputs).** Every globally cost-minimizing feasible pair satisfies

\[
 \boxed{\frac{27}{50}<y_P,y_Q<\frac{59}{100}.}
\]

Indeed, let the exact feasible rational reference be

\[
 P_0=(231138/10^6,555681/10^6),\qquad
 Q_0=(237807/10^6,575694/10^6).
\]

For **every** feasible real pair `P,Q`, if either source's `y<=27/50`, then

\[
 \boxed{T(P,Q)-T(P_0,Q_0)>\frac{17}{250000}=0.000068.}
\]

If either source's `y>=59/100`, then

\[
 \boxed{T(P,Q)-T(P_0,Q_0)>\frac{87}{250000}=0.000348.}
\]

Boundary points at both values are excluded, so the final source bounds are strict. Combined with Stage369-B, every global minimizer is contained in the sharper open rectangle

\[
 \boxed{\bigl(577/2500,239/1000\bigr]\times\bigl(27/50,59/100\bigr)}
\]

for each source independently. The preceding `x` bound is a re-use of Stage369-B; **this stage's new theorem is the strict two-sided `y` exclusion**, not an unconditional global optimizer identification.

## Proof by exact interval certificates

Stage368-B gives the entire feasible set inside `R x R`, with

\[
 R=[219/1000,239/1000]\times[51/100,16/25].
\]

Set `lambda=6/5`, `L=c+lambda b`, and the two closed rational strips

\[
 R_{\rm lo}=[219/1000,239/1000]\times[51/100,27/50],
\]
\[
 R_{\rm hi}=[219/1000,239/1000]\times[59/100,16/25].
\]

The accompanying exact program independently verifies the three **whole-real-box** strict inequalities

\[
 \begin{split}
 L(x,y)&>\frac{373}{10000}&&\forall(x,y)\in R,\\
 L(x,y)&>\frac{3767}{100000}&&\forall(x,y)\in R_{\rm lo},\\
 L(x,y)&>\frac{3795}{100000}&&\forall(x,y)\in R_{\rm hi}.
 \end{split}
\]

**Bound semantics.** For each rational interval `[a,z] subset [0,1]`, the only possible interior stationary point of `B_k` is `k/3`, so evaluating its endpoint and interior-critical-point values gives rigorous rational min/max bounds. For any constant `v` and interval `[l,u]`, `min_{t in [l,u]}|v-t|` is either zero (when `v in [l,u]`) or the smaller endpoint distance. Interval arithmetic bounds each residual `r_k`, each of the 16 separately labelled port discrepancies, hence `b`, `c`, and `L`; the lower bound `L_lower(J)` is valid for **every real point in** the box `J`. All operations are Python `Fraction` (exact integer numerator/denominator), with no floating-point rounding or sampling. The recursive dyadic cover divides the entire closed input rectangle, including all edges; overlap along split boundaries is harmless. A leaf is accepted only if `L_lower(J)>target`, strictly. Exhaustive leaf closure therefore implies the claimed universal inequalities.

The executed checker reports:

| box | exact target | splits | closed leaves | max depth | unresolved |
|---|---:|---:|---:|---:|---:|
| `R` | `373/10000` | 1190 | 1191 | 16 | 0 |
| `R_lo` | `3767/100000` | 1661 | 1662 | 17 | 0 |
| `R_hi` | `3795/100000` | 94 | 95 | 15 | 0 |

The two new certificates comprise 1757 leaves. Their deterministic CSV is 257043 bytes and SHA256 `b21fe204b5baa2485dfb08d529cd9a003f2491caf83d2e27012cb83b8dab58a0`. The checker additionally **regenerates** the original Stage369-B `R` lower-bound cover, so its use here does not rely on a merely quoted positive-bound claim. The CSV is locally preserved and may be regenerated from the published checker by `python REPRO_STAGE370B.py --emit CERTIFICATE_STAGE370B_Y_STRIPS.csv`.

**Reference feasibility and budget ceiling.** The same checker independently re-establishes the rational root bracket for `r_0=r_1=0`, signs of `r_2` and `r_3`, and bounds `beta_star`. In particular,

\[
 b(P_0)+b(Q_0)<2\beta_*+11/5000<61/6250.
\]

It verifies exactly

\[
 c(P_0)+c(Q_0)=\frac{16174439790495832521}{256000000000000000000}<\frac{6319}{100000}.
\]

Now suppose `P in R_lo`, `Q in R` and `P,Q` feasible. Directly,

\[
 \begin{aligned}
 c(P)+c(Q)&=L(P)+L(Q)-\frac65\bigl(b(P)+b(Q)\bigr)\\
 &>\frac{3767}{100000}+\frac{373}{10000}-\frac65\frac{61}{6250}\\
 &=\frac{31629}{500000}=0.063258.
 \end{aligned}
\]

Subtract `c(P_0)+c(Q_0)<6319/100000=0.06319` and cancel the constant `33/1024` in `T`: the gap is strictly greater than `17/250000`. If `P in R_hi`, replace `3767/100000` by `3795/100000`; one obtains `>87/250000`. The roles of `P` and `Q` are symmetric. Stage368-B covers any feasible pair in `R x R`, so there is no missed feasible case outside `R`. Compactness of the full feasible set ensures a global minimizer exists, and the explicit rational feasible reference excludes both strips from any global minimizer. **QED.**

## Verification scope and limits

`REPRO_STAGE370B.py` was executed twice, once with `--emit` (writing the exact CSV) and once without; the two stdout files were compared byte-for-byte and matched. It verifies the finite rational proof certificate, not an exhaustive four-dimensional global optimum and not a Lean/formal-kernel derivation. The certificate does not establish the exact optimizer inside the remaining rectangle. Author-side evidence is `PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED`; it has not passed independent mathematical review nor a native Source Result/Driver admission.

No BRC-Shor native rotation arithmetic is being simulated here: `B_k` is a Bernoulli polynomial in a **separate external auxiliary observer**, preserved with provenance and audit channels. A faithful theorem transport to P000 native X6, independent time, three-dimensional slice, triadic closure, and Cell-address relations still requires a typed, observer-preserving map.

## Next discriminating work

Stage371-B: on the now much smaller per-source rectangle `x>0.2308`, `0.54<y<0.59`, combine the exact two-source budget with joint 4D interval cost bounds to certify further nonlocal exclusion **or** locate an exact rational feasible competitor against the post-audit-cusp candidate with algebraic enclosure. If an interval subdivision remains unclosed, report the actual boxes and denominator arithmetic rather than infer global optimality. Prefer reusable existing BRC/provenance-aware interval operators over a new software subsystem.
