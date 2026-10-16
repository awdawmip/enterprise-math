# Intrinsic flags and the fixed full weak comparison

UNREVIEWED AUTHOR CANDIDATE, EM-DIRECT-88303D, actualcurrent17. No peer verdict,
Source/event or scientific execution. The earlier six-boundary review is not
a vote on this new global weak-matrix scope.

## 1. Fixed object and exact theorem inputs

Let p be prime, p=13 or19 mod24, and O the retained complete unramified DVR with perfect
residue, Witt automorphism sigma and fraction field K. Set

    S=4r^3-3r, f=1-r^2, q=4r^2-1, P=fq,
    A=2S-1, B=4S-5, D=(2P)^(-1)[[A,1],[B,-A]],
    R=O[r,f^-1,q^-1]^dagger[1/p], theta(r)=1+(r-1)^p.

Retain the EXACT old integral source lift, not an arbitrary lift of its
reduction. For the fixed g in O, let n=(p-1)/2, s0=1-2g and

    H_b(x)=g(1+x^n)+(4s0/5)x+(s0/5)x^(n-1),
    w=(8r^p-4r)/f, rho=w e1, b_ext=-w H_b(r^2),
    N=[[D,0,0],[0,0,0],[rho,b_ext,0]].                    (1)

Blocks2,1,1 correspond to(y1,y2,z,V). The source constant s0 differs from sigma.
H_b(1)=1 exactly; sigma(g)=g is not assumed. Old17493/14956 fix this lift;
13743 assumes a selected triangular shape, not an intrinsic global weak flag.

The input theorems used below, with their earlier independent reviews, are:
(i) six-normalform@1c619205: integral rational partial fractions, weak generator
presentations, all four finite normalized period gauges and the good-infinity
gauge, genuinely convergent on their whole open unit disks, with legal weak
Robba restrictions; (ii) properweak@cf379b16: the actual canonical proper
comparison G in GL2(R) satisfying G'=DG-GD_theta; (iii) joint5530, with its
true whole review8615: for a=rho dr,

    [a] != c Phi_theta[a] for every c in K*,
    Phi_theta(b dr)=theta' sigma(b)(theta)G^-1 dr.       (2)

Equation (2) is the earlier specific source-class nonproportionality theorem,
not a new replay of its two-residue/isogeny proof. We use its original proper
normalization. The new question is whether any invertible full matrix can
escape the previously selected shape. The claim to be checked here is

    no F in GL4(R) satisfies F'=NF-FN_theta,
    N_theta=theta' sigma(N)(theta),                    (3)

for THIS fixed connection, ring and lift. This does not deny a geometric
carrier or a different p-adic lift, ring, lattice or functional.

## 2. A local-to-global channel consequence of the old weak estimates

We spell out the needed consequence rather than assume rigid GAGA or infer
weak kernel uniqueness from a cokernel dimension. The four a are1,-1,1/2,-1/2;
their pairwise differences are p-units. Every b in R has a presentation
p^-s sum_(l>=0) p^l b_l, with integral rational b_l of generator degree at most
C(l+1). The old integral partial-fraction lemma writes each b_l as a polynomial
and principal parts at these four points, of degree/pole order at most
C'(l+1), with all coefficients integral. The bounds follow before completion
from monic linear factors with unit pairwise resultants; no DVR structure on
a power-series base is used.

Regroup coefficients at each monomial and pole order. A coefficient of order
j can only occur for l>=j/C'-1. Hence their valuations are at least j/C'-C0.
The sums converge in K and give

    b=P_+(r)+sum_a sum_(j>=1) d_(a,j)(r-a)^(-j),        (4)

where P_+ has radius>1 and v(d_(a,j)) grows linearly in j. The same bounds give
actual weak presentations for these regrouped channels. At a fixed a, the
other channels expand in nonnegative powers of x=r-a on |x|<1: a-b is a unit,
negative-binomial coefficients are integral and the coefficient gain in j
ensures convergence. P_+(a+x) is also analytic there. Thus the negative local
Laurent coefficients of b are exactly d_(a,j), by uniqueness on a common
annulus. In particular if b extends analytically throughout all four disks,
all these coefficients vanish, and b=P_+(r), a power series of radius>1.
This also proves directly that the differential constants of R are K.

At infinity z=1/r the old corrected proper frame has

    e_old=e_good J, J=diag(z,z^-1).

Accordingly a dual horizontal row transforms as h_good=hJ and a period
endomorphism as E_good=J^-1 E J. A power series in r of radius>1 has its Laurent
expansion in z on a nonempty annulus inside |z|<1. Regularity at z=0 therefore
forces the forbidden negative powers of that Laurent series to vanish. This
elementary comparison, together with (4), is all the global analytic input.

## 3. Proper horizontal kernels and the actual endomorphism ring

Write N_a=Res_a(D dr). These are nilpotent. The input gauges satisfy

    H_a'=D H_a-H_a N_a/x, H_a(0)=I,

and H_a,H_a^-1 are analytic throughout |x|<1. For a weak horizontal row
h'+hD=0, set k=hH_a on a common annulus. It obeys xk'=-kN_a. At every Laurent
index j!=0, jI+N_a is invertible over K, so k_j=0. Its constant satisfies
k0N_a=0. Therefore h=k0H_a^-1 extends analytically throughout that disk.
This applies to all four points, including infinite principal parts: the
coefficient equations are equations of convergent annular Laurent series.

At the good point the regular gauge similarly makes h_good analytic at z=0.
Apply (4) to each h entry. They are power series of radius>1, and regularity
of h_good=(z h1(1/z),z^-1 h2(1/z)) forces deg h1<=1 and h2=0. The second
component of h'+hD=0 is then h1/(2P)=0, so h=0. Thus H0 of the proper dual
row connection is zero. Since trD=0, the constant alternating matrix converts
this row equation to y'=Dy; the proper period-column kernel is also zero.
This directly consumes old gauge/partial-fraction inputs, not a separate paper.

Now let E in M2(R) satisfy E'=[D,E]. Locally set C=H_a^-1 E H_a. Then
xC'=[N_a,C]. The operator ad N_a is nilpotent, so jI-ad N_a is invertible for
every j!=0; all nonzero Laurent coefficients vanish. Hence E=H_a C0 H_a^-1
extends across every finite disk. At infinity the regular gauge makes
E_good=J^-1 E J analytic at z=0. Equation (4) then makes each original entry
a power series of radius>1. The four transformed entries are

    E11(1/z), z^-2 E12(1/z), z^2 E21(1/z), E22(1/z).

Their regularity forces E11=a,E22=d constant, E12=0, and E21=u(r) a polynomial
of degree at most2. In E'=[D,E], the11 entry is0=u/(2P) and the12 entry is
0=(d-a)/(2P). Consequently

    End^nabla(proper_R)=K I.                              (5)

## 4. Two intrinsic full flags

The literal baseline in (1) has residue2 at r=1, because Res w=-2 and
H_b(1)=1. An annular derivative has zero residue, so b_ext is not a derivative
of any element of R. This retains the full baseline; it is not deleted by
projecting to the proper source row.

For a horizontal column of N the proper entries vanish by Section3. Then
z is constant, and V'=b_ext z. Nonexactness forces z=0; V is constant. Thus

    H0(N_R)=K e4, W0=R e4.                              (6)

Modulo W0 the connection is proper direct-sum the constant z channel, so its
horizontal columns are exactly K e3. Their preimage generates

    W1=R e3+R e4.                                      (7)

These are intrinsic differential submodules, defined by the module and its
global horizontal sections, not the selected filtration imposed in old13743.
The same holds for N_theta. Its proper block is actually isomorphic to D by
G, while the pulled baseline has residue2p at r=1, still nonzero in K. The
weak substitution exists since theta preserves the inverted factors modulo p.
The coefficient action on g does not change sigma(H_b(1))=1.

Any invertible matrix in (3) maps horizontal columns and their R-spans in
both directions, including after quotient by W0. It must therefore preserve
(6)-(7). It has shape

    F=[[G1,0,0],[q0,a0,0],[u,v,lambda]],

where a0 and lambda are nonzero constants. Its middle-left block obeys
q0'=-q0 D_theta. Multiplying by G^-1 converts it to a horizontal row for D;
Section3 forces q0=0. The remaining proper block satisfies
G1'=DG1-G1D_theta. Hence E=G1G^-1 satisfies E'=[D,E], and (5) gives

    G1=mu G, mu in K*.                                 (8)

Invertibility forces mu!=0. No proper determinant or central grade of F was
assumed to obtain (8); a0,lambda,mu are arbitrary nonzero constants at this
stage. This is precisely the newly justified shape reduction.

## 5. The old source obstruction now tests every such weak matrix

The bottom-left equation of (3), using q0=0, is

    u'+uD_theta=mu rho G-lambda rho_theta,
    rho_theta=theta' sigma(rho)(theta).

Set h=uG^-1. Differentiating the inverse of the actual proper comparison gives

    L_D(h)=mu rho-lambda rho_theta G^-1.                (9)

Thus in the exact old row cokernel,
[rho dr]=(lambda/mu)Phi_theta[rho dr]. The ratio lies in K*, contradicting
the already proved theorem (2), and proving (3) for the fixed object (1).
The contradiction does not use a value of Y, sigma(g)=g, a freely normalized
proper Frobenius, a new beta eigenvalue calculation, or a new isogeny proof.

## 6. Deduplication and limits

Old17493 supplied the extension law;14956 the isolated Kummer/nonexact baseline;
13743 a selected regular formal shape;ba9/joint5530 the selected source-row test.
The normalform supplied weak cokernel/gauges, not End or intrinsic flags.
Old input authors4A56 and7CDA confirm those weak-global arrows were outside their
frozen scopes, without new construction or repair. This is bounded dedup, not
review. Old manuscripts, accepted results and genuine reviews remain unchanged.

The claim concerns this exact p-dependent N, weak ring and theta. It does not
extend to strong completion, formal K[[r-1]], other integral lifts or geometric
carriers. Old local/formal existence is unaffected. The relative realization,
source functional/normalization and target remain open. No general Tool,
Native result, Task admission, budget reset or Goal closure is asserted. This
is one unreviewed whole; the preliminary kernel consequence is not counted
separately. All stopped execution branches remain stopped.
