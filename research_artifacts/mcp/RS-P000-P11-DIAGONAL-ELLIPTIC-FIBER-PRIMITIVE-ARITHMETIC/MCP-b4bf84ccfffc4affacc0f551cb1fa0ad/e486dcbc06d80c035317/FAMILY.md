# An explicit infinite primitive family on the core (11,8)

This is derived rational/elliptic arithmetic for the frozen P11 interface. It does not change the native X6 basis, introduce a native plane, or interpret the auxiliary elliptic curve as native geometry. The static argument needs no physical-time parameter.

## 1. Birational carrier and exact inverse

Fix a primitive Euclidean core `(r,s)`, write `A=r^2-s^2`, `B=2rs`, `C=r^2+s^2`, `P=A+B`, `Q=|A-B|`, `a=P+Q`, `b=P-Q`, `R=PQ`, and `S=P^2+Q^2`. Thus `P>Q>0`.

For the accepted normalized fiber

`D^2+U^2=P^2`, `D^2+V^2=Q^2`,

put `T=U+V` and `Y=2TD`. Its quartic is

`Y^2=(a^2-T^2)(T^2-b^2)`.

The exact map to the monic integral Weierstrass model is

`E_{P,Q}: eta^2=xi(xi-P^2)(xi-Q^2)`,

`xi=R(a+T)/(a-T)`, `eta=aRY/(a-T)^2`.

Indeed the three cubic factors are respectively

`R(a+T)/(a-T)`, `Pa(T-b)/(a-T)`, and `Qa(T+b)/(a-T)`.

Their product is `a^2R^2(a+T)(T^2-b^2)/(a-T)^3`, precisely `eta^2` by the quartic. The inverse on the nonboundary task domain is

`T=a(xi-R)/(xi+R)`, `Y=4aR eta/(xi+R)^2`,

`D=Y/(2T)`, `U=(T+(P^2-Q^2)/T)/2`, `V=(T-(P^2-Q^2)/T)/2`.

Substitution recovers both quadrics and both original coordinates. The excluded `D=0` points, with `T=a,b,-b,-a`, extend respectively to `O,(P^2,0),(Q^2,0),(0,0)`. Thus the chosen origin `[D:U:V:Z]=[0:P:Q:1]` goes to O. No rational point of the intersection has `Z=0`: then `D^2+U^2=0` forces D=U=0 over Q, and the second quadric forces V=0, impossible projectively. Also T=0 is impossible because `U^2-V^2=P^2-Q^2` is nonzero. There are no real E points at `xi=R` or `xi=-R`, since the cubic is negative at both; these inverse-map denominators cause no rational task exception.

## 2. A certified nontorsion seed

For `(r,s)=(11,8)`, `(A,B,C)=(57,176,185)` and `(P,Q)=(233,119)`. The inherited witness has `(D,U,V)=(105,208,56)`, hence `(T,Y)=(264,55440)`. Its image is

`S0=(xi0,eta0)=(194089,69872040)=(7PQ,2520PQ)`.

The monic cubic discriminant is

`disc(f)=P^4 Q^4(P^2-Q^2)^2`.

It is a 5-adic unit: P and Q are 3 and 4 modulo 5, and `P^2-Q^2=3 mod 5`. But eta0 is nonzero and divisible by 5. The generalized Nagell–Lutz theorem for an integral monic Weierstrass cubic therefore excludes rational torsion.

An alternative reduction to the classical integral short form is explicit: set `X=9xi-3S`, `Yshort=27eta`. Then

`Yshort^2=X^3+27(3R^2-S^2)X+27(9R^2 S-2S^3)`.

Its elliptic discriminant is `3^12 * 16 * disc(f)`, still a 5-adic unit, while Yshort is a nonzero multiple of 5. The ordinary short-form Nagell–Lutz theorem gives the same contradiction. The imported theorem is classical prior mathematics; this explicit point and the prime-5 certificate are its task-specific application.

## 3. Explicit family indexed by positive integers

For every integer `n>=1`, calculate the exact rational point `S_n=[n]S0` by the usual chord/tangent group law on E. Since S0 is nontorsion, S_n is never O or a 2-torsion boundary point, and all S_n are distinct. Map S_n back by the formulas above to `(D_n,U_n,V_n)`, retaining its raw signs, coordinates, and multiplier n as provenance.

Replace the three signs only for the requested positive displayed sextuple:

`(dbar,ubar,vbar)=(|D_n|,|U_n|,|V_n|)`.

The full signed triple remains recorded; this is a declared finite-to-one display readout, not erasure of the original elliptic point. We have `D_n!=0` because the D=0 boundary is E[2]. The quadrics force `0<|D_n|<=Q<P` and `U_n!=0`. Equality `|D_n|=Q` would give V_n=0 and `U_n^2=P^2-Q^2=4AB`. For the coprime primitive Pythagorean legs A,B, this is excluded by the accepted Fermat fourth-power descent in the parent. Consequently `0<dbar<Q` and `ubar,vbar>0` for every n.

Let L_n be the positive lcm of the denominators of these three reduced rational numbers, and set `k_n=2L_n`. Construct the integer sextuple

`F_n=(k_n*176,k_n*57,k_n*185; k_n*dbar,k_n*ubar,k_n*vbar)`.

All six entries are even; hence the exact fixed-locus parity and even-mu/even-nu requirements hold. All equations and strict inequalities hold by homogeneity. Apply the inherited exact 16-outer-root formula, let g_n be the positive gcd of its sixteen integer outputs, and define the final sextuple

`Primitive_n=F_n/g_n`.

The accepted primitive-quotient theorem proves that this division remains integral, preserves the P11 reconstruction and parity, and gives outer-root gcd one. Explicitly, differences of outer roots give x and y, while sums/differences give b,d and the remaining roots give mu/2,nu/2; therefore g_n divides all required integer data. Because the primitive core has gcd(A,B,C)=1, g_n divides k_n. The resulting scale is the integer `k_n/g_n`.

This is an exact computable family for every positive n, not a growing census or an unproved assumption that one selected point generates the full Mordell–Weil group.

## 4. Infinitely many distinct primitive outputs

The birational inverse is one-to-one on all S_n. Absolute values have fibers of cardinality at most eight on the signed triples. Therefore infinitely many distinct positive normalized triples result.

The denominator clearing and outer-root primitive quotient cannot identify two different positive normalized triples: from any resulting sextuple the fixed primitive core recovers its scale k by `x/176=y/57=b/185=k`, and then `(d/k,mu/k,nu/k)` recovers the normalized triple exactly. Different positive normalized triples therefore give different primitive sextuples. Each final sextuple can occur at most eight times in this explicit n-indexed sequence, so the set of primitive outputs is infinite.

The multiplier n, elliptic point, core, raw signs, denominators, initial clearing scale, root gcd, and final scale form the retained reconstruction ledger. The integer division is the exact accepted common-root scaling quotient, not a naive gcd of the six displayed coordinates.

## 5. Scope remaining open

This proves `DIAGONAL_ELLIPTIC_FIBER_INFINITE_PRIMITIVE_FAMILY_PROVED` for the fixed core `(11,8)`. It rules out a finite global list of primitive P11 fixed-locus points. It does not compute every rational point on this fiber, prove that S0 generates its free Mordell–Weil group, determine all ranks across cores, or classify all primitive points uniformly. The family proof uses nontorsion, exact birational reconstruction, a finite sign-fiber bound, and the preserved primitive quotient; finite checker success is only validation of those interfaces.

Authorship: root researcher EM-DIRECT-49ADE6's authorized P11 run, with inherited context; this contribution is `NOT_INDEPENDENT / NONBLIND_DISCLOSED` and is not an independent Driver review.
