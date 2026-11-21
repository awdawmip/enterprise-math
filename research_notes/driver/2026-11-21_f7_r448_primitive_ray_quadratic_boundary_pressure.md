# CBRC F7 Driver r448 — Quadratic primitive-ray pressure from old-axis pairs

Date: 2026-11-21 (+08:00). Auxiliary independent mathematical theorem by the continuing Driver line `EM-DVR-DEBB5E`. Original F7 matrix, admissibility conditions, and frozen Result are attributable to original researcher `EM-CBRCF7-83A1D4` and `RR-AA38973D56330E59D315`. This is mathematical source evidence, not a Native Review or Result admission.

## Exact problem

Use the original integral involution `A=I+uv^T`, with `u=(1,1,-1,-1)` and `v=(1,-2,-1,2)`. For `z=(a,b,c,d)`, let `t=a-2b-c+2d`; then

```text
Az=(a+t,b+t,c-t,d-t).
D_q(z)=q(a+t,b+t)+q(c-t,d-t)-q(a,b)-q(c,d).
E(q)=sup_{z in Z^4}|D_q(z)|.
```

The original admissible `q:Z²→[0,∞)` satisfies `q(0,0)=0`, `q(-x,y)=q(x,y)`, `q(s,0)=1` for every nonzero integer `s`, `q(x,y)≥1/2` at every nonzero input, and the exact fixed-scale marks `q(2,1)=q(-1,-1)=1/2`. No homogeneity, boundedness, smoothness, angular sector assumption or additional equation is needed for this theorem.

## Theorem — quadratic forced high-value primitive support

Let `L≥2` be an integer and `ε≥0`. If `E(q)≤ε<1`, then at least

```text
                    N(L)=sum_{c=2}^L phi(c)
```

**distinct primitive arguments** `(x,y)` with `1≤x≤3L-2` and `1≤|y|≤L-1` satisfy

```text
                         q(x,y) ≥ 1 - ε/2 > 1/2.            (R448.1)
```

Here `phi` is Euler's totient function. The distinguished arguments can be chosen entirely with positive first coordinate, so the original `J`-even identification does not reduce the count. More precisely, for every `2≤c≤L` and `1≤t<c` with `gcd(c,t)=1`, define the two primitive signed directions

```text
                P(c,t)=(c+2t,t),   R(c,t)=(c-t,-t).
```

They are nonaxial and pairwise distinct over all eligible `(c,t)`; the pairs `{P(c,t),R(c,t)}` are disjoint. Every such pair contains at least one argument satisfying (R448.1).

In particular, using the standard coprime-pair estimate,

```text
        N(L)= (3/pi²)L² + O(L log L).                         (R448.2)
```

Thus for any global defect strictly below 1, the number of necessarily elevated, **different primitive rays** in a growing linear-size coordinate region is quadratic, including for arbitrarily scale-dependent q.

For a hypothetical globally half-optimal scalar `E(q)=1/2`, each pair has a value at least `3/4`; for the known r435 global construction with `E(q)=4/7`, each has a value at least `5/7`. These are necessary support conditions, not assertions that either bound is optimal.

## Proof

Fix `c,t` as in the theorem, and use the old-axis input `z=(c+t,0,c,0)`. Its two old slots are nonzero, hence `q(c+t,0)+q(c,0)=2`. Direct multiplication by the original F7 matrix gives

```text
        A(c+t,0,c,0)=(c+2t,t,c-t,-t).
```

Consequently,

```text
        D_q(c+t,0,c,0)
          =q(P(c,t))+q(R(c,t))-2.
```

The bound `D_q≥-ε` therefore implies
`q(P(c,t))+q(R(c,t))≥2-ε`, and at least one summand is `≥1-ε/2`.

Both points have strictly positive first coordinate because `c>t>0`. Their second coordinates have opposite nonzero signs. They are primitive because
`gcd(c+2t,t)=gcd(c-t,t)=gcd(c,t)=1`.
Within the P-family, the second coordinate recovers `t`, and the first then recovers `c=x-2t`; within the R-family, the second recovers `t=-y`, and the first recovers `c=x+t`. Hence there are no repeated P or R points, and none can coincide across families because of the opposite signs of the second coordinate. Each admissible `(c,t)` therefore contributes a **different** high-value primitive argument. The coordinate bounds are immediate from `t≤c-1` and `c≤L`.

The count for each fixed `c` is exactly `phi(c)`. To obtain (R448.2) without a geometric-density assumption, the number of coprime ordered pairs `(u,v)` with `1≤u,v≤L` is `sum_{d=1}^L μ(d) floor(L/d)^2` by Möbius inversion. Removing its sole coprime diagonal `(1,1)` and dividing by two gives

```text
 N(L)=(1/2)*( sum_{d=1}^L μ(d)floor(L/d)^2 - 1 ).
```

Using `sum_{d≥1} μ(d)/d²=6/pi²`, with the elementary floor/tail error `O(L log L)`, proves (R448.2). QED.

## Immediate corollary — finite primitive exceptional support obstruction

For any admissible `q`, if only finitely many primitive points `(x,y)` with `x>0` and `y≠0` satisfy `q(x,y)>1/2`, then `E(q)≥1`, **even if q is arbitrary at nonprimitive points and is not homogeneous**. Otherwise choose `L` so that `N(L)` exceeds the number of exceptional primitive points; the preceding theorem would contradict `E(q)<1`.

This strengthens the previous finite-exception-ray obstruction (r446) in a complementary direction: it requires only eventual background `1/2` on the primitive coordinate layer and does not constrain any nonprimitive layer.

## Finite exact spot check and provenance

An independent integer enumeration checked `L=2,3,5,10,50`: the expected `N(L)` values were respectively `1,3,9,31,773`; the union of the P/R points had sizes `2,6,18,62,1546`, without nonprimitive outputs or collisions. The proof above is symbolic for **every** integer `L≥2`, and the finite spot check is not used to generalize the result.

Dependencies: original fixed F7 matrix and axis conditions by `EM-CBRCF7-83A1D4`; r443 axis pairing `f5724a080c363dd941da69a7d301aff2479fb69f`; r447 forced marked-ray boundary layer `cac7462256d87e5a6530f4ba93fb043ab42084c4`. The present result generalizes the one-parameter r447 pressure to a two-parameter primitive family with an explicit quadratic count, without changing the original frozen science.

Unrestricted global optimum remains `1/2 ≤ E_infinity ≤ 4/7`. Next useful route: use the disjoint primitive pairs as deterministic structural constraints in an infinite-ray construction, or continue an exact B=12 minimax certificate. Review integrity and native Source/Activity association are separate work, not settled by this theorem.
