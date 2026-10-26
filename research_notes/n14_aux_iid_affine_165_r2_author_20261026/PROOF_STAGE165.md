# Stage165: a further exact real minimax interval with support-line sharpness

**AUTHOR_EXACT / computation assisted / no native CLAIM / not independently reviewed.** 2026-10-26. External N14 ternary iid sequential decision problem, not a native P000/X6 or heartbeat-BRC theorem. Frozen input: Stage164 author certificate at `awdawmip/enterprise-math@c085c64c14515b4d2fc3cbfb33751d4e1171530c`, path `research_notes/n14_aux_iid_affine_163_r2_author_20261026/certificate164.json`. GLOBAL_KNOWLEDGE_V1 source pin: `main@26a5b1b309aee44516bb5ee17ae76620521fe9de`.

## Exact theorem

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14. Behavioral policies can use **entire ordered observation histories** and randomized decisions P/Q/continue; stop no later than depth 14. Define `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P(tau)`, `tQ=E_Q(tau)`; `V14(alpha)=min max(tP,tQ)` subject to both errors <=alpha.

Write
- `K=13623672285/49693891`, `L=40009085000/149081673`; `m=K+L=80880101855/149081673`.
- `A=62947091618416625195/180720939287325966336`, `B=2138584004831606037541/180720939287325966336`.
- `eta=248469455/93707153704539389952`.

**For every real 0<=delta<=eta, V14(A+delta)=B-m*delta.**

Right endpoint, reduced rationals:
`alpha165=881259282664541428015/2530093150022563528704`;
`V165=4277168009143268563157/361441878574651932672`.

The Bellman support line proved here is unattainable for any alpha>alpha165. This does not assert that the value function terminates or has no other supporting lines beyond alpha165.

## Bellman lower support for unrestricted full-history policies

For a count state s=(n,a,b), with a zeros and b ones in n draws, the P-normalized likelihood ratio is `ell(s)=2^(a+b)/3^a`. Backward recursion:
`H_s=min{K ell(s), L, 1+sum_i P_i H_(s+e_i)}`; omit continuation at n=14. For arbitrary **ordered-history** randomized policies, backward induction at each history gives
`tP+K eQ+L eP >= H_root`.
Hence `V14(alpha) >= H_root-(K+L)alpha` since max(tP,tQ)>=tP and K,L>0.

Fraction-exact checking of all `sum_{n=0}^{14}(n+1)(n+2)/2=680` count states yields
`H_root=819944053177461253554178891/4083385870731431154548736`.
Precisely two ties exist:
`R=(10,0,1)` Q/continue, and `W=(10,7,3)` P/continue.
The other **1,238** action gaps are strictly positive, minimum `8257109179793/821825520500736`. The replayer independently regenerates all 680 Bellman minima and these gaps.

## Constructive optimal behavioral policies for every real point

Let r be the probability of choosing Q at R, and w the probability of choosing P at W. All other actions choose the unique Bellman minimum. Track four observers `M(r,w)=(eP,eQ,tP,tQ)` with distinct positive P/Q branch weights (3,1,20)/24 and (1,1,10)/12.

All first-hit R histories (10 prefixes) and W histories (30 prefixes) are at *the same depth* 10 but have different zero-letter counts, hence the two prefix cones are disjoint. The R first-hit P/Q masses are `9765625/120932352`, `9765625/60466176`; W masses `5/4831838208`, `5/10319560704`. P- and Q-mass normalization to 1 holds at all corners.

A Fraction **count-state suffix recursion** and a literal **unmerged ordered-history integer-weight DFS** agree on all four deterministic corners, with 409696, 408976, 409456, 408736 visited nodes (total **1,636,864**). They establish
`M(r,w)=M00+r*dR+w*dW`, zero mixed difference for all four components, where:

`M00=(608952193221479015/1752976676930715648,9337786780675/26748301344768,2600355721215262961/219122084616339456,153514628699909/13374150672384)`

`dR=(4521484375/1486016741376,-3232421875/1253826625536,-61181640625/557256278016,-20751953125/104485552128)`

`dW=(-8195/1603087953297408,1975/213986410758144,-77375/66795331387392,-10625/17832200896512)`.

Set `D(M)=eP-eQ`. The exact coefficients are
`D(M00)=-3009001236837785/1752976676930715648`,
`D(dR)=225517578125/40122452017152`,
`D(dW)=-50280865/3505953353861431296`.
Thus `D(M)=0` iff

`r(w)=257914391728953/844544000000000+(30168519/11823616000000000)w`.

Every real w in [0,1] gives legal coins, since `0<r(0)<=r(w)<=r(1)=3610801514373861/11823616000000000<1`. The common error is exactly `alpha(w)=A+eta*w`; at w=0, `r(0)` is the verified Stage164 endpoint R coin and `M=(A,A,B,tQ)`. At w=1 the asserted alpha165 and V165 result.

At w=0 the time advantage `tP-tQ=25049209729437132035/60240313095775322112>0`; at w=1 it is `350688935928809353165/843364383340854509568>0`. The advantage interpolates affinely, remaining positive throughout. Also `tP+K*eQ+L*eP=H_root` holds exactly at both endpoints, and therefore throughout the real interval. The feasible policies thus attain the Bellman lower bound pointwise, proving the theorem without floating-point fitting or sampling.

## Strict right-support sharpness

If the *same support line* attained equality at any alpha>alpha165, positivity of K,L and the inequalities above would force eP=eQ=alpha and Bellman-minimal actions at every reached positive-probability history. Compactness of the finite-horizon policy space assures attainment if equality for V14 held. Every strict-action state has a unique forced move.

At each tie count state, all first-hit ordered histories share the same conditional iid suffix and Q/P likelihood ratio. Averaging a history-dependent tie coin with **P prefix-mass weights** leaves all four observers unchanged under P and Q. Because R and W first-hit cones are disjoint, every equality-attaining full-history policy is four-observer equivalent to some `M(r,w)` with r,w∈[0,1]. Equal errors imply r=r(w), and `alpha(w)=A+eta*w<=alpha165`, contradiction. Hence this support line is *strictly* unattainable beyond alpha165.

## Evidence, boundaries and next question

The included executable exact verifier regenerates both algorithms, 680 states, 1,238 positive gaps, four complete corner vectors, first-hit masses, error balance and endpoint identities. Its companion JSON stores every exact rational. The calculations share the explicitly declared P/Q model, not a clean independent mathematical review. The main Stage165 result is *author-exact*, not a Source Result, Foundation theorem or native BRC computation; the positive two-measure ordered branch interpretation is an auxiliary BRC-style observer only, with original source and path identity retained.

The separately scanned **Stage166 dual-only** candidate has K=`310447538892/1139969309`, L=`912521643352/3419907927` and a new P/continue tie at `(7,4,1)` alongside R. The exact first-closure step from Stage165 is `103222121856592293/56649510584791319`. **Stage166 primal optimality is open**: compute first-hit ordered cones, four observers and the legal balanced real interval or a rational obstruction. See next task packet.

Native owner read returned `CONTROL_QUOTA`; native session start returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. The verified GitHub identity has repository write permission but no inferred native CLAIM or independent Driver authority. P000 and ACTIVE worldview remain unchanged.
