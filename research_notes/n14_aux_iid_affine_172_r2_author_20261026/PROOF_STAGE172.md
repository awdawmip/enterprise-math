# Stage172 — complete real-interval minimax theorem (external N14 ternary IID)

**Scientific classification (2026-10-26): AUTHOR_EXACT, NOT_NATIVE_CLAIMED, NOT_ADMITTED.** This document is a full proof in the explicitly scoped auxiliary model, supported by locally executed exact-rational two-structure computation. It does not assert independent Driver validation, formal Lean checking, or a P000-native Cell result.

## 1. Model, sources, and theorem

Frozen global snapshot: GLOBAL_KNOWLEDGE_V1 main@656cd167e44f250e1e900e5c903ad96beb8315a5 (bootstrap, manual, P000 startup and ACTIVE worldview); P000 original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched the startup projection. Source Enterprise Math main@f990313d69b823ce51e583a26d01d5f7dc08d1d1 (current docs/PORTABLE_RESEARCH_PROTOCOL.md). The distinct Stage171 author predecessor is immutable commit 53826073e9b493695cf20f014ead19088fd4d0d6.

Let P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6) be distributions on three labelled IID symbols. Allow every randomized sequential test on **complete ordered histories**, forced to stop by observation 14, with terminal verdict P or Q. Let eP=P(verdict Q), eQ=Q(verdict P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha. Compactness of the finite full-history policy tree ensures the minimum exists.

Define
- alpha171 = 882435274780741015735/2530093150022563528704;
- V171 = 4191188444229937372757/361441878574651932672;
- K172 = 2453276570264541/10128738563455;
- L172 = 7332367848199016/30386215690365;
- S172 = K172+L172 = 14692197558992639/30386215690365;
- H172 = 7500321462434479703133415412645/41614318285465632307238928384;
- width172 = 10128738563455/93707153704539389952;
- alpha172 = 220608887064170557255/632523287505640882176;
- V172 = 1047792388565411809841/90360469643662983168.

**Theorem:** For *every real* delta in [0,width172], including irrational delta,

    V14(alpha171+delta) = V171-S172*delta.

For every alpha>alpha172, the same support line H172-S172*alpha is strictly smaller than V14(alpha). This is sharpness of that support, not termination of the value function.

## 2. Exact Bellman dual bound

For each prefix count state s=(n,a,b), the Q/P likelihood ratio is ell(s)=2^(a+b)/3^a, independent of the ordering given the counts. Under P, the three candidate costs are (i) K172*ell(s) for deciding P; (ii) L172 for deciding Q; and (iii) 1+sum_i P_i*h(child_i(s)) to continue, omitted at n=14. Define h(s) as the backwards minimum. Apply conditional optimality separately to **each ordered history**: there is no assumption that admissible strategies are count-only. Backwards induction yields for any full-history strategy

    H172=h((0,0,0)) <= tP+K172*eQ+L172*eP.

Because both dual multipliers are positive, V14(alpha)>=H172-S172*alpha for every feasible alpha.

The exact Fraction calculation exhausts sum_{n=0}^{14} binomial(n+2,2)=680 states. There are exactly 1,238 positive nonwinning action gaps (minimum 3442966771823/273475941213285), no negative gaps, and precisely two tied count states: R=(10,0,1), stop Q / continue, and Y=(5,4,1), stop P / continue. All other best actions are strict. No float tolerance is used. See VERIFY_STAGE172.py, certificate172.json and the local original execution log.

## 3. Exact attainment by disjoint randomized first-hit cones

At R stop Q with probability r; otherwise continue. At Y stop P with probability y; otherwise continue. Everywhere else use the unique Bellman minimizer. R and Y cannot occur on the same ordered history: at depth five, Y has four outcomes of symbol zero, while R at depth ten has no zero. Their first-hit cones are disjoint, so the policy observable M=(eP,eQ,tP,tQ) satisfies

    M(r,y)=M00+r*dR+y*dY

with exactly zero mixed r*y term. Two independently implemented computations were executed on all four deterministic (r,y) corners: a Fraction conditional-suffix recurrence and a separate unmerged ordered-history DFS with integer step numerators P=(3,1,20)/24 and Q=(1,1,10)/12. All 16 observer coordinates matched exactly; terminal P and Q masses were each one for all corners. DFS visits: M00=290341, M01=286156, M10=290101, M11=285916, total 1,152,514. The 4-coordinate mixed difference is (0,0,0,0).

R has ten labelled first-hit histories of total P mass 9765625/120932352 and Q mass 9765625/60466176. Y has three labelled first-hit histories of total P mass 1/32768 and Q mass 1/82944. These are separate positive masses, not signed amplitudes.

The exact equality eP=eQ has unique solution

    r(y) = 8992237821259453/11823616000000000
           + (7247493724371/59118080000000000)*y.

Both r(0) and r(1) lie strictly between 0 and 1, so this randomization is a valid policy for every real y in [0,1]. At y=0, the two errors equal alpha171, tP=V171, and tP-tQ=939402695545477608775/2530093150022563528704>0. At y=1 they equal alpha172, tP=V172, and tP-tQ=234844840446617153803/632523287505640882176>0. The exact width is alpha172-alpha171=width172>0 and V172-V171=-S172*width172. Both endpoint policies satisfy tP+K172*eQ+L172*eP=H172.

Every coordinate of M(r(y),y) is affine in y, hence for all real y∈[0,1] the errors stay equal; tP>=tQ by endpoint positivity; Bellman dual equality persists; and the common error increases strictly from alpha171 to alpha172. This attains the universal lower bound on the entire real interval.

## 4. Exact right-hand support-line sharpness

Suppose for alpha>alpha172 an optimal policy achieved equality in V14(alpha)>=H172-S172*alpha. Compactness gives an optimizer. Strict Bellman gaps and full support of all three symbols force unique minimizing actions at every positive-reach history outside R,Y. Positive K172,L172 force eP=eQ=alpha. At R or Y, all ordered histories with identical counts have identical Q/P likelihood and continuation suffix law. Their possibly history-dependent randomization probabilities can be averaged under P-prefix weights; because Q/P is constant at each count state, all four (eP,eQ,tP,tQ) are preserved. The disjoint first-hit cones rule out interactions. Thus the only possible equality strategies have effective r,y∈[0,1] and affine M00+r*dR+y*dY.

Error balance forces the unique r(y) above. Its common error is a strictly increasing affine function of y, bounded above at y=1 by alpha172. It therefore cannot equal alpha>alpha172. Contradiction; the Stage172 support is strictly unattained beyond the right endpoint.

## 5. Scientific and control limits

This is a finite-horizon **external auxiliary** sequential-decision model. The BRC information-retention discipline was genuinely used to retain labels, independent positive P/Q path weights and first-hit provenance; no native typed BRC operator was executed. A native X6 embedding, three-dimensional slice semantics, full residual-preserving observer map and P000 transfer theorem are *not* established.

Current authenticated GitHub identity: awdawmip (repo push true). Native em_control_tasks returned CONTROL_QUOTA; em_session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Thus live Task owner is unknown; this is an independent author-side research note, not a native session/CLAIM/Source Result/Driver acceptance. Actual local full scripts and logs are in the portable ZIP. Next open question: NEXT_TASK_PACKET_173.md.
