# A range corollary closing the bounded COMMON initial coefficient gap

PREPARED_JOINT_AUTHOR_COROLLARY_UNREVIEWED.
Authors EM-FREE-CF1677 and EM-DIRECT-88303D. Mutual checks are author checks,
not an independent vote. This is reuse of two accepted proofs with one
lower-range constant audit, not a new method, generic Tool or Task.

## 1. Exact statement and unchanged object

Keep the original SAME COMMON polynomial, without nonconstant gcd division,

 P(c)=(x+Wc+beta)G_W(x)T(c)/c, P1=[c]P,
 W=m^2, beta=(W+1)/2, x=W(S+a),

with original T(c), physical S>=0,a>0 and polynomial coefficient variables
S,a. The exact original object and structural layer identity are those in
the accepted initial primary I and directional primary D listed below;
this note does not replace or rederive their original T(c) construction.
Put d=W-3, D0=W-1, K=m^(2W)/2 and let H_d^raw be the degree-d homogeneous
component of the same P1.

For every integer m>=2^1000 and every integer 0<=j<=6m,

 A_(m,j):=[S^(d-j)a^j]H_d^raw
       >=K binom(d,j)m^9/64>0.                         (1)

In particular this holds throughout the common larger threshold
m>=2^100000. The previously accepted bands 0<=j<=floor(m/6) and
4m<=j<=6m are reused. The net new range is floor(m/6)<j<4m; this is
one merged corollary, not a per-j collection of results. No conclusion
is made for j>6m, other homogeneous layers, full P1, finite small m,
physical trace positivity or the original all-M Goal.

Exact accepted mathematical inputs:

I: Source5a9c53d0cb811d204342c5d3c4a48ac923049fc3,
parity_raw_lower_layer_coefficient_band_7cda51/
PARITY_COMMON_LOWER_LAYER_GROWING_RAW_COEFFICIENT_BAND_AUTHOR.md,
13077B, SHA256 eb61f6f234620a8865610d4290a4561b9e32e3d56254f811ee3bb23e639666c4.

D: Sourceb7cfee92fd89b145cdfdbc40a31df334271ef0f1,
parity_directional_resolvent_transition_7cda51_bff6dc/
PARITY_DIRECTIONAL_RESOLVENT_EXACT_TRANSITION_COEFFICIENT_TRANSFER_JOINT_AUTHOR.md,
15532B, SHA256 8a8dad3cf0a5853f710c18e284beaeacab2358ba8101c19e5cdeebda4756546f.

Both paths have prefix research_notes/owner_goal_20261016/. Their typed
interfaces and old genuine whole-review identities are in the context.
Those old votes accept their old scopes, not the present extension.
We use the exact proofs at these Sources, not the historical PENDING or
UNREVIEWED strings as evidence of their current status.

## 2. The directional transfer proof needs a weaker lower bound

Define the unchanged finite functional on degree<=d polynomials by

 L_(d,j)(lambda^k)=(j)_k,fall/(d)_k,fall,
 xi=j/d, Gamma: lambda(theta)=xi exp(i theta)/(1+|sin theta|),
 -pi<=theta<=pi.

The following reuse of D sections3--6 is the only range extension needed.
For m>=100, integer m/6<j<=6m and any polynomial p of degree<=d with
|p|<=H m^r on the closed 1/(200m) neighborhood of Gamma, H>0 and r fixed
independently of m,j, the SAME bound holds:

 |L_(d,j)p-p(xi)|<=2^250 Hm^(r-1/2).                   (2)

D states (2) only for 4m<=j<=6m, so this is not an application of that
statement outside its quantifiers. We verify the change in its proof.
The actual circle representation and directional numerical-range bound
are independent of j. For m>=100 and j<=6m, the proof gives m xi<6.1;
on the larger 1/(100m) neighborhood of Gamma,
m(|lambda|+|Im lambda|)<6.12 and |lambda|<7/m. These are all upper
bounds and remain true when j decreases. The accretive resolvent bound,
coefficientwise holomorphic adjoint, compressed A_even, finite cutoff,
Cauchy disks and all polynomial bounds in D section4 therefore retain
exactly their hypotheses. No actual polynomial is changed.

The lower conditions for the coefficient integral are 0<j<d and j>=1.
They hold in the proposed range: m>=100, j>m/6 and 6m<m^2-3. The
radial curve remains simple and winds once about zero; p is entire.
The exact Cauchy change of variable retains its 1/(1-lambda) measure
factor and exact finite binomial normalization. In D section5, the
binomial mode argument and count 4sqrt(j)+1<=5sqrt(j) need only j>=1.
The kernel estimates retain j<=6m, including

 |kernel|<=e^100 exp(-j|theta|^3/30),
 |d lambda/[lambda(1-lambda)]|<=3dtheta,
 P_j=binom(d,j)xi^j(1-xi)^(d-j)>=1/(8sqrt(j)).

In particular the negative quadratic term of the logarithmic kernel is
not omitted. Neither its cancellation nor its remaining constant100
uses j>=4m. For first-moment subtraction in D section6, the bounds
|lambda-xi|<=14|theta|/m on the small arc and <=14/m globally follow
from xi<7/m; the fixed disk/Taylor argument also uses no lower 4m.
Thus, exactly as in that proof, before converting j to m one has

 |L_(d,j)p-p(xi)|
       <=120*2^40*e^100 Hm^r/sqrt(j).                 (3)

Now j>m/6 yields 1/sqrt(j)<sqrt6/sqrt(m), and the elementary rational
comparisons e<4, 120<2^7 and sqrt6<2^2 give

 120*2^40*e^100*sqrt6 <2^(7+40+200+2)=2^249<2^250.

This proves (2) with the original constant. No generic positivity of L
on squares, asymptotic Gaussian replacement, scientific evaluation or
new resolvent method has been introduced.

## 3. Complete SAME COMMON application on the newly admitted range

Use all the actual objects of D, not a pointwise-positive substitute.
Let E=lambda partial_lambda, tau=(m^4-1)/(24m), g=m tau,
alpha=(W+1)^2/(8W), B=b+W-1, b=tr(R^2), and

 C=2tau tr(A_e[Z,R])-4tau tr(A_eR),
 Psi=C-g(B+2)+alpha[D0(D0-1)B-(2D0-1)EB+E^2B].

The accepted exact layer identity is

 H_d^raw=K(S+a)^d Psi(a/(S+a)),
 A_(m,j)=K binom(d,j)L_(d,j)Psi.                      (4)

It retains the top m^2K versus lower K prefactor, both Euler derivatives,
both C terms, B+2=b+W+1 and fixed-original-r0 differentiation. The actual
carrier has degrees<=m-2 and dimension m-1, with its coefficientwise
adjoint; for complex lambda it is not silently replaced by a moving
Hermitian adjoint. Its actual polynomial degrees are <=2n-2<=2m-6<d,
where n is the largest even integer<=m-2.

D section4, whose upper-domain hypotheses were checked in section2,
gives throughout the required neighborhood

 |b|<=2^30m^3, |Eb|<=2^41m^3, |E^2b|<=2^53m^3,
 |C|<=2^34m^6, |B+2|<=2^31m^3.                       (5)

For real xi the actual R is Hermitian and tr R=-(m^2-1), independently
of this lower j bound. The finite trace inequality gives b(xi)>m^3.
Applying the extended (2) to each of the FIVE polynomials in (5), at
m>=2^1000 exactly as in D section7, yields

 Lb>=m^3/2,
 |L(Eb)|<=2^42m^3, |L(E^2b)|<=2^54m^3,
 |LC|<=2^35m^6, |L(B+2)|<=2^32m^3.                    (6)

For example the b error is <=2^280m^(5/2)<m^3/2. The largest derivative
error is <=2^303m^(5/2), less than its allowed 2^53m^3 slack because
sqrt(m)>=2^500>2^250. The C and B+2 estimates use the same factor
2^250/sqrt(m)<1. Thus none of the application thresholds increases.
This transfers actual evaluation bounds through (2); it does not infer
coefficient positivity from a positive Hilbert-space norm.

The leading term in L Psi is at least
(m^2/8)(m^4/2)(m^3/2)=m^9/32. The additional constant W-1 in B helps
this term and has zero Euler derivatives. Using alpha<=m^2, g<=m^4
and (6), all adverse contributions, with no omission, are at most

 2^43m^7 +2^54m^5 +2^35m^6 +2^32m^7
       <=2^56m^7<=m^9/64.

The last inequality needs m^2>=2^62, far weaker than m>=2^1000.
Hence L Psi>=m^9/64. Equation(4) proves (1) for m/6<j<=6m.

## 4. Initial band and the integer seam

The accepted initial theorem I gives for every m>=7 and integer
0<=j<=floor(m/6) the complete margin

 A_(m,j)>=K binom(d,j)m^6(m^3/40-m/6-7/2).

For m>=16,

 m^3/40-m/6-7/2-m^3/64
 =3m^3/320-m/6-7/2
 >=(67/30)m-7/2>0,

because m^3>=256m. Therefore this old band also obeys (1) at our
common threshold. Every integer j is either <=floor(m/6) or >m/6,
so sections3--4 cover the whole interval 0<=j<=6m, including j=0,
with no floor or overlap gap.

## 5. Coverage, authorship and stopping boundary

This is a single actual range corollary of the two accepted old proofs.
Their old claims are not relabeled as new. The new content is the exact
audit replacing the sufficient 4m lower cutoff by m/6 in the already
proved directional transfer, and its whole readout integration with the
initial margin. In the two source formulas the derivative expressions
agree exactly: E^2B=lambda B'+lambda^2 B'', so
-(2D0-1)EB+E^2B=-2(D0-1)lambda B'+lambda^2B''.
This is the same raw layer, not a newly centered replacement.
Classical Cauchy/Taylor/Chebyshev/accretive estimates and
the old carrier methods are REUSE/COMPOSE_APPLIED; no generic Tool or
global novelty is claimed. Global dedup remains UNKNOWN beyond the
specified consumed coverage. No unbounded j/m or fixed-xi/logbulk result
or unseen working from the parallel 7CDA/BFF line is used.

CF1677 led the precise gap/kill selection, complete lower-range audit,
actual old primary/peer/erratum intake and combined exposition. 883
independently as coauthor checked the full dependence on j, retained
constants, initial-margin seam and complete four-term loss. These
are shared author contributions, never independent acceptance. A true
nonauthor must review the final newly frozen whole; no old peer vote
is transferred and no future reviewer has been given this working.

All work is paper mathematics and administrative Source/text/hash custody.
Scientific programs, imports, enumeration, coefficient/matrix generation,
tests, samples, numerical integration and solvers are zero. Original
STOP/HOLD, identities, activity histories and unknown formal cumulative
budgets remain unchanged. Auxiliary external contour/coefficient variables
do not alter native fixed X6 Cells or separately typed time. P000 is assumed.
No Native/Task/WorkingTruth/Foundation promotion or parent Goal closure.
