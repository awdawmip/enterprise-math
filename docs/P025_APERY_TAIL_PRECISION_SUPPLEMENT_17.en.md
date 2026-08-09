# P025 Supplement 17 — Task-Minimal Apéry Tail Precision and Finite Exact Access Signature

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplement 16; P023 task-relative quotient/minimal repair  
Hard block: `NONE`

## 1. Question

Supplement 16 attached to a primitive positive coefficient row `b` the finite Apéry access profile

\[
\Sigma_{\rm Ap}
=
\bigl(P,(a_j,L_j)_{j\bmod P}\bigr),
\qquad
P=\sum_i b_i,
\]

where `a_j` is the least semigroup defect in residue `j`, and `L_j` is the minimum nonnegative `L_infinity` factorization radius of `a_j`.

That state is sufficient for the eventual access law, but P023 asks a sharper question:

> Which part of it is actually visible to the declared future language?

For the language that asks only whether a target has entered its exact affine-periodic tail and, once there, what `kappa_b(N)` is, the full value `L_j` is too fine.

## 2. P025-D08 — certified-tail coordinate

Define

\[
\boxed{
q_j
=
\left\lceil\frac{L_j}{2}\right\rceil.
}
\]

Supplement 16 proved that the Apéry lower bound

\[
r_0(N)=\frac{N+a_j}{P},
\qquad j\equiv-N\pmod P,
\]

is exact precisely when

\[
L_j\le2r_0(N).
\]

Because `r_0(N)` is an integer, this condition is equivalent to

\[
\boxed{q_j\le r_0(N).}
\]

Thus the parity/detail inside `L_j` beyond `ceil(L_j/2)` is invisible to the tail-certification language.

Define the **certified-tail signature**

\[
\boxed{
\Sigma_{\rm tail}(b)
=
\bigl(P,(a_j,q_j)_{j\bmod P}\bigr).
}
\]

## 3. P025-T50 — `Sigma_tail` exactly determines tail entry and stable access

For target `N>=0`, set `j congruent -N mod P`. Then `Sigma_tail` determines the first stable target in that residue by

\[
\boxed{
N_j^*
=
\min\{N\ge0:
N\equiv-j\pmod P,
\ N\ge Pq_j-a_j\}.
}
\]

Hence it answers exactly

\[
\boxed{
\text{stable}(N)
\iff
N\ge N_j^*.
}
\]

Whenever stable,

\[
\boxed{
\kappa_b(N)
=
\frac{N+a_j}{P}.
}
\]

So no raw `L_j` value is needed for any query in this future language. ∎

## 4. P025-N07 — Apéry values alone are not enough

Consider two distinct primitive four-coordinate rows

\[
\boxed{b=(2,4,5,11),
\qquad
b'=(2,5,7,8).}
\]

Both have

\[
P=22.
\]

They generate the same numerical semigroup `S=<2,5>` and have the same complete Apéry value table with respect to `22`:

\[
\boxed{
(0,23,2,25,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21).
}
\]

But their factorization geometry differs at defect residue `6`.

For the first row,

\[
6=2+4
\]

uses each coordinate at most once, so

\[
L_6=1,
\qquad q_6=1.
\]

For the second row, the available coefficient coordinates force

\[
6=2+2+2,
\]

so

\[
L_6=3,
\qquad q_6=2.
\]

The corresponding target residue is

\[
N\equiv-6\equiv16\pmod{22}.
\]

At the first target `N=16`, the Apéry lower radius is `1`. It is feasible for the first row and infeasible for the second:

\[
\boxed{
\kappa_b(16)=1,
\qquad
\kappa_{b'}(16)=2.
}
\]

Indeed the second row does not enter its Apéry tail in that residue until `N=38`.

Therefore

\[
\boxed{
\text{same numerical semigroup + same Apéry values}
\not\Rightarrow
\text{same access precision}.
}
\]

This is a project-relevant boundary because prime-labelled witness coordinates retain factorization multiplicity/geometry that ordinary semigroup membership forgets.

## 5. P025-T51 — raw `L_j` is over-refined for tail certification

Now compare

\[
\boxed{b=(2,4,5,11),
\qquad
c=(2,5,6,9).}
\]

Again both have period `22` and the same complete Apéry value table. Their raw minimum factorization-radius profiles are different. For example some Apéry elements require two copies in one representation and only one in the other.

Nevertheless the compressed values satisfy

\[
\boxed{
\left\lceil L_j(b)/2\right\rceil
=
\left\lceil L_j(c)/2\right\rceil
=1
\quad\text{for every nonzero residue }j.
}
\]

Thus their entire `Sigma_tail` signatures agree even though the raw `L_j` profiles do not.

By P025-T50 they therefore give exactly the same tail-entry answer and stable access value for every nonnegative target. In fact in this example every target is already stable, so the whole nonnegative access functions agree.

This gives an explicit quotient witness:

\[
\boxed{
L_j
\longmapsto
q_j=\lceil L_j/2\rceil
}
\]

loses real factorization detail while preserving the declared tail language exactly.

## 6. P025-D09 — finite exact access signature

The tail signature does not claim to reconstruct access values inside the finite exceptional preperiod. Supplement 16 already proved that the exception set

\[
\mathcal E_b
\]

is finite and exactly computable.

Attach the finite response table

\[
\boxed{
\mathcal X_b
=
\{(N,\kappa_b(N)):N\in\mathcal E_b\}.
}
\]

Define

\[
\boxed{
\Sigma_{\rm exact}(b)
=
\bigl(\Sigma_{\rm tail}(b),\mathcal X_b\bigr).
}
\]

## 7. P025-T52 — a finite state reconstructs the entire infinite access function

For every `N>=0`:

1. if `N in E_b`, read `kappa_b(N)` from the finite exception table;
2. otherwise `N` is in its certified tail, and `Sigma_tail` gives
   \[
   \kappa_b(N)=\frac{N+a_{-N}}P.
   \]

Therefore

\[
\boxed{
\Sigma_{\rm exact}(b)
\text{ reconstructs }N\mapsto\kappa_b(N)
\text{ for all }N\in\mathbb N_0.
}
\]

This is exact finite information, not an asymptotic approximation or a hidden infinite table. ∎

### Examples

- `(5,2)` has exception table `{(1,2)}`;
- `(2,5,7,8)` has exception table `{(16,2)}`;
- `(2,4,5,11)` has an empty exception table.

## 8. P023 interpretation

Stages 16–17 now exhibit three different precision states for the same coefficient row:

\[
\boxed{
\begin{array}{ll}
(P,a_j) & \text{candidate affine branches only},\\
(P,a_j,q_j) & \text{certified tail + exact stable values},\\
(P,a_j,q_j)+\mathcal X_b & \text{entire exact nonnegative access function}.
\end{array}
}
\]

The full factorization geometry is still richer because it can answer witness-identity or decomposition queries not present here.

So the correct representation depends on the declared future language; neither “keep everything” nor “semigroup membership alone” is universally minimal.

## 9. Prior-art discipline

Apéry sets, numerical-semigroup factorization theory, `L_infinity` factorization length, and eventual quasipolynomial behavior are prior art, including the modern `p`-length work registered for Supplement 16.

P025 claims no priority for those general structures. The project-side result under test is the task-relative compression chain obtained after transporting signed certificate access into the semigroup defect language, especially the exact distinction

\[
\text{Apéry membership state}
<
\text{tail-certification state}
<
\text{full exact-access state}.
\]

Historical novelty remains `NOVELTY_UNVERIFIED`.

## 10. Executable assets

Added:

- `src/enterprise_math/abc_apery_tail_precision.py`
  - certified-tail signature `(a_j,ceil(L_j/2))`;
  - exact tail query;
  - finite exact access signature;
  - full response reconstruction;
  - equal-Apéry/different-onset counterexample;
  - equal-tail/different-raw-factorization example.
- `tests/test_abc_apery_tail_precision.py`
  - exact counterexamples above;
  - reconstruction of complete access functions;
  - finite exception tables;
  - explicit partiality of the tail-only state on exceptional targets.

## 11. Next frontier

No hard block exists. Continue with:

1. ask whether `Sigma_exact` itself admits a coarser canonical encoding of the exception table;
2. compare this finite-tail/exception decomposition with P024 numerical-semigroup boundary precision;
3. test transformations of the profile under multiplication and exponentiation of the originating integer block;
4. extend from scalar target access to several simultaneous derivative/certificate targets;
5. search for the same finite-tail + exception-table pattern in non-abc relation-conditioned witness systems.
