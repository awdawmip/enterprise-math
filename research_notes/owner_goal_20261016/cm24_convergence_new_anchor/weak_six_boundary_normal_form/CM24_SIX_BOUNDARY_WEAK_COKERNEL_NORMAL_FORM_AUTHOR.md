# A six-boundary normal form for the actual proper row cokernel

FROZEN_UNREVIEWED_AUTHOR_PROOF, EM-DIRECT-88303D, current15. No scientific execution or Native vote. Old joint Source5530/peer8615 remain unchanged.

## 1. Exact claim and reused inputs

Let p be prime, p=13 or19 mod24; let O be the specified unramified complete DVR, K=O[1/p], S=4r^3-3r,

    f=1-r^2, q=4r^2-1, P=fq, A=2S-1, B=4S-5,
    D=(1/(2P))*[[A,1],[B,-A]], K(v)=(Pv')'-2qv.

Write R0=K[r,P^-1] and R=O[r,f^-1,q^-1]^dagger[1/p], with the exact embedded weak presentations of the old actual proper theorem. Let L(h)=h'+hD on rows. The claim is that inclusion induces

    R0/K(R0) -> R/K(R),

an isomorphism with basis 1,r,(r-a)^-1 for a in E={1,-1,1/2,-1/2}. The proper row cokernel has the same basis times e1 dr. Four finite residues and the two-component infinity residue give a complete class test.

Consume old9897 Sections2-3: matched scalar equation, balanced/log f0,g0 and gauge method; joint5530 Sections2,5-6: differential Robba restrictions and actual good-infinity matrix. New: four-puncture composition, rational normal form, logarithmic primitive bounds and weak passage. The old nonproportionality is not needed.

Retain Heartbeat native X6. This external arithmetic/module calculation has no spatial-axis interpretation; reversible elimination and six-observation completeness apply only to this cokernel, not original functionals or native state.

For b=(b1,b2), subtract L(2Pb2,0). The remaining row is (c(b),0), where

    c(b)=b1-2(Pb2)'-A b2.

For h(v)=(-2Pv'+Av,v), L(h(v))=(-2K(v),0). Thus [b] maps to [c(b)] in the scalar cokernel, reversibly, over either ring. This old exact elimination fixes signs and transposes.

## 2. Four logarithmic gauges from the old balanced series

At a in E put x=r-a and epsilon=S(a) in {1,-1}. With z=(1-epsilon S)/2,

    a=1:    z=(-9/2)x(1+2x/3)^2;
    a=-1:   z=(9/2)x(1-2x/3)^2;
    a=1/2:  z=3x^2(1+2x/3);
    a=-1/2: z=3x^2(1-2x/3).

Thus z=kappa x^e u, e=1 or2, u(0)=1, with integral polynomial coefficients and p-unit constants. The old scalar equation is invariant under S->-S. Its same f0(z),g0(z) satisfy Lhyper f0=0 and Lhyper(f0 log z+g0)=0, with

    v((f0)n)>=0, v((g0)n)>=-log_p(3(n+1)).

For a scalar h use

    J_epsilon(h)=(h,-12 epsilon z(1-z)h'
                              +(1-2epsilon+4epsilon z)h)^T,
    E_epsilon=J_epsilon(g0)-(0,12epsilon(1-z)f0)^T.

The exact old reconstruction formula in S verifies both proper equations. Set ell=log u and

    Ba=[E_epsilon+ell J_epsilon(f0), J_epsilon(f0)],
    Ca=Ba(0)=[[0,1],[-12epsilon,1-2epsilon]], Ha=Ba Ca^-1.

Choose the derivative-consistent formal branch log z=e log x+ell; no log(kappa) is evaluated. Then Ba x^(e E21) is horizontal. Therefore

    Ha'=D Ha-Ha Na/x, Ha(0)=I, Na=Ca(e E21)Ca^-1.

Na=Res_a Ddr is integral, nonzero and square-zero, with kernel vector ka=(1,1-2epsilon)^T. Composition uses indices<=n; z h' introduces integers, and ell=d log(1+-2x/3) has valuation>=-log_p n. Ca and its inverse are integral, so the old argument gives

    v((Ha)n),v((Ha^-1)n)>=-log_p(3(n+1)).             (1)

For the inverse use det Ha=1 from the trace-zero equation, hence adjugation. Both gauges converge on every |x|<1. No new geometric Frobenius at the other nodes is assumed.

## 3. Good infinity: a quantitative consequence of actual Frobenius

Put z=1/r, J=diag(z,z^-1). Joint5530 constructs the actual good-family canonical integral M(z), det M=p, and G=M^-T in p^-1 Mat2(Zp[[z]]). Both G^-1=M^T and G(0)^-1 are integral. In the good period basis the connection is

    Dinf=-J^-1 J'-z^-2 J^-1 D(1/z)J,
    Dinf(0)=[[0,1/8],[0,0]].

Its normalized H'=Dinf H, H(0)=I, and inverse satisfy the exact old identities

    H(z)=G(z) H(z^p)G(0)^-1,
    H^-1(z)=G(0) H^-1(z^p)G(z)^-1.

The coefficients of H are rational, so coefficient sigma fixes them. For n>=1, either identity gives a coefficient lower bound -1 plus the minimum of earlier bounds at indices j<=floor(n/p)<n. Induction therefore gives

    v(Hn),v((H^-1)n)>=-1-floor(log_p n), n>=1.        (2)

Constants are integral. No bound on the unit circle or exchange of localization and inverse limits is used.

## 4. Boundary observations and rational normal form

At a define

    la(b)=Res_x(b(a+x)e1 Ha dx) ka.

At infinity define

    Q(b)=Res_z(-z^-1 b(1/z)e1 H dz) in K^(1x2).

For every weak b, the old degree estimate at p-separated punctures and(1)-(2) justify these annular residues. They kill K(v): L(h(v))=-2K(v)e1, the finite gauge identity, Res d=0 and Na ka=0; at infinity use the flat frame. This applies to all weak primitives.

In R0, K((r-a)^-n) has leading pole n^2 P'(a)(r-a)^(-n-1) for n>=1. The coefficient is nonzero. Also

    K(r^j)=-4(j+1)(j+2)r^(j+2)
                  +(5j(j+1)+2)r^j-j(j-1)r^(j-2).

Finite partial-fraction reduction removes every pole of order>=2; it only creates lower poles and a polynomial. Polynomial reduction then removes all degrees>=2. Thus every b in R0 is uniquely K(v)+n with

    n=c0+c1 r+sum_(a in E) da/(r-a).                 (3)

Uniqueness: a pole of a nonzero rational v forces a pole of K(v) of order>=2; if v is polynomial its nonzero leading term forces degree>=2. Neither can equal a normal form. This also proves the rational kernel is zero.

The observations read these coefficients without solving a large triangular system:

    la(n)=da, Q(n)=(-c0,-c1/8).                     (4)

Indeed other finite terms are regular at a, Ha(0)=I and e1 ka=1. Each simple pole is regular in the transformed good one-form at infinity. For 1 and r use H0=I and e1 H1=e1 Dinf(0)=(0,1/8). Consequently all six observations are independent on rational classes.

## 5. Uniform logarithmic loss for the rational primitive

Let FN consist of partial fractions with polynomial degree<=N and finite pole orders<=N, and let vF be the minimum valuation of their coefficients. Take N>=2, vF(b)>=s and set

    LN=2+ceil(log_p(3(N+2))).

All Taylor expansions of the other partial fractions at a, and all regular expansions at infinity, have integral coefficients because distinct punctures have p-unit differences. Equations(1)-(2), using only jets through N, give each coefficient of n in (3) valuation>=s-LN. Thus btilde=b-n has vF>=s-LN.

Let v be its unique rational primitive K(v)=btilde. Pole and polynomial leading terms show that v has finite poles of order<=N-1 and polynomial degree<=N-2. Put h=h(v), so L(h)=-2btilde e1. At a write k=h Ha and F=-2btilde e1 Ha. Then

    k'+k Na/x=F, k_j=F_(j-1)(jI+Na)^-1, j<0,
    (jI+Na)^-1=I/j-Na/j^2.                         (5)

Only -N<=j<0 and Ha indices<=N can occur in the negative part. Its input coefficients have valuation>=s-2LN. The inverse in(5) loses at most2LN; multiplying by Ha^-1 loses at most LN. Therefore all finite principal-part coefficients of h, hence of v=h2, have valuation>=s-5LN. No constant or logarithmic homogeneous term affects this negative part.

At infinity hgood=hJ, and k=hgood H satisfies

    k'=2 z^-1 btilde(1/z)e1 H.

For j<0 use k_j=F_(j-1)/j. The source has pole order<=N+1, so again only indices through N enter. Input, division and multiplication by H^-1 lose at most2LN,LN,LN respectively. All negative coefficients of hgood have valuation>=s-4LN. Since v=z(hgood)2, these include every coefficient of the polynomial part of v. Finite principal parts of v contribute no negative term to z^-1 v(1/z), so this assertion does not mix the two components of partial-fraction decomposition.

We have proved the concrete bound

    vF(n)>=s-LN, vF(v)>=s-5LN, v in FN.             (6)

This holds for every rational input in FN, avoiding factorial loss from descending division.

## 6. Passage to weak completion and completeness of the test

An integral polynomial of degree<=N in r,f^-1,q^-1 lies in FN with integral partial-fraction coefficients: factor f,q into their p-separated linear factors and perform monic division and integral Taylor expansions. Conversely each integral element of FN has a polynomial presentation of degree<=2N in these generators, since each (r-a)^-1 is an integral linear polynomial times f^-1 or q^-1. These statements preserve valuations; the number of summands does not cause loss in a nonarchimedean norm.

After a finite p denominator, take an arbitrary weak presentation b=sum_l p^l bl, each bl integral of presentation degree Nl<=C(l+1), enlarged to Nl>=2. Apply the rational decomposition to each term:

    bl=K(vl)+nl.

By(6), the coefficients of nl and vl have lower bound -5 LNl, and vl has integral presentation degree<=2Nl after multiplication by p^(5 LNl). Since LNl=O(log(l+2)), the exponents l-5 LNl tend to infinity and are at least l/2 for sufficiently large l. Regrouping terms by these integer exponents gives a finite p denominator and linear degree/valuation presentation. Hence v=sum_l p^l vl belongs to R. The six coefficients of n=sum_l p^l nl converge in K. Derivation on the displayed integral generators is p-adically continuous, so termwise equality gives

    b=K(v)+n in R.                                  (7)

The observations on this weak sum equal the convergent sums of the observations on bl: the original degree bound gives geometric convergence on a common closed annulus, and residue is continuous there. Thus n is exactly the normal form specified by la(b) and Q(b), independent of the chosen weak presentation. If all six observations vanish, (7) supplies a weak primitive. Conversely Section4 shows every weak K-image has zero observations. Normal representatives have the independent values(4), proving inclusion of rational cokernels is bijective and the stated six-dimensional row result.

Weak primitive uniqueness is not needed. This specific-ring/frame test supplies no computed general Frobenius values, executable consumer, original functional, strong-completion theorem or comparison in the old excluded shape.
