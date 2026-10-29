# EC49AB: exact causal supporting facet and first post-wedge boundary

Status: AUTHOR_PROVED / EXACT_BIGINT_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED (2026-10-29). Source: author-side continuation of EC49AA, immutable commit 3a4ef17a056ed340607f74ef6a26933b7512c2d9, Draft PR #1682. This is an auxiliary positive-rational source-labelled BRC observer, not native signed-BRC amplitude arithmetic.

## Theorem, unchanged real behavioral model

Histories w=0,1,2 have prior 1/3. Before forgetting w, the observer chooses STOP or first action A0/A1 (cost 1) or B0/B1 (cost 2), with probabilities x_wc (nonnegative, each row sums at most 1). A first sensor produces u=0,1 with t_w(u)=1/2+(2u-1)(1-w)/200. After forgetting w, the observer buys S with probability s_cu depending only on c,u, then if bought sees z=0,1,2 and accepts with probability a_cuz; without S the terminal rule sees only c,u. Decisions use independent fresh behavioral coins with no retained ex-ante shared seed. Sources are P(w,u,z)=t_w(u)*(1/6 when w=z, else 1/12) and Q(w,u,z)=t_w(u)/9. They each have 18 strictly positive normalized leaves and identical marginal P(w,u)=Q(w,u). Costs under EACH source are C1=43/48 and C2=7/8. Set alpha=P(accept), beta=Q(accept), delta=alpha-beta.

**Universal exact inequality, for every real admissible causal policy and delta>=0:**

    alpha >= 3*delta + (5346/2341)*max(0,delta-17/288).                (1)

**Sharp entire interval:** The exact lower boundary for all real 0<=delta<=3047/38400 is the right side of (1), and rational delta admits a rational fresh-coin implementation. In particular,

    alpha_min(delta=1/16) = 915/4682, beta=4979/37456.                (2)

This closes EC49AA's previous strict enclosure 19689/103424 <= alpha_min <= 9/46 and also proves a genuinely sharp post-threshold segment, not merely a new sample.

## Analytic reduction to 288 finite endpoints

Let T=sum_wc x_wc, b=sum_{w,c in B}x_wc, m=sum_wcu x_wc*t_w(u)*(1-s_cu). Both budgets imply

    T+b=43/16; T-m=21/8; b+m=1/16; 0<=b<=1/16.                       (3)

Let h_w=1-sum_c x_wc and b_w=sum_{c in B}x_wc, so sum h_w=H=5/16+b, sum b_w=b, and the two A labels have total mass 1-h_w-b_w in history w. Because H+b=5/16+2b<=7/16<1, the row capacity h_w+b_w<=1 is automatic for every pair of simplex allocations. For fixed b, each A-mass split can be expressed as a convex combination of pure A0/A1 tags, and each B-mass split as a mixture of pure B0/B1 tags. Each h and b vector is itself a convex combination of its three single-history simplex vertices. Therefore EVERY feasible prefix x at fixed b is a convex combination of 144 arrays indexed by STOP history i, B history j, three A tags a_w and a B tag q:

    h_w=(5/16+b)*[w=i],  b_w=b*[w=j],
    x_{w,a_w}=1-h_w-b_w, x_{j,q} += b.                                  (4)

For each choice of labels, x(b) is affine in b, hence a convex combination of its b=0 and b=1/16 endpoint arrays, with coefficients 1-16b and 16b. Thus all legal real x lie in the convex hull of 144*2=288 explicit rational prefix arrays. The endpoint arrays at b=0 are a relaxation for the missing-S cost, not fictitious legal source policies.

For a sensed observation atom c,u,z (with unit acceptance), let P_cuz(x),Q_cuz(x) sum x_wc times the corresponding P,Q leaf over w. Define D_cuz=P_cuz-Q_cuz and L_cuz=3Q_cuz-2P_cuz. With v=x_zc*t_z(u) and r=sum_{w!=z}x_wc*t_w(u), exact source algebra yields

    D_cuz=(2v-r)/36,   L_cuz=r/6 >=0.                                 (5)

A legal sensed acceptance multiplies this by y_cuz=s_cu*a_cuz in [0,1], independent of erased w. For early STOP and paid-but-no-S, the accessible P,Q marginal is identical, so discrimination is zero and L=3beta-2alpha contributes nonnegative source mass. Consequently total delta=sum_cuz y_cuz D_cuz and total L:=alpha-3delta>=sum y_cuz L_cuz>=0.

Set k=5346/2341 and d0=17/288. The attached exact BigInt verifier computes for each of the 288 source-defined endpoint arrays

    F_v(k)=sum_cuz max(0, k*D_cuz(x_v)-L_cuz(x_v))
          <= k*d0 = 5049/37456.                                       (6)

All 288 exact inequalities pass; 48 labeled vertices saturate (6), all at b=1/16. The checker enumerates 3 STOP choices * 3 B choices * 8 A-tag assignments * 2 B tags at both budget endpoints, uses rational source leaves, and checks normalization and the witness. This is an exhaustive justified FINITE certificate, not interpolation from numerical samples.

For any endpoint v and real y in [0,1]^24, the weighted score k*sum y D(v)-sum y L(v) cannot exceed F_v(k). For general legal x=sum lambda_v*x_v, D and L are linear in x. Use the same legal y on EVERY vertex, average the endpoint inequality and retain the nonnegative unsensed slack. It follows that

    k*delta - L <= k*d0.                                               (7)

Together with L>=0 and alpha=3delta+L, (7) proves (1) over ALL real independent-coin causal policies. The convex representation is only a proof of a linear upper bound: it does NOT allow the observer to retain a mixture seed.

## All-rational sharp witness and interval

Set w0->A0 surely, w1->A1 surely, and w2->A0 with 9/16, B0 with 1/16, STOP with 3/8. Always buy S after paid actions. Accept on (A1,z=1) and (B0,z=2), for both signals u. These two SOURCE-PURE cylinders yield

    (alpha,beta,delta)=(17/96,17/144,17/288), L=0.                    (8)

Additionally accept on the single atom (A0,u=1,z=0) with fresh probability a∈[0,1]. Its exact unthinned masses are

    P_atom=4123/38400, Q_atom=2507/28800,
    D_atom=2341/115200, L_atom=5346/115200=k*D_atom.                  (9)

Hence delta=17/288+a*(2341/115200) and alpha=17/96+a*(4123/38400), with equality in (1). At a=1, delta=3047/38400 and alpha=3641/12800. At delta=1/16, a=400/2341, and exact leaf summation yields (2) with both costs. For 0<=delta<=17/288, independently thin the two pure cylinders by the same probability delta/(17/288), giving alpha=3delta. Thus (1) is attained throughout [0,3047/38400], with rational parameters whenever delta is rational.

## Verification boundary and type separation

The finite certificate was EXECUTED in a JS BigInt rational environment using the exact source law and 288 endpoint arrays. VERIFY.js is the actual executable source and EXACT_REPORT.json contains its output. All-real coverage relies on the stated analytic simplex/convex/observer argument, not mere finite enumeration; the mathematical proof has NOT been independently peer reviewed or formally checked in Lean. This auxiliary positive source BRC readout is not a native signed/phase BRC amplitude. No automatic transfer to P000's six-dimensional X6, its three-dimensional native slice, or heartbeat dynamics; the required carrier, embedding, third-coordinate semantics and operation-preservation proof are open.

The next unit EC49AC asks for the first departure after 3047/38400 or a second sharp facet. Keep all causal products; never replace this model with the convex hull of persistent mixed strategies. No protected P000/worldview content was changed.
