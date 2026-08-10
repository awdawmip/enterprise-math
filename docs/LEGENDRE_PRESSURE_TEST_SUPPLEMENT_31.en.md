# Legendre Pressure Test — Supplement 31

Status: `PROVED RESEARCH NOTE`  
Scope: fixed-prime split density and unbounded global split-shell spectrum  
Depends on: P017 L068–L070, finite primorial roughness, classical equidistribution of irrational rotations  
Discipline: Beatty-sequence counting, equidistribution of multiples of an irrational, and divergence of the reciprocal-prime series are classical mathematics. The new project-side result is their exact application to the L067 split-shell repair statistic.

## 1. Fix one least prime and vary the square basin

Fix a prime

\[
p.
\]

For every sufficiently large basin index `k>=p`, let

\[
I_p(k)
=
\mathbf1[\text{the realized least-prime shell }p\text{ splits across two cofactor roots}].
\]

L068 expresses this through the next p-weighted square boundary and p-rough occupancy.

The first result of this supplement is that `I_p(k)=1` has an exact natural density.

## 2. Beatty core of the raw upper split condition

Set

\[
\alpha=\sqrt p.
\]

Because `p` is prime, `alpha` is irrational.

Let

\[
m=m_p(k)=\left\lceil\frac{k}{\sqrt p}\right\rceil.
\]

Equivalently, `m` is the least integer with

\[
pm^2>k^2.
\]

Write

\[
\tau_p=pm^2-k^2.
\]

L068 says the upper raw branch exists exactly when

\[
\tau_p\le2k.
\]

But

\[
\tau_p\le2k
\iff
pm^2\le k^2+2k
\iff
pm^2<(k+1)^2.
\]

Together with `pm^2>k^2`, this is

\[
\boxed{
k<m\sqrt p<k+1.}
\]

Hence

\[
\boxed{
\tau_p\le2k
\iff
k=\lfloor m\sqrt p\rfloor.
}
\]

So the raw upper-bound candidates are exactly the Beatty sequence

\[
\boxed{
\mathcal B_p
=
\{\lfloor m\sqrt p\rfloor:m\ge1\}.
}
\]

## 3. P017-L072-A — The Beatty core has density 1/sqrt(p)

Status: `PROVED`.

Because `sqrt(p)>1`, the Beatty sequence is strictly increasing.

The number of its elements not exceeding `K` is exactly the number of positive integers `m` satisfying

\[
m\sqrt p<K+1,
\]

namely

\[
\left\lfloor\frac{K+1}{\sqrt p}\right\rfloor.
\]

Therefore

\[
\boxed{
\delta(\mathcal B_p)
=
\frac1{\sqrt p}.
}
\]

No prime-distribution theorem is used here.

## 4. Actual split failures are confined to fixed-width roughness boundary layers

Let

\[
P_{<p}
=
\prod_{r<p\atop r\text{ prime}}r.
\]

Call this fixed primorial `M_p`.

Every interval of `M_p` consecutive integers contains an integer congruent to `1 mod M_p`, hence contains a `p`-rough integer.

Therefore if a Beatty-core candidate fails to split **actually**, at least one L068 branch must have raw length strictly below `M_p`.

Let

\[
L_p
=
\left\lceil\frac{\tau_p}{p}\right\rceil-1,
\qquad
U_p
=
\left\lfloor\frac{2k-\tau_p}{p}\right\rfloor+1.
\]

Then actual failure inside `B_p` implies

\[
L_p<M_p
\quad\text{or}\quad
U_p<M_p.
\]

## 5. Lower-boundary failures force fractional part near zero

Write

\[
\delta_m
=
\{m\sqrt p\}
=
m\sqrt p-k
\]

for `k=floor(m sqrt(p))`.

Since

\[
\tau_p
=(m\sqrt p-k)(m\sqrt p+k),
\]

we have

\[
\boxed{
\delta_m
=
\frac{\tau_p}{m\sqrt p+k}.
}
\]

If `L_p<M_p`, then

\[
\tau_p\le pM_p.
\]

Hence

\[
0<\delta_m
\le
\frac{pM_p}{m\sqrt p+k}
<
\frac{pM_p}{2k}.
\]

Thus lower-side failures occur only when the irrational rotation point `{m sqrt(p)}` lies within `O_p(1/k)` of zero.

## 6. Upper-boundary failures force fractional part near one

Let

\[
\varepsilon_m
=1-\delta_m
=k+1-m\sqrt p.
\]

Then

\[
(k+1)^2-pm^2
=
\varepsilon_m(k+1+m\sqrt p).
\]

If `U_p<M_p`, then from the L068 formula

\[
0\le2k-\tau_p<p(M_p-1),
\]

so

\[
1\le(k+1)^2-pm^2\le p(M_p-1).
\]

Therefore

\[
0<1-\delta_m
\le
\frac{p(M_p-1)}{k+1+m\sqrt p}
=O_p(1/k).
\]

Thus upper-side failures occur only when `{m sqrt(p)}` lies in an `O_p(1/k)` neighborhood of one.

## 7. P017-L072-B — Actual fixed-prime split density is exactly 1/sqrt(p)

Status: `PROVED`, using classical equidistribution of irrational rotations.

The sequence

\[
\{m\sqrt p\}
\]

is uniformly distributed in `[0,1)` because `sqrt(p)` is irrational.

For any fixed `epsilon>0`, once `k` is large enough the exceptional boundary layers from Sections 5–6 are contained in

\[
[0,\epsilon)
\cup
(1-\epsilon,1).
\]

Uniform distribution gives asymptotic relative frequency at most `2 epsilon` among the `m` parameters. Since the Beatty map `m -> floor(m sqrt(p))` is injective and scales counts linearly, the corresponding exceptional `k` set has upper natural density at most a constant multiple of `epsilon`.

Letting `epsilon ->0` shows that Beatty-core candidates failing actual p-rough splitting have density zero.

Therefore removing all actual-realizability exceptions from `B_p` does not change its density:

\[
\boxed{
\delta\{k:I_p(k)=1\}
=
\frac1{\sqrt p}.
}
\]

This is the fixed-prime split-density theorem.

## 8. Interpretation

For every fixed least prime `p`, as the square basin moves outward, the shell `p` actually needs the nontrivial factor-to-root repair bit for a positive fraction

\[
\boxed{1/\sqrt p}
\]

of all basin indices.

The realizability filter removes infinitely many possible exceptional states, but only a zero-density set of basin indices for each fixed `p`.

This is much stronger than bounded computation of individual split events.

## 9. P017-L073-A — The mean number of split shells diverges

Status: `PROVED`.

Recall

\[
S(k)=\sum_{p\le k\atop p\text{ prime}} I_p(k).
\]

Fix any finite prime cutoff `Y`. For large `K`,

\[
\frac1K\sum_{k\le K}S(k)
\ge
\frac1K\sum_{k\le K}\sum_{p\le Y}I_p(k).
\]

Because the prime set `p<=Y` is finite, L072-B allows termwise passage to the limit:

\[
\liminf_{K\to\infty}
\frac1K\sum_{k\le K}S(k)
\ge
\sum_{p\le Y}\frac1{\sqrt p}.
\]

Now the classical Euler theorem says

\[
\sum_p\frac1p
\]

diverges. Since

\[
\frac1{\sqrt p}\ge\frac1p,
\]

we also have

\[
\sum_p\frac1{\sqrt p}=\infty.
\]

Letting `Y` grow therefore gives

\[
\boxed{
\frac1K\sum_{k\le K}S(k)
\longrightarrow
\infty.
}
\]

So the Cesaro mean of the split-shell count diverges.

## 10. P017-L073-B — S(k) is unbounded

Status: `PROVED`.

If `S(k)` were bounded by a constant `C`, then every Cesaro average would also be at most `C`.

This contradicts L073-A.

Hence

\[
\boxed{
\sup_k S(k)=\infty.
}
\]

Thus L067's second relative repair-spectrum coefficient is rigorously unbounded.

## 11. P017-L073-C — Bounded local alphabet, unbounded global repair-spectrum mass

L064 gives the universal local bound

\[
\boxed{
\rho(P,R)\le2.
}
\]

So one binary repair symbol is always enough **inside any individual least-prime shell**.

But L067 identifies

\[
\mathcal R_2(P\leftarrow P\cap R)=S(k),
\]

and L073-B proves this quantity unbounded.

Therefore

\[
\boxed{
\text{maximum local repair alphabet is uniformly bounded}
}
\]

while

\[
\boxed{
\text{global number of coarse fibers requiring that repair is unbounded}.
}
\]

These are mathematically distinct notions of precision complexity.

## 12. Consequence for fixed rectangular state formats

A representation that reserves one repair bit for every factor shell uses capacity proportional to the number of factor shells, even though only `S(k)` shells actually split.

L073 says `S(k)` itself grows without a uniform bound, so the set of genuinely active bit-bearing shells cannot be confined to one finite exceptional catalogue.

At the same time, the alphabet per active shell remains binary.

Thus the natural long-range state is sparse/local rather than one globally widening digit:

\[
\boxed{
\text{many locally binary defects}
\neq
\text{one large local alphabet}.
}
\]

## 13. Executable audit

- `src/enterprise_math/p017_fixed_prime_split_density.py`
- `tests/test_p017_fixed_prime_split_density.py`

The finite audit verifies the integer Beatty-core equivalence, checks that every bounded actual failure lies in the fixed primorial boundary layer, and records fixed-prime split counts through `k=5000` for several small primes. These computations are regression only; the density theorem uses equidistribution.

## 14. Prior-art boundary

Beatty sequences, equidistribution of irrational rotations, primorial coprimality, and divergence of the reciprocal-prime series are classical results and are not claimed as Enterprise Math inventions.

The new project-side theorem is their combination with the exact P017 overshoot/rough-occupancy calculus to prove fixed-prime repair density and the unboundedness of the global second repair-spectrum coordinate.
