# R227 — Sharp 38-mode block-symmetric reversible Markov source ideal observer

Date: 2026-11-17 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Native BRC EffectHistogram integration: NOT_EXECUTED.

## Pinned mathematical source and scope

Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Direct dependencies: R215 (Stirling-weight fibres and ideal sizes), R221 (killed-chain survival), R224 (generic 250-state sharpness), R225 (reset 64-state witness), R226 (general source-block orbit realization). This is a precise scalar principal-ideal-cardinality observer on the abstract paired-event monoid J_(m,k,L). The native X6 six-dimensional space, its three-dimensional slice, time and P000 axioms stay fixed. Source/branch/port/sign/multiplicity and exact-weight BRC states remain typed independently.

We prove generic sharpness of R226's 38-state bound for the source partition (3,3) and provide a small strictly positive stationary reversible rational certificate.

## Exact model

The source alphabet is {0,1,...,6}, where 0 is neutral, and two nonneutral groups are G1={1,2,3}, G2={4,5,6}. Use m=12 native signed-direction labels as *abstract event letters* and tail depth L=2. The scalar ideal readout is F_n=T_|S_n| for n>=2, where S_n is the set of observed nonneutral source labels and R215 yields

    W = (144,576,1440,4320,17280,86400,518400),
    T_r=sum_(s=r)^6 binom(6-r,s-r) W_s.

Consider the stationary Markov source transition P. Put, for g,h in {1,2},

    b=(1/40,1/50),      P_(0,j)=b_g for j in group g,
    c=(1/25,1/30),      P_(i,0)=c_g for i in group g,
    e=[[1/80,1/100],
       [1/96,1/90]],   P_(i,j)=e_(g,h) for j!=i, group(i)=g,group(j)=h,
    a=P_(0,0)=173/200,
    d=(181/200,263/288), P_(i,i)=d_g for i in group g.

Every row sums to 1, with strictly positive rational entries. Detailed balance holds for

    pi0=40/187, pi_i=25/187 (i in G1), pi_i=24/187 (i in G2),

since pi0*b_g=pi_g*c_g, and pi_G1*e_12=pi_G2*e_21. Consequently P is reversible. Its diagonal entries a,d1,d2 exceed 1/2. By Gershgorin each eigenvalue lies in a disc centered at a positive real d with radius 1-d<d. Reversibility makes the eigenvalues real, hence P is strictly positive definite in its weighted self-adjoint representation; its principal killed blocks are likewise positive definite.

## Theorem — exact minimal order 38

For the above explicit stationary reversible 7-state Markov source chain, with f_n=E[F_n] for n>=2, the least degree of a homogeneous constant-coefficient linear recurrence for the tail (over Q) is exactly

    d_min = 38.

Proof. For each allowed subset U of the nonneutral labels, the killed source Markov matrix is permutation-invariant within G1 intersect U and G2 intersect U. Fix r1=|U intersect G1| and r2=|U intersect G2|. Its scalar survival vector reduces to neutral plus one coordinate per included group (dimension 1+1_(r1>0)+1_(r2>0)). There are binom(3,r1)binom(3,r2) equivalent U. The complete U={1,...,6} gives survival 1, so its original 3-dimensional block can be replaced by a 1-dimensional constant. Thus the total rational linear realization dimension is

    sum_(r1=0)^3 sum_(r2=0)^3 (1+1_(r1>0)+1_(r2>0))-2
      = 16+12+12-2 = 38.

Let H be the 38x38 Hankel matrix H_(i,j)=f_(2+i+j), i,j=0,...,37. Companion exact Python code reduces this matrix modulo two independent primes, using denominators invertible in the relevant finite fields, and obtains

    p=1,000,000,007: det(H) mod p = 166,715,278 !=0,
    p=1,000,000,009: det(H) mod p = 549,336,287 !=0.

If det(H) were zero over Q, both reductions would vanish. Hence rank_Q(H)=38. Any rational recurrence of degree d induces Hankel rank at most d. The already constructed 38-dimensional realization gives the reverse inequality, so the least degree is exactly 38. QED.

## Generic sharpness in the two-block reversible family

The family of strictly positive stationary reversible block-exchangeable source kernels with two source groups of three includes this explicit rational witness. On any rational parameter chart with nonzero normalizing denominators, the Hankel entries are rational functions of the parameters. The determinant is therefore a rational function that is not identically zero. Its nonvanishing set is nonempty Zariski open and Euclidean dense in the component containing the witness. Therefore 38 is a generic and sharp scalar recurrence degree in this two-block structural family. On collision/degeneracy strata the minimal degree may be lower.

The R223, R225, R226, R227, and R224 exact six-source structural models now provide scalar complexity examples, respectively 7 (fully uniform reset), 64 (nonuniform reset), 12 (reversible fully source-exchangeable nonreset), 38 (reversible (3,3) block exchangeable) and 250 (unrestricted positive stochastic). These are *different hypothesis families*; no total ordering by source symmetry alone is asserted.

## Independent exact computation and reproducibility

The companion standard-library-only file R227_block33_hankel38_certificate.py constructs P explicitly and checks all row sums, pi stationarity through detailed balance, positivity and exact first six f_n via two distinct methods:

1. Direct propagation over reachable states (current source, cumulative six-bit seen mask), where there are 256 possible states.
2. Reduced killed-subchain 3+3 source-count orbit propagation, grouping all 64 subsets by their 16 count-vector orbits.

Six moments match exactly. It computes f_2 through f_76 modulo each prime from the reduced realization, constructs 38x38 Hankel H and evaluates its determinant by modular Gaussian elimination (all inversions over prime fields). This produces the two explicit nonzero determinant residues above, and writes R227_verification.json. All operations are exact integers or fractions; no numerical tolerance or floating-point eigensolver is used.

Exact initial sequence:
    f_1=228907872/187,
    f_2=1130749344/935,
    f_3=2234767473/1870,
    f_4=3614457454417/3060000.

Finite evidence status: six independently checked rational full-state/reduced moments, two full-rank modular Hankel determinant certificates, symbolic group-orbit dimension proof. Independent external review: NOT_REVIEWED. Native BRC integration, Result/Review/Foundation admission and formal Task CLAIM: none.

## Next questions

1. Extend the explicit full-rank certificate to general group-size partitions (k_1,...,k_B) and classify exceptional low-rank strata.
2. Compare arithmetic and rational input/output bit cost across 7/12/38/64/250-dimensional scalar observers and 256 reachable complete seen-mask/current-source states.
3. Design and execute a *read-only* ideal observer on native typed BRC EffectHistogram retaining signed ports, complete provenance, branch identity, positive rational weights, multiplicity and cross-moments. An actual many-to-one native quotient would require a separate future-operation preservation proof.
