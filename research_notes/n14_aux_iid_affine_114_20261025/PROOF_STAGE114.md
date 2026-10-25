# Stage114: sharp exact real-affine optimum for the external ternary iid N=14 test

Evidence: AUTHOR_EXACT_FINITE_PROOF (two locally executed exact arithmetic implementations; not native CLAIM/Result, independent Driver review, Foundation acceptance, or a P000/X6/Heartbeat theorem).

## Frozen inputs and theorem

Pinned reads for this research turn: GLOBAL_KNOWLEDGE_V1 main@85640815cacedf31031681f61024edb9e04a13df; Enterprise Math main@fdbfdfc1b2d6121cccfd91cad8d8a33b07803ce9. Read both GLOBAL entry files, EM task bootstrap, ACTIVE worldview, P000 startup+full contract, native X6 and joint-observer restrictions, math/code policies, and current docs/PORTABLE_RESEARCH_PROTOCOL.md. Native owner listing returned CONTROL_QUOTA. Native researcher session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No current native owner or CLAIM is inferred.

External model: at most 14 iid draws, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). All randomized full ordered-history stopping tests are admissible. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau); V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

Reuse the author-verified Stage113 right endpoint alpha113=183184813761431567431/527550113844125761536 and V113=27026770528279165031729/2110200455376503046144, at A=(10,3,0) P-stop probability u113=929342188946273/986137600000000 and at D=(9,1,2) forced continuation. Stage113 is author evidence, not a native Result.

Define
K=1903247523/2052316, L=443700120/513079,
S=K+L=525435429/293188,
gamma=465217/1320720,
w*=170386233161181/1042086080000000,
eta114=594704749143575417/150993774647608376033280.

**Theorem. For every real 0<=delta<=eta114,**
V14(alpha113+delta) = V113 - S*delta.

Its right endpoint is
alpha114=900372060659842701793/2592933255351443128320,
V114=132764620121352969281069/10371733021405772513280.

The same supporting affine line is strictly below V14(alpha) for every alpha>alpha114; no shape of V14 beyond this support face is asserted.

## Global Bellman lower bound (full ordered-prefix tree)

For state s=(n,a,b), where a and b count symbol-0 and symbol-1 outcomes, the likelihood ratio R=Q/P=2^(a+b)/3^a. In conditional P-units, the exact Bellman recursion is

H(s)=min{ K*R(s) [stop and declare P], L [stop and declare Q], 1+(1/8)H(n+1,a+1,b)+(1/24)H(n+1,a,b+1)+(5/6)H(n+1,a,b) [continue] }.

At depth n=14 continuation is excluded. Fraction-arithmetic enumeration checks all 680 count states, 1238 strictly positive non-minimizer gaps, minimum positive gap 11023/9235422, zero negative gaps, and exactly two action ties: A=(10,3,0) Pstop/continue, D=(9,1,2) Qstop/continue. The root rational value is
H(0,0,0)=4462691822843638799135951/7026683753304176984064
=V113+(K+L)*alpha113.

For every ordered history, conditional future symbol laws and the likelihood ratio depend solely on its count state. Inducting on the *entire ordered-prefix tree*, rather than restricting competitors to count-only strategies, establishes
H(root)<=tP+L*eP+K*eQ<=max(tP,tQ)+(K+L)*alpha.
Thus V14(alpha)>=H(root)-(K+L)*alpha for all alpha.

## Positive ordered-history carrier and moment identities

Let u=probability of declaring P at A, otherwise continue; let w=probability of declaring Q at D, otherwise continue. Elsewhere use the unique Bellman-minimizer action.

Their two positive branch cones are disjoint *independently of policy*: D has already accumulated two symbol-1 outcomes, which can never decrease to A's zero; A has 10 draws and cannot be an ancestor of D at 9 draws. Literal ordered-path enumeration identifies 172 D-first-hit histories, positive masses
P(D first)=671875/53747712,
Q(D first)=671875/20155392.
With D forced to continue, there are exactly 31 conditional terminal suffixes, so stopping at D replaces 172*31=5332 terminal ordered histories. The D continuation moments, with additional time counted after reaching D, are
(eP,eQ,tP,tQ)=(97421/98304,641/248832,51509/36864,25831/20736).

The root moment vector M(u,w)=(eP,eQ,tP,tQ) is *exactly affine*, with no u*w term, because the tie cones are disjoint. Its exact first derivatives are

dM/du=(-248046875/990677827584,
        65234375/208971104256,
       -3012109375/41278242816,
       -417578125/17414258688).

dM/dw=(593265625/5283615080448,
       -430671875/5015306502144,
       -34607609375/1981355655168,
       -17355203125/417942208512).

The inherited policy at (u113,w=0) is recomputed in the current action table and yields eP=eQ=alpha113 and tP=V113 exactly, with tP>tQ.

Equating the *two actual error probabilities* gives, uniquely,
u(w)=u113+(465217/1320720)*w.

Here is the decisive new boundary condition: at w=1 one would need u=3830112646838819/2958412800000000>1, an impossible stopping probability. The true feasible saturation is at u=1, w=w*=170386233161181/1042086080000000, with 0<w*<1. As w increases from zero to w*, both errors grow equally from alpha113 to alpha114, increasing by eta114. At the two ends,

(tP-tQ)|w=0 = 451683124663758426763/703400151792167682048 > 0,
(tP-tQ)|w=w* = 444777657503394885715/691448868093718167552 > 0.

Affineness gives tP>tQ throughout the *entire real interpolation interval*. For each w in [0,w*], the policy has equal errors, tP=max(tP,tQ), and its Bellman action at every positive path is minimizing. Hence it attains the global bound H(root)-(K+L)*alpha, proving the full-real theorem.

## Sharp right endpoint against arbitrary history-dependent randomization

The full-horizon policy set is a finite product of compact simplexes, so any feasible optimal value is attained. To attain the *same dual line* above alpha114, equality in the Bellman inequality and both positive-multiplier error bounds is necessary. Every positive-mass action must be Bellman-minimizing; only A or D admit any local randomization, and both eP and eQ must equal alpha.

Every ordered prefix entering a given count state has the same fixed Q/P ratio. Averaging any history-dependent tie randomization by the positive P first-hit mass at that state therefore preserves both error and expected-time contributions, for the four explicitly declared observers only. Actual first-hit path provenance is retained and the cone-disjointness proof certifies absence of cross terms. Thus all equality cases reduce to aggregate u,w in [0,1] with eP=eQ forcing u=u113+gamma*w. The bound u<=1 yields w<=w*, and consequently alpha<=alpha114. This contradicts alpha>alpha114. The support line has a sharp right endpoint.

## Executed verification, limitations, next question

Author program 1 uses Fraction Bellman and independently computes policy moments, positive D reachability, exact conditional suffix moments and all rational identities. Author program 2 constructs the Bellman table separately, then directly walks literal ordered prefixes, accumulating integer numerators over 24^14 and 12^14. Its four deterministic-corner visits are 884347, 880747, 876607, 873007 nodes, with D first-hit 172 in each; it reproduces both derivatives and zero mixed coefficient. Both executed locally and passed. The local reproducibility package additionally contains expanded proof, actual executed source code, raw outputs, exact JSON certificate and SHA256 manifests.

The work remains AUTHOR_EXACT_FINITE_PROOF, pending independent Driver review and native CLAIM/Result. It is external iid, not a derivation of native X6/Heartbeat behavior. All reductions are observer-typed.

**Stage115 next research:** The A randomization saturates at u=1 while D still has w=w*<1. Characterize the next min-max/two-error LP support face immediately to the right, allowing dual changes in sample-time weights and binding error constraints instead of extrapolating the invalid u>1 compensation; prove the next exact continuous interval, or an exact obstruction.
