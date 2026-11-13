# PREFIX-600-R2 — Sharp uniform-source phase recurrence for native X6-BRC

Date 2026-11-08. Native scientific input frozen at `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Author-side exact proof and executed symbolic checker; independent Driver review pending. Reuses PREFIX-595/596 positive 48-tail carrier and PREFIX-599 zero-weight minpoly, without changing P000 or the original 48 phases/96 bit-ports/576 typed actions.

## Exact model and declared observer

The four original STAR triples are `(1,3,6),(1,4,5),(2,3,5),(2,4,6)`. For the existing 48-dimensional post-first-step native phase carrier, fix native axis weights `(1,1,1,1,0,0)`. Gate target is phase `g=4` in original zero-based enumeration. Put `Q(z)=Q(0,z)` for the previously established 48-tail operator. Its row i is zero for source native axes 5 or 6. Otherwise for j in the original 3 native phase successors N(i): `Q[i,j]=1` when `i=g`, `Q[i,j]=2` when `i!=g,j!=g`, and `Q[i,g]=3+z` for the three gate-target transitions. All other elements are zero.

Let `e=ones(48)`. Define uniform right-source endpoint state `v_n(z)=Q(z)^n e`, arbitrary left phase observation `h_n(l,z)=l^T v_n(z)`, and the explicit all-phase sum `f_n(z)=e^T v_n(z)`. This is a *tail-phase observer*, not a claim that every original 96-bit-port endpoint is uniform.

## Theorem A: exact lower-order vector recursion

Set `s=4z+12`. For **every real z**, the polynomial vector identity is

```
Q(z)^7 e - 2 Q(z)^6 e - s Q(z)^3 e + 2s Q(z)^2 e = 0.
```

Equivalently, `P_z(Q)e=0` for `P_z(t)=t^2(t-2)(t^4-s)`. Since Q commutes with its polynomial, multiplying by `l^T Q^n` proves for **every n>=0 and every l**

```
h_(n+7) = 2 h_(n+6) + s h_(n+3) - 2s h_(n+2).
```

At z=1 the stronger exact vector identity `Q(1)^6e=16Q(1)^2e` holds and gives `h_(n+6)=16h_(n+2)`.

**Exact proof certificate.** The companion standalone script regenerates all 48 native phases and successors directly from the STAR triples, constructs Q over `Z[z]`, iterates `v_0=e; v_(n+1)=Qv_n`, then expands all 48 entries of the stated polynomial vector difference and obtains zero. At z=1 all 48 entries of the six-step difference are likewise zero. This is a complete finite symbolic calculation of an explicit polynomial matrix-vector identity, not a finite-sample extrapolation. By comparison the entire 48x48 Q matrix's generic sharp minimal polynomial from PREFIX-599 has degree ten.

## Theorem B: sharp minimal uniform-source order for all z>=0

For the scalar `f_n=e^TQ(z)^ne`, the **zero-start** minimal homogeneous recurrence order is **7** at all `z>=0,z!=1`, and **6** at `z=1`. The full uniform-source *vector* Krylov sequence has the same sharp orders (Theorem A bounds it; the scalar lower bound witnesses it).

To prove sharpness, form exact Hankel matrices `H_k(z)=(f_(i+j)(z))_{0<=i,j<k}`. Direct symbolic native enumeration gives

```
det H_7(z) =
 -260919263232 (z-1)^2 (z+3)^3
 (81z^3 - 27z^2 + 27z + 11)
 (4z^4 + 31z^3 + 123z^2 + 61z + 613).
```

On `z>=0`, the quartic is positive; the cubic is positive because its derivative `243z^2-54z+27` has negative discriminant and positive leading coefficient, while its value at zero is 11. Consequently `H_7` is nonsingular for all `z>=0,z!=1`, precluding a zero-start recurrence of order <7. At `z=1` the exact `det H_6(1)=-179821690748928!=0` rules out order <6; the stronger six-step vector identity supplies order 6.

Note: the factor `t^2` represents a two-stage transient. The *eventual* recurrence after the transient has order 5 for nonunit nonnegative z, and order 4 at z=1. The theorem reports **zero-start** order, not a general full-matrix recurrence.

## Exact rational generating function

As a formal power series in u, for all parameter z,

```
F_z(u)=sum_{n>=0} f_n(z) u^n
      = N_z(u) / ((1-2u)*(1-(4z+12)u^4)),

N_z(u)=48 + 3(z+32)u + 3(3z+61)u^2
      +18(z-1)u^3 -8(20z+77)u^4
      -32(11z+38)u^5 -768(z+3)u^6.
```

The numerator is obtained by directly enumerating the first seven native phase-output polynomials and applying the proved vector recurrence. The standalone checker verifies each coefficient in `Z[z]` and computes/factors the full H7 determinant exactly.

## Reusable algorithm and verification

For stationary z, compute `t^n mod P_z(t)` by polynomial modular exponentiation, then combine `e,Qe,...,Q^6e` to obtain all 48 phase outputs simultaneously. All 48 left-endpoint observations inherit this upper recurrence. No claim of universal end-to-end speedup is made: first-step encoding, 96-port output recovery, integer bit costs and input-observer scope must be charged for a specific workload.

Evidence: `PREFIX600_R2_uniform_observer_recurrence_checker.py` and `PREFIX600_R2_uniform_observer_recurrence_results.json` in this commit. The script verifies all 48 polynomial-vector coefficients; 7x7 symbolic Hankel determinant; 6x6 z=1 Hankel determinant; generating numerator; and 21-step exact independent parameter propagation for z=0,1,2,3/2,5. All executed local assertions passed.

Next precise question: classify which nonuniform initial source vectors have similarly reduced phase Krylov orders, identify their original 96-port lifting semantics, and compare exact jump and endpoint restoration costs. Native Research-Activity-ID: RA-79CF6AC40EFDC108B48AC3A7 (registered separately); no formal claim, native Result, or independent Driver review for this note.
