# R749SA — Exact eight-to-one signed-Port quotient, two-layer source residual and observer spectrum

Date: 2026-11-12. Status: AUTHOR-PROVED / FINITE EXACTLY CHECKED / UNREVIEWED. Researcher EM-DIRECT-9F7D25, Activity RA-D46184D9060689BCC1124235. Continuation within R749S PR #2170; TASK RS-X6-TRIADIC-CLOSURE-DYNAMICS remains with its separate active owner. The output is a finite observer theorem, not a native Cell/Link/Port transition authorization.

Frozen input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 triadic and native six-axis source); R749N predecessor @e8c5c874aca5b7098acfdbaf8fadb8ad64a1506f; R749S same PR.

## Carrier and exact quotient

Use R749S's 60-vertex signed-Port graph G, directed-edge carrier D of size 960, deterministic signed C1 successor f(u,v)=u△v, and noisy kernel P_p=pR+(1-p)A on D.

Let U be the 15 unordered pairs of *unsigned axes* {i,j} with i≠j in {0,...,5}. Define π:V→U by forgetting Port signs only, and Π:D→D_U by Π(u,v)=(π(u),π(v)). The unsigned adjacency graph G_U is the triangular graph T(6): each support pair has eight unsigned neighbors, and its directed-edge set D_U has size 15×8=120. Every directed unsigned edge has exactly eight distinct signed lifts: assign a sign independently to the three named axes in the two overlapping supports, subject to the common Port sign being shared. This gives an exact 8:1 carrier projection.

For unsigned adjacent supports A,B, the distinguished successor is f_U(A,B)=A△B. Define Q_p on D_U as the noisy model with deterministic f_U and uniform resampling among the eight neighbors of the current support.

## Theorem 1 — Strong lumpability for all p

For every signed directed state (u,v) with Π(u,v)=(A,B) and every unsigned outgoing support C~B,

 Pr_{P_p}[π(Z_next)=C | (u,v)]
  = (1+7p)/8   if C=f_U(A,B),
  = (1-p)/8    otherwise.

Consequently Π intertwines the full signed Markov kernel P_p with the unsigned 120-state kernel Q_p for all p∈[0,1], for every initial signed law (with push-forward to unsigned initial law), not merely in stationarity. In operator language P_p(L_U g)=L_U(Q_p g), where (L_U g)(u,v)=g(Π(u,v)).

Proof. The sixteen signed neighbors of current v group into eight unsigned successor supports, each with exactly two signed representatives. Of the sixteen, one is the original signed-source forced successor f(u,v). Its unsigned support equals f_U(A,B). The second signed representative at that same unsigned support is a nonforced transition. The remaining fourteen signed neighbors project two-to-one onto the other seven unsigned successors. Summing exact probabilities q=(1+15p)/16 and r=(1-p)/16 gives q+r=(1+7p)/8 for C=f_U and 2r=(1-p)/8 elsewhere; this depends only on the projected pair. The exact Markov intertwining follows from the strong-lumpability criterion.

This safe quotient is explicitly scoped: it preserves *all future unsigned axis-support path events* under the specified P_p transition family. It intentionally forgets signed-Port identity and is not valid for future observers that query the discarded signed labels or BRC branches.

## Theorem 2 — Exact joint residual splitting and sufficient statistics

At each step of the signed chain classify the transition by its actual signed source into three mutually exclusive types:
 S: the exact signed forced successor (probability q=(1+15p)/16);
 U: the unsigned forced support but the *opposite signed lift* (probability r=(1-p)/16);
 O: one of the fourteen alternatives with different unsigned successor support (probability 14r=7(1-p)/8).

The conditional probabilities (q,r,14r) are independent of the current signed edge and all preceding history. Thus these three step-labels are iid, even though the signed-Port state process generally has order two. For a path of n≥2 vertices, m=n−2 transitions, let K_S count exact signed C1 completions and K_U count unsigned C1 completions. Then

 (K_S, K_U−K_S, m−K_U) ~ Multinomial(m; q,r,14r).

The unsigned completion statistic has
 K_U ~ Binomial(m,(1+7p)/8).

The entire unsigned n-block likelihood is
 Pr_p(A_0,...,A_(n−1))
   = (1/120) q_U^{K_U} r_U^{m−K_U}
with q_U=(1+7p)/8 and r_U=(1-p)/8, under the uniform initial signed-edge law (hence uniform 120-state unsigned edge).

For all p>0 and fixed current unsigned support B, the eight possible preceding support neighbors A have distinct next-support distributions, so precisely three fixed-length historical bits are necessary and sufficient to predict future unsigned supports exactly; at p=0 the unsigned support process becomes first-order Markov. By comparison R749N established four historical bits for full signed-Port prediction at p>0. This is an observer-dependent minimality result.

Conditional on an unsigned C1 completion being observed, its probability of also preserving the *signed* C1 source is q/(q+r)=(1+15p)/(2+14p), which equals 1/2 at p=0 and 1 at p=1. This quantifies the residual erased by the unsigned quotient.

## Theorem 3 — Exact spectral factorization of the quotient

Let the cubic F_h(λ;p)=λ³−p²−(1−p)h λ(λ+p) be as in R749S. The normalized unsigned T(6) adjacency has eigenvalues 1 (multiplicity 1), 1/4 (5), −1/4 (9). Its 120 directed-edge states split under pure unsigned C1 into 40 three-cycles. Applying the same rank-15 resolvent determinant argument as R749S gives

 det(λI_120−Q_p)
 = (λ³−p³)^25 F_1(λ;p) F_(1/4)(λ;p)^5 F_(-1/4)(λ;p)^9.

It divides the R749S signed characteristic polynomial *exactly*, and the discarded signed sector has the complementary polynomial

 det(λI_960−P_p)/det(λI_120−Q_p)
 = (λ³−p³)^235 F_(1/2)(λ;p)^6 F_0(λ;p)^15 F_(-1/8)(λ;p)^24.

Thus the observer projection has an explicit 840-dimensional invariant information-loss sector. The eigenvalue factorization describes linear dynamics, whereas the sign/source semantics of that sector are specified by Theorems 1 and 2.

## Theorem 4 — Coarse loop return is still provenance-multiple

For adjacent unsigned supports A={i,j}, B={j,k}, the common unsigned neighbors are f_U(A,B)={i,k} and the three supports {j,l} for l outside {i,j,k}. Consequently, a three-step return to the same unsigned directed edge has probability q_U³+3r_U³, with conditional probability q_U³/(q_U³+3r_U³) of using the true unsigned C1 completion. At p=1/2, q_U=9/16 and r_U=1/16, so this conditional probability is 243/244. The fully signed-return posterior in R749S is 4913/4919 under its finer observation. Their different denominators arise from distinct observer events, not contradictory estimates.

## Verification and next question

The companion exact checker R749SA_UNSIGNED_OBSERVER_LUMPABILITY_CHECK.py constructs both carriers, verifies all 960 signed outgoing transition partitions (one S, one U, fourteen O), counts all eight lifts for each unsigned directed edge, exhausts the 120×8²=7680 unsigned length-four blocks with K_U histogram (5880,1680,120), and finds exactly four unsigned length-three return intermediates per directed edge. It uses only finite integer and rational operations. The theorem for all n and all p follows from the transition-class and determinant arguments; the checker supplies finite constituent validation.

Further science: relate the 840-dimensional discarded signed sector to a declared BRC provenance-sensitive observer on an actually authorized native event family. The unsigned quotient is safe only for its stated observer and transition family. An event-level closure witness, source guard and V29/V39 license must be checked independently.
