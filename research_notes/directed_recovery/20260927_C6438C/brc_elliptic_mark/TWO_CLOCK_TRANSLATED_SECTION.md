# A translated section joins two return clocks without squaring depth

Status: PURE_SYMBOLIC_CANDIDATE / SHARED_CONTEXT / NOT_ADMITTED. This is a new proof unit, not another run. It uses the frozen translated Kummer and translated trace contracts; no scientific module is imported and no numerical reference is used. The parent objective remains native BRC order/factor discovery.

## Elliptic statement

Let R=Z/NZ, N odd, and let E be the smooth curve B y^2=x^3+A x^2+x, with B(A^2-4) a unit. Fix an actual affine point P=(a,b) with b a unit. In particular, P is not a two-torsion point in any residue field. Suppose primitive Kummer pairs (X0:Z0), (X1:Z1) coherently represent Q and Q+P. Set W=X1-a Z1.

For an actual point T, write d(T) for the common gcd of N and the X,Z coordinates of a primitive ordinary plane-projective representative of T. This is the pullback of the identity ideal, including its truncated prime-power depth; it is independent of multiplying the representative by a unit.

Then

    gcd(N,W) = d(Q) d(Q+2P),
    gcd(d(Q),d(Q+2P)) = 1,
    gcd(N,Z0,W) = d(Q).

Consequently, after the two actual gcds are evaluated, the exact positive integer quotient

    gcd(N,W) / gcd(N,Z0,W)

is d(Q+2P). The quotient must be computed and certified by native exact division when used as an algorithm. It is not modular inversion, and this note has not executed that additional readout.

For Q=EP, one adjacent Kummer pair therefore exposes returns at E and E+2. It does not require propagating (E+2)P just to derive its return divisor through this identity.

## Proof with every local branch accounted for

Fix p^e dividing N. The map x:E to the projective line identifies T with -T. Since b is a unit, the fiber x(T)=a has two distinct smooth points P and -P modulo p, and x-a has a simple zero at each. Indeed the derivative of B y^2-f(x) with respect to y is 2Bb, a unit at either point; x-a is a local parameter there.

For T=Q+P, W vanishes modulo p precisely when Q is O or -2P modulo p. At such a point the denominator Z1 is a unit, so its use in the homogeneous expression adds no valuation. If T is O modulo p, X1 is a unit and W is a unit instead: the pole is not an extra zero. If T is any other point, W is also a unit.

Near Q=O the frozen translated-mark theorem proves that x(Q+P)-a is a local identity parameter times a unit. Near Q=-2P, put S=Q+2P. Then x(Q+P)=x(S-P); applying the same translated-mark theorem with the fixed point -P=(a,-b) gives the identity parameter of S times a unit. These arguments preserve every truncated valuation over Z/p^eZ, not merely zero sets over the field.

The two neighborhoods are disjoint modulo p: overlap would imply 2P=O, impossible because b is a unit in odd characteristic. Thus at each prime at most one of d(Q), d(Q+2P) is nonunit. The local valuations of W equal that one return depth. Multiplication of the coprime local divisors proves the first two identities over N. The third is exactly the frozen translated Kummer theorem.

This proof requires genuine coherent points and primitive projective pairs. It does not authorize an arbitrary pair of residues as a trajectory or allow cancellation of an unchecked nonunit.

## Regular companion/HBW version

Let M=[[0,1],[-1,k]], Delta=k^2-4 a unit, and V_n=tr(M^n). For epsilon in {+1,-1}, let d_n^epsilon be the common gcd of N and all entries of M^n-epsilon I. It equals the cyclic marked-vector return divisor under the frozen companion contract. Set

    w_epsilon = V_(E+1)-epsilon k.

Then

    gcd(N,w_epsilon) = d_E^epsilon d_(E+2)^epsilon,
    gcd(d_E^epsilon,d_(E+2)^epsilon) = 1.

One proof uses the finite etale quadratic algebra S=R[lambda]/(lambda^2-k lambda+1). Lambda and lambda-lambda^-1 are units; the latter squares to Delta. M is diagonalizable over S with unit determinant change of basis. The exact identity is

    w_epsilon = (lambda^E-epsilon)(lambda^(E+2)-epsilon) / lambda^(E+1).

There is no division by a nonunit here. The two factors cannot both vanish in a residue component, because that would force lambda^2=1 while lambda-lambda^-1 is a unit. Their companion conjugates have the same vanishing order, since lambda^-n-epsilon is a unit multiple of lambda^n-epsilon. Therefore their truncated valuations give precisely the two signed primitive-return ideals. The same argument works in split components and in the unramified quadratic component; faithful etale extension preserves these base-ring p-adic valuations. This proves the identities.

The already proved joint observer

    gcd(N,V_E-2epsilon,w_epsilon) = d_E^epsilon

selects one branch; native exact division selects the other. A short adjacent-trace recurrence can therefore carry two signed clocks without a full matrix. Its actual bit-operation bill remains to be measured by a new frozen native experiment.

## Consequences for the research direction

The useful object is the translated geometric section, together with its marked branch, rather than an expanded history distribution. The section combines two return events while retaining unsquared local depth. This is compatible with the HBW program of keeping a small coherent state and exposing a chosen section of its orbit. For a genuine HBW implementation, the complete move-to-register observer certificate remains required; the elliptic typed program is not by itself an admitted nonlinear X6 move.

For factor extraction, a proper gcd(N,W) is already useful. When W is saturated because different CRT components lie on the two different branches, the marked common gcd can still separate them. If all components stay outside both branches, the result is 1. If they all return on the same branch, separation may still fail. Thus two clocks do not provide a factor-blind success probability or a generic efficient exponent selector.

This is not a claim that elliptic x-coordinate collision tests are new: they are established in ECM stage-two methods. The contribution of this unit is the explicit primitive-depth product identity, its signed companion analogue, and its exact native readout contract in this project. The author-hosted GMP-ECM stage2 source explicitly implements common continuation for ECM, p-1 and p+1 using polynomial arithmetic: https://members.loria.fr/PZimmermann/ecmnet/cov/ecm/stage2.c.gcov.html . The page was retrieved in this research unit; the source is prior-art context, not evidence of our native costs or success rate.

No new algorithm execution or admission is claimed. The next useful test would target a predeclared second-branch hit, with a full native return comparison and all readout costs; parameter selection and larger-input success are separate open obligations.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1
