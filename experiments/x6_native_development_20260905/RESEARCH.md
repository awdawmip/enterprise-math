# X6 Cell/path development: construction and seam obstruction

Date: 2026-09-05. Source: enterprise-math@c53492f9e2946f2b10f8b1000fbf0d67da2db27a.
Status: CONDITIONAL_CONSTRUCTION / EXACT_SELF_CHECK / NOT_NATIVE_FOUNDATION_PROMOTION.

## Premises and typing

P000 remains the given six-spatial-axis premise. Group rank, word length and graph degree are not used to infer spatial dimension. PF packets have quantity one; each actual adjacency event has count one. Reversal, loops and revisits are allowed. R061 supplies separately typed local endpoint displacements and a directed gauge; a bare PF_PATH is not automatically such a displacement. The accepted K4/S4 atlas supplies six axis labels and twelve incidence flags.

This construction ADDS an explicit ideal completion rule: four homogeneous local endpoint systems act at every candidate packet, and only their internal endpoint coalescences are initially imposed. This is a candidate global model, not a proof that PF alone supplies all these channels or uniquely chooses this model. In particular same-axis labels in different charts are not silently identified as the same native packet orbit.

Source definitions: PACKET_PATH_FOUNDATION.md; FOUNDATIONAL_LOGIC.md; p000_reality_foundation.json; definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md; definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md; definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md; research_notes/SIX_AXIS_DERIVED_FOUNDATION_CLOSURE_V2_20260905.md.

## 1. Explicit endpoint construction

For v in {A,B,C,D}, let D_v have three positive local events t_vw, w!=v, with commuting ENDPOINT actions and product(t_vw)=1. The latter is a three-event endpoint return, not path identity, not a primitive native vector equation. D_v is Z^2 with local event codes (1,0),(0,1),(-1,-1). A local derived displacement (x,y) is displayed as can(x,y,0); this is not primitive point-address quotienting.

Set G_dev=D_A*D_B*D_C*D_D. Its underlying set X_dev is a concrete candidate packet set. A packet normal form is a sequence (v_i,d_i) of nonzero local displacements with neighbouring v_i distinct. The empty normal form is an anchor PACKET c*, never the geometric origin O_E.

Reduction combines neighbouring equal-chart displacements and erases zero sums. It terminates since each step shortens the sequence. For uniqueness, let each D_v act on reduced words by right-tail insertion, addition and zero deletion. These are inverse permutations and satisfy the local additive laws. A nonempty reduced word sends the empty word to itself as a nonempty word, hence cannot represent the identity. Distinct reduced words induce distinct images of the empty word. Thus the normal form is unique. This gives a decidable exact endpoint algorithm.

Given four homomorphisms D_v->K, multiply their images along the reduced sequence. Local reduction preserves the product, so this is the unique extension to G_dev. The same argument extends four declared local permutation actions on a set to a G_dev action. These are standard free-product methods, not a novelty claim about group theory. A primary reference for the broader graph-product/normal-form framework is Yang Dandan and Victoria Gould, On graph products of monoids, arXiv:2102.06409.

## 2. Actual paths, local recovery and rotation

At x, an event (v,w,+/-) moves to x*t_vw^(+/-). All candidate packets carry unit quantity one. The ordered event list and all prefix packets are retained separately from its reduced endpoint. Empty path: 0 events, 1 visited packet. Immediate return: 2 events, 2 visited packets. Local triangle: 3 events, 3 visited packets, endpoint c*. Reversal flags are not new spatial axes and do not invert positive branch weights.

Each right coset xD_v injects and has exactly the local triangular centre adjacency. A three-packet elementary incidence is a separate IncidenceVertex type; it cannot be supplied as a PacketPath start. This prevents identifying the native triple-intersection origin with the anchor packet. A fully native endpoint-decoration bridge remains separately required.

rho_g(t_vw)=t_(gv)(gw), g in S4, preserves each local presentation and hence extends uniquely. It is an automorphism, rho_g rho_h=rho_(gh), and acts directly on normal forms. It preserves adjacency, ordered paths, weights, counts and axis-label covariance. This proves an S4 action, not the classification of the entire native rotation group.

Use the existing V2 proper rotation_matrix and flag_ray. The map p:G_dev->Lambda_FCC adds the integer q(v,vw) along the endpoint word, where Lambda_FCC is the even-coordinate-sum lattice. The local sum-zero relation makes this well-defined. It satisfies p(rho_g x)=R_g p(x). It is injective on each individual local D_v, not globally. Scaling its local rays by 1/sqrt(2) recovers the selected carrier's unit centre spacing; circles and their radius stay downstream observations.

The shortest witness h_uv=t_uv t_vu has zero p but two nonzero distinct-chart syllables, so it is not the identity in G_dev. This is precisely information that the FCC readout erases.

## 3. A derived gauge and an exact seam no-go

Let ell_v(d)=sqrt(sum can(d)_i^2), the accepted local directed gauge. Define L_dev(x)=sum ell_vi(di) on the reduced word. It is positive off identity. Since can(d+e) is componentwise bounded by can(d)+can(e), local triangle inequality holds. Every word reduction decreases or preserves total cost, proving L_dev(xy)<=L_dev(x)+L_dev(y). Thus D_dev(x,y)=L_dev(x^-1 y) is left-invariant and directed. S4 permutes the three local display components and preserves it.

Every subadditive group gauge agreeing with all ell_v is bounded above by L_dev, by decomposing the word into its local syllables. Hence L_dev is the MAXIMAL extension within this explicit class, not the unique native length. It is not event count: a positive local step has gauge 1, its inverse has gauge sqrt(2), while both are one event.

The additive local gauge-isometry group is exactly S3: the three positive events are exactly the three nonzero elements of squared gauge 1, so any additive isometry permutes them; each permutation indeed preserves the relations and gauge.

Now impose reciprocal carrier seam identification t_uv=t_vu^-1. The left side has local gauge 1 in chart u, the right side has gauge sqrt(2) in chart v (it is the sum of the other two positive local axes). Therefore NO slice-independent endpoint gauge can both make this identification and restrict to all existing local directed gauges. This excludes only that untyped gluing; framed gauges, groupoid transitions and richer state fibres are not excluded.

Equivalently, an axis-group gluing k->+k is gauge-preserving, whereas matching the two fixed opposite FCC rays requires k->-k. Those two demands cannot be met by a single unframed axis identification.

## 4. Complete classification of two naive seam quotients

For reciprocal seams, write a=t_AB,b=t_AC,d=t_BC. Local commutations in A,B,C make a,b,d pairwise commute. All other forward flags reduce to t_AD=(ab)^-1, t_BD=a*d^-1, t_CD=b*d. The D relation is then automatic. Conversely send a,b,d to independent Z^3 generators; all relations hold. Therefore G_dev/normal_closure{t_uv t_vu} is exactly Z^3, with no torsion or further hidden relation.

Its FCC readout is (a,b,d)->(-a+b,-a-d,b-d), whose inverse is ((z-x-y)/2,(x+z-y)/2,(x-y-z)/2) on the even-sum lattice. Thus the seam normal closure is exactly ker p. This is a classification of endpoint algebra, NOT an inference that native space has three dimensions.

For same-positive seams t_uv=t_vu, the corresponding presentation has a,b,d commuting, the other three directions -(a+b),-(a+d),-(b+d), and final relation 2(a+b+d)=0. Hence that quotient is Z^2 plus Z/2. This recovers the V2 unsigned-star warning and is not promoted to native identity.

## 5. Exact reduction of the remaining native-state question

Consider only systems with four total local group actions satisfying the declared local laws and with all packets reachable from c*. Let H={w:c*·w=c*}. H is a subgroup. The map H w -> c*·w is a bijection from RIGHT cosets to states, since H w=H z iff w z^-1 in H. Equality is stable under any common right suffix. H need not be normal; universal left-context equations would require additional normality.

An S4 action fixing c* descends iff rho_g(H)=H. A point-valued FCC readout descends iff H is contained in ker p. Under that condition each local leaf remains injective: a conjugated local difference in H has zero p, and p is injective on the local factor.

Thus X=H\G_dev is an exact parameterization for THIS ideal local-action class. H={1} gives the free development; H=ker p gives the flat quotient. The class does not cover undeclared partial/state-dependent local channels; those require a typed path groupoid. General subgroup membership is not claimed algorithmically solved.

The genuine missing datum is now the actual cross-chart return/congruence law and its coverage of native adjacency. Identical axis labels or carrier positions cannot supply it. In the free development distinct leaves generally share a packet and labels but not an entire native axis trajectory; actual axis gluing is still unproved.

## 6. BRC reuse and validation

T0_BRC is actually reused through the pinned BranchKey implementation. T6's future-fibre constancy test is applied: a=t_AB,b=t_CD give ab and ba with equal six-count/length/weight/frame summaries but different endpoints; adding a^-1 b^-1 returns ba to the root and does not return ab. T7's exact V2 matrices are actually reused, with their action extended to packet words.

The local 3-4-5 example has 35 distinct seven-event histories, one endpoint, unit-weight total 35, Boolean support 1, and gauge 5. An event of weight 2/3 followed by its inverse returns in endpoint but keeps event count 2 and weight 4/9.

Both check scripts were run with SymPy 1.14.0. The independent checker imports neither x6_development nor vendored six_axis/atlas_brc: it uses min-zero triples and repeated leftmost rewriting, compared with the main integer-pair tail-stack algorithm. All 14,425 histories of length at most three have identical endpoint digest dfd27fa76b4d6acffc3b667bff78df8fca7e6b05145ca70d87bec4f2932e7e10. Further primary checks include 4,704 local gauge rotations, 4,608 carrier-equivariance cases, 600 cases per group/composition invariant and 6,561 exact local triangle certificates. Independent signed/unsigned incidence Smith forms and 24 flat actions/576 products also pass.

Seven negative guards are exact counterexamples to false claims, NOT injected-code mutation testing. Finite checks do not replace the proofs. This is independent implementation within one research execution, not external review, Lean, repository CI or Foundation promotion.

Vendor source alignment: the previously delivered V2 ZIP contains an appended archive-only addendum in six_axis.py. This experiment deliberately uses the exact current 12648-byte main source at blob 2a16d04bd6c5e6d50e0fdd20e455f854b71bdcf4; all checks were rerun after alignment. Original ZIP unchanged. atlas_brc.py remains exact blob 881a34d1919da64a85e6e06902ec3f23654a147e.

Run: python check_development.py && python check_reference.py.

Remaining: actual native same-axis orbit identification, local-channel coverage, the correct return subgroup/groupoid, and native global metric/incidence admission. Do not report this conditional candidate as unique X6_native.
