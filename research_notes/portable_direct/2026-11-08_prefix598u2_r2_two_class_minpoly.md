# PREFIX-598U2-R2 | Explicit two-class native X6-BRC: sharp degree 22 / 28 recurrence

Date: 2026-11-08. Author-side exact algebraic special-family theorem, continuing PREFIX-598U-R2 in this branch; frozen native model `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Retains native 96 ordered ports, 576 labeled actions and all original observers. No P000 change.

## Exact parameter family and theorem

Fix all six native axis weights `x=(1,1,1,1,2,2)`, and the same real constant gate weight z on every 48-tail step. Let `Q_z` have entries `(Q_z)_{i,j}=x_(a(i))` when i=g and j in N(i), otherwise `2*x_(a(i))` for j in N(i), j!=g, and `x_(a(i))*(3+z)` for j=g in N(i), where g=4 and a(i) is the frozen source axis of native phase i. Set A=Q_1 and t a formal spectral variable.

Define polynomials by exact factored forms:

```
F30(t)=(t-2)(t+2)(t²-8)^6(t²+24)^2(t⁴+12t²-96)^3.
H10(t)=(t-2)(t+2)(t²-8)(t²+24)(t⁴+12t²-96).
P18(t)=(t-2)(t+2)(t⁴+12t²-96)
        (t³-2t²-24t-144)(t³-2t²+8t+48)
        (t³+2t²-24t+144)(t³+2t²+8t-48).
B14(t)=4*(9t^14+160t^12+5200t^10-111488t^8
          +104448t^6-37601280t^4+429981696t²-1146617856).
R_z(t)=P18(t)-(z-1)B14(t).
```

**Theorem.** For every real z the exact characteristic polynomial is

`chi(Q_z,t)=F30(t) R_z(t)`.

Its **sharp monic minimal polynomial** is

```
z=1:   mu(Q_z,t)=rad(F30(t)P18(t)),  degree 22
z!=1:  mu(Q_z,t)=H10(t) R_z(t),       degree 28.
```

Here rad means the product of distinct irreducible rational factors of its exact polynomial argument; it is explicit from the displayed factors. Thus all exact tail observation sequences obey the indicated degree22 or degree28 recurrence. The z!=1 conclusion holds also for z=0 and for exceptional multiple roots of R_z.

## Proof

Reconstruct the same original 48 phases and typed native actions as the PREFIX-598U proof; row-scaled transfer Q_z has the rank-one perturbation `Q_z=A+(z-1)ue_g^T`, now `u_i=x_(a(i))*1[g∈N(i)]`. Exact integer characteristic calculations at gate values z=1,2 and the matrix determinant lemma yield `chi(A)=F30 P18`, `chi(Q_2)-chi(A)=-F30 B14`, hence `chi(Q_z)=F30 R_z` as a polynomial identity for all z.

The square-free radical `rad(chi(A))` annihilates A in all 2304 matrix entries, so A is diagonalizable. Exact rational Krylov elimination gives `dim span(u,Au,...,A^17u)=18`. This A-invariant subspace U is invariant under all Q_z and has cyclic generator u under Q_z. Hence the characteristic and minimal polynomial of Q_z|U is R_z. The quotient V/U has the unchanged A-action and exactly the 10 distinct spectral factors H10; its minimal polynomial is H10. Therefore H10 R_z annihilates Q_z. The exact polynomial GCD `gcd(P18,B14)=1` also gives `gcd(H10,R_z)=1` whenever z!=1, so H10 R_z is sharp. For z=1 the square-free radical of chi(A) is exactly the base minimal polynomial of degree22.

This constitutes a new fixed two-class instance showing a larger sharp recurrence order (22 or 28) than the all-equal six-axis case (10 or 18). It does not presuppose a result for arbitrary six-axis weights.

## Exact executed checks

The standalone extension script `PREFIX598U2_R2_two_class_certificate.py` imports the native 48-phase reconstruction from `PREFIX598U_R2_uniform_gate_certificate.py`. It exactly verifies: full characteristic identities at z=1 and 2, diagonalizability of A via square-free radical, 18-dimensional Krylov rank, `gcd(P18,B14)=gcd(H10,B14)=1`, and full 48×48 annihilator matrix identities at z=0,1,2,3. All assertions passed in the local SymPy execution. Also computed alternative explicit weight profiles: x=(1,1,1,1,1,2) had square-free minimal degrees 24 (z=1) and 30 (z=2); those are exact finite examples, not a general theorem.

## Next

Study the symmetric weight parameter `x=(1,1,1,1,w,w)` over `Q(w)` and determine the exceptional values at which the 28-degree generic z!=1 minimal polynomial collapses. Couple this to the exact bit-complexity and batch-query workload comparison; preserve original gate-label observer and full 96-port endpoint adapter.
