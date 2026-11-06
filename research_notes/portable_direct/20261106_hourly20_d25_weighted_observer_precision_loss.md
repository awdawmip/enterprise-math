# D25 — Exact p-adic precision loss and minimal repair for the weighted 216 observer

Date: 2026-11-06. Scope: exact linear algebra over Z/p^r, p>=5 prime, r>=1. Status: AUTHOR-DERIVED / EXACT PROOF / 428-PRIME MODULAR CHECK / UNREVIEWED / NOT_ADMITTED / PORTABLE.

Mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen scientific input c47e13e4aba0e006366f989d6334d443f6333ae3. This continues the exact four-shell/weighted-kernel result recorded in research_notes/portable_direct/20261106_hourly20_d25_carry_filtration_clausen_third_jet.md at commit 4cb49e0594f4a80bae35a42e37298c7a8f3bc030.

## Theorem: coefficientwise weighted observer over p^r

For any prime p>=5 and integer r>=1, put R_r=Z/(p^r), P_r=R_r[z]_{degree<p}, and let D:P_r->P_r be D=1+6z(d/dz). Thus D acts diagonally on the j-th coefficient with weight w_j=6j+1, 0<=j<p.

There is a unique index j_* at which p divides w_j. It is

    j_*=(p-1)/6,  w_{j_*}=p          for p=1 mod 6;
    j_*=(5p-1)/6, w_{j_*}=5p         for p=5 mod 6.

Set v=v_p(w_{j_*}), so v=1 for every p>=7, and v=2 for the exceptional p=5. Let g=min(v,r).

Then the image and kernel of D are exactly

    Im(D) = { B(z)=sum_{j<p} b_j z^j : b_{j_*} divisible by p^g in R_r },

    Ker(D) = (p^(r-g) R_r) z^{j_*}.

Both Ker(D) and Coker(D) have p^g elements. For a B in the image, all inverse coefficients x_j for j!=j_* are unique and computable as

    x_j = (6j+1)^(-1) b_j (mod p^r).

At j=j_*, the congruence w_{j_*} x_{j_*}=b_{j_*} determines x_{j_*} modulo p^(r-g), leaving exactly g high base-p digits as a minimal additional repair coordinate. Conversely, specifying those digits restores the complete coefficientwise polynomial A from B=DA.

In the frozen target class p=13,19 mod 24, v=1. Thus at modulus p^2 the coefficientwise weighted D25 observer loses exactly one higher p-adic digit of the single coefficient at j_*=(p-1)/6. For p=5, w_4=25 and the modulo-25 observer loses two digits, not one.

## Proof

For j in [0,p-1], p | 6j+1 has one solution because 6 is a unit mod p. The displayed j_* lies in range and gives w=p or 5p respectively. For p>=7, p does not divide 5, so v=1; for p=5, v_p(25)=2. All other weights are units mod p^r and hence invertible on R_r. For the unique exceptional coordinate, multiplication by w=p^v u with u a p-adic unit is equivalent to multiplication by p^g on R_r. Its image is p^g R_r, and its kernel is p^(r-g)R_r. The kernel has size p^g, as does the quotient R_r/p^g R_r. These facts and invertibility of the other diagonal entries prove every assertion.

The lossless repair guarantee is explicitly scoped to **coefficientwise B(z)=DA(z)** and subsequent operations on the restored polynomial. If the observer retains only the final scalar B(1), many more coordinates are collapsed and the one-digit repair claim does not apply. Signed/source labels and the single exceptional coefficient must remain available before the scalar observation.

## Exact finite test

The accompanying standalone Python program enumerates all 428 primes 5<=p<=3000. For each, it verifies the unique exceptional coordinate, precise p-adic valuation, image/kernel divisibility for r=1,2,3,4, explicit fiber witnesses and invertibility at the remaining coefficients. Result: **428/428 PASS**.

Examples modulo p^2: p=5 has kernel size 25 at j*=4; p=13 has kernel size 13 at j*=2; p=19 has kernel size 19 at j*=3; p=373 has kernel size 373 at j*=62.

## Next scientific action

Use the lossless coefficientwise inverse and the exceptional high-digit repair to translate the D25 signed Gauss-jet Theta_p question into a candidate congruence for the exceptional coordinate. Preserve separate regular/single/double/triple shell data for further operations, rather than using scalar weighted summation as a complete observer. Attempt finite telescoping in the G=0 and G!=0 branches at p=13,19,373. The original native H0/B0, [X]U mod373^2, Frobenius eta/kappa, independent review and the frozen target Delta_p-R_p=0 (mod p) remain separate scientific obligations.

BRC: COMPOSE_APPLIED as a proof of exact signed observer losslessness with a minimal repair coordinate. This is author-side portable evidence, not native Source checkpoint, Result or admissibility.
