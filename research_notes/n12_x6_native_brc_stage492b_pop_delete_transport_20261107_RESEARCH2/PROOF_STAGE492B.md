# Stage492-B — POP-before-moving-SET and interior-DELETE transport

Status: AUTHOR-SIDE PROOF AND EXACT FINITE EXECUTION; UNREVIEWED / NOT ADMITTED.
Parent: Stage491-B, research PR #1736, commit f9d322dd5387f4ef40d820ff7b38cbc4382e7490.
Frozen scientific pins (unchanged): global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 source blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. These are science inputs, not the present control snapshot.
Current behavioral reference consulted separately: global canonical main b6b3e5ca8d3b955cf859f001e9f58c6fe6f848c5; Enterprise Math canonical main 92475b52954b0c560af566341cb8fbe0be6e23a1; research_method.json and portable research protocol.
P000 current startup projection verified against original global P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.

## Model and observer

D={A,...,L} denotes six signed native spatial directions and their inverses (+E1,...,+E6,-E1,...,-E6); these remain twelve steps in six native dimensions, not twelve dimensions. For a word q, let displacement be the six-component signed integer sum, and E(q) the 144-component directed adjacent-pair count. The full observation for ordered histories P,Q is (|P|,|Q|, displacement(P), displacement(Q), E(P),E(Q),K(P,Q)), with K equal to the number of equal directions at overlapping one-based indices. Every compared public action trace has the same labels and replacement/append parameters; P and Q have respective stated POP/APPEND budgets. Let ~0 denote *actual* equality for every legal no-SET base trace. It is not identified here with an unreviewed repair-key formula.

Write tau_j(q)=(q[j-1],q[j],q[j+1]) for an original interior index j and SET_FROM_END(d,z) to replace current q[|q|-d] by z.

## Theorem 492.1 — transported reachable-neighborhood signature

Assume two starting histories have the same initial Q length n and identical P history. Permit before at most one Q_SET_FROM_END(d,z) any public interleaving of at most p Q_POP operations and b Q_APPEND operations; after SET, any remaining legal base actions of the declared finite budgets. Assume every pre-SET action trace that permits SET targets an ORIGINAL surviving interior letter with BOTH original neighbors surviving and at index strictly beyond the maximum possible P length. (This is a condition on the grammar and n,d,p,b, not on any hidden word.) Let J be the set of all these reachable original indices. Then

    X ~enhanced Y  <=>  X ~0 Y  and  tau_j(Q_X)=tau_j(Q_Y) for every j in J.

The statement assumes both histories have the same P and action budgets. Some tau coordinates may be redundant within a particular initial fiber; the theorem asserts a sufficient-and-exact signature, not independent coordinate minimality.

For a schedule with t APPEND and q POP actions before SET, the current length is n+t-q and its target is j=n+t-q-d; when all integer net shifts -p,...,b are realizable under the grammar and all resulting sites meet the surviving-original-neighborhood hypothesis, J={n-d-p,...,n-d+b}. The order of public operations can affect retained public appended letters but not the original triple at the target under the stated hypothesis.

Proof of necessity: The no-edit sublanguage implies ~0. To inspect any j in J choose a public schedule reaching it. Its pre-SET observer agrees by ~0. Set to every z in D. The six-component displacement difference v(z)-v(center) reveals the center because the twelve signed unit vectors are distinct. Choose z distinct from the at most four candidate neighbor letters and both candidate centers (12 choices are enough). The directed edge difference is

    -[left,center]-[center,right]+[left,z]+[z,right].

The counts of edges into and out of this fresh z isolate the ordered left and right neighbors, so they also agree. Therefore every reachable tau_j agrees.

Proof of sufficiency: For each enlarged trace remove its unique SET, producing a legal base trace with the same public POP/APPEND labels. Its observations coincide by ~0 at all times. The pre-SET edit targets an untouched original triple from J, so its observer correction is determined by that triple and the publicly specified z. Subsequent suffix POP/APPEND operations either leave the edited adjacency intact, delete the right original or public suffix neighbor, or finally remove the edited letter; each differential observer correction relative to the no-SET trace is determined by the same original triple and known public operations. P cannot overlap the edited site under the strict index bound, so its positional K is unchanged by SET. Therefore the edited observers coincide at every stage. QED.

The survivor-original-neighborhood hypothesis matters: INSERT/DELETE or a SET applied to a publicly appended symbol requires a provenance-aware address transport, not simply this fixed original-index expression.

## Strict counterexample 492.2 — POP makes a new hidden neighbor observable

Take T=P=ABGABA, W=GH, Q=T W A H A, H1=ABAGGG and H2=BAAGGG, so both Q have n=16. Restrict P and Q baseline to at most one POP and one APPEND each, with all twelve future append directions and arbitrary legal interleavings. These histories have the same exact initial observation, including directed edge counts and K; the Q tail symbol is A. Their complete base futures agree: the only original Q edge removed by a single POP is GA, and P never reaches the hidden positions. The previous append-first relative-end SET at d=3 reaches J_old={13,14}; both original triples at 13 and 14 agree, so it cannot distinguish these histories.

A Q_POP removes the final A from both Q words, leaving length 15; the relative-end SET(d=3,I) now targets original index 12. The original triples are tau_12(Q1)=BAG and tau_12(Q2)=AAG. The POP leaves all observers equal, but SET makes their 144-edge counts differ. In the signed difference E(Q1_after)-E(Q2_after), the nonzero coordinates are -[AA]+[AI]+[BA]-[BI] (direction I=-E3). This is a strict 2-action distinguishing trace not available to the old append-first signature.

For p=b=1 and d=3, J_new={12,13,14}. Exact finite census of all H in {A,B,G,H}^6 (4096 raw histories) gives 1202 initial directed-edge fibers, 3904 old J_old classes and 4096 POP-aware J_new classes. These are Boolean class counts, not raw-history population or proof of a complexity improvement.

## Strict counterexample 492.3 — individually invisible interior DELETE

On the same two Q histories, remove original absolute position 15 by an internal Q_DELETE(15), where it is G immediately before final A. Both affected local triples are GGA: the signed local edge change is -[GG]-[GA]+[GA]=-[GG], and the displacement decrement is -v(G), equal for both histories. This DELETE result is a DIFFERENT word from merely popping the final A, so the interior-delete witness is not an alias of Q_POP. Thus all declared observations remain equal immediately after DELETE (also K, because P occupies only the first six, or seven after its one APPEND, positions). Q is now length 15. The subsequent SET_FROM_END(3,I) again targets index 12 and separates the histories.

This shows a local *individually unobservable* interior delete may transport an editing address so that an earlier hidden neighbor becomes observable. The previous fixed index signature is not future safe for this enlarged operation grammar. It does not prove that all INSERT/DELETE grammars lack finite safe quotients.

## Exact local rewrite and provenance transport

If an interior adjacent pair a|b receives insertion of public z between a and b:

    Delta E = -[a,b]+[a,z]+[z,b],     Delta displacement = +v(z).

If an original interior letter c in a c b is deleted:

    Delta E = -[a,c]-[c,b]+[a,b],     Delta displacement = -v(c).

For a SET of c to z, the same local difference uses -[a,c]-[c,b]+[a,z]+[z,b]. If INSERT occurs immediately before old original index i, that original index shifts from i to i+1. If an original index i is deleted, surviving original positions after i shift one left. Composition of these formulas must use the CURRENT neighbors after each mutation; summing original-context corrections generally misses interaction terms (as Stage490-B showed). A correct future transducer must track original/public symbol provenance when transported indices enter inserted or appended regions.

## Executed scope / checks

The full author execution REPRO_STAGE492B.py checked 988 paired baseline P/Q observer samples, 156 pre-POP moving-SET comparisons for all twelve signed directions, and 3072 each of the exact INSERT, DELETE, SET edge-delta identities and original-index transport on {A,B,G,H}^4 x D. The independent compact REPRO_STAGE492B_PORTABLE.py was separately run from standard-library Python: 4096 exhaustive H histories, 1202 edge fibers, 3904 old classes, 4096 new classes, 988 baseline paired observations, 156 pre-POP SET checks. See the actual executed JSON outputs. All assertions passed on these finite domains; the general conditional theorem is supported by the above algebraic proof, not inferred from finite tests.

The 144 edge coordinates are retained, while the enumerated raw history alphabet is the declared 4-letter subset. No independent Driver review, native Result, physical correspondence, or algorithmic end-to-end acceleration is claimed.

## Next scientific unit

Stage493-B: allow one internal INSERT at variable public/hidden boundary and a subsequent moving SET, with POP/APPEND on either side; derive an exact provenance-aware transported-neighborhood signature or a strict collision counterexample that invalidates a proposed signature. Evaluate high-support 12-direction sparse Euler–BRC ranking including input encoding and output recovery cost. Do not re-run completed Stage492 finite census except when an assumption or algorithm changes.
