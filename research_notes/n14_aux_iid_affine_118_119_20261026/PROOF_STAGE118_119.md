# Exact affine Stage118–119 of the N=14 auxiliary sequential test

Status: AUTHOR_EXACT_COMPUTATION_ASSISTED_PROOF; independent Driver review and native Result admission pending. These are theorems for the stated external iid model only, not P000, X6, Heartbeat physics or native six-dimensional Cells.

## 1. Model, verified input and universal dual

For ordered ternary histories of length at most 14, let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). A randomized stopping and decision policy has four observables eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau). Define V14(alpha)=inf_{eP,eQ<=alpha} max(tP,tQ), allowing the entire ordered-history policy class.

Previous author-level Stage117 input: alpha117=900390161470101555373/2592933255351443128320; V117=132635001628579939136609/10371733021405772513280. Source: research_notes/n14_aux_iid_affine_117_20261026/PROOF_STAGE117.md.

For a count state (n,a,b), n<=14, the conditional likelihood ratio R=Q/P=2^(a+b)/3^a. Given positive rational dual multipliers K,L define the backward Bellman value H(n,a,b) as the minimum of:
P-stop cost K*R; Q-stop cost L; and, if n<14, continuation cost 1+(1/8)H(n+1,a+1,b)+(1/24)H(n+1,a,b+1)+(5/6)H(n+1,a,b).
There are sum_{n=0}^{14} binom(n+2,2)=680 count states and exactly 1240 non-chosen action comparisons (at final depth only two actions). For ANY randomized policy on literal ordered histories, the conditional suffix is iid and depends only on counts; Bellman backward induction on those literal prefixes therefore proves H(0)<=tP+L*eP+K*eQ. Hence the global lower bound V14(alpha)>=H(0)-(K+L)*alpha. This use of counts is limited to the declared four observers, iid laws and horizon; it does not erase provenance in a general future-dependent state.

## 2. Stage118 – full real interval theorem

Dual parameters K118=254421/296, L118=90232/111, S118=K118+L118=1485119/888.
Claim for every real delta with 0<=delta<=eta118=11742875/9527238592561152:
V14(alpha117+delta)=V117-(1485119/888)*delta.

Right endpoint alpha118=900390164666042415373/2592933255351443128320 and V118=132634980248613749666609/10371733021405772513280.

A complete exact Fraction Bellman check of all 680 states gives exactly two tied count states: D=(9,1,2), Q-stop/continue, and G=(13,6,4), Q-stop/continue. Exactly 1238 remaining action gaps are strictly positive, no negative gap exists, and the least strictly positive gap is 837575281/15909322752. Root H118(0)=3609077962245944299849/6080637848103419904=V117+(K118+L118)*alpha117.

Ordered first-hit prefixes along the deterministic Bellman skeleton: D has 172 prefixes, P mass 671875/53747712 and Q mass 671875/20155392; G has 15234 prefixes, P mass 317375/3131031158784 and Q mass 317375/2229025112064. This is a provenance- and multiplicity-preserving exact positive-rational labeled-history BRC-style carrier, not signed-amplitude cancellation.

The first-hit descendant cones are disjoint: G cannot precede D by depth, while D (depth9 with one zero) cannot precede G (depth13 with six zeros) because four additional draws cannot add five zeros. Consequently the four-moment vector M=(eP,eQ,tP,tQ) is EXACTLY M(0,0)+w*d_w+z*d_z, with w=P(Q-stop at D) and z=P(Q-stop at G) denoting randomized action probabilities (not law P probabilities). Derivatives computed by exact rational suffix recursion and independently by literal integer-weighted DFS:

d_w=(593265625/5283615080448, -430671875/5015306502144, -34607609375/1981355655168, -17355203125/417942208512).
d_z=(317375/25048249270272, -317375/26748301344768, -317375/3131031158784, -317375/2229025112064).

Set u=1-z, 0<=u<=1, and choose
w(u)=376073711298041/1042086080000000+(921657/7443472000)*u.
All probabilities remain between zero and one. Substituting these rational functions into the four-moment map, direct exact endpoint calculations give, for both u=0,1, eP=eQ=alpha117+eta118*u, tP=V117-S118*eta118*u, and tP>tQ. Since all four moments are affine in u, these claims hold for EVERY REAL u between the endpoints, not just sampled rational u. All chosen actions minimize Bellman costs, attaining H(0)-S118*alpha and establishing the global primal optimum.

## 3. Stage119 – full real interval theorem

At Stage118 right endpoint G fully continues while D remains randomized. The next exact dual boundary preserving D's Q-stop/continue tie is J=(6,5,1), P-stop/continue. The computed parameters:
K119=14079159385935/17413198588;
L119=272890577165656/352617271407;
S119=K119+L119=2231974218923359/1410469085628.

For EVERY REAL delta in 0<=delta<=eta119=4353299647/592805956870471680:
V14(alpha118+delta)=V118-S119*delta.

Endpoint:
alpha119=900390183707375071351/2592933255351443128320,
V119=132634859722005927805223/10371733021405772513280.

A fresh full Bellman recursion has exactly two ties, D=(9,1,2) Q-stop/continue and J=(6,5,1) P-stop/continue, with 1238 strict positive gaps, 0 negative gaps, minimum strict gap 76168651372577/5483903804921664, and root H119(0)=2715351325492390545950322492769/4829139473901711838949670912=V118+S119*alpha118.

D has the same 172 first-hit prefixes and masses as before. J has precisely four first-hit ordered prefixes, total P mass 1/196608 and Q mass 1/746496. The first-hit cones are disjoint: D is too late to precede J; J has five zeros versus D's one, and monotonic counts exclude J preceding D. Four-moment affinity M(w,y)=M(0,0)+w*d_w+y*d_y therefore holds with D Q-stop probability w and J P-stop probability y, with the same d_w and
d_y=(-287489051/10820843684757504,5340805/160489808068608,-2860972883/450868486864896,-27244717/13374150672384).

For any real 0<=y<=1, error equalization yields
w(y)=376202743278041/1042086080000000+(157363588513/521043040000000)*y.
Exact endpoint checks show legal 0<w<1, eP=eQ=alpha118+eta119*y, tP=V118-S119*eta119*y and strict tP>tQ. Affinity yields all real interior points. These strategies select only Bellman minimizers, so the global lower bound is attained on the entire interval.

## 4. Right-edge sharpness (both stages)

The finite ordered-history random-policy space is compact; the infimum is attained. If the SAME dual support remained exact for some alpha larger than the displayed right endpoint, equality in the positive-multiplier dual lower bound would force BOTH errors equal to alpha, tP=max(tP,tQ), and all positive-mass choices to be Bellman minimizers. Each dual has only its two displayed tie states. Because iid suffix observers and P/Q likelihood ratio are constant on any ordered prefix with the same count, arbitrary history-dependent randomization can be averaged on each tied count fiber to a single effective probability preserving all four observers. Disjoint first-hit cones exclude interaction terms. Error equality then forces respectively w(u) or w(y), and the feasible parameter box implies u<=1 or y<=1. This forces alpha<=alpha118 or alpha<=alpha119, contradiction. Therefore each stated support line is strictly below the true value for every larger alpha (not a claim about the shape of the succeeding optimal segment).

## 5. Executed exact certificates and limitations

The author ran VERIFY_STAGE118_119.py locally using standard-library fractions, checking full Bellman states/action inequalities, four deterministic tie corners, first-hit masses, exact derivatives and both real-interval endpoint identities. It also executes an independent literal ordered-history DFS on integer weights P=(3,1,20)/24, Q=(1,1,10)/12 (not merely a recomputation of count-state moments). DFS corner visits Stage118 were 898165,852463,890425,844723, and Stage119 were 898165,893725,890425,885985. Additionally two separately authored local integer DFS programs each returned PASS (standalone local scripts currently refer to the separately preserved exploration JSON; see bundled source). Full observed exact output is verification118119.json and certificate118119.json. GitHub source publishing alone does NOT prove execution on GitHub.

BRC resolution: REUSE_APPLIED, namely typed positive-rational provenance-preserving first-hit ordered history with four declared observers and exact iid suffix factorization; not a native BRC–Shor computation or transferable six-axis physics theorem. P000 remains unchanged.

## 6. Stage120 exact dual candidate, not yet a primal theorem

From the Stage119 right endpoint, J uniquely decides P; D still mixes. Keep D's Q/continue tie along dL/dK=164096/214569. At distance x=201770757485956473/33139040819624212 the unique first formerly-positive action gap reaches zero: A=(9,3,0), P-stop/continue. The candidate K120=1527132609/1903099, L120=1463947128/1903099 has 680 states, exactly D and A tied, 1238 strict positive gaps and minimum positive gap 76168651372577/4909786414055424. **Stage120 primal attainable interval is OPEN**. Compute true ordered first-hit masses, feasible error-equalizing mixtures and independent DFS, then prove primal interval or an exact obstruction.

## 7. Frozen source, authorship and authority

GLOBAL_KNOWLEDGE_V1 canonical main pinned 10181a7d48695beba8a4375e2d3d94112989ad6a; Enterprise Math input main pinned 0e8eda0b046aafd500c082fab9f1e22e3d8e6451. P000 startup Git blob equals canonical original 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Current ACTIVE worldview and docs/PORTABLE_RESEARCH_PROTOCOL.md were inspected.

Connected GitHub login awdawmip has project-repository write permission. Native em_status exposed v0.6.11; native tasks read failed BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. Native session creation failed STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Live Owner remains unknown, and this local author activity cannot assert native CLAIM, Result admission or independent Driver review. This research_notes persistence is scientific provenance only.
