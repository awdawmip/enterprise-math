# C26 target K: projective inverse bounds and the nonuniform-control boundary

REUSE_STANDARD_COMPOSE / FIRST PERSISTED WORKING INTERFACE LEDGER.
Sole author of this explicit applied hand derivation: EM-DVR-BFF6DC.
This preserves an earlier private C26 conditioning route, not a new paper,
generic Tool, principal theorem, priority claim or independent review vote.
First persistence 2026-10-17 11:45:04 UTC.
The complete quantity argument previously had no accurately held frozen
local/Source proof locator; the present full chat/store argument is preserved
here. That is a personal locator boundary, not a full-library absence.
No independent Source-bound acceptance is inferred from this author ledger.
Root supplied preservation/routing requirements and zero mathematics.

## 1. Actual input and the unchanged conditional model

The necessary literal model is the already personally whole-read C26
schedule interface:
Source c1c633fec98a2e5ce02e93972045551ec662b33f,
research_notes/owner_goal_20261017/c26_returned_control_schedule_criterion_4a56e9/
C26_ARBITRARY_RETURNED_CONTROL_SCHEDULE_DRIFT_ALIAS_IFF_AUTHOR_COMPOSE_APPENDIX_V1.md,
17238 UTF8B; SHA256
e9936a2f886d866339364acc5526b3d6945539e199142755112983bfa7fb6427;
Git blob e292a9a04f0fa5aaab051dca325cb7d794f219a4.
BFF's prior genuine whole and own Source custody are honestly reused.
No new old GET/compare/whole, C22/C24 result or borrowed actor API is claimed.

Keep finite nonempty labelled Y with basepoint y0, known real square T
whose entries are all strictly positive, d>=0, distinct known NONNEGATIVE
integer positions n_j, binary labels b_j, and
 V_jk=binom(n_j,k), k=0,...,d.
Assume the GOOD schedule b is outside col_R V.
An actual complete normalized positive table has the same original form
 R_j(y)=Q(y)K(y)r_K(y)^b_j product_(k=1)^d D_k(y)^V_jk / Z_j,
 r_K(y)=(TK)(y)/K(y),                                      (1)
where K>0 has uniform mean1 and belongs to the actual admissible family F,
Q>0 with sum Q=1, D_k>0 with D_k(y0)=1, and every Z_j is the actual positive
finite row sum. All those Q,D,Z may differ between the two models below.
There is no restriction on their amplitudes beyond the original model.

For positive vectors write
 d_H(f,g)=osc_y log(f(y)/g(y)).
For two complete positive tables define
 d_obs(R,S)=max_j d_H(R_j,S_j).                            (2)
These are exact deterministic projective discrepancies. Signed contrasts
below are mathematical functionals, not native controls or probabilities.

The upper bound applies to ANY two actual endpoints in the SAME original F.
It does not replace restricted F by all positive targets, assume that F
contains a path between endpoints, or solve an existence/member test.
The counterexample in section5 explicitly chooses F_all, the unrestricted
positive mean-one family; it is not a counterexample in every restricted F.

## 2. Exact observable contrast, with every nuisance retained

Because b is outside col V, finite real linear algebra gives a row vector w
with
 w^T V=0, w^T b=1.                                        (3)
For example, extend a basis of col V by b and prescribe the linear functional
to be zero on the former and one on the latter. The resulting real w can
be fixed once the known schedule is fixed. Nothing is solved numerically.
The constant column V_j0=1 implies sum_j w_j=0.

Taking the logarithm of the ACTUAL equation(1) and summing with w gives
 sum_j w_j log R_j(y)=log r_K(y)-sum_j w_j log Z_j.         (4)
Indeed the full log Q+log K term is multiplied by sum w=0, and every
log D_k term is multiplied by sum w_j V_jk=0. The final Z term is a
state-independent constant, not an omitted normalization.

For two actual models R^(1),R^(2), with targets K1,K2 and arbitrary allowed
nuisances, subtract(4) and take oscillation. The exact triangle inequality is
 d_H(r_K1,r_K2)
 <= sum_j |w_j| d_H(R_j^(1),R_j^(2))
 <= ||w||_1 d_obs(R^(1),R^(2)).                           (5)
This is the first precise arrow. It uses full labelled rows and the same
original schedule, not an artificial positive mixture or an already fitted
table image. It does not require the new best-fit theorem.

## 3. A self-contained quantitative positive-T inverse

Let
 t_minus=min_(i,y) T_iy, t_plus=max_(i,y) T_iy,
 c=(t_minus/t_plus)^2.                                    (6)
Then 0<c<=1. These are parameters of the actual known finite T.
We prove for arbitrary positive endpoint vectors K1,K2 that
 d_H(TK1,TK2)<=(1-c)d_H(K1,K2).                            (7)

Put u(y)=log(K1(y)/K2(y)), and introduce the AUXILIARY positive vector
 K_theta(y)=K2(y) exp(theta u(y)), 0<=theta<=1.
This auxiliary calculus vector need not have uniform mean1 or belong to F.
It is not proposed as an actual target, observed experiment or new datum.
The following inequality is a fact on the positive cone and will only
be applied to the actual two endpoints of(1).

For each row i let
 p_i^theta(y)=T_iy K_theta(y)/(T K_theta)(i).
It is a genuine finite positive probability row. For any rows i,k,
 p_i^theta(y)/p_k^theta(y)
 = (T_iy/T_ky) (T K_theta)(k)/(T K_theta)(i) >= c,          (8)
because each factor is at least t_minus/t_plus.
Set q(y)=min(p_i^theta(y),p_k^theta(y)) and alpha=sum_y q(y).
The pointwise bound p_i>=c p_k implies alpha>=c.
Removing the common q part leaves two nonnegative measures of the same
mass 1-alpha. Hence, for any real vector u,
 |sum_y (p_i^theta(y)-p_k^theta(y))u(y)|
 <=(1-alpha)osc u <=(1-c)osc u.                           (9)
For alpha=1 the left side is zero; there is no division by a vanishing
remaining mass. Subtracting min u proves the same estimate for arbitrary
signed u, without assuming u>=0.

Finite differentiation gives
 d/dtheta log(T K_theta)(i)=sum_y p_i^theta(y)u(y).
Integrating its difference for rows i,k from0 to1 and using(9) bounds every
pair difference of the vector v=log(TK1/TK2) by (1-c)osc u.
Taking the largest pair difference proves(7), including singleton Y.

Now set h=log(r_K1/r_K2)=v-u. Oscillation satisfies the triangle inequality,
so
 osc u <=osc v+osc h <=(1-c)osc u+osc h.
Thus the second exact quantitative arrow is
 d_H(K1,K2)<=c^(-1)d_H(r_K1,r_K2).                         (10)
No original-family membership has been inferred for an auxiliary vector;
only the two positive endpoints are used in the conclusion.

## 4. The actual target interface supplied by the two arrows

Combining(5),(6),(10) gives, for every pair of actual admissible models,
 d_H(K1,K2)
 <=(t_plus/t_minus)^2 ||w||_1 d_obs(R^(1),R^(2)).           (11)
The same original T, labels and positions are essential. The actual Q,D,Z
are allowed to differ freely as in(1). Equation(11) is a quantitative
inverse for the target K after nuisance elimination, not just exact
identifiability and not the distance of arbitrary data to a model set.

If an arbitrary complete positive table P is within epsilon of each of
two actual admissible models, the triangle inequality for(2) additionally
gives d_H(K1,K2)<=2(t_plus/t_minus)^2||w||_1 epsilon.
This last statement is conditional on existence of both actual models;
it does not assert a restricted-family fit or use an unattained infimum.

The constant is a simple explicit finite certificate, not an optimized
condition number. No claim is made about its sharpness. The family F need
not be convex, closed or compact. A real physical parameter lambda is not
recovered without its separate original map/injectivity/conditioning data.

## 5. Strict positivity alone has no T-uniform inverse modulus

The dependence on a quantitative control parameter cannot in general be
discarded. Here is an actual two-point model, with all nuisances and row
normalizers paid explicitly.

Take Y={1,2}, d=0, n_1=0,n_2=1, b=(0,1). Then V is the constant column,
the schedule is good, and w=(-1,1) satisfies(3).
For every epsilon>0 choose the SAME known matrix for the two endpoints
 T_epsilon=[[1,epsilon],[epsilon,1]].
All four entries are strictly positive. Choose F=F_all and
 K_plus=(3/2,1/2), K_minus=(1/2,3/2),
 Q_plus=(1/4,3/4), Q_minus=(3/4,1/4).                      (12)
Both targets have uniform mean1, both Q rows are strictly positive and
sum1, and no D nuisance is present because d=0.
For both signs Q(y)K(y)=3/8 at each state. Consequently the b=0 observation
row is exactly (1/2,1/2), with actual Z_0=3/4.

The two actual ratio vectors are
 r_plus=(1+epsilon/3,1+3epsilon),
 r_minus=(1+3epsilon,1+epsilon/3).
Their sums agree. The b=1 observation rows are therefore r_plus/s and
r_minus/s, s=2+(10/3)epsilon, with actual positive
 Z_1=(3/8)s. Every table entry is positive and every row is normalized.
There is no replacement by a formal unobservable ratio.

It follows by direct two-coordinate oscillation that
 d_obs(R_plus,R_minus)
 =2 log((1+3epsilon)/(1+epsilon/3)) ->0,
 d_H(K_plus,K_minus)=2 log3>0.                            (13)
Thus no function omega(t)->0 as t->0, independent of the particular
strictly positive T, can uniformly satisfy
 d_H(K1,K2)<=omega(d_obs(R^(1),R^(2)))
for this fixed two-row good design and all positive T in the stated
unrestricted family. Each epsilon is a separate fully positive instance;
epsilon=0 is never used as an allowed observation/control.
This does not contradict(11) for any one fixed known T.
It does not prove a nonuniformity claim for every possible restricted F.

## 6. Reuse, credit and current preservation boundary

The actual intellectual history is NONZERO. BFF considered the original
projective/log-ratio quantitative inverse question during the earlier C26
route, before the later data-image/best-fit consumers. This round explicitly
checked the two literal arrows and the complete positive-model witness.
It is classified REUSE_STANDARD_COMPOSE, not a new mathematical discovery.
The proof is self-contained after the literal model, and no unconsumed
C24 contraction theorem is borrowed. Classical positive-kernel contraction
and finite linear algebra are the methods.

4A owns the upstream exact schedule/model contribution. Her messages in
this direction supplied only held-coverage/occupation facts, not a formula
or proof repair. She did not construct the present explicit argument.
Root supplied CONTROL/durability requirements and zero mathematical input.
No independent peer vote is claimed here; this author ledger does not
turn old private thought into Source-reviewed evidence.

The genuinely accepted14637 image and16050 best-fit appendices stay
unchanged and are not additional mathematical premises needed in this
proof. Their separate Source/peer/ordinary histories are not migrated.
The original prereviewed/conditional physical-model, registration and
denial boundaries of the upstream C26 remain unchanged as well.
This working record is not a generic implemented tool, new paper, formal
Task closure, physical/noise/sampling claim or Native capability.

The first actual readback/identity and external author-freeze must follow
this writing. No main window, Source publication or independent acceptance
is inferred from local persistence. Original SID/DA/noRA, all STOP/UNKNOWN/
budget boundaries and ParentGoalOPEN remain. Only hand mathematics and
administrative prose/UTF8/hash IO were used, with no scientific program,
optimizer, enumeration, sampling, external query or new helper.

Global-Knowledge-Sync: main@67a02007 / GLOBAL_KNOWLEDGE_V1

