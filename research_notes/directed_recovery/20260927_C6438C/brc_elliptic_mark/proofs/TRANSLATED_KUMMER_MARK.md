# A translated Kummer coordinate recovers primitive return depth

Status: **PURE_SYMBOLIC_OBSERVER_CANDIDATE / NOT_EXECUTED / NOT_ADMITTED**. Shared author activity `RA-CAAAC604CB513AEA8BBC1DFC`. This is a bounded symbolic derivation, with no numerical oracle, scientific execution, professional query or remote write. It addresses the lost valuation proved in `KUMMER_RETURN_VALUATION.md`, SHA-256 `3b7a522fdb487bb5fdbe054a8e41a517f7f067881fdd5ac1822d367a1975f222`; that file remains unchanged.

## 1. Exact hypothesis and conclusion

Let R=Z/NZ, N odd, and let the smooth Montgomery curve be

`E: B y^2=x^3+A x^2+x`, with `gcd(B(A^2-4),N)=1`.

Its ordinary plane projective model is `B Y^2 Z=X^3+A X^2 Z+X Z^2`, with identity O=[0:1:0]. Fix a known affine point P=(a,b) with b a unit and a paid curve-equation certificate. The commonly requested ladder condition that a be a unit already follows here: `B b^2=a(a^2+A a+1)` is a unit. Keep that fact as an explicit chart obligation rather than assuming it from a purported input tuple.

Let Q be a genuine curve point, represented by a unimodular ordinary projective triple `(X_Q,Y_Q,Z_Q)`. Suppose the two supplied unimodular Kummer pairs represent the **same actual Q and its translate Q+P**:

`(X0:Z0)=x(Q)`, `(X1:Z1)=x(Q+P)`, with x(O)=[1:0].

Define

`W=X1-a Z1`,

`g_mark=gcd(N,Z0,W)`, `g_point=gcd(N,X_Q,Z_Q)`.

Then the exact divisor identity is

`g_mark=g_point`.                                         (1)

It includes every prime-power valuation, with no square inflation. The point Q=mP is an intended source of these adjacent pairs, but the observer theorem applies to any Q with the stated translation witness. No factorization of N, order, point Y-coordinate, or square root is required to evaluate W or its gcd once the valid pair certificate is available.

## 2. Local identity near O

Work at any p^e component of N. If Q reduces to O, Y_Q is a unit. Put

`u=X_Q/Y_Q`, `v=Z_Q/Y_Q`,

`h=B-Au^2-u v`, `s=h-a u^2`.

Both u and v lie in the maximal ideal, while h and s are units. The curve equation gives

`h v=u^3`.                                                (2)

Consequently the full point-identity ideal `(u,v)` is `(u)`, and the first Kummer pair has the regular local representative `[h:u^2]`. This uses the x-coordinate morphism, not division of an actual residue pair by the nonunit u.

The exact translated-coordinate formula is

`x(Q+P)-a = u R(u,v)/s^2`,                                 (3)

where

`R(u,v)=-2 B b h + (3a^2+2Aa+1) h u + a(1-a^2)u^3`.

In particular, R is a unit, since its reduction modulo p is `-2 B^2 b`. The multiplier R/s^2 reduces to `-2b`, so the translated difference has a simple zero in u, not a double zero.

### Explicit algebra and the nonunit-cancellation boundary

On a valid generic affine overlap the chord slope is

`ell=(1-bv)/(u-av)=(h-bu^3)/(u s)`.

The Montgomery addition formula gives `x(Q+P)=B ell^2-A-x(Q)-a`. Thus the numerator for `x(Q+P)-a`, over denominator `u^2 s^2`, is

`B(h-bu^3)^2-h s^2-(A+2a)u^2 s^2`.

Expansion, using `B-h-Au^2=uv`, (2), and `B b^2=a^3+A a^2+a`, gives exactly

`-2 B b h u^3 + (3a^2+2Aa+1)h u^4 + a(1-a^2)u^6`

`=u^3 R(u,v)`.

This verifies the sign and the last coefficient in (3). It must not be read as cancelling u^2 in an arbitrary residue ring.

A precise extension argument is available without such a cancellation. Use a formal indeterminate U over the local residue ring. The equation

`B V=U^3+A U^2 V+U V^2`

has a unique solution `V(U) in U^3 R[[U]]`, because its coefficient of V at (0,0) is the unit B. In the Laurent series ring, U is invertible and the displayed chord calculation is valid; its result (3) lies in the power-series ring because s has unit constant term. It is the formal translate near the affine point P. Now substitute the actual u, which is nilpotent in the finite local ring. All power series evaluate by finitely many terms. The resulting V(u) equals the actual v: subtracting their equations gives `(v-V(u))[B-Au^2-u(v+V(u))]=0`, whose bracket is a unit. This proves (3) at the actual point without ever inverting its u. The formal argument is proof only, not a proposed production propagation algorithm.

## 3. Equality of ideals and all prime-power gcds

If Q is not O modulo p, its x-coordinate is finite modulo p. The primitive Kummer denominator Z0 is then a unit. At least one of X_Q,Z_Q is a unit as well, because otherwise a unimodular curve point would reduce to [0:1:0]. Hence both ideals in (1) are the entire local ring.

If Q is O modulo p, then Q+P reduces to the finite point P, so Z1 is a unit. Any primitive representative of the first Kummer point differs locally from `[h:u^2]` by a unit. Therefore

`(Z0)=(u^2)`,

`W=Z1(x(Q+P)-a)=Z1 u R/s^2`, so `(W)=(u)`.

It follows that

`(Z0,W)=(u^2,u)=(u)=(u,v)=(X_Q,Z_Q)`

in the local ring. All unit changes of projective representatives preserve these ideals. Taking all p^e components proves (1), including nilpotent returns and the exact identity Q=O.

This also explains why W alone is insufficient. A translated x-coordinate can equal x(P) at another point, for example Q=-2P when that is distinct from O. The simultaneous denominator Z0 removes such an affine false match: away from O it is a unit. The theorem concerns the intersection of the two conditions through their common gcd, not the union of their factor supports.

The b-unit assumption is substantive. At a ramified x-coordinate point P with b nonunit, the coefficient `-2b` need not be a unit, so this proof gives no unsquared-depth guarantee. Oddness and smoothness are likewise explicit hypotheses.

## 4. Minimal executable observer contract

An existing **certified** adjacent-pair ladder can add the following observer:

1. Retain the fixed affine coordinate a, and the actual adjacent primitive Kummer pairs for Q and Q+P.
2. Compute `a Z1` and `W=X1-a Z1` with actual typed modular arithmetic.
3. Compute `gcd(N,Z0,W)` using actual typed Euclidean operations and verify every proper factor by exact division.
4. Preserve source, setup, ladder, primitive-coordinate/adjacency receipts, failed or saturated outcomes, and complete costs.

The extra expression uses one modular multiplication and one subtraction, then a common gcd. This is a constant number of modular arithmetic interfaces, not a constant bit-cost or free gcd claim. The existing neighboring point is reused; no extra full Y lift is needed for this observer. A projective base point would instead require the corresponding cross product and a unit affine-chart denominator, with the additional operations charged.

The hypothesis is not fulfilled merely by naming two arbitrary pairs as ladder outputs. A valid transition certificate must establish both their primitive projective meaning and their common adjacent-point relation over all local components. Common nonunit scaling, an all-zero pair modulo a prime, or a silently cancelled ladder factor destroys that guarantee. Such events require a retained factor/failure branch or a proved alternate chart. Neither this note nor the frozen Kummer note implements that nonlinear native certificate.

## 5. Result and remaining gap

The proposed marked observer is correct under the stated certificate contract. It restores the full identity ideal that an isolated x-coordinate squares at repeated prime factors. On squarefree N its factor support agrees with the ordinary Kummer infinity observer; this theorem alone gives no new separation probability. It also does not prove the common gcd is cheaper than all single-coordinate factor probes.

This is a geometric observer repair using standard elliptic translation and a supplied adjacent Kummer pair, not a new smoothness theorem or a completed factoring algorithm. Choosing the curve, base point and useful multiplier, validating the nonlinear ladder, managing exceptional charts, and proving total native cost remain unpaid obligations. No general Shor closure, advantage over classical elliptic-curve methods, or executed BRC elliptic primitive is asserted.

Reviewer actual read context: main@7a63984; coordinator current shared context: main@8c23cca3 / GLOBAL_KNOWLEDGE_V1.
