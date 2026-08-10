# Legendre Pressure Test — Supplement 32

Status: `PROVED RESEARCH NOTE`  
Scope: finite-prime asymptotic independence of split shells and density-one divergence of the global split count  
Depends on: P017 L072 fixed-prime density, multivariate equidistribution of rationally independent irrational rotations, Euler divergence of reciprocal primes  
Discipline: multidimensional Weyl/Kronecker equidistribution and multiquadratic linear independence are classical mathematics. The project-side theorem is their application to the exact L068/L069 split-shell events.

## 1. Fixed-prime densities suggest a stronger joint law

L072 proves that for every fixed prime `p`,

\[
I_p(k)
=
\mathbf1[\text{actual least-prime shell }p\text{ splits at basin }k]
\]

has natural density

\[
\frac1{\sqrt p}.
\]

The proof identifies the main event with the interval condition

\[
\left\{\frac{k}{\sqrt p}\right\}
\in
\left(1-\frac1{\sqrt p},1\right),
\]

up to a zero-density realizability boundary layer.

For several fixed primes, these interval conditions live on a finite torus.

## 2. Rational independence of the rotation frequencies

Fix distinct primes

\[
p_1,\ldots,p_m.
\]

Set

\[
\alpha_i=\frac1{\sqrt{p_i}}.
\]

Then

\[
\boxed{
1,\alpha_1,\ldots,\alpha_m
\text{ are linearly independent over }\mathbb Q.
}
\]

### Proof

Suppose

\[
a_0+\sum_{i=1}^m a_i\frac1{\sqrt{p_i}}=0
\]

with rational coefficients. Clear denominators and multiply by

\[
\sqrt{P},
\qquad
P=\prod_i p_i.
\]

This gives a rational linear relation among

\[
\sqrt P,
\quad
\sqrt{P/p_1},
\ldots,
\sqrt{P/p_m}.
\]

These are distinct square-root monomials in the multiquadratic extension

\[
\mathbb Q(\sqrt{p_1},\ldots,\sqrt{p_m}),
\]

whose standard monomial basis is indexed by subsets of the primes. Therefore all coefficients vanish. ∎

## 3. Multidimensional equidistribution

By the classical Kronecker/Weyl theorem, the sequence

\[
\boxed{
\left(
\{k\alpha_1\},\ldots,\{k\alpha_m\}
\right)
}
\]

is uniformly distributed in the torus

\[
[0,1)^m.
\]

For each prime define the core split interval

\[
J_p
=
\left(1-\frac1{\sqrt p},1\right),
\]

whose length is

\[
|J_p|=\frac1{\sqrt p}.
\]

L072 says the actual split event differs from membership in `J_p` only on a zero-density exceptional set.

## 4. P017-L074-A — Simultaneous split density for any fixed prime family

Status: `PROVED`.

For distinct fixed primes

\[
p_1,\ldots,p_m,
\]

the basin indices where **all** those least-prime shells split actually have natural density

\[
\boxed{
\delta\{k:I_{p_i}(k)=1\text{ for every }i\}
=
\prod_{i=1}^m\frac1{\sqrt{p_i}}.
}
\]

### Proof

The torus box

\[
J_{p_1}\times\cdots\times J_{p_m}
\]

has Lebesgue measure

\[
\prod_i|J_{p_i}|
=
\prod_i p_i^{-1/2}.
\]

Multidimensional equidistribution gives this density for the simultaneous core events.

Replacing each core event by the actual split event changes the intersection only inside the finite union of the fixed-prime zero-density exceptional sets from L072. Hence the density is unchanged. ∎

In particular, every prescribed finite set of least-prime shells splits simultaneously for infinitely many square basins, in fact for a positive-density set of basins.

## 5. P017-L074-B — Full finite split-pattern law

Status: `PROVED`.

Fix a finite prime set `P` and a pattern

\[
\varepsilon_p\in\{0,1\}
\qquad(p\in P).
\]

Then

\[
\boxed{
\delta\{k:I_p(k)=\varepsilon_p\ \forall p\in P\}
=
\prod_{p\in P}
\left(\frac1{\sqrt p}\right)^{\varepsilon_p}
\left(1-\frac1{\sqrt p}\right)^{1-\varepsilon_p}.
}
\]

The proof uses the torus rectangle in which coordinate `p` lies in `J_p` when `epsilon_p=1` and in its complement when `epsilon_p=0`, again ignoring only a finite union of zero-density boundary exceptions.

Thus the family of fixed-prime split indicators is asymptotically independent in every finite dimension.

This is a deterministic natural-density statement, not a probabilistic model imposed on the integers.

## 6. P017-L074-C — Finite-cutoff repair-support generating law

Let

\[
S_Y(k)
=
\sum_{p\le Y\atop p\text{ prime}}I_p(k).
\]

For fixed `Y`, L074-B says that under natural density `S_Y` has exactly the same limiting distribution as a sum of independent Bernoulli variables with parameters

\[
q_p=p^{-1/2}.
\]

Equivalently, for a formal variable `z`,

\[
\boxed{
\lim_{K\to\infty}
\frac1K\sum_{k\le K}z^{S_Y(k)}
=
\prod_{p\le Y}
\left(1-q_p+q_pz\right).
}
\]

This is a new generating law for the active factor-to-root repair support over moving square basins.

Its limiting mean and variance are

\[
\boxed{
\mu_Y
=
\sum_{p\le Y}\frac1{\sqrt p},
}
\]

and

\[
\boxed{
V_Y
=
\sum_{p\le Y}
\frac1{\sqrt p}
\left(1-\frac1{\sqrt p}\right).
}
\]

## 7. P017-L075-A — S(k) tends to infinity in natural density

Status: `PROVED`.

The full split count satisfies

\[
S(k)\ge S_Y(k)
\]

for every `k>=Y`.

Because

\[
\sum_p\frac1{\sqrt p}=\infty,
\]

we have

\[
\mu_Y\to\infty.
\]

Also

\[
V_Y\le\mu_Y.
\]

Fix any integer threshold `M`. For `Y` large enough that `mu_Y>M`, Chebyshev's inequality in the finite limiting density distribution gives

\[
\delta\{k:S_Y(k)<M\}
\le
\frac{V_Y}{(\mu_Y-M)^2}
\le
\frac{\mu_Y}{(\mu_Y-M)^2}.
\]

The right side tends to zero as `Y` grows.

Since `S(k)>=S_Y(k)`, for every `epsilon>0` one can choose a fixed `Y` such that

\[
\overline\delta\{k:S(k)<M\}<\epsilon.
\]

Therefore

\[
\boxed{
\delta\{k:S(k)\ge M\}=1
\qquad\text{for every fixed }M.
}
\]

Equivalently,

\[
\boxed{
S(k)\longrightarrow\infty
\quad\text{in natural density}.
}
\]

## 8. P017-L075-B — Every finite repair support occurs simultaneously on a positive-density set

A simpler but useful corollary of L074-A is: for any distinct primes

\[
p_1,\ldots,p_m,
\]

the set of basins where all `m` corresponding shells require the nontrivial root-repair bit has density

\[
\boxed{
\prod_{i=1}^{m}p_i^{-1/2}>0.
}
\]

Hence for every `m`,

\[
\boxed{
\{k:S(k)\ge m\}
}
\]

contains a positive-density subset.

L075-A strengthens this further to density one for the entire event `S(k)>=m`.

## 9. P017-L075-C — Local binary simplicity coexists with density-one global proliferation

L064 still says

\[
\rho(P,R)\le2.
\]

No individual factor shell ever needs more than one binary root-repair coordinate.

Yet L075 says that, for density-one many large basin indices, the number of factor shells that actually need this binary refinement exceeds every fixed bound.

Thus

\[
\boxed{
\text{uniformly bounded local repair alphabet}
}

coexists with

\[
\boxed{
\text{density-one divergence of active repair-support size}.
}
\]

This is a fundamental distinction between local precision width and global precision support complexity.

## 10. Consequence for the L067 repair polynomial

L067 gives

\[
K_k(t)
=(N_P(k)+S(k))t+S(k)t^2.
\]

L075 proves that the quadratic coefficient tends to infinity in natural density:

\[
\boxed{
[t^2]K_k(t)=S(k)\to\infty
\quad\text{in density}.
}
\]

So the relative repair polynomial becomes increasingly nontrivial on a density-one set of moving square basins even though its degree remains exactly two.

This is a useful new phenomenon:

\[
\boxed{
\text{bounded polynomial degree}
\not\Rightarrow
\text{bounded coefficient complexity}.
}
\]

## 11. Number-theoretic interpretation

The factor-to-root precision defect is now understood at three levels:

1. local shell degree is at most two;
2. each fixed prime shell splits with exact density `1/sqrt(p)`;
3. the total number of simultaneously active split shells tends to infinity in density.

Thus L067's repair statistic is not a finite-exception artifact. It is an asymptotically pervasive feature of the square-basin factor/root geometry.

## 12. Executable audit

- `src/enterprise_math/p017_split_pattern.py`
- `tests/test_p017_split_pattern.py`

The executable layer evaluates exact bounded split patterns and pins finite simultaneous examples. It is not used to prove the asymptotic independence theorem.

## 13. Prior-art boundary

Multidimensional irrational-rotation equidistribution, multiquadratic field bases, Bernoulli generating functions, Chebyshev's inequality, and reciprocal-prime divergence are established mathematics.

The project-specific theorem is the exact reduction of P017 split-shell events to these torus intervals after removing zero-density realizability boundary layers, producing a new deterministic asymptotic law for the repair spectrum.
