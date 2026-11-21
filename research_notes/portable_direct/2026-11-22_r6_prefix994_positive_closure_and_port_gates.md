# PREFIX-994 — Nonempty BRC closure and history-sensitive port gates

Date: 2026-11-22 (+08). Status: **AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED**.
Scope: independent portable continuation, no new formal CLAIM/Result/Review.
Frozen P000 V5 science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`.
Immediate prior frontier: PREFIX-993 at `45b71416907502e0f12a29b3d2ed30705fe45fc1`.
BRC typed foundation: WBRC-T30/T31 Schur positive rational port module, WBRC-T36/T37 full exact positive weight histogram.
P000 native frame: the Heartbeat World X6 affine Cell torsor, with six positive primitive axis steps in a fixed chosen chart; internal history ports are typed nonspatial state.

## 1. Question, exact observer and finite interfaces

PREFIX-993 exhibited an explicit Schur kernel with six incoming history ports compressed into two positive-projective classes. Does this compression survive positive serial/recurrent composition? Which state-dependent path-availability rules preserve its **full named-path, endpoint, terminal-port, exact-weight histogram**, not merely a scalar total?

Let `J={0,...,m-1}`, `C` be a nonempty set of r history classes, and `κ:J→C`. For rational `ρ_h>0`, define the `m×r` rectangular class-lift
`R[h,c]=ρ_h 1_{κ(h)=c}`.
Every positive row template `F∈Q_{>0}^{r×m}` defines `W=RF`; hence `W[h,j]=ρ_h F[κ(h),j]`.

The exact positive weight-histogram semiring is `H=N[Q_{>0}^×]`: `[u][v]=[uv]`, `[u]+[v]` records two alternatives with multiplicity. Zero is the empty histogram and unit is `[1]`. A named `n`-step path's mass is its product of `n` port weights; its endpoint, terminal output port, ordered source labels and branch multiplicity remain typed observations. The matrix history formulas below are *port marginals*; whenever endpoint is required, carry the Cell state in the transfer, as in Theorem 994.3. Do not infer signed/phase conservation from positive histograms.

## 2. Theorem 994.1 — closure under nonempty positive serial/recurrent paths

Fix `R` above. The cone
`C_R={RF:F∈Q_{≥0}^{r×m}}`
is closed under matrix addition, positive rational scaling and matrix multiplication. For any `W=RF`,

```text
W^n=R(FR)^(n-1)F                    (n>=1).
```

If `W` is substochastic with `q=max_h sum_j W[h,j]<1`, its convergent nonempty-walk kernel is

```text
W^+ = sum_{n>=1} W^n = R (I_r-FR)^(-1) F.
W^* = (I_m-W)^(-1) = I_m + W^+.
```

Both the nonempty powers and `W^+` have the original fixed `κ,ρ` factorization. The identity contribution `I_m` generally cannot be represented by the same nontrivial history-class quotient.

*Proof.* If `B=RF` and `D=RG`, then `BD=R(FR)G`; addition and scaling are immediate. Induction gives the power formula. The nonzero eigenvalues of `RF` and `FR` coincide; the stated norm bound implies convergence of both Neumann series (or equivalently use the absolutely convergent factored power sum). The empty walk has source-specific identity `δ_{h,j}`, while every nonempty walk carries the left factor `R`. If `r<m` and `κ` is onto, `rank(R)<=r<m`, so `I_m` is outside `C_R`. QED.

**Full exact histogram strengthening.** Replace every positive scalar `a` by the monomial `[a]`; form rectangular matrices `R_H,F_H` entrywise (zero remains zero). For `H=R_H F_H` in the histogram semiring,

```text
H^n = R_H (F_H R_H)^(n-1) F_H                 (n>=1)
sum_{n>=1} z^n H^n = z R_H (I-zF_H R_H)^(-1) F_H
```

holds coefficientwise in `H[[z]]`. These are formal power series: no real analytic convergence of a histogram is required. Associativity/distributivity proves the result. Thus the entire ordered-length distribution of exact positive weights and multiplicities is retained, with incoming/terminal port labels available at both boundaries. It is not a proof that dropping internal named paths preserves every later provenance-sensitive observer: retain those labels where required.

## 3. Theorem 994.2 — maximal fixed-class Boolean availability gate

Let `A_s(h,j)∈{0,1}` be a state-indexed availability indicator at a retained typed state `s`; assume `F[c,j]>0` for every entry. Define gated outgoing kernel `W_s(h,j)=A_s(h,j)W(h,j)`.

For fixed `s`, the original `κ` and normalization scalars `ρ` still factor `W_s` if and only if

```text
A_s(h,j)=A_s(k,j), whenever κ(h)=κ(k), for every j.
```

*Proof.* For each class c, `W_s(h,j)/ρ_h=A_s(h,j)F[c,j]`. The common class template exists exactly when those quotients are equal across h; strict positivity of F turns equality of quotients into equality of Boolean gates. QED.

For every fixed state s the safe gates form a Boolean subalgebra, the class-homogeneous masks. A next-port-only gate and any state-dependent gate that is class-homogeneous are safe; a gate that distinguishes two histories inside one class yields an immediate named-source support witness.

## 4. Theorem 994.3 — full endpoint and terminal-port histogram with local gates

Consider native positive X6 Cell steps `z→z+e_j` and additional retained typed state s. Assume that both the next retained state `T(s,j)` and availability `a(s,c,j)` depend only on s, the class c=κ(h), and the named port j, rather than on the concrete incoming h inside c. The named port of each step becomes the next history port. Preserve z (or a certified lossless endpoint observer), actual terminal j and each named path's weight.

Then the exact direct history-dependent path histogram is computed by a transfer over just `(s,κ(h))`. Put internal transition weight `[ρ_j F[c,j]]`; for a positive-length path from initial port h ending at terminal port j, apply boundary monomial `[ρ_h/ρ_j]` to the internal product and retain the final j. For length zero retain the actual original h in the identity boundary.

*Proof.* For any admissible named word `j_1...j_n` with `j_0=h`, internal transfer has weight
`∏_{t=1}^n ρ_{j_t}F[κ(j_{t-1}),j_t]`.
Multiplication by `ρ_h/ρ_{j_n}` produces exactly
`∏_{t=1}^n W[j_{t-1},j_t]`.
By the hypothesis, the legal word set and successor typed states are the same in the direct and class transfer. The map is wordwise, so grouping by endpoint, last port and exact positive weight preserves every coefficient and multiplicity at every finite n. QED.

A sufficient, observer-specific extension allows successor states to agree only after an explicitly certified quotient. Here we keep the native six-component endpoint, avoiding an unproved spatial collapse.

## 5. Exact six-port witness and the zero-length obstruction

Reuse the *unchanged* PREFIX-992/993 Schur module:
```text
κ=(0,0,1,1,0,1), ρ=(1,2,1,2,3,3);
Xnum=[[1,2,1,3,2,4],[2,1,3,1,4,2]];
W[h,j]=ρ_h Xnum[κ(h),j]/5000.
R[h,c]=ρ_h 1_{κ(h)=c}; F=Xnum/5000.
```
Its maximum row sum is `39/5000<1`, and
```text
FR=[[11/5000,19/5000],[2/625,11/5000]].
(I-FR)^(-1)=[[24945000,95000],[80000,24945000]]/24889817.
first row of W^+=[5027,9997,5046,14986,10054,19994]/24889817.
```
Exact rational Gaussian elimination gives the same six-by-six inverse:
`(I_6-W)^(-1)=I_6+R(I_2-FR)^(-1)F`.

The positive-length closure `W^+` has **two** projective history classes `{0,1,4},{2,3,5}`. The full star `W^*=I+W^+` has **six** pairwise nonproportional rows. Indeed each row sum of `W^+` is at most `(39/5000)/(1-39/5000)=39/4961<1`. Hence in `I+W^+` every row has its own unique strictly largest diagonal entry, precluding positive proportionality with any other row.

**Safe state-dependent gate, exact path experiment.** Let the auxiliary availability rule at positive native X6 displacement z be `a(z,j)=1_{z_j<2}`, so a given positive axis may be used at most twice. This is an explicit toy capacity constraint on the native Cell steps, **not** a claim about the project's full Link/Port occupancy law. It is independent of incoming h. The exact checker compares the full `(z,terminal-port,positive-rational-weight)→multiplicity` distributions of direct and class-transfer algorithms, for **all six initial h** at **every n=0,...,7**, with no mismatches. At n=7 each initial h has precisely **128,520** legal ordered named paths. The certificate retains sample exact masses and number of distinct histogram keys.

**Unsafe gate, exact counterexample.** Add the auxiliary immediate no-repeat condition `a(h,j)=1_{j≠h}`. Every history row now has a different forbidden named port; hence its weighted support differs from all others and the six history classes are necessary for the full named first-step observer. In particular, old same-class histories h=0 and h=1 have gated port-0 weights `0` and `2/5000`, respectively, although originally `W[0,0]=1/5000`. The two-class quotient fails at n=1. This counterexample separates history-dependent admissibility loss from the positive-weight row factorization of PREFIX-992.

**Exact additional check.** For n=1,...,6 the checker evaluates histogram-semiring matrix powers directly and via the 2-state rectangular factorization. All 6×6 entry histograms coincide coefficientwise; each initial port has `6^n` unrestricted named paths. Rational arithmetic uses Python `fractions.Fraction` and exact integer `Counter`, not floating point.

## 6. Scientific boundary and next action

Theorems 994.1–994.3 are analytic statements under explicitly typed positivity and gating assumptions; the six-port calculation checks the frozen example. This extends PREFIX-993 from a fixed feedback context to a compositional nonempty-path closure and identifies the exact extra condition required when availability itself depends on retained state/history. The Link/Port restrictions in the examples are synthetic stress tests; full native Link/Port incidence and occupancy must be read and typed before claiming a corresponding native invariant. Ordered provenance and joint relations are retained or must be separately certified against any further quotient.

Next: identify the actual source-defined X6 Link/Port incidence and occupancy transition operator (rather than a toy gate), project its allowed outgoing named edges onto the old history classes, and either prove class-homogeneous availability with a future-operation certificate or exhibit a minimal native counterexample. The historical mother objective `B_fix,odd(32)∈{19,20}` is still open.

Evidence: `PREFIX994_R6_PORT_GATE_CLOSURE_CHECK.py`, `PREFIX994_R6_EXACT_RESULTS.json`. Scientific inputs retain the frozen P000 pin; all checks are author-executed, independent mathematical review remains pending.
