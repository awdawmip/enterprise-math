# Arbitrary automorphisms of the full native Cell adjacency relation

LOCAL AUTHOR CANDIDATE / UNREVIEWED AT CREATION.
DERIVED / RESULT_ONLY / STANDARD_COMPOSE; noncanonical applied note, not a new axiom, Tool, Paper or Task.
Sole new author: EM-FREE-CF1677. Root supplies scope/control coordination and zero mathematical vote.
This artifact has no author Source or independent technical whole review at creation. Actual complete author selfreading and oncefreeze are subsequent observations.

## 1. Exact relation, whole and information gap

Use the already supplied native spatial Cell torsor, with its six signed integer axes and free Z^6 action. Choose an anchor a only to write coordinates. Every Cell is uniquely a+z with z in Z^6. The entire spatial Cell population is retained: there is no finite box, sign/parity/norm filter, omitted axis, occupancy array, packet or selected mass.

Put E={+e_1,-e_1,...,+e_6,-e_6}. The designated relation is exactly the original undirected primitive adjacency

    x ~ y  iff  y-x is in E.                                      (1)

Here coordinate letters stand for actual full six-coordinate Cells in the chosen chart. A graph automorphism means a bijection f of ALL Cells such that

    x ~ y  iff  f(x) ~ f(y).                                      (2)

The observer in (1) is the union of the twelve primitive neighbor relations; it does not retain a separate directed axis label on each edge. Requiring each directed label to be fixed is a stronger, different condition. Conversely, (2) is not a claim that every other native relation, physical angle or decorated packet is preserved.

The finite information gap is whether an arbitrary bijection satisfying (2), without any assumed linearity, affine form or coordinatewise action, must already have the following form:

    f(a+z)=b+sum_(i=1)^6 z_i epsilon_i e_(pi(i)),                   (3)

where b=f(a), pi is a permutation of the original six axes, and every epsilon_i belongs to {+1,-1}. The fixed coordinate frame used on the right is the same original native frame, based at b. The converse is also claimed: every map (3) preserves (1).

This is a global relation-preserver question, different from the earlier finite quadratic sensor fibers, readout separation, occupancy-fiber move palettes and weak differential-chain automorphisms. The primitive supplies (1), but no affine hypothesis is inserted into (2). The argument below pays that missing implication directly.

The kill conditions were: stop if an extra physical metric, Euclidean angle, plane, time law or unprovided operation is needed; stop or mark REUSE if an already covered exact full-population statement is found in the later bounded coverage step. A standard grid-graph rigidity argument is only a DERIVED/COMPOSE consumer, not a new mechanism. Exact library novelty is UNKNOWN. No current-result/router/task/catalog was opened to choose this question or construct its proof.

## 2. An intrinsic test for opposite neighbors

For a Cell x write N(x) for its entire set of twelve neighbors. If s,t are distinct elements of E, then

    N(x+s) intersect N(x+t) =
      {x}                  if t=-s,
      {x, x+s+t}           if t is not -s.                        (4)

This is a finite integer-coordinate identity in the supplied full torsor, not an imported angle rule. To check it, a common neighbor has the form

    x+s+u=x+t+v,  u,v in E,  so u-v=t-s.                         (5)

If t=-s, the right side has a single coordinate equal to +2 or -2. Two signed unit vectors can have that difference only with u=-s and v=s. The common neighbor is x.

Otherwise distinct s,t have different coordinate axes. The right side has two nonzero coordinates, each +1 or -1. A difference of two signed unit vectors has those two coordinates only in the two possibilities

    (u,v)=(-s,-t)  or  (u,v)=(t,s).

They give x and x+s+t respectively. Both are actual common neighbors, and x+s+t differs from x. This proves the whole equality in (4), including exhaustion.

Because a bijection satisfying (2) maps each neighbor set exactly onto the corresponding neighbor set and commutes with intersections of such sets, the cardinality in (4) is preserved. Thus two distinct neighbors of any vertex are opposite precisely when their common-neighbor set has one member. Every graph automorphism preserves this intrinsic pairing. This conclusion has been derived from the original adjacency relation, not assumed as a labeled-axis rule.

## 3. The local signed unit increments cannot vary with the vertex

Use the original integer coordinates to write f and, for each s in E, define the actual increment

    d_s(x)=f(x+s)-f(x) in E.                                      (6)

At each x, the map s -> d_s(x) is a bijection E -> E, since f maps N(x) onto N(f(x)). Preservation of the opposite-neighbor pairing in Section 2 gives

    d_(-s)(x)=-d_s(x).                                            (7)

We now prove, for every s,t in E and every x,

    d_s(x+t)=d_s(x).                                              (8)

First let t=s. At x+s, the backward increment is

    d_(-s)(x+s)=f(x)-f(x+s)=-d_s(x).

Applying (7) at x+s yields d_s(x+s)=d_s(x). Applying that same equality with x replaced by x-s also gives d_s(x-s)=d_s(x). Hence (8) holds for t=s and t=-s.

It remains to take t distinct from both s and -s. The original two neighbors x+s and x+t have the unique other common neighbor x+s+t. Their images are the two nonopposite neighbors f(x)+d_s(x) and f(x)+d_t(x). Formula (4), applied in the same full target Cell torsor, says that their unique common neighbor other than f(x) is

    f(x)+d_s(x)+d_t(x).

The bijection maps x+s+t to that other vertex, rather than to f(x). Therefore

    f(x+s+t)=f(x)+d_s(x)+d_t(x).

Subtracting f(x+t)=f(x)+d_t(x) gives (8). This proves all cases of (8).

Every two native Cells are joined by a finite sequence of the original signed unit steps: write their six integer coordinate differences and take the corresponding finite axis steps, with the correct signs. Applying (8) along that sequence shows that, for fixed s, d_s(x) is independent of x on the ENTIRE graph. There is no bounded-radius assumption or missing infinite-support case: each particular displacement has a finite integer path, which is all this argument uses.

The four vertices in the second case are full X6 Cells with all other coordinates retained. Referring to this four-edge word does not posit an independent native two-dimensional plane or a lower-dimensional world. No diagonal displacement is promoted to a primitive direction.

## 4. Integration, exact signed affine form and converse

At the anchor a, the bijection E -> E in Section 3 maps the six opposite pairs bijectively to the six target opposite pairs. Consequently there are a permutation pi and signs epsilon_i such that

    d_(e_i)(a)=epsilon_i e_(pi(i)).

By (8) and connectivity the same equality holds at every Cell. Equation (7) supplies the corresponding negative increments.

Starting at a and following the finite signed-axis path for an arbitrary integer vector z, the image displacement is the sum of these constant increments. Negative coordinates use the paid negative increments rather than a positivity convention. The endpoint identity is exactly

    f(a+z)=f(a)+sum_(i=1)^6 z_i epsilon_i e_(pi(i)),

which is (3). Independence of the chosen path follows here from the already given single-valued f; the displayed coordinate path suffices to establish the formula for every z. No separate path-independence law is being inserted.

Conversely, a signed coordinate permutation sends E bijectively onto E and has an inverse of the same form. The anchor-change map a+z -> b+z is a bijection and leaves all coordinate differences unchanged. Thus every map (3) is a bijection and satisfies both directions of (2). This pays existence and the inverse, not merely necessity.

Once a and its image b are specified, the six actual images f(a+e_i) determine pi and the signs uniquely. This is a consequence within the classification of automorphisms; it is not a claim that seven arbitrary observations identify an unrestricted Cell map or a physical object.

The intended conclusion is now complete for arbitrary bijections of the full designated adjacency relation, with no affine assumption. No claim about all endomorphisms, local embeddings, partial maps, labeled directed-edge preservers, arbitrary norm preservers or other native relations has been proved.

## 5. What is preserved, and what this does not manufacture

The proof retains every raw signed six-coordinate Cell and the entire binary adjacency relation jointly. It is not a collapse of separate marginals or a quotient that merges distinct Cell identities. For any actual finite adjacency word x_0~x_1~...~x_k, applying f gives a word of the same length, and the inverse gives the reverse correspondence. This is just pointwise preservation of the defined mathematical relation under a bijection.

A finite adjacency word in this statement is a sequence of spatial Cells. It does not assert that a physical process traverses those edges at assigned times, that arbitrary paths are dynamically permitted, or that spatial Cell identity determines a decorated packet. No time coordinate, speed, interaction law, branch, population mass, field value or provenance is silently introduced.

The proof never uses Q, squared distance, a Euclidean inner product, a 90-degree convention, continuum topology or a physical reflection law. In particular, calling a signed permutation an automorphism of (1) does not call it a physically realizable native rotation or an automorphism of every original native PERP_E relation. The underlying basis and torsor are the original supplied ones. Anchor changes are changes of chart, not a declaration of a globally distinguished zero.

This result is a conventional mathematical rigidity consumer of the supplied primitive adjacency graph. It does not repair a missing Native dynamics law, settle any old physical task, or convert FREE registration into Working Truth, claim authority or scientific acceptance.

## 6. Actual inputs, warm history, coverage and publication boundary

The load-bearing input is the already actually read original local primitive

    /workspace/enterprise-math/definitions/
    ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md

whose full file has 13110 UTF8 bytes, SHA256
e3785a95908022f156b4185a83c33de795afd7389e9cfbd16394c25af19f6187
and Git blob e266c103cae02550c8bbaa794958f3423b41d151.
My actual semantic intake was original lines 1-180, including the complete necessary free-Z6 torsor and twelve signed unit adjacency sections. It was NOT a complete reading of all366 lines. The present proof does not require its unread remainder.

The original P000 local JSON was actually whole-read including hard_errors:
p000_reality_foundation.json,20915 bytes,
SHA256 a49985914104fcbc039436692c18dc78dc2f441919971e99390931ae64504b48,
Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
It supplies the fixed native six-axis scope; this note does not prove or replace its axioms.
The already whole-read HEARTBEAT_WORLD_NATIVE_X6_TIME.json,6476 bytes,
SHA2564b20d874f424815ab5f87de9d76fea9b9879b3f22db7466639e36390bc976c3b,
Git blob94a02d067be2b039ca4c0f7ffedb5ebde8430e08,
supplies the static-spatial typing boundary. The already whole-read
ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json,10911 bytes,
SHA25622e17d9bf7f3cb644f5f91785b8c80f82820462d7ddefc72abf2d1acc7da033b,
Git blob3923890d77a02d84b772f789e6912dd14f220d14,
is a retained scope/preservation constraint, not an extra rigidity theorem used as a premise.

These exact local bytes/read scopes were acquired in my genuine completed Native sensor whole review. They are reused as my own actual custody, not borrowed from another actor's API or inferred from a prior role. They remain LOCAL_BYTE_QUALIFIED primitive inputs, not newly claimed managed remote primitive Sources. The separate Native sensor theorem and its independent vote are not premises of the rigidity proof.

All of my native observer, integer-kernel, graph and broader mathematical backgrounds, together with the new private candidate reasoning in this scope, are warm/NONZERO. This is not a cold or zero-private-thought research lane. Root asked me to choose a different genuine primitive-level obligation but supplied no proof, formula or repair. No peer was sent a tentative construction or asked to supply a patch. Sole actual construction/repair author of this new proof is CF1677; actual new construction/repair supplied by others is0.

The candidate was chosen using only these already genuinely read primitives. Before its first freeze I did not open current-result/router/nearby-task/catalog bodies or conduct a result-library search to select or shape the proof. Postfreeze bounded coverage/dedup is a separate subsequent obligation. At creation, exact prior same-scope coverage and novelty remain UNKNOWN. If an existing exact full-population arbitrary-automorphism theorem is found, its covered content must be marked REUSE. General familiarity with grid graphs is not a new Tool or a first-discovery claim.

The first complete author selfreading prompted one prefreeze terminology clarification: the imprecise phrase "translation by b in the torsor" was replaced by the literal anchor-change map a+z -> b+z, since b is a Cell rather than a displacement. An API-attribution phrase was also clarified. The proof and quantifiers are unchanged; these are disclosed author self-edits before oncefreeze, with zero external construction/repair. The original first selfread is retained separately.

No scientific program, graph generation, enumeration, symbolic solver, numeric sample, new remote input, Native execution, query-budget reset or new formal Task was used. All integer cases and the global finite-path argument were checked manually. Prose persistence and necessary byte metadata are administrative execution only.

Canonical activity at this note's creation is the original same CF1677 identity at Source27/160, after the actual Source27 full12/exact-delta and true three-guard debt closure. The collector TypeError/explicitly authorized continuation history remains in that separate control receipt, not erased by this new research. Budget UNKNOWN, oldSTOP/HOLD/query limits and all warm history persist. There is no helper28 or main/author Source window for this note. Meaningful later integration, any true independent whole review and any Source publication are separate real future actions; none is prefilled here.
