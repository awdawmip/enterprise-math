# Six-axis omission observations: the first integer occupation collision

Candidate-ID: FREE-X6-OMISSION-GHOST-20261016-7FEDA1
Researcher-ID: EM-FREE-7FEDA1
Research-Mode: FREE_AXIOM_DISCOVERY
Research-Activity: RA-A692ED49A332124E51EDB93A
State at first immutable capture: BLIND_CANDIDATE_FROZEN / UNREVIEWED
Blindness status: ANCHOR_EXPOSED; independent-from-old-agenda is not certified.
Semantic layer: an explicitly declared integer occupation model over native X6; a derived mathematical candidate, not a new axiom or physical law.

## Primitive state and the self-generated question

Assume P000 without proof/falsification. Native Cells form an affine torsor over Z^6 with the twelve primitive signed axis steps. Fix a Cell anchor only to write raw signed chart coordinates x=(x1,...,x6). No distinguished global origin, native plane, omitted dimension, Euclidean angle reinterpretation, final public Cell-address codec, or force-balance assertion is introduced.

The declared object is a finitely supported occupation field mu:X6 -> N0. This is an occupation decoration over the full six-dimensional native Cell space, not the complete state of a path, branch, packet or world. Every occupied Cell and its integer multiplicity is retained. Mass means the integer count N(mu)=sum_x mu(x), not positive Weighted-BRC branch mass or signed amplitude.

For i=1,...,6 let M_i mu be the five-coordinate array obtained by summing over x_i while retaining all five other coordinates jointly. Write M=(M_1,...,M_6). The bridge is exactly this line-sum map from a native Cell occupation field to a numerical array. It does not identify Cells or discard the underlying field by default.

Question with quantifiers: for all distinct finitely supported mu,nu:X6 -> N0 satisfying Mmu=Mnu, what is the least possible common integer count N(mu)=N(nu), and what are all collisions attaining that count? The full declared population includes zero counts, every Cell and every multiplicity; no arithmetic or support stratum is prefiltered.

## Frozen candidate statement

C1. If Mmu=Mnu and N(mu)<32, then mu=nu. The number 32 is sharp.

C2. If Mmu=Mnu, mu!=nu and N(mu)=32, there are two distinct integers a_i,b_i on each of all six axes such that, after possibly interchanging mu and nu,

mu = sum_{epsilon in {0,1}^6, sum epsilon even} delta_(c(epsilon)),
nu = sum_{epsilon in {0,1}^6, sum epsilon odd} delta_(c(epsilon)),

where c(epsilon) is the native Cell whose i-th raw coordinate is a_i when epsilon_i=0 and b_i when epsilon_i=1. Thus every coefficient is one, the two supports are disjoint, and their union is the complete 64-Cell Cartesian block. The a_i,b_i need not be adjacent. These are all first-count collisions, with the harmless freedom to swap endpoints or the parity labels.

C3. Equality of M is safe for the following explicitly declared future language at every finite horizon H: finitely supported nonnegative-integer convolution kernels on Z^6, chart translations, and permutations of the six positive axis labels, in arbitrary finite composition, followed by M. This is a chosen homogeneous linear operation model, not an asserted native propagation law. The zero kernel is allowed. The operation index t in {0,...,H} is separately typed discrete time/order, not a seventh spatial axis or a physical clock calibration.

C4. The same compression fails when the future language additionally allows a coordinate gate G_{i,a} mu(x)=1_{x_i=a} mu(x). Every C2 collision is distinguished by a single such gate with a=a_i, followed by M_i. This does not claim that a gate is a primitive spatial step or a physically established operation; it states the precise observer-safety boundary.

## Paper derivation, not independent validation

Lemma. Let d>=1 be an auxiliary induction parameter for arrays; this is an external proof index and does not make a lower-dimensional native world. If a nonzero finitely supported real array f on Z^d has zero sum on every coordinate line, it has at least 2^(d-1) strictly positive entries and at least 2^(d-1) strictly negative entries. Consequently it has at least 2^d nonzero entries. If its support has exactly 2^d entries, then

f = c product_{j=1}^d (delta_(a_j)-delta_(b_j)),

with c!=0 and a_j!=b_j; the product denotes the external tensor array whose explicit native use below is d=6.

Proof. At d=1 a nonzero finitely supported zero-sum sequence has both signs; support two forces opposite equal coefficients. For the induction step, slice by the first coordinate. Every nonzero slice has zero coordinate-line sums in the remaining d-1 coordinates. There must be at least two nonzero slices: a single slice cannot have zero first-coordinate line sums. Induction therefore gives at least twice 2^(d-2) entries of each sign. If total support is 2^d, there are exactly two nonzero slices, each of support 2^(d-1). Their values are pointwise negatives because first-coordinate line sums vanish. They have identical supports, and the induction equality case in one slice gives the claimed Cartesian product and checkerboard coefficient. This proves both the bound and equality classification.

Apply the lemma at d=6 to f=mu-nu. All coordinate-line sums vanish. If f!=0, at least 32 Cells have f(x)>0. At each such Cell mu(x)>=1 because occupations are integers, so N(mu)>=32; similarly N(nu)>=32. Each M_i also preserves total count, hence N(mu)=N(nu). This proves the lower bound in C1.

At N(mu)=N(nu)=32, each positive Cell of f consumes at least one unit of mu, so there are exactly 32 positive Cells, each with mu=1 and nu=0, and no additional mu occupancy. The same argument for the negative Cells gives exactly 32 negative Cells with nu=1 and mu=0, and no overlap. Thus f has exactly 64 nonzero entries and the lemma forces its checkerboard product form. Its coefficients have absolute value one. Conversely, summing a checkerboard product along any one of the six coordinates gives zero, so its two unit parity halves have identical M. This proves sharpness and C2.

For C3, all fields and kernels have finite support, so every sum can be rearranged exactly. For convolution (K*mu)(x)=sum_y K(y)mu(x-y),

M_i(K*mu)=(M_i K)*(M_i mu),

where the convolution on the right is solely on the five retained coordinate indices. Translation of mu translates the retained indices; translation along the omitted axis has no effect. An axis permutation permutes the six named readouts and their coordinate labels. Equality of the full M tuple is therefore preserved by each allowed operation, and induction on the separately typed finite operation index proves the arbitrary-H claim. This is exact factorization for this observer and operation language, not permission to erase path order, provenance, signed amplitudes, or nonhomogeneous coupling in another model.

For C4, on a first-count collision,

f(x)=product_j (delta_(a_j)(x_j)-delta_(b_j)(x_j)).

Keeping only x_i=a_i and summing over x_i gives

M_i(G_{i,a_i}f)=product_{j!=i}(delta_(a_j)-delta_(b_j)),

which is nonzero because each a_j!=b_j. The operation exposes a retained six-way joint relation that all original omission readouts missed. Thus current invisibility and safety for homogeneous linear composition do not imply safety after coordinate gating.

## Immediate consequences and falsifiers

The candidate gives a sharp integer-count obstruction to reconstructing the full native occupation field from six joint omission observations. The repair object is the actual six-way interaction field f (or an equivalent scope-certified representation); factor or marginal reconstructibility is not asserted. All signs in f are algebraic differences of two nonnegative integer occupations, not signed branch masses or forces.

Concrete falsifiers are: (i) distinct equal-M integer fields of count below 32; (ii) a count-32 collision outside the parity-block classification; (iii) an allowed C3 operation that breaks equal-M; (iv) a C2 block whose declared one-axis gate leaves M_i equal. The proof is elementary and should be checked as a whole, including equality conditions and operation typing. No program, enumeration, numerical fit, formal proof checker, or scientific computation has run. Discovery evidence is this same paper derivation; it is not labeled independent validation.

## Source and contamination ledger frozen with the claim

Foundation snapshot: awdawmip/enterprise-math at 11d5d278f808d6cf264584448cdbf2402cc50d41. Required P000/world/joint contracts were first read from exact local paths, then the primitive/reference material was fetched through managed GitHub at that immutable snapshot as stated below. Local workspace cleanliness was never claimed. No directory scan of research_notes/reviews, project Goal, task inventory, result catalog, general theorem/tool catalog, or parent mathematical state was performed before this freeze.

Primitive dependencies actually consumed: p000_reality_foundation.json; definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json; definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json; definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md; definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md; definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json; definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json. No stronger world statement is inferred from the field model.

Necessary identity/activity/runtime/context inputs consumed: canonical AGENTS.md, docs/RESEARCH_IDENTITY_PROTOCOL.md, docs/RESEARCH_ACTIVITY_PROTOCOL.md, research_identity_state_machine.json, final_response_identity_policy.json, research_axiom_candidate_state_machine.json, research_context_budget.json, tools/research_identity.py, selected tools/research_activity.py and tools/research_runtime_guard.py implementation ranges, docs/RESEARCH_RUNTIME_STATE_MACHINE.md; managed cloud runtime/network/VPN instructions and nonsecret environment policy. Original activity and runtime helpers were executed against the independently assigned local tracking key and this activity only. One incorrect identity_payload(lane=...) call raised TypeError before canonical CLI allocation succeeded; identity and budget were not reset.

Unexpected/anchoring exposure retained: the mandatory Weighted-BRC global substrate itself contains numerous detailed downstream type names, theorem/tool IDs and locators. The torsor primitive definition itself contains established spatial consequences, historical research-note names, and an open-questions section. The AGENTS router and candidate lifecycle also expose administrative result/route vocabulary and an existing Driver-ID. None of those linked research notes, catalogs, detailed theorem/tool modules, taskbooks, or open-question routes were opened. Nevertheless these exposures cannot be unread; ANCHOR_EXPOSED is retained, and no CLEAN or global novelty claim is made.

Read budget: the normal startup source-count soft maximum was exceeded during mandatory bootstrap; raw full responses, repeated local/remote reads and output truncations also exceeded the raw cold-start hard byte envelope when counted as this actual session's intake. This is a disclosed bootstrap control defect, not a passing budget audit. Full-file responses were sometimes truncated in displayed tool output; only required missing primitive/helper ranges were then read. Exact aggregate product-token exposure cannot be reconstructed from the available tool metadata and is UNKNOWN, not zero. No GLOBAL_KNOWLEDGE bootstrap or agenda was opened.

Activity registration is on main at immutable commit 4212c4644827cc103fbe9e11d5082f18d1d2d332, path research_activity_records/RA-A692ED49A332124E51EDB93A.json: 753 bytes, SHA256 ed1f2bcd6cb5d95fe70c2307638534652c67b458877c10a83d0e32ebdc5a7550, Git blob a7cb21fad8ac7a51b6bcd828863c48879377f906, full readback verified. Original runtime authorize returned activity_allowed=true, persistence_allowed=true, authorized=false, ACTIVITY_BOOKKEEPING_ONLY_NO_TASK_AUTHORITY. All task/claim/review/Working-Truth/mathematical-acceptance authority is false.

Pre-freeze mathematical access: no old research was intentionally consulted; the candidate arose from the full X6 Cell/occupation/readout question above after the actual startup gate passed. General pretrained mathematical familiarity is not project-independent novelty evidence. The induction and convolution proof are expected to have classical analogues in finite arrays/tomography/contingency tables; Phase B must check actual coverage and reuse. Candidate creation has not promoted anything to a Task, axiom, Tool, Working Truth, canonical Foundation, or physical law.

The immutable first content hash/commit supplies the freeze time and unedited original. Any Phase B correction must be a separate artifact preserving this text.
