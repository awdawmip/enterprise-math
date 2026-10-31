# Four policy labels suffice: exact time-only BRC N=4 minimax theorem

Date: 2026-10-31. Classification: AUTHOR_ANALYTIC_PROOF / EXECUTED_EXACT_INTEGER_CERTIFICATE / UNREVIEWED / NOT_ADMITTED. The theorem is about the stated finite BRC probability model; it does not assert Heartbeat X6 physical dynamics.

## Frozen source model and game

Six typed latent LR cells are AU0, AU1, AV, BU0, BU1, BV. The six distinct conditional prepared rows are

M = (1/20) [
 (10,10,0,0,0,0),
 (9,11,0,0,0,0),
 (0,0,20,0,0,0),
 (0,0,0,10,10,0),
 (0,0,0,2,18,0),
 (0,0,0,0,0,20)
].

They arise from the original strictly positive 16-leaf P/Q laws with a fair future K. AV/BV P/Q rows coincide, giving six rather than eight distinct prepared rows. For both AU and BU, the Q preparation is the equal mixture of its two cell-conditioned laws, while P is a possibly unequal convex mixture. A single lawful causal strategy uses the same time kernel conditional on each latent cell under P and Q.

The public output is time T in {1,2,3,4}, with neither Decision nor BU sensor exposed. Let H range over ALL deterministic lawful S23 stopping tables and, for the stronger upper claim, over any behavioral-randomized lawful S23 extension that preserves its first-stage A/B information restriction. The ex-ante label L(H) has at most m=4 values and cannot see the realized input, latent cell, random coin or observed outcome. Before H is chosen, one common stochastic encoding E with k states is fixed; decoding D_l may depend only on label l. The loss is the maximum over legal H and all six prepared rows of total variation between true time distribution and E D_(L(H)).

R_(k,m) = inf_(E,L,D_1,...,D_m) sup_(H) max_i TV( (M K_H)[i,.], (M E D_(L(H)))[i,.] ).

Equivalently the encoder may be regarded as 6 x k on the latent cells; our upper construction sends every cell to one code. A notation with 6 x k encoded prepared rows gives the same upper and the lower applies to either variant. This distinction is immaterial here because the upper construction ignores the source completely. The lower proof only uses the fact that decoded laws for each fixed prepared source and label cannot depend on H within the label.

## Exact result

For every integer k >= 1,

R_(k,4)(S23 deterministic; T) = 2/3.

The SAME equality holds when all lawful behaviorally randomized causal S23 policies are included, provided their first-stage decision is based only on observed A/B and the subsequent law/latent-cell kernels are shared between P and Q. In particular R_(1,4)=R_(2,4)=R_(3,4)=2/3. All noise parameters 0 <= epsilon <= 1/2 are permitted because the sensor is deleted and this time-only model does not use epsilon.

This upgrades the prior author-side result R_(k,1)=R_(k,2)=R_(k,3)=3/4 and 2/3 <= R_(k,4) <= 3/4. The full-lawful S2 equality is not asserted until the 64 S23 lower witnesses pass an independent S2 causal grammar audit.

## Upper bound: one code state, four policy labels, all randomized laws

Write p_i^H for the four-atom stopping-time law of prepared row i under fixed H, and define the heavy-time set

Hvy(H) = {t in {1,2,3,4}: some i has p_i^H(t) > 2/3}.

We prove |Hvy(H)| <= 3, so at least one time t(H) is non-heavy for every prepared input.

Auxiliary mixed-row lemma: if F0,F1 are arbitrary probability laws and Q=(F0+F1)/2, P=a F0+(1-a) F1 with 0<=a<=1, then P and Q cannot each put strictly more than 2/3 on DIFFERENT atoms. Indeed Q(v)>2/3 implies F0(v)+F1(v)>4/3. For u != v, F0(u)+F1(u)<2/3. Therefore P(u) <= F0(u)+F1(u)<2/3. Also one probability measure cannot have >2/3 on two distinct atoms. Thus the pair (P,Q) together has at most one distinct heavy time. Apply this to each of the AU and BU pairs using the Q equal-mixture weights in M. AV and BV each contribute at most one heavy time.

At stage 1, a lawful policy has only the observable A/B, not the unseen U/V or LR cell or the hidden P/Q preparation. Thus for ALL A-preparations the time-1 probability equals the same r_A, and for ALL B-preparations it equals r_B. This is also true for behavioral randomization, with 0<=r_A,r_B<=1.

If time 1 is NOT heavy, heavy times are confined to {2,3,4}. If time 1 IS heavy for the A group (r_A>2/3), no A-preparation can be heavy at any other time; the B group has only the BU P/Q pair and BV, together contributing at most two OTHER heavy atoms by the mixed-row lemma. The B-heavy case is symmetric; if both A and B are heavy at time 1, there is no other heavy atom. Therefore in all cases |Hvy(H)|<=3.

Select the smallest omitted time t(H) outside Hvy(H), and let L(H)=t(H), one of four ex-ante policy messages. For each l define the fixed decoder distribution q^(l) to be uniform on the other THREE times and zero at l. For each source law p_i^H, p_i^H(l)<=2/3. The elementary inequality

sum_(s != l) min(p_i^H(s),1/3)
  >= min( sum_(s != l) p_i^H(s), 1/3 ) = 1/3

gives

TV(p_i^H,q^(l)) = 1 - sum_(s != l) min(p_i^H(s),1/3) <= 2/3.

Encode all six latent cells deterministically to the SAME code state and ignore the other k-1 states. The label map depends on the publicly specified entire policy H, not its realized random draw or the true source. Thus R_(k,4)<=2/3 for all k>=1, uniformly over lawful randomized causal strategies.

## Lower bound: 64 legal deterministic S23 signatures and an exact finite covering obstruction

The S23 grammar used by the frozen predecessor has 2 stage-one A/B continue bits, 3 stage-two continue bits (AU and BU tied; AV and BV separate), and 6 stage-three LR-history stop bits: 2^2 * 2^3 * 2^6 = 2048 deterministic tables.

Among them, exactly 64 distinct policies-as-signatures make AU0/AU1 and BU0/BU1 stop at the same time, and emit a deterministic four-source signature s=(t_AU,t_AV,t_BU,t_BV). Every such signature has a genuine legal policy witness from the table. The Q-prepared AU,AV,BU,BV inputs therefore yield four point-mass output laws delta_(s_j).

Suppose some common stochastic encoder and four labeled stochastic decoders have uniform TV loss STRICTLY below 2/3. Fix a label l and one of the four prepared inputs j. For every signature s assigned l, the fixed reconstructed distribution q_j^l obeys

TV(delta_(s_j),q_j^l) = 1-q_j^l(s_j)<2/3,

so q_j^l(s_j)>1/3. A four-atom probability vector has AT MOST TWO entries strictly greater than 1/3. Hence signatures assigned l belong to a Cartesian box with at most two allowed times per coordinate j.

There are exactly choose(4,2)^4 = 1296 maximal two-choice boxes. Exhaustive integer enumeration of the explicit 64 signatures proves (i) every box meets them in at most 16 signatures; (ii) exactly nine boxes meet 16 signatures; (iii) NONE of these nine contains signature (1,1,1,1). Four boxes covering 64 signatures would each have to contain exactly 16, yet such boxes collectively miss (1,1,1,1), a contradiction. The finite enumeration is complete over all 1296 two-choice boxes, and is independently reproducible by VERIFY.js. This proves R_(k,4)>=2/3 for every real-valued encoder/decoder and every k>=1: no search grid over stochastic matrices is assumed.

The uniform four-label decoder from the previous section attains the bound. The lower applies equally to the randomized policy family because it contains these 64 deterministic witnesses.

## Executed verification, scope and BRC semantics

VERIFY.js reconstructs BOTH 16-positive-leaf P/Q laws, enumerates all 2048 deterministic S23 bit tables, checks 12,288 exact source/time-decoder TV comparisons, reconstructs 64 signatures, and exhausts all 1296 Cartesian two-choice boxes. It also checks 3072 exact source comparisons for a deterministic set of 512 rational mixtures of two tables. Full randomized universality follows analytically above, NOT from that sample. All comparisons use integers; RUN_EVIDENCE.txt contains the actually executed output.

BRC reuse: the conditional source mixture M and observer/policy family are the typed carrier; time-only output is a declared lossy observer. The four-label result is a bounded minimax approximation, NOT a safe information quotient or a proof of arbitrary future-operation equivalence. It supplies no native Heartbeat X6 spatial-cell embedding, triadic force law or physical-time calibration; P000 and the joint-observer preservation constraint remain intact.

## Source and authority

This proof reuses the lower finite-cover certificate of the prior UNREVIEWED author note, commit eeebd1560f795f2eb964c71ef4eec7bd8c2c1dc6, research_notes/brc_n4_time_policy_2_3_label_saturation_20261031_emr1/PROOF.md. The new contribution is the explicit universal 4-label, 1-state upper construction and consequently full equality for ALL k>=1 (including randomized causal strategies).

Frozen GLOBAL_KNOWLEDGE_V1 canonical main: 31e8f57bcf015f65e370ca0666acfb5129afd0ff; Enterprise Math canonical main input: cd0d692a5510dddcc42991b056ed032933e0b164. Project P000 V5 source blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488 was loaded with ACTIVE worldview and project portable protocol. Authenticated GitHub actor awdawmip. Native research_authority_granted=false and active quota 5/5, current formal owner unconfirmed; no native CLAIM, Result, review or admission is claimed.

Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_EXECUTED / GITHUB_ARTIFACT / UNREVIEWED / NOT_ADMITTED.
