# P000 Philosophy-First Q9 — Weakest Nonlocal Probe / Joint Separation Return

Task: `RS-P000-PHILOSOPHY-FIRST-NONLOCAL-PROBE-JOINT-SEPARATION`  
Publication: `TP2-35D8011A9CE8FF9207EC`  
Researcher: `EM-PHQ9-91C85B`  
Claim: `chatgpt-phq9-20260830-1328-6908e6`  
Execution branch: `research/p000-phil-q9-nonlocal-probe-joint-separation-em-phq9-91c85b`  
Hard target: `P000_NONLOCAL_PROBE_JOINT_SEPARATION_OR_NO_GO_CLASSIFIED`

## Terminal verdict

`SUCCESS / TESTED_PARETO_MINIMAL_NATIVE_JOINT_PROBE_FOUND / FULL_U_2REG_PERIOD_COMPLETION_CLASSIFIED`

At the frozen Q2/Q6 witness scope, the smallest successful candidate among the tested low-language probes is a **single native path-return scalar**:

\[
R_{\min}(X)=
\min\{\ell\ge 3:
\text{there exists a simple nonbacktracking native-adjacency loop of length }\ell\}.
\]

Only after fixing this native path semantics may one call `R_min` the graph-theoretic **girth**.

It does two things simultaneously:

1. it separates the entire accepted Q2 collision family
   \[
   C_{2m}\quad\text{vs}\quad C_m\sqcup C_m
   \]
   because their minimum native return lengths are `2m` and `m`; and
2. it removes the accepted Q6 minimal pure virtual profile `(t,p)=(0,3)` already at structural compatibility level: `t=0` forces the shortest native cycle to have length at least four, while a support of only three Cells cannot contain such a loop.

This does **not** make the observation map globally complete. The first exact remaining collision for `(t,p,R_min)` occurs at eleven Cells:

\[
C_3\sqcup C_8
\quad\text{vs}\quad
C_3\sqcup C_4\sqcup C_4,
\]

both having `(t,p,R_min)=(3,8,3)`.

A stronger probe — the rootwise first nonbacktracking return-period histogram — is exactly complete on the declared `U_2REG` class. If

\[
q_k(X)=\#\{x:\rho_X(x)=k\},
\]

then

\[
X\text{ is represented by }(q_k)_{k\ge3}
\iff
q_k\equiv 0\pmod{k}\ \text{for every }k,
\]

and the inverse is explicit: `q_k/k` copies of `C_k`. Thus the same path mechanism supplies both a reconstruction certificate and a representability certificate without exposing opaque Cell identities.

The result is deliberately **not** a claim that `R_min` is universally weakest among all conceivable P000 probes. It is the Pareto-minimal joint-success candidate in the declared tested family below, and the exact stronger completion is also classified.

## 1. Frozen accepted scope

This return uses only the scopes accepted by the Q1-Q8 Driver review.

### Q2 witness class `U_2REG`

A state in the declared witness class consists of:

- a finite set of opaque native Cells;
- a finite simple native-adjacency graph on those Cells;
- degree exactly two at every Cell;
- the uniform six-axis local fiber, accepted `SLICE` carrier-star readouts, accepted carrier rotation readout, and one identical opaque PF-10 token at every Cell.

Consequently every state is, at this witness layer only, an unordered disjoint union

\[
X=\bigsqcup_{k\ge3} h_k C_k,
\qquad h_k\in\mathbb N.
\]

This cycle decomposition is a theorem about finite simple 2-regular graphs, not a replacement for P000 ontology.

### Q2 restricted observation

At radius one the local count profile is

\[
\operatorname{Obs}_1(X)=(t(X),p(X)),
\]

where

\[
t(X)=3h_3,\qquad
p(X)=\sum_{k\ge4} k h_k.
\]

The accepted Q2 family says that for every fixed finite `r>=1` and every `m>=2r+2`,

\[
X_r=C_{2m},
\qquad
Y_r=C_m\sqcup C_m
\]

have identical selected fixed-radius local profiles but are nonisomorphic.

### Q6 representability boundary

The accepted Q6 image theorem is

\[
(t,p)\text{ representable}
\iff
t\equiv0\pmod 3
\ \text{and}\
(p=0\ \text{or}\ p\ge4).
\]

The minimal support-aware pure virtual profile is

\[
(t,p)=(0,3).
\]

It is assembled from three individually legal radius-one rooted-path symbols, but no three-Cell `U_2REG` state realizes it.

## 2. Allowed equivalence and probe discipline

All native candidates below must satisfy:

1. **Cell-isomorphism invariance.** Relabeling opaque Cells by an adjacency- and decoration-preserving bijection does not change the output.
2. **No identity lookup.** No probe returns a Cell name, address, canonical label, or component-membership list.
3. **Declared-data derivation.** Native probes use only the native adjacency already declared inside `U_2REG`. A transport/holonomy probe is treated separately as an explicitly enriched relational candidate.
4. **Carrier guard.** Carrier `S4`, K4/FCC, and carrier vertices are not promoted to native Cell identity or full native rotation.
5. **Lowest-language rule.** No groupoid/descent language is required merely to define the successful Q9 path-return probes.

## 3. Candidate A — `CONN_BIT`

Define

\[
\operatorname{CONN}(X)=
\begin{cases}
1,&\text{every two native Cells are joined by a native-adjacency path},\\
0,&\text{otherwise}.
\end{cases}
\]

This is a one-bit nonlocal invariant derived from the declared native adjacency.

### Q2 separation

For every accepted Q2 parameter pair,

\[
\operatorname{CONN}(C_{2m})=1,\qquad
\operatorname{CONN}(C_m\sqcup C_m)=0.
\]

So `CONN_BIT` kills the entire known Q2 collision family.

### Q6 representability test

It does not cure the Q6 completion defect. In the Q6-style formal language, the augmented symbol

\[
(t,p,\operatorname{CONN})=(0,3,1)
\]

is still assembled from three pointwise legal path-root observations plus one legal global connectedness value. Yet there is no actual three-Cell simple 2-regular connected state with path-root radius-one observations: the unique three-Cell connected 2-regular graph is `C3`, whose roots are triangles.

Hence the virtual-profile mechanism persists.

### Remaining noninjectivity

Even after adding connectedness,

\[
C_4\sqcup C_6
\quad\text{and}\quad
C_5\sqcup C_5
\]

both have `(t,p,CONN)=(0,10,0)`.

`CONN_BIT` is therefore **separation-only** for the target Q2 family.

## 4. Candidate B — `MIN_NATIVE_RETURN` / girth

Define a native simple nonbacktracking loop to be a Cell sequence

\[
x_0,x_1,\dots,x_{\ell}=x_0
\]

such that:

- consecutive Cells are native-adjacent;
- there is no immediate reversal;
- `x_0,...,x_{\ell-1}` are pairwise distinct.

Define

\[
R_{\min}(X)=
\min\{\ell\ge3:\text{such a loop exists}\}.
\]

Only after this semantics is frozen do we identify it with the classical girth of the declared adjacency graph.

### Q2 separation theorem

For a cycle `C_k`, the shortest native return has length exactly `k`. Therefore

\[
R_{\min}(C_{2m})=2m,
\qquad
R_{\min}(C_m\sqcup C_m)=m.
\]

Thus `R_min` separates the accepted Q2 family for every `r>=1, m>=2r+2`.

### Exact representability image for `(t,p,g)`

Write `g=R_min(X)`.

**Theorem.** A triple `(t,p,g)` is realized by some `U_2REG` state iff one of the following disjoint cases holds.

**Case I: `t>0`.**

\[
g=3,\qquad
t\equiv0\pmod3,\qquad
p=0\text{ or }p\ge4.
\]

**Case II: `t=0`.**

\[
g\ge4,\qquad
p=g\text{ or }p\ge 2g.
\]

#### Proof

If `t>0`, at least one triangle component exists, so the shortest native loop has length three. The remaining conditions are exactly the accepted Q6 image theorem. Conversely, `t/3` copies of `C3`, together with no nontriangle component when `p=0` or one `C_p` when `p>=4`, realize the triple.

If `t=0`, every component has length at least four and at least one component has length exactly `g`. Remove one such `C_g`. The residual mass is either zero or is a sum of cycle lengths each at least `g`; hence it is at least `g`. Therefore `p=g` or `p>=2g`. Conversely, `C_g` realizes `p=g`, while

\[
C_g\sqcup C_{p-g}
\]

realizes every `p>=2g` because `p-g>=g`. ∎

### Q6 virtual-profile elimination

For `(t,p)=(0,3)`, Case II would require `g>=4` while also `p=g` or `p>=2g`; neither can hold. Equivalently, a simple native cycle of length at least four cannot fit inside a support of three Cells.

So the minimal accepted Q6 virtual profile has **no** `R_min` extension at all.

This is the first tested candidate that both:

- splits the accepted Q2 collision family; and
- removes the accepted minimal Q6 virtual profile without returning native identities.

### Exact remaining kernel

`R_min` is not reconstruction-complete. The first collision of `(t,p,R_min)` occurs at `n=11`:

\[
C_3\sqcup C_8
\quad\text{and}\quad
C_3\sqcup C_4\sqcup C_4.
\]

Both map to `(3,8,3)`.

Thus the exact claim is **joint improvement**, not complete tomography.

## 5. Candidate C — `ROOT_RETURN_PERIOD_HIST`

For a native Cell `x` in the declared degree-two class, choose either adjacent Cell and continue without backtracking. Degree two makes the continuation deterministic. The first return to `x` occurs after the length of its cycle component; the two initial directions give the same return time.

Define

\[
\rho_X(x)=\min\{\ell\ge3:
\text{the deterministic nonbacktracking path from }x
\text{ returns to }x\},
\]

and the anonymous histogram

\[
q_k(X)=\#\{x\in Cell(X):\rho_X(x)=k\}.
\]

The probe reports only integer periods and multiplicities. It never reports which Cells form a component.

### Invariance

A Cell isomorphism transports native paths and preserves first-return lengths, so the entire histogram `(q_k)` is invariant.

### Q2 separation

\[
C_{2m}: q_{2m}=2m,
\qquad
C_m\sqcup C_m: q_m=2m.
\]

The outputs differ for every `m>=3`, hence on the full accepted Q2 family.

### Exact representability theorem

**Theorem.** A finite nonnegative sequence `(q_k)_{k>=3}` is realized by a `U_2REG` state iff

\[
q_k\equiv0\pmod{k}
\quad\text{for every }k.
\]

When this holds, the realization is unique up to Cell isomorphism and is

\[
X(q)=
\bigsqcup_{k\ge3}
\frac{q_k}{k}C_k.
\]

#### Proof

Every `C_k` contributes exactly `k` roots of first-return period `k`, proving necessity. Conversely, if every `q_k/k` is a nonnegative integer, the displayed disjoint union realizes exactly the prescribed histogram. Finite simple 2-regular graphs are classified up to isomorphism by their cycle-length multiplicities, proving uniqueness. ∎

The Q6 local counts become

\[
t=q_3,\qquad
p=\sum_{k\ge4}q_k.
\]

The minimal virtual profile `(0,3)` cannot pass the period integrality gate because no positive multiple of any `k>=4` can sum to three.

More strongly, at this declared witness scope the period profile has **no representability gap at all** once the explicit divisibility gate is enforced.

### Reconstruction theorem

The inverse formula `h_k=q_k/k` recovers the full cycle partition. Hence the `ROOT_RETURN_PERIOD_HIST` map has zero isomorphism kernel on `U_2REG`.

This completeness is special to finite simple degree-two graphs. It is not extrapolated to richer P000 Cell classes.

## 6. Candidate D — `HOLONOMY_EXACTNESS` negative control

Q4 supplies a legitimate comparison only after transport data are explicitly declared.

Enrich each native adjacency edge with a `C2` transport and define

\[
\operatorname{HOL\_EXACT}(X)=1
\]

iff every fundamental-cycle transport product is identity.

Take the legal enrichment where every edge transport is identity.

Then for every cycle decomposition,

\[
\operatorname{HOL\_EXACT}(X)=1.
\]

In particular,

\[
\operatorname{HOL\_EXACT}(C_{2m})
=
\operatorname{HOL\_EXACT}(C_m\sqcup C_m)=1.
\]

So this genuinely nonlocal summary does **not** split the Q2 family.

Likewise `(0,3,HOL_EXACT=1)` remains a formally legal Q6-style completion symbol but has no native realization.

This is the required negative certificate: global holonomy can be the right invariant for **frame synchronization** while being the wrong invariant for **underlying Cell gluing topology**. Q4 and Q9 are therefore complementary, not interchangeable.

Because transport is an explicit enrichment rather than a frozen bare-P000 primitive, `HOLONOMY_EXACTNESS` is also rejected as the native minimal Q9 repair.

## 7. Minimality / information audit

The tested candidates have the following exact status.

| Probe | Native at declared `U_2REG` scope? | Q2 family | Q6 `(0,3)` | Global `U_2REG` reconstruction |
|---|---|---|---|---|
| `CONN_BIT` | yes, derived from native adjacency | separates | virtual persists | no |
| `MIN_NATIVE_RETURN` (`girth`) | yes, derived from native paths | separates | eliminated | no |
| `ROOT_RETURN_PERIOD_HIST` | yes, derived from native paths | separates | eliminated; exact divisibility image | yes |
| `HOLONOMY_EXACTNESS` | only after explicit transport enrichment | fails under trivial transports | virtual persists | no |

### What information is missing from `CONN_BIT`

It knows only whether the component partition has one block. It forgets all cycle lengths. The exact witness

\[
C_4\sqcup C_6
\quad\text{vs}\quad
C_5\sqcup C_5
\]

shows this loss.

### What information `R_min` adds

`R_min` retains one genuine path-composition datum: the first global closure scale. This is enough to make the support shortage behind `(0,3)` visible and to distinguish `m` from `2m` in the Q2 family.

It does not expose the rest of the cycle partition.

### What information the period histogram adds

`ROOT_RETURN_PERIOD_HIST` retains **all anonymous first-return periods**, not identities. It strictly refines `R_min` because

\[
R_{\min}(X)=\min\{k:q_k(X)>0\}.
\]

Strictness is witnessed by

\[
C_3\sqcup C_8
\quad\text{vs}\quad
C_3\sqcup C_4\sqcup C_4,
\]

which have the same `R_min=3` but different period histograms.

### Tested Pareto-minimality verdict

Among the tested candidates:

- `CONN_BIT` discloses less but fails the Q6 side;
- `HOLONOMY_EXACTNESS` is semantically enriched and fails the Q2 side;
- `ROOT_RETURN_PERIOD_HIST` succeeds more strongly but discloses strictly more path information;
- `MIN_NATIVE_RETURN` is a single anonymous integer, native to the declared adjacency semantics, and succeeds on both required benchmark defects.

Therefore:

`TESTED_PARETO_MINIMAL_JOINT_PROBE = MIN_NATIVE_RETURN`.

This is **not** a universal theorem that no other incomparable one-bit or scalar P000-native observable could do the same job on the benchmark. Universal minimality would require first fixing a complete admissible probe universe and an information preorder, which Q9 does not assume.

## 8. Exact kernel and no-go boundary

For the successful scalar probe define

\[
\Phi_{\min}(X)=(t(X),p(X),R_{\min}(X)).
\]

Its kernel is nontrivial; `C3+C8` and `C3+2C4` are an explicit kernel pair.

For the period probe define

\[
\Phi_{\mathrm{per}}(X)=(q_k(X))_{k\ge3}.
\]

On `U_2REG`,

\[
\Phi_{\mathrm{per}}(X)=\Phi_{\mathrm{per}}(Y)
\iff
X\cong Y.
\]

Its formal image is exactly the divisibility locus `q_k mod k = 0`.

The Q9 no-go is therefore also exact:

> A global summary can be genuinely nonlocal and still fail joint separation if it measures the wrong global structure. Connectivity alone misses component mass; holonomy exactness measures transport twisting rather than topology. The repair must retain a path-return quantity tied to native Cell support.

## 9. Relation to Q3 and Q4

Q3 showed that groupoid arrows and canonicality depend on actual primitive-preserving morphism semantics. No such morphism quotient is needed for the present `U_2REG` path-return theorem: Cell-isomorphism invariance suffices.

Q4 showed that cycle holonomy is exactly the obstruction to strict synchronized-frame descent on its declared overlap-graph class. Q9 shows that holonomy triviality is not, by itself, a reconstruction invariant for the underlying Cell adjacency. A path can carry two independent kinds of global information:

1. **where/when the path closes** — Q9 return period;
2. **what transport accumulates around the closed path** — Q4 holonomy.

The first repairs the current Q2/Q6 topology/representability benchmark; the second repairs a frame-synchronization problem after a transport enrichment is declared.

This separation avoids importing higher abstraction before the lower-language obstruction requires it.

## 10. Deterministic checker

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_NONLOCAL_PROBE_JOINT_SEPARATION_CHECK_20260830.py`

The checker verifies:

- accepted six-axis carrier generator-order regressions;
- the exact `(t,p,g)` representability theorem through `n=79`;
- Q2 family separation for `r=1..32` and several admissible `m` values per radius by `CONN`, `R_min`, and period histogram;
- Q4-style trivial-holonomy negative control;
- persistence of the Q6 minimal virtual profile under connectedness;
- elimination of `(0,3)` by `R_min`;
- period divisibility and explicit inverse construction;
- the first connectedness collision at `n=10`;
- the first girth-profile collision at `n=11`;
- absence of a period-histogram collision through `n=60`, plus the exact algebraic inverse proof.

Executed output:

`PASS P000_NONLOCAL_PROBE_JOINT_SEPARATION; checks=1645086; q2_family=SEPARATED_BY_CONN_GIRTH_PERIOD; holonomy_exactness=NEGATIVE_CONTROL; q6_minimal_virtual=(0,3)_REJECTED_BY_GIRTH_AND_PERIOD; girth_image=EXACT_THROUGH_N79; period_reconstruction=EXACT_THROUGH_N60_AND_PROVED_BY_INVERSE; conn_first_collision_n=10; girth_first_collision_n=11; period_collision_none_through_n60; carrier_S4_regression=PASS`

## 11. Control-plane recommendation

Driver review should accept only the declared finite witness scope:

`UNIFORM_DECORATED_FINITE_SIMPLE_2_REGULAR_NATIVE_CELL_GRAPHS`.

Recommended reusable gate:

`NATIVE_PATH_RETURN_GATE_V1`

with two levels:

1. `MIN_RETURN`: before treating a fixed-radius local profile as globally meaningful, retain at least one native loop-closure scale when the task is sensitive to component assembly.
2. `PERIOD_INTEGRALITY`: when a rootwise first-return profile is used as a formal completion object, require `q_k mod k = 0`; only then may it serve as a native existence witness on this class.

For richer finite Cell classes, do **not** automatically carry over the period theorem. Instead test whether branching, multiple cycle bases, higher-dimensional Cell incidence, or independent transport labels create two new defects:

- same path-return spectrum but nonisomorphic native gluing;
- formally legal path-return packets with no native realization.

Only after an explicit lower-language failure should Q3/Q4 groupoid or descent machinery be reintroduced.

## Boundary / non-claims

- P000 is not altered.
- Six native spatial dimensions and relational time remain primitive.
- `U_2REG` is a finite witness class only.
- Carrier `S4` remains a carrier readout, not the complete native rotation group.
- Carrier vertices are not native Cells.
- No opaque Cell identity is returned by any successful probe.
- Native adjacency is used only because Q2/Q6 explicitly declared it in their witness class.
- Holonomy is not promoted to bare-P000 primitive data.
- No novelty claim is made for classical girth, cycle decompositions, or nonbacktracking walks.
- `MIN_NATIVE_RETURN` is only the weakest **tested** joint-success candidate under the stated benchmark, not a universal minimality theorem over all possible future P000 probes.
- The period-histogram reconstruction theorem is not generalized beyond finite simple 2-regular graphs.

Result-ID: `RR-BCD1FA15FA40C628701F`  
Execution-Record-ID: `ER-D3865EA8B33644E97A75`
