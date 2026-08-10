# Legendre Pressure Test — Supplement 36

Status: `PROVED RESEARCH NOTE`  
Scope: canonical product measure on the split-profile completion and the dense-null actual state image  
Depends on: P017 L074 finite-pattern densities, L077 projective completion, classical product measure and Borel–Cantelli  
Discipline: product probability measures, weak convergence, and Borel–Cantelli are standard probability/topology. The theorem is a statistical limit of deterministic basin profiles; it is not an ontological claim that a random infinite split profile is a physical state.

## 1. Finite split-pattern densities form a consistent probability family

For every prime `p`, let

\[
q_p=\frac1{\sqrt p}.
\]

L074 proves that for every finite prime set `F` and every binary pattern

\[
\varepsilon\in\{0,1\}^{F},
\]

the natural density of basin indices realizing that split pattern is

\[
\boxed{
\prod_{p\in F}
q_p^{\varepsilon_p}(1-q_p)^{1-\varepsilon_p}.
}
\]

These finite-dimensional laws are projectively consistent when coordinates are forgotten.

## 2. P017-L080-A — Canonical completion measure

Status: `PROVED / STANDARD PRODUCT-MEASURE CONSTRUCTION`.

On the infinite Boolean completion

\[
\Omega=\{0,1\}^{\mathbb P},
\]

define the product probability measure

\[
\boxed{
\mu
=
\bigotimes_{p\text{ prime}}
\operatorname{Bernoulli}(q_p).
}
\]

For every finite cylinder fixing pattern `epsilon` on `F`,

\[
\boxed{
\mu(C_{F,\varepsilon})
=
\prod_{p\in F}
q_p^{\varepsilon_p}(1-q_p)^{1-\varepsilon_p}.
}
\]

Thus the completion measure reproduces exactly the deterministic natural-density laws of all finite split shadows.

No independent probabilistic ansatz is being fitted to the data; the product law is already forced by L074.

## 3. Actual profiles remain finite-support

Recall the all-prime actual profile

\[
I(k)=(I_p(k))_p,
\]

with `I_p(k)=0` whenever `p>k`.

Therefore every actual profile has finite support:

\[
\boxed{
\#\{p:I_p(k)=1\}<\infty.
}
\]

Let

\[
\mathcal A=\{I(k):k\in\mathbb N\}
\subseteq\Omega.
\]

L077 proves that `A` is countable and dense in `Omega`.

## 4. P017-L080-B — A typical completion profile has infinitely many active split bits

Status: `PROVED` by the second Borel–Cantelli lemma.

Under `mu`, the coordinate events

\[
E_p=\{\omega:\omega_p=1\}
\]

are independent and

\[
\mu(E_p)=q_p=p^{-1/2}.
\]

Since

\[
\sum_p q_p
=
\sum_p p^{-1/2}
=\infty,
\]

Borel–Cantelli gives

\[
\boxed{
\mu\{\omega:\omega_p=1\text{ for infinitely many primes }p\}=1.
}
\]

Hence a `mu`-typical completion profile has infinite support.

## 5. P017-L080-C — The actual basin image has completion measure zero

Status: `PROVED`.

Every actual profile has finite support, while `mu`-almost every completion profile has infinite support.

Therefore

\[
\boxed{
\mu(\mathcal A)=0.
}
\]

Combining with L077's density result,

\[
\boxed{
\overline{\mathcal A}=\Omega
\qquad\text{but}\qquad
\mu(\mathcal A)=0.
}
\]

The actual integer states are topologically dense yet statistically null inside their natural infinite precision completion.

## 6. Dense does not mean typical

Every finite cylinder contains actual basin profiles, and in fact every finite split pattern occurs with positive natural density.

Yet the completion measure assigns probability one to profiles that are **not** any actual basin profile.

Thus two different completion notions must be separated:

- topological approximation by finite-coordinate agreement;
- statistical typicality under the limiting cylinder law.

The actual image is maximal in the first finite-shadow sense and negligible in the second.

## 7. P017-L081-A — Empirical basin measures converge on every cylinder

Define the empirical measure of the first `K` basin profiles by

\[
\boxed{
\nu_K
=
\frac1K\sum_{k\le K}\delta_{I(k)}.
}
\]

For every finite cylinder `C_{F,epsilon}`, L074 gives

\[
\boxed{
\nu_K(C_{F,\varepsilon})
\longrightarrow
\mu(C_{F,\varepsilon}).
}
\]

So the deterministic basin sequence has exactly the product measure as its limiting law on every finite precision query.

## 8. P017-L081-B — Weak convergence to the completion measure

Status: `PROVED / STANDARD COMPACT-PRODUCT ARGUMENT`.

The countable Boolean product `Omega` is compact metrizable. Finite-cylinder indicator functions are continuous because cylinders are clopen, and finite-coordinate functions form an algebra separating points and containing constants.

By the standard density/approximation theorem for continuous functions on this compact product, convergence of empirical integrals for all finite-coordinate functions implies convergence for every continuous function.

Therefore

\[
\boxed{
\nu_K\Rightarrow\mu.
}
\]

So empirical measures supported entirely on actual finite-support profiles converge weakly to a measure that assigns those actual profiles total mass zero.

There is no contradiction: weak limits need only lie in the closure of supports, and L077 says that closure is all of `Omega`.

## 9. P017-L081-C — Statistical completion can be canonical without being state realization

The measure `mu` is canonically determined by the finite split-pattern densities.

Yet

\[
\mu(\mathcal A)=0.
\]

Hence a mathematically natural statistical completion may be highly useful for asymptotic statements even though its typical points are not actual primitive states of the original integer system.

This gives a precise distinction:

\[
\boxed{
\text{canonical limiting law on a completion}
\not\Rightarrow
\text{completion points are actual states}.
}
\]

## 10. Relation to P005 projective realization

P005-S1 separates finite realizability from completion realizability.

L080–L081 add a statistical layer:

1. every finite shadow is fully realized;
2. actual profiles are dense but not completion-surjective;
3. deterministic finite-shadow frequencies select a canonical probability measure on the completion;
4. that measure is concentrated on non-actual infinite-support profiles.

Thus completion may be simultaneously:

- the closure of actual states;
- the support of an asymptotic law;
- larger than the actual state ontology.

These roles must not be conflated.

## 11. Relation to physical/statistical interpretations

The theorem does not say that nature samples `mu`, nor that infinite-support profiles physically exist.

It says only that if one summarizes the deterministic basin sequence by all finite split-coordinate frequencies, the unique compatible product law lives on the formal completion and is almost surely outside the actual point image.

Any physical interpretation would require additional modeling assumptions.

## 12. Foundation feedback

This gives Enterprise Math a concrete arithmetic example of a subtle but important pattern:

\[
\boxed{
\text{finite exact states}
\to
\text{dense projective completion}
\to
\text{canonical asymptotic measure}
}
\]

without the reverse implication

\[
\boxed{
\text{typical completion point}
\to
\text{actual primitive state}.
}
\]

So statistical completion can be an external derived object even when infinite completed states are not primitive ontology.

## 13. Prior-art and novelty discipline

Kolmogorov/product measure construction, Borel–Cantelli, weak convergence on compact product spaces, and cylinder-set determination are established mathematics.

The project-specific content is the deterministic split-shell arithmetic from L074 that produces this exact dense-null completion law.
