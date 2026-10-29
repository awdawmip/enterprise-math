# D25/LIFT portable GH-116 — uniform signed CM Frobenius trace on the split reflected-Hasse branch

Date: 2026-10-29 Asia/Hong_Kong. Author-side derivation and exact finite-field checking. UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is not a Source checkpoint, CLAIM, independent review, or GH-3 result. No alteration of frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Statement (new extension of GH-113 and GH-115)

For **every rational prime p >= 11 with p == 11 (mod 24)**, choose positive integers x,y with

    p = 2*x^2 + 3*y^2.

Let q=p^2, k=F_p, r^2=2 in F_q, T=2r/3 and define the **reflected-source elliptic curve**

    C_T:  v^2 = u^3 + u^2 + ((1+T)/8)*u   over F_q.

Then, independently of x,y signs, its **signed Frobenius trace** and exact point count are

    a_q(C_T) = 6*y^2 - 4*x^2,
    #C_T(F_q) = p^2 + 1 + 4*x^2 - 6*y^2.

All integer equalities above are literal, not merely mod p. The representation exists by the classical discriminant -24 binary quadratic form theory. No assertion about the separate reflected-tail R_p(9) or original GH-3 follows.

## Proof

1. The earlier GH-113 exact invariant calculation places C_T in the CM discriminant -24 family, with j=2417472-1707264 sqrt(2); over F_q the parameter T is defined because (2/p)=-1. The corresponding CM field is K=Q(sqrt(-6)), with maximal order Z[sqrt(-6)]. Good reduction holds for p>3 (the cubic discriminant is nonzero because T^2=8/9 != 1).

2. The classical reduction theory for positive definite binary quadratic forms of discriminant -24 has two reduced classes, [1,0,6] and [2,0,3]; alternatively Minkowski's bound (2/pi)*sqrt(24)<4 and the prime ideals of norms 2 and 3 show the class number is two. Since p==11 mod24 is split in K, its prime ideal class is one of these. The principal form x^2+6y^2 cannot represent p==3 mod8 (possible residues mod8 are 0,1,2,4,6,7), so the split prime is in the nonprincipal class and has the indicated 2*x^2+3*y^2 representation.

3. Write beta=2x+y sqrt(-6). Its norm is 2p. If P_2 is the ramified norm-2 ideal, the ideal of beta factors as P_2 times one of the two primes over p. Squaring and dividing by (2)=P_2^2 gives a generator of the square of the selected p-ideal:

    alpha=beta^2/2=(2*x^2-3*y^2)+2*x*y sqrt(-6),
    Norm(alpha)=p^2,  Tr(alpha)=4*x^2-6*y^2.

   Imported standard ordinary CM/Deuring Frobenius theory then puts the p^2-Frobenius of the CM reduction in {+alpha,-alpha} (or their conjugates, which have the same trace). Consequently a_q is one of the **two integers** +(4*x^2-6*y^2) or -(4*x^2-6*y^2). This is the only imported non-elementary bridge in the proof.

4. GH-100's independently established elliptic Hasse coefficient is Ha_p(T)=E_p(T^2)=E_p(8/9), **an element of F_p**. Since the curve is ordinary in the split case, E_p(8/9) is nonzero. The characteristic-p Hasse/Frobenius identity gives

    a_q == Ha_p(T)^(p+1) == E_p(8/9)^2 (mod p).

   Thus the residue of the actual trace is a nonzero **square** in F_p. This is a field-level squaring constraint, not a claim of positive real sign.

5. The candidate Tr(alpha) reduces, using p=2*x^2+3*y^2, to

    4*x^2-6*y^2 == 8*x^2 (mod p).

   For p==11 mod24, p==3 mod8, so (2/p)=-1. Hence +(4*x^2-6*y^2) is a **quadratic nonresidue**. Since (-1/p)=-1, its negative is a quadratic residue. The nonzero Hasse square in step 4 selects the negative candidate uniquely:

    a_q = -(4*x^2-6*y^2) = 6*y^2-4*x^2.  QED.

## Exact checks and scope

A separate integer C++17 checker reconstructs Ha_p from the Legendre recurrence, independently computes a_q by a complete q-element quadratic-character sum for every p<800 with p==3 mod8, and verifies the split formula for **17 split primes**. The direct norm-character calculation uses chi_q(w)=chi_p(Norm_{F_q/F_p}(w)); p==3 mod8 guarantees r^2=2 is irreducible. It also logs 19 inert primes but makes **no general inert-branch theorem claim**. GH-115's previously executed independent full q-element count at p=3347 is not represented as re-executed in this checker.

Examples (p;x,y;trace;points): (11;2,1;-10;132), (59;4,3;-10;3492), (83;2,5;134;6756), (107;4,5;86;11364), (347;10,7;-106;120516).

At p=3347, x=40,y=7, the formula **predicts without enumerating F_(3347^2)**:

    a_(3347^2)=6*49-4*1600=-6106,
    #C_T(F_(3347^2))=11208516.

This agrees with GH-115's independent exhaustive 11,202,409-element calculation and its E_p(8/9)=783 Hasse residue. The new gain is a **uniform sign theorem across all p==11 mod24**, not the old single-prime count.

## BRC / provenance, limitations, next

BRC resolution COMPOSE_APPLIED: retain distinct CM ideal class and norm-form (x,y), full signed trace, base field F_p versus extension F_q, Hasse-square observer, quadratic-character sign and point-count operation. Squaring the Hasse coefficient loses the sign of E but preserves the squareclass needed to select the trace sign; discarding the CM candidate pair would erase information. This is classical auxiliary finite-field number theory, not an assertion about native Heartbeat X6 coordinates.

Depends on classical CM reduction and class-form theory; independent review remains outstanding. The result does NOT predict R_3347(9)=0, does not prove GH-83 stationarity for all p, and does not close GH-3 T_(p,9)=0 mod p. Next smallest nonduplicative unit: search for an independently evaluable Jacobi/WZ/CM p-adic period that maps signed a_(p^2) and necessary extra local data to the reflected-tail special value; a re-expression of GH-98–GH-103's finite-log moment alone is insufficient.

Historical origin: GH-113/GH-115 author-side notes and signed p3347 trace. Research logical lane chatgpt-research-hourly-enterprise-math-20260923, kept distinct from CONTROL_PLANE_MAINTENANCE; no native session, CLAIM, OPEN, or Source checkpoint was obtained.
