# A3 residual-H orbit comparison versus genuine quotient descent — Driver mathematical addendum (2026-11-13)

**Scope and provenance.** This is an additional RESEARCH_DRIVER mathematical check of frozen `RR-9FF7F84F01C577774649` (publication `TP2-D2D715EB36415B0CA0C5`, original researcher `EM-A3SCR-7A41D2`). It builds on the separately saved 2026-11-13 alphabet/faithful-shell audit. It does not alter the frozen Result, its author's work, PR #1491, any CLAIM, or a native review record. Original science: `research_artifacts/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_7A41D2_20260917/result.md` at `945c81cc1f8dc4ac828cb5f2b330e1cd2b6966f1`.

## 1. Two distinct meanings of "modulo global H"

Let `Y=B_n` be the finite A3 carrier, `X=A^Y` with a **nontrivial** finite alphabet `|A|>=2`, and `H={e,h}` where `h=(12)` acts on `Y` by the faithful sign-twisted permutation `R_h=-P_h`. A carrier permutation `P` acts by push-forward on labeled states, written `P_* f`. Let `pi:X -> X/H` be the orbit projection.

One may always compare `pi L_*:X -> X/H` with `pi U_*:X -> X/H`, as in the frozen result's universal orbit-comparison predicate. This comparison **does not require** either operator to act on `X/H`. In contrast, the notation `[f] -> [P_* f]` defines a genuine quotient operator `X/H -> X/H` only if `f~_H f' => P_*f~_H P_*f'`.

**Lemma (order-two quotient-descent criterion).** For a nontrivial involution `h` acting on a finite carrier `Y` and `|A|>=2`, a carrier bijection `P` induces a map `X/H -> X/H` **iff** `P h P^{-1}=h`. Equivalently, `P` centralizes `h`.

*Proof.* Sufficiency follows from `P_*h_*=h_*P_*`. For necessity, take two labels and identify their indicator states with subsets `S subseteq Y`. Set `k=P h P^{-1}`. Well-definedness forces `k(S) in {S,h(S)}` for every subset `S`. On singletons, `k(x) in {x,h(x)}`, so `k` preserves each one- or two-point `h`-orbit. It is identity or swap on each two-point orbit. If its choices differed between two two-point orbits, a subset choosing one point from each would be carried to neither itself nor its global `h`-translate. Thus all two-point orbits have the same choice. `k` fixes one-point orbits and is conjugate to the nonidentity `h`, so `k` cannot be identity and must equal `h`. (The argument also covers a single two-point orbit.) QED.

## 2. Exact condition for the A3 partial radial move

For `1<=d<=n`, let `D_{n,d}(g)` act as `R_g=sgn(g)P_g` on shells `S_r` with `r>=n-d+1` and as identity on lower shells. The `S_4` action on **every** `S_r`, `r>=1`, is faithful: the scaled root vectors `r(e_i-e_j)` in `S_r` span the A3 hyperplane, on which the signed permutation representation is faithful.

Consequently
\[
D_{n,d}(g)\text{ induces an operator on }A^{B_n}/H
\quad\Longleftrightarrow\quad g(12)g^{-1}=(12).
\]
Indeed, conjugating the global `R_h` by `D_{n,d}(g)` gives `R_{ghg^{-1}}` on active shells and `R_h` on inactive shells. At least one active nonzero shell exists, and its faithfulness makes equality to global `R_h` equivalent to `ghg^{-1}=h`. The centralizer in `S_4` is `C_{S_4}((12))={e,(12),(34),(12)(34)}`.

In particular, the frozen counterexample aligner `g=(23)` does **not** define a map on the global residual-`H` state quotient at scales where its radial partial action is used. The comparison of the two output orbits for each *specified input state* remains meaningful, as does the frozen exact carrier defect `K=L U^{-1}`; it must not be silently upgraded to a commuting square of intrinsically defined quotient-state morphisms.

## 3. A fully explicit binary-label witness

Take `n=2,d=1,g=(23)`, with `P=D_{2,1}(g)` (so `P` acts on `S_2` and fixes `S_1`). Let
\[
x=(1,0,-1,0)\in S_1,\qquad y=(2,-2,0,0)\in S_2,\qquad T=\{x,y\}.
\]
For the sign-twisted action,
\[
h x=(0,-1,1,0),\quad h y=y,\quad g y=(-2,0,2,0),\quad h(gy)=(0,2,-2,0).
\]
The two input binary indicator states for `T` and `hT` represent the **same** element of `X/H`. But
\[
PT=\{(1,0,-1,0),(-2,0,2,0)\},\quad
P(hT)=\{(0,-1,1,0),(-2,0,2,0)\},
\]
while
\[
h(PT)=\{(0,-1,1,0),(0,2,-2,0)\}.
\]
Thus `P(hT)` is neither `PT` nor `h(PT)`: quotient descent fails on explicit equivalent inputs. These coordinates have been independently checked by exact integer permutation arithmetic.

## 4. Impact on the pending A3 review

- **Preserved at their original scope:** the shellwise `K` formula, support-transition versus overlap phase split, the `n=2,d=2,g_- = g_+=(23)` raw carrier collision, and the old frame-only invariant's insufficiency.
- **Clarify the mathematical type of Section 5's claim:** `forall f in X, pi(L_*f)=pi(U_*f)` is an output-orbit comparison of two maps `X -> X/H`; a square with arrows defined **on** `X/H` additionally requires each arrow to satisfy the centralizer/normalizer test above.
- **Review disposition remains open:** original researcher and Result are unchanged. A formal Native Review must consider this distinction along with the separately verified `|A|>=2` and shell-faithfulness hypotheses. No Task or parent Objective closure follows from this note.

No `sorry`, `admit`, new axiom, or unverified universal numerical extrapolation is used.


## 5. Exact criterion for a genuine adjacent-scale quotient square

The restriction $\rho_{n+1,n}$ is $H$-equivariant and hence always defines an arrow on quotient states. A **genuine square whose upper and lower partial moves are each defined on quotient states** requires both $g_+\in C_{S_4}(h)$ and $g_-\in C_{S_4}(h)$, in addition to the frozen universal comparison of the two output orbits.

Combining this exact descent requirement with the separately proved carrier-shell/global-$H$ witness classification gives the following complete criterion for $\lvert A\rvert\ge2$, $1\le d\le n$, $q=n-d+1$:

| Adjacent-scale regime | Genuine square on $X_{n+1}/H$ and $X_n/H$ commutes iff |
| --- | --- |
| $n=1,d=1$ | $g_-\in H$ **and** $g_+\in C_{S_4}(h)$ |
| $q\ge2,d=1$ | $g_-=e$ **and** $g_+\in C_{S_4}(h)$ |
| $q\ge2,d\ge2$ | $g_-=g_+=e$ |
| $q=1,n\ge2$ | $g_-\in H$ **and** $g_+=e$ |

*Proof.* The orbit-comparison iff cases are obtained by inspecting the three shell regions of $K=L U^{-1}$ and requiring one common global $H$ witness (the previous independent audit supplies the binary-label quantifier bridge). The upper partial move at scale $n+1$ has a nonempty active shell even when its action is discarded by restriction, so Section 2 requires $g_+\in C_{S_4}(h)$; the lower similarly requires $g_-\in C_{S_4}(h)$. Intersect these conditions with the four universal orbit-comparison regimes. In the last two cases, identities and $H$ elements already centralize $h$; only the $d=1$ regimes acquire a new upper-aligner condition. QED.

In particular, at $n=2,d=1,g_-=e,g_+=(23)$, the two *raw* composite paths from $X_3$ to $X_2$ agree exactly after restriction, but the upper $D_{3,1}((23))$ is not a map on $X_3/H$. Thus equality of output orbits after restriction is strictly weaker than the existence of a quotient-state naturality square. This refinement affects only claims of genuine quotient morphisms, not the frozen carrier or output-orbit formulas.
