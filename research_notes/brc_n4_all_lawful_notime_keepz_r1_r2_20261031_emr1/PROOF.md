# BRC N=4 — erase stopping time but retain BU sensor: exact all-lawful one- and two-symbol radii

Date: 2026-10-31. Status: **AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Portable continuation of author-side Enterprise Math PR #1757 at immutable predecessor 08b716689211beaaafde39677fdc6b74aa1d44b4. No native task Result, owner CLAIM, independent review or physical X6 claim is implied.

## Precise frozen experiment

The two external laws P and Q each have sixteen strictly positive potential leaves (S,J,K). The provenance S is AU, AV, BU or BV; the latent bit J and independent fair K are binary. Per-K leaf masses with denominator 240 are:

| S | Q: J=0,1 | P: J=0,1 |
|---|---|---|
| AU | 10,10 | 9,11 |
| AV | 20,20 | 5,5 |
| BU | 15,15 | 3,27 |
| BV | 15,15 | 30,30 |

For eight source-prepared inputs (S,B) with B=P or Q, the conditioned J rows are AU_Q=(10,10)/20, AU_P=(9,11)/20; AV_Q=AV_P=(10,10)/20; BU_Q=(10,10)/20, BU_P=(2,18)/20; BV_Q=BV_P=(10,10)/20. K remains fair and independent. These are stipulated finite source preparations, not new native spatial axes.

The same lawful causal policy H acts via a law-independent Markov kernel on each potential (S,J,K), including internal randomization. S2 time-two AU/BU actions agree; S23 also requires equal-likelihood-ratio third-stage histories to share actions (classes AU0, AU1, AV, BU0, BU1, BV). Time-one continuation is used in the witnesses. The public record in **this** problem is Y=(Decision,Z_BU), with stopping time T removed. Z_BU belongs only to BU and includes a visible presence flag: outside BU it equals bottom. For terminal BU at stage 3, Z=J xor Bernoulli(epsilon), with 0<=epsilon<=1/2. For BU stopped at stage 2 before J is revealed, use bottom; the universal upper bound below in fact tolerates **any** law-independent BU-only sensor/early-stop kernel, as long as non-BU always emits bottom. No output leaks T.

The encoder E(c|S,B) uses at most k symbols and is chosen before H; stochastic E is allowed. For each H, stochastic decoder D_H(Y|c) may be chosen but cannot see source labels or the realized J,K. This is distributional reconstruction of Y, not pathwise recovery. Define

~~~text
R_k(F; noT, withZ) = inf_E sup_(H in F) inf_(D_H)
                     max_(S,B) TV(H#L_(S,B), (E D_H)_(S,B))
~~~

for F equal to all lawful S23 or all lawful S2 causal policies. Standard finite probability identity: TV(mu,nu)=1-sum_y min(mu(y),nu(y)).

## Exact theorem

For every real epsilon in [0,1/2], in **each** complete lawful family S23 and S2,

~~~text
R_1(F; noT, withZ; epsilon) = 2/3
R_2(F; noT, withZ; epsilon) = 1/2.
~~~

In particular the previously open one-code interval 2/3 <= R_1 <= 3/4 closes **at 2/3**, not at the complete-observer value 3/4. The upper bound makes no assumption that stage-two BU emits a bit; only BU exclusivity of Z and law-independent H are needed.

## Exact one-symbol upper bound: BU-only submeasure + two unsensed decision atoms

Let nu_BU on full (S,J,K) be supported on S=BU, have J distribution (1/5,4/5), and independent fair K. For each BU preparation L_(BU,B),

~~~text
(1/3)nu_BU <= L_(BU,B)  pointwise as finite measures, B=P,Q.
~~~

Indeed, on J=0 the left mass is 1/15, smaller than min(1/10,1/2); on J=1 it is 4/15, smaller than min(9/10,1/2). Attaching common fair K preserves each inequality. Positivity of Markov kernels preserves measure domination, hence (1/3)H#nu_BU <= H#L_(BU,B) for **every** lawful H, regardless of its randomization, BU early stopping, dependence on observed J, T4 continuation or epsilon.

For each policy H construct a single probability decoder row on Y:

~~~text
r_H = (1/3)delta_(P,bottom) + (1/3)delta_(Q,bottom) + (1/3)H#nu_BU.
~~~

The two delta atoms are syntactically valid public records. If an implementation requires decoder support inside the actual H-feasible output set, any impossible unsensed decision atom can transfer its 1/3 mass to the other unsensed atom; non-BU inputs are then supported there, and the same guarantee holds.

For BU inputs, their true Y law contains (1/3)H#nu_BU as a submeasure, so its overlap with r_H is at least 1/3 and TV is at most 2/3. For any non-BU input, Z is always bottom, so its Y law is p delta_(P,bottom)+(1-p)delta_(Q,bottom), for some p in [0,1]. Since r_H assigns at least 1/3 to **each** of these atoms,

~~~text
sum_y min(mu(y),r_H(y)) >= min(p,1/3)+min(1-p,1/3) >= 1/3.
~~~

Thus TV<=2/3 simultaneously on all eight inputs. The encoder is the one-symbol constant encoder, so R_1 <=2/3 for all S2/S23 policies and every real epsilon.

This is a **general tagged-observer domination lemma**: two unsensed decision atoms plus one source-exclusive tagged observation family admit a three-part common decoder if one-third of a reference tagged-source law is dominated by every tagged-source preparation. It depends on the scored observer alphabet, not on erasing provenance from the underlying carrier.

## Exact one-symbol lower bound: lawful H*

Use the already-defined lawful S23 witness H* (also S2): at time 2 stop AV with Decision Q, and continue AU,BU,BV; at time 3 terminate AU and BU with Decision P, and BV with Decision Q. On all potentially active J histories, same-ratio third-stage actions agree; AU/BU time-two action kernels agree. BU at time 3 emits its noisy sensor, always *present*, for all epsilon in [0,1/2].

Three prepared inputs have pairwise disjoint public Y supports:

~~~text
AU_Q -> {(P,bottom)}.
AV_Q -> {(Q,bottom)}.
BU_Q -> {(P,0),(P,1)}.
~~~

For any probability row r, its total mass across these disjoint supports is at most 1. Thus on one of the three inputs its overlap is at most 1/3 and TV at least 2/3. This holds for any common decoder and all epsilon. Combine with the explicit upper bound to give R_1=2/3.

## Two-symbol exact value

H* supplies three disjoint public support blocks. If an arbitrary two-symbol stochastic encoder plus decoder attained TV<1/2 on all three, each corresponding reconstructed law would assign >1/2 probability to its own block. For each input at least one of two decoder rows must assign >1/2 to that block. A single probability decoder row cannot do this for two disjoint blocks, contradicting three inputs and two rows. Therefore R_2>=1/2.

For the upper bound, reuse the verified positive-rational full-path reference measures from the predecessor no-Z result, before observer projection:

~~~text
F_L: AU0=19/80, AU1=21/80, AV0=1/4, AV1=1/4.
F_R: BU0=1/10, BU1=2/5, BV0=1/4, BV1=1/4.
~~~

All other entries are zero; attach fair K. Map AU and AV preparations deterministically to code L, and BU and BV to code R. For every one of the eight input laws, overlap with its corresponding F reference equals 1/2 by coordinatewise comparison on its own S-fiber. Hence TV(L_(S,B),F_group)=1/2. For every lawful H, define decoder D_H(.|L)=H#F_L and D_H(.|R)=H#F_R, then remove T but keep Z; data processing under the **same** kernel gives TV<=1/2. The support packing lemma and construction match: R_2=1/2.

## Validation and scope

VERIFY.js uses exact integers only; it reconstructs all 16 positive source leaves for each of P and Q, verifies the BU one-third domination and eight exact F-group overlaps, checks the three H* disjoint public supports, and enumerates 27 lawful time-two deterministic action patterns times 64 S23-consistent time-three deterministic decision patterns. Across four exact epsilon values (0,1/8,1/4,1/2) and eight prepared inputs it checks both one- and two-code full six-atom Y distributions: **110,592 exact TV comparisons**. Maxima are exactly 2/3 and 1/2. For this exhaustive **stated deterministic subfamily** stage 1 always continues and all time-three survivors stop. S2's larger language, internal stochastic actions, T4 continuation and the epsilon continuum are covered by the analytic domination, disjoint-support and data-processing arguments, not by finite enumeration.

This is an author-side finite statistical experiment within a restricted BRC provenance-path model; no native P000 six-axis Cell transition, true physical heartbeat evolution or experimentally calibrated sensor follows. The general total-variation identities and data processing are classical; mathematical novelty, if any, is the exact typed application to this frozen lawful observer problem, not a claim to invent the underlying probability method. Independent mathematical review and native Source admission remain outstanding.
