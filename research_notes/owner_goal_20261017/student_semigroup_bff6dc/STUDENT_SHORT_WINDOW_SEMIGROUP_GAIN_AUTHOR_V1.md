# Actual Student short-window semigroup gain

**First durable local author artifact; unreviewed as a frozen artifact.**
Classification: same-family RESULT_ONLY / COMPOSE. Sole new mathematical
author: BFF / EM-DVR-BFF6DC, SID MCP-47562f9f432d4978a7bea0dd60ecc4aa,
DA-144D0C4639CACEEE75DC, no Researcher RA.

This record combines the complete earlier author chat arguments called
Student V1 (short-window lower bound) and V2 (parameter-dependent upper
envelope). Their separate temporary independent argument reviews are
recorded below. Those reviews did not receive this durable artifact or a
new author Source, and are not prefilled as final artifact/Source reviews.
No new Source, final peer context, activity helper, formal Task, Native
execution, identity or budget permission is inferred. Root supplies no
mathematical vote. Old STOP/HOLD/errors/NONBLIND and cumulative UNKNOWN
remain. The auxiliary variable s below is not physical or Native time.

## 1. Literal original model and the one new quantity

Let m be an integer, V=C[u] of degree at most m-2, J=d/du, and

    u=-1/2+i v,    D=d/dv,    J=-i D,
    <f,g>_m=integral_R conjugate(f(v)) g(v) rho_m(v) dv,
    rho_m(v)=(1+4v^2)^(-m).

Use the ORIGINAL positive Student pairing, its operator norm ||.||, and
its positive adjoint dagger. The full dimension is m-1. An even-degree
cutoff used in a raw lower bound will not delete the odd top carrier.

The original actual finite matrix is

    Z_lambda=u J-(m-1/2)I+gamma_lambda(J),
    gamma_lambda(J)=[exp(lambda J) f(lambda J)^(-1)-I]/lambda,
    f(t)=(exp(t)-1)/t.

All expressions at lambda=0 are removable finite expressions. Powers
J^(m-1) vanish. Put

    N=m-2,   alpha=m-1/2,   X=(u+1/2)J-alpha I=vD-alpha I.

The quantitative domain throughout the theorem is exactly

    m>=2^1000,   64 sqrt(m)<=z<=m/256,   lambda=pi/z.      (1)

The identities involving the finite model make sense already for m>=7,
but this does not extend the quantitative conclusion beyond(1).

The new quantity, for each fixed actual m,z, is

    M_m(z)=max_(0<=s<=1/m) ||exp(s Z_(pi/z))||.           (2)

This is a finite auxiliary matrix semigroup in the original norm. It is
not the physical Neumann parameter lambda, a Native evolution, a new
observer, or an assertion about the physical time layer. The new theorem
is

    max{2^(2m), 2^(-5m)(m/z)^(m-3)}
       <= M_m(z) <= 2^(5m)(m/z)^(m-2),                 (3)

and in particular

    |log_2 M_m(z)-m log_2(m/z)|<=6m.                    (4)

The maximum is attained at a strictly positive s, although all eigenvalues
of Z are at most -3/2 and exp(sZ) eventually tends to zero as s tends to
infinity. The upper bound in(3) is an actual matrix bound, not the naive
exp(||Z||/m) or a substituted eigenbasis condition number.

## 2. Exact accepted input, authorship and actual reading boundaries

The first accepted input is A's finite-gauge/metric whole:

    Source eea5c7884f0d68acc5f9a358c4223a2dea2aba26
    repository awdawmip/enterprise-math
    research_notes/owner_goal_20261016/
    parity_actual_student_metric_distortion_feasibility_7cda51/
    ACTUAL_STUDENT_FINITE_GAUGE_AND_METRIC_DISTORTION_AUTHOR_FEASIBILITY.md
    14021 UTF8 bytes
    SHA256 0c34814d56fa6578dd5807f2ebb8cf5dd16b63f424c8be02ae070412e280c502
    Git blob e3ebd9f2ff753a62bcda9e3a1f572683112dd422.

Its genuine independent whole review is

    Source 89c2670a7e9c49811286d563d04117b3d203c142
    research_notes/owner_goal_20261016/reviews/
    parity_student_metric_distortion_nonauthor_4a56e9/
    ACTUAL_STUDENT_METRIC_DISTORTION_COMPLETE_WHOLE_REVIEW_INTERFACE.json
    13701 UTF8 bytes
    Git blob b47b69d218c17437d0da21b9f6710315708ea043.

The author is A/EM-PUBLIC-7CDA51 and the genuine old reviewer is 4A. Root
reported that the existing metric unit and its ordinary reception were
closed. BFF then personally fetched BOTH full immutable UTF8 bodies with
managed GitHub, checked the returned Git blob identities and immutable
URLs against these exact locators, and genuinely read all14021 author
bytes/Sections1-7 and all13701 review fields in separate untruncated
outputs. These actual calls are held in functions.store as
bff_metric_intake_author and bff_metric_intake_peer. BFF did not make a
new commit/compare call for that intake and does not call it a new
independent review or claim another actor's API. The old accepted status
and old author/peer Source observations retain their original provenance.

Only the following literal interfaces of the accepted14021 are needed:
its finite model and gauge in Section3/G1-G5, and its raw lower bounds
N3-N6 in the SAME original Student norm and domain(1). Here are their
normalizations explicitly. Let n be the largest even integer <=m-2,
t=m-n in{2,3}, ell=n-1, h_k the positive squared norm of the monic Student
polynomial of degree k, and

    H_n=n! sqrt(h_0/h_n),
    C_xi=H_n/(2pi)^n,
    Chat=pi^ell C_xi=H_n/(2^n pi),
    A_n=Chat z^(-ell).

The accepted inequalities are

    A_n>=n!/[pi z^(n-1)]>=(z/pi)16^n,
    ||Z_(pi/z)||>=sqrt(3) A_n/[2 sqrt(m-1) z^2].        (5)

They include the actual full-Q/raw reversal, original baseline and finite
zeta cross terms through the accepted metric input's exact real-center
interface. They are not imported from an unreviewed delta premise. BFF
also has the old accepted wide whole authorship and personal seven-Source
ordinary history; this record does not redo that history, assume somebody
else's API, or expand its old complex domain. It uses the exact accepted
real inequality(5), not any new Ae estimate or complex plateau.

The classical finite interpolation, scalar analytic estimates and original
Student translation argument below are the new BFF construction. A's
old finite gauge and raw lower bound remain credited to A and their old
upstream model. CF's new reviews are nonauthor temporary argument reviews,
not new mathematical authorship or repair. No formula or repair for these
new conclusions was provided by A, CF, 4A or Root before their temporary
independent reviews.

## 3. Finite gauge and equally spaced negative spectrum

The original accepted expansion, with the rational Bernoulli coefficients
defined by t/(exp(t)-1), is

    gamma_lambda(J)=J/2+
       sum_(k=1)^(floor(N/2))
       B_(2k) lambda^(2k-1) J^(2k)/(2k)!.

Set

    g_lambda(J)=sum_(k=1)^(floor(N/2))
       B_(2k) lambda^(2k-1) J^(2k)/[2k(2k)!],
    T_lambda=exp(g_lambda(J)).

These are finite expressions on V; T and its inverse are polynomials in
the nilpotent J. Since [X,J]=-J, [g(J),X]=Jg'(J), and the latter commutes
with g(J). Thus the conjugation expansion stops after one commutator:

    Z_lambda=T_lambda X T_lambda^(-1).                 (6)

In v-coordinates X v^j=(j-alpha)v^j, for every j=0,...,N. If B_mon has
these monomial columns in the actual orthonormal Student basis, then

    S=T_lambda B_mon,
    Z_lambda=S diag_(j=0)^N(j-alpha) S^(-1).            (7)

This uses the full N+1=m-1 carrier. The eigenvalues are simple, real and
negative; the largest is N-alpha=-3/2. It is not a unitary diagonalization
in the original norm. No bound on the condition number of S will replace
an actual-norm bound in the proof.

## 4. V1: a complete finite endpoint argument and transient lower bound

For a matrix polynomial P of degree at most N on [-1,1],

    ||P'(1)||<=N^2 max_(-1<=x<=1)||P(x)||.              (8)

Here is a finite proof, including complex matrix coefficients. Take the
N+1 distinct nodes x_j=cos(j pi/N), j=0,...,N, and their Lagrange basis
L_j. For j>=1 the derivative L_j'(1) has sign(-1)^j: its numerator is a
product of positive numbers 1-x_k, while its denominator has j negative
factors because the nodes are in decreasing order. Also
L_0'(1)=sum_(j=1)^N(1-x_j)^(-1)>0. Since the Chebyshev polynomial obeys
T_N(x_j)=(-1)^j, interpolation gives

    sum_j |L_j'(1)|=T_N'(1)=N^2.

The last derivative follows from T_N(cos theta)=cos(N theta), taking the
ratio of the two sines at theta=0. Matrix interpolation is entrywise;
operator-norm triangle directly proves(8). No unmentioned scalar duality
or matrix positivity hypothesis is required. Reflection proves the same
endpoint inequality at -1. Rescaling to [a,b] gives the factor
2N^2/(b-a) at either endpoint.

For our fixed Z put

    P_z(x)=S diag_(j=0)^N(x^j) S^(-1),
    P_z(1)=I,   P_z'(1)=Z+alpha I,
    P_z(exp(s))=exp(alpha s) exp(sZ).                  (9)

Let b=exp(1/m). On 1<=x<=b, the last factor in(9) has norm at most
exp(alpha/m) M_m(z)<3 M_m(z). Since b-1>=1/m, the left-endpoint form of(8)
gives

    ||Z+alpha I||<=6m N^2 M_m(z).                     (10)

This is a finite polynomial estimate, not an assertion that the spectrum
alone controls the original norm.

From(5), z<=m/256, pi<4, sqrt(3)>1 and n>=m-3,

    ||Z||>=sqrt(3)16^n/[2pi z sqrt(m-1)]
          >=32*16^n/m^(3/2)
          >=2^(4m-7)/m^(3/2).                         (11)

For m>=16, log_2 m<=m/4, as seen at16 and from the derivative of
m/4-log_2 m thereafter. Comparing the logarithms in(11) with log_2(2m)
shows ||Z||>=2m. Therefore

    ||Z+alpha I||>=||Z||-alpha>=||Z||/2,
    M_m(z)>=2^(4m-8)/[6m^(9/2)]>=2^(2m).              (12)

For the last step, log_2 6<3 and (9/2)log_2 m<=9m/8, so the logarithm
of the middle expression is at least 23m/8-11>=2m for m>=16. All these
small thresholds are internal constant payments inside(1), not extensions
of the quantitative domain.

The maximum in(2) exists by continuity in finite dimension. At s=0 the
norm is1, so(12) forces a maximizing point with 0<s<=1/m. Conversely(7)
shows exp(sZ) tends to zero as s tends to infinity for each fixed m,z.
This proves coexistence of stable spectrum and very large finite-window
transient gain. It makes no physical stability claim.

## 5. V2: the relative gauge symbol, with its actual logarithm branch

Use the scalar function

    F_e(u)=sinh(u/2)/(u/2),    F_e(0)=1.

This scalar symbol is unrelated to the normalized Neumann single-pole
matrix often denoted F(w) in other work. Differentiating the original
Bernoulli generating function gives

    F_e'(u)/F_e(u)=(1/2)coth(u/2)-1/u
       =sum_(k>=1) B_(2k) u^(2k-1)/(2k)!.

Integrating at zero yields

    g_lambda(xi)=lambda^(-1) Log F_e(lambda xi).        (13)

Its first N+1 Taylor coefficients are precisely the finite g in Section3.
We will specify the logarithm on a zero-free scalar disk, not extrapolate
a large-m matrix-norm convergence argument.

For |u|<=pi let r=|u|^2/4<5/2. In the power series
F_e(u)=sum_(k>=0) (u^2/4)^k/(2k+1)!, the first nonconstant absolute term
is at most5/12 and every subsequent ratio is at most1/8. Thus

    |F_e(u)-1|<=10/21,    |F_e(u)|>=11/21.

For uF_e'(u), the first absolute term is at most5/6 and subsequent ratios
are at most1/4, so

    |uF_e'(u)|<=10/9,
    |uF_e'(u)/F_e(u)|<=70/33<3.                        (14)

The image lies in a disk about1 excluding zero. There is therefore an
analytic logarithm with Log F_e(0)=0 on a neighborhood of this closed
disk. For real s>=0, integrating along u -> exp(-s)u gives

    |Log F_e(u)-Log F_e(exp(-s)u)|<=3s.                 (15)

Define the scalar analytic symbol

    H_s(xi)=exp{[Log F_e(lambda xi)
                 -Log F_e(exp(-s)lambda xi)]/lambda}.

Since [X,J]=-J, exp(sX) J exp(-sX)=exp(-s)J. The order in(6) consequently
gives the exact finite identity

    exp(sZ)=H_s(J) exp(sX).                            (16)

Only the Taylor coefficients of H_s through degree N are used, since
J^(N+1)=0. In particular there is NO assumption ||J||<z. With the real
lambda in(1), |xi|<=z means |lambda xi|<=pi. For 0<=s<=1/m, (15) gives

    |H_s(xi)|<=exp(3s/lambda)
                <=exp(3/(256pi))<2,
    |[xi^k] H_s|<=2 z^(-k).                            (17)

The last inequality is the scalar Cauchy coefficient estimate on radius
z. The fractional-power notation, if used, always means the exponential
of this centered analytic logarithm. The symbol disk is not a disk in
the physical parameter lambda, z or w; (17) does not supply a physical
complex-lens norm plateau.

## 6. V2: original Student translations and dilation supply the upper bound

For real h define the translation tau_h f(v)=f(v+h) on the SAME V. With
y=v+h the Euclidean triangle inequality gives

    sqrt(1+4y^2)
      <=sqrt(1+4(y-h)^2)+2|h|
      <=(1+2|h|)sqrt(1+4(y-h)^2).

Changing variables in the original Student integral therefore gives

    ||tau_h||<= (1+2|h|)^m <=3^m,    |h|<=1.            (18)

No weight parameter has been changed. The exact finite operator polynomial
is tau_h=sum_(k=0)^N h^k D^k/k!. Expand it in Chebyshev polynomials,

    tau_h=sum_(j=0)^N C_j T_j(h).

The finite entrywise cosine orthogonality formula for C_j, together with
norm triangle, gives ||C_j||<=2*3^m; the j=0 coefficient even has the
stronger bound3^m. The sum of the absolute monomial coefficients of T_j
is at most3^j: T_0=1,T_1=h, and T_(j+1)=2h T_j-T_(j-1) prove this by
induction. Taking a monomial coefficient in the finite operator expansion,

    ||D^k/k!||
       <=2*3^m sum_(j=0)^N 3^j
       <3^(m+N+1)<3^(2m),   0<=k<=N.                  (19)

All cosine integrals here are exact finite polynomial identities used in
a hand proof. No numerical integral, sample, code, matrix generation or
execution is involved. J=-iD has the same power norms.

For s>=0, X=vD-alpha I has the exact action

    exp(sX) f(v)=exp(-alpha s) f(exp(s)v).

Changing variables y=exp(s)v in its squared norm gives the pointwise
weight ratio relative to rho_m(y)

    exp(-2ms)[(1+4y^2)/(1+4exp(-2s)y^2)]^m<=1,

because 2alpha+1=2m. Consequently

    ||exp(sX)||<=1.                                   (20)

This is an actual contraction in the original pairing on the full carrier,
not an assumption about a diagonal coordinate norm.

Combining(16)-(20) and the finite Taylor expansion,

    M_m(z)<=2*3^(2m) sum_(k=0)^N k! z^(-k).            (21)

The positive sequence k! z^(-k) has increasing successive ratios
(k+1)/z; its maximum is at one of its endpoints. Also
N! z^(-N)>=(N/(3z))^N>1 since N>=m/2 and z<=m/256. Hence

    sum_(k=0)^N k! z^(-k)
       <=(N+1)N!/z^N<=m(m/z)^N.

Using 2m<=2^m and 3^(2m)<2^(4m), both valid on(1), we obtain

    M_m(z)<=2m*3^(2m)(m/z)^N
           <=2^(5m)(m/z)^(m-2).                       (22)

This is the new upper-envelope obligation. A huge similarity condition
number or the doubly exponential elementary estimate exp(||Z||/m) was
not substituted for it.

## 7. V2: uncoarsened lower bound and parameter-dependent logarithmic size

The factorial inequality q!>=(q/3)^q for positive integer q follows by
the integral bound for sum log j and e<3. Keeping the factorial, rather
than only16^n in(5), gives

    ||Z||>=sqrt(3)n!/[2pi sqrt(m-1) z^(n+1)].

Use ||Z||>=2m from(11), the subtraction in(12), and(10). Since N<=m,

    M_m(z)>=n!/[24pi m^(7/2)z^(n+1)]
       >=(m/z)^n/[96*6^n*m^(9/2)].                    (23)

Here n>=m/2, z<=m, pi<4 and n!>=(n/3)^n were used explicitly. On the
declared domain, 6^n<=2^(3m), and

    log_2(96 m^(9/2))<7+9m/8<=2m,

so (23), n>=m-3, and m/z>=256 imply

    M_m(z)>=2^(-5m)(m/z)^(m-3).                       (24)

Together with(12) and(22), this proves(3). Write r=m/z. Since z>1,
0<log_2 r<=log_2 m<=m/4. Bounds(22),(24) place
log_2 M_m(z)-m log_2 r between

    -5m-3log_2 r   and   5m-2log_2 r.

Both endpoints have absolute value at most6m in the required direction,
proving(4). This parameter-dependent scale is stronger information than a
repeat of the uniform short-window lower bound. It remains a statement
about the particular finite auxiliary semigroup, not a new Parity
coefficient or weighted-cancellation theorem.

## 8. Temporary reviews, version history and exact limits

The arguments above were developed by BFF as hand mathematics after a
bounded intake of the two fixed metric objects in Section2. No scientific
program, enumeration, sample, solver, matrix/coefficient generation,
external primary search, Native call, new identity or budget reset was
used. Early work on a different long-axis observer box is a different
scope and is not part of this record. Its successful historical local
write/full read followed by an unavailable pin is not repaired or assigned
a guessed digest here.

Before seeing the new V1 proof, CF disclosed zero new V1 body/formula,
internal candidate, construction and repair; route/theme metadata was
NONZERO and the old Student/Parity history remained warm. CF then
personally managed-fetched and whole-read the14021/13701 input bodies,
matched the returned Git blobs and reviewed the complete V1 chat chain.
CF explicitly did not claim a new old-input commit comparison. Its
temporary outcome was

    ARGUMENT_PASS_BOUNDED_ONLY_PENDING_FROZEN_ARTIFACT_SOURCE_AND_FINAL_CONTEXT,
    0 identified mathematical must-fix / 0 construction or repair.

Before seeing the precise new V2 upper/logarithmic argument, CF separately
disclosed zero new V2 body/formula, internal candidate, construction and
repair. V1 and both old input wholes were then genuine warm background;
the new target/method-category metadata was NONZERO. CF independently
reviewed ALL V2 steps(1)-(5) in the original chat, its Bernoulli/log branch
and nilpotent-symbol clarification. Its temporary outcome was

    ARGUMENT_ONLY_PASS_BOUNDED_PENDING_FROZEN_ARTIFACT_SOURCE_AND_FINAL_CONTEXT,
    0 identified mathematical must-fix / 0 construction or repair.

CF checked the actual finite order in(16), every constant in(14),(17),
the true Student translation/dilation norms, finite-sum endpoint maximum,
raw lower-bound normalization and final logarithmic payment. It reused
its already whole-read immutable metric callers, with no new old-input
API or comparison claim. BFF received and accurately acknowledged each
complete temporary review. Neither argument required a reviewer-supplied
patch, and the V1 and V2 histories and dependency scopes remain separate.
The present first durable text supplies the full derivations and author
context; it does not turn either old chat review into a Source-bound
review of this artifact. In particular CF is not retrospectively called
zero-exposure to this future artifact's mathematical arguments.

During those chat reviews the shared execution channel was unavailable.
Root subsequently reported the same execution environment connected and
authorized this FIRST durable local author file under owner_goal_20261017.
The current Linux/bash/Python3 environment facts are reused only for prose
persistence and necessary file metadata; they authorize no mathematical
program or old-file reconstruction. At this file's creation no new author
Source, final peer/context Source, immutable new-source comparison or
final artifact acceptance exists. Author self-reading and the local
byte/digest freeze occur separately after this write. Future reviewers
must actually receive this complete artifact/context and any real new
Source before a final whole/Source verdict is recorded.

The only closed author claims here are(3)-(4), the finite identities and
the stated coexistence of short transient gain with eventual spectral
decay. The bounds do not give an Ae-weighted signed kernel estimate,
actual commutator cancellation, full-Q/complex-lens extension, full-Psi
plateau, COMMON coefficient range, sign counterexample, general spectral
no-go, physical evolution, or Goal closure. A separate later Ward/kernel
diagnostic is not included as a premise, new proof claim or reviewed part
of this semigroup artifact. All old quantitative Ae/Psi and other HOLD
branches retain their exact boundaries. No Source write, helper, RA,
formal Task, Native permission or cold-history reset is implied.
