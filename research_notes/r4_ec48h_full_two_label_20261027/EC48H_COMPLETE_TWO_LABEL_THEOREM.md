# EC48H — Complete two-label BRC ROC preservation: convex-hull capacity = seedless capacity

**Date:** 2026-10-27. **Status:** AUTHOR-SIDE PROOF / FINITE EXACT VALIDATION; NOT NATIVE RESULT, DRIVER ACCEPTANCE, WORKING TRUTH, OR FOUNDATION.

## 1. Source, continuation, and scientific scope

Latest checked predecessor: EC48G, immutable proof at [fef0cd38](https://github.com/awdawmip/enterprise-math/blob/fef0cd38d2f715b3e6fdfd83df9986dda5116165/research_notes/r4_ec48g_k2_y2_20261027/EC48G_TWO_LABEL_K2_THEOREM.md). EC48G proved equality for two future labels when K_hull<=2 and left the K_hull=3 boundary open. This work resolves that boundary, then combines it with the four-corner trivial construction.

Verified current GLOBAL_KNOWLEDGE_V1 main snapshot: 968db47fa025cb6727542a945fdd54890f95dd78. Read the canonical 00_BOOTSTRAP.md, OPERATING_MANUAL.md, the Enterprise Math project/task router, P000_REALITY_FOUNDATION.json (Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matching P000_STARTUP.json), ACTIVE 我眼中的世界.md, MATH_RESEARCH_POLICY, and BRC research priority. EM source/control read pinned to ee5577fbae5b505a868d917bf5f93d580a24b6ed, including docs/PORTABLE_RESEARCH_PROTOCOL.md and current_control_authority.json.

Model: an auxiliary positive-source, finite, two-stage, binary-hypothesis BRC observation experiment. Its two future labels are *not* two native spatial axes, and the kernel is neither signed amplitudes nor a native Heartbeat/X6 propagator. P000 native six-dimensional Cell space, three-dimensional slice, and separate time remain unchanged. Claims apply only to the explicitly defined source observer.

## 2. Exact model and complete theorem

Let H be any nonempty finite set of source-provenance histories and Y={1,2}. Positive joint laws p(h,y),q(h,y) each sum to one. After h, a private-randomized encoder chooses m in {1,...,K} according to π_h(m). On observing y, a decoder outputs hypothesis P with probability u_m(y)∈[0,1]. No persistent shared random seed is carried between decisions. Put

\[
w(h,y)=\sum_{m=1}^{K}\pi_h(m)u_m(y),\qquad
(\alpha,\beta)=\sum_{h,y}(p(h,y),q(h,y))w(h,y).
\]

Let S_K denote achievable pairs and let Z=Σ_(h,y)[0,(p(h,y),q(h,y))] be the complete-history zonotope. The corresponding fixed-depth four observation vector is (1−α,β,2,2). Define K_hull=min{K:conv(S_K)=Z} and K_seed=min{K:S_K=Z}.

**Theorem EC48H.1.** For every such strictly positive finite two-future-label experiment, even with arbitrarily many exact cross-history or cross-column likelihood-ratio collisions,

\[
\boxed{K_{\rm seed}=K_{\rm hull}.}
\]

Consequently **for |Y|=2**, conv(S_K)=Z implies S_K=Z for every integer K>=1. Neither theorem asserts the corresponding implication for three or more future labels.

## 3. New three-decoder Boolean-square lemma

**Lemma EC48H.2.** Suppose each h has endpoint binary words b_h≤a_h coordinatewise in {00,10,01,11}. If B={b_h} and A={a_h} each have at most THREE distinct words, then there exists a piecewise continuous, coordinatewise nondecreasing readout path w_t(h)∈[b_h,a_h] from b to a. Every member factors through at most THREE private-memory decoder states.

Use corners v0=(0,0), v1=(1,0), v2=(0,1), v3=(1,1).

### 3.1 Endpoint bank padding

Enlarge B,A to THREE-corner sets B',A', permitting unused dummy endpoint corners, such that every lower bank corner admits an upper bank corner and conversely. Four exhaustive cases establish existence:

* If v3∉B and v0∉A, choose B'={v0,v1,v2}, A'={v1,v2,v3}.
* If v3∈B and v0∉A, then v3∈A. Choose A'={v1,v2,v3}; pad B to three, including v0 whenever possible. Otherwise B'={v1,v2,v3}. Both options have required comparabilities.
* If v3∉B and v0∈A, then v0∈B. Dually choose B'={v0,v1,v2}; pad A including v3 whenever possible, otherwise A'={v0,v1,v2}.
* If v3∈B and v0∈A, positivity of the Boolean order forces v0,v3 into BOTH B and A. Pad each to three arbitrarily.

Let i be the unique corner missing in B', j the corner missing in A'. Only ELEVEN ordered cases are possible:

(0,0), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2), (3,0), (3,1), (3,2), (3,3).

The remaining five (0,1),(0,2),(0,3),(1,3),(2,3) are impossible: they contain an upper v0 without lower v0, or lower v3 without upper v3.

### 3.2 Exhaustive constructive case table

Start with three decoders at the corners in B'; each history initially uses its b_h decoder with probability one. The allowed operations are (a) change one or several histories' *private encoder distributions* linearly while holding decoders fixed; (b) slide one decoder along a straight coordinatewise monotone segment while holding encoders fixed; and (c) reset an unused decoder to another corner (no readout change). The full case algorithm is:

**Case i=j (4 cases):** The banks coincide. Keep all decoders at these three corners and privately interpolate every history between its actual lower and upper corner. Their coordinatewise order guarantees monotonicity.

**Cases (1,0),(2,0):** Every history initially at v0 whose upper corner is not vi may privately finish at that upper corner, which is already in B'. The only histories still using decoder v0 have transition v0→vi. Slide this one decoder to vi, then privately finish all remaining histories at their actual upper corners, now in the decoder bank.

**Cases (1,2),(2,1):** The corner vj has disappeared from the upper bank. Every history starting there necessarily ends at v3. Privately move all these histories onto the already present v3 decoder, then reset the unused vj decoder to vi and privately finish all other histories. Throughout, outputs increase and lie within their individual [b_h,a_h] boxes.

**Cases (3,1),(3,2):** Again all histories at vj necessarily end at v3. Slide the vj decoder continuously to v3; the other two corner decoders stay fixed. Then privately finish all remaining histories with the three correct upper-corner decoders.

**Hard case (3,0):** B'={v0,v1,v2}, A'={v1,v2,v3}. First move every history starting at v0: those targeting v1 or v2 finish there; those targeting v3 move privately to the midpoint (v1+v2)/2=(1/2,1/2), represented by equal weights on the v1 and v2 decoders. All these intermediate values are within [v0,a_h] and are ≥v0. Decoder v0 is now unused, so reset it to v3. Finally privately interpolate remaining histories to their true a_h, including midpoint→v3. Each stage is coordinatewise nondecreasing; no fourth decoder or persistent shared seed is used.

In every line of the table all stages have affine readout in their stage parameter s∈[0,1]; checking that each row's endpoints satisfy b_h≤old≤new≤a_h proves the entire stage remains in the support-face box. Unused-decoder reset changes no readout. Concatenating the stages yields the claimed path. **QED Lemma EC48H.2.**

## 4. Proof of Theorem EC48H.1

For any critical likelihood-ratio threshold r>0 let d_r(h,y)=p(h,y)−r q(h,y). The complete-history support maximizer for α−rβ chooses 1 at strictly positive d_r and 0 at strictly negative d_r; tied cells admit any probability [0,1]. Define endpoint words

\[
b_h(y)={\bf1}_{d_r(h,y)>0},\qquad
a_h(y)={\bf1}_{d_r(h,y)\ge0}.
\]

The EC47/EC48A threshold-signature/hull theorem gives |B|,|A|≤K_hull: B and A are the strict sign profiles on the two sides of r. If K_hull=3, apply EC48H.2. Its three-memory path fixes the strictly signed cells, and all tied-cell decision probabilities increase continuously from 0 to 1. Therefore

\[
T(t)=\sum_{d_r(h,y)=0}q(h,y)w_t(h,y)
\]

runs through the entire interval [0,Q_r], Q_r=Σ_(d_r=0)q(h,y). Tied generators have common positive slope r, so the entire exposed zonotope support edge is achieved by THREE-memory observers. Complementing decoders implements the antipodal edge. Noncritical support vertices are implemented by at most three strict-sign words. Thus ∂Z⊆S_3. Scaling all decoder probabilities by c∈[0,1] proves S_3 is star-shaped about 0, and every z∈Z lies on a radial segment from 0 to ∂Z; hence S_3=Z.

When K_hull=1 or 2, the already checked EC48G two-label construction yields K_seed=K_hull. If K_hull=4, every target history-conditioned pair (x_h,y_h)∈[0,1]^2 is realized by FOUR fixed corner decoders v0,v1,v2,v3: after observing h, the private encoder chooses the corners with probabilities (1−x)(1−y), x(1−y), (1−x)y, xy, respectively. This realizes both terminal marginal decisions exactly, without maintaining a shared random seed. So K_seed≤4=K_hull. Finally K_hull≤4 automatically, as there are only four possible strict-sign words, and K_seed≥K_hull always. All cases establish the theorem. **QED.**

Inherited inputs EC47/EC48A and EC48G remain AUTHOR-SIDE checked sources rather than independent Driver accepted theorems. The new three-bank lemma and its exhaustive elementary case proof are fully specified above. A review defect in an inherited claim would require reopening only its dependent assertion, not rewriting P000.

## 5. Exact positive cross-history collision example

Take five histories, two future labels and strictly positive integer arrays, each total mass 20:

\[
P_{\rm raw}=
\begin{pmatrix}
1&2\\2&1\\2&3\\3&2\\2&2
\end{pmatrix},
\quad
Q_{\rm raw}=
\begin{pmatrix}
2&2\\2&2\\2&2\\2&2\\2&2
\end{pmatrix},
\quad p=P_{\rm raw}/20,\ q=Q_{\rm raw}/20.
\]

Likelihood ratios are 1/2,1,3/2. The numbers of strict-sign history profiles across the four noncritical threshold intervals are 1,3,3,1. Hence K_hull=3. At r=1 the five lower words are (00,00,01,10,00) and upper words (01,10,11,11,11), with ties distributed across multiple histories in BOTH future columns, including a history tied in both. The optimal support value is α−β=1/10, and the support edge has β∈[1/5,4/5].

**Stage I:** use decoder states d0=00,d1=10,d2=01, parameter s∈[0,1], and five history readout rows

\[
W_I(s)=\begin{pmatrix}0&s\\s&0\\0&1\\1&0\\s/2&s/2\end{pmatrix}.
\]

The final history privately draws decoder 0,1,2 with probabilities (1−s,s/2,s/2), respectively. Stage I satisfies β=1/5+3s/10 and α−β=1/10.

**Stage II:** after decoder 0 becomes unused reset it to d0=11, retaining d1=10,d2=01, and use readouts

\[
W_{II}(s)=\begin{pmatrix}0&1\\1&0\\s&1\\1&s\\(1+s)/2&(1+s)/2\end{pmatrix}.
\]

The final history privately chooses decoders (d1,d2,d0) with probabilities ((1−s)/2,(1−s)/2,s); histories 3,4 interpolate to 11. Here β=1/2+3s/10 and α−β=1/10. These paths meet exactly at β=1/2, cover the full support edge and use three decoder states throughout.

## 6. Actual exact evidence and boundary

[EC48H_VERIFY.js](EC48H_VERIFY.js) was executed *before publication* and its identical source was read back from immutable GitHub. It enumerates ALL 2^9−1=511 nonempty subsets of the nine possible comparable Boolean-corner endpoint pairs, including patterns not necessarily realized by particular normalized probability matrices. Of these, 291 have at most three distinct lower and three distinct upper corners; 220 lie outside the lemma domain. The executed checker verifies compatible three-bank padding and affine endpoints for the full constructive table: **667 stages and 4,964 coordinate inequalities, PASS**. It additionally verifies eight dyadic rational support-face values of the explicit positive five-history witness. Arithmetic values used by the endpoint checker belong to {0,1/2,1} and its dyadic convex combinations, exactly representable in the JavaScript binary numeric format; continuum coverage rests on the affine-stage algebraic proof, not finite samples. An independent Python fractions.Fraction checker of the same 511 configurations and eight rational witness samples also passed in the available local execution environment. [Structured report](EC48H_REPORT.json).

No claim is made for |Y|>=3, microscopic kernel preservation, variable stopping depths, native heartbeat evolution, independent Driver assessment, or formal/proof-assistant verification. Existing provenance and branch multiplicities remain distinguishable in the declared observation model. BRC semantics applied: EC47 sign-profile observer audit, EC48A threshold sweep, EC48B/C support-face reasoning, and EC48G memory-bank interpolation.

## 7. Next independent question EC48I

The unresolved area is **|Y|>=3**. First classify K_hull=2 for three future labels and multiple simultaneous cross-history/column ties. Either derive a finite decoder-bank interpolation theorem or give normalized positive rational P,Q,K,r with all EC48C optimal-encoder connected component source-mass intervals and an exact uncovered rational gap. Prove every claimed finite search boundary and retain actual author/reviewer status. Do not treat closure of the two-label auxiliary observer theorem as a native X6 physics result.

**Activity:** RA-EMR4-20261027-EC48H-Y2-LOCAL0713; local author-side Researcher-ID EM-R004-EC48H-20261027-LOCAL. GitHub identity awdawmip/push verified. Native owner read returned CONTROL_QUOTA, while native session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false); no verified live Owner/CLAIM, Source execution Result, independent Driver review, or Foundation mathematical acceptance.
