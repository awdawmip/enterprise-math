# D25/LIFT GH-118/GH-119: rational group classification of the reflected CM elliptic family

Author-side mathematical proof and executed finite-field checks; 2026-10-30 Asia/Hong_Kong. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Current logical Research lane: chatgpt-research-hourly-enterprise-math-20260923. This is not a Source-native CLAIM/checkpoint, review, or proof of GH-3. Scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged.

## Definitions and imported prior results

Fix any rational prime p>=11 with p=3 mod8, set q=p^2, r^2=2 in F_q, T=2r/3 and

    C_T: v^2 = u^3+u^2+((1+T)/8)u.

Carry GH-113's unreviewed author-side maximal-order CM discriminant -24 identification, GH-116's signed split Frobenius theorem, GH-117's signed inert Frobenius theorem, and the standard endomorphism and torsion facts for elliptic curves. None of these dependencies is promoted here. The classical CM order is O=Z[s], s^2=-6.

## GH-118: the entire rational 2-primary subgroup

For every such p, conditional on the cited signed-trace formulas,

    #C_T(F_q) = 4 (mod8),
    C_T(F_q)[2^infinity] = C_T(F_q)[2] = (Z/2Z)^2.

In particular E[2] is fully rational over F_q but no point of order 4 is rational. This applies at p=3347 and is independent of the separate value R_p(9).

Proof: The cubic factors as u(u^2+u+b), b=(1+T)/8. The nonzero two-torsion roots have discriminant delta=(1-T)/2, whose norm from F_q to F_p is (1-T^2)/4=1/36. The norm is a square, hence the quadratic character of delta in F_q is +1. The three distinct nonzero two-torsion points are rational. For p=19 mod24 the GH-117 order is (p-1)^2; since p=3 mod8 this equals 4 mod8. For p=11 mod24 write p=2x^2+3y^2. GH-116 gives #=p^2+1+4x^2-6y^2. Parity forces y odd; reduction mod8 then forces x even. Therefore #=1+1+0-6=4 mod8. Full E[2] supplies all four points of the Sylow-2 subgroup. QED.

## GH-119: complete finite abelian group, not just its order

Inert class p=19 mod24:

    C_T(F_q) = (Z/(p-1)Z) x (Z/(p-1)Z).

Proof: GH-117 yields a_q=2p, so q-Frobenius pi_q obeys (pi_q-[p])^2=0 by Cayley-Hamilton. The endomorphism algebra is a division algebra and has no nonzero nilpotents, hence pi_q=[p]. Rational points are ker(pi_q-1)=E[p-1]. Since p does not divide p-1, E[p-1] is abstractly (Z/(p-1))^2. QED.

Split class p=11 mod24: let x,y be positive with p=2x^2+3y^2, set A=2x^2-3y^2, B=2xy,

    g=gcd(|A+1|,B),  N=(A+1)^2+6B^2
      =p^2+1+4x^2-6y^2.

Then

    C_T(F_q) = (Z/gZ) x (Z/(N/g)Z),   g divides N/g.

Proof: The ordinary reduction has End(E_bar)=O=Z[s] by the maximal-order CM bridge (standard CM fact). By GH-116 its q-Frobenius is -A+B*s or -A-B*s (the choice is immaterial), so pi_q-1=-(A+1) +/- B*s. Thus g is the largest positive integer n dividing pi_q-1 inside End(E). The finite elliptic group has invariant factors n1|n2, n1*n2=N. Its first invariant n1 is prime to p, since E[p](Fbar) has only p geometric points for an ordinary curve. The quantity B=2xy obeys 0<B<=p/sqrt(6)<p, so g is also prime to p.

Since pi_q-1=[g]*eta, all E[g] is rational, forcing g|n1. Conversely E[n1] is fully rational and n1 is prime to p, so pi_q-1 annihilates E[n1]. The quotient map [n1]:E->E by the separable kernel E[n1] factors pi_q-1, giving pi_q-1=[n1]*eta' in End(E)=O; hence n1|g. Therefore n1=g, n2=N/g. Conjugating the CM embedding only changes B to -B and leaves g invariant. As x even and y odd, A+1=6 (mod8), while B is divisible by4, so v_2(g)=1. QED.

### Concrete exact results

|p|branch|x,y|#E(F_(p^2))|group|number killed by [4]|
|--:|--|--|--:|--|--:|
|11|split|2,1|132|Z/2 x Z/66|4|
|19|inert|n/a|324|Z/18 x Z/18|4|
|43|inert|n/a|1764|Z/42 x Z/42|4|
|59|split|4,3|3492|Z/6 x Z/582|4|
|83|split|2,5|6756|Z/2 x Z/3378|4|
|3347|split|40,7|11208516|Z/2 x Z/5604258|4 (theorem)|

For p=3347: A=3053, B=560, g=gcd(3054,560)=2 and N=3054^2+6*560^2=11208516.

The separate companion Python source d25_gh118_gh119_cm_group_check.py was executed locally using exact F_(p^2)=F_p[r]/(r^2-2) arithmetic. It independently enumerated every point, checked the elliptic group law, the full second invariant exponent, all g-torsion and 4-torsion for p=11,19,43,59,83. Five cases returned PASS. For p3347 the program checked the integer formula only; its previously published full point-count enumeration was not repeated.

## BRC, source scope, and frontier

BRC use: COMPOSE_APPLIED. Retain the carrier p/F_q/C_T, CM branch and CM generator, and the observer's signed trace, rational-point count, group invariant factors and 2-power torsion. Passing from group to count discards torsion structure; passing from Frobenius to unsigned trace discards needed sign. The coordinates here are auxiliary standard finite-field arithmetic, not a new native X6 theorem. Preserve P000.

These results are conditional on the GH-113/116/117 author-side CM bridge and require independent mathematical review. They do not evaluate R_3347(9), do not claim GH-83 stationarity, do not close GH-3 T_(p,9)=0 modp, and do not perform the native p373 experiment. Next precise research unit: obtain a separately normalized CM/Jacobi/WZ or p-adic-period evaluation for R_p(9) whose information is not already fixed by signed Frobenius trace and rational torsion. The issue of restoring original Source owner/session/CLAIM remains with enterprise-math#1558; preserve historical uploads and request IDs and do not borrow the maintenance conversation ID.
