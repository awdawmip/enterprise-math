# P018 — Finite-Precision Proof Calculus, Supplement 03

Status: `ACTIVE RESEARCH NOTE`  
Scope: factor precision as a second precision axis; exact bridge from P018 to the P017 Legendre pressure test  
Discipline: prime sieving and least-prime-factor partitions are classical; the new question is their role inside a general finite-precision proof calculus.

## 1. Precision is not only numerical scale

P018 Stages 1–3 used positive integer scale factors as the precision coordinate.

That is only one possible finite precision system.

A proof can gain information along other finite axes.  The Legendre pressure test already contains one:

> how far have we searched for a prime divisor?

For a positive integer `n` and a factor cutoff `y`, define the **factor-precision state**

\[
D_y(n)
=
\{p\le y:p\text{ prime and }p\mid n\}.
\]

This state records the divisibility witnesses that have become visible by precision `y`.

## 2. P018-T29 — Factor-precision projection compatibility

Status: `PROVED`

If

\[
y\le z,
\]

then the high factor-precision state projects to the lower one by forgetting witnesses above `y`:

\[
\boxed{
\pi_{z\to y}(D_z(n))
=
D_z(n)\cap\{p:p\le y\}
=
D_y(n).
}
\]

Consequently, for

\[
x\le y\le z,
\]

projection composes exactly:

\[
\pi_{z\to x}
=
\pi_{y\to x}\circ\pi_{z\to y}.
\]

Thus factor cutoff is a genuine finite precision chain with compatible many-to-one forgetting maps.

No numerical scale factor is involved.

## 3. P018-T30 — Persistent factor certificates

Status: `PROVED`

At factor precision `y`, use three proof states:

- `COMPOSITE` if `D_y(n)` is nonempty;
- `UNRESOLVED` if `D_y(n)` is empty and the known completeness horizon has not yet been reached;
- `PRIME` if `D_y(n)` is empty and a proved finite completeness horizon has been reached.

If a factor witness appears at precision `y`, it remains present at every higher precision:

\[
\boxed{
D_y(n)\ne\varnothing
\Longrightarrow
D_z(n)\ne\varnothing
\qquad(z\ge y).
}
\]

Hence a COMPOSITE certificate is permanent.

This is exactly the P018 Stage-3 proof-persistence rule on a new precision axis.

## 4. P018-T31 — Square-basin factor horizon is a finite PRIME certificate

Status: `PROVED`

Let

\[
k^2<n<(k+1)^2.
\]

The P017 Root-Factor Horizon gives

\[
n\text{ composite}
\iff
\exists p\le k,\ p\text{ prime},\ p\mid n.
\]

Therefore

\[
\boxed{
D_k(n)=\varnothing
\iff
n\text{ is prime}.
}
\]

So factor precision does not need to increase without bound.  The finite precision

\[
\boxed{y=k}
\]

is complete for primality on this entire square basin.

The proof process is therefore:

\[
\text{UNRESOLVED}
\to
\text{COMPOSITE}
\]

as soon as a witness appears, or

\[
\text{UNRESOLVED}
\to
\text{PRIME}
\]

at the terminal finite horizon `k` if no witness ever appears.

This is a direct exact bridge between P017 and P018.

## 5. P018-T32 — Factor survivors decrease with precision

Status: `PROVED`

Define the factor survivors in the open square basin by

\[
S_y(k)
=
\{n:k^2<n<(k+1)^2,\ D_y(n)=\varnothing\}.
\]

If

\[
y\le z,
\]

then

\[
\boxed{S_z(k)\subseteq S_y(k).}
\]

Therefore

\[
\boxed{|S_z(k)|\le |S_y(k)|.}
\]

At the finite terminal horizon,

\[
\boxed{
S_k(k)
=
\{p:p\text{ prime},\ k^2<p<(k+1)^2\}.
}
\]

Hence the P017 prime count has the precision interpretation

\[
\boxed{
\Pi(k)=|S_k(k)|.
}
\]

Legendre's conjecture is exactly the assertion

\[
\boxed{|S_k(k)|\ge1\quad\text{for every }k\ge1.}
\]

P018 has not proved that inequality; it has identified P017's sieve dynamics as a finite proof-precision process.

## 6. P018-T33 — First-witness precision shells

Status: `PROVED`

For each prime `p<=k`, define

\[
L_p(k)
=
\{n:k^2<n<(k+1)^2,\ \operatorname{spf}(n)=p\}.
\]

Equivalently,

\[
n\in L_p(k)
\]

if and only if `n` has no prime factor below `p` and becomes COMPOSITE exactly when factor precision reaches `p`.

The sets `L_p(k)` are pairwise disjoint.

Every composite in the basin belongs to exactly one such shell because its least prime factor is at most `k`.

Therefore

\[
\boxed{
I_k
=
\left(
\mathop{\bigsqcup}_{p\le k}L_p(k)
\right)
\sqcup
S_k(k),
}
\]

where `I_k` is the open square basin.

This is a **first-witness precision-shell decomposition**.

Unlike the signed Möbius shells in the original P017 inclusion-exclusion route, these shells are nonnegative and disjoint because each composite is assigned to its first proof witness.

This does not remove the hard number theory: counting `L_p(k)` exactly already requires excluding all smaller prime factors.  The parity problem is reorganized, not magically solved.

## 7. P018-T34 — Exact P017/P018 bridge identity

Status: `PROVED`

The open square basin has exactly

\[
2k
\]

states.

T33 gives

\[
2k
=
\sum_{p\le k}|L_p(k)|
+
|S_k(k)|.
\]

Using T32,

\[
|S_k(k)|=\Pi(k).
\]

Hence

\[
\boxed{
\Pi(k)
=
2k-\sum_{p\le k}|L_p(k)|.
}
\]

P017 separately proved the signed carry identity

\[
\Pi(k)
=
2+
\sum_{d\mid P_k}\mu(d)\kappa_d(k).
\]

Therefore the two precision descriptions obey the exact bridge

\[
\boxed{
2+
\sum_{d\mid P_k}\mu(d)\kappa_d(k)
=
2k-\sum_{p\le k}|L_p(k)|.
}
\]

This equality does not prove Legendre.  It says that:

- the original P017 side measures the final survivor count by signed overlap cancellation;
- the P018 factor-precision side measures the same survivor count by disjoint first-witness exit shells.

This is the first rigorous statement that a nontrivial P017 object is an instance of P018 precision dynamics rather than merely an analogy.

## 8. Two different precision axes now coexist

P018 now has at least two mathematically distinct precision coordinates.

### Scale precision

A state is refined by increasing an integer scale factor under divisibility.  Projection is Euclidean quotient and each fiber has a bounded numerical detail.

### Factor precision

A proof state is refined by increasing the tested prime-factor horizon.  Projection forgets high-cutoff witnesses and the new detail is a newly visible divisibility witness set.

The common abstract structure is not the arithmetic formula for detail.  It is:

\[
\boxed{
\text{finite precision levels}
+
\text{compatible forgetting maps}
+
\text{nested fibers/information}
+
\text{persistent certificates}.
}
\]

This strongly suggests that the next P018 layer should be an abstract finite precision system rather than another scale-specific identity.

## 9. Precision direction versus time direction

There is also a structural contrast with T012.

### Time evolution

Under deterministic many-to-one forward dynamics, historical fibers merge, so merged-history multiplicity is nondecreasing.

### Precision refinement

Under compatible refinement, the set of fine states consistent with the current coarse observation shrinks, so ambiguity multiplicity is nonincreasing.

This is not yet claimed as a categorical time/precision duality.  But the monotonic directions are exact opposites:

\[
\boxed{
\text{time: distinguishable histories merge},
\qquad
\text{precision: compatible possibilities separate}.
}
\]

An abstract precision-system formulation can now test whether this opposition has a deeper order-theoretic meaning.

## 10. Prior-art boundary

Eratosthenes-style sieving, trial division, least-prime-factor classification, and increasing factor cutoffs are classical.  P017 already records sieve/dynamical prior art, including the use of sieve survival ideas on consecutive-square intervals.

P018 therefore does not claim factor sieving or the first-prime-factor partition as new.

The project-specific result under test is the **cross-axis synthesis**:

- scale refinement and factor refinement are both finite precision systems;
- both support persistent coarse proof certificates;
- P017's final prime survivor count becomes the terminal state of the factor-precision proof process;
- the signed P017 carry identity and the disjoint first-witness precision-shell identity are two exact decompositions of the same terminal survivor count.

Historical novelty of that synthesis remains `NOVELTY_UNVERIFIED`.

## 11. Stage-4 status

- P018-T29 factor-precision projection compatibility: `PROVED`
- P018-T30 persistent factor certificates: `PROVED`
- P018-T31 square-basin terminal factor horizon: `PROVED`
- P018-T32 survivor monotonicity and terminal-prime identity: `PROVED`
- P018-T33 disjoint first-witness factor shells: `PROVED`
- P018-T34 exact P017/P018 bridge identity: `PROVED`
- abstract finite precision-system axioms: `NEXT`
- product of scale precision and factor precision: `OPEN`
- time/precision order duality: `OPEN`
- Legendre's conjecture: `OPEN / NOT PROVED HERE`

Executable checks live in `src/enterprise_math/factor_precision.py` and `tests/test_factor_precision.py`.
