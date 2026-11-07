# R5 parametric extension: robust FULL/LR rank-four convex-hull identity and genuine real-image gap

Date: 2026-10-30 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Frozen control inputs: GLOBAL_KNOWLEDGE_V1 main@63f701b793312d4d7997eb893a218f9c29c070fb; Enterprise Math main@f05844fa7a1ed5fa3e75fc98eecd757949bcb3f2. Companion concrete model/proof: RESEARCH.md at preceding PR commit 907a72ab1dbbdc447d2834c16d19af94528d273f. The original **strict stop/continue-only mother target is still open**: X below is a **nonterminal route-choice** that does not terminate either route. It cannot be renamed a stop decision. This is a scoped auxiliary mathematical construction; no native Heartbeat/X6/physical model claim.

## Exact model and complete legal parameter domain

Fix real p,q with 0<p,q<1. First choose nonterminal route X~Bernoulli(x), x∈[0,1], under both P and Q; then independently of X sample U in {0,1}, under P with P(U=0)=p, under Q with Q(U=0)=q, with strictly positive complements. At time 3 choose stop Y=1 or continue to compulsory stop at time 4. FULL chooses independent real conditional probabilities y_{x,u}∈[0,1]; seedless LR chooses y_u∈[0,1] as a function only of (time, P/Q likelihood ratio), not X or any persistent random seed. For p≠q, the two LR values p/q and (1−p)/(1−q) differ, and each U yields a genuine collision of the distinct X routes.

Both P and Q use the same terminal error-probability kernel k(X,Y)=c+aX+bXY. Require the three real numbers c,c+a,c+a+b all strictly in (0,1); they exhaust the possible kernel values and thus ensure legal probability. Observe the original four quantities O=(eP,eQ,TP,TQ), with eL=E_L[k], TL=4−E_L[Y], L=P,Q.

**Theorem.** For every such real legal parameter tuple and all real behavioral strategies:

(1) conv(O_FULL)=conv(O_LR), with equality for ALL signed linear support directions.

(2) The common convex hull has affine dimension FOUR iff (p−q)b≠0.

(3) When (p−q)b≠0, the FULL real image properly contains the seedless LR image. In fact

    O*=(c+a/2+bp/2, c+a/2+bq/2, 7/2, 7/2)

belongs to FULL but not LR, and its usual unscaled coordinate sup-norm distance to the complete LR real image is at least

    |b|·|p−q| / [4(1+|b|)] > 0.

Thus full-rank hull equality plus real-image non-equality holds over a nonempty open real parameter family (relative to legal parameter domain), not merely a numerically fitted rational point.

## Proof

**All-signed convex-hull identity.** The FULL observation map is multi-affine in its five independent real behavior parameters x,y00,y01,y10,y11: every path probability is a product in which each local behavior parameter occurs at most once. Its real image is contained in the convex hull of its 32 Boolean-corner images by the exact multi-affine Bernstein expansion. At every Boolean FULL corner, X is deterministic, so only the two later Y decisions for that chosen route are reached. Select the LR Boolean policy with the same X and these two effective U decisions. It realizes the identical four-observer vector under P and Q, because all unreachable FULL decisions have zero path weight. Therefore every FULL Boolean vector is one of the eight LR Boolean vectors. The reverse inclusion of real LR behaviors in FULL is immediate from the policy definitions. The two convex hulls coincide exactly.

**Full-rank classification.** For LR Boolean x,y0,y1∈{0,1}, write
    mP=p y0+(1−p)y1, mQ=q y0+(1−q)y1,
    v(x,y0,y1)=(c+ax+bx mP,c+ax+bx mQ,4−mP,4−mQ).
Take v000 as base. The determinant of four difference columns from v010,v001,v100,v110 is
    D1=−a b(p−q)^2.
The determinant of four differences from v010,v001,v110,v101 is
    D2=b(2a+b)(p−q)^2.
The exact symbolic determinant identities are verified in the executed VERIFY_PARAMETRIC.py and can also be checked directly by elementary expansion. When (p−q)b≠0 and a≠0, D1≠0. If a=0, D2=b²(p−q)²≠0. Hence rank four in all allowed cases. Conversely if b=0, eP=eQ identically for every policy, so rank≤3; if p=q, the P and Q laws coincide, so both errors and both times coincide and rank≤2. These exhaust the cases. No approximate or genericity claim is involved.

**Universal LR invariant and explicit FULL witness.** Under seedless LR, route X is selected before independent U and the later Y policy depends only on U. Hence E_L[XY]=x E_L[Y] for L=P,Q. Moreover E_P[X]=E_Q[X]=x. Subtracting error expectations gives

    eP−eQ = bx(E_P[Y]−E_Q[Y]) = bx(TQ−TP),    0≤x≤1.

Therefore every real LR behavior satisfies |eP−eQ|≤|b|·|TP−TQ|.

Set FULL x=1/2 and conditional Y=X when U=0, Y=1−X when U=1. Then under BOTH laws E[Y]=1/2 and E[X]=1/2, while E_P[XY]=p/2 and E_Q[XY]=q/2. The resulting O* is precisely the vector in the theorem and has TP=TQ=7/2 but eP−eQ=b(p−q)/2≠0. Therefore NO seedless LR real behavioral strategy implements O*.

For any LR O' at coordinate sup distance ε from O*, triangle inequalities give
    |eP'−eQ'|≥|b|·|p−q|/2−2ε
and |TP'−TQ'|≤2ε. The LR invariant forces |b||p−q|/2−2ε≤2|b|ε, i.e.
    ε≥|b||p−q|/[4(1+|b|)].
This proves a positive universal distance lower bound, not claimed optimal. QED.

## Exact evidence and method boundaries

For the concrete legal rational specialization p=1/4, q=1/2, a=b=1/8, c=1/4, O*=(21/64,11/32,7/2,7/2), D1=−1/1024, and the lower bound is 1/144, recovering companion RESEARCH.md. The standalone executed SymPy source VERIFY_PARAMETRIC.py establishes the two symbolic determinant identities, witness error difference, rational specialization and selected rank witnesses. The original stdout is PARAMETRIC_OUTPUT.txt and ends PASS_EXACT_R5_ROUTE_MEMORY_PARAMETRIC_OPEN_FAMILY. Real universal quantification comes from the displayed algebraic proof, NOT from finite testing; no Lean/formal theorem checker or independent reviewer is claimed.

BRC interface actually applied: definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json at the pinned Enterprise Math main. Retain separate strictly positive P/Q route-and-U branch masses and source labels; the LR key quotient is ONLY the behaviorally admissible observer for decision Y. Source/path provenance is NOT declared globally redundant, and arbitrary future observer safety is not inferred. Resolution: REUSE_APPLIED; this is a mathematical application, not a new general BRC tool family.

Native research_authority_granted=false; live owner read CONTROL_QUOTA; this logical conversation's own session_start was explicitly denied STATIC_READONLY_SCOPE_DENIED (operation_sent=false). No native activity, CLAIM, Result, or independent Driver acceptance. The protected P000 and ACTIVE worldview remain unchanged. Project GitHub PR evidence is author-side preservation only.

**Next exact research question:** Check the original Task's authoritative action alphabet when real owner read becomes available; if genuinely nonterminal routing is permitted, submit this strictly scoped model for independent mathematical review. Otherwise find a faithful strictly stop/continue-only construction that replicates this route-memory anticorrelation and its four-observer equality, or prove that this mechanism cannot be embedded into the allowed strictly stopping topology. Do not claim a stop-only solution by relabelling X. Require exact all-signed convex-hull certificates before any new real-image nonmembership claim.