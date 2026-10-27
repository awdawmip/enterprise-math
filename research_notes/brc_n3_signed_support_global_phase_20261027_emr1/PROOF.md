# R1: Global signed-support phase diagram for R5 ternary BRC collision

2026-10-27 | AUTHOR_PROVED / UNREVIEWED / NOT_ADMITTED. External finite two-law observation model, NOT a native Heartbeat/X6 computation.

## Pinned sources and actual authority
GLOBAL_KNOWLEDGE_V1 main@2971137f2a579c1591c8c5abef7c1363db0b6f30: canonical bootstrap/manual, Enterprise Math TASK role router, P000 startup projection verified against original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview, mathematical and BRC rules.
Enterprise Math initial main@9c323bc07b78931640344a469ba530733ca1773b; exact R5 source and next task read at 993762ba159b6b3720948d8069cf24f840e7de02, path research_notes/brc_n3_ternary_single_collision_facet_oracle_20261027_r5/. GitHub actor awdawmip verified; native task inventory returned CONTROL_QUOTA. Author research is not an official TASK CLAIM, Result, independent Driver review, or Foundation admission.

BRC reuse: T0_BRC / REUSE_APPLIED to ordered positive two-law branch weights, labeled history, P/Q conservation and LR observer. Positive mass is not a signed amplitude. The readout may erase decision-relevant future kernel information. Native P000 has six spatial Cell axes, separate time, a 3D slice, no native plane; no Cell-to-probability-tree dynamics/readout bridge has been demonstrated.

## Model and theorem

Use the R5 eight-positive-leaf, 15-prefix tree with (Q(h),r=P/Q):
root (1,1); a (1/2,3/2), b (1/2,1/2);
ax (1/4,1), ay (1/4,2), bu (1/8,1), bv (3/8,1/3).
At ax and bu (the only nonterminal time/LR collision), choose respectively conditional Q terminal kernels K(s_a),K(s_b)=(s,1-2s,s) on terminal LR (1/2,1,3/2). At ay and bv there is one terminal child preserving its LR. Assume 0<s_a,s_b<1/2. Set every P(h)=Q(h)r(h). Conservation holds under BOTH laws since E_K[r_terminal]=1.

For a common stopping/decision policy observe O=(P(decide Q),Q(decide P),E_P[tau],E_Q[tau]); take signed linear support J=298 O_1+375 O_2+37 O_3-17 O_4. Let F(s_a,s_b) be the minimum over full-history behavioral policies and C(s_a,s_b) the minimum over seedless, time/LR-only behavioral policies (fresh local randomization, no persistent root seed). Write [x]_+=max(x,0).

**Global exact theorem, all real parameters in the stated square:**

F = 281 - [18 s_a-5]_+ - [9 s_b-5/2]_+.

C = min(281, 282 - [18 s_a-5]_+ - [9 s_b-3/2]_+).

C-F = min([18 s_a-5]_+, [1-[9 s_b-3/2]_+]_+).

Thus the one fixed normal J strictly separates the full-history hull from the seedless convex hull **iff s_a>5/18 AND s_b<5/18**. For this J the exact maximal gap is 1, attained when s_a>=1/3 and s_b<=1/6 (respecting positivity). At the original point (1/3,1/6): F=280,C=281. At a distant strictly positive rational point (49/100,1/100): F=13859/50,C=13909/50. Equality for this single J outside the rectangle does NOT imply hull or behavioral-image equality.

## Proof

Normalize future cost at history h by Q(h), subtracting the already elapsed time cost. With r(h)=r, choosing P costs 375, choosing Q costs 298r, and continuing adds 37r-17 plus the conditional Q-weighted future value. Q-weighted mean successor LR equals r, so this is the correct time increment under both laws.

At terminal LR (1/2,1,3/2), optimal immediate classification costs (149,298,375). Thus at either colliding ratio-one state K_s, immediate optimum is 298 while continuing has cost 20+149s+298(1-2s)+375s =318-72s. The full-history optimal value is g(s)=min(298,318-72s)=298-[72s-20]_+, lying between 282 and 298 on the positive open domain.

The singleton descendants give value 375 at ay (r=2; continuing adds 57>0), and 284/3 at bv (r=1/3; continuing adds -14/3). At a, with children ax,ay each conditional Q mass 1/2, continuing costs (g_a+452)/2<=375, so it is weakly optimal. At b, with children bu,bv conditional Q masses 1/4,3/4, continuing costs g_b/4+145/2<=147<149, so it is strictly optimal. At root, continuation costs 677/4+g_a/4+g_b/8<=281<298. Expanding both g's proves the formula for F.

For the seedless class, deterministic actions on each time/LR class suffice to minimize any *linear* functional: the class is visited at most once because time advances, so independent presampling of its action reproduces the expectation of fresh randomization. At terminals every history sharing an LR has the same individually optimal classification decision; at every other nonterminal class, histories are unique. Only ax and bu must share a nonterminal action. Evaluate their three possible common actions:

- Both stop/decide Q: their conditional values are 298 each. Optimal a=375,b=147, root=281.
- Both stop/decide P: their conditional values are 375 each. Optimal a=375,b=149, root=282, dominated by the preceding option.
- Both continue: their values are h_a=318-72s_a, h_b=318-72s_b. Optimized a=min(375,385-36s_a)=375-[36s_a-10]_+, and b=min(149,152-18s_b)=149-[18s_b-3]_+. Root continues (cost <=282<298), yielding exactly 282-[18s_a-5]_+-[9s_b-3/2]_+.

Their minimum is C, valid for all real behavioral kernels. To simplify set X=[18s_a-5]_+, Y=[9s_b-5/2]_+, Z=[9s_b-3/2]_+. Then F=281-X-Y and C=281-[X+Z-1]_+, so the gap is min(X+Y,1+Y-Z). For s_b<=1/6 this is min(X,1); for 1/6<s_b<5/18 it is min(X,5/2-9s_b); and for s_b>=5/18 it is zero because Z=Y+1. This establishes the closed form and exactly the stated strict region and maximum. QED.

## Evidence and limits

VERIFY.py executed locally with standard-library exact Fraction arithmetic. It checks all 15 node weights, eight positive leaf masses and P/Q flow identities, and 64 cross-product pairs including the boundary 5/18. It independently compares full-history Bellman minima and the three forced-common-action Bellman minima with both closed forms, and checks iff membership in the separating region. EXACT_OUTPUT.txt preserves executed stdout. The full real-parameter result is proven analytically above, not inferred from 64 examples.

The original R5 23,328 deterministic tables, 326 distinct compressed vectors, full Bellman minimum, and genuine 4D facet at the original parameter point are already preserved in R5 PROOF/VERIFY/EXACT_OUTPUT; no repeat or new facet claim at other parameters is made. Beyond the strict rectangle this particular signed normal cannot distinguish the hulls; other normals remain untested and the mother hull-equal/image-unequal existence problem remains open. Independent Driver review, native TASK CLAIM, formal proof and P000 native transfer are not obtained.

Next: at positive rational (s_a,s_b)=(1/6,1/3), use exact rational compressed-hull facet enumeration plus full-history Bellman to find another separating normal or a complete hull-equality certificate; only after hull equality is established should real-algebraic image nonmembership be attempted.
