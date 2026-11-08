# PREFIX-600-R2: positive spectral collision locus for two-class native X6-BRC

Date 2026-11-08. Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Continuation of PREFIX-599-R2; original 96 ordered ports, 576 labeled actions, three gate sources and 48-dimensional positive tail retained. Exact algebraic root-collision theorem, not a completed Jordan/minimal-polynomial classification.

## Exact theorem

Let w>0, z>=0, z!=1. The native axis weights are (1,1,1,1,w,w). Set s=t² and L(s,w)=s²+4(w+1)s-48w. PREFIX-599 proved the full characteristic factorization chi(Q)=F30(w,t)*R18(w,z,t), with R18=P18-(z-1)B14, and defined the baseline degree-10 factor

    H10=(s-4)(s-4w)(s+12w)L.

Then gcd_t(H10,R18) is nontrivial if and only if at least one of the following holds:

(A) w=1: for every z>=0, z!=1, the exact monic gcd equals (t²-4)².

(B) w!=1, w!=25/4, z=z_A(w)=(4w²-100w+75)/(4w-25)>=0, z!=1. Then t²-4w divides both H10 and R18. The admissible w intervals before excluding w=1 and w=25 (where z_A=1) are [(25-5sqrt(22))/2,25/4) union [(25+5sqrt(22))/2,infinity).

(C) w!=1, z=z_B(w)=(12w³+28w²-23w-9)/(5w+3)>=0, z!=1. Then t²+12w divides H10 and R18. This admissible curve begins at the unique positive root rho=0.868387904607292... of 12w³+28w²-23w-9.

Curves B and C intersect for positive z!=1 at the single point w_*=(5+4sqrt7)/3, z_*=(14635+6848sqrt7)/411. At this point the two distinct factors t²-4w_* and t²+12w_* both divide the gcd.

## Exact proof / certificates

The gate-sensitive polynomial P18 is divisible by (s-4)L. Its values together with B14 at the three roots are:

    s=4:     P=0; B=-6291456 w² (w-1)² (3w+1).
    s=4w:    P=8388608 w^5 (w-25)(w-1)^3;
             B=2097152 w^5 (w-1)²(4w-25).
    s=-12w:  P=-679477248 w^5(w-1)(w+3)(3w+1)²;
             B=-169869312 w^5(3w+1)(5w+3).

Setting R=P-(z-1)B=0 yields exactly the curves z_A,z_B outside w=1. At w=25/4, B vanishes at s=4w but P is nonzero, so it does not produce an extra root. At s=4 and w!=1, B nonzero and z!=1 excludes a common root.

For the quadratic factor L(s,w), exact polynomial elimination in s yields:

    resultant_s(L,B)=-712483534798848 w^7(w-1)²(3w³+42w²+2w+1).

For w>0,w!=1, this is nonzero; since P is divisible by L, R18 cannot share an L root for z!=1. At w=1, direct symbolic gcd over Q(z)[t] gives (t²-4)²; after dividing this factor out, its remaining factor is nonzero on t²=4 or t²=-12 for all z!=1, by explicit residues proportional to z-1.

The nonnegative z_A intervals follow by numerator and denominator signs. The polynomial defining z_B has exactly one positive root by Descartes' rule and its signs at 0 and +infinity. Finally:

    z_A-z_B = -16w(w-1)(3w²-10w-29)/((4w-25)(5w+3)).

The unique positive intersection other than w=1 is therefore w_*, with positive z_* above. Positivity conditions and denominator exclusions are explicit.

## Verification and continuation

The separately stored Python/SymPy certificate evaluates all root substitutions and the resultant in exact arithmetic, checks the generic w=1 gcd, performs exact rational point gcd tests, and verifies the two-curve positive intersection. Actual executed outcome: ALL_ASSERTIONS_PASS. These statements classify algebraic factor collisions. Minimal-polynomial orders at positive w on these curves, full Jordan structure, 96-port endpoint complexity, and independent Driver review remain open. Preserve the pinned native model and typed branch/gate provenance.

Research identity: EM-DIRECT-1C076C; activity RA-D8B36FCD19B160E4AE44D76C; author-side only, no formal Task CLAIM or native Result.
