# Owner review route: all base points and degree, conditional on exact identities

Source: the frozen N,D0 of EM `341f36bb53c25d97c3ae533a71c92ad273a7b904`. Task: `RS-RB-CM24-SOURCE-EXPOSED-EXACT-MAP-CERTIFICATE`. Reviewer: Driver `EM-DVR-01E1D9`. This is a source-exposed paper review route, not an executed certificate or formal acceptance. In particular, the displayed Norm identity and B0 substitutions must actually be checked; no historical PASS is used as their premise.

Write s=alpha^2, beta=sqrt(2), h=s*beta, a=3(s-1), and

`A=a*t+i*alpha*uN*(R+s)*(R-LN)`, so `N=(R+2)*A`.

Useful exact coefficient simplifications are

`uN=(beta-1)(3-2s)`, `uD=-2-(s-1)(beta-1)`,

`r=-3-3beta-2s-h`, `s*r=-LN`, `r-MD=-3-2h`.

The candidate identity to verify in the full curve algebra is

`Norm(A) = A(R,t)A(R,-t) = -s*uN^2*(R+s)*(R+3s)*(R-r)^2`.

It retains exact constants. A zero full polynomial remainder, together with the established coefficient/function-field basis, will justify its use as an equality of functions.

## Enumerating the zeros of N from that identity

All finite zeros of A must have R=-s, R=-3s, or R=r. The curve's R-involution has no further points above those coordinates.

At Tminus=(-s,0), t is a local parameter and R+s has order two, so A=a*t+O(t^2) has order one. At R=-3s, the point `B0=(-3s,6*i*beta*alpha)` lies on the curve. Once A(B0)=0 is exactly verified, A on the conjugate point is -2a*t(B0), hence nonzero. The simple R+3s norm factor then proves order one at B0 because t(B0) is nonzero and R is a local parameter there.

At R=r, the norm has a double zero and r is not a branch coordinate. The coefficient a is nonzero, so the two values of A above r cannot both vanish: their difference is 2a*t. The unique zero is Z with

`t_Z=-i*alpha*uN*(r+s)*(r-LN)/a`.

The norm equation certifies that this t_Z is on the carrier, and the other conjugate A value is nonzero. Consequently A has order two at Z.

The two additional zeros of N come from R+2, at Pplus and Pminus with t=+/-i*beta. The norm factors show A is nonzero at both of them, so each N zero has order one. Thus the finite zero divisor of N is

`[Pplus]+[Pminus]+[Tminus]+[B0]+2[Z]`.

The already checked O calculation gives function pole order six, consistent with these six zeros. In the L(7O) representation, N has one further section zero at O, while D0 is nonvanishing as a section there.

## Excluding common zeros except B0

At Tminus, `D0=i*alpha*uD*6*(-s-MD)`. The last factor equals `s+beta*(3-s)>0` in the selected real embedding, and the other factors are nonzero. Thus this is not a common zero.

At Pplus/Pminus, D0 has form

`i * [ +/- beta*QD(-2) + alpha*uD*(-2)*(-2-s)*(-2-MD) ]`,

where

`QD(-2)=10-12beta-10s+4h != 0`.

Both bracketed coefficient terms apart from alpha belong to Q(beta,s). The proven coefficient basis makes 1 and alpha independent over that field, so they cannot cancel. D0 is nonzero at both points.

For Z, exact real inequalities suffice. From 1<s,beta<2 and 2<h<3, we have r<-10. Also s>3/2, so uN<0, while a>0. Since r+s and r-LN are negative, t_Z is positive imaginary. Put QD(R)=R^2+bR+c. Its exact coefficients satisfy b<5 and c>-30. Because r is negative,

`QD(r)>r^2+5r-30>20`.

The factors r, r-s and r-MD=-3-2h are all negative, and uD<0. Therefore both terms `t_Z*QD(r)` and `i*alpha*uD*r*(r-s)*(r-MD)` are positive imaginary. Their sum D0(Z) is nonzero. This is a proof in the declared embedding, not a numerical approximation.

Finally, verify N(B0)=D0(B0)=0 directly. Since N has order one there, the common section divisor at B0 has multiplicity exactly one. This does not yet assert the individual order of D0 there or a finite value of X(B0); those remain relevant to complete special-fiber data.

## Exact degrees once the checks above hold

D0 is a polynomial in the affine carrier coordinates, so it has no finite poles. Its sole function pole at O has order seven. Its section divisor in L(7O) therefore has degree seven. The complete common section divisor of N,D0 is then exactly [B0]; O and every other N zero have been excluded. The pole divisor of the nonconstant X=N/D0 has degree 7-1=6, proving the descended carrier-to-P1 degree. The argument uses actual section valuations, not generic polynomial degree.

For the source double cover, the already established odd valuation of F proves `[L(D):L(C)]=2`. Hence `[L(D):L(X)]=12`. The nonsingular target equation `Y^2=C*X*(X-1)*(X-lambda)` has degree two over L(X), because its cubic has three distinct simple roots and is not a rational square. The actual nonzero rational Y supplied by the complete ODE gives an embedding of that target function field in L(D). The tower law therefore gives degree six for D to the target elliptic curve. The normal-curve/proper-target extension theorem makes this a morphism on the projective normalizations.

## Scope still open

Even successful validation of this route is not the full task. Individual D0 multiplicities, all four special-fiber divisors, transformed empty-infinity representative, exact unramified twists/half-points/constants, original-field descent, source-bound counterchecks and the complete proof/return must retain their own evidence. It also gives no period homology index, absolute period ratio, or exhaustive surviving-family classification.
