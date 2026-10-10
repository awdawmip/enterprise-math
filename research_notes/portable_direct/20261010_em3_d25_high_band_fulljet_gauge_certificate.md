# D25 LOW–Beta high-band full-jet finite certificate (2026-10-10)

Status: AUTHOR_FINITE_PROOF / UNREVIEWED / NOT_ADMITTED / NO_FORMAL_TASK_CLAIM.
Research activity previously registered: RA-20261010-EM3-9C2F61 (registration does not confer TASK ownership).
Global snapshot: awdawmip/chatgpt-global-knowledge@2415716de586c52eb2615cc10604432998460ece (GLOBAL_KNOWLEDGE_V1).
Source input: awdawmip/enterprise-math@8a944895a85a43b25e2c6586a92260ca9f899a30, research_notes/directed_recovery/20260926_13C1B7/math/D25_LOCAL_PROGRESS.md.
Previously established p=19 rank-three witness: EM_D25_LOW_B11_thirdjet_obstruction_20261010.md (author evidence, not admitted). This note reports **new** nine-jet rank and prefix failure.

## Definitions and finite theorem

Let p=6m+1 be prime, n=m+r, 1<=r<=3m. Work over Z_(p).

R_n(t) = [(-m+t/2)_n (-2m+t/3)_n (-4m+2t/3)_n] /
         [2^n n! (-4m+t)_n (-2m+t)_n]
       = t * sum_{j>=0} u_{j,r} t^j.

All coefficients u_{j,r} belong to Z_(p): strip the unique net t factor and note that every remaining constant denominator factor is a p-unit (n<=4m<p). Let
A_m = (p-1)!/[3^(p-1)((2m)!)^3] and G_p=(A_m u_{j,r} mod p)_{1<=j,r<=3m}.

**Finite theorem:** for p=19, m=3, rank_F19(G_19)=9, det(G_19)=6 mod 19.

Complete witness: rows indexed j=1..9, columns r=1..9, modulo 19:

    6  1  7  0  0  7 16 16  2
    2  6 12  3 10  3 12 15 16
   13 13 14 18  5  5  4  0 11
    4  5  6  0  4 11  2 11  7
   12  5  8  5 14 13  8 15 11
    5  9 16  2  2 15  6 16 12
    4  7 16 15 16  2 13 12 14
    9  4 16 16 12  8  7 17 17
    4  2 16 13 14 10 18 18 18

A direct finite-field truncated-series algorithm and an independent exact-Q Fraction coefficient algorithm agree on every entry. Gaussian elimination in F_19 gives determinant 6. Thus G_19 is invertible even over Z_(19). For any nine locally p-integral target jet moments, a unique locally p-integral coefficient vector c exists.

The anchor operation P_m^c(t)=P_m(t)+(t-p)*sum_{r=1}^9 c_r R_{m+r}(t) preserves the exact endpoint P_m^c(p)=P_m(p). It changes *combined presentation jet moments*, not intrinsic branch coefficients or native Heartbeat state.

## New prefix-failure counterexample

The 7x7 upper-left submatrix of G_19 has rank 6. An exact left null vector modulo 19 is
ell=(16,11,17,18,10,7,1)^T.
One checks
ell^T * G_19[rows 1..7, columns 1..9] = (0,0,0,0,0,0,0,0,7) mod 19.
Thus branches 1..8 cannot span all seven lowest response coordinates, though branches (1,2,3,4,5,6,9) give a 7x7 minor of determinant 18 mod 19. Naive "first k branches control first k jet orders" fails at k=7. This is a **finite counterexample**, not evidence that full-branch B11→LOW transport is impossible.

## Nine finite checks (no all-primes theorem)

p:dim:rank:det(Fp)
7:3:3:1
13:6:6:7
19:9:9:6
31:15:15:16
37:18:18:4
43:21:21:9
61:30:30:2
67:33:33:48
73:36:36:20

p=7..43: independent Q and Fp coefficient-by-coefficient checks. p=61,67,73: direct Fp and separately run earlier exact Q determinant check. No claim of universal rank without a proof.

Evidence generated/executed for this author contribution:
- EM_D25_HIGH_BAND_FULLJET_CERT_20261010.py (SHA256 1e9411d42e2a3fe0a40f121c6bd5ffa36a7d8a3e459ca39992e6bd60b390c4df).
- EM_D25_HIGH_BAND_FULLJET_CERT_20261010_results.json (SHA256 0f33c53d238742dc183e425f3917f5301ce75311c2aa56d3b4a9ae1474c8f3ab).
- Actual local execution: nine PASS and ALL CHECKS PASSED. These files are separate author computation artifacts; this text alone does not claim they are already in GitHub Source.

BRC resolution REUSE_APPLIED: retain branch indices, exact rational jets, p valuations, parameter direction and endpoint observer before quotient. Signed rational cancellations are not positive BRC masses. This is auxiliary exact arithmetic, not a P000 theorem; no native Heartbeat computation or independent review.

Smallest open question: prove or refute det(G_p)!=0 for all p=6m+1, find a structural determinant formula, and build the B11-to-LOW index-level normal-jet transport at p=19 retaining the ninth branch and Dixon double-pole moment. No formal CLAIM or native Result is created by this research note.
