# The actual six-boundary weak row Frobenius

UNREVIEWED THREE-AUTHOR WHOLE, EM-DIRECT-88303D / EM-DVR-F73673 / EM-DVR-BFF6DC.
This is one new paper unit for joint author checking, not a peer verdict. The
old six-dimensional normal-form proof and its genuine review are inputs, not
votes on the new geometric and arithmetic arrows below. No scientific program,
Native operation, new Task, or Source/RA mutation is used to construct this text.

## 1. Object, conventions, old inputs and the new assertion

Let p be prime with p=13 or19 mod24. Work first over Z_p; O is the previously
allowed complete unramified DVR with perfect residue field, Witt automorphism
sigma and fraction field K=O[1/p]. No power-series base is treated as a DVR. Put

    S=4r^3-3r, f=1-r^2, q=4r^2-1, P=fq,
    A=2S-1, B=4S-5, D=(2P)^(-1)[[A,1],[B,-A]],
    Dalg=Z_p[r,P^(-1)], R=O[r,f^(-1),q^(-1)]^dagger[1/p].

Rows have connection L_D(h)=h'+hD. The proper family is the literal cubic

    Y^2=X^3+alpha X+gamma,
    alpha=3(4S-5), gamma=4S^2-28S+22.

Its retained proper basis is e=(omega,eta), omega=dX/(2Y), with eta represented
by the corrected proper cocycle, rather than just the affine form X omega.
The cohomological Frobenius convention is F(e)=e M_psi. Period comparison is
G_psi=M_psi^(-T). Its induced row-oneform map is

    Phi_psi(b dr)=psi' sigma(b)(psi) M_psi^T dr.                 (1)

Transpose, coefficient sigma and the base oneform derivative are all part of
this definition. The specified old actual proper weak realization supplies M
for phi(r)=r^p, integral weak with det M=p, and its actual canonical finite-level
comparison, not merely a horizontal differential solution.

We consume the proved six-boundary theorem at Source1c619205b6abd1f15e923fdfe126edf518e19b7b.
It identifies coker L_D on R-rows with K^6. For a=1,-1,1/2,-1/2 let H_a be
its normalized period gauge, H_a(0)=I in x=r-a, and k_a=(1,c_a)^T, where c_a=-1
for S(a)=1 and c_a=3 for S(a)=-1. The finite coordinates are

    ell_a(b)=Res_x(b H_a dx) k_a.

At infinity z=1/r, in the actual good frame below, write Q(b) for the row
residue after its normalized regular gauge. On scalar rows n e1, where

    n=c0+c1 r+sum_a d_a/(r-a),

the six coordinates are (d_1,d_-1,d_1/2,d_-1/2,-c0,-c1/8). They kill all weak
L_D-images and are complete. The old proof also gives full open-disc gauge
bounds and the weak/Robba restriction needed for continuous residues. We do
not reprove its dimension, normal form, primitive loss, or weak regrouping.

The new assertion is that the actual map (1), on this specified weak cokernel,
is independent of the concrete congruent Frobenius lifts used below and has
coordinates

    (d_1,d_-1,d_1/2,d_-1/2,Q1,Q2)
      |-> (p^2 sigma(d_1),p^2 sigma(d_-1),p^2 sigma(d_1/2),
           p^2 sigma(d_-1/2),(p^2/beta) sigma(Q1),p beta sigma(Q2)).       (2)

Here beta is the actual canonical good-central matrix entry M_infty(0)_22 in
the fixed corrected basis, and beta belongs to Z_p^*. Its numerical value is
not computed. Formula (2) will follow from actual models and maps. It is not
an arbitrary choice of a diagonal Frobenius compatible with the connection.

## 2. Three genuine additional log models

The old r=1 base inverted factors vanishing at the other nodes, so cannot be
pulled into their regular local rings. For each a=-1,1/2,-1/2 set x=r-a and

    B_a=Z_p[r, product_(b!=a)(r-b)^(-1)], b in {1,-1,1/2,-1/2},
    A_a=Z_p[[x]], log chart N -> x.

The genuine ordinary common open is B_a[x^-1]=Dalg BEFORE completion. A_a is
completed evaluation, not a ring identified with B_a or its ordinary open.
The new finite data are

    a        S(a)  ord_x(S-S(a))  e=ord_x(discriminant)  c_a  nu_a  P'(a)
    -1        -1          1                  3           3     3      6
     1/2      -1          2                  6           3     3      3
    -1/2       1          2                  2          -1    nu     -3

Here nu^2=-3; nu exists in Z_p since p=1 mod3. All displayed roots and
denominators are p-units. The retained old a=1 row has e=1,c=-1,P'(1)=-6.
In particular p does not divide any thickness e in {1,2,3,6}.

To establish the actual model, choose an etale local critical section C with
3C^2+alpha=0, C(0)=c_a. The derivative6c_a is a unit. Put Z=X-C, choose
h^2=3C+Z with h(0)=nu_a, and put W=Zh. Both h and W_X=h+Z/(2h) are units near
the node. Then U=Y-W,V=Y+W satisfy

    UV=gamma-2C^3,
    4alpha^3+27gamma^2=27(gamma-2C^3)(gamma+2C^3).

The second factor has central value -4 for c=-1, or108 for c=3, hence is a
unit. Directly factoring the displayed discriminant gives gamma-2C^3=x^e u
with u a unit and e as in the table. Absorb u into V. The resulting chart is
UV=x^e, the actual log base change of UV=s along s=x^e. This proves integral
log smoothness; it is not inferred from a discriminant order alone. It glues
to the usual pulled-back base log structure on the smooth complement.

Relative to the log base, dlog U+dlog V=0 and dW=-Y dlog U. Thus

    omega=-(2W_X)^(-1) dlog U.

This is a unit log-differential generator also at the thick node. Infinity
and the remaining smooth points give the same global dualizing generator.

Here is why the old proper/free and all-PD constructions apply to these new
models. With t=-X/Y and h0=Y/X=-1/t one has the literal identity

    X omega-dh0=(alpha/X+2gamma/X^2)omega.                     (3)

Use U0=the affine complement of infinity and a suitable infinity neighborhood
V0, refining to affine charts. The proper cocycles, with alpha_V-alpha_U=d b_UV,
are

    Omega=(omega,omega;0),
    Eta=(X omega,(alpha/X+2gamma/X^2)omega;-h0).               (4)

The monic plane cubic sequence gives H^1 O(3 infinity)=0 over every coefficient
algebra. The functions X^i and YX^i have distinct pole orders2i and2i+3, with
unit leading terms even over rings with nilpotents. Its principal-part
sequences give H^0 O=T, H^1 O(infinity)=0, and H^1 O=T times the class of1/t,
where T is the coefficient algebra, not a localization ring. The Cech part
-h0=1/t of Eta lifts that last generator. Since Omega_log=O omega by the actual
chart just proved, the hypercohomology sequence gives free H^1 with basis
Omega,Eta, and free H^0,H^2. These literal cochains commute with coefficient
change. The bounded affine Cech terms are flat and compute the declared
derived coefficient changes; no flatness of the coefficient algebra is assumed.

At p^n level the old all-PD construction can now be repeated with the actual
log section x. On an exact base immersion its lift is a log section and the
other inverted factors lift as units. A PD ideal killed by p^n is elementwise
nilpotent, which suffices for the local extension and unit arguments. The
actual HK embedding/product comparisons identify the relative proper complexes
and descend the canonical maps on overlaps. This is exactly the proved
proper/all-PD construction with its new hypotheses verified, not a passage
from the excluded old B-ring. It supplies canonical integral matrices M_a,n
for psi_a(r)=a+(r-a)^p: substituted inverted factors are pth powers modulo p,
hence units modulo p^n. Their compatible A_a evaluation is regular.

The actual log connection is also identified here. Lift x d/dx in the chart
UV=x^e u by assigning log value e+xu'/u to U and0 to V; ordinary smooth
charts give the other lifts. Cech Lie derivative/Cartan descent gives the
intrinsic connection on (4). On Dalg it is the saved D^T. Both modules are
free and x is a non-zero-divisor even modulo p^n, so equality after ordinary
localization identifies the regular logarithmic matrix with xD^T already on
B_a/p^n. This justifies using the literal residues below for the actual object.

## 3. Actual lift comparison, determinant and a weak oneform homotopy

The determinant input for the new nodes must not reverse the old cup proof,
whose Section5 already assumed det M=p. We instead use the same actual
canonical proper complex on the finite common open Dalg/p^n.

For polynomial lifts psi,chi congruent modulo p define period transport J(u,v)
by its formal Taylor expansion, with

    partial_u J=D(u)J, partial_v J=-J D(v), J(v,v)=I.

Its coefficients satisfy C_0=I,C_(j+1)=C_j'+C_j D. They are p-integral rational
functions with generator degree growing at most linearly in j. For our lifts
phi=r^p, theta=1+(r-1)^p, psi_a=a+(r-a)^p, delta=psi-chi is in pZ_p[r] and has
degree at most p-1. The transport term delta^j C_j(chi)/j! has valuation at
least j-v_p(j!). Substituted inverse f(chi),q(chi) are expanded using their
ratios to f^p,q^p, which are1+p times integral rational functions. The negative
binomial coefficients are integral. With these extra geometric indices k,
the degree is O(j+k) and valuation at least j-v_p(j!)+k. Since p>2 this grows
linearly. Thus the substitution is genuinely integral weak transport.

The same proof works for a weak input sum_l p^l b_l of generator degree O(l):
the combined terms have degree O(l+j+k) and valuation at least
l+j-v_p(j!)+k. Regrouping gives an actual weak presentation. Differentiating
the rational coefficients or adding one integration denominator changes only
the indicated linear factorial index. No strong-completion input is silently
declared annular or weak.

The actual finite PD comparison, followed by these proved weak substitutions,
has the definite direction

    M_psi^T=J(psi,chi) M_chi^T.                              (5)

The identity is supplied by canonical unit/crystal functoriality on the same
proper complexes. Horizontality alone would leave an unidentified constant.
Trace D=0 implies det J=1 as an exact formal characteristic-zero identity with
initial value1. The integral weak evaluation preserves that identity and its
reductions modulo p^n. In particular this is the actual trivial determinant-line
stratification, not the insufficient statement that a derivative vanishes in
characteristic p. Taking chi=phi and using the known actual det M_phi=p gives
det M_a,n=p on Dalg/p^n. The map B_a/p^n -> Dalg/p^n localizes the non-zero-
divisor x and is injective. Pull back this equality at each n, then take the
specified compatible coefficient limit. Hence det M_a=p. No inverse of M_a,
cancellation of p in torsion, or exchange of localization and a limit is used.

For completeness the map (1) is a map on the row cokernel: actual
cohomological horizontality is

    (M_psi^T)'+M_psi^T D=D_psi M_psi^T,
    D_psi=psi' sigma(D)(psi).

It gives Phi_psi(L_D h dr)=L_D(sigma(h)(psi)M_psi^T)dr.
To compare the resulting class maps, for any weak row b define

    I_b=integral_(chi(r))^(psi(r)) sigma(b)(u)J(u,chi(r))du
       =sum_(j>=0) delta^(j+1)/(j+1)!
                    (nabla_row^j sigma(b))(chi).

This integral is its Taylor series, not a path selection. The preceding
degree/valuation bounds prove it is weak. Differentiation of the convergent
series gives

    I_b'+I_b D_chi=psi' sigma(b)(psi)J(psi,chi)-chi' sigma(b)(chi),
    L_D(I_b M_chi^T)dr=Phi_psi(b dr)-Phi_chi(b dr).             (6)

Thus the actual class action is lift independent for these concrete lifts.
The regular log lift psi_a is used at a node; raw phi is compared only on the
punctured ordinary common open. No raw non-log lift is evaluated at the node.

## 4. Fixed graph class and the positive finite residues

At the central cubic for c=c_a, its ordinary normalization is P^1 with

    v=Y/(X-c), X=v^2-2c, Y=v(v^2-3c),
    omega=dv/(v^2-3c), kappa=eta-c omega=dv.                  (7)

The last equality does not make kappa exact on the singular proper curve.
Its normalized proper cocycle (4) has primitives

    f_U=v, f_V=v-h0=c v/(v^2-2c), f_V-f_U=-h0.

They are regular on the chosen normalized charts, f_V vanishes at infinity,
and the ordered branch jump v=+nu_a minus v=-nu_a is2nu_a, a unit.

The thick central relation dlog U+dlog V=e dlog x=0 relative to the base shows
that the normalized log forms have residues whose sum is zero. Consequently
the actual conductor and residue maps give a short exact sequence of complexes

    0 -> [O_C -> Omega_C/T,log]
      -> [q_*O_P1 -> q_*Omega_P1(branches)]
      -> [O_node --0--> O_node] ->0.                        (8)

In degree0 the quotient is value at +nu_a minus value at -nu_a; in degree1 it
is the sum of residues. This assertion holds over Z/p^n with its nilpotents.
Global normalized functions are constants with zero difference, so the
connecting map R_n -> H^1 of the first complex is injective. We do NOT equip
the ordinary normalization with a nonexistent log morphism.

The actual HK embedding/de Rham comparison identifies degree-zero constants
with the unit map underline R_n -> Ru_crys,* O. Naturality of the ordinary
constant-sheaf conductor sequence with (8) therefore identifies its connecting
class with the crystalline graph injection j_a,n(1). The explicit primitives
in (7) show

    sp(kappa)=2nu_a j_a,n(1).                                (9)

Absolute log Frobenius and the base map N->pN act naturally on that unit.
The two ordered branches are individually F_p rational, so the normalization
diagram fixes its conductor generator. Thus Phi(j(1))=j(1) and Phi(kappa)=kappa.
For O this is sigma-semilinear; the named unit1 and nu_a lie in Z_p and are
sigma-fixed. This checks the new thickness explicitly rather than inferring
graph identity from equal dimensions or nilpotent residues.

In the original cohomological basis the residue is

    N_coh=(2P'(a))^(-1)[[A(a),B(a)],[1,-A(a)]].

Set F_a=[[-c,0],[1,1]], so the graph basis is (kappa,eta)=e F_a. Direct
substitution in the displayed table gives

    F_a^(-1) N_coh F_a=(e/12)E12.                           (10)

The three positive coefficients are1/4,1/2,1/6, respectively; the old a=1
coefficient is1/12. These are the literal rational signs for x=r-a, with the
same ordered branches, not an ordering of a p-adic field. The discriminant
exponent e, not the smaller ord(S-S(a)), is required at S=-1.

The actual graph identity and det M_a(0)=p from Section3 now give

    M_graph(0)=[[1,b_a],[0,p]], b_a in Z_p,
    M_orig(0)=F_a M_graph(0)F_a^(-1)
       =[[1-b_a,-c b_a],[(b_a+p-1)/c,b_a+p]],
    M_orig(0)^T k_a=p k_a, k_a=(1,c)^T.                    (11)

No value of b_a is needed. The same identity follows without any inverse in
a torsion ring from M^T J_alt M=(det M)J_alt and M kappa=kappa. Only after
inverting p may G(0)k_a=p^(-1)k_a be written. The graph cohomology eigenvalue1
must not be assigned to this dual period kernel.

## 5. The four finite observations have multiplier p squared

The normalized gauges of the old normal-form theorem satisfy

    H_a'=D H_a-H_a N_a/x, N_a=Res(D dr), H_a(0)=I, N_a k_a=0.

Their coefficients and k_a are rational, hence sigma-fixed. Actual canonical
horizontality for psi_a:x->x^p gives

    G_a(x) H_a(x^p)=H_a(x)G_a(0),
    M_a(x)^T H_a(x)=H_a(x^p)M_a(0)^T.                       (12)

To justify the constant and exclude any hidden horizontal parameter, put
C=H_a^(-1)G_a H_a(x^p). Then xC'=N_a C-p C N_a. Its constant term is G_a(0)
and satisfies N_a C0=p C0 N_a by central horizontality. For each j>0 the
operator jI-(left N_a-p right N_a) is invertible over K, since its correction
is nilpotent. Thus C_j=0. This proves (12) formally. The old full-disc bounds
identify the same functions on the actual common annulus.

Use (11), (12) and (1). The residue substitution x->x^p, valid for convergent
annular Laurent series, gives

    ell_a(Phi b)
      =Res(p x^(p-1) sigma(b)(x^p)H_a(x^p)M_a(0)^T dx)k_a
      =p^2 sigma(ell_a(b)).                                (13)

One p is the action M_a(0)^T on k_a; the other is the residue degree of the
base oneform. Weak/Robba continuity handles infinite principal parts. Equation
(6) identifies this regular local-lift action with the common ordinary lift
on the weak class. The retained actual r=1 graph certificate proves the same
calculation there. Thus (13) covers all four coordinates without replaying
its old central b calculation or substituting an excluded base ring.

## 6. The actual good-infinity arithmetic block

We reuse the old actual good-infinity model and canonical comparison, not its
old isogeny/no-eigen-p argument. With z=1/r, X_old=r^2 X,Y_old=r^3Y, the good
central fibre is

    E0:Y^2=X^3+64, discriminant=-2^16*3^3.

The old good integral regular M_infty(z) has det p, and its actual canonical
specialization is the crystalline Frobenius of E0 in the fixed corrected frame
e_infty=(Omega,Eta). The ordinary family/coefficient identifications precede
completion. In particular its ordinary common-open equality is
(Cbase tensor O)[z^-1]=Dalg[r^-1], not a localization/limit exchange. The saved
old frame change is e_old=e_infty diag(z,z^-1).

Choose zeta of order3 in Z_p. It is sigma-fixed, and zeta-zeta^2 is a unit.
The actual automorphism rho:(X,Y)->(zeta X,Y) acts on the fixed proper classes
of E0 with two distinct characters. Here all Cech components are checked:

    Omega=(dX/(2Y),dX/(2Y);0),
    Eta=(X Omega,128 X^(-2)Omega;-Y/X),
    d(Y/X)=(X-128/X^2)Omega.

Omega has character zeta. The affine and infinity oneforms AND the correction
function -Y/X of Eta all have character zeta^2. A stable refinement of the
cover may be taken if necessary. There is no unspecified holomorphic shift.
Canonical crystalline Frobenius is natural for this actual automorphism.
Writing T=diag(zeta,zeta^2), its convention gives M0 sigma(T)=T M0. Hence
the unit character difference forces strictly

    M0=M_infty(0)=diag(alpha0,beta), alpha0 beta=p,
    alpha0,beta in Z_p.                                    (14)

It remains to locate the p-divisible column for this actual map, rather than
for an arbitrary commuting matrix. On a smooth affine formal cover of E0,
choose actual local Frobenius lifts F_i. If u is an etale coordinate,
dF_i(u) is divisible by p, since F_i(u)=u^p modulo p. Thus each oneform
component F_i^*Omega is p-divisible. On an overlap the difference of the two
lifts is delta in p times the smooth coordinate ring. The canonical PD/Taylor
comparison of the global holomorphic form Omega=g(u)du has function component

    sum_(j>=0) F_i^*(partial_u^j g) delta^(j+1)/(j+1)!.

The derivatives are integral on the etale chart; each term has valuation at
least (j+1)-v_p((j+1)!)>=1 and these valuations tend to infinity. The overlap
functions are therefore also p-divisible. These are exactly the oneform and
overlap-function components of the actual degree-one Cech/de Rham Frobenius
cocycle, identified by the actual PD product comparison. Since the original
global Omega has zero overlap function, there is no omitted degree-zero input
term; higher nerves have no extra degree-one component.

All terms of this smooth affine Cech complex are p-torsionfree. Divide the
whole displayed cocycle by p. Its total differential remains zero by
torsionfreeness, so it is an integral cocycle. Consequently the actual image
F(Omega) is in p H^1_crys(E0/Z_p). This free module has the retained integral
basis Omega,Eta; (14) therefore implies alpha0 in pZ_p. Its determinant p
then forces alpha0=p/beta with beta in Z_p^*. This is an actual canonical
unit, not a free normalization parameter. No point counts or Jacobi sums are
used, and beta's value is left unevaluated.

The old regular gauge H_infty has H_infty(0)=I, rational coefficients and
proved full open-disc convergence. Actual horizontality gives
M_infty(z)^T H_infty(z)=H_infty(z^p)M0^T. The actual good-frame coefficient
map, including the frame change above, therefore gives for every weak row

    Q(Phi b)=p sigma(Q(b))M0^T
       =((p^2/beta)sigma(Q1(b)),p beta sigma(Q2(b))).         (15)

Again the initial p is the oneform residue degree; it is not part of M0.
For arbitrary coefficients sigma cannot be suppressed. This calculation uses
the proved weak-to-annular map and does not assert that strong completed
functions have convergent annular Laurent expansions.

## 7. Assembly, exact scope and contribution

Equation (6) makes the actual weak class map independent of which declared
congruent lift is used to test a coordinate. Equations (13) and (15), followed
by the already proved completeness of the six observations, prove (2). This
is a sigma-semilinear isomorphism over K: beta is a unit and all six displayed
scalars are nonzero. Five diagonal multipliers have valuation2 and one has
valuation1 in these coordinates. This conclusion does not evaluate beta or
reprove the old isogeny exclusion.

The precise new content beyond the old normal form is the actual extension
to three omitted log bases, their canonical finite graph/basis/determinant
comparison, the actual class lift homotopy, and the strict good-central
arithmetic block. EM-DIRECT-88303D supplies the models/all-PD applicability,
common-open determinant, weak Taylor oneform homotopy and assembly, with the
initial directed rho/Hodge direction. EM-DVR-F73673 supplies the proper
kappa cochains, thick graph/unit naturality, positive residues and finite
dual variance; he identified the determinant circular-use risk in the first
unfrozen working. EM-DVR-BFF6DC supplies the corrected CM-character and
actual p-divisible Hodge-column proof. Their mutual checking is coauthorship,
not independent review. The old proper input authors and all previous true
reviews retain their original NONBLIND and scope histories. Root supplies
CONTROL/fair scheduling, not a second mathematical vote.

This assertion is confined to the named actual proper object, the fixed
corrected frames, the specified weak ring and row-oneform action (1). It
does not construct a full rank-four Frobenius, identify an original source
functional, evaluate a geometric source, claim all gauges or strong
completions, prove uniqueness of arbitrary weak primitives, or close the
mother Goal. No stopped m7/core98 budget or Task is revived. All old frozen
manuscripts and their UNREVIEWED historical metadata remain unchanged. A
genuinely different reviewer must read this whole proof after its real freeze.
