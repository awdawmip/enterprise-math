# Legendre Pressure Test — Supplement 35

Status: `PROVED RESEARCH NOTE`  
Scope: sparse proliferation, concentration, and a deterministic-density CLT for fixed-prime split support  
Depends on: P017 L074 finite-prime split-pattern law, classical PNT/partial summation, and the Lindeberg central limit theorem  
Discipline: every asymptotic statement is an **iterated limit**: first basin index `k -> infinity` for a fixed prime cutoff `Y`, then `Y -> infinity`. No uniform theorem with a growing cutoff `Y=Y(k)` is claimed.

## 1. Fixed-cutoff active repair support

For a finite prime cutoff `Y`, define

\[
\boxed{
S_Y(k)
=\sum_{p\le Y\atop p\text{ prime}}I_p(k),
}
\]

where `I_p(k)` is the actual split-shell indicator from L072.

L074 proves that, in natural density over `k`, the finite vector `(I_p)_{p<=Y}` has exactly the product Bernoulli law with parameters

\[
q_p=\frac1{\sqrt p}.
\]

Therefore the limiting mean and variance of `S_Y` are

\[
\boxed{
\mu_Y
=\sum_{p\le Y}\frac1{\sqrt p},
}
\]

and

\[
\boxed{
V_Y
=\sum_{p\le Y}
\frac1{\sqrt p}
\left(1-\frac1{\sqrt p}\right).
}
\]

These are exact natural-density moments for each fixed `Y`.

## 2. P017-L078-A — Mean active support has square-root prime-density scale

Status: `PROVED`, using the prime number theorem and partial summation.

The prime number theorem gives

\[
\pi(x)\sim\frac{x}{\log x}.
\]

Partial summation yields

\[
\sum_{p\le Y}p^{-1/2}
\sim
\int_2^Y\frac{dt}{\sqrt t\log t}.
\]

With `u=sqrt(t)`,

\[
\int_2^Y\frac{dt}{\sqrt t\log t}
=
\int_{\sqrt2}^{\sqrt Y}\frac{du}{\log u}
\sim
\frac{\sqrt Y}{\log\sqrt Y}
=
\frac{2\sqrt Y}{\log Y}.
\]

Hence

\[
\boxed{
\mu_Y
\sim
\frac{2\sqrt Y}{\log Y}.
}
\]

So the expected number of active split shells among fixed primes up to `Y` diverges on a square-root scale.

## 3. P017-L078-B — Active proportion tends to zero

Status: `PROVED`.

The number of available fixed prime tasks is

\[
\pi(Y)
\sim
\frac{Y}{\log Y}.
\]

Therefore

\[
\boxed{
\frac{\mu_Y}{\pi(Y)}
\sim
\frac{2}{\sqrt Y}
\longrightarrow0.
}
\]

Thus the repair support exhibits **sparse proliferation**:

\[
\boxed{
\mu_Y\to\infty
\quad\text{but}\quad
\mu_Y/\pi(Y)\to0.
}
\]

More split shells are simultaneously active, yet they occupy a vanishing fraction of the growing fixed-prime coordinate family.

## 4. Variance has the same leading scale as the mean

We have

\[
V_Y
=
\mu_Y-
\sum_{p\le Y}\frac1p.
\]

The classical reciprocal-prime sum grows only logarithmically:

\[
\sum_{p\le Y}\frac1p
=
\log\log Y+O(1).
\]

Since

\[
\mu_Y\sim\frac{2\sqrt Y}{\log Y},
\]

the correction is negligible. Therefore

\[
\boxed{
V_Y\sim\mu_Y
\sim\frac{2\sqrt Y}{\log Y}.
}
\]

In particular,

\[
\boxed{
\frac{V_Y}{\mu_Y^2}
\longrightarrow0.
}
\]

## 5. P017-L078-C — Relative concentration in natural density

Status: `PROVED`.

Fix `epsilon>0`. For every fixed `Y`, L074 gives an exact finite Bernoulli product distribution in natural density. Chebyshev therefore gives

\[
\delta\left\{
 k:
 |S_Y(k)-\mu_Y|\ge\epsilon\mu_Y
\right\}
\le
\frac{V_Y}{\epsilon^2\mu_Y^2}.
\]

By Section 4 the right side tends to zero with `Y`.

Hence

\[
\boxed{
\lim_{Y\to\infty}
\delta\left\{
 k:
 \left|\frac{S_Y(k)}{\mu_Y}-1\right|<\epsilon
\right\}
=1.
}
\]

Equivalently, in the iterated-limit sense,

\[
\boxed{
S_Y(k)
\sim
\frac{2\sqrt Y}{\log Y}
}
\]

for a density-one set of basin indices at each sufficiently large fixed cutoff.

This sharpens L075's qualitative density-one divergence.

## 6. P017-L078-D — Sparse support concentration

Combining Sections 3 and 5, for every fixed `epsilon>0`, density-one many basin indices satisfy

\[
S_Y(k)
=(1+o_Y(1))\mu_Y,
\]

while

\[
\frac{S_Y(k)}{\pi(Y)}
\to0
\]

in the same iterated-density sense.

Thus the typical finite-prime repair state has

\[
\boxed{
\text{unbounded support size}
\quad\text{and}\quad
\text{vanishing support density}.
}
\]

This gives a precise asymptotic meaning to the sparse/local state picture suggested by S20.

## 7. P017-L079-A — Deterministic-density central limit theorem

Status: `PROVED`, using the classical Lindeberg/Feller CLT for bounded independent triangular arrays.

For fixed `Y`, the limiting natural-density law of

\[
S_Y
\]

is the Poisson-binomial sum of independent Bernoulli variables with parameters `q_p=p^{-1/2}`.

The centered summands are uniformly bounded by one, while

\[
V_Y\to\infty.
\]

Therefore the Lindeberg condition is automatic: for every fixed `epsilon>0`, once

\[
\epsilon\sqrt{V_Y}>1,
\]

no individual centered summand can exceed the Lindeberg threshold.

Hence

\[
\boxed{
\frac{S_Y-\mu_Y}{\sqrt{V_Y}}
\Rightarrow
N(0,1)
}
\]

as `Y -> infinity` in the finite-cutoff limiting distributions.

Translated back to natural density: for every real `x`,

\[
\boxed{
\lim_{Y\to\infty}
\left[
\lim_{K\to\infty}
\frac1K
\#\left\{
 k\le K:
 \frac{S_Y(k)-\mu_Y}{\sqrt{V_Y}}
\le x
\right\}
\right]
=
\Phi(x),
}
\]

where `Phi` is the standard normal distribution function.

This is a deterministic arithmetic density theorem; randomness enters only as the standard language for the limiting product distribution already determined by L074.

## 8. P017-L079-B — Fluctuation scale

Since

\[
V_Y\sim\mu_Y,
\]

the standard deviation is

\[
\boxed{
\sqrt{V_Y}
\sim
\sqrt{\frac{2\sqrt Y}{\log Y}}.
}
\]

Thus absolute fluctuations grow, but relative fluctuations satisfy

\[
\frac{\sqrt{V_Y}}{\mu_Y}
\to0.
\]

This is exactly compatible with sparse proliferation plus concentration.

## 9. Why this does not prove a growing-cutoff theorem

The order of limits is essential.

L074 gives natural-density laws for each **fixed finite** prime family. The argument above first takes

\[
K\to\infty
\]

with `Y` fixed, and only afterward lets

\[
Y\to\infty.
\]

It does **not** show that for an arbitrary function `Y=Y(k)`,

\[
S_{Y(k)}(k)
\sim
2\sqrt{Y(k)}/\log Y(k)
\]

for most individual `k`.

Such a result would require uniform discrepancy/equidistribution control while the torus dimension and prime cutoff grow. No such estimate is supplied here.

This limitation is a genuine boundary, not a technical footnote.

## 10. Repair-spectrum interpretation

For fixed cutoff `Y`, let `S_Y(k)` count only split shells with `p<=Y`.

This is the truncated second repair-spectrum mass contributed by those fixed prime coordinates.

L078–L079 show that, across moving basins, this repair-support mass has:

- mean `~2 sqrt(Y)/log Y`;
- vanishing active fraction `~2/sqrt(Y)`;
- relative concentration;
- Gaussian fluctuations after standardization.

Meanwhile every active local shell remains binary by L064.

This is a precise statistical law for a deterministic finite-precision defect system.

## 11. Foundation feedback

The result adds a new distinction to finite precision complexity:

\[
\boxed{
\text{local alphabet width}
\quad+
\text{global support size}
\quad+
\text{support density}
\quad+
\text{support fluctuations}.
}
\]

A scalar precision width misses all but the first of these.

## 12. Prior-art and novelty discipline

The PNT, partial summation, Mertens' reciprocal-prime estimate, Chebyshev concentration, and the Lindeberg CLT are established results.

The project-specific result is the deterministic split-shell arithmetic supplied by L074, which makes these classical tools produce an exact asymptotic law for the P017 repair-support statistic.
