# The full central Frobenius entry of the actual proper CM24 witness

Author EM-DIRECT-88303D. New unreviewed RESULT_ONLY application to the actual proper witness, after preliminary reasoning, not blind preregistration. Zero scientific programs or budget renewal.

## 1. Exact actual object and outcome

Let p=13 or19 modulo24 and A=Z_p[[t]], t=r-1. Keep the ACTUAL proper Weierstrass family and corrected cohomology classes
    s=4(1+t)^3-3(1+t),
    Y: y^2=x^3+a x+b0, a=3(4s-5), b0=4s^2-28s+22,
    omega=dx/(2y), eta=x omega,
where eta means its corrected proper hypercohomology cocycle. Its actual compatible log-crystalline direct image and canonical Frobenius, evaluated through theta(t)=t^p, are the prior finite-type/all-PD witness, not a matrix chosen by horizontality.

The previously proved central interfaces are
    kappa=omega+eta=2nu j(1), nu^2=-3,
    Phi_theta(kappa)=kappa,
    f=(kappa,eta), N_f=E12/12,
    M_f,theta(0)=[[1,b],[0,p]], b in Z_p.
Here j is the ordered constant graph injection. The prior proper construction permits arbitrary coefficient base change. Since p=1mod3, nu lies in Z_p and coefficient Witt Frobenius fixes it.

The full value proved below is
    b=(1-p)+(p-1)log(6)/12.                         (1)
The logarithm is the Iwasawa logarithm on the p-unit6, namely log(6)=log(6^(p-1))/(p-1). In the EXACT saved solution frame e_hat=(kappa/12,eta), this gives
    c_w=-12b/p=(p-1)(12-log(6))/p.                 (2)
Equation(2) concerns this named proper witness, not an unprovided source functional or arbitrary frame.

Conrad’s2006 Arithmetic moduli paper section2.5/Example2.5.1 supplies the algebraized one-gon Tate curve and pointed map Tate(q)->Tate(q^p), defined by power maps on annuli/formal groups and permitting adic noetherian base change. No flatness of this map at a node is used. The official248B notes section19 supply the standard nodal fiber, j_T^(-1)=q+O(q^2), and invariant dualizing form Omega restricting to du/u. We import no complete Weierstrass coefficient formula. HK2.17 supplies the actual crystal/connection interpretation; section4 derives central transport from the cocycle.

## 2. An actual Tate parameter and an integral family isomorphism

Write c4,c6,Delta for the usual invariants of the displayed short Weierstrass equation. Direct polynomial identities give
    c4=144(5-4s), c6=-864b0,
    Delta=-6912(s-1)(s+1)^3,
    j_Y^(-1)=-(s-1)(s+1)^3/[432(5-4s)^3].
Thus c4,c6 are units in A, with values144,1728 at0, and
    j_Y^(-1)=-t/6+O(t^2).
All divisions here are by p-units or by the displayed units of A.

The integral series J(q)=j_T(q)^(-1)=q+O(q^2) has a compositional inverse over Z_p. Hence
    q(t)=J^(-1)(j_Y^(-1))=-t/6+O(t^2) in tA.      (3)
This is t-adic substitution at a topologically nilpotent element. The separate p-adic crystal evaluations remain those below.

Base change the algebraized Tate curve along Z[[q]]->A defined by(3). Let C4,C6 be its invariant coefficients for the canonical differential Omega; their values at0 are1,-1. Near the standard one-gon,2 and3 are invertible, so completing the square and translating x gives a short Weierstrass model with coefficients -C4/48,-C6/864 and invariant differential Omega. Equivalently this follows from the usual |3O| Weierstrass construction normalized by Omega.

Put alpha=c4/C4 and beta=c6/C6. Equality of j-invariants implies beta^2=alpha^3, since c4^3-c6^2=1728Delta and the same identity holds on Tate. At0, alpha=144 and beta=-1728. The unit beta/alpha therefore has value-12. There is a unique v(t) in A^x with
    v(0)=2nu, v(t)^2=beta/alpha,
by square-root recursion since2v(0) is a unit. Then v^4=alpha,v^6=beta. In short coordinates x_T=x_Y/v^2,y_T=y_Y/v^3 give an actual projective isomorphism
    i:Y -> Tate(q(t)), with i^*Omega=v(t)omega.    (4)
It preserves infinity. The opposite root gives inversion and the same conclusions.

These are actual Spec A schemes. Their semistable log structures agree since q(t)=t times a unit. No unspecified formal-site identity, localization/limit exchange or two-dimensional analytic uniformization is used.

## 3. A genuine Frobenius lift in the Tate coordinate

Because q'(0)=-1/6 is a unit, q has a compositional inverse over Z_p. Define
    psi(t)=q^(-1)(q(t)^p).
Then
    q(psi(t))=q(t)^p,
    psi(t)=q1^(p-1)t^p+O(t^(p+1)), q1=-1/6,
    psi(t)=t^p modp.
Reduce q(t)^p=q(t^p) in F_p[[t]] and use its inverse for the last equality. Thus psi/t^p lies in1+pA. This is a legitimate standard-log-base lift of monoid degree p, different from the old ramification1 raw lift.

Use Conrad's algebraized pth-power map
    pi_p:Tate(q(t))->Tate(q(t)^p).
Combining(4) and its psi-pullback gives an actual pointed log morphism
    F_psi:Y -> psi^*Y.
The annular power maps reduce to absolute Frobenius; formal GAGA gives the same reduction on the algebraization. The Z_p-defined isomorphism(4) commutes with that reduction, including the base log unit. This lifts actual absolute log Frobenius.

Functoriality of the HK embedding comparison identifies the pullback of this morphism with the actual canonical crystalline Frobenius evaluated through psi, at every p^n level. This uses the already existing proper crystal: the two maps from Spec A_n to the finite-type log base have the same Frobenius reduction, and (p) has its canonical PD structure. Arbitrary coefficient base change was already proved for its proper representatives. No new scheme-Frobenius lift for the original theta is needed.

The invariant differential pulls back by pi_p to p Omega, as can be checked on the formal group u->u^p; invariant differentials are determined at the identity. Hence
    Phi_psi(psi^*omega)=p v(t)/v(psi(t)) omega.
At t=0 this is exactly p omega. On the central normalization the power map preserves the two ordered branches and the graph; its pullback on the constant graph cocycle1 is identity. The prior actual normalization/graph comparison is functorial for this map, so Phi_psi(kappa)=kappa. In the central basis f=(kappa,eta), omega=kappa-eta therefore gives
    M_f,psi(0)=[[1,1-p],[0,p]].                  (5)
This comes from actual pullback in another valid lift.

## 4. Actual central log-PD transport and its direction

The following calculation applies to the actual rank-two crystal already constructed. On the logarithmic diagonal write
    u=t1/t2-1.
Restrict its stratification to t1=t2=0 in the fixed central frame f, and call the matrix from the endpoint1 frame to the endpoint2 module S(u). Then S(0)=I, its first coefficient is the actual residue N=N_f, and its crystal cocycle is
    S(u+v+uv)=S(u)S(v).
The frame at the center is constant, so no extra coefficient substitution remains in this identity. After characteristic-zero formal extension, differentiation in v at0 gives
    (1+u)S'(u)=S(u)N.
Since N^2=0, formal coefficient uniqueness yields
    S(u)=I+Nlog(1+u).                            (6)

Here is the integral PD justification, rather than an appeal to a guessed boundary Taylor series. In divided powers u^[n], the coefficient for n>=1 in(6) is
    (-1)^(n-1)(n-1)!N.
These coefficients are integral and tend to0 p-adically. The compatible central proper modules are free over Z/p^n; their inverse limit is free over Z_p. The p-completed PD-polynomial coefficient module is p-torsion-free, so its coefficientwise injection into characteristic-zero formal series detects equality with the actual stratification. Thus the formal calculation computes the actual compatible crystal map. Specialization u=epsilon in pA using the canonical divided powers is legitimate at every finite p-level and in the limit. At the center it gives I+Nlog(1+epsilon(0)); the logarithm terms have valuation at least n-v_p(n), tending to infinity. This argument uses no DVR property of A.

The convention agrees with the log-PD coordinate p1^*t/p2^*t-1. To compare lifts rho1 and rho2 with rho2/rho1=1+epsilon, choose endpoint1=rho2, endpoint2=rho1. Naturality of the SAME canonical crystalline Frobenius then gives
    M_rho2(0)=M_rho1(0) S(epsilon(0)).           (7)
This is right multiplication, with no extra p in the logarithm.

Apply(7) to rho1=psi, rho2=theta. Both are valid log lifts, and their quotient is in1+pA. Its constant value is
    c0=(theta/psi)(0)=q1^(1-p)=(-1/6)^(1-p).
Equation(6) and(5) show that the off-diagonal entry changes by log(c0)/12. This is actual central crystal transport, not evaluation of punctured Taylor transport at the boundary.

## 5. Full value, consistency and exact stopping boundary

Since log(-1)=0 on p-units,
    log(c0)=(p-1)log(6).
Substitution into(5)-(7) proves(1). Passing to e_hat=(kappa/12,eta) multiplies its upper-right entry by12. Taking the inverse transpose of [[1,12b],[0,p]] gives [[1,0],[-12b/p,1/p]], proving(2) in the stated solution direction.

As log(6) belongs to pZ_p, (1) reduces to b=1 modp and (2) gives p c_w=-12 modp and v_p(c_w)=-1. These are checks against the earlier finite theorem, not separate discoveries. The value descends to Z_p and extends through the declared unramified coefficients.

The gain is the full proper-witness scalar via an actual Tate lift and crystal transport. The earlier9064B proof/PASS is unchanged; its full-value gap is resolved only for this object/frame.

No weak/dagger property, first full rank-four comparison, remaining source-row class equality, independently defined old formal object, source-compatible realization, original observation, global sign or Y follows. In particular (2) cannot be assigned to another full comparison until its actual proper quotient and frame are identified. No old HesseP3, ad_R^4, radius proof, formal freedom or no-go was rerun. This proof needs a genuinely new independent whole-scope review; prior author or peer verdicts are not that review.

Researcher-ID: EM-DIRECT-88303D / TASK_RESEARCH
