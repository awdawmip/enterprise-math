# CBRC F4 — Positive-Separation Rank-Lift Return

Researcher-ID: `EM-CBRCF4-381080`  
Task-ID: `RS-CBRC-F4-POSITIVE-SEPARATION-RANK-LIFT-CLASSIFICATION`  
Owner branch: `research/cbrc-f4-positive-separation-rank-lift-classification`  
Owner base: `bd10bc351dbe7c90b47a3ffba3ef7796479170f5`

Taskbook source:
`bd10bc351dbe7c90b47a3ffba3ef7796479170f5`

Blind mathematical input:
`research_inputs/CBRC_F4_BLIND_POSITIVE_SEPARATION_RANK_LIFT_PACKET_20260823.md@c6bdd396f1777185b8791228492ca50f996307a7`

Primary verdict:

`F4_RANK_ONE_SURVIVOR_EXISTS`

Hard target:

`GLOBAL_ZERO_SEPARATION_RANK_ONE_EXTENSION_CLASSIFIED`

## 0. Executive classification

The rank-one extension class does **not** admit the requested universal rank-one
no-go under the blind packet as written.

What is true is sharper and split into two parts:

1. For every finitely generated rank-one carrier `C ≅ Z e ⊕ T`, the finite
   torsion minimum envelope satisfies an exact free conservation equation.
   Under `GLOBAL_ZERO_SEPARATION`, every nonzero free integer has strictly
   positive envelope value.
2. Every **non-signed-permutation** free quotient block
   `A∈GL_2(Z)` is then impossible: mixed-difference identities force a nonzero
   period of the envelope.
3. However, a signed-permutation free quotient can still support a genuinely
   cross-slot, balanced, reversible, scalar-conserving operation through finite
   torsion fibers.  There is an exact least-torsion witness on
   `C=Z⊕Z/2` satisfying `GLOBAL_ZERO_SEPARATION`.
4. Consequently F4 does **not** prove
   `torsion_free_rank(C) >= 2`.  Torsion-only enlargement already suffices
   under the stated operational requirements.

The precise loophole is that the blind packet pins `q(e)=1` at one point of
the free-one torsion fiber, but does not force the minimum over that fiber to
equal `1`.  Nor does it require a genuinely mixing operation to induce a
non-signed-permutation map on the free quotient.

## 1. Q1 — rank-one carrier and automorphism normal form

### Theorem 1 — carrier splitting

Let `C` be a finitely generated abelian carrier of torsion-free rank one with
an embedded primitive free generator `e` and an additive retraction

`π:C→Z`, `π(e)=1`.

Then

`T=ker π`

is finite and

`C ≅ Z e ⊕ T`.

### Proof

Since `rank(C)=1` and `π` is onto, `rank(ker π)=0`.  A finitely generated
abelian group of rank zero is finite, so `T=ker π` is finite.

For any `z∈C`,

`z = π(z)e + (z-π(z)e)`

and the second term lies in `T`; hence `Z e + T=C`.  If `ne+t=0` with `t∈T`,
applying `π` gives `n=0`, then `t=0`.  The sum is direct.

### Theorem 2 — two-slot automorphism block form

Relative to `C^2 ≅ Z^2 ⊕ T^2`, every additive automorphism has the form

`M(v,s) = (A v, R v + P s)`

with

- `A∈GL_2(Z)`;
- `P∈Aut(T^2)`;
- `R∈Hom(Z^2,T^2)` arbitrary.

Equivalently, if `v=(n,m)` and `s=(t,u)`, then the two free output coordinates
are

`an+bm`, `cn+dm`

for

`A=[[a,b],[c,d]]∈GL_2(Z)`,

while the torsion outputs are an affine translate of the automorphism `P`.

### Proof

The torsion subgroup of `C^2` is exactly `T^2` and is characteristic, so an
automorphism restricts to `P∈Aut(T^2)`.  Passing to the quotient by torsion
gives `A∈GL_2(Z)`.  A homomorphism from the free part to torsion supplies the
cross term `R`.  Conversely this block-triangular map is invertible exactly
when both `A` and `P` are invertible.

For every fixed free input `v`, the torsion map

`s ↦ P s + Rv`

is therefore a bijection of the finite set `T^2`.

Deliverable:

`F4_RANK_ONE_CARRIER_AND_AUTOMORPHISM_NORMAL_FORM_CLASSIFIED`

## 2. Q2 — finite-torsion minimum envelope

Let

`f(n)=min_{t∈T} q(n,t)`.

The minimum exists because `T` is finite.

### Theorem 3 — torsion-blind conservation

If `M` conserves

`Q(x,y)=q(x)+q(y)`

exactly, then for all integers `n,m`,

`f(an+bm)+f(cn+dm)=f(n)+f(m)`.        (E)

### Proof

Fix the free input `(n,m)` and minimize the exact conservation identity over
all `(t,u)∈T^2`.  On the input side the minimum separates as
`f(n)+f(m)`.  On the output side the torsion labels range bijectively over all
of `T^2` by Theorem 2, so the minimum separates as
`f(an+bm)+f(cn+dm)`.

### Consequences that really follow

- `f(0)=0`, because `q(0,0)=0` and `q≥0`.
- Under `GLOBAL_ZERO_SEPARATION`, `f(n)>0` for every `n≠0`, since the finite
  fiber over a nonzero free integer contains only nonzero coefficient states.
- If the inherited absolute sign transport acts by
  `(n,t)↦(-n,-t)` and leaves `q` invariant, then `f(-n)=f(n)`.
- `f(1)≤1`, because `q(e)=q(1,0)=1`.

If

`M(e,0)=((a,α),(c,γ))`

is balanced, exact conservation gives

`q(a,α)=q(c,γ)=1/2`.

Hence only

`f(a)≤1/2`, `f(c)≤1/2`

is automatic.

### The required `f(1)=1` step is false

The blind packet does not force the point `(1,0)` to minimize `q` on its
torsion fiber.  The exact rank-one survivor in Section 5 has

`q(1,0)=1`

but

`q(1,1)=1/2`,

so

`f(1)=1/2`.

Its balanced elementary outputs also occur at non-minimizing/minimizing
torsion labels in different free fibers.  Thus neither `f(1)=1` nor exact
balanced first-column **envelope** values can be derived without an additional
fiber-transitivity/fiber-normalization axiom.

This is not a numerical failure; it is an exact counterexample to that
implication.

Deliverable:

`F4_FINITE_TORSION_MIN_ENVELOPE_CLASSIFIED`

with the classification that the requested normalization subclaim is
**not implied by the stated axioms**.

## 3. Q3 — arbitrary free-block obstruction

Assume from here only that `f` is nonnegative, even, satisfies `f(0)=0`,
satisfies (E), and obeys

`f(n)>0` for `n≠0`.

No normalization `f(1)=1` is needed.

Let

`A=[[a,b],[c,d]]∈GL_2(Z)`.

### 3.1 Axis identities

From (E),

`f(an)+f(cn)=f(n)`,                        (C1)

`f(bn)+f(dn)=f(n)`.                        (C2)

Because (E) is invariant under `A^{-1}` and `f` is even,

`f(dn)+f(cn)=f(n)`,                        (I1)

`f(bn)+f(an)=f(n)`.                        (I2)

Hence

`f(an)=f(dn)`, `f(bn)=f(cn)`.

### 3.2 Zero-entry blocks

If one entry of `A` is zero, global envelope separation forces `A` to be a
signed permutation.

For example, if `a=0`, unimodularity gives `|b|=|c|=1`.  Then (C2) becomes

`f(n)+f(dn)=f(n)`,

so `f(dn)=0` for all `n`.  Positivity off zero forces `d=0`; hence the matrix
is signed anti-diagonal.  The other zero-entry cases are identical after
interchanging rows/columns.

Therefore any non-signed-permutation block has all four entries nonzero.

### 3.3 Mixed-difference identities

Write

`Δ_r f(k)=f(k+r)-f(k)`.

Taking the mixed input difference of (E) gives, because `A` is onto `Z^2`,

`Δ_aΔ_b f(u)+Δ_cΔ_d f(v)=0`

for independently arbitrary `u,v`.  Therefore

`Δ_aΔ_b f = K`, `Δ_cΔ_d f = -K`             (D1)

for a constant `K`.

A second independent mixed-difference identity is obtained by shifting inputs
along the two primitive kernel directions `(d,-c)` and `(b,-a)`.  It yields

`Δ_aΔ_c f = L`, `Δ_bΔ_d f = -L`             (D2)

for another constant `L`.

### 3.4 The constants vanish

Lemma: if `r,s≠0`, `f` is even, and

`Δ_rΔ_s f = K`

is constant, then telescoping over an integer rectangle gives

`f(rsN)=rs K N^2/2`                          (R)

for every integer `N`.

Indeed choose rectangle multiplicities `sN` and `-rN`; the two endpoint
increments cancel, and evenness turns the remaining two values into
`-2f(rsN)`.

Apply this to `(r,s)=(a,b)`.  The inverse-axis identity (I2) says

`f(an)+f(bn)=f(n)`.

Substitute `n=abN` into (R).  The left side becomes the same quadratic formula
with multipliers `aN` and `bN`, so

`(a^2+b^2-1)abK N^2/2 = 0`.

Since `a,b≠0`, `a^2+b^2>1`, hence `K=0`.

The same argument using (C1) gives `L=0`.  Thus

`Δ_aΔ_b f=0`,
`Δ_cΔ_d f=0`,
`Δ_aΔ_c f=0`,
`Δ_bΔ_d f=0`.                                (D0)

### 3.5 Forced period

Set

`g=gcd(|a|,|d|)`,
`h=gcd(|b|,|c|)`.

From (D0), `Δ_a f` has periods `b` and `c`, hence period `h`.
Because `h|b` and `gcd(a,b)=1`, we have `gcd(a,h)=1`.

Therefore

`f(n+ah)-f(n)
 = Σ_{j=0}^{h-1} Δ_a f(n+ja)`

is independent of `n`: the residues `n+ja mod h` run through all residue
classes.  A globally nonnegative function cannot have a nonzero constant
increment over a nonzero step in both forward and backward directions, so the
constant is zero.  Hence `ah` is a period of `f`.

The same argument with `d` shows `dh` is a period.  Their gcd is

`gcd(|a|h,|d|h)=gh`.

Thus

`f(n+gh)=f(n)` for all `n`.                  (P)

Since `gh>0`,

`f(gh)=f(0)=0`,

contradicting envelope zero separation.

### Free-block theorem

Every rank-one globally zero-separating conserving model has a signed-
permutation induced free block.

Equivalently:

`NON_SIGNED_PERMUTATION_FREE_BLOCK + ENVELOPE_ZERO_SEPARATION -> NO_GO`.

This theorem is uniform in the finite abelian torsion group `T`.

## 4. Why the free-block theorem does not imply rank lift

The theorem only constrains the induced free quotient.  It does not say that
the full automorphism on `C^2` is a signed permutation or a product of unary
slot maps.  Finite torsion cross-data can still produce genuine two-slot
mixing while the free quotient is a signed permutation.

That possibility is realized exactly below.

## 5. Least exact rank-one counterexample

Take

`C = Z e ⊕ Z/2`.

Write `(n,t)`, `t∈{0,1}`.  Define

`r(0)=0`, `r(n)=1` for `n≠0`

and

`q(n,0)=r(n)`,
`q(n,1)=r(n)+1/2` for even `n`,
`q(n,1)=r(n)-1/2` for odd `n`.

Then:

- `q(0,0)=0`;
- `q(e)=q(1,0)=1`;
- every nonzero coefficient state has strictly positive scalar.

Define

`p=n+m mod 2`

and

`M((n,t),(m,u))=((n,u+p),(m,t+p))`.

### Exact checks

- `M` is additive.
- `M^2=id`.
- `M` commutes with swapping the marked slots.
- each output depends on both input slots; it is not a direct product of unary
  slot maps;
- `M(e,0)=((1,1),(0,1))`;
- `q(1,1)=q(0,1)=1/2`;
- `Q(Mv)=Q(v)` for every `v`;
- sign inversion leaves `q` unchanged.

The free block is `I_2`.  Thus this is precisely the signed-permutation torsion
loophole.

### Least-torsion proof

If `T=0`, a non-signed-permutation free block is impossible by Section 3.  A
signed-permutation first column has one zero entry, so one elementary output
would be the zero coefficient, violating the required nonzero balanced split.
Therefore `T=0` cannot work.

The smallest nontrivial finite abelian group is `Z/2`, and the construction
above works.  Hence the counterexample is smallest by torsion cardinality.

### C1-compatible strengthening

There is also a rank-one survivor on

`Z e ⊕ Z/3 ⊕ Z/2`

that contains the old `Z/3` torsion and preserves the explicitly frozen
`R,J,S` scalar invariances.  It is given in the ablation packet.  Therefore the
survivor is not an artifact of simply discarding the old current-carrier unary
semantics.

Deliverable:

`F4_RANK_ONE_POSITIVE_SEPARATION_MIXING_CLASSIFIED`

Result:

`F4_RANK_ONE_SURVIVOR_EXISTS`.

## 6. Q4 — rank lower bound

Because a rank-one survivor exists, F4 cannot freeze

`torsion_free_rank(C) >= 2`.

The exact classified consequence is instead:

- torsion-free rank one remains possible;
- torsion-only enlargement can evade the non-signed-free-block obstruction;
- the only universal theorem proved here is that the **free quotient block**
  must be a signed permutation under global zero separation;
- no rank-two carrier is constructed, named, selected, or implied.

Since the old signed generator is embedded, the structural lower bound remains
only the already-assumed

`torsion_free_rank(C) >= 1`.

Deliverable:

`F4_MINIMUM_TORSION_FREE_RANK_LOWER_BOUND_CLASSIFIED`

with verdict:

`RANK_LIFT_TO_TWO_NOT_PROVED`.

## 7. Q5 — ablation and minimality

An exact weak-scalar non-signed-free-block survivor is

`A=[[2,3],[3,4]]`

with the even period-six free scalar

`f(0)=0`,
`f(±1)=1`,
`f(±2)=1/2`,
`f(3)=1/2`.

It satisfies exact conservation and the balanced split
`f(2)=f(3)=1/2`, but

`f(6)=0`.

Therefore `GLOBAL_ZERO_SEPARATION` is genuinely load-bearing against that
periodic free-block survivor.

However:

- positivity only on elementary states is insufficient;
- positivity only on the elementary split outputs is insufficient;
- `FINITE_COPY_NONDEGENERACY` is insufficient for an all-rank-one no-go,
  because the Section 5 survivor satisfies the stronger global condition;
- full `GLOBAL_ZERO_SEPARATION` itself is insufficient for an all-rank-one
  no-go;
- for **non-signed-permutation free blocks**, the weaker condition
  `f(n)>0` for all nonzero `n` already suffices.

Deliverable:

`F4_POSITIVE_SEPARATION_ABLATION_AND_MINIMALITY_CLASSIFIED`.

## 8. Deterministic checker

Required path:

`scripts/cbrc_f4_validate_positive_separation_rank_lift.py`

Checker source SHA-256:

`751dea8f2d1023ad0f119cb3683eaefed5c1c3c4abab4708b04b66d7d57b559b`

Deterministic result SHA-256:

`be9a6cf62635ad6689510c1e4da94755a42838976921a5f66a29012f36aba12a`

Coverage includes:

- finite torsion-fiber affine-bijection/min-envelope checks for
  `0`, `Z/2`, `Z/3`, `Z/4`, and `Z/2×Z/2`;
- bounded `GL_2(Z)` regression through coefficient bound `4`;
- `360` unimodular matrices checked, with `0` theorem/enumeration mismatches;
- the exact period-six weak-scalar survivor;
- the minimal global rank-one survivor on `Z⊕Z/2`;
- the `Z⊕Z/3⊕Z/2` strengthening preserving old `R,J,S`;
- all mandatory ablations.

Enumeration is used only as regression, never as proof of the arbitrary-group
or arbitrary-`GL_2(Z)` theorems.

## 9. Artifact SHA-256s known before freeze-manifest creation

- source/target-leak audit:
  `9672750c71c8e56df7e4a0e502498a6121e24b1e2525aa8eab4e750238fd4132`
- ablation/countermodel packet:
  `863f6478cd1a26d3b0984a05d62d700266804e131d5d6e806656bb6de92568ad`
- deterministic checker source:
  `751dea8f2d1023ad0f119cb3683eaefed5c1c3c4abab4708b04b66d7d57b559b`

The return file and manifest hashes are computed after their contents are
frozen to avoid circular self-hashing.  The manifest records the return hash;
the final handoff reports the manifest hash and final owner-head commit.

## 10. Acceptance-gate status

- `F4_RANK_ONE_CARRIER_AND_AUTOMORPHISM_NORMAL_FORM_CLASSIFIED` — **PASS**
- `F4_FINITE_TORSION_MIN_ENVELOPE_CLASSIFIED` — **PASS**, with requested
  `f(1)=1` implication refuted by exact counterexample
- `F4_RANK_ONE_POSITIVE_SEPARATION_MIXING_CLASSIFIED` — **PASS**
- `F4_MINIMUM_TORSION_FREE_RANK_LOWER_BOUND_CLASSIFIED` — **PASS**
- `F4_POSITIVE_SEPARATION_ABLATION_AND_MINIMALITY_CLASSIFIED` — **PASS**
- `TARGET_LEAK_AUDIT_PASS` — **PASS**
- deterministic checker — **PASS**

## 11. Unresolved assumptions / semantic boundary

Two phrases in the blind packet do not carry a stronger formal condition than
their listed operational consequences:

1. **Accepted absolute unary transports on newly added torsion.**  The packet
   does not require every new torsion direction to be traversed transitively by
   a new accepted shear.  The minimal `Z/2` witness respects inversion; the
   strengthening on `Z/3⊕Z/2` also preserves the old frozen `R,J,S` invariances.
   Requiring an additional accepted shear on the new `Z/2` factor would be a
   new axiom.
2. **Genuine mixing.**  The packet does not define it as “non-signed-
   permutation on the free quotient.”  The witness is additive, involutive,
   slot-swap equivariant, non-slotwise, depends across slots, and sends
   `(e,0)` to two nonzero balanced outputs.  If a future specification adds
   `FREE_QUOTIENT_NON_SIGNED_PERMUTATION` as a separate axiom, Section 3 would
   immediately give the conditional no-go and hence the authorized
   rank-at-least-two conclusion.  That condition is not assumed in F4.

## 12. Freeze verdict

`GLOBAL_ZERO_SEPARATION_RANK_ONE_EXTENSION_CLASSIFIED`

`F4_RANK_ONE_SURVIVOR_EXISTS`

No rank-two structure has been selected or constructed.
