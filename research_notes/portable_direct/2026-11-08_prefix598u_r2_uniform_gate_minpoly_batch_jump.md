# PREFIX-598U-R2 | Uniform-gate native X6-BRC: exact degree-10/18 minimal polynomials and logarithmic-depth jumps

Date: 2026-11-08; role: independent author-side TASK_RESEARCH; mathematical admission: UNREVIEWED. Scientific model frozen at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Direct predecessor: PREFIX-597-R2 at `511ad9d811cd6e853296749baa087880db89f7ef`. The suffix "598U" distinguishes this spectral result from the concurrently existing separate PREFIX-598 positive image cone PR #1807. The P000 six-axis world and frozen native model remain unchanged.

## Definition and scope

The original native operator has 48 phases, 96 ordered bit-ports, 576 axis-labeled arcs and three exceptional gate arcs. Fix all six axis weights equal to 1, and fix the same gate parameter `z` at **every** step. Write `g=4` for the original gate-target phase and `N(i)` for the three native successors. Use the already-proved exact 48-state post-first-step positive carrier of PREFIX-596/597, whose coordinates are `v_i=r_(i,0)+r_(i,1)` for `i!=g` and `v_g=r_(g,0)=r_(g,1)`. Define `Q_z` by:

```
(Q_z v)_g = sum(v_j for j in N(g))
(Q_z v)_i = 2 sum(v_j for j in N(i) if j!=g)
              + 1[g in N(i)] (3+z) v_g                 (i!=g).
```

The original first-step encoder and complete 96-port terminal decoder are still used. This result concerns the stationary, equal-axis *transition carrier*, not a reduction of P000 native spatial dimension. The indeterminate `t` below is a spectral variable, not the world's time coordinate.

Define three integer polynomials:

```
H8(t) = (t²-4)(t²+12)(t²-4t+12)(t²+4t+12)
      = t^8+16t^6+160t^4+768t²-6912
P10(t)= (t²-36)H8(t)
      = t^10-20t^8-416t^6-4992t^4-34560t²+248832
B6(t) = 4(t²-12)(5t^4+72t²+1296)
      = 20t^6+48t^4+1728t²-62208
R_z(t)= P10(t)-(z-1) B6(t).
```

## Theorem (exact over Q for rational z, over R for real z)

The characteristic polynomial is, **for every z**,

```
chi(Q_z,t) = F38(t) R_z(t),
F38(t)=(t-2)^12(t+2)^12(t²+12)^5(t²-4t+12)(t²+4t+12).
```

Its monic minimal polynomial has a sharp gate-dependent order:

```
z=1:   mu(Q_z,t) = P10(t),           degree 10
z!=1:  mu(Q_z,t) = H8(t) R_z(t),     degree 18.
```

These are polynomial **identities** for all eligible parameters, including `z=0` and exceptional repeated spectral roots. Consequently every scalar terminal observation `s_n=l Q_z^n v` satisfies the corresponding exact degree-10 or degree-18 linear recurrence for all `n>=0`.

## Full proof

1. Set `A=Q_1`, `u_i=1[g in N(i)]`, and `e=e_g`. The gate target has no self-successor. The original graph definition then gives the *exact rank-one update*
   `Q_z=A+(z-1)u e^T`.
2. Exact integer characteristic computation of the native 48-phase matrix gives `chi(A,t)=F38(t)P10(t)`. Independent Horner evaluation of the full 48×48 matrix verifies the **2,304** entries of `P10(A)=0`. The ten complex roots of `P10` are distinct; each occurs in `chi(A)`, so `mu(A)=P10` and `A` is diagonalizable over its splitting field.
3. The matrix determinant lemma gives `chi(Q_z,t)=chi(A,t)[1-(z-1)e^T(tI-A)^(-1)u]`, affine in `z-1`. Direct *exact* characteristic calculation for `z=2`, and subtraction from `chi(A)`, gives `chi(Q_2)-chi(A)=-F38 B6`. Since the expression is affine in the gate perturbation, this proves the characteristic identity for **all z**.
4. Let `U=span(u,Au,...,A^9u)`. Exact row reduction gives `dim U=10`. By `P10(A)=0`, `U` is invariant under A and hence under `Q_z` (the correction has image in the line of u). The vectors `u,Q_z u,...,Q_z^9u` are a unitriangular change of the A-Krylov list, so u remains a cyclic vector for `Q_z|U`. The quotient action on V/U is exactly that of A, with characteristic polynomial F38. Thus `chi(Q_z|U)=R_z`, and `mu(Q_z|U)=R_z`.
5. Each of the ten distinct A-eigenvalues contributes exactly one line to U. The quotient `V/U` therefore carries precisely the eight distinct eigenvalues of `H8`, all present, with a square-free quotient minimal polynomial `H8`. Hence `H8(Q_z)V subset U`, and the commuting product `R_z(Q_z)H8(Q_z)=0` is an exact degree-18 annihilator.
6. Exact Euclidean arithmetic gives `gcd(P10,B6)=1`, so for `z!=1`, `gcd(H8,R_z)=1`. The minimal polynomial of the full operator must be divisible by both the 10-degree cyclic subspace polynomial R_z and the 8-degree quotient polynomial H8. Their coprime product is already an annihilator, proving sharp degree18. At z=1 the established minimal polynomial is P10 of degree10.

## Exact jump algorithm and scope

Let `m=mu(Q_z)`, `k=deg m` (10 or 18). Compute `c(t)=t^n mod m(t)` by binary polynomial exponentiation and Euclidean reduction, then evaluate:

```
Q_z^n v = sum(c_j Q_z^j v for j in range(k)).
```

This is an all-endpoint exact integer algorithm with `O(k² log n + 147k + 48k)` arithmetic operations for one 48-vector, including 147 typed coefficient operations per Krylov step. The ordinary stepwise path uses `O(147n)` such typed transitions. Integer bit lengths, input conversion and complete terminal-port recovery are included in any end-to-end bit-cost assessment; uniform stationary gating is an explicit hypothesis of the improvement.

## Executed evidence

A self-contained Python/SymPy checker reconstructs the original 48 phases and all 576 native typed arcs. Exact checks: `chi(Q_1)=F38 P10`, `chi(Q_2)=F38(P10-B6)`, `P10(Q_1)=0`, rank of the ten-vector Krylov matrix =10, `gcd(P10,B6)=1`, and full 48×48 annihilator for each z in 0,1,2,3,5. It also performs 35 exact jump-versus-step iterations, gate z in 0,1,2,3,5 and n in 0,1,2,8,32,128,512. All pass. At n=512, maximum exact integer bit lengths for these five gates were 1327,1331,1335,1339,1346.

One untuned single-process Python exact-integer timing sample for z=2 and n=128/512/2048 recorded iterative tail 2.669/12.397/81.161 ms versus polynomial jump 0.656/0.857/3.042 ms, with identical 48-dimensional exact outputs. These times are descriptive, not a universal cross-implementation comparison.

## Remaining question

Determine invariant factors under symmetric two-class and general six-axis stationary weights. Compare original optimized 96-port adjoint and the 48-state polynomial-jump path on repeated terminal queries, with complete initial and final adapters and exact bit cost. Extend nonstationary gate sequences only after deriving a separate valid certificate. The project-native Result/CLAIM and independent mathematical review remain pending.
