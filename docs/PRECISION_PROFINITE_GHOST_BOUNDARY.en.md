# Profinite Ghost Boundary: Completion Is Not Exact Descent

Status: `RESEARCH BRIDGE / NONCANONICAL`

The current local-global line needs one explicit negative boundary: **arbitrarily fine finite precision can converge to a genuine profinite state without converging to an exact integer state.**

The positive affine-lattice theorems avoid this failure because they have an extra structural property: integer lattice images are profinitely closed.

## 1. Two different questions

Given an exact integer world with finite modular quotients, distinguish:

1. **completion question** — is there a compatible state in the inverse limit of all finite modular worlds?
2. **descent question** — does that inverse-limit state come from an actual state in the original integer world?

For integers, the inverse limit is the profinite completion

`Z_hat ~= product_p Z_p`.

The natural embedding

`Z -> Z_hat`

is injective but not surjective.

So finite-precision coherence can create valid points in the completion that are not ordinary integers.

## 2. Sharp polynomial witness

Consider

`F(x)=(x^2-13)(x^2-17)(x^2-221)`.

There is no integer root because none of `13,17,221` is an integer square.

Nevertheless F has a root modulo every positive integer.

### Prime powers

For every prime p choose one factor that has a root in `Z_p`:

- p=2: 17 is a 2-adic square because `17==1 mod8`;
- p=13: 17 has simple root `2 mod13`, hence lifts by Hensel;
- p=17: 13 has simple root `8 mod17`, hence lifts;
- other odd p: if 13 or17 is a quadratic residue use it; if both are nonresidues, then 221 is a residue because its Legendre symbol is their product `(+1)`.

Thus for every p there is `x_p in Z_p` with

`F(x_p)=0`.

### Profinite state

The tuple

`x_hat=(x_p)_p in product_p Z_p ~= Z_hat`

is a genuine profinite solution:

`F(x_hat)=0 in Z_hat`.

But no `x in Z` maps to this solution, because F has no integer zero.

Hence

`profinite solution exists`

does not imply

`integer solution exists`.

## 3. Every finite modulus still sees a valid state

For any finite modulus

`M=product_p p^(e_p)`,

reduce the selected p-adic roots modulo each `p^(e_p)` and combine them by CRT. The result is one residue `x_M` with

`F(x_M)==0 mod M`.

So no finite modular experiment, and not even the entire compatible inverse system of finite experiments, can distinguish the profinite ghost from an exact realizable world **without an additional descent theorem**.

## 4. Why the affine linear theorem does not fail

For

`A:Z^n -> Z^m`,

exact reachability of b is membership in the lattice image

`L=im_Z(A)`.

The identity

`L = intersection_M (L + M Z^m)`

says precisely that L is closed in the profinite topology.

Therefore

`A x == b mod every M`

forces

`b in L`

and hence an actual integer solution.

The local-global success is not caused by “testing every finite precision” alone. It is caused by

`all finite precisions + profinite closedness of the declared solution relation`.

## 5. Foundation-level routing rule

For a new world law or state predicate, the following implication must not be assumed automatically:

`compatible at every finite precision -> exact realizable`.

Before making that inference, one needs a route-specific theorem such as:

- profinite closedness / subgroup separability;
- a valid local-global or Hasse-type principle for the declared equation class;
- an independent finite height/compactness bound that forces descent;
- another project-native structure proving that completion points are exact states.

Without such a theorem, the inverse-limit state belongs only to the **precision completion**, not necessarily to the exact world.

## 6. Bounded worlds are different again

If the admissible integer state family is independently bounded, it is finite. Then sufficiently fine modular reduction can become injective on that finite set, and any exact predicate on the bounded family can in principle be recovered from one large enough finite quotient.

So the ghost boundary concerns unbounded exact descent, not a claim that finite precision can never be exact on a finitely bounded world.

## 7. Prior-art boundary

Quadratic residues, Hensel lifting, CRT, profinite completion and intersective polynomials are standard prior mathematics. The specific polynomial witness is classical in character and is used here only as a pressure test.

The Enterprise Math conclusion is architectural:

> **precision completion and exact-world realization are separate layers; local-global descent is an additional theorem, not a consequence of precision refinement itself.**