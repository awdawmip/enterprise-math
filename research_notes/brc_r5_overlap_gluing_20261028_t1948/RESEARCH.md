# R5: Exact source-overlap gluing polytope and a two-stage rational collision

2026-10-28 author-side portable mathematical research. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. No native CLAIM, Result, Driver review, or X6 dynamical validation is claimed.

## Frozen sources

Global: awdawmip/chatgpt-global-knowledge main@10fb65d6beb36b83f02330b85d435412414cdccc (read 00_BOOTSTRAP.md, OPERATING_MANUAL.md, P000_REALITY_FOUNDATION.json, ACTIVE worldview, math/code/BRC/EM activity rules). Project: awdawmip/enterprise-math main@3d0d3af5fa56b9451d43f157aa763bdeb8050504 (read AGENTS, P000, X6, residual/joint observer constraints, BRC substrate, current portable/autonomous protocols, and immediate predecessor brc_r5_joint_tv_polygon_20261028_t1844/RESEARCH.md + NEXT_TASK.md).

This extends, and does not repeat, the predecessor's exact two-law total variation (TV) polygon. BRC REUSE_APPLIED: rational positive branch mass, source labels, LR transport, and a retained intersection/overlap coordinate. The TV observer is an auxiliary finite statistical observer, not a sufficient X6 native state.

## Main theorem — exact triple polytope

Fix n>=3 and 0<s1<...<sn, s1<r<sn. Let q,q' be real nonnegative conditional Q probability laws on the signatures, each of mean r. Their conditional P laws are p_i=(s_i/r)q_i and p'_i=(s_i/r)q'_i. Put

    u=(1/2) sum |q_i-q'_i|,   v=(1/(2r)) sum s_i |q_i-q'_i|,
    gamma_k=min(q_k,q'_k), M=1-u, C=r(1-v).

For a specified k, let ell=min(s_j:j!=k), h=max(s_j:j!=k). The exact feasible set of (u,v,gamma_k) over ALL real nonnegative kernels is the intersection of these LINEAR inequalities:

    u>=0
    s2*u <= r*v <= s[n-1]*u
    0<=gamma_k<=1-u
    ell*(1-u-gamma_k) <= r*(1-v)-s_k*gamma_k <= h*(1-u-gamma_k).

In particular the inequalities force 0<=u<=1 and u=0 => v=0. The strictly positive Q/P-kernel locus is precisely the same TV wedge together with gamma_k>0, 1-u-gamma_k>0, and both last inequalities STRICT. For rational input all rational feasible triples have rational witnesses; all rational triples in the strict locus have strictly positive rational witnesses.

### Proof of necessity

Decompose q=c+a, q'=c+b coordinatewise with c_i=min(q_i,q'_i), a_i=(q_i-q'_i)_+, b_i=(q'_i-q_i)_+, so a_i b_i=0. Common normalization and mean give sum a=sum b=u, sum s_i a_i=sum s_i b_i=r v, sum c=M, sum s_i c_i=C. For u>0 the two disjoint probability laws a/u,b/u have identical mean m=rv/u. If m<s2 each must charge unique lowest signature s1, contradiction; if m>s[n-1] both must charge unique highest signature sn. Thus s2*u<=rv<=s[n-1]*u; u=0 is immediate. Fixing c_k=gamma leaves common mass M-gamma and moment C-s_k gamma on the remaining signatures. Their mean must lie in [ell,h], proving the final pair of halfspaces. If all q_i,q'_i are strictly positive then every c_i>0, so gamma>0, M-gamma>0 and the final inequalities are strict.

### Proof of sufficiency

For u>0 set m=rv/u. Choose A supported on {s1,sn} with mean m by endpoint interpolation. Choose B supported on {s2,s[n-1]} with mean m (for n=3 B is point mass on s2). A and B have DISJOINT supports. For u=0 take no signed residual. Set c_k=gamma. The last two halfspaces permit distributing mass M-gamma and moment C-s_k gamma over the minimum and maximum signatures OTHER THAN k (zero mass case forces zero remaining moment). Then q=c+u A and q'=c+u B are normalized, mean-r and nonnegative. Because A and B do not intersect, min(q_i,q'_i)=c_i, so the target (u,v,gamma) is realized exactly. If the strict inequalities hold, choose arbitrarily small positive weight at every remaining signature and adjust the extreme weights, making every c_i>0. Rational interpolation and a rational small perturbation yield rational witnesses. This proves the full all-real and strictly-positive assertions, not merely a finite-grid check. QED.

### Closed form for highest output signature

For k=n, gamma_n has the SHARP interval

    max(0, (r*(1-v)-s[n-1]*(1-u))/(sn-s[n-1]))
      <= gamma_n <=
    (r*(1-v)-s1*(1-u))/(sn-s1).

For 1<k<n, the sharp maximum is min(1-u, (C-s1*M)/(s_k-s1), (sn*M-C)/(sn-s_k)); exact construction follows from the theorem.

## Fully rational two-stage witness

Stage 1: s=(1/2,1,2,3), r=3/2. Fix (u,v)=(3/5,3/5). The highest signature has 0<=gamma_4<=4/25. An exact boundary witness (nonnegative) is

    q_A=(3/5,0,0,2/5)
    q_B=(6/25,3/10,3/10,4/25).

An ALL-STRICTLY-POSITIVE witness with the SAME (u,v) is

    q_A=(147/250,1/100,1/100,49/125)
    q_B=(57/250,31/100,31/100,19/125),

whose gamma_4=19/125. Hence the tempting independent tuple (u,v,gamma_4)=(3/5,3/5,1/5) is IMPOSSIBLE for any real kernels: 1/5 > 4/25.

Embed it in a complete two-law history tree with initial hidden source Q masses (A,B,O)=(1/4,1/4,1/2), P masses (3/8,3/8,1/4), so A/B share first-stage LR r=3/2 and O has LR 1/2. Emit the above positive stage-1 kernels under A/B and use P(child|h)=(s_i/r)Q(child|h). At signature s4=3 both histories meet at a second NONTERMINAL LR fiber, where source A/B kernels with next signatures (1,2,4,5) and r2=3 are

    z_A=(3/8,1/8,1/8,3/8)
    z_B=(1/8,3/8,3/8,1/8),

so second-stage TV_Q=TV_P=1/2. Use P(child|F2)=(next_LR/3)Q(child|F2). Other branches stop; P and Q TOTAL LEAF MASS each exactly 1. Every live branch has strictly positive two-law mass.

The incoming common-source Q mass of the second collision is

    min(Q(A->F2),Q(B->F2))=(1/4)*gamma_4=19/500.

At fixed first-stage (u,v) this shared capacity cannot exceed 1/25 (attained for nonnegative kernels), so a requirement of 1/20 is impossible by exact rational separation 1/20>1/25. This is the cross-layer gluing obstruction FOR THE EXTENDED OBSERVER WITH SOURCE OCCUPATION.

Essential caveat: if one erases gamma and keeps ONLY (u1,v1,u2,v2), the local TV polygons can be independently realized in this unconstrained tree; there is NO proved obstruction to their four-coordinate Cartesian product here. The result shows a future-relevant branch/occupation coordinate is erased by TV-only compression. It does NOT establish the ultimate full-vs-LR four-dimensional signed-support equality or true-image inequality.

## Verification and provenance

Accompanying VERIFY.py executes Fraction-only exact checks for all displayed masses and probabilities, a deterministic 1080-case full-positive sample across n=3..6, and 603 exact feasible triple points of the stated rational grid. Output: EXACT_OUTPUT.txt. Finite checks corroborate examples, not the universal theorem; the latter follows from the explicit proof. No formal proof assistant or X6 native simulation was executed.

Literature background, without first-discovery/novelty claim: Charalambous, Tzortzis, Loyka and Charalambous, Extremum Problems with Total Variation Distance and their Applications (2013), https://arxiv.org/abs/1301.4763. Earlier verified project source: research_notes/brc_r5_joint_tv_polygon_20261028_t1844/RESEARCH.md.

Native control reads in this run: em_control_tasks -> CONTROL_QUOTA; em_status -> research_authority_granted=false, CODE_REVIEW_REQUIRED; em_session_start -> STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Active Source Owner not verifiable, no Source CLAIM/Result/Driver review. GitHub write permission was independently verified. This file is author-side evidence, NOT native control authority.

Next: retain gamma as an explicit occupation/repair coordinate in two interacting nonterminal stop/continue decisions, derive a sharp source-tagged Bellman gap or signed support certificate, and first eliminate support-separated cases. Only after proving all-direction convex hull equality search for an all-real semialgebraic true-image witness.