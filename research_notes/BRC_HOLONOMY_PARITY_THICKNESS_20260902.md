# BRC rational holonomy parity skeleton and exact prime-power thickness

Status: `RESEARCH CANDIDATE / EXACT m-POWER-FREE DECOMPOSITION`
Date: `2026-09-02`
Research mode: `TASK_RESEARCH continuation`
Foundation baseline: `main@4f6761bbb5fb5b256d856cbfd25958483ebc1d72`
Parent research: `BRC_PRIME_VALUATION_HOLONOMY_MODULE_20260902.md`

## 0. Question

The previous checkpoint classified positive rational BRC gauge by prime-valuation cohomology and showed that reduction modulo `m` gives `H^1(G;Z/m)` holonomy shadows.

Can the information lost by a mod-`m` shadow be recovered as an exact rational `m`-th-power thickness, analogously to the earlier arithmetic split between squarefree support and repeated-prime thickness?

Yes, once a spanning-tree/fundamental-cycle basis is fixed.

The mod-`m` cohomology class itself is intrinsic. The concrete decomposition below is canonical **relative to the chosen tree normal form**, not basis-free.

## 1. Unique m-power-free decomposition of a positive rational

Fix `m>=2` and let

\[
q\in\mathbb Q_{>0}^{\times}.
\]

For each prime write the Euclidean valuation decomposition

\[
v_p(q)=m k_p+r_p,
\qquad
0\le r_p<m,
\qquad
k_p\in\mathbb Z.
\]

Define

\[
\boxed{
s_m(q):=\prod_p p^{r_p}}
\]

and

\[
\boxed{
t_m(q):=\prod_p p^{k_p}\in\mathbb Q_{>0}^{\times}.}
\]

Then `s_m(q)` is a positive `m`-power-free integer: every prime exponent lies in `{0,...,m-1}`.

Moreover

\[
\boxed{
q=s_m(q)\,t_m(q)^m.
}
\]

The pair `(s_m(q),t_m(q))` is unique.

Proof: prime valuations of the right side are `r_p+mk_p=v_p(q)`. Uniqueness is coordinatewise uniqueness of Euclidean division of each integer valuation by `m`.

Candidate theorem name:

`BRC_RATIONAL_M_POWER_FREE_THICKNESS_DECOMPOSITION`.

## 2. Squarefree / C2 specialization

For `m=2`,

\[
v_p(q)=\varepsilon_p+2k_p,
\qquad\varepsilon_p\in\{0,1\}.
\]

Put

\[
\boxed{
s(q)=\prod_{\varepsilon_p=1}p}
\]

and

\[
\boxed{r(q)=\prod_pp^{k_p}.}
\]

Then

\[
\boxed{
q=s(q)\,r(q)^2,
}
\]

with `s(q)` a positive squarefree integer and `r(q)` a positive rational.

The squarefree integer `s(q)` packs the all-prime parity vector

\[
(v_p(q)\bmod2)_p
\]

without loss at the parity layer.

The rational factor `r(q)^2` carries exactly the even valuation depth discarded by parity.

We call:

```text
s(q) = C2 / parity skeleton representative
r(q) = rational square-thickness root
r(q)^2 = square-thickness factor
```

This terminology is a BRC typing convention, not a claim that generic square-class decomposition is new mathematics.

## 3. Denominator primes are part of the same parity skeleton

Negative valuations cause no separate case.

For example,

\[
q=\frac12
\]

has

\[
v_2(q)=-1=1+2(-1),
\]

so

\[
s(q)=2,
\qquad
r(q)=\frac12,
\]

and

\[
\frac12=2\left(\frac12\right)^2.
\]

Thus `p^{-1}` and `p` have the same parity class because they differ by the rational square `p^{-2}`.

The squarefree representative is always a positive integer even when the original holonomy is a proper fraction.

## 4. Exact BRC ROOT materialization of thickness

Let

\[
q=\frac ab
\]

be reduced and set

\[
\frac{q}{s_m(q)}=\frac NM
\]

in lowest terms.

By construction every prime valuation of this ratio is divisible by `m`. Hence

\[
N=u^m,
\qquad
M=v^m
\]

for unique positive integers `u,v`, and

\[
\boxed{t_m(q)=u/v.}
\]

Therefore thickness recovery can pass through the existing exact BRC root facade:

```text
q / s_m(q)
-> reduced DIV carrier N/M
-> ROOT_m(N), ROOT_m(M)
-> exact perfect-power traces
-> thickness root u/v
```

No floating root is required.

Candidate theorem/tool bridge:

`BRC_HOLONOMY_MTH_POWER_THICKNESS_ROOT_MATERIALIZATION`.

## 5. Tree-normal gauge coordinate decomposition

For a connected rationally weighted graph, fix root/spanning tree `T` and normalize all tree weights to `1` as in the preceding checkpoint.

Let the `beta_1` fundamental rational holonomies be

\[
\widehat q_1,\ldots,\widehat q_{\beta_1}.
\]

Apply the decomposition coordinatewise:

\[
\boxed{
\widehat q_j
=s_{m,j}\,t_{m,j}^{\,m}.
}
\]

Then:

- `(s_{m,j})` is a complete representative of the mod-`m` holonomy shadow in the chosen fundamental-cycle basis;
- `(t_{m,j})` retains the integer quotient valuations discarded by that shadow;
- together the pair recovers the complete rational gauge class.

For `m=2`, the exact normal form is

\[
\boxed{
\widehat q_j=s_jr_j^2,
\qquad
s_j\text{ squarefree integer},
\quad
r_j\in\mathbb Q_{>0}.
}
\]

Candidate theorem name:

`BRC_TREE_GAUGE_PARITY_THICKNESS_COMPLETE_NORMAL_FORM`.

## 6. Exact forgetful map and its fibers

For one coordinate the parity forgetful map is

\[
\pi_2:\mathbb Q_{>0}^{\times}\to
\{\text{positive squarefree integers}\},
\qquad
q\mapsto s(q).
\]

Every fiber has the exact form

\[
\boxed{
\pi_2^{-1}(s)=\{s r^2:r\in\mathbb Q_{>0}^{\times}\}.
}
\]

Thus the `C_2`/parity shadow is highly many-to-one. Its lost information is not mysterious: it is precisely the rational square-thickness root `r`.

For `beta_1` tree-normal cycle coordinates, a fixed parity skeleton has fiber

\[
\boxed{
(\mathbb Q_{>0}^{\times})^{\beta_1}
}
\]

through the independent thickness roots `r_j`.

This is a direct analogue of the project rule that Boolean/support projection should not silently be treated as a complete weighted state.

## 7. Parity does not determine recurrent stability

The parity shadow is too coarse even for the simplest recurrent BRC.

Consider one positive self-loop.

The two weights

\[
q_1=\frac12,
\qquad
q_2=2
\]

have the same squarefree skeleton:

\[
s(q_1)=s(q_2)=2.
\]

Indeed

\[
\frac12=2(1/2)^2,
\qquad
2=2(1)^2.
\]

But the recurrent phases are opposite:

\[
q_1<1\quad\Rightarrow\quad\text{stable},
\]

while

\[
q_2>1\quad\Rightarrow\quad\text{divergent}.
\]

Therefore

\[
\boxed{
C_2\text{ parity holonomy does not determine positive recurrent stability.}
}
\]

The thickness coordinate is dynamically material.

Candidate negative boundary:

`BRC_C2_SHADOW_DOES_NOT_DETERMINE_POSITIVE_MASS_PHASE`.

## 8. Parity also does not determine loop surplus inside the stable phase

Even after restricting to stable weights, parity remains insufficient.

Take

\[
q_1=\frac12,
\qquad
q_2=\frac18.
\]

Both have squarefree skeleton `2`, but

\[
r(q_1)=\frac12,
\qquad
r(q_2)=\frac14.
\]

Their one-state loop-zeta ratios are

\[
Z_1=\frac1{1-1/2}=2,
\qquad
Z_2=\frac1{1-1/8}=\frac87.
\]

Hence

\[
\Gamma_1=\ln2,
\qquad
\Gamma_2=\ln(8/7).
\]

So the full positive recurrent loop surplus depends on thickness within a fixed `C_2` shadow.

Candidate negative boundary:

`BRC_C2_SHADOW_DOES_NOT_DETERMINE_LOOP_SURPLUS`.

## 9. Relation to earlier arithmetic support/thickness

The structure mirrors an earlier arithmetic phenomenon.

For integer prime exponents, squarefree projection retains only whether each exponent is zero/one modulo the relevant support rule and discards repeated-prime depth. Here rational cycle holonomy has the exact valuation split

\[
v_p=\varepsilon_p+2k_p.
\]

The parity vector `epsilon_p` gives the squarefree/C2 skeleton; the integers `k_p` give the residual prime-power thickness.

The important common principle is:

```text
REDUCED SUPPORT / PARITY SHADOW
!=
FULL PRIME-POWER STATE
```

and the omitted strata can change actual BRC dynamics.

This does not identify the old divisor-thickness observable `Theta` with the present rational gauge thickness; it identifies a recurring **typed decomposition pattern**.

## 10. m-th-power hierarchy

The same mechanism exists for every `m>=2`:

\[
q=s_m(q)t_m(q)^m.
\]

The residue exponents

\[
r_p=v_p(q)\bmod m
\]

encode the `Z/m` holonomy shadow, while the quotient exponents

\[
k_p=(v_p-r_p)/m
\]

encode the retained thickness root.

Thus the rational positive gauge layer naturally supports a hierarchy

\[
\boxed{
\text{full integer valuations}
\to
\text{mod-}m\text{ holonomy shadow}
\to
\text{m-power-free representative}
}
\]

with an exact complementary rational `m`-th-power factor.

For `m=2`, this hierarchy lands on the existing `C_2/H^1` layer.

## 11. Basis dependence versus intrinsic shadow

The abstract class

\[
[v_p(q)\bmod m]\in H^1(G;\mathbb Z/m)
\]

is intrinsic.

A concrete tuple of `m`-power-free integers

\[
(s_{m,1},\ldots,s_{m,\beta_1})
\]

requires the chosen spanning-tree/fundamental-cycle basis.

Changing the tree changes the coordinate tuple by the corresponding integral cycle-basis transformation before reduction.

Therefore:

```text
MOD-m COHOMOLOGY SHADOW = INTRINSIC
m-POWER-FREE FUNDAMENTAL COORDINATES = TREE/BASIS-RELATIVE CANONICAL FORM
```

This boundary is essential for later tool design.

## 12. Prior-art boundary

Classical ingredients include:

- unique factorization and Euclidean division of prime valuations;
- rational square classes and `m`-th-power classes;
- perfect-power extraction;
- graph cohomology with finite coefficients.

No generic novelty claim is made.

The project-specific synthesis under test is:

```text
BRC RATIONAL HOLONOMY
-> PRIME-VALUATION COHOMOLOGY
-> mod-m HOLONOMY SHADOW
-> m-POWER-FREE INTEGER SKELETON
   + EXACT RATIONAL m-THICKNESS ROOT
-> BRC ROOT_m MATERIALIZATION
-> EXPLICIT PROOF THAT SHADOW ALONE CAN LOSE DYNAMIC PHASE/SURPLUS
```

## 13. Hard boundaries

This candidate does not claim:

- a basis-free canonical `m`-power-free tuple without choosing cycle coordinates;
- that `C_2` parity determines positive recurrent dynamics;
- that rational thickness is non-negative in log orientation (`r` may be less than one);
- that this decomposition handles signed/amplitude holonomy;
- that the previous arithmetic `Theta` variable equals the present thickness root;
- generic novelty of rational square-class decomposition.
