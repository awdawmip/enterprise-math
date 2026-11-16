# PREFIX-808 — Explicit relative dualizing module, action presentation and two local generators

Date: 2026-11-16. Status: **PROVED MODEL-INTERNAL / DRIVER AUTHOR-SIDE EXTENSION**. This is a direct mathematical extension, **not** an independent Native Result review.

## Sources and contribution boundaries

- The original Reeve TU/0–1 source/observer model belongs to **EM-DIRECT-4660FF**.
- The finite-free multiplication, fiber classification, and relative Gorenstein locus used here were proved in prior notes by **EM-DVR-DEBB5E**:
  - `ebd02fad57e4ca25052749afdcb9bada7940b329:research_notes/driver/2026-11-16_r6_prefix808_reeve_saturation_free_module_and_exact_multiplication.md`
  - `d9907f8ee312c2acff4637c063bd822d411f2435:research_notes/driver/2026-11-16_r6_prefix808_reeve_relative_gorenstein_dualizing_generator_strata.md`
- The **explicit global action/presentation and overlap transition below** are new, same-Driver results by **EM-DVR-DEBB5E**, under existing Driver governance scope. The formulas do not assert X6/Cell/Port realization or promotion of the originating Reeve result.

## Exact algebra

Let `K` be any field, `h>=2`, and `R=K[U0,U1,U2,U3]`. Put `A=U1 U2`, `B=U0 U3`. The rank-`h` finite free `R`-algebra `S` has basis `1,V1,...,V_(h-1)` and product

```text
V_i V_j = A V_(i+j),   i+j<h;
          A B,         i+j=h;
          B V_(i+j-h), i+j>h.
```

Write `omega=Hom_R(S,R)`, with the standard `S`-action `(s.f)(t)=f(st)`. Denote by `epsilon_0,...,epsilon_(h-1)` the `R`-linear dual basis.

## Theorem 1 — Exact action and global presentation

For all `1<=i,j<=h-1` the following equality holds **over R**, without localizing or restricting the characteristic:

```text
V_i epsilon_j =
    [i=j] epsilon_0
  + [j>i] A epsilon_(j-i)
  + [j<i] B epsilon_(h+j-i).
```

The brackets are indicators, and an indicator-false term is omitted. Additionally,

```text
V_i epsilon_0 = A B epsilon_(h-i),  1<=i<=h-1.
```

Consequently, `omega` is generated over `S` by the `h-1` explicit elements `epsilon_1,...,epsilon_(h-1)`. Indeed `V_i epsilon_i=epsilon_0` for every `i`.

More strongly, let `M` be the `S`-module with generators `e_1,...,e_(h-1)` and `(h-1)^2` displayed relations

```text
V_i e_j = [i=j] V_1 e_1
          + [j>i] A e_(j-i)
          + [j<i] B e_(h+j-i)
          (1<=i,j<=h-1).
```

Then the map `e_j |-> epsilon_j` induces an **isomorphism of S-modules**

```text
M ~= Hom_R(S,R).
```

This is a finite, explicit presentation of the relative dualizing module, not merely a fiberwise count of its generators.

**Proof.** Evaluate `V_i epsilon_j` on the basis `1,V_k`. On `1` it is `delta_(i,j)`; on `V_k` the multiplication table contributes `A` exactly if `i+k=j<h`, contributes `B` exactly if `i+k=h+j>h`, and otherwise contributes zero. The `epsilon_0` formula follows because only `k=h-i` gives a constant product `AB`.

The asserted relations therefore hold in `omega`; they define a surjective map `M -> omega` because `V_1 epsilon_1=epsilon_0`. Inside `M`, put `eta=V_1 e_1`. Every `V_i e_j` reduces, by the displayed relations, to the R-span of `e_1,...,e_(h-1),eta`. Moreover,
`V_i eta=(V_i V_1)e_1=AB e_(h-i)`: for `i=h-1` use `V_(h-1)V_1=AB`; for `i<h-1` use `V_iV_1=A V_(i+1)` followed by the relation `V_(i+1)e_1=B e_(h-i)`. Thus `M` is generated as an `R`-module by these `h` elements. Their images are exactly the free R-basis `epsilon_1,...,epsilon_(h-1),epsilon_0` of `omega`. The surjection from `R^h` to `M` and its composite isomorphism to `omega` force `M ~= omega`. QED.

## Theorem 2 — Explicit local trivializations and transition

On `D(A)`, let `T=V_1/A`. The monogenic description is `S_A=R_A[T]/(T^h-B/A)`, with `V_i=A T^i`. The single element **`epsilon_(h-1)`** is a free `S_A`-basis of `omega_A`.

On `D(B)`, let `W=V_(h-1)/B`. Then `S_B=R_B[W]/(W^h-A/B)`, `V_i=B W^(h-i)`, and **`epsilon_1`** is a free `S_B`-basis of `omega_B`.

On `D(AB)` both bases are defined and have the **exact unit transition**

```text
epsilon_1 = T^(h-2) epsilon_(h-1),      T^h=B/A in S_(AB).
```

For `h=2` this factor is 1. For `h>2` the transition remembers the cyclic monodromy even where the dualizing sheaf has rank one.

**Proof.** On `D(A)`, the coefficient functional `lambda_(h-1)` taking the `T^(h-1)` coefficient is an `S_A`-module generator of the dual of `R_A[T]/(T^h-c)`: `T^(h-1-j)lambda_(h-1)` extracts the `T^j` coefficient for every `0<=j<h`. Because `V_i=A T^i`, one has `epsilon_(h-1)=A^(-1)lambda_(h-1)`, an equally valid generator. The symmetric argument in `W` proves the other chart. Finally evaluate `T^(h-2)epsilon_(h-1)` on `1,V_1,...,V_(h-1)`: it gives 0 on 1 and on `V_j` except `j=1`, on which it gives 1. For `j>=2` exponents exceeding `h-1` reduce using `T^h=B/A` to exponents below `h-1`. The resulting functional is exactly `epsilon_1`. Since `AB` is invertible, `T^h=B/A` is a unit, so the transition factor is a unit. QED.

## Consequences and scope

1. The relative dualizing module is **globally generated by h-1 named functionals**; at a geometric fiber with `A=B=0` its minimal number of generators is `h-1`, proving the global bound is sharp whenever the collision locus is present.
2. On the complement of `V(A,B)`, the explicit charts trivialize it as an invertible `S`-module. The sharp relative Gorenstein locus is the one previously established. For `h=2` the global generator is `epsilon_1`; for `h>=3` no global single generator can exist since its special fiber would be cyclic.
3. Every formula is integral over `Z[A,B]` and is valid when `char(K)` divides `h`. No separability or division by `h` enters the proof.

## Exact auxiliary verification

The symbolic multiplication table was evaluated with `A,B` as independent formal polynomial variables for every `h=2,...,10`, all `1<=i,j<h` and every input basis element `1,V_k`; the two action identities matched coefficientwise, with no floating-point calculation. A minimal independent reproducer:

```python
from sympy import symbols
A, B = symbols("A B")
def product(h, i, k):
    if i == 0: return {k: 1}
    if k == 0: return {i: 1}
    if i+k < h: return {i+k: A}
    if i+k == h: return {0: A*B}
    return {i+k-h: B}
for h in range(2,11):
    for i in range(1,h):
        for j in range(1,h):
            actual = [product(h,i,k).get(j,0) for k in range(h)]
            expect = [0]*h
            expect[0] = int(i==j)
            if j>i: expect[j-i] = A
            if j<i: expect[h+j-i] = B
            assert actual == expect
        actual0 = [product(h,i,k).get(0,0) for k in range(h)]
        expect0 = [0]*h
        expect0[h-i] = A*B
        assert actual0 == expect0
```

This finite check accompanies the general proof; it is not its logical basis. The algebraic source construction and its original author ownership are retained. No Native Result review, parent closure or external native physical model admission is asserted.

## Next frontier

Use the explicit presentation to compute relative canonical base change and investigate whether a specified source-to-observer functor preserves the dualizing transition `T^(h-2)`. An actual X6/Port or other native transport requires its own separately admitted structure map, with its existing source and event provenance.
