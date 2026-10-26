# EC48E — Single-column critical ties imply exact seedless BRC observation-region preservation

**Claim scope:** Author-side proved mathematical theorem for strictly positive, finite, separately normalized rational source laws; finite exact numerical checks. Not a native Result, independent Driver-accepted theorem, Working Truth, Foundation or native X6/Heartbeat dynamic law. Date 2026-10-27.

**Fixed source pins:** GLOBAL_KNOWLEDGE_V1 main 3e3fac26dc5e8d176f31e6aefbc706157315e456; Enterprise Math control main at research read ad928e16207ae4c8d62035d4b62e7e6606755925. Source dependencies EC48C d582d2bd1487446008648fe9da1fae63d2c86b9c, EC48D 6b320868bc664072b722ed32bfa0dc87660c68a6; read P000, ACTIVE worldview, AGENTS, joint-observer-preservation and portable protocol. Authenticated connected GitHub actor: awdawmip. Native owner query returned CONTROL_QUOTA: no live owner or formal CLAIM established.

## 1. Declared positive BRC source-readout model

Let H denote finitely many history labels observed at t0 and Y finitely many later future labels observed at t1 > t0. Let p(h,y)>0 and q(h,y)>0 be two separately normalized rational joint laws preserving history and future-label provenance. The observer encodes h using a stochastic K-state private encoder pi(m|h); after observing y, a decoder chooses hypothesis P with probability u(m,y) in [0,1]. There is no persistent policy-selection/public random seed. Induced terminal choices and two readouts are

    w(h,y) = sum_m pi(m|h) u(m,y)
    alpha = sum_(h,y) p(h,y) w(h,y)
    beta  = sum_(h,y) q(h,y) w(h,y).

Let S_K be the set of feasible (alpha,beta). With full history the attainable region is the zonotope

    Z = { (sum p(h,y)w(h,y),sum q(h,y)w(h,y)): 0<=w(h,y)<=1 }.

The fixed-depth four-coordinate lift is (e_P,e_Q,t_P,t_Q)=(1-alpha,beta,2,2). Define K_hull as the least K with conv(S_K)=Z; K_seed as the least K with S_K=Z. By EC48A/EC47, K_hull is the maximum number of distinct binary strict-sign history profiles over generic likelihood-ratio thresholds. EC48D showed K_hull <= K_seed <= min(|H|,2K_hull).

These auxiliary finite history/label alphabets are not native spatial dimensions. A claim of native six-axis Cell or Heartbeat dynamics would additionally require a typed X6 source path embedding/readout, admissible future operation class, relation/provenance preservation and actual native evidence. No such transfer is made.

## 2. The single-tied-column face theorem

For positive lambda define gain d_lambda(h,y)=p(h,y)-lambda q(h,y), tied set T_lambda={(h,y):d_lambda(h,y)=0}, and two binary history signatures

    a_lambda(h)[y] = 1[d_lambda(h,y)>=0]   (ties as one)
    b_lambda(h)[y] = 1[d_lambda(h,y)> 0]   (ties as zero).

Write A_lambda,B_lambda for the sets of distinct history signatures and L=|A_lambda|, R=|B_lambda|. They are precisely the left and right generic sign profiles adjacent to lambda, so L,R <= K_hull.

**Theorem EC48E.1 (complete exposed-face realization):** If T_lambda is nonempty and all its pairs have the same future label y_star, the entire full-history support face

    F_lambda = { z in Z: alpha(z)-lambda beta(z)=sum_(h,y) max(d_lambda(h,y),0) }

lies in S_max(L,R). The proof explicitly builds a piecewise-continuous family of seedless policies using at most max(L,R) memory labels; it applies to any positive rational tie masses, including repeated ratios across histories in the same y_star column.

**Proof.** At every y other than y_star, all d_lambda are strictly signed. Define c(h) as the vector of forced binary positive/negative decisions in those |Y|-1 columns, and partition H into classes C with identical c. Each class gets its own memory labels with forced decoder bits c outside y_star. Since the c-vectors differ, their required decoder words cannot coincide and memory counts across classes sum.

Within a class C, record whether history signs at y_star include any P (strictly positive), N (strictly negative) and T (tied). Every tied history in a class is assigned a common declaration probability s_C in [0,1] at y_star. Class-by-class the following exact policies exist:

(A) Both strict P and strict N present: two decoder labels with y_star bits 1 and 0; strict histories deterministically use their sign label and tied histories privately encode into the labels with probabilities s_C and 1-s_C. Two labels remain necessary and sufficient for all s_C, even if T is absent.

(B) P and T present, N absent: positive histories use decoder bit 1; tied histories use another decoder bit s_C. When s_C=1 the two decoders coalesce, hence the label count equals one at s_C=1 and two for 0<=s_C<1.

(C) N and T present, P absent: negative histories use bit 0; tied histories use another bit s_C. At s_C=0 the two decoders coalesce, hence the label count equals two for 0<s_C<=1 and one at s_C=0.

(D) Only T present: a single decoder bit s_C suffices. With no ties, one decoder suffices for the sole strict sign and two for both P and N.

These cases exhaust the sign patterns. All decoder labels in a class carry the same mandatory c, so strict gains remain maximized. Arbitrary s_C affect only tie entries and hence do not change alpha-lambda beta. The induced choices are exactly factored as private memory encoding followed by future-label decoding. No persistent common random seed is used.

Begin with every s_C=1. This realizes the full-history all-ties-one endpoint with exactly L labels: the decoder words are the distinct a_lambda signatures. First, decrease to zero the s_C of every type (C) class (memory releases), one class at a time. Next vary all constant-size classes (A)/(D), and finally decrease s_C for all type (B) classes (memory consumers), one class at a time. The initial count is L and the final count is R. If D is the number of releasing classes and U the number of consuming classes, intermediate counts start at L, decrease by D, and then increase by U to R=L-D+U. The maximum on this path is thus max(L,R). Unused labels may be padded. At a decoder collision the resource representation may change discontinuously but the observable probabilities vary continuously.

For classes with ties let Q_C=sum_{h in C:(h,y_star) tied}q(h,y_star)>0. On the constructed path, the total tied q-mass chosen as P is t=sum_C Q_C s_C; it varies continuously and nonincreasingly from Q_lambda=sum_C Q_C to 0. Thus it attains every t in [0,Q_lambda]. Along a support face, all tied generators have the same slope lambda and all nontied choices are forced, so

    (alpha,beta) = (alpha_0+lambda t, beta_0+t).

Every point of F_lambda is therefore on the constructed path and has a valid max(L,R)-state seedless realization. QED.

## 3. Global equality on all cross-column noncollision models

**Theorem EC48E.2 (generic equality):** If

    p(h,y)/q(h,y) != p(k,z)/q(k,z) whenever y != z,

then K_seed=K_hull for the full pair ROC region. Ratios may repeat for multiple histories inside a fixed future-label column.

**Proof.** Every critical ratio lambda has ties only in a single future-label column. Theorem EC48E.1 realizes every point of that support face using at most max(|A_lambda|,|B_lambda|)<=K_hull states. At generic noncritical slopes, the support maximizer is a single zonotope vertex obtained from strict sign profiles, also using at most K_hull states.

Every nontrivial boundary edge of the planar zonotope generated by positive vectors (p(h,y),q(h,y)) is exposed by a normal (1,-lambda) or its negative, lambda>0. The latter edges arise by decoder complementation u->1-u, preserving memory count; extremal vertices (0,0),(1,1) are trivially attainable. Hence every point on the boundary of Z is in S_Khull.

S_K is star-shaped about (0,0): replacing every decoder probability u(m,y) with c u(m,y), 0<=c<=1, realizes c(alpha,beta) without adding memory. Since Z is convex and contains the origin, every point in Z lies on a segment from the origin to a point of its boundary. Boundary coverage and star-shapedness imply S_Khull=Z. Since S_K subseteq Z always, we conclude K_seed<=K_hull; the reverse inequality follows directly from convexification. QED.

**Corollary EC48E.3 (necessary algebraic counterexample locus):** If K_seed>K_hull, then at least two ties at the same likelihood ratio occur in distinct columns, i.e., there exist (h,y),(k,z) with y!=z such that

    p(h,y) q(k,z) = p(k,z) q(h,y).

This is a necessary condition, not a sufficient condition for failure. The finitely many cross-column equalities define proper polynomial hypersurfaces of the strictly positive separately normalized p,q parameter manifold. Their union has relative Lebesgue measure zero; the complementary generic models are relatively open and dense, with rational models dense therein. This does not resolve equality on the collision locus.

## 4. Constructive rational witness improving the earlier two-bank resource certificate

Take H=4 and Y=2, with unnormalized integer masses

    P_raw = [[30,70],[30,50],[90,20],[90,50]];
    Q_raw = [[1,1],[1,1],[1,1],[1,1]].

Normalize p=P_raw/430 and q=Q_raw/8. The critical raw ratio 50 corresponds to normalized lambda=40/43, tied cells (h_1,y_1),(h_3,y_1). Its left signature set is A={(0,1),(1,0),(1,1)} and right set B={(0,1),(0,0),(1,0)}. Thus L=R=3 while the fixed two-bank union |A union B|=4. A complete open-interval raw-ratio scan gives signature peak K_hull=3 with counts 1,2,3,3,2,1.

For the face at lambda=40/43 the exposed maximum is alpha-lambda beta=10/43 and its exact parametrization is

    alpha=25/43+(40/43)t; beta=3/8+t; 0<=t<=1/4.

First vary the tied h_3 entry from 1 to 0 with h_1 held at 1, releasing one memory label; that covers t in [1/8,1/4]. Then vary tied h_1 from 1 to 0 holding h_3 at 0, consuming one label; that covers t in [0,1/8]. Three memory labels suffice at every intermediate policy. This is a *strict improvement of EC48D's construction bound* four to three, not a counterexample to K_seed=K_hull.

## 5. Independent reproducibility, scope of validation and next obligation

Executed exact Fraction checker: 49,920 H=4,Y=3 single-tie-column sign templates; 146,280 path stages; 1,755,360 exact cell checks; 864 cases combine release and expansion. Fixed-seed nonuniform H=8,Y=4 positive rational instances: 250 models, 4,593 distinct threshold faces, 13,216 path stages, 422,912 exact cell checks. Separate executed BigInt checker confirms the explicit H=4,Y=2 witness, support equality, signatures, three-state factorization. Local executed reports EC48E_REPORT.json and EC48E_BIGINT_REPORT.json contain all counts. These finite checks support implementation but the general theorem rests on the displayed constructive proof, not sampling.

Applied method: REUSE_APPLIED on EC47–EC48D strict sign profiles and the EC48B/C face optimization; EXTEND_EXISTING_TOOL for exact conditional stochastic encoder validation. Positive BRC source provenance and both hypothesis masses retained. There is no signed/phase cancellation analysis, native-X6 heartbeat computation, independent mathematical peer review or formal Lean certificate.

**Open EC48F:** What happens at *simultaneous cross-column ties*? Search deliberately on the collision locus with H>=8,Y>=4,K>=3, nonuniform positive rational laws; compute exact EC48C encoder components and uncovered rational intervals if any, or prove a multi-column reconfiguration law. For a counterexample record P,Q, lambda, K_hull, every component interval and an exact missing open interval. If not proved, the global equality question remains OPEN. Variable decision depths and transfer to native X6 are separate outstanding obligations.
