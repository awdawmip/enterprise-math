# D25/LIFT portable note: scalar-square twisted top-digit gauge, exact residual and changed parity at p=373

Date: 2026-10-25. TASK_RESEARCH **author derivation and finite exact checks**. Status: **UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / NO_NEW_NATIVE_CHECKPOINT**. Logical research lane: chatgpt-research-hourly-enterprise-math-20260923. Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT (publication TP2-B6F4FC938FF94941C1B7). Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged.

## Exact smallest new question

The previous author theorem classified top-digit perturbations around the **identity** semilinear matrix. Actual native Frobenius, if eventually obtained, need not be identity in the fixed H0/B0 basis. Which part of that theorem survives for a genuinely nonidentity base matrix, without changing basis or discarding a branch?

Fix an odd prime p, integer r >= 2, A_r = Z/p^r Z, R_r = A_r[T]/(T^2-2), and the A_r-linear involution sigma(T) = -T. Put q = p^(r-1), so q^2 = 0 modulo p^r. Let n >= 1, let C0 be any invertible n-by-n matrix over R_r, and S0 = C0 sigma(C0). Assume **only**
    
    S0 mod p = lambda I_n, lambda in F_p^*.

The condition concerns the **mod-p semilinear square**; S0 need not be scalar at higher p-adic precision. Every matrix below is an external auxiliary coefficient module, not a native two-dimensional Enterprise plane or a native CM operator.

Use the R_1 = R_r/pR_r parameter D in M_n(R_1), with any lift, to set

    C_D = (I_n + q D) C0,        F_D(v) = C_D sigma(v).

The near-identity gauge group is P_X = I_n + q X, X in M_n(R_1). This is a deliberately fixed-baseline, fixed-readout equivalence problem; no unrestricted basis change is silently admitted.

## Theorem: complete twisted even quotient, scalar-square case

Define the F_p-linear map

    tau(X) = Cbar0 sigma(X) Cbar0^{-1}

on M_n(R_1), where Cbar0 = C0 mod p. Then tau^2 = id. Write

    D_plus  = (D + tau(D))/2,
    D_minus = (D - tau(D))/2.

For every p, r, n, C0 satisfying the displayed assumptions:

1. The exact gauge action modulo p^r is

       P_X^{-1} C_D sigma(P_X)
          = (I_n + q [D + tau(X) - X]) C0.

2. The exact semilinear square is

       F_D^2 = C_D sigma(C_D)
             = (I_n + q [D + tau(D)]) S0.

3. The following conditions are equivalent:

       (a) C_D and C_D' are gauge-equivalent by some P_X;
       (b) D_plus = D'_plus;
       (c) F_D^2 = F_D'^2 as full matrices in the fixed basis modulo p^r.

4. Every gauge class has exactly one tau-even parameter representative D_plus, reached constructively by

       X = D_minus / 2;
       P_X^{-1} C_D sigma(P_X) = C_(D_plus).

5. The tau-even and tau-odd subspaces each have F_p-dimension n^2. Consequently, there are exactly p^(n^2) distinct near-identity gauge classes for this fixed base C0. For rank two, exactly p^4.

**Proof.** From Cbar0 sigma(Cbar0) = lambda I, applying sigma and conjugating shows sigma(lambda) = lambda and lambda belongs to F_p. Moreover

    tau^2(X) = Sbar0 X Sbar0^{-1} = X.

Since q^2 = 0, expanding P_X^{-1}=(I-qX) and sigma(P_X)=(I+q sigma X) gives (1), while multiplication of C_D sigma(C_D) gives (2). In (2), reduction modulo p of C0 and S0 is sufficient in every term multiplied by q.

If (a) holds then D' = D + (tau-1)X; applying (1+tau)/2 gives (b), because (1+tau)(tau-1)=tau^2-1=0. Conversely, if (b) holds, Delta = D'-D has tau(Delta)=-Delta. Choosing X=-Delta/2 yields (tau-1)X=Delta, proving (a) explicitly. Formula (2) shows (b) iff (c): multiplication by invertible S0 and q identifies the residue space M_n(R_1) injectively with the top-digit ideal q M_n(R_r), and 2 is invertible mod p. Setting Delta = D_plus-D=-D_minus in the explicit construction gives (4).

Finally T is a unit in R_1 (T^2=2, p odd), and tau(TX)=-T tau(X). Multiplication by T exchanges the +1 and -1 eigenspaces of the F_p-linear involution tau. Their direct sum has dimension 2n^2 over F_p, so both have dimension n^2, establishing (5). QED.

The theorem is an elementary new **project-scoped generalization of the previous identity-base note**, not a global literature-priority claim. Its safe observer is the **full square matrix in the fixed baseline**, under the declared near-identity future gauge operations; the trace, determinant, native kappa, and arbitrary basis changes are different readouts.

## Exact p=373 witness: ordinary sigma parity reverses under a legitimate nonidentity baseline

Choose p=373, r=2, q=373, n=2 and

    C0 = diag(2,-2),       S0 = 4 I_2.

This satisfies all theorem hypotheses and has nonidentity C0. Write E12 for the elementary upper-right matrix. Since tau(X)=C0 sigma(X) C0^{-1}, its off-diagonal action is

    tau(E12) = -E12,       tau(T E12) = +T E12.

Hence the **sigma-even** perturbation D=E12 is now *pure near-identity gauge*, with explicit X=E12/2 and canonical representative zero. By contrast the **sigma-odd** perturbation D=T E12 survives as tau-even:

    F_(T E12)^2 = 4 I_2 + 8q T E12
               = 4 I_2 + 2984 T E12   (mod 139129),

and no allowed P_X can gauge it to C0, since its complete normalized square is different. Both claims are exact coefficient-ring statements. Reversing the previous identity-baseline labels without tracking C0 would falsely delete the surviving branch. This witness is **not** a measured native H0/B0 Frobenius.

## Boundary certificate: scalar-square reduction is not cosmetic

At p=373, r=2 instead let C0=diag(1,2), so S0=diag(1,4), noncentral mod p. Take P=I+q E12 and C'=P^{-1}C0 sigma(P). These are gauge-equivalent by construction, but

    C' sigma(C') = P^{-1} S0 P
                  = diag(1,4) - 3q E12
                  = diag(1,4) - 1119 E12   (mod 139129),

which is not the original fixed-basis S0. Thus **exact equality of square matrices is not even necessary for gauge equivalence** without the scalar-square mod-p hypothesis. The general case needs a conjugacy-compatible observer or explicit twisted stabilizer analysis, not reuse of the above equivalence.

## Finite author validation and limitations

An independently programmed exact-pair evaluator represented a+bT by (a,b), multiplied via (a,b)(c,d)=(ac+2bd,ad+bc), conjugated (a,b) to (a,-b), and used exact 2-by-2 matrix arithmetic modulo p^r. For each p in {13,19,373} and r in {2,3}, it checked 31 deterministic pseudorandom D/X pairs against (1), (2), and the explicit canonicalizing gauge (4): **186/186 checks passed**. It separately checked tau(E12)=-E12, tau(T E12)=T E12 and the nonzero square witness in all six settings.

The T E12 upper-right square coefficient was 8 p^(r-1) times T: 104T (p=13,r=2), 1352T (13,3), 152T (19,2), 2888T (19,3), 2984T (373,2), and 1113032T (373,3), in the corresponding modulus. This finite validation is AUTHOR_CHECKED, **not** independent review, and the general result rests on the displayed algebraic proof. No actual CM/crystalline experiment or native Source execution is claimed.

## Typed BRC interface and smallest remaining mother-target action

- Carrier: (A_r,R_r,sigma; C0, its raw coefficient basis; D, D_plus, D_minus; semilinear F and full square).
- Allowed operations: composition, sigma, exact mod-p^r ring arithmetic, and fixed-baseline near-identity gauge.
- Safe quotient **only in that operation domain**: D -> D_plus. It is a proven exact gauge classifier because the discarded D_minus has a displayed removal gauge.
- Unsafe quotient: the unqualified sigma-even part of D without C0; p=373 shows it reverses which E12 branch is removable. Also unsafe: trace/determinant or scalar Norm as a universal replacement for the complete rank-two square, and any claim that this auxiliary rank is Enterprise native spatial dimension.
- Mathematical status: portable author derivation; neither P000 nor the frozen scientific Source pin changes.

For the D25/LIFT/JT2 mother target, the critical missing source remains the **actual same-class divided-power H0/B0 representative**, rank, directed semilinear Frobenius matrix, [X]U mod p^2, normalization, and proof of the map to frozen kappa and Delta_p-R_p. If the native reduced square is scalar and the coefficient matrix has been obtained authentically, apply the theorem to its exact fixed basis (without presumed normal form). If not scalar, preserve the full matrix/conjugation data and solve the genuinely different twisted stabilizer problem.

Source publication, CLAIM/open, review/freeze and independent mathematical admission require their own current canonical receipts. Recheck the original Research lane continuation request and do not duplicate prior Hesse Green, Hilbert-90, identity-base top-digit work, or the prior native checkpoint.
