# R4-EC48C — Encoder-only exact criterion for seedless BRC memory preservation

Date: 2026-10-27. STATUS: AUTHOR-SIDE PROVED + EXACTLY FINITE-VALIDATED; NOT native Result/Driver-accepted/Foundation/Heartbeat dynamics.

## Frozen sources and authority
GLOBAL_KNOWLEDGE_V1 canonical main e2d38ad0f2c3726cfad2c66d90c515e96f3ee36e; read 00_BOOTSTRAP.md, OPERATING_MANUAL.md, P000_STARTUP.json and the full P000_REALITY_FOUNDATION.json (blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE worldview and math/code/BRC policies. EM canonical main d2d534fdd3c02cbccd02f831b2989e03e6e9ae68; read AGENTS.md, PORTABLE_RESEARCH_PROTOCOL.md, research persistence and activity protocol, Heartbeat X6, residual-fidelity and joint-observer-preservation companions. Predecessor EC48B immutable commit 91d7c15573afaf7803c62e3bbdfc0aa00e52aa73, path research_notes/r4_ec48b_face_components_20261027/EC48B_FACE_COMPONENT_THEOREM.md. BRC method: REUSE_APPLIED to positive provenance-aware source labels, EC48A sign profiles and EC48B exact exposed-face theorem; EXTEND_EXISTING_TOOL for this narrow decoder-free graph, not a new primitive arithmetic.

Current connected GitHub login awdawmip with repository write permission. Native owner list returned CONTROL_QUOTA; native session start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No live CLAIM, owner verification, review or native approval is asserted. This is independent author-side auxiliary work and does not assume a native X6 trajectory or an embedding of the two-stage statistical model into the six native spatial axes.

## Declared two-stage model
Finite nonempty history alphabet H, subsequent observed label alphabet Y and K>=1. Independently normalized, strictly positive rational masses p(h,y),q(h,y) for two hypotheses. Histories carry source identity, not merely total mass. A seedless observer chooses pi_h in the probability simplex over m=1..K, then binary-declaration probabilities u(m,y) in [0,1]. w(h,y)=sum_m pi_h(m)u(m,y). Let alpha=sum p*w and beta=sum q*w; S_K is their reachable set. Complete-history Z=sum_(h,y)[0,(p(h,y),q(h,y))] is a convex zonotope. The actual declared four observations are (1-alpha,beta,2,2). Variable stopping time/depth and persistent public random mixing are excluded.

Fix each distinct positive source likelihood ratio r=p(h,y)/q(h,y). Write d(h,y)=p(h,y)-r q(h,y), T={(h,y):d(h,y)=0}, Q_T=sum_T q(h,y), and O=sum max(d(h,y),0). EC48B proves S_K=Z iff the attainable T mass while maximizing alpha-r beta=O fills [0,Q_T] for every ratio r.

## New theorem EC48C.1: exact decoder-free graph
For a deterministic history encoder f:H->{1,...,K}, assign each block (m,y) a two-bit mask M_f(m,y): 1 if some assigned h has d(h,y)>0, plus 2 if some assigned h has d(h,y)<0. Values 0,1,2,3 are possible. f is VALID iff no mask equals 3.

For each valid f, define
  L_f = sum_{(h,y) in T; M_f(f(h),y)=1} q(h,y),
  U_f = L_f + sum_{(h,y) in T; M_f(f(h),y)=0} q(h,y).

Construct a graph E_r. Its vertices are exactly VALID encoders f. Adjacent encoders f and g must (a) differ in the memory label assigned to EXACTLY one history h, and (b) satisfy bitwise M_f(m,y) OR M_g(m,y) != 3 at EVERY block (m,y).

**Statement (all finite alphabets, positive rational p,q, K>=1):**
The set of tied masses realized by all seedless support-optimal randomized K-memory observers is EXACTLY
  UNION over connected components C of E_r of
  [ min_{f in C} L_f, max_{f in C} U_f ].  (EC48C.1)

Consequently S_K=Z iff the above union equals [0,Q_T] for every distinct ratio r. Empty graph means the full support cannot be attained and the equality test fails. The mathematical identity also holds for positive real masses, while its submitted verifier uses exact integer source counts.

### Proof
(1) Support is a sum of individually bounded contributions: to attain O every positive d-cell must receive declaration bit 1 and every negative d-cell bit 0. A deterministic encoder f permits such a decoder iff no block has both signs (mask 3). On mask 1 the decoder bit is forced to 1; on mask 2 it is forced to 0; on mask 0 the bit is arbitrary. Therefore its full support-optimal stochastic decoder set is a product of intervals, with tied-mass image the exact interval [L_f,U_f]. Its deterministic decoders form a connected free-bit hypercube.

(2) Compare EC48B's graph with vertices all support-maximizing deterministic pairs (f,b), edges changing one history code or one decoder bit. For each fixed valid f, its compatible b form the connected free-bit hypercube from (1). Two such f-fibers have an EC48B edge iff the codes differ at exactly one history and there exists a SINGLE decoder b satisfying the strict positive/negative requirements of both f and g. This exists iff the union of their masks contains no 3. Those are precisely E_r edges. Contracting connected b-fibers therefore preserves components EXACTLY.

(3) The support functional F(pi,u)=sum d(h,y)pi_h(m)u(m,y) is multiaffine in the independent encoder simplexes and decoder intervals. Expansion into Cartesian deterministic corners shows that a randomized strategy with value O may put positive product barycentric weight only on deterministic maximizing corners. Its entire product-support face consists of maximizing policies, has connected one-skeleton in the EC48B graph, and conversely all such faces occur. Thus each graph component corresponds to a connected union of product faces. Their tied-mass continuous image is a compact interval; its extrema are attained at deterministic corners. By (1) and (2), the interval endpoints are min_C L_f and max_C U_f, with no attainable values outside their union. This proves (EC48C.1).

(4) Apply EC48B's exact exposed-face argument. Since p,q>0, all nontrivial support edges of Z have normals (1,-r) or their negatives at its likelihood-ratio breakpoints. Complementing every terminal declaration maps (alpha,beta) to (1-alpha,1-beta) and covers the reflected edges. S_K is star-shaped about 0 since scaling all u(m,y) by t in [0,1] scales the result. If all boundary edges of Z are covered, every radial segment from 0 to Z's boundary is therefore covered, yielding S_K=Z. Necessity is automatic. QED.

### Cheap sufficient certificate
If for every ratio r one valid f has L_f=0 and U_f=Q_T, then S_K=Z. This condition is SUFFICIENT only; failing it does not establish any gap.

### Complexity
EC48B enumerates up to K^|H| * 2^(K|Y|) joint deterministic policies. EC48C enumerates at most K^|H| valid encoders, at most K^|H|*|H|*(K-1)/2 undirected one-history candidate edges, builds masks in O(K^|H|*|H|*|Y|), and tests candidate edges in O(K^|H|*|H|*K^2*|Y|) elementary mask operations. These bounds exclude arbitrary-precision arithmetic bit cost. For raw positive integer counts P,Q separately normalized, ratio ordering and sign use exact cross products P_j Q_i-Q_j P_i at breakpoint i; tie masses are measured in raw Q units, preserving coverage by positive rescaling.

## Verification and scientific limits
The saved EC48C_VERIFY.js was EXECUTED in the connected tool runtime: over all 4,096 ordered raw P,Q arrays in {1,2}^(3*2), H=3,Y=2,K=2, 10,766 exact breakpoint faces were traversed; sign-profile histogram 1:100,2:2412,3:1584; 2,512 pairs have hull threshold <=2; 1,872 faces have >1 quotient-graph component. Its output agrees with a separately executed local Python Fraction/integer program that compared the *complete component interval multiset* and component count against the original EC48B full encoder/decoder graph on all 10,766 faces. The Python program further checked 1,900 seeded extended models, 200 hull-eligible, with 1,170 eligible faces and no observed gap. The complete standalone Python source, exact reports and cold-start package are provided as a separate downloadable artifact in the conversation.

Additional exhaustive finite sign family: H=5,Y=2,K=2, Q_raw=1 and P_raw∈{1,2,3} entrywise. 59,049 templates; 5,019 hull-eligible, 4,835 containing a center tie, 2,550 disconnected quotient graphs; zero uncovered center faces. THIS IS NOT A GENERAL THEOREM THAT CONV(S_K)=Z IMPLIES S_K=Z. Independent Driver mathematics, formal proof checker and native X6 experiment remain pending.

## Next EC48D
Use the quotient algorithm to test larger H>=6,Y>=3,K>=2 and positive nonuniform Q weights or prove an all-finite-alphabet face-reconfiguration invariant. If a counterexample to convex-hull preservation implying seedless preservation exists, return exact raw P,Q,K, a ratio, all connected-component intervals and an uncovered OPEN RATIONAL tie-mass interval. Otherwise pursue a structural proof; do not promote finite no-gap search. Separately address genuine variable-depth four-coordinate reachability; no promotion from the auxiliary two-stage model to native Heartbeat X6 is licensed.
