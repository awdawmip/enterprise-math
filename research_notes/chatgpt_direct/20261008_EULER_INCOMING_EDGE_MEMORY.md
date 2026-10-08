# Euler first returns without erasing the incoming edge

Status: PROVISIONAL MODEL THEOREMS AND EXACT BRC CERTIFICATES; NOT FORMALLY ADMITTED.
Date: 2026-10-08 (Asia/Tokyo). Same-conversation continuation, not independent replication.
Global read snapshot: 50f7f62ad67b6573ef86e307fac9cb2f47a2b3a7.
Source read snapshot: f7eebe767e574ff2672737814bdb62fde7dfd78a.
Prior frontier: add590ed5939884cc2b8f741c9cfb3a219d30a52, research_notes/chatgpt_direct/20261008_EULER_LOCAL_FIRST_RETURN_CLOCK.md, Git blob 6d0717195b3173fdf72a0cefcaafb0b2460b8a07.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01; not platform-attested.
Research activity: UNVERIFIED / REGISTER_PENDING. No borrowed role, CLAIM or acceptance.

## 1. What changes, and what does not

The preceding source proves one nonbacktracking (NB) excursion, with no previous neighbour at its initial departure. It explicitly does NOT assume an incoming-memory reset between repeated NB excursions. This unit supplies the continuous version: after returning to the base, the actual incoming neighbour is retained and the next departure cannot immediately retrace that edge.

The state is (binary channel triple x, carried sign chi, previous comparison vertex a, current comparison vertex b). At the base, first execute the unchanged local collision P^chi, then choose equally among the two neighbours other than the current and previous vertices. Away from the base, traverse such an edge without another collision. Each edge transports chi by the sourced comparison bit. The previous vertex changes to the vertex just left, INCLUDING across a completed return. A first-return macro merely observes successive visits to the base; it performs no extra reset.

The no-immediate-reversal rule, equal fresh local choices, fixed contact base and collision-before-departure boundary remain declared candidate assumptions. They are not deduced from a primitive force law. K4 is the existing comparison graph, not native X6 space; previous-vertex and channel/sign data are internal relation types, not added spatial axes. Edge count and completed-contact count are distinct and neither is calibrated physical time. P000 and the residual-faithful worldview are unchanged.

Actual reuse: prior archive euler_first_return_evidence.zip SHA256 c9db213c791a962780c14a46057a40d7f4d70916e4fffafbac6df7bd2067227e. Its 22 manifest files were verified. Eleven required Python files are reused byte-for-byte, including brc_first_return.py SHA256 f5059c5c1e482630a600ad6ca0060aa4b05e267330543aa9f5bc5e8b93740cbc and the unchanged route/collision/phase/source chain. Every new positive edge uses existing edge_children, source transition_bit, cwm_edge/cwm_propagate and cwm_recoalesce. Source brc_weighted.py remains full blob 3f205696709e847909958a153f8fe10d3f6b70f0; source euler_fcc_chirality.py remains full blob 6f8b147c094720c2749f620a40394c4d7b67a386. The latter is executed through the unchanged inspected dependency-closed excerpt, not misrepresented as the whole module.

REUSE_EXECUTED and EXTEND_EXISTING_TOOL: this extends the existing path state and its observer certificates, not a newly admitted BRC family. No numerical pi, trigonometry, roots, matrix exponential or alternative numerical state propagator is used. Rational matrices below describe certified sums of actual BRC paths, not a substitute positive-world solver.

## 2. Exact joint first-return kernel including the arrival port

Fix the contact base b and an actual incoming neighbour i. For the first positive return let L be its length, j its arrival neighbour and h its closed-loop flip parity. Define B_l(i;j,h) to be the total positive BRC mass of precisely these paths. It records a joint event, not separate marginals.

The first two choices have two alternatives each. After those two edges, the walk is among the three nonbase vertices: one allowed next edge returns to b, while the other must continue to the third nonbase vertex. Conditional on not returning, this internal directed traversal repeats with period three. In six such transitions it repeats every internal edge twice, restoring its parity for ANY sourced edge assignment. Thus, for l>=3,

B_(l+6)(i;j,h) = B_l(i;j,h)/64.

This is a bijection of the four supported first-return path skeletons at each length, with their actual weights. Consequently the exact formal length kernel is

B(u)[i;j,h] = [sum_(l=3)^8 B_l(i;j,h) u^l] / (1-u^6/64).

Evaluation at u=1 closes the infinite MASS sum by multiplying the first six coefficients by64/63. The infinite path count is NOT represented as a finite CWM count. Actual execution keeps finite stopped paths and pending paths; the geometric closure is a proved observer identity.

For every i and every edge field,

Pr(L=l | i)=2^(-(l-2)), l>=3;
Pr(L>M | i)=2^(-(M-2)), M>=2.

Thus L has mean four, even with an actual incoming edge at the base. This conditional law is the same for all i, not a claim that the complete returned state is independent of i.

After summing over parity, the arrival-neighbour kernel is universally

T_ij = 3/7 if i=j, and 2/7 if i!=j.

This follows by grouping the internal directed three-cycle's returns modulo three. In matrix notation T=J/3+(I-J/3)/7, so an initially uniform incoming-neighbour distribution stays uniform, although the arrival neighbour is correlated with its predecessor. This statement concerns the comparison ports, not physical momentum.

## 3. A complete criterion for deleting incoming memory at return boundaries

Change comparison frames so all three edges incident with b have flip bit zero. The remaining three internal edges form a signed triangle. Let k be the number of its negative edges. Equivalently k counts odd rooted triangular face holonomies, so this classification is gauge invariant. Permuting the three nonbase labels leaves only four rooted types.

Summing the source-generated B_l for l=3,...,8 using section2 gives the following conditional even-return probabilities:

k=0: p_i=1 for all three ports.
k=1: p_i=1/2 at the two endpoints of the negative edge; p_i=4/9 at the third port.
k=2: p_i=4/7 at the common endpoint of the two negative edges; p_i=5/14 at the other two ports.
k=3: p_i=1/3 for all three ports.

These rational values have a finite complete certificate: the four canonical internal triangles, the four length-skeleton choices at each of six lengths, and the exact period-six continuation. The checker additionally verifies all64 edge assignments,4 bases,3 actual incoming ports and16 frame changes. Rooted field counts are32,96,96,32 for k0,1,2,3.

The completed-return update is

(x,chi,i) -> (P^chi x, (-1)^h chi, j), with mass B(1)[i;j,h].

Projecting this to (x,chi) is an exact Markov aggregation for EVERY preparation iff p_i is the same for every i. Sufficiency: after summing all arrival ports, both output-sign probabilities are independent of i, hence every future composition factors through the projection. Necessity: different p_i already give different next-sign distributions from states with identical current (x,chi). Therefore incoming memory may be deleted at these return boundaries exactly for k=0 or3, but not for k=1 or2.

This is the standard row-sum factorization principle for strong lumpability, applied here with explicit BRC witnesses. It is not a new general aggregation theorem. It also does not license deletion of the previous vertex during an unfinished NB excursion, where the next allowed edge explicitly depends on that vertex.

## 4. In the all-negative field, no hidden reset is needed for the old p=1/3 law

For the all-negative source representative the two three-port kernels are

B_even = (1/126) [[20,11,11],[11,20,11],[11,11,20]],
B_odd  = (1/126) [[34,25,25],[25,34,25],[25,25,34]].

They have row sums1/3 and2/3, and their sum is T from section2. Evenness and arrival port are still correlated: for example the even diagonal entry is10/63, not (1/3)*(3/7)=1/7.

Nevertheless, after every actually completed excursion, the channel/sign endpoint law is exactly the old contact(p=1/3) mass law, for any joint preparation at the base. No independent reinitialization of the incoming port is required. Furthermore h=L mod2 in this representative, and the full law of (L,h) is independent of i. Thus the length-resolved channel/sign renewal law also closes. Hidden port correlations remain relevant to a future operation that queries the port or changes the comparison field.

The proof distinguishes two assertions: the microscopic incoming relation persists; this particular coarse observer does not need it under this particular continuation language. Fixed equal-mass macrorows preserve the specified endpoint masses/phases only, not the infinite original return-path multiplicity or maximum path weight.

## 5. A mixed sourced field makes the reset error observable

Use source edge order01,02,03,12,13,23 and the assignment e=(0,0,0,1,1,0), base0. Port1 is the common endpoint of the two negative internal edges. Its p is4/7; ports2,3 have p5/14.

First, consider a field-only unit x=(0,0,1) with initial signs fair and a known incoming port. Let zeta_0=omega^2, where omega^2+omega+1=0. The two-contact phase factors are

incoming1: zeta_2/zeta_0=1/7;
incoming2 or3: zeta_2/zeta_0=13/28.

The current channel/sign preparations and entire length marginal are identical. Only the incoming relation differs. It changes future phase without adding or losing positive weight.

Now prepare the incoming neighbour uniformly ONCE, and keep its actual subsequent value. Compare this true programme to a DIFFERENT operation which, at each return, redistributes the incoming neighbour independently with weights1/3 while preserving the channel/sign marginal. The reset is not natural NB continuation.

In both preparations, the incoming marginal remains exactly uniform, the sign marginal stays fair, and their joint marginal is1/6 per port/sign at every return. The marginal even-return probability stays3/7. Yet their phase multipliers are

n:          0       1        2          3
retained:   1      -1/2     5/14      -25/98
reset:      1      -1/2     5/14      -11/49.

Thus retained minus reset at the third contact is -3*zeta_0/98.

There is a direct two-return explanation. The true probability of two consecutive even returns is8/49, whereas independently resetting gives(3/7)^2=9/49. In a three-contact word the phase factor is1 only when both previous returns were even; otherwise it is-1/2 under a fair initial sign. Hence c_3=(3/2)Pr(even,even)-1/2, proving both values. The covariance of the consecutive even indicators is-1/49. One-time fairness does not delete the correlation that drives the next collision.

## 6. Two incoming classes are sufficient and necessary in each mixed rooted type

For k=2, classify port1 as C and ports2,3 as R. Exact parity-resolved class kernels, with rows and columns ordered(C,R), are

B_even^class = [[0,4/7],[1/14,2/7]],
B_odd^class  = [[3/7,0],[3/14,3/7]].

The two R ports have identical sums into every (next class,parity) block. Thus a histogram on (channel,sign,C/R) exactly predicts every future channel/sign distribution under the fixed completed-return programme. It is a12-state positive mass/phase representation in the unit-count sector instead of18.

For k=1, let C be the port not incident to the unique negative edge. The corresponding kernels are

B_even^class = [[17/63,11/63],[1/7,5/14]],
B_odd^class  = [[10/63,25/63],[1/7,5/14]].

The same statement holds. A one-class incoming representation cannot work because the current channel/sign can be identical while next-sign probabilities differ. Since the observer itself distinguishes the six channel/sign states, each requires two future-distinguishable incoming classes:12 is the minimum deterministic partition quotient for THIS coarse observation law. For k=0 or3 the minimum is six. This counts predictive stochastic states at completed returns, not native dimensions, all physical states, or the bit cost of exact weights.

The comparison-port name inside R can be erased only for the stated endpoint observer and repeated macros. Exact port observations, comparison-field interventions, individual source paths, intermediate edges, or history-dependent controls require a new equivalence proof. The full continuous carrier retains (x,chi,previous,current), with72 states in the unit-count sector.

## 7. Continuous NB edge time has a different Euler recurrence

Return to the all-negative representative and the continuous, incoming-preserving edge update. At any visit to the base, the collision occurs before the NEXT edge. Initially all paths are at the base, with any valid incoming neighbour and any binary-channel/sign preparation.

The first-return length functions are the earlier one-excursion formulas, now proved to apply conditionally on every genuine incoming neighbour:

R_even(u)=u^4/(4-u^2), R_odd(u)=2u^3/(4-u^2),
S(u)=sum_(t>=0) Pr(L>t)u^t=(u^2+u+2)/(2-u).

No-reset conditional factorization in section4 justifies a scalar renewal equation for initially positive/negative signs:

G_chi=1+omega^chi [S-1+R_even G_chi+R_odd G_-chi].

The common denominator after elimination is4-u^2+u^4-u^6. The numerator of G_+ is

4+4omega*u+(4omega-1)*u^2+3omega*u^3+(3+omega)*u^4+u^5,

and G_- is its conjugate. These are exact formal length-generating identities of actual BRC paths, not trigonometric series or an alternative world propagator.

Consequently every phase coefficient obeys

4*zeta_(t+6)=zeta_(t+4)-zeta_(t+2)+zeta_t, t>=0.

For a fixed initial triple and an independent fair sign, write zeta_t=c_t*zeta_0. Then

sum c_t u^t=(8-4u-6u^2-3u^3+5u^4+2u^5)/(8-2u^2+2u^4-2u^6),

c_0,...,c_8=1,-1/2,-1/2,-1/2,1/4,1/4,7/16,1/16,-5/64.

In particular, ordinary retracing and NB continuation first differ at edge4: the previous ordinary programme has factor-1/6, while NB has+1/4. The difference NB minus ordinary is5*zeta_0/12. They share the graph, all-negative comparison field, collision and mean return length four, not the incoming rule.

There is a uniform bound without numerical roots. For either parity subsequence, 4s_(n+3)=s_(n+2)-s_(n+1)+s_n. Starting from a triple bounded byB, the next three magnitudes are bounded by3B/4,11B/16,39B/64. Thus the triple sup norm contracts by at most3/4 per six edges. Since each binary-triple phase coefficient has magnitude at most1, normalized positive populations supported at the base satisfy

||zeta_t||_infinity <= (3/4)^floor(t/6).

For total positive weight W, multiply the bound byW. It certifies this phase, not disappearance of paths or energy. At each finite edge count a single initial path has CWM=(2^t,1,2^-t); the two-sign fair preparation has(2^(t+1),1,2^(-(t+1))). Comparison-edge time is not physical heartbeat time.

## 8. Evidence, literature boundary and continuation

Final execution passed117109 exact assertions, including35 integrity assertions (prior archive,22 prior manifest entries,11 reused Python sources, current CWM blob). New coverage:768 rooted-field/incoming kernels;16 frame changes for each; period-six tail certificates through length14; rooted-type and minimum incoming-class criterion; mixed reset and adjacent-even covariance witnesses; all16 binary/sign atoms at three incoming ports for no-reset macro factorization and36-edge clock traces; explicit paths and full-state CWM comparisons through seven edges at all four bases; recorded inverse-channel recovery; exact renewal numerator coefficients.

Actual unchanged source calls: cwm_edge369944, cwm_propagate410994, cwm_recoalesce219896; existing contact26394; sourced transition_bit427662 and gauge_action12288. These are assertions and function calls, not independent experiments. The116807-assertion development run preceded stronger package-integrity and renewal-numerator/covariance checks; the final run is not independent replication. An initial streaming-container invocation was rejected before files or tests were created; supported noninteractive execution was used. No earlier scientific suite was replayed as new work.

Run python check_incoming_memory.py using Python3.10+ and the standard library. The package contains the new adapter/checker, unchanged source dependencies, original compact archive, proof, full exact output and hashes. Source publication records this proof and validation frontier, not a claim that every executable attachment byte was also uploaded or formally admitted.

Primary background read at official abstract scope: Lev-Ari et al., Analytical results for the distribution of first return times of non-backtracking random walks on configuration model networks, arXiv:2412.12341v2 (2025), for NB incoming-edge terminology; Jacobi and Goernerup, A dual eigenvector condition for strong lumpability of Markov chains, arXiv:0710.1986v2, for established exact aggregation context. No unread full-paper result supplies the model-specific formulas and no literature-wide novelty is claimed.

Own read-only status request: private bridge3123, status-20261008-euler-incoming-memory-22. Its matching reply was received. No new Source-bound activity, CLAIM, formal Result, independent review or successful final gate was established. Prior failed registration remains unverified provenance. No old rejected prerequisite or safety-blocked payload was retried. No automation or generated-index settings were changed.

Completed increment: continuous return boundary without erasing arrival memory; complete sourced rooted incoming-parity kernels; exact no-reset closure criterion and minimal incoming classes; positive reset/covariance witnesses; NB edge-clock renewal and its uniform phase bound. Remaining native obligation: independently specify which local incidence/field relations permit or exclude immediate retracing and how the contact boundary is realized. This does not infer those laws from the comparison graph. A future changing comparison field must retain the field/incoming joint state; the fixed-field quotient cannot be silently reused.
