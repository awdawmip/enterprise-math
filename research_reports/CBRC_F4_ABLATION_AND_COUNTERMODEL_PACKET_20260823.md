# CBRC F4 — Ablation and Countermodel Packet

Researcher-ID: `EM-CBRCF4-381080`

Primary verdict: `F4_RANK_ONE_SURVIVOR_EXISTS`

## A. Minimal exact globally zero-separating rank-one survivor

Take

`C = Z e ⊕ Z/2`.

Write a coefficient as `(n,t)`, with `t∈{0,1}`.  Define

- `r(0)=0`;
- `r(n)=1` for every `n≠0`;
- `q(n,0)=r(n)`;
- `q(n,1)=r(n)+1/2` if `n` is even;
- `q(n,1)=r(n)-1/2` if `n` is odd.

Thus the only zero is `q(0,0)=0`; every other coefficient state has positive
scalar.

Define, for two marked inputs `(n,t)` and `(m,u)`,

`p = n+m (mod 2)`

and

`M((n,t),(m,u)) = ((n, u+p), (m, t+p))`.

All torsion arithmetic is modulo `2`.

### Exact properties

1. `M` is additive.
2. `M^2 = id`, hence it is reversible.
3. `M` commutes with interchange of the two marked slots.
4. Each output depends on data from both inputs; the map is not a product of
   two independent unary slot maps.
5. With `e=(1,0)`,

   `M(e,0)=((1,1),(0,1))`

   and

   `q(1,1)=q(0,1)=1/2`.

6. Exact conservation holds for all inputs:

   `q(M_1(x,y))+q(M_2(x,y)) = q(x)+q(y)`.

7. `q(-n,-t)=q(n,t)`; on `Z/2`, torsion inversion is the identity.
8. Old signed cancellation remains available because the embedded free copy
   is the ordinary additive `Z e`.

The induced free quotient block is `I_2`, a signed permutation.  The actual
mixing lives in the finite torsion fibers.

### Conservation proof by parity

Write `χ(n)=(-1)^n` and
`s(n,t)=χ(n)t/2`, so `q(n,t)=r(n)+s(n,t)`.

The `r(n)+r(m)` part is unchanged because the free coordinates are unchanged.
If `p=0`, then `n,m` have the same parity and the two torsion labels are merely
swapped, so the `s`-sum is unchanged.  If `p=1`, then `χ(m)=-χ(n)` and both
torsion bits are complemented.  Hence

`χ(n)(1-u)+χ(m)(1-t) = χ(n)t+χ(m)u`,

which is exactly conservation of the correction term.

## B. Why this counterexample is smallest in torsion size

If `T=0`, the finite-fiber loophole is absent.

Under global zero separation, every non-signed-permutation free block is
impossible by the forced-period theorem proved in the main return.  A signed
permutation free block sends `(1,0)` in the free quotient to a column with one
zero entry, so with no torsion one of the two actual outputs is the zero
coefficient, contradicting the required nonzero balanced split.

Therefore no torsion-free carrier `C=Z` works.  The smallest nontrivial finite
abelian torsion group has order `2`, and the construction above works on
`Z⊕Z/2`.  Hence it is least by torsion cardinality.

## C. Strengthening that retains the old C1 unary transports

To remove the possible objection that the new carrier discarded the old
`Z/3` unary semantics, take instead

`C = Z e ⊕ Z/3 ⊕ Z/2`.

Write `(n,a,b)`.  Let

`q_*(n,a,b)=q(n,b)+1/4`

only when `n=0` and `a≠0`; otherwise let `q_*(n,a,b)=q(n,b)`.

Define

`M_*((n,a,b),(m,c,d)) = ((n,a,d+p),(m,c,b+p))`

with `p=n+m (mod 2)`.

Then:

- `q_*` has global zero separation;
- `M_*` is additive, involutive, balanced, and conserving;
- the old `R(n,a,b)=(n,a+n,b)` leaves `q_*` invariant;
- `S(n,a,b)=(n,-a,b)` leaves `q_*` invariant;
- `J(n,a,b)=(-n,-a,-b)` leaves `q_*` invariant.

Thus even a rank-one extension containing the old `Z/3` torsion and retaining
the explicitly frozen `R,J,S` scalar invariances can survive after adding only
a finite `Z/2` torsion direction.

## D. Weak-scalar survivor when GLOBAL_ZERO_SEPARATION is removed

Take `C=Z` (or take the old `Z/3` torsion and let the scalar ignore it) and

`A = [[2,3],[3,4]]`, `det(A)=-1`.

Define an even period-six scalar by

- residue `0`: `0`;
- residues `±1`: `1`;
- residues `±2`: `1/2`;
- residue `3`: `1/2`.

Then exactly for all integers `x,y`,

`f(2x+3y)+f(3x+4y)=f(x)+f(y)`.

Also `f(1)=1` and the elementary split has
`f(2)=f(3)=1/2`.

The first positive free integer with zero scalar is `6`, because
`f(6)=f(0)=0`.  This is an exact witness that the new zero-separation
regularity removes the old non-signed-free-block survivor, but it does not
remove all rank-one carriers because of the torsion-mediated signed-
permutation survivor in Part A.

## E. Mandatory ablations

### Positivity only on elementary states

Insufficient.  The period-six witness has `f(±1)=1>0` and survives.

### Positivity only on the two elementary split outputs

Insufficient.  The period-six witness has `f(2)=f(3)=1/2>0` and survives.

### FINITE_COPY_NONDEGENERACY: `q(ne)>0` for every nonzero integer `n`

Insufficient for a rank-one no-go.  The globally zero-separating survivor in
Part A satisfies the stronger condition `q(ne)>0` for every `n≠0`.

### Full GLOBAL_ZERO_SEPARATION

Still insufficient for a rank-one no-go under the blind packet as written:
Part A satisfies it exactly.

### What regularity is actually load-bearing for the free-block obstruction?

For a non-signed-permutation free block, the proof uses only

`ENVELOPE_ZERO_SEPARATION: f(n)>0 for every n≠0`

for the torsion minimum envelope

`f(n)=min_t q(n,t)`.

That is weaker than full global zero separation on every coefficient state.
It kills every non-signed-permutation free block because conservation forces a
nonzero period of `f`.

But even envelope zero separation does not kill the signed-permutation
torsion-mediated construction: its envelope is

- `f(0)=0`;
- `f(n)=1` for nonzero even `n`;
- `f(n)=1/2` for odd `n`.

So the actual missing condition is not stronger positivity; it is an
additional structural restriction excluding the signed-permutation
torsion-fiber loophole, if such a restriction is desired.

## F. Ablation verdict

`F4_POSITIVE_SEPARATION_ABLATION_AND_MINIMALITY_CLASSIFIED`

The candidate regularity is genuinely load-bearing against the old
non-signed-free-block periodic survivor, but it is **not sufficient** to force
torsion-free rank lift under the stated F4 extension class.
