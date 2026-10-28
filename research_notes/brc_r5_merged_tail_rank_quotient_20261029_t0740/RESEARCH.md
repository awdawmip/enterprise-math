# Enterprise Math R5: A sharp rank criterion and exact coin-pushing quotient at a source-sensitive merger

2026-10-29, author-side portable research. Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. This is a finite two-law auxiliary decision model, not a Source CLAIM, admitted theorem, independent review, or native X6 result.

## Sources, observer, and scope

This is a new structural continuation of the source-sensitive diamond proof (enterprise-math commit 7d15ad6ab750b1caf041d1e760b8b354fc804083, research_notes/brc_r5_sensitive_tail_bellman_20261029_t0337/RESEARCH.md) and the all-signed finite-hull certificate (author research branch in PR #1663). The earlier rank-two negative joint-flow determinant is used as a regression witness, not presented as a new discovery.

Frozen knowledge input: GLOBAL_KNOWLEDGE_V1 main@7b33f8066e9993e7c941959a9d738ed405248eb8; project source input: enterprise-math main@d41c13c55100140ac6ca6bab920abd6ea93174c3, native read-only snapshot 147f7b53374e32a4606a5c6d9a9611e6594a385f0edd3be902c2e01806b05f04. Read global bootstrap/manual, project bootstrap, full locked P000, ACTIVE worldview, BRC, current autonomous/portable protocol. P000 and Heartbeat World remain unchanged. BRC carrier is the positive source-by-route Q-mass vector. The LR observer must not be mistaken for a full source label.

The native gateway denied session_start with STATIC_READONLY_SCOPE_DENIED and operation_sent=false, and active owner search returned CONTROL_QUOTA. Hence the current Source owner/CLAIM and formal Result remain unverified. Author-side GitHub preservation grants no native execution/review authority.

## Model, all-real scope

Let d>=1 hidden origins, k>=1 separately identifiable predecessor routes, and strictly positive rational source-Q-mass columns v_j in R^d. Their predecessor (time,LR) information keys are distinguishable, so a seedless LR policy can have independent route continuation coins alpha_j. A common root continues with U in [0,1], yielding L_j=U alpha_j in [0,U]. At a single later merged LR node, one shared fresh coin gamma in [0,1] continues the Q-source vector x=V L as m=gamma V L. Each trajectory visits each information key at most once; gamma does not store the incoming route or origin. Define:

E = {(U,L,m): 0<=U<=1; 0<=L_j<=U; exists gamma in [0,1] with m=gamma V L}.
F = {(U,m): exists L such that (U,L,m) belongs to E}.

At merger LR r, a finite terminal signature s has source-conditional Q probability eta_i(s)>0, sum_s eta_i(s)=1, and sum_s s eta_i(s)=r, so P mass at signature s is s times its Q mass. Set K_(s,i)=eta_i(s), H=K m. The terminal signal s permits a fresh independent declaration coin d_s, with tail-only error contributions eQ_tail=sum_s d_s H_s and eP_tail=sum_s s(1-d_s)H_s. These are contributions from the merged terminal subtree, not the full-process four observables (eP,eQ,TP,TQ).

## Theorem A (necessary and sufficient joint-flow convexity)

For every real behavioral policy probability under this model, E is a compact convex polytope IF AND ONLY IF rank(V)=1.

Proof. If rank(V)=1, positivity gives v_j=c_j v with common positive vector v and scalars c_j>0. Put t=gamma sum_j c_j L_j. For each feasible U,L the attainable t are EXACTLY 0<=t<=sum_j c_j L_j, because any t in this interval is implemented by gamma=t/(sum c_j L_j), with gamma=0 if denominator zero. Consequently E is an affine image of a bounded linear-inequality polytope (U,L,t).

If rank(V)>=2 choose non-collinear columns v_a,v_b. Both points (U,L,m)=(1,e_a,v_a) with gamma=1 and (1,e_b,0) with gamma=0 are feasible. Their arithmetic midpoint would require v_a=gamma(v_a+v_b) for some real gamma, impossible by column independence. Thus E is nonconvex. This proves the equivalence without an action grid or a limiting argument.

For two routes, x_h=v L_h+w R_h, m_h=gamma_h x_h, the mixed origin-flow minor at the midpoint of strategies h=1,2 is exactly
D_mid = (gamma_1-gamma_2)/4 * det(v,w) * (L_1 R_2-R_1 L_2).
It can be nonzero only when source columns, route mixtures, and merged continuation coins all contrast. This is a lifted provenance statement; no coarse-observer nonconvexity follows automatically.

## Theorem B (exact all-rank post-merger quotient)

For ALL ranks and ALL real coins,
F = {(U,m): 0<=U<=1; exists b in R^k with 0<=b_j<=U and m=V b}.
Thus F is a compact convex polytope; at fixed U its source fiber is the zonotope V[0,U]^k.

Proof. Every policy has b_j=gamma L_j, so 0<=b_j<=U and m=V b. Conversely any such b is implemented by a genuine seedless LR policy: keep U, set gamma'=1 and L_j'=b_j. If U>0 choose alpha_j'=b_j/U; if U=0 all b_j vanish and choose alpha_j'=0. No persistent random seed or source access is required. These transformations preserve (U,m) EXACTLY for every real policy. Because the displayed feasibility set is a linear projection of a bounded polytope, F is compact and convex. QED.

Boundary: this coin pushing changes predecessor L_j, so it is NOT automatically safe for earlier stopping-time survival, path-specific declarations, earlier terminal Q/P errors, or native dynamics. A nonzero determinant in E can be invisible in F.

## Theorem C (source-sensitive randomized terminal declarations remain a polytope for a tail-only observer)

The actual seedless LR image of (U,eP_tail,eQ_tail) is exactly the linear projection of

0<=U<=1; 0<=b_j<=U; H=K V b; 0<=a_s<=H_s;
eQ_tail=sum_s a_s; eP_tail=sum_s s(H_s-a_s).

Proof. Necessity: b=gamma L, H=K V b, a_s=d_s H_s. Sufficiency: use Theorem B to realize H by a genuine seedless LR policy, and select d_s=a_s/H_s when H_s>0, zero otherwise. This realizes precisely the specified real tail-error observer. All constraints are linear and bounded, giving a compact convex polytope even when eta_i differ. QED.

The tail-signature histogram needs at most rank(KV) independent linear source coordinates. Total-only compression is safe for this tail histogram precisely when K V factors through the positive total-mass row (1,...,1)V on the attainable span; an otherwise nonzero tail composition residual is observable with a rich enough signature readout.

## Exact R5 source-sensitive diamond and repaired midpoint

Use v=(11/1200,23/3600) and w=(1/40,1/100), so det(v,w)=-49/720000. At terminal S=(1/2,1,3/2,5/2), set eta_A=(1/8,1/4,3/8,1/4) and eta_B=(5/32,3/16,13/32,1/4). Each kernel is strictly positive, Q-normalized and has mean LR 3/2. The joint-flow midpoint between (U,L,R,gamma)=(1,1,0,1) and (1,0,1,0) has the exact nonzero collinearity defect -49/2880000, so it is impossible as a single lifted joint-flow policy.

Nevertheless, its post-merge source vector and the ENTIRE four-signature terminal Q histogram are exactly realized by the true LR policy (U,alpha_L,alpha_R,gamma)=(1,1/2,0,1): one can push gamma into the predecessor route coins. The terminal kernels differ, so this example is stronger than the earlier source-insensitive safe-quotient case, but it remains explicitly tail-only. Moreover the final histogram determines both source masses through
m_A=20 H_(5/2)-32 H_(1/2);  m_B=32 H_(1/2)-16 H_(5/2).
Thus retaining the full histogram still preserves rank-two composition information, while reducing to error sums can erase it.

## Evidence, limits, and next question

The companion VERIFY.py executes exact rational Fraction checks: P/Q row conditions, rank-two minor and its midpoint, legal coin-pushed reconstruction, two signature-based source readout formulas, all 1296 rational root/route/merger combinations with four terminal declaration choices each, plus 1296 rank-one interval regressions. Actual output is EXACT_OUTPUT.txt. The universal theorems rely on the constructive algebraic proofs above; 1296 finite samples are only regression checks. No original native X6 computation, symbolic CAD, full four-observer convexity proof, Source result acceptance, independent review, or external novelty conclusion is claimed.

Scientific increment: exact iff rank-one criterion for the JOINT flow; at every rank, real seedless coin-pushing gives a convex source-tail quotient; with origin-sensitive terminal kernels and genuine randomized declarations, the tail-only errors remain a polyhedral observer. This identifies a safe BRC observer boundary and prevents falsely promoting a joint-flow nonconvexity into a four-observer impossibility statement.

Next executable unit: add one independently measured ancestor-flow statistic C=c.L to (U,m) or to the terminal error observer, and derive a sharp exact convexity/nonconvexity criterion. In particular test the previous diamond's time rows that expose L. A mother-question candidate still requires exact ALL-SIGNED convex-hull equality before proving any real four-observer nonmembership; this unit does NOT solve that mother question.