# D25/LIFT: when two scalar square observers become complete — simple-spectrum semilinear last-digit classification

2026-10-25 · TASK_RESEARCH portable author derivation plus exact finite checks · **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM / NO_NEW_NATIVE_CHECKPOINT**. Logical Research lane chatgpt-research-hourly-enterprise-math-20260923, parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7. Frozen original science pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

This is a **second, distinct** finite-ring result after the scalar-square twisted near-identity classification. The earlier rank-two loss witness proves that trace and determinant can fail; this theorem identifies a precise **sufficient and necessary complete two-scalar observation in the stated fixed-base simple-spectrum class**, without claiming universal completeness.

## Fixed coefficient carrier and exact hypotheses

Let p be an odd prime, r >= 2, q=p^(r-1), A_r=Z/p^rZ, R_r=A_r[T]/(T^2-2), sigma(T)=-T. Let c1,c2 be units in R_r and set

    C0 = diag(c1,c2),     s_i = c_i sigma(c_i) in A_r^*.

Assume the two reductions of s1 and s2 **differ modulo p**. No prior rank-one norm model, crystalline Frobenius or H0/B0 basis is assumed. Define the top-digit semilinear family

    C_D = (I_2+qD) C0,     F_D(v) = C_D sigma(v),   D in M_2(R_1).

Only near-identity gauges P_X=I_2+qX, X in M_2(R_1), are allowed. This is an auxiliary rank-two coefficient module, **not** a two-dimensional native plane or a complete Enterprise spatial slice.

## Theorem: complete fixed-base near-identity gauge classification by trace and determinant of F^2

Write D_ii = a_i+b_i T in R_1, with a_i,b_i in F_p, and define the fixed-baseline readout

    Phi(D) = (a_1,a_2) in F_p^2.

Then:
1. Every C_D is near-identity gauge-equivalent to exactly one

       C_can = (I_2+q diag(a_1,a_2)) C0.

2. Two matrices in this family are equivalent under an allowed gauge **iff** their Phi vectors agree.
3. The **pair of scalar observations** tr(F_D^2) and det(F_D^2), read as complete A_r residues modulo p^r, is a complete invariant for this equivalence. Its last-digit data determine a_1,a_2 constructively.
4. There are exactly p^2 gauge classes, contrasting with p^4 for the scalar-square baseline in the previous note.

For the explicit reconstruction, set S_D=C_D sigma(C_D) and let

    B = [det(S_D)/(s1*s2) - 1] / (2q) mod p,
    H = [tr(S_D) - s1 - s2] / (2q) mod p.

The numerators are divisible by q in A_r, so dividing produces well-defined modulo-p residues. With bar(s_i)=s_i mod p,

    a1 = (H - bar(s2)*B) / (bar(s1)-bar(s2)) mod p,
    a2 = (bar(s1)*B - H) / (bar(s1)-bar(s2)) mod p.

These formulas require the **actual fixed reference s1,s2**; the two bare numbers without their source baseline do not declare a canonical CM comparison.

### Proof and constructive gauge

Define tau(X)=Cbar0 sigma(X) Cbar0^{-1} in M_2(R_1). The earlier direct expansion, which does **not** need scalar square, gives

    P_X^{-1} C_D sigma(P_X)
       = (I_2+q[D+(tau-1)X]) C0.

On the diagonal components, tau acts as sigma; the sigma-odd component b_i T is removed by choosing X_ii=b_i T/2. On the off-diagonal (i,j) component, tau acts on z in R_1 by

    tau_ij(z) = (bar(c_i)/bar(c_j)) sigma(z),
    tau_ij^2(z) = rho_ij z,
    rho_ij = bar(s_i)/bar(s_j) != 1.

Thus tau_ij-1 is **invertible** on that off-diagonal F_p-vector space, with explicit inverse

    (tau_ij-1)^{-1} = (tau_ij+1)/(rho_ij-1).

Taking X_ij = -(tau_ij+1)(D_ij)/(rho_ij-1) removes the corresponding off-diagonal coefficient *exactly at top precision*. These diagonal and off-diagonal choices are independent at first order q because q^2=0, so a unique diagonal sigma-even normal form is obtained. Conversely, a_i cannot be changed by any allowed gauge: the diagonal variation is sigma(X_ii)-X_ii, which has zero sigma-even component. This proves (1), (2), and the p^2 count.

For the canonical representative, the full square is diagonal with entries

    s_i (1+2q a_i).

Therefore the trace and determinant of S_D, which are invariant under all these gauges because F^2 changes by P_X-conjugation, obey the exact congruences

    tr(S_D)  = s1+s2+2q(s1*a1+s2*a2),
    det(S_D) = s1*s2[1+2q(a1+a2)]            (mod p^r).

Their normalized top digits are H = bar(s1)a1 + bar(s2)a2, B=a1+a2. The 2-by-2 linear system has determinant bar(s1)-bar(s2) != 0, giving the displayed recovery formulas and proving (3). QED.

No unqualified statement about arbitrary full GL_2(R_r) gauge, all reductions, noninvertible Frobenius, repeated-square eigenvalues, or actual native crystalline observations follows from this theorem.

## Explicit contrast at p=373 (same auxiliary coefficient ring)

At p=373,r=2 use C0=diag(1,2), s1=1,s2=4. Then a1,a2 are completely recovered from

    B = [det(S_D)/4 - 1]/(2*373) mod373,
    H = [tr(S_D) - 5]/(2*373) mod373,

    a1 = (H-4B)/(-3) mod373,   a2=B-a1 mod373.

The off-diagonal D=E12 is completely removable by an allowed gauge and changes neither scalar. Unlike the scalar-square baseline C0=diag(2,-2), whose same-p coefficient ring has equal square eigenvalues (4,4), the simple spectrum (1,4) leaves **no top-digit off-diagonal extension gauge invariant** in this restricted family.

The previous repeated-eigenvalue example D=T E12 at C0=diag(2,-2) has a nonzero full-square upper-right entry 2984T modulo 373^2 while trace and determinant remain at their baseline values. It is an exact obstruction to dropping the distinct-eigenvalue hypothesis. The two baselines must not be conflated with one another or with a Source-fixed H0/B0 basis.

## Finite reproducibility certificate

Used exact pair arithmetic a+bT, sigma(a,b)=(a,-b), and direct 2x2 matrix multiplication over Z/p^rZ. For each p in {13,19,373} and r in {2,3}, tested 31 deterministic pseudorandom D (total **186 / 186 passing**) by:
- constructing X_ii=b_iT/2 and X_ij=-(tau_ij+1)D_ij/(rho_ij-1);
- verifying P_X^{-1}C_D sigma(P_X) = (I+q diag(a1,a2))C0 modulo p^r;
- computing tr and det of the **raw** square C_D sigma(C_D), verifying the coefficients lie in A_r and reconstructing the exact (a1,a2) via B,H above.

The algebraic proof is general. This check is author finite validation, not an independent review, Lean certificate, or native Frobenius experiment.

## Observer/provenance implications and next native comparison

BRC information-preservation application: the permissible observer is (trace, determinant) **plus its named baseline and the distinct-reduced-square spectrum condition**, under fixed C0 and near-identity gauges. Within this precisely specified domain, the two scalar readouts are complete and the off-diagonal branch is a certified removable gauge direction. At repeated eigenvalues this compression is unsafe; the full matrix square retains information invisible to both scalars. Thus the amount of necessary residual information changes with the actual source operator, not with a universal preference for more or fewer coordinates.

The D25/LIFT/JT2 parent still needs an authenticated original-class divided-power H0/B0 basis, actual [X]U mod p^2, real semilinear Frobenius rank and direction, the normalization eta and source-compatible map to frozen kappa, omega+6 nabla_lambda omega and Delta_p-R_p. Upon obtaining the **real** coefficient matrix, inspect its mod-p square first: distinct eigenvalues permit the above simple-spectrum scalar completion only after checking diagonalizability over the declared coefficient field and fixing the eigenvalue-labeled baseline; scalar repeated square permits the previous twisted full-matrix quotient; nonscalar repeated or other Jordan cases need new analysis. Do not treat a portable coefficient experiment as a native test.

No new Source checkpoint, current CLAIM, authorized run, Result, Driver review or mathematical admission is asserted by this GitHub note. Preserve previous confirmed native units, previous portable rank-two work and frozen science source pin; do not recredit them.
