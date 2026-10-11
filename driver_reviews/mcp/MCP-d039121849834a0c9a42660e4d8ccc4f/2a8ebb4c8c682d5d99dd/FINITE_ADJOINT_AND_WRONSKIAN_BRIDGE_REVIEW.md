# Independent paper review of the finite Gauss adjoint and Wronskian bridge

Verdict: PASS for the exact adjoint, finite integral, double-sum and their
identity with the previously fixed Wronskian scalar. No new arithmetic
campaign, provider query, Task claim or formal acceptance was performed.
UR/LIFT, the raw-period normalization and the mathematical mother goal remain
OPEN. This is shared, directed, nonblind review of a paper consequence.

Exact full-read author input: FINITE_ADJOINT_GAUSS_CONCOMITANT_PREPARATION.md,
4780B, SHA256 4e6fe9b1aa8ec5ce618f79341c7b012ad8591713fd402af537e3fd5e56e3fca8,
Git blob 60cc07dc1c35f9758ddabdb578851dc3a1509aa6.
Reverse Gauss input: author certificate SHA256
4de6c2ae746acf9dad026c334b9aa2998d49e3147606fc35422be4d3901d8869,
reviewed independently at SHA256
d48e893d7d2e6992cb6a1179191f51ef779cb056025f38bed1f9bd60db1a5d52.
Original integrated Wronskian preparation SHA256
ee3f73f6b81985333694ce83d826e11e1db9902681be6bff490e2a2ab9430b1e.
Primary scientific Source is d9f1cc87019d8b43e7058b98f545c025bc753cfe,
Task RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT,
publication TP2-21DFFFD4A8788C0FF5CA. Previously frozen bytes are unchanged.

Let p=6m+1>=7. The independent V=M mod p=f_p mod p has degree exactly
m and satisfies D_G V=0. The independent reverse C has degree <=3m-1
and satisfies D_C C=-[(1-w)^(3m)-1]/(9w). For a=w(1-w),
b=1-3w/2, c=-1/18, the formal flat-dw adjoint is

    (a d^2+b d+c)^*=a d^2+(2a'-b)d+(a''-b'+c).

Its derivative coefficient is 1-5w/2 and its constant is -5/9, exactly
D_C. For the concomitant

    K=a(CV'-VC')+(b-a')VC
     =w(1-w)(CV'-VC')+(w/2)VC,

expanding its derivative gives coefficients b on CV', b-2a' on VC'
and b'-a'' on VC. Thus K'=C D_G V-V D_C C, with the displayed signs.
Consequently

    K'=(1/9)V[(1-w)^(3m)-1]/w,       K(0)=0.

Both quotients here are polynomials; no punctured-domain division is used.
The degree bound is K<=4m<p, and the integrand has degree <=4m-1.
Every integration denominator lies in 1,...,4m, hence is a unit in Fp.
A derivative-zero polynomial of degree <p is constant, so the endpoint
fixes K uniquely. This proves the memo's finite integral without a hidden
w^p kernel. It is coefficientwise polynomial integration over Fp, not an
analytic contour integral or a choice of period normalization.

At the target CM classes, V(1/2)=0. The concomitant is therefore
K(1/2)=C(1/2)V'(1/2)/4=-tau. The integral and the double-sum signs are
correct:

    tau=-(1/9) sum_(k=0)^m sum_(r=1)^(3m)
              v_k(-1)^r binom(3m,r)2^(-(k+r))/(k+r) mod p.

Indeed expanding the numerator uses powers z^r for r>=1, and multiplying
by V produces z^(k+r-1), whose primitive evaluation at 1/2 is exactly
2^(-(k+r))/(k+r). The bounds 1<=k+r<=4m<p justify all divisions.
This is a separate constructor of the finite correction; it does not
consume U or an old target value.

The following global bridge was proposed by me and independently checked
by the author after the author memo was frozen; it is saved here without
altering those 4780B. In Fp[x], set t=1-2x and q=4x(1-x). The earlier
full objects satisfy A=t C(q), H=V(q). The Wronskian is independent of
adding B H to I, so T_x=x(1-x)(A'H-AH') is exactly the earlier T_*.
Using A'=-2C+4t^2 C' and H'=4t V', one obtains

    T_x=(q/4)[(-2C+4t^2 C')V-4t^2 CV']
       =-(q/2)CV-q(1-q)(CV'-VC')
       =-K(q).

This is a global polynomial equality, not just a CM evaluation. It proves
that the new integral uses exactly the original Wronskian normalization.
Differentiating also recovers T_x'=-(2/9)S_p H, since q'=4t and
S_p=2t[(1-q)^(3m)-1]/q. Both original endpoints x=0,1 map to q=0,
matching K(0)=0. There is no extra condition K(1)=0: the point q=1 is
the ramification image and must not be assigned the x endpoint condition.

The q primitive has degree <=4m<p. Upon pullback its degree can reach
8m=p+2m-1, which explains the original x primitive's resonant p term.
The new integral avoids that resonance by genuine polynomial descent;
it does not delete an arbitrary integration constant from the old object.

The retained old fixed target is still

    U=(M(1/2)/p)(M(1/2)+6M'(1/2)) mod p^2,
    U=1+p(R_p+6tau) mod p^2.

The old R_p is independently source-defined, and M(1/2)/p still requires
M through p^3. This adjoint proof evaluates the finite correction tau,
but does not evaluate U's first divided digit or prove the target equality.
A succeeding boundary/telescoping certificate must derive UR first and
then compare its second digit with the fixed OLD-R observer. Full signed
marked branches, derivatives, Jacobians, exact lifts and h/omega tags remain.

Author EM-ENTERPRISE-CB50ED supplied the adjoint and double-sum derivation;
reviewer EM-ENTERPRISE-3F2857 independently checked its paper algebra and
supplied the global T_x=-K(q) bridge; Root EM-DVR-4C90FB coordinates the
next scope. No blind or exclusive-discovery claim is made.

Researcher-ID: EM-ENTERPRISE-3F2857 / RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT
