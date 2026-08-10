# R004 precision genesis — Supplement 02: locality obstruction, latent capacity, minimal bridges, and derived record overlap

Status: `PROVED_WIP + EXECUTABLE_CHECKED + COUNTEREXAMPLE + PRIOR_ART + PHYSICAL_HYPOTHESIS`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_01.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

This supplement attacks the sharpened frontier left by Supplement 01:

> what independently motivated finite structural restriction can prevent a complete latent/pre-sampled completion, while also moving hierarchy geometry toward connected space and moving P016 from a free overlap parameter toward a derived observable?

It produces the first partial positive answer to the latent-completion question, but only under explicit Bell-locality assumptions. It does not claim `CANONICAL_MAIN`, prove cosmological genesis, or establish unconditional ontic randomness.

## 1. The first operational obstruction to complete local pre-sampling

Supplement 01 proved that finite deterministic towers, finite rational stochastic kernels, and even finite adaptive intervention policies admit finite pre-sampled completions if arbitrary counterfactual response tables are allowed.

The new move is to restrict those response tables independently of the observed outcome data.

Consider two separated binary-response wings. Alice chooses setting `x in {0,1}` and Bob chooses setting `y in {0,1}`. A deterministic **setting-local** latent table is

\[
\lambda=(A_0,A_1,B_0,B_1),
\qquad
A_x,B_y\in\{-1,+1\},
\]

where Alice's value depends on `x` and the latent seed but not on Bob's setting, and Bob's value depends on `y` and the latent seed but not on Alice's setting.

The second restriction is **measurement-setting independence**: the latent-seed multiplicities/probabilities are the same for all four setting pairs. In the finite integer implementation, one nonnegative integer weight `w_lambda` is assigned to each local table once, before the setting pair is chosen.

These are substantive causal restrictions. They are not implied by finiteness alone.

## 2. Exact integer CHSH theorem for finite local tables

For one deterministic local table define

\[
S_\lambda
=A_0B_0+A_0B_1+A_1B_0-A_1B_1.
\]

Rewrite it as

\[
S_\lambda
=A_0(B_0+B_1)+A_1(B_0-B_1).
\]

Because `B_0,B_1` are each `+1` or `-1`, exactly one of the two parentheses is zero and the other is `+2` or `-2`. Therefore

\[
\boxed{S_\lambda\in\{-2,+2\}.}
\]

There are exactly sixteen deterministic local tables. R004 exhaustively checks all sixteen and obtains eight at `-2` and eight at `+2`.

Now give those tables nonnegative integer multiplicities `w_lambda`, with

\[
W=\sum_\lambda w_\lambda>0.
\]

The same multiplicities are used for every setting pair. Let the four correlation numerators be

\[
C_{xy}=\sum_\lambda w_\lambda A_x(\lambda)B_y(\lambda).
\]

Then

\[
C_{00}+C_{01}+C_{10}-C_{11}
=\sum_\lambda w_\lambda S_\lambda,
\]

so ordinary integer triangle inequality gives

\[
\boxed{
|C_{00}+C_{01}+C_{10}-C_{11}|\le2W.
}
\]

If one divides by the common positive weight `W`, this is the usual CHSH bound `|S|<=2`. R004 keeps the cross-multiplied integer form as the primitive executable statement.

This theorem is Bell/CHSH prior mathematics, not a new Enterprise Math theorem family [SRC-BELL-1964-EPR; SRC-CHSH-1969]. The R004 contribution is the explicit use of that established obstruction against its own finite pre-sampled-completion loophole.

## 3. A fully rational quantum target outside the local completion class

The usual maximal CHSH example is often written using `sqrt(2)`. R004 does not need that form.

Choose planar unit directions

\[
a_0=(1,0),
\qquad
a_1=(0,1),
\]

and the Pythagorean rational directions

\[
b_0=(3/5,4/5),
\qquad
b_1=(3/5,-4/5).
\]

For the spin singlet, the standard quantum correlation is

\[
E(a,b)=-a\cdot b.
\]

Therefore the four exact correlations are

\[
(E_{00},E_{01},E_{10},E_{11})
=
(-3/5,-3/5,-4/5,+4/5).
\]

With the preceding CHSH sign convention,

\[
S
=E_{00}+E_{01}+E_{10}-E_{11}
=-14/5,
\]

hence

\[
\boxed{|S|=14/5>2.}
\]

No floating-point number and no irrational direction is required.

With unbiased binary marginals, the corresponding joint probabilities

\[
P(A=a,B=b\mid x,y)
=\frac{1+abE_{xy}}4
\]

are all integer multiples of `1/20`. R004 therefore represents the target by exact twenty-atom count tables. For `E=-3/5` the counts are `(2,8,8,2)` over `(--,-+,+-,++)`; for `E=-4/5` they are `(1,9,9,1)`; for `E=+4/5` they are `(9,1,1,9)`.

Thus a completely finite rational observable target already lies outside the setting-local, setting-independent pre-sampled class.

## 4. What this does—and does not—say about generation

The result is the first partial positive answer to the R004 generative-identifiability problem:

\[
\boxed{
\text{locality + setting independence + pre-sampling}
\Longrightarrow |S|\le2,
}
\]

while an exact finite rational target has `|S|=14/5`.

Therefore **that restricted latent completion class is operationally distinguishable** from the target.

The conclusion must not be overextended. It does not exclude:

- nonlocal hidden-variable completions;
- models in which the latent state is statistically dependent on future measurement settings;
- superdeterministic or other measurement-dependence constructions;
- physical models that reject the singlet correlation law being tested;
- arbitrary metaphysical claims about when an outcome becomes ontically real.

Hensen et al. provide an experimental benchmark closing the locality and detection loopholes in their Bell test [SRC-HENSEN-2015-BELL], while Bell-certified randomness has a substantial device-independent literature [SRC-PIRONIO-2010-BELL-RANDOMNESS]. R004 consumes these as pressure tests. It does not claim that one Bell violation unconditionally proves the whole precision-genesis ontology.

The remaining R004 question is now narrower:

> can Enterprise Math derive or independently justify locality and setting independence from its finite causal/geometry layer rather than inserting them only to inherit Bell's theorem?

## 5. A second obstruction: finite initial latent capacity

Locality is not the only possible restriction. A different candidate is a hard finite resource bound on the initial latent carrier.

Suppose a declared future language has `m` steps and `r>=1` possible responses per step. The number of complete response strings is

\[
\boxed{r^m.}
\]

Let a deterministic pre-sampled seed state select one complete response string. If the target future law has **full support**—every one of the `r^m` strings must occur with positive probability—then the seed-to-string map must be surjective. Consequently

\[
\boxed{|U|\ge r^m.}
\]

This bound needs no logarithm and no rational-probability assumption. It is ordinary finite surjectivity counting.

It is sharp: `r^m` seed states suffice by assigning one seed state to each response string and then choosing whatever positive weights the target distribution requires when such weights are available.

For a finite initial seed capacity `K`, the largest full-support horizon is therefore the greatest integer `m` satisfying

\[
r^m\le K.
\]

The executable layer computes this by repeated integer multiplication rather than `log_r K`.

### Precision-one corollary

If the strong R004 pregeometry semantics says that precision one contains exactly one complete physical state and **no additional hidden carrier**, then `K=1`. A deterministic complete pre-sampling of even one genuinely two-outcome full-support future step would require `K>=2` and is impossible inside that ontology.

This does not by itself prove how the second outcome is physically generated. It proves only that a deterministic all-at-once latent encoding is unavailable once the one-state/no-hidden-carrier premise is taken literally.

## 6. Minimal cross-fiber bridges: exact connectivity cost

Supplement 01 proved that nested refinement canonically induces an ultrametric but need not produce connected local space.

Now view the nested precision classes as a finite rooted refinement tree. For every parent class `v`, let

\[
c(v)=\text{number of immediate child classes of }v.
\]

Add **witnessed leaf edges**. An edge counts as a bridge for parent `v` only when its two leaf endpoints lie in different immediate children of `v`.

To make the quotient graph on `v`'s children connected requires at least

\[
c(v)-1
\]

such bridge witnesses.

Nestedness gives every leaf edge a unique first-divergence parent, so one edge cannot simultaneously pay the cross-child connectivity cost of two different parents. Hence every bridge certificate requires at least

\[
\sum_v(c(v)-1)
\]

leaf edges.

For one root and singleton final classes, the refinement-tree count telescopes:

\[
\boxed{
\sum_v(c(v)-1)=|X|-1.
}
\]

Choosing one spanning tree on the child quotient of every parent realizes exactly that many witnessed leaf edges. By induction from the leaves upward, the resulting leaf graph is connected. Therefore

\[
\boxed{
\text{minimum immediate-child bridge certificate size}=|X|-1.
}
\]

The resulting graph is a spanning tree and is globally edge-minimal for connectivity.

This is established finite tree/graph mathematics specialized to the R004 refinement hierarchy; it is not claimed as a novel graph theorem.

## 7. Minimal connectivity still does not determine macroscopic geometry

The exact connectivity cost closes one gap but exposes another.

For the binary hierarchy on eight leaves with scales `(1,2,4,8)`, the minimum bridge count is seven. R004 constructs two different seven-edge certificates on the **same hierarchy**:

1. a first-representative witness tree with graph diameter `5`;
2. an ordered boundary-witness tree that is the path `0-1-2-3-4-5-6-7`, with diameter `7`.

Both connect every immediate child quotient using the exact minimum `|X|-1=7` edges.

Thus

\[
\boxed{
\text{hierarchy + minimum connectedness}
\not\Rightarrow
\text{unique macroscopic geometry}.
}
\]

The next geometric variable must constrain **which** cross-fiber witnesses are physically admissible—e.g. translation symmetry, bounded degree, homogeneous local neighborhoods, causal accessibility, or another exact finite condition—not merely how many bridges exist.

## 8. P016 continuation: derive eta from a finite record generator

The first R004 P016 premodel treated the environment-record overlap `eta` as a predeclared parameter. This supplement removes that freedom in one explicit toy subfamily.

Let the finite environment state be

\[
e\in\{0,1,\ldots,d-1\},
\]

with positive integer resolution `d`. Define the record generated by system state `x` as

\[
R_d(x,e)=\left\lfloor\frac{e+x}{d}\right\rfloor,
\]

implemented by integer division.

Compare two alternatives `x=0` and `x=delta`, with `delta>=0`. Since `R_d(0,e)=0` throughout the declared environment cell, the two records agree exactly when

\[
e+\delta<d.
\]

Therefore the exact agreement count is

\[
\max(d-\delta,0),
\]

and under the toy uniform environment cell

\[
\boxed{
\eta(d,\delta)=\frac{\max(d-\delta,0)}d.
}
\]

The executable formula is independently checked against explicit record enumeration over many bounded integer cases.

If the visibility law remains

\[
V_{\mathrm{predicted}}=\eta V_{\mathrm{ordinary}},
\qquad 0\le V_{\mathrm{ordinary}}\le1,
\]

then the representative Pedalino lower numerical endpoint `0.09` [SRC-PEDALINO-2026-NANOPARTICLE] cannot be reached when `eta<0.09`. In this derived subfamily the condition is exactly

\[
\boxed{100\delta>91d.}
\]

This is an integer cross-product inequality. It is still only an algebraic range exclusion, not a confidence-level result.

The decisive missing physical map is now narrower:

`real apparatus/environment -> integer record resolution d and alternative separation delta`.

Until that map is independently calibrated, `R004-THRESHOLD-RECORD-PREMODEL-V1` remains `PHYSICAL_HYPOTHESIS`.

## 9. Revised closure picture

The R004 frontier is no longer one undifferentiated question.

### Generative identifiability

Arbitrary finite pre-sampling survives deterministic refinement, rational randomness and adaptive interventions. It fails after adding at least some independently testable restrictions. Bell locality plus measurement-setting independence is one proven example; a hard finite initial seed-capacity bound is another, purely combinatorial resource restriction.

### Geometry

Nested refinement gives hierarchy/ultrametric structure. A complete immediate-child bridge certificate adds connectedness at the exact minimum `|X|-1` leaf edges. But the choice of witnesses still changes macroscopic graph geometry.

### P016

The overlap variable can be derived from a concrete finite record map rather than freely fitted. The unresolved task is now apparatus calibration, not algebraic freedom in `eta`.

These three advances point toward one stronger common target:

> derive locality/resource bounds, admissible cross-fiber bridges, and record-generation parameters from one finite causal dynamics, then test its unavoidable joint predictions.

That would be qualitatively stronger than adding another isolated toy mechanism, because the same primitive law would have to survive the Bell/locality boundary, geometry reconstruction, and P016 falsification simultaneously.
