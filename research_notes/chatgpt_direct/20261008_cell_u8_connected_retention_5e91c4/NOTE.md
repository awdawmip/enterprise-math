# U8 — connected overlap, relative retention, and a declared trial position law

Event: EM-20261008-CELL-U8-CONNECTED-RETENTION-5E91C4
Status: CONDITIONAL_MODEL_THEOREMS / ACTUAL_TYPED_BRC / UNREVIEWED / NOT_ADMITTED
Researcher: EM-DIRECT-196A46
Activity: RA-43B2B984B88EF62CACAC398A
Own public session: MCP-f3787278d1ac436f919881044b359f90
Logical conversation: chatgpt-heartbeat-cell-attraction-20261006-8b74f0 (not platform-attested)
Global read snapshot: awdawmip/chatgpt-global-knowledge@8004ac0e3f369a2ff2f81d53202c56bb20eb1e21.
EM control/science intake: d6169e0d9a19408a677c9a5392dbff3cc1a09f66.
Registration observed: 5b850ac932aee571111800941c768f88428aa696; activity blob9243bf47399f85cd9a20e14c79a0210c33637c64.

## 0. Exact advance and model boundary

Consume U7@9cd16ea1d377ba0caff2609f3897a68ed93f9010: the fixed U5 active/dormant mixing circuit cannot sustain a finite moving local response aggregate. Do not repeat its proof or tune its release parameters. The present unit instead asks which positive, source-derived *joint assembly scores* can support a finite relative-position law on unbounded X6.

Reuse the initial attraction study ae0012234dfaf2045019fc2b45c04aecd5112318, research_notes/chatgpt_direct/20261006_8B74F0_CELL_ATTRACTION_221.md: its exact positive Green path family, NOT a claim that its directional observer is native force. The cross-line triadic-interface note at 71b905027327eadf3417cddd6b4dcb54cc3eac71 remains TEST_ONLY; no force quantum is equated with a coordinate step.

NEW CHOICES, not derived physics: (i) use two source-path overlaps as association weights; (ii) compose selected associations multiplicatively, sum alternative spanning trees; (iii) use a specified Barker-type one-actor/one-native-edge proposal rule. These choices provide a constructive existence test. They are neither uniquely forced by the old response equation nor an empirical discovery of attraction. Locality of the MOVE is proved; finite-speed local availability of the all-path association score is NOT proved. Native signed triad legality, third-action provenance, indivisible action/readout and mechanical reaction remain open.

P000, six spatial axes/twelve signed directions and separately typed time are unchanged. A tree edge below is an association carrying TWO complete native paths and their source identities, not a new primitive diagonal segment or a two-force equilibrium. All backtracks/loops remain inside the path kernels. A spanning tree is a connectivity witness, not a claim that the physical field has no loops. Positions are jointly distinct; the coordinate choice x1=0 is a translation quotient, NOT a fixed physical anchor. No square-number shell, primality label, target shape or external wall is used.

## 1. A source-derived overlap with an all-depth positive BRC certificate

Let A sum the twelve native neighbors, 0<lambda<1/12 and rho=12lambda. Set

    G(r) = sum_(n>=0) lambda^n A^n(0,r).

Every ordered word has positive weight lambda^n. The point-source identity gives G>0 everywhere and sum_r G(r)=1/(1-rho). Define

    K(r) = sum_z G(z)G(z-r).

This is a positive paired-path observer: one path from each source meets at z. It is not interference amplitude, a force or energy. Reversing one path and concatenating gives a single path between the sources, with its split position distinguished. Consequently

    K(r) = sum_(n>=0) (n+1) lambda^n A^n(0,r).                 (1)

For each n there are n+1 DISTINCT split labels. The implementation merges n+1 copies as alternatives, rather than falsely changing one path's multiplicity with a scalar factor. The identity preserves finite count/total/dominant for total path length n. In particular

    K(r)>0; K(-r)=K(r); K(r)<=K(0);
    S := sum_r K(r) = 1/(1-rho)^2 < infinity.                 (2)

The upper bound by K(0) follows from Cauchy--Schwarz on translated G. Absolute summability gives K(r)->0 as |r|_1->infinity.

For K_L using total path lengths <=L, each endpoint coefficient is bounded by the unrestricted twelve-branch mass. Hence, uniformly in r,

    0 <= K(r)-K_L(r) <= tau_L,
    tau_L = rho^(L+1)*[(L+2)/(1-rho)+rho/(1-rho)^2].          (3)

The finite part and comparison geometric closures ACTUALLY use the pinned BRC. At lambda=1/48 and L=24, tau_L=79/2533274790395904. The proof is on the infinite lattice; a finite prefix is NEVER used as a hard cutoff in the dynamics. A tested proposal whose lower score is zero is rejected by the implementation as uncertified, not assigned zero probability.

## 2. Connectivity is exactly the partition criterion for this score family

Take N>=2 labelled material positions, pairwise distinct. Work modulo common translation, represented by x1=0. For a fixed simple association graph H on all N identities define

    W_H(X) = product_({i,j} in E(H)) K(x_i-x_j).

THEOREM: the sum of W_H over all relative distinct-position configurations is finite and strictly positive if and only if H is connected.

Connected case: choose a spanning tree T of H. Each extra edge is bounded by K(0). Root T at identity1. Its N-1 directed edge displacements independently parameterize all anchored positions: recursively sum them down the tree. Thus, even allowing co-occupancy,

    sum_X product_(e in T) K(displacement_e) = S^(N-1),
    sum_distinct X W_H(X) <= K(0)^(|E(H)|-N+1)*S^(N-1).

All rearrangements are nonnegative sums. Exclusion can only lower this upper bound. At least one distinct configuration exists and has positive weight, so the partition is not zero.

Disconnected case: freeze a distinct internal configuration in every component. Keep the component containing identity1 fixed and translate one other component by arbitrary t in Z6. Its internal edge weights do not change. Only finitely many translations cause collisions with the frozen other components. Infinitely many valid anchored configurations therefore have the SAME positive weight. Their sum diverges.

For a finite positive mixture of graph scores, finiteness holds precisely when every graph with nonzero coefficient is spanning and connected. Any positive disconnected term, however small its coefficient, makes this infinite-volume relative partition diverge. This is a statement about this explicit product/mixture family, NOT a theorem that every physical bound object must carry a tree or that two-body interactions cannot bind.

In particular, simply adding all pair overlaps does not define a normalizable whole-N relative density for N>=3. For four units

    X_R = (0,e1,R*e2,R*e2+e1),  R>=2,
    sum_(i<j) K(x_i-x_j) >= 2 K(e1)>0.                      (4)

The two internally intact dimers can separate without limit while retaining this score floor. Their own stability is not the intactness of the four-unit whole. This is why a total association score can miss the difference the user wants to preserve.

## 3. A constructive connected candidate without a prescribed shape

Declare a new candidate assembly score

    W_N(X) = sum_(T a labelled spanning tree on N identities)
                 product_({i,j} in T) K(x_i-x_j).            (5)

All trees are retained as alternatives; no tree is selected as the uniquely correct physical decomposition. There is no best-score or zero-residual postselection. Let t_N be their finite count. The same argument gives

    0 < Z_N^excl := sum_distinct anchored X W_N(X)
      <= t_N*S^(N-1) < infinity.                            (6)

Consequently pi_N(X)=W_N(X)/Z_N^excl is a well-defined translation-free relative distribution. This is statistically localized: it has tight, exponentially decaying diameter tails, not an absolute location or a hard maximum diameter.

For graph distance radius R let T_K(R)=sum_(|r|_1>R)K(r). A path reaching such r has length >R, so T_K(R)<=tau_R from (3). If every edge of a spanning tree has length <=R, every pair of material positions is at distance <=(N-1)R. A union bound on its N-1 increments gives

    pi_N(diameter>(N-1)R)
      <= min(1,t_N*(N-1)*T_K(R)*S^(N-2)/Z_N^excl).          (7)

The denominator is the positive excluded partition, not silently replaced by its co-occupancy upper bound. One tested distinct configuration gives a conservative positive lower bound if a numeric tail certificate is desired. This bound concerns relative shapes only; whole-object translation need not have a finite stationary law. Even a positive recurrent shape chain can make arbitrarily large rare excursions over an infinite history. No pathwise bounded radius is claimed.

For N=2 the excluded normalizer is EXACTLY S-K(0). Thus

    pi_2(|x2-x1|_1=1) = 12 K(e1)/(S-K(0)).                  (8)

At lambda=1/48, the executed all-depth interval is

    0.6758097246486349... <= this fraction
                          <= 0.6758097246491538... .

This is a conditional mathematical stationary fraction, not a measured natural frequency.

## 4. A local-step trial dynamics that actually has this relative law

For a joint state X choose one of its 12N proposal labels (actor a, signed port p) equally. Move ONLY actor a by that ONE native edge to proposed Y. Collision proposals remain wait branches. For a distinct Y choose

    alpha(X,Y)=W_N(Y)/(W_N(X)+W_N(Y)),                       (9)

otherwise wait. This is the declared Barker rule; it is not a force-to-velocity derivation. Each proposal retains both accepted and rejected contributions. Its reverse label is (a, opposite p), with the same proposal weight q=1/(12N), and

    W_N(X)*q*alpha(X,Y)
      = q*W_N(X)*W_N(Y)/(W_N(X)+W_N(Y))
      = W_N(Y)*q*alpha(Y,X).                               (10)

Therefore (6) is invariant for the relative chain. Moving actor1 induces a rechart of all other relative coordinates, not a simultaneous physical jump of those actors. Multiple proposal labels leading to one relative state are summed with their multiplicity; each has the above reverse bijection.

For 2<=N<=6, irreducibility also has a direct path proof. Z6 minus at most N-1<=5 forbidden sites is connected: from any free point select a coordinate line containing no forbidden site (each other site can spoil at most one of six lines). Travel first along that clean line to a coordinate value not used by any forbidden site, then set the remaining coordinates to a common remote point with similarly fresh coordinates. Paths from both endpoints meet there. Move the labelled materials successively into distinct remote parking sites and then into the desired distinct destinations, avoiding at most N-1 others at each move. All accepted edge weights are positive. Positive rejection on every finite score supplies aperiodicity. Standard countable-chain consequences may then be applied; no practical mixing-time or experimentally realized equilibrium is claimed here.

This is OUTSIDE U5/U7, not a repair that invalidates them. W_N changes relative-motion preferences through a nonuniform connected score. It is not propagation by the fixed doubly stochastic U2 scattering table. The old active/dormant field, held requests and measured radiation are NOT replaced, reset, translated, or asserted to supply the new score automatically. A physically sourced local mechanism that maintains/accesses this score, and its reaction/cost, remain missing. The scalar score is sufficient only for the explicitly memoryless trial law (9); future operations reading individual graph/path histories require those records.

## 5. Actual original-four calculation and truncation honesty

At lambda=1/48, L=24, full-path uniform remainder (3) bounds every pair weight. For the original preparation (0,e1,e1+e2,e2), let a=K(e1), b=K(e1+e2). Summing ALL sixteen labelled trees gives the exact polynomial

    W_4(square221)=4*a*(a+b)^2.                             (11)

Its terms represent four all-side trees, eight two-side/one-diagonal association trees, and four one-side/two-diagonal association trees. A diagonal association still consists of native path pairs; it is not a primitive diagonal force.

Executed score intervals (rounded only for display):

    square221: 0.0003571847086301301 ... 0.00035718470863136634
    four chain:0.00008947173961188242... 0.00008947173961249001
    four star: 0.00011187931945220731... 0.00011187931945283521

These are unnormalized scores for labelled states with the same N. They are NOT probabilities of geometric shape or isomorphism classes: degeneracy/multiplicity would have to be included. The comparisons do not prove the square maximizes this score over every configuration and do not make perfect-square cardinalities special.

The original square has 48 single-actor proposals: eight collide and wait; forty have distinct destinations. Their true conditional acceptance intervals have two symmetry classes: eight in-axis extensions, about0.0247324094922; thirty-two departures along the other four axes, about0.0337188714199. The unconditional one-query moving weight is about0.0266013158621. Waiting is not primitive equilibrium or complete-state zero.

Because infinite K is not a finite rational table, the executable carefully separates TWO objects: (i) intervals for the exact candidate (9); (ii) a one-query rational surrogate using the positive prefixes K_L, WITH a bound on its distance to the true query. It never iterates a finite-support surrogate into artificial confinement.

If old score is in [oL,oU] and proposed score in [nL,nU],

    nL/(oU+nL) <= alpha <= nU/(oL+nU).                      (12)

The surrogate alpha0=nL/(oL+nL) lies in this interval. For each proposal, TV between its binary accept/wait choices is |alpha-alpha0|. Averaging over labels and projecting to joint positions cannot increase TV. Summing q*max(alpha0-alphaL,alphaU-alpha0) therefore certifies the complete query. For the original square this bound is <5.384e-13. Its surrogate contains all88 positive branches (8 collision waits plus2*40 vacancy decisions), total weight1. This is not an unbounded exact-path simulation or a native probability measurement.

Four-unit dimer separations R=2..6 were also executed. Their pair-sum score stays above2K(e1), approximately0.0858016989705. The connected score drops from about5.6397e-6 to2.9102e-12, with certified positive all-depth intervals. The infinite separation and partition conclusions come from the proof, not these samples.

## 6. Execution, attribution and remaining work

Actual final run: 5692 assertions. Actual core calls, including comparison-tail construction: edge3230, propagate88102, recoalesce89294, recurrent3. The result records the exact counters; an isolated same-author repeat is separately verified. The checks cover all endpoints through five native bulk steps; 36 split/glue identities; every labelled tree on N=2,3,4,5; finite tree-increment reconstructions; nested all-tail link intervals through total length28; five complete local proposal sets; all24 material relabellings and representative signed-axis/translation changes; split dimers and two additional lambda parameters. No full-state enumeration at depth24, long trajectory, native force experiment or independent review is claimed.

Unchanged dependencies: packet_router.py blob7465f5aa16cbb8fba61ba4be80f8a6884b879c53 and its brc_weighted.py blob3f205696709e847909958a153f8fe10d3f6b70f0. The inherited adapter removes only two unused relative imports and verifies unchanged function/class ASTs. Scientific path extension, concatenation, tree product, alternatives and trial composition actually use those BRC functions. Ratios, interval contrasts and comparison bounds are typed observers/normalizers, not signed response destruction or a conventional simulator renamed BRC. Ordered microscopic words are reconstructible from the finite grammar, not individually serialized forever.

Barker/Metropolis detailed balance is established prior art, not a new natural law. Primary attribution: C. Andrieu, A. Lee, S. Livingstone, A general perspective on the Metropolis-Hastings kernel, arXiv:2012.14881v1 (official abstract read); Gautam Iyer's own CMU lecture, Metropolis Hastings Revisited (2024), definitions/proof and Barker remark8 read. The elementary positive path and connectivity proofs above are self-contained. Public pages: https://arxiv.org/abs/2012.14881v1 and https://www.math.cmu.edu/~gautam/c/2024-387/notes/09-metropolis-hastings2.html . No claim of inventing spanning trees, graph products, Green functions or MCMC.

Dedicated literature query KQB3008 concerned an initially considered ground-state-transform route: matching request769e935967db56932b4ef5eb0188eb09efc7d625341b80ce5bba6eda54a6e46d, batch06e45530-72bf-4fb0-b77d-5fbda17cda9c. It returned outer FAILED / child PARTIAL with three off-topic metadata/abstract records. They are not theorem evidence, not a clean cache hit; originals remain in that Issue. That ground-state route was not promoted into a result here. Cache raw/catalog archival remains a separately recorded debt.

Exact next scientific issue: derive or falsify a local, source-accounted realization of the connected assembly dependence using admissible triadic ACTION events, including reaction and score-update cost after a material moves. Connectivity selection and the Barker rule must not be smuggled in as consequences of P000. Alternatively a different connected graph family gives another admissible mathematical candidate, showing nonuniqueness of the current premises. The current construction does not determine unique final positions, solve an autonomous material-plus-field heartbeat, or detect primes. It proves a specific distinction between persistent parts and an intact whole, and supplies one precisely typed finite relative-law candidate beyond the excluded U5 mixing model.
