# P022 — Barlow Stacking Polynomial and Task-Relative Precision

Status: `ACTIVE RESEARCH NOTE / EXACT INTEGER SPECIALIZATION / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: `P022_GEODESIC_MULTIPLICITY.*`, `P022_GEODESIC_MULTIPLICITY_SUPPLEMENT_01.*`  
Cross-route relation: concrete P022 specialization of the A2/P023/P024 rule that required state depends on the declared future language

## 1. Motivation

FCC and HCP should not be treated as two unrelated graph examples. They are two members of the same close-packed stacking family.

Each close-packed layer is a triangular lattice. From one layer to the next there are two possible triangular-hole orientations. Encode the interface choice by

\[
\sigma_j\in\{-1,+1\}.
\]

A finite prefix

\[
\sigma_0,\sigma_1,\ldots,\sigma_{k-1}
\]

describes the contact geometry traversed from layer zero to layer `k`. Periodic sign patterns give periodic Barlow stackings.

The precision question is not merely how many layer choices exist. It is:

> **which part of the stacking word must remain visible for the future geometric queries we actually ask?**

For the full root-to-one-target-layer language of exact native distance and shortest-path multiplicity, the answer is unexpectedly small: one integer imbalance.

## 2. Interface polynomials

Use triangular Laurent coordinates and define

\[
A=x+x^{-1}+y+y^{-1}+xy^{-1}+x^{-1}y,
\]

\[
B_-=1+x^{-1}+y^{-1},
\qquad
B_+=1+x+y.
\]

`A` records one in-layer triangular move. `B_-` and `B_+` record the three possible horizontal offsets of one upward close-packed interface of the two orientations.

They satisfy

\[
\boxed{B_-B_+=A+3.}
\]

The same identity was the HCP vertical-pair formula. Here it becomes the basic close-packing relation.

For downward traversal, the edge offsets reverse, so an upward sign `sigma` is read as effective sign `-sigma` when traversed downward.

## 3. P022-BS01 — no geodesic uses vertical backtracking

Fix a root and a target layer `k`.

A vertical backtrack crosses one interface and later crosses it back. The horizontal displacement polynomial of that matched crossing pair is always

\[
B_-B_+=A+3.
\]

Its support consists of zero and the six primitive triangular displacements. Therefore two matched cross-layer steps can be replaced by:

- zero in-layer steps if their net displacement is zero;
- one in-layer step otherwise.

Either replacement is strictly shorter than two steps.

Hence

\[
\boxed{
\text{every shortest path from layer 0 to layer k crosses exactly }|k|
\text{ interfaces monotonically.}
}
\]

This reduces arbitrary close-packed shortest paths to a finite interface prefix plus in-layer correction.

## 4. P022-BS02 — vertical witness polynomial

Let the effective monotone interface signs from layer zero to target layer `k` be

\[
\epsilon_1,\ldots,\epsilon_{|k|}\in\{-1,+1\}.
\]

Define

\[
\boxed{
P_k(x,y)=\prod_{j=1}^{|k|}B_{\epsilon_j}(x,y).
}
\]

The coefficient

\[
[x^qy^r]P_k
\]

is exactly the number of minimal-vertical witness sequences reaching horizontal coordinate `(q,r)` on the target layer.

Let

\[
t_*(q,r;k)=
\min\{t\ge0:[x^qy^r]P_kA^t>0\}.
\]

Because every `B_±` contains the zero monomial, this finite minimum always exists with

\[
t_*\le h(q,r),
\]

where `h` is triangular distance.

Then

\[
\boxed{
d(q,r,k)=|k|+t_*}
\]

and

\[
\boxed{
g(q,r,k)
=\binom{|k|+t_*}{t_*}
[x^qy^r]P_kA^{t_*}.}
\]

The binomial factor interleaves the ordered vertical and in-layer subsequences.

### Executable verification

The reference implementation compares this formula with independent BFS. An additional in-session reconstruction checked every periodic ± pattern of period at most four through graph radius four: 30 patterns and 9,530 states, with no mismatch.

## 5. P022-BS03 — commutative normal form

Let

\[
n_-(k)=\#\{j:\epsilon_j=-1\},
\qquad
n_+(k)=\#\{j:\epsilon_j=+1\}.
\]

Then

\[
n_-+n_+=|k|.
\]

Define the integer prefix imbalance

\[
\boxed{\delta_k=n_+(k)-n_-(k).}
\]

Because Laurent multiplication is commutative, literal order inside the traversed prefix disappears from `P_k`:

\[
P_k=B_-^{n_-}B_+^{n_+}.
\]

Use `B_-B_+=A+3`. Put

\[
c_k=\min(n_-,n_+)=\frac{|k|-|\delta_k|}{2}.
\]

Then

\[
\boxed{
P_k=(A+3)^{c_k}
\begin{cases}
B_+^{\delta_k},&\delta_k>0,\\
1,&\delta_k=0,\\
B_-^{-\delta_k},&\delta_k<0.
\end{cases}}
\]

This is the **Barlow prefix normal form**.

It separates two finite ingredients:

- `c_k`: how many opposite-orientation interface choices pair into an HCP-like oscillation factor `A+3`;
- `|delta_k|`: how much unmatched stacking drift remains in one orientation.

For a fixed target layer `k`, either quantity determines the other because `|k|` is known.

## 6. P022-BS04 — one integer is sufficient for the full target-layer metric+count language

Suppose the future language asks, for one declared target layer `k`, the exact pair

\[
(d(q,r,k),g(q,r,k))
\]

for arbitrary horizontal endpoints `(q,r)` on that layer.

The target index `k` is query context. From `(|k|,delta_k)` recover

\[
n_-=(|k|-\delta_k)/2,
\qquad
n_+=(|k|+\delta_k)/2,
\]

then reconstruct `P_k`, then the exact distance and geodesic count by BS02.

Therefore

\[
\boxed{
\delta_k
\text{ is a sufficient stacking-prefix state for the complete root-to-layer-k distance+count language.}
}
\]

No individual interface identity is needed for this declared language.

This is a concrete P022 instance of task-relative precision.

## 7. P022-BS05 — the imbalance is also necessary up to finite relabeling

Sufficiency alone would not show that `delta_k` is the exact precision coordinate. We can recover it from the complete target-layer count language.

For a Laurent polynomial

\[
P=\sum_{q,r}c_{q,r}x^qy^r,
\]

define total mass and first exponent moments

\[
M(P)=\sum c_{q,r},
\]

\[
Q(P)=\sum q\,c_{q,r},
\qquad
R(P)=\sum r\,c_{q,r}.
\]

For one interface,

\[
M(B_+)=M(B_-)=3,
\]

\[
Q(B_+)=R(B_+)=1,
\qquad
Q(B_-)=R(B_-)=-1.
\]

The product moment identity

\[
Q(PQ)=Q(P)M(Q)+M(P)Q(Q)
\]

therefore gives, for `|k|>0`,

\[
\boxed{
M(P_k)=3^{|k|},
\qquad
Q(P_k)=R(P_k)=\delta_k\,3^{|k|-1}.}
\]

Hence

\[
\boxed{
\delta_k=Q(P_k)/3^{|k|-1}.}
\]

Now observe that the full root-to-layer `distance+count` language reconstructs `P_k` itself:

- if `[x^qy^r]P_k>0`, then the endpoint `(q,r,k)` has distance exactly `|k|`, and its shortest-path count at `t=0` equals that coefficient;
- if the coefficient is zero, the endpoint needs at least one in-layer step and therefore has larger distance.

Thus the future language recovers the coefficient function `P_k`, which recovers `delta_k`.

Therefore, among exact finite quotients of stacking prefixes for this language,

\[
\boxed{
\delta_k
\text{ is minimal up to a bijective relabeling of its finite represented values.}
}
\]

Two distinct imbalance values cannot be safely identified.

## 8. P022-BS06 — selected-layer precision is a vector of selected prefix imbalances

Let the future language query a finite set of target layers

\[
J=\{k_1,\ldots,k_m\}.
\]

By BS04, the vector

\[
\boxed{
\Delta_J=(\delta_{k_1},\ldots,\delta_{k_m})
}
\]

is sufficient for all root-to-selected-layer distance+count queries.

By BS05, each coordinate is recoverable from the corresponding target-layer language. Therefore `Delta_J` is also minimal up to finite relabeling.

This makes the precision cost grow with the **queried layer set**, not automatically with the literal stacking-history length.

### Extreme cases

If only one far layer is queried, one integer is enough.

If every upward prefix layer `1,2,...,N` is queried, then

\[
\sigma_j=\delta_{j+1}-\delta_j
\]

with `delta_0=0`. So the full imbalance trajectory

\[
(\delta_1,\ldots,\delta_N)
\]

reconstructs the entire stacking word.

Hence

\[
\boxed{
\text{query every intermediate layer}
\Longrightarrow
\text{no stacking-order compression remains.}}
\]

This is not a contradiction. It is precisely the task-relative nature of exact precision.

## 9. Same final state, different intermediate future

Take two four-interface words

\[
(-,-,+,+)
\]

and

\[
(-,+,-,+).
\]

At layer four both have

\[
(n_-,n_+)=(2,2),
\qquad
\delta_4=0.
\]

Therefore their entire root-to-layer-four distance+count language is identical.

At layer two, however,

\[
\delta_2=-2
\]

for the first word and

\[
\delta_2=0
\]

for the second. Their layer-two endpoint semantics differ.

So

\[
\boxed{
\text{same final prefix imbalance}
\not\Rightarrow
\text{same intermediate-layer future language}.}
\]

This is the close-packing analogue of the broader P023/P024 lesson: a quotient is legal only for the operations/observations actually declared.

## 10. FCC and HCP as two normal-form extremes

### FCC-type constant drift

A constant sign pattern has

\[
|\delta_k|=|k|,
\qquad c_k=0,
\]

so

\[
P_k=B_\pm^{|k|}.
\]

This reproduces the `A_3/FCC` contact-graph shell and multiplicity spectra in the executable checks.

### HCP-type alternating stacking

An alternating sign pattern has bounded imbalance:

\[
\delta_{2m}=0,
\qquad |\delta_{2m+1}|=1.
\]

Thus

\[
P_{2m}=(A+3)^m,
\]

and odd layers carry one extra `B_±` factor. This is exactly the HCP formula of Supplement 01.

### General Barlow prefix

Every finite prefix lies between these extremes in the normal-form sense:

\[
P_k=(A+3)^{(|k|-|\delta_k|)/2}B_{\operatorname{sgn}\delta_k}^{|\delta_k|}.
\]

This makes `|delta_k|` a direct integer measure of unpaired stacking drift for the declared root-to-layer language.

## 11. Period-boundary universality

Let a periodic stacking word have period length `L` with period imbalance

\[
D=\sum_{j=0}^{L-1}\sigma_j.
\]

At layer `mL`,

\[
\delta_{mL}=mD.
\]

Therefore every periodic stacking with the same pair `(L,D)` has exactly the same vertical witness polynomial, and hence the same root-to-layer-`mL` distance+count language, at every period boundary:

\[
\boxed{
P_{mL}
=(A+3)^{m(L-|D|)/2}
B_{\operatorname{sgn}D}^{m|D|}.}
\]

Literal order inside the period is invisible at those queried layers.

For example, all zero-drift periods have

\[
P_{mL}=(A+3)^{mL/2}
\]

at period boundaries, even though their intermediate layers and complete rooted shell spectra can differ.

This theorem is exact. It should not be overextended to all-layer or all-shell equivalence.

## 12. Current open growth question

Bounded computation shows a structured phenomenon:

- zero-drift periodic stackings tested so far approach the same shell-total geodesic growth rate as HCP;
- nonzero-drift periodic stackings lie between HCP and FCC in the tested examples;
- patterns with the same long-run drift but different order show different finite shells while appearing to approach the same exponential rate.

This is **not yet promoted to a theorem**.

The new normal form suggests a precise next target:

> determine whether the asymptotic shell-total geodesic growth rate of a periodic Barlow stacking depends only on the rational drift `|D|/L`, and if so derive the algebraic growth constant from that drift.

Any proof must control whole-shell queries, which see the entire prefix-imbalance trajectory inside a period, not only the period-boundary state.

## 13. Ownership and architecture

The generic statement “future language determines the legal quotient” remains A2/P023/P024 mathematics.

P022 owns the concrete specialization:

- close-packed stacking signs;
- `B_±` and `A` Laurent polynomials;
- Barlow prefix normal form;
- exact integer imbalance coordinate;
- FCC/HCP and periodic-stacking consequences.

The cross-route relation is therefore `SPECIALIZATION / CONSUMER`, not `SAME_MOTHER`.

## 14. Executable assets

Added:

- `src/enterprise_math/p022_barlow_stacking.py`;
- `src/enterprise_math/p022_barlow_precision.py`;
- `tests/test_p022_barlow_stacking.py`;
- `tests/test_p022_barlow_precision.py`.

The executable layer checks:

- the unified formula against BFS for FCC and HCP;
- FCC reconstruction against `A_3` spectra;
- HCP reconstruction against the independent HCP module;
- same-count/different-order prefix equivalence at the selected final layer;
- intermediate-layer failure of that equivalence;
- first-moment recovery of `delta`;
- exhaustive finite minimality shadows on short stacking words.
