# R5: two-parameter B-bypass — simultaneous H/J gap cancellation with a robust third four-observer separator

**2026-11-01 (Asia/Shanghai)** · Author-side proof and exact-rational certificate · **UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**.

## 1. Provenance, aim, and exact mathematical scope

The four-observer mother objective asks whether a finite strictly-positive two-law stopping model with genuinely shared `(time, likelihood ratio)` decision keys can satisfy `conv(FULL)=conv(LR)` while `O(FULL) != O(LR)` for **actual real behavioral policies**. This note studies the explicit auxiliary `I/J/K/L` model and classifies **two specified signed directions** while producing a **third exact separation certificate** over a nontrivial two-parameter rectangle. The mother objective remains open.

- **Frozen scientific inputs inherited from R5:** GLOBAL_KNOWLEDGE_V1 `main@a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `main@86149263e38c22292c9def1e0f69092efa1be77e`; immutable prior scientific frontier `34312c8a8ec231590d48ac909b9ce73594f4b904`, `research_notes/brc_r5_bypass_L_one_parameter_20261101_t2036/RESEARCH.md` and `VERIFY.py`.
- **Current normative context checked separately:** Global Knowledge `main@d63e70daeafb077bdd91e2cc837104b97e43c689`, entry `00_BOOTSTRAP.md` and `OPERATING_MANUAL.md`; Enterprise Math `main@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14`, `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `research_priorities/research_method.json`, P000, joint-relation preservation, and native-world/time contract. P000 and the protected worldview are unchanged. The frozen and current project P000/joint blobs agree at this task's read.
- **BRC actual reuse:** Source identity A1/A2/B/C and every nonnegative rational P/Q terminal branch mass remain separate until observation. The projection is the explicitly declared four-coordinate `O`; negative coefficients occur **only in signed observer functionals**. The observer projection is not asserted lossless for source identity or future operations. The proof concerns only this finite stopping-horizon observable and its policy class.

## 2. Positive-law model, source-preserving observer, and new parameter

Source initial masses under P/Q are respectively `A1=A2=(1/8,1/8)`, `B=(1/4,1/8)`, `C=(1/2,5/8)`; each law sums to one. The four observables are

`O=(eP,eQ,TP,TQ)=(Pr_P(final P),Pr_Q(final Q),E_P(stop time),E_Q(stop time))`.

All behavior bits in `[0,1]` are shared between the laws. The full-history strategy has 11 parameters `(p1,p2,q1,q2,qB,r,k1,k2,l1,l2,lB)`. The seedless LR policy ties `p1=p2=p`, `q1=q2=qB=q`, `k1=k2=k`, `l1=l2=lB=l`, with `r` free, yielding five parameters. Terminal answers P/Q and stopping times are labels rather than untyped spatial axes.

The A/C pathways and genuine shared decision keys `I=(1,1)`, `J=(2,2)`, `K=(3,8/5)`, `L=(4,12/5)` are exactly those in the pinned predecessor. A1/A2 go through I, J and K; B goes directly to J and can bypass into L; C has an independent r decision. At J on B, behavior qB stops P at t=2; continuing B undergoes nature's **strictly positive** split

- high: conditional `(P,Q)=(6η/5,η)` enters L, where lB stops P at t=4 or answers Q at t=5;
- low: conditional `(P,Q)=(1−6η/5,1−η)` terminates at t=4. **New** nature split answers P with common conditional probability `1−z` and Q with `z` under both laws.

The parameter domain is `0<η<5/6`, `0<z<1`. Every natural edge has strictly positive P and Q probability. The B-high likelihood ratio is precisely `2(6η/5)/η=12/5`, so the existing shared key L remains genuine. No behavioral key repeats on any trajectory. The full terminal-flow algorithm is explicitly implemented in `VERIFY.py`; it checks both-law normalization exactly.

The observation map is multi-affine separately in each behavioral variable. For a fixed deterministic policy it is bilinear (`a+bη+cz+dηz`) in nature parameters `(η,z)`, since a trajectory contains at most one occurrence of each nature parameter. Consequently each signed support extremum over the **entire real behavioral cube** is attained at a deterministic policy.

## 3. Exact support-gap phase diagrams for two independent directions

Let

`H(O)=5eP+5TP−8TQ`, `C(O)=3eP+TP`, `J(O)=−C(O)`.

Write

`m(η)=5/4−3η/2>0`, `n(η)=3/4−9η/10>0`,

`D(η,z)=1/2−η−m(η)z`, `E(η,z)=1/2−3η/5−n(η)z`.

The preceding one-parameter model corresponds to the **boundary** `z=0`. The only observer changes in that model's flow formula are B-low terminal contributions `−m(η)z(1−qB)` to H and `−n(η)z(1−qB)` to C. Explicitly the H B term becomes

`−qB/4+(1−qB)[1/4−η+η*lB−m(η)z]`

and the C B term becomes

`(5/4)qB+(1−qB)[7/4−(3η/5)(1−lB)−n(η)z]`.

The two A source terms remain, independently for `(p,q,k,l)`:

`H_A=13p/16−pq/8+q/8+[(-3/8+l/4)(1−p)(1−q)(1−k)]/8`,

`C_A=p/2+(1−p){1/8+5q/16+(1−q)[3/16+3k/40+(1−k)(19/320+3l/160)]}`.

The H base is `−33/8+(5/2)r` and the C source C term is `r/2+3(1−r)`. These formulas are exact P/Q positive-flow expansions.

**Theorem 1 (complete phase diagrams; all real behavioral policies).** For all `0<η<5/6` and `0<z<1`,

```
min_FULL H = −143/32 + min(0,D),
min_LR   H = −33/8   + min(0,D−11/32),
G_H := min_LR H − min_FULL H =
       0              when D≤0,
       D              when 0≤D≤11/32,
       11/32          when D≥11/32.

min_FULL C = 399/160 + min(0,E),
min_LR   C = 21/8    + min(0,E−21/160),
G_J := max_FULL J − max_LR J = min_LR C−min_FULL C =
       0              when E≤0,
       E              when 0≤E≤21/160,
       21/160         when E≥21/160.
```

**Proof.** Each A source minimizes H at `p=q=k=l=0` with value `−3/64`; for C it minimizes at the same four zeroes with value `119/320`. For H, the A p coefficient is positive, k and l can only increase the objective, and the q comparison at their minimizing values is positive. For C, l is nondecreasing; with l=0 the k coefficient is positive, q is nondecreasing, and the p=1 branch cost 1/2 exceeds the p=0 minimum. The independent C source selects r=0 for H and r=1 for C. In FULL, B selects between qB=1 and qB=lB=0; the respective cost differences are exactly D and E. This proves the two FULL minima. In LR the same monotonicity selects p=k=l=r=0 for H and p=k=l=0,r=1 for C, leaving only a shared affine q decision. Its two endpoint values give the displayed LR minima. Subtracting and sorting at the exact thresholds proves both phase diagrams. These minimizations are valid over the entire real policy cubes by the multi-affine extreme-point property. ∎

**Corollary 1 (nonempty two-gap cancellation region).** Both old signed support gaps vanish exactly when `D≤0` and `E≤0`. A nonempty **open**, strictly-positive-branch parameter region satisfies `D<0,E<0`, e.g. all parameters in the closed test rectangle

`R=[1/2,3/5]×[3/4,9/10] ⊂ (0,5/6)×(0,1)`.

Bilinearity and four exact corner values show throughout R:

`D≤−29/80<0` and `E≤−7/400<0`.

Thus `G_H=G_J=0` for every real policy and every parameter in R. The original two independent supporting directions no longer separate the hulls.

## 4. New third signed separator throughout the two-gap-cancellation rectangle

Take the integer four-observer functional

`N(O)=25eP−160eQ−95TP+242TQ`.

Fix one legal deterministic FULL policy, listed in the order of Section 2:

`Wbits=(0,0,1,1,0,0,1,1,1,1,1)`.

**Theorem 2 (exact uniform third-direction obstruction).** For **every** `(η,z)∈R` and **every real LR behavioral strategy**,

`N(O_FULL(Wbits;η,z)) − N(O_LR(strategy;η,z)) ≥ 7/4 > 0`.

Hence `conv(FULL) ≠ conv(LR)` over the entire two-dimensional rectangle R, despite the exact simultaneous vanishing of `G_H` and `G_J` there. The fixed FULL witness has

`dist_∞(O_FULL(Wbits;η,z), conv O_LR) ≥ (7/4)/(25+160+95+242)=7/2088`.

**Exact finite certificate and proof.** For the 32 deterministic LR policies, evaluate the four-parameter-corner differences `N(W)−N(LR_v)` using rational P/Q terminal masses. The minima across those 32 policies, in order `(η,z)=(1/2,3/4),(1/2,9/10),(3/5,3/4),(3/5,9/10)`, are

`(29/8, 7/4, 29/8, 29/8)`.

For a **fixed** LR vertex v, the difference is bilinear in η,z. Bilinear interpolation on R expresses its interior value as a convex combination of the four corner values, each at least 7/4. Therefore the difference is at least 7/4 at every point of R for each of the 32 vertices. Since the LR observation under any real behavior is multi-affine in its five local decisions, its N value is a convex combination of the 32 deterministic N values. The same inequality follows for all real LR behavior. Dividing a separating functional's margin by its ℓ1 coefficient norm yields the displayed ℓ∞ distance bound. ∎

At the strictly positive interior point `η=1/2,z=3/4`, the explicit witness is

`O_FULL(Wbits)=(4/5,15/64,3,23/8)`,

`N(W)=1573/4`, `max_LR N=3117/8`, `gap=29/8`,

and hence `dist_∞(W,conv LR)≥1/144`. This is an exact concrete model disproving the inference that simultaneous cancellation of two obstruction directions establishes complete four-observer hull equality.

## 5. Full-dimensional LR observation and independent verification scope

In the LR slice `k=l=1,r=0`, take the differences of the four observer vectors associated with p, q, pq and r (the r row is obtained by toggling r at `p=q=0`). The exact 4×4 determinant is

`det=[59+(59η−46)z]/10240`.

Only the q row of this determinant depends on the B-low nature split; the other rows come from A/C and are constant. Thus the determinant is bilinear in η,z, and the four exact corner identities computed by the verifier establish the formula for all parameters by interpolation. Throughout `0<η<5/6, 0<z<1`, its numerator is greater than 13, so **the LR affine hull has dimension four everywhere in the entire strict-positive domain**.

`VERIFY.py` is a standalone Python-standard-library `fractions.Fraction` certificate. It executed and checked **8,320** exact deterministic-policy flow and H/C identity calculations (`4×(2048 FULL+32 LR)`), both-law terminal normalization, exact minima, the two-dimensional D/E rectangle bounds, four N-support gaps, the rank determinant and the explicit witness. No floating-point numerical result is used in these mathematical certificates. The all-real statements follow from the declared multi-affine/bilinear structural degree bounds, complete vertex evaluation and exact interpolation, together with the analytic minimization in Theorem 1.

**Research boundary and native authority.** This is a finite classical two-law stopping-process result with explicit source provenance and positive rational nature kernels, not a native X6 dynamics theorem. The protected worldview and P000 remain untouched. During this run the native gateway reported `research_authority_granted=false`; a bounded Owner query returned `CONTROL_QUOTA`, and a Researcher session attempt returned `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`). GitHub owner-level author-side preservation is separate from native CLAIM/Result/Driver review. No fresh authenticated Owner, formal Result or independent scientific acceptance is asserted.

## 6. Next discriminating research unit

The two-gap cancellation rectangle proves that **direction-by-direction repair can succeed without convex-hull repair**. Continue with either (a) a third independent source-sensitive bypass branch capable of changing the N support while preserving the exact old H and J cancellation region, or (b) a complete symbolic signed-convex-hull condition for a low-dimensional model family. For a candidate, enumerate every FULL deterministic four-observer vertex and give either exact LR mixtures with at most five vertices or one exact separating Farkas direction. If the complete hulls coincide, test **actual real** LR observer-image membership semialgebraically. Keep source flows and terminal-law normalization exact at each modification.
