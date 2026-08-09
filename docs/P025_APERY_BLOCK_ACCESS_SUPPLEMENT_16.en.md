# P025 Supplement 16 — Apéry Defect Semigroup for High-Dimensional Block Access

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplements 13–15  
Hard block: `NONE`

## 1. Why the next object is not another abc-specific lattice

Supplement 15 isolated the block access function

\[
\kappa_n(T)
=
\min\left\{
\|x\|_\infty:
\sum_{p\mid n}\frac{n v_p(n)}p x_p=T
\right\}.
\]

The same problem exists for any positive integer row. Divide out the row gcd and write the primitive row as

\[
\boxed{b=(b_1,\ldots,b_d),\qquad \gcd(b_1,\ldots,b_d)=1.}
\]

For `N>=0` define

\[
\boxed{
\kappa_b(N)
=
\min\{\|x\|_\infty:x\in\mathbb Z^d,\ b\cdot x=N\}.
}
\]

Let

\[
\boxed{P=b_1+\cdots+b_d.}
\]

The two-variable modular solver from Supplements 10–11 is one specialization. The present supplement removes the dimension restriction.

## 2. P025-T46 — exact signed-access to nonnegative-defect transform

Fix a candidate radius `r>=0`. Then

\[
\boxed{
\exists x\in\mathbb Z^d:
\|x\|_\infty\le r,
\ b\cdot x=N
}
\]

if and only if there exists

\[
y\in\mathbb N^d
\]

such that

\[
\boxed{
 b\cdot y=rP-N,
\qquad
0\le y_i\le2r.
}
\]

### Proof

Given `x`, define

\[
\boxed{y_i=r-x_i.}
\]

Because `-r<=x_i<=r`, one has `0<=y_i<=2r`. Moreover

\[
b\cdot y
=
\sum_i b_i(r-x_i)
=rP-b\cdot x
=rP-N.
\]

Conversely, from such a nonnegative `y`, define

\[
x_i=r-y_i.
\]

Then `-r<=x_i<=r` and the same identity rearranges to `b·x=N`. ∎

### Consequence

The signed minimum-preimage problem is controlled by the numerical semigroup

\[
\boxed{
S_b=\langle b_1,\ldots,b_d\rangle
\subseteq\mathbb N_0.
}
\]

The defect at radius `r` is

\[
\boxed{\delta=rP-N.}
\]

The only extra condition beyond `delta in S_b` is that the chosen nonnegative factorization of `delta` fit inside the coordinate cap `2r`.

## 3. P025-D07 — Apéry defect profile

Because `P=sum b_i` belongs to `S_b`, define the Apéry set

\[
\operatorname{Ap}(S_b;P)
=
\{a_0,\ldots,a_{P-1}\},
\]

where

\[
\boxed{
a_j
=
\min\{s\in S_b:s\equiv j\pmod P\}.
}
\]

For each Apéry element define its minimum nonnegative `L_infinity` factorization radius

\[
\boxed{
L_j
=
\min\left\{
\|y\|_\infty:
 y\in\mathbb N^d,
\ b\cdot y=a_j
\right\}.
}
\]

The finite data

\[
\boxed{
\Sigma_{\rm Ap}(b)
=
\bigl(P,(a_j,L_j)_{j=0}^{P-1}\bigr)
}
\]

will be called the **Apéry access profile**.

## 4. P025-T47 — exact first stable target in every residue class

Fix a target `N>=0`, and let

\[
j\equiv-N\pmod P.
\]

Any radius `r` realizing `N` has defect

\[
\delta=rP-N\equiv j\pmod P.
\]

By definition of the Apéry element,

\[
\delta\ge a_j.
\]

Therefore every access radius satisfies

\[
\boxed{
 r
\ge
 r_0(N)
:=
\frac{N+a_j}{P}.
}
\]

The lower bound is exact if and only if the Apéry element itself fits inside the transformed coordinate cap:

\[
\boxed{
\kappa_b(N)=r_0(N)
\iff
L_j\le2r_0(N).
}
\]

### Proof

If `r<r_0`, then

\[
rP-N<a_j
\]

while having the same residue `j`, so the defect cannot lie in `S_b`. Thus `r_0` is an absolute lower bound.

At `r=r_0`, the defect is exactly `a_j`. P025-T46 says this radius is feasible exactly when `a_j` has a nonnegative factorization with every coordinate at most `2r_0`, which is equivalent to `L_j<=2r_0`. ∎

Define

\[
q_j=\left\lceil\frac{L_j}{2}\right\rceil.
\]

Then the stable Apéry formula is available precisely when

\[
\boxed{
N\ge Pq_j-a_j
}
\]

inside the target residue class `N congruent -j mod P`.

Hence the **first stable target** in that residue is the smallest nonnegative integer

\[
\boxed{
N_j^*\equiv-j\pmod P,
\qquad
N_j^*\ge Pq_j-a_j.
}
\]

This is exact, not merely sufficient.

## 5. P025-T48 — eventual affine-periodic access law

For every

\[
N\equiv-j\pmod P,
\qquad
N\ge N_j^*,
\]

one has

\[
\boxed{
\kappa_b(N)
=
\frac{N+a_j}{P}.
}
\]

Therefore

\[
\boxed{
\kappa_b(N+P)=\kappa_b(N)+1
}
\]

for every target in the stable tail of its residue class.

### Proof

Once `N>=N_j^*`, P025-T47 makes the Apéry lower bound feasible and therefore exact. Replacing `N` by `N+P` leaves the defect residue and Apéry element unchanged while increasing `(N+a_j)/P` by one. The cap condition only becomes easier. ∎

Thus the access response has a finite irregular preperiod followed by an exact affine-periodic law of period `P`.

## 6. P025-T49 — the complete exceptional-target set is finite and explicit

For each target residue

\[
\rho=(-j)\bmod P,
\]

the targets before the stable tail are exactly

\[
\boxed{
\rho,
\rho+P,
\rho+2P,
\ldots,
<N_j^*.
}
\]

Taking the union over all `j` gives a finite set

\[
\boxed{\mathcal E_b}
\]

such that

\[
N\notin\mathcal E_b
\Longrightarrow
\kappa_b(N)
=
\frac{N+a_{-N}}P.
\]

Moreover every `N in E_b` is a genuine failure of that Apéry closed formula, because at those targets the Apéry defect cannot yet fit inside the available `2r_0` coefficient cap.

So the preperiod is not merely bounded: it is exactly enumerable from the finite profile `Sigma_Ap`.

## 7. Example: `(5,2)` and the old coarse stability bound

For

\[
b=(5,2),
\qquad
P=7,
\]

the Apéry values by defect residue are

\[
\boxed{
(a_0,\ldots,a_6)
=(0,8,2,10,4,5,6).
}
\]

The corresponding minimum nonnegative `L_infinity` radii are

\[
\boxed{
(L_0,\ldots,L_6)
=(0,4,1,2,2,1,3).
}
\]

The exact exceptional target set is only

\[
\boxed{\mathcal E_{(5,2)}=\{1\}.}
\]

Indeed

\[
\kappa(1)=2,
\qquad
\kappa(2)=1,
\]

so access is locally nonmonotone, but after that single exceptional target the Apéry affine law is already exact.

This sharply improves the earlier engineering-safe `N>=max(A,B)^2` sufficient region in `abc_access_response.py`. That older bound remains correct but is no longer the best structural description.

## 8. Example: the `1+242=243` block

The nontrivial block equation from Supplement 15 reduces to

\[
11x_2+4x_{11}=405.
\]

Thus

\[
b=(11,4),
\qquad
P=15,
\qquad
N=405\equiv0\pmod{15}.
\]

For residue zero,

\[
a_0=0,
\qquad
L_0=0.
\]

Hence the stable formula gives immediately

\[
\boxed{
\kappa_{(11,4)}(405)
=
405/15
=27,
}
\]

recovering the exact block access radius without solving a two-variable Bezout optimization.

## 9. Example: genuinely higher-dimensional block

For the primitive three-coordinate row

\[
\boxed{b=(15,10,6),\qquad P=31,}
\]

the finite profile has only three exceptional nonnegative targets below 70 in the committed reference regression:

\[
\boxed{3,7,13.}
\]

Every other tested target is already on its exact Apéry affine branch. The executable suite compares the profile formula against an independent finite exact access oracle rather than treating the sample as a proof.

The theorem itself is dimension-independent.

## 10. Relation to numerical-semigroup prior art

This stage sits very close to established factorization theory and must be attributed accordingly.

Numerical semigroups, Apéry sets, and extremal factorization lengths are classical. In particular, Chapman–Dugan–Gaskari–Lycan–Mendoza De La Cruz–O'Neill–Ponomarenko study `p`-lengths including `p=infinity` for numerical semigroups and prove eventual quasipolynomial behavior; their minimum `L_infinity` analysis explicitly uses Apéry sets [SRC-CHAPMAN-ETAL-2024-P-LENGTHS].

Therefore P025 does **not** claim as new:

- Apéry-set residue compression;
- eventual quasipolynomial/affine-periodic behavior of numerical-semigroup factorization invariants;
- `L_infinity` factorization length itself.

The project-side contribution under test is narrower:

\[
\boxed{
\text{signed certificate preimage access}
\xrightarrow{y=r\mathbf1-x}
\text{Apéry-controlled numerical-semigroup defect}
}
\]

and its use as an exact finite-precision state for arithmetic-derivative witness access.

Historical priority of that exact bridge remains `NOVELTY_UNVERIFIED`.

## 11. Architectural consequence

Supplements 13–16 now form a strict information ladder inside one arithmetic block:

\[
\boxed{
\text{full prime-coordinate row}
\to
A(n)=\gcd(\text{row})
\to
\text{primitive row }b
\to
\Sigma_{\rm Ap}(b)
\to
\text{eventual access response}.
}
\]

Different future languages stop at different levels:

- image membership needs only `A(n)`;
- exact absorption floor may need only block image generators and ideal intersections;
- one selected target may need a local access calculation;
- all sufficiently large target-access queries need only the finite Apéry access profile;
- exact small-preperiod access can still require finer information.

So `precision` is again a question of which future query must remain exact, not a universal scalar attached to the block.

## 12. Executable assets

Added:

- `src/enterprise_math/abc_block_access_apery.py`
  - primitive positive row normalization;
  - exact signed-access/nonnegative-defect transform;
  - Apéry values modulo `P=sum b_i`;
  - minimum nonnegative `L_infinity` factorization radius for each Apéry element;
  - exact residue-specific first stable target;
  - exact exceptional-target set;
  - exact eventual access formula and period-shift check;
  - independent finite exact access oracle.
- `tests/test_abc_block_access_apery.py`
  - exact `(5,2)` profile and sole exceptional target `1`;
  - exhaustive agreement with the closed two-variable solver on small coprime rows;
  - three-coordinate regression;
  - recovery of `nu=27` and `nu=13` block examples;
  - target/row gcd scaling compatibility.

## 13. Next frontier

No hard block exists. Continue with:

1. compare the exact Apéry access profile with P024's boundary/semigroup precision and decide mother-layer ownership;
2. characterize how `Sigma_Ap` changes under multiplication/exponentiation of the underlying integer block;
3. determine whether the finite exceptional set admits a smaller task-specific signature than the full Apéry pair list;
4. derive direct upper bounds on the first stable targets in terms of block coefficients without hiding the exact profile;
5. test whether the same signed-preimage/defect-semigroup transform applies to non-abc relation-conditioned certificate systems;
6. preserve the distinction between established numerical-semigroup theory and the P025 architecture application.
