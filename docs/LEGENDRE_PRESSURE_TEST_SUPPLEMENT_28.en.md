# Legendre Pressure Test — Supplement 28

Status: `PROVED RESEARCH NOTE`  
Scope: exact Mobius representation of the split-shell statistic and a Jacobsthal-type occupancy certificate  
Depends on: P017 L068–L069 inputs, canonical P017 Mobius tools, p-rough cofactor semantics  
Discipline: finite inclusion-exclusion, primorial coprimality, and Jacobsthal functions are classical number theory. This supplement only specializes them to the exact P017 root-split intervals.

## 1. Realizability is coprimality to a finite primorial

Fix a prime `p` and define

\[
\boxed{
P_{<p}
=
\prod_{r<p\atop r\text{ prime}} r.
}
\]

For every positive integer `q`,

\[
\boxed{
q\text{ is }p\text{-rough}
\iff
\gcd(q,P_{<p})=1.
}
\]

Indeed, `q` fails to be `p`-rough exactly when it has a prime divisor smaller than `p`, equivalently when it shares a prime factor with `P_{<p}`.

Thus the realizability filter in L068 is an exact finite reduced-residue condition.

## 2. P017-L069-A — Exact Mobius count on any p-rough interval

Status: `PROVED`.

For a positive integer interval

\[
[a,b],
\qquad
1\le a\le b,
\]

define

\[
R_p[a,b]
=
\#\{q\in[a,b]:q\text{ is }p\text{-rough}\}.
\]

Then inclusion-exclusion gives

\[
\boxed{
R_p[a,b]
=
\sum_{d\mid P_{<p}}
\mu(d)
\left(
\left\lfloor\frac bd\right\rfloor
-
\left\lfloor\frac{a-1}{d}\right\rfloor
\right).
}
\]

### Proof

For square-free `P_{<p}`,

\[
\mathbf1_{\gcd(q,P_{<p})=1}
=
\sum_{d\mid\gcd(q,P_{<p})}\mu(d).
\]

Sum over `q in [a,b]` and interchange the finite sums. The number of `q` divisible by `d` in the interval is exactly

\[
\left\lfloor\frac bd\right\rfloor
-
\left\lfloor\frac{a-1}{d}\right\rfloor.
\]

∎

No asymptotic sieve approximation is involved.

## 3. Apply the formula to the two L068 root branches

For each prime `p<=k`, let

\[
W_p^-
\]

and

\[
W_p^+
\]

be the lower and upper root subwindows from L068, separated by the boundary quotient `m_p^2`.

Define

\[
\boxed{
R_p^-(k)=R_p[W_p^-],
\qquad
R_p^+(k)=R_p[W_p^+],
}
\]

with empty intervals assigned count zero.

These are explicit finite Mobius sums determined entirely by `k,p`.

## 4. P017-L069-B — Exact Mobius positivity criterion for a split shell

Status: `PROVED`.

By L068, the actual least-prime shell realizes both cofactor-root branches exactly when each branch contains at least one `p`-rough quotient.

Therefore

\[
\boxed{
r_p=2
\iff
R_p^-(k)>0
\text{ and }
R_p^+(k)>0.
}
\]

Equivalently, the split bit is

\[
\boxed{
\beta_p^{\rm split}(k)
=
\mathbf1[R_p^-(k)>0]\,
\mathbf1[R_p^+(k)>0].
}
\]

This turns the realizability part of the root-split theorem into two exact local inclusion-exclusion signs.

## 5. P017-L069-C — Exact Mobius formula for the second repair-spectrum coordinate

Status: `PROVED`.

L067 identifies

\[
S(k)=\sum_{p\le k}\mathbf1[r_p=2].
\]

Using L069-B,

\[
\boxed{
S(k)
=
\sum_{p\le k\atop p\text{ prime}}
\mathbf1[R_p^-(k)>0]\,
\mathbf1[R_p^+(k)>0].
}
\]

Each `R_p^±` is the explicit finite Mobius sum from L069-A.

Hence the P011/P023 second relative repair-spectrum coordinate is now written entirely in classical finite sieve arithmetic.

The difficulty is no longer defining the quantity; it is controlling the simultaneous positivity of these short moving rough intervals.

## 6. Relation to the overshoot criterion

If the L068 raw overshoot gate fails,

\[
p<\tau_p\le2k
\]

is false, then one of the two subwindows is empty and the corresponding Mobius count is zero automatically.

Thus one may also write

\[
\boxed{
S(k)
=
\sum_{p\le k\atop p\text{ prime}}
\mathbf1[p<\tau_p\le2k]
\mathbf1[R_p^-(k)>0]
\mathbf1[R_p^+(k)>0].
}
\]

This makes the two layers explicit:

1. exact quotient/root geometry decides whether two raw branches exist;
2. exact sieve arithmetic decides whether each branch contains a realizable least-prime state.

## 7. The k=6,p=3 correction becomes one zero Mobius count

At `k=6,p=3`, L068 says the raw window crosses the root boundary.

The upper raw branch consists only of the quotient

\[
q=16.
\]

Since

\[
P_{<3}=2
\]

and `gcd(16,2)>1`,

\[
\boxed{R_3^+(6)=0.}
\]

The lower branch has positive rough count, but the product of the two positivity bits is zero.

So the false raw collision is removed by one exact local Mobius cancellation.

## 8. Jacobsthal-type sufficient occupancy certificate

Let `j(n)` denote the classical Jacobsthal function in the convention:

> `j(n)` is the smallest positive integer `m` such that every interval of `m` consecutive integers contains an integer coprime to `n`.

Then any interval of length at least

\[
j(P_{<p})
\]

must contain a `p`-rough integer.

Therefore L068's raw slot counts give a sufficient split certificate:

\[
\boxed{
L_p\ge j(P_{<p})
\quad\text{and}\quad
U_p\ge j(P_{<p})
\Longrightarrow
r_p=2.
}
\]

Equivalently, if a raw split fails realizability on one side, that empty rough side must have length strictly below the relevant Jacobsthal guarantee.

This is a sufficient certificate only. Shorter intervals may still contain p-rough integers.

## 9. Why the Jacobsthal bridge matters

L068 separates the problem into a moving boundary and rough occupancy. L069 now gives two ways to attack occupancy:

- **exact mode:** evaluate the finite Mobius count;
- **guarantee mode:** use a Jacobsthal upper bound to certify positivity from interval length alone.

This creates a clean interface to established covering/gap results without changing the P017 state semantics.

It also prevents a common mistake: a Jacobsthal bound is a worst-case interval guarantee, not the exact rough count in the particular moving subwindow.

## 10. Complexity boundary

The direct Mobius formula has one term for every square-free divisor of `P_{<p}`, hence exponential size in the number of primes below `p` if expanded naively.

This does not invalidate the theorem; it says that the exact closed expression is not automatically the best executable algorithm.

Existing P017 rough/Buchstab recursion, CRT compression, Bonferroni truncation, or Jacobsthal bounds may provide cheaper proof certificates depending on the task.

Thus the research-tool distinction remains:

\[
\boxed{
\text{exact semantic formula}
\neq
\text{optimal proof algorithm}.
}
\]

## 11. Executable specification

- `src/enterprise_math/rough_interval_mobius.py`
- `src/enterprise_math/p017_root_split_mobius.py`
- `tests/test_p017_root_split_mobius.py`

The executable layer compares the Mobius count to a direct gcd oracle on bounded intervals, reconstructs the L067 split-shell set from Mobius positivity alone, and pins the `k=6,p=3` zero-upper-count correction.

## 12. Prior-art boundary

Primorial coprimality, Mobius inclusion-exclusion, and Jacobsthal's function are established number theory. They are not Enterprise Math inventions.

The project-specific contribution is the exact identification of the L067 repair-spectrum coefficient with positivity of **two specific moving primorial-coprime interval counts** generated by the quotient-root overshoot calculus.
