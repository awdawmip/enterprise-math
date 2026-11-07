# EC49S — Exact phase diagram for informative first-stage causal BRC observation

Status: AUTHOR_PROVED / EXACT_FRACTION_GRID_PASS / UNREVIEWED / NOT_ADMITTED. This is author-side positive-weight auxiliary BRC mathematics, not a Source-issued CLAIM/Result or native signed-BRC theorem.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@794471c0becbb4e592926210e952855ebc858da6; Enterprise Math main@a64342a6b2c72856b4d76b4c955d03bb1799c364; parent EC49R PR #1660 immutable head e02d9fd7e6d72916020d2868d610974a4ec41758. P000 startup projection canonical SHA1 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc agrees with P000 original. P000 and ACTIVE worldview are unchanged.

## Typed model and exact target

W=Z={0,1,2}. The two strictly positive source probability masses are Q(w,z)=1/9 and P(w,z)=1/6 if z=w, 1/12 otherwise. Write Delta(w,z)=P(w,z)-Q(w,z), equal to 1/18 if w=z and -1/36 otherwise. P_W=Q_W=uniform(3).

The first purchased sensor produces U in {0,1} with t(w,u)=Pr(U=u|W=w)=1/2+(2u-1)*eta*sigma(w), where sigma=(1,0,-1) and real 0<=eta<1/2. The same kernel is used in P,Q and for either first action. U and Z are independent conditional on W. Source-labeled joint mass R(w,u,z)=R(w,z)*t(w,u) (R=P,Q), with 18 strictly positive atoms in each source; masses are rational if eta is rational.

W is observed initially. The source-independent controller may stop and accept/reject freely, or buy first action A at cost 1 or B at cost 2 and observe U. This purchase erases W. Compressed policy retains only chosen action A/B and one external memory bit D assigned causally before W erasure; full policy retains W. After U, it may stop and accept/reject, or buy second sensor S at cost 1, observe Z and accept/reject. S cannot be bought before A/B. Randomization is fresh, behavioral, source-independent, and independent across information sets; no shared seed or undeclared register is permitted.

O=(alpha,beta,E_PT,E_QT): P and Q terminal-acceptance probabilities plus P/Q expected total sensor resource bills. Let H(O)=alpha-beta-(E_PT+E_QT)/48. T is a resource and *not* Heartbeat World time. Because P and Q induce identical (W,U) distributions, and all purchase choices precede Z, E_PT=E_QT for every policy in this exact protocol. P-Q is an external comparison of positive BRC branch masses, not a signed/phase primitive.

## Theorem 1 — exact all-real sharp support phase diagram

For every real 0<=eta<1/2, over every legal real source-independent fresh behavioral policy,

  max H(full) = 1/12,
  max H(compressed) = max(5/72,eta/6).

Thus the exact *sharp* gap is g(eta)=1/12-max(5/72,eta/6). It equals 1/72 for 0<=eta<=5/12 and (1-2eta)/12 for 5/12<eta<1/2. In particular at the inherited eta=1/200, the exact compressed optimum is 5/72 and the exact gap is 1/72. EC49R's TV-based lower bound 49/7200 stays valid but is strictly nonsharp.

### Proof of the real-policy upper bound

The finite protocol is acyclic and every local behavioral randomization distribution is used at most once per realized path. H is multi-affine in independent local simplex coordinates, so fixing all other coordinates and taking a maximizing simplex vertex, successively for all coordinates, yields a deterministic maximizer. Hence it suffices *analytically* to classify deterministic policies, for any real eta. The exact finite Fraction checks below are not used to extrapolate real-eta generality.

The first-stage deterministic compressed map sends each w to STOP or to one of four codes (A,0),(A,1),(B,0),(B,1). For each code (a,d), let G be the inverse-image subset of W, n=|G|, and c_a=1 for A and 2 for B. The sum of its best possible terminal discrimination and cost penalty is

 V_a(G) = -n*c_a/72
   + Sum_u [ Sum_z [ Sum_{w in G} t(w,u)*Delta(w,z) ]_+
              - Sum_{w in G} t(w,u)/72 ]_+,

where [x]_+=max(0,x). The first term pays the initial sensor cost in BOTH sources with weight 1/48 each. The second cost term pays S with combined source-neutral mass. The inner acceptance maximum chooses the common Z-event with positive *aggregate* P-Q mass, not separate P- and Q-optimized policies. Stopping before S yields no P-Q acceptance difference, since the (W,U) marginal is source-neutral, and has no additional cost. Thus this formula optimizes all downstream decisions, including optional S and all terminal masks.

For a singleton {w}, the positive terminal event is exactly Z=w, both U values. Direct substitution gives
 V_A({w})=1/36, V_B({w})=1/72, independently of eta.

For a pair G={i,j}, its two inside-Z differences are (2*t(i,u)-t(j,u))/36 and (2*t(j,u)-t(i,u))/36, while the outside-Z difference is negative. Their positive-part sum equals
 (t(i,u)+t(j,u) + [t(j,u)-2*t(i,u)]_+ + [t(i,u)-2*t(j,u)]_+)/36.
After subtracting S cost, the resulting gain is always nonnegative. Since Sum_u(t(i,u)+t(j,u))=2, the exact pair contributions are
 V_A({0,2})=[6*eta-1]_+/36,
 V_A({0,1})=V_A({1,2})=[2*eta-1/2]_+/36,
 V_B(G)=V_A(G)-1/36 for every pair.

For G=W the sum of t(w,u) is 3/2 at each u and the three Z differences are (+eta/12,0,-eta/12), or reversed under the other U. Therefore
 V_A(W)=-1/24+2*[eta/12-1/48]_+ <0 (eta<1/2)
 and V_B(W)=V_A(W)-1/24<0.
An unused code contributes zero. The more informative pair {0,2} weakly dominates the other two pairs for eta>=0. A B code is always more costly than an A code with the same observation kernel, but only two A codes exist.

It remains to compare partitions of three W histories into code fibers:
 (i) three singletons, two A and one B: 2/36+1/72=5/72;
 (ii) one pair {0,2} using an A code, singleton {1} using the other A code: ([6*eta-1]_++1)/36;
 (iii) all remaining partitions or stopped histories, weakly dominated by (i) or (ii).
For eta<=1/6 the value in (ii) is 1/36<5/72; for eta>1/6 it is eta/6. Thus max H(compressed)=max(5/72,eta/6).

Under full recall, for each W and U, buying cheapest A followed by S and accepting just Z=W maximizes discrimination net of cost. The total positive Delta mass for a W row is 1/18; source-neutral cost A+S contributes 2/72 in H for that row, leaving 1/36 per W. U provides no increase over this full-history strategy because both t(w,u) values sum to one and action prices are nonnegative; stopping contributes zero discrimination. Summing the three rows gives max H(full)=3/36=1/12. QED.

### Explicit feasible witnesses, showing sharpness

For eta<=5/12, code W=0→A0, W=1→A1, W=2→B0; always buy S; accept exactly Z=decoded W. This gives O=(1/2,1/3,7/3,7/3), H=5/72, for all eta.

For eta>=5/12, code W=0,2→A0 and W=1→A1; always buy S. At A0 accept Z=0 for U=1 and Z=2 for U=0; at A1 accept Z=1. Direct source-mass multiplication yields O=(5/12+eta/6,1/3,2,2), H=eta/6.

Full witness: buy A+S for every W and accept only Z=W, giving O=(1/2,1/3,2,2), H=1/12. Therefore this full four-vector is outside the convex hull of compressed vectors for every eta<1/2. The gap tends to zero as eta approaches 1/2, where strict positivity of the U conditional kernel is lost.

## Theorem 2 — exact cost lower bound at maximal discrimination

For all real 0<=eta<1/2, the largest possible alpha-beta is 1/6, the total positive Delta mass on Z=W. Reaching it forces the same accept/reject label for every positive/negative full-support (w,u,z) atom, so buying S and recognizing Z=W with probability one for every W is necessary. Since both U values have positive probability for every W, two distinct W values sharing a (a,d) code would require contradictory accept/reject labels when Z is one of those W values. Even with randomized encoding, the code supports for distinct W must be disjoint. Three W require three codes; only two cheapest A codes exist, hence at least one W pays for B. Since W is uniform under both sources, average first-stage cost is at least (1+1+2)/3=4/3 per source; buying S costs another 1. Thus E_PT=E_QT>=7/3 for every compressed controller with alpha-beta=1/6, attained by the three-singleton witness. Full recall attains alpha-beta=1/6 at E_PT=E_QT=2. QED.

## Verification and epistemic scope

Actual Python fractions.Fraction checker: 45 selected rational eta values (including 0,1/200,1/6,1/4,1/3,5/12,49/100), 125 initial deterministic maps per eta (5625 exact map evaluations), complete group identities, 18 positive atoms per source, both explicit policy witnesses, and a strict rational gap at every tested eta. PASS. The universal results above are derived from exact algebra and the multi-affine deterministic reduction, not from grid extrapolation. The original extended executed checker/report and source ledgers are in this research unit's companion artifacts; the compact reproducer and validation summary are here.

Related, non-equivalent external research: Anderson & Montúfar, ICML 2026, PMLR 306:2677–2715 on infinite-horizon memoryless POMDP value sets; Bork et al., UAI 2025, PMLR 286:355–387 on multi-cost-bounded POMDP reachability (links in SOURCES.md). Neither is a proof of this finite parametric calculation or an independent originality review.

The unresolved whole-four-vector causal encoding criterion is EC49T (NEXT_TASK.md). For native signed BRC, Enterprise coordinates/X6 or the three-dimensional slice, an explicitly typed provenance-preserving morphism, observer commutation and native independent verification remain required. No native heartbeat dynamics inference is made.
