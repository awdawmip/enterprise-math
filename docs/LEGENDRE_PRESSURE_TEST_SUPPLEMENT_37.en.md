# Legendre Pressure Test — Supplement 37

Status: `PROVED RESEARCH NOTE`  
Scope: logarithmic exceptional set for fixed-prime split density  
Depends on: P017 L072 fixed-prime Beatty core, L068 branch-length formulas, classical generalized Pell orbit theory  
Discipline: generalized Pell equations and their fundamental-unit orbit structure are classical number theory. The project-side result is the exact localization of every fixed-prime realizability failure into finitely many such equations.

## 1. L072 gives density but not yet a quantitative error term

For fixed prime `p`, L072 proves

\[
\delta\{k:I_p(k)=1\}=\frac1{\sqrt p}.
\]

The main Beatty-core candidates are

\[
\mathcal B_p=\{\lfloor m\sqrt p\rfloor:m\ge1\},
\]

and actual realizability removes only a zero-density boundary layer.

Because `p` is fixed, that boundary layer can be sharpened to a finite family of Pell-type defects.

## 2. Fixed roughness guarantee

Let

\[
M_p=P_{<p}
=
\prod_{r<p\atop r\text{ prime}}r.
\]

Every interval of `M_p` consecutive integers contains a `p`-rough integer.

Therefore if a Beatty-core candidate `k` fails to split actually, at least one L068 raw branch has length below `M_p`.

Recall

\[
L_p=\left\lceil\frac{\tau_p}{p}\right\rceil-1,
\qquad
U_p=\left\lfloor\frac{2k-\tau_p}{p}\right\rfloor+1,
\]

where

\[
\tau_p=pm^2-k^2,
\qquad
k=\lfloor m\sqrt p\rfloor.
\]

## 3. P017-L082-A — Lower-side failures lie in finitely many negative Pell equations

Status: `PROVED`.

If

\[
L_p<M_p,
\]

then

\[
\left\lceil\frac{\tau_p}{p}\right\rceil\le M_p,
\]

so

\[
1\le\tau_p\le pM_p.
\]

Thus every lower-side failure satisfies

\[
\boxed{
k^2-pm^2=-N}
\]

for one integer

\[
\boxed{1\le N\le pM_p.}
\]

For fixed `p`, only finitely many negative generalized Pell equations occur.

## 4. P017-L082-B — Upper-side failures lie in finitely many positive Pell equations

Status: `PROVED`.

Inside the Beatty core define

\[
D=(k+1)^2-pm^2.
\]

Since

\[
D=2k+1-\tau_p,
\]

we have

\[
U_p
=
\left\lfloor\frac{D-1}{p}\right\rfloor+1
=
\left\lceil\frac Dp\right\rceil.
\]

If

\[
U_p<M_p,
\]

then

\[
1\le D\le p(M_p-1).
\]

Hence every upper-side failure satisfies

\[
\boxed{(k+1)^2-pm^2=N}
\]

for one integer

\[
\boxed{1\le N\le p(M_p-1).}
\]

Again only finitely many generalized Pell equations occur for fixed `p`.

## 5. Classical Pell orbit growth

For fixed nonsquare `p` and fixed nonzero integer `N`, the integer solutions of

\[
x^2-py^2=N
\]

form finitely many orbits under multiplication by powers of the fundamental unit of

\[
\mathbb Z[\sqrt p]
\]

(or the corresponding ring of integers).

Along each orbit the positive coordinates grow exponentially.

Therefore the number of solutions with

\[
|x|\le K
\]

is

\[
\boxed{O_{p,N}(\log K).}
\]

This standard Pell fact is the only non-elementary input needed for the quantitative exceptional bound.

## 6. P017-L082-C — Fixed-prime actual failures are logarithmically sparse

Status: `PROVED`.

Sections 3–4 place every actual split failure inside a finite union, depending only on `p`, of fixed generalized Pell equations.

Each contributes at most `O(log K)` solutions up to basin index `K`.

Hence

\[
\boxed{
\#\{k\le K:\ k\in\mathcal B_p\text{ but }I_p(k)=0\}
=O_p(\log K).
}
\]

So the p-rough realizability filter removes only logarithmically many Beatty-core candidates up to `K`.

This is much stronger than the density-zero statement in L072.

## 7. P017-L082-D — Quantitative fixed-prime split count

Status: `PROVED`.

The Beatty sequence count is exact:

\[
\#\{k\le K:k\in\mathcal B_p\}
=
\left\lfloor\frac{K+1}{\sqrt p}\right\rfloor.
\]

Discarding the finitely many initial indices with `k<p` changes the count only by `O_p(1)`. Removing the actual-realizability failures costs `O_p(log K)` by T03.

Therefore

\[
\boxed{
\sum_{k\le K}I_p(k)
=
\left\lfloor\frac{K+1}{\sqrt p}\right\rfloor
+O_p(\log K)
}
\]

and hence

\[
\boxed{
\sum_{k\le K}I_p(k)
=
\frac{K}{\sqrt p}+O_p(\log K).
}
\]

The constant may be very large because it depends on the fixed primorial `M_p`; no useful uniformity in growing `p` is claimed.

## 8. P017-L082-E — Raw and realized fixed-prime split counts differ by O_p(log K)

The raw Beatty/root geometry and the actual p-rough shell geometry therefore agree for all but logarithmically many basin indices up to `K`:

\[
\boxed{
\#\{k\le K:\ I_p^{\rm raw}(k)\ne I_p(k)\}
=O_p(\log K).
}
\]

Thus, for each fixed prime shell, the envelope-to-realizability correction is quantitatively tiny on the basin-index axis even though individual false raw states are mathematically important.

## 9. Why this does not yet give a growing-prime uniform theorem

The finite set of Pell defects extends up to sizes on the order of

\[
pM_p,
\]

and `M_p` is a primorial that grows rapidly with `p`.

Accordingly, the implied `O_p` constant is not controlled uniformly as `p` grows.

Therefore L082 does **not** justify replacing the iterated-limit statements of L074–L079 by a simultaneous theorem with prime cutoff `Y=Y(K)`.

A genuinely uniform result would require new control over these growing families of Pell/roughness exceptions or a different sieve argument.

This remains a sharp open boundary.

## 10. Relation to the equidistribution proof

L072 used irrational-rotation equidistribution to show the exceptional boundary layers have density zero.

L082 gives a different, arithmetic explanation of the same phenomenon:

\[
\boxed{
\text{short boundary branch}
\Longrightarrow
\text{bounded Pell defect}
\Longrightarrow
O_p(\log K)\text{ exceptions}.
}
\]

The two proofs are complementary:

- equidistribution is structurally simple and extends naturally to finite-prime joint laws;
- Pell localization is one-dimensional but quantitative for each fixed prime.

## 11. Executable audit

- `src/enterprise_math/p017_fixed_prime_split_exceptions.py`
- `tests/test_p017_fixed_prime_split_exceptions.py`

The executable layer classifies every bounded Beatty-core failure by its lower or upper Pell defect and checks the exact finite defect bounds. It does not prove the classical logarithmic orbit-count theorem.

## 12. Tool feedback

This stage illustrates another reusable research pattern:

\[
\boxed{
\text{density proof via equidistribution}
\to
\text{boundary localization}
\to
\text{Diophantine defect equations}
\to
\text{quantitative exceptional bound}.
}
\]

A coarse asymptotic statement can therefore be sharpened by identifying the exact arithmetic equations that encode its rare failures.
