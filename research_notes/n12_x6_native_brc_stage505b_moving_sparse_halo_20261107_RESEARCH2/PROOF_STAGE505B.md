# Stage505-B — Sparse moving-port halo compression for native X6 BRC histories

Date: 2026-11-07. Classification: AUTHOR_PROOF / EXACT_FINITE_EXECUTED / UNREVIEWED.
Mother objective: observer- and operation-sufficient compression of native X6 direction histories, with provenance retained where queried. Parent Stage504-B commit: eb89cae0fa37cb55d8d14d2184ca87b4bdb26018.

Immutable scientific pins retained from Stage504-B: account bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative requirements are read separately from current main. Static typed exact BRC direction/edge combinatorics; no physical heartbeat propagation or native dynamical law claimed.

## 1. Exact model

The alphabet A has twelve signed directions ±E1,…,±E6. The injective chart displacement v:A→Z^6 maps each direction to the signed unit coordinate; time is a separate type. The test program uses direction codes 0=+E1, 1=−E1, 2=+E2 (the other nine codes are also defined). A word w of length n has exact observation

F(w)=(n,D(w),E(w)), D(w)=Σ_i v(w_i), E_ab(w)=#{i:w_i=a,w_{i+1}=b}

with all 144 ordered edge counts. The first and last direction of every nonempty word are recovered by

v(first)=D−Σ_ab E_ab v(b);  v(last)=D−Σ_ab E_ab v(a).

Therefore the associative exact BRC directed-relation product F(u)⊙F(v)=F(uv) adds n,D,E and the single cross-boundary edge (last(u),first(v)) when both are nonempty. The empty word is the identity. This is the exact interface established in Stage496-B and reused in Stage504-B.

A token may carry a provenance label O (original) or P (inserted). The present observer F and operation language do not query provenance; the constructive representation nevertheless retains labels of every individually retained token. Separate ranked-public-deletion operations require a separate sufficient-state analysis.

Fix a finite nonnegative end-offset set R (the experiments use R={2,5}), horizon h≥0, and operations:

* POP: remove the final token when length≥1.
* INSERT2(c): insert new token c immediately before the final two tokens, when length≥2.
* SET_END(r,c): replace token at current index n−1−r by c, when r∈R and 0≤r<n.

Every operation's legality and the observer F are observed at all prefixes of all common sequences of at most h legal operations. All operations are discrete and exactly typed.

## 2. Theorem 505.1 — Sparse moving-port halo theorem

For an original token at initial position i in a length-n history, define its initial end offset ρ(i)=n−1−i. Let the protected original-offset set be

H_(R,h) = {ρ:0≤ρ≤h+2} ∪ ⋃_(r∈R){ρ: max(0,r−h)≤ρ≤r+h},

intersected with the valid range 0≤ρ<n.

Construct K_(R,h)(w) by retaining each original token whose initial offset lies in H, in its exact order and with its direction and label. Replace each maximal intervening unprotected contiguous original segment by its exact F summary, including its length and recovered endpoints. Preserve the order and position of these segments. This is a typed ordered concatenation of singleton tokens and gap summaries, not an unordered count or positive-mass quotient.

**Theorem.** If K_(R,h)(x)=K_(R,h)(y) for two tagged original histories and the operation language above is shared, then every common legal operation sequence of length at most h has identical legality at every step and identical exact observations F at all prefixes. There is an explicit update algorithm on K that does not inspect the interior of any summarized gap for any such sequence.

**Proof.** Associate immutable identities with the original tokens solely for this argument. Suppose a surviving original token started at offset ρ and currently has offset ρ_j after j operations. POP decreases its offset by exactly one if it survives. INSERT2 either leaves the offset unchanged (the token lies to the right of the insertion), or increases it by exactly one (the token lies to the left). SET changes no offsets. Hence |ρ_j−ρ|≤j.

For any SET_END(r,c) at step j+1≤h, if the target is an original token, ρ_j=r, so |ρ−r|≤j≤h−1, placing the original token inside the saved halo around r. If the target is a token inserted earlier, it is explicitly saved by the update algorithm.

At any POP step j+1≤h, the removed original token, if any, has current offset 0, so its initial offset satisfies ρ≤j≤h−1 and lies in the saved tail. An inserted token is again explicit.

At any INSERT2(c) step, insertion is at index current_n−2. The immediately adjacent old tokens (when they exist) have current end offsets 1 and 2. Any such surviving original token has initial offset at most j+2≤h+1, inside the saved tail. Inserted tokens are explicit. Thus the insertion boundary lies between explicitly retained pieces and cannot split an opaque gap during the allowed horizon.

This establishes that every legal operation can be performed on the ordered compressed pieces without editing, deleting or splitting any summarized original gap. At each step the current length comes from the sum of piece lengths, hence legality is determined. The compressed update modifies only explicit tokens, and the associative exact ⊙ product reconstructs F exactly from the untouched gap summaries and current singleton tokens, including all cross-boundary edges. Starting from equal compressed states, induction over the common operation sequence gives equal legality, updated states and observations at all prefixes. QED.

## 3. Representation cost and strict improvement for remote sparse ports

The saved set is a union of at most |R|+1 intervals, containing at most (h+3)+(2h+1)|R| original tokens. Consequently there are at most |R|+2 nonempty unsaved gaps. Each F gap has one length counter, six signed displacement counters and 144 nonnegative edge counters, with O(log(n+1)) bits per counter. Explicit token labels and direction identities need O(1) bits each. For fixed twelve-direction alphabet, the exact representation has the sufficient storage upper bound

O(150(|R|+2) log(n+1) + (h+3+(2h+1)|R|) + |R|log(n+1)) bits.

Equivalently, O((|R|+1)log(n+1)+(|R|+1)h) bits with model-dependent constants. The initial scan takes O(n) primitive operations and O(144n) straightforward counter-update work (sparse edge updates reduce the latter to O(n)), excluding integer-bit arithmetic. An operation can locate pieces using a balanced length tree and update the full F monoid along a logarithmic path, with counter-operation cost O(144 log(|R|h+h+|R|+2)) for a maintained balanced tree, plus integer-bit costs. The executed reproducibility implementation uses a simpler sequential piece scan; the balanced-tree runtime is an algorithmic construction, not a measured benchmark.

Numerical example (symbolic storage count, not a million-token program run): n=1,000,000, h=3, R={2,100000}. Exactly 13 original tokens belong to H; the remaining original positions can be stored in gap F summaries. A uniform suffix retaining all offsets through max(R)+h would retain 100004 original tokens. The halo certificate therefore scales with the number of accessible offset ports and horizon rather than the largest distance from the tail.

## 4. Counterexample 505.2 — Static sparse port summaries cease to be sufficient after POP

For R={2,5}, take length-ten words in numeric direction codes

x=(0,0,1,0,2,0,0,1,0,0)
y=(0,1,0,0,2,0,0,1,0,0).

Their first four directions are AABA and ABAA, which share exact F; all later tokens agree. The two editable absolute sites at the original length are positions 4 and 7 (end offsets 5 and 2), and both words have the same letters at those sites. Therefore the fixed-port Stage504 K_R consisting only of original port tokens and immutable-gap F summaries is equal for x and y.

Execute the common three-operation trace POP, POP, SET_END(5,+E2). The first two prefixes have equal exact F. The final SET targets original index 2, whose old directions are −E1 in x and +E1 in y. After replacing both by +E2, the new displacement difference D(x')−D(y') is (2,0,0,0,0,0), an exact witness. The Stage505 moving halo contains original position 2 for h=3 and separates x,y at initialization. This proves the fixed-port quotient is not a congruence for the enriched operation language.

## 5. Nontrivial positive collision (real compression)

For R={2,5} and h=3, set x=(0,0,1,0)+nine copies of 0 and y=(0,1,0,0)+nine copies of 0. Both words have length 13, differ within the summarized four-token prefix, and have exactly equal K_(R,3) (the saved original suffix contains nine tokens). All operation traces of length≤3 preserve F-equivalence by Theorem 505.1; the executed checker explicitly compared 1111 operation-tree prefix states for this distinct-word pair.

## 6. Executed exact tests and reproducibility

The separately archived complete Python3 implementation is provided as compressed base64 UTF-8 source in REPRO_STAGE505B.py.gz.b64; restore with base64 and gzip, then execute REPRO_STAGE505B.py using only the Python standard library. Its output is REPRO_STAGE505B_EXECUTED.json. The executable independently constructs F from all twelve signed native directions, computes the associative 144-edge monoid, simulates original words, performs compressed-piece updates, and verifies exact equality after every operation prefix.

Complete finite test domain: all 1,093 three-letter words of lengths 0..6; for each, all operation trees through horizon 2 with replacement/insert alphabet {0,1,2}, R={2,5}. Exact observations matched at 101,095 visited tree nodes and 108,790 tested transitions (including illegal-operation checks). Also ran 180 deterministic seeded words of lengths 0..50 over all twelve signed directions, each against every depth≤3 operation tree over three replacement directions: 186,354 visited nodes and 188,160 transitions. The distinct protected-prefix pair was checked at 1111 nodes through depth 3. All assertions passed. This execution used exact Python integers, not floating-point approximations.

Scope: the theorem covers precisely POP, INSERT2, and SET_END offsets in fixed R for a fixed h. The proof supports arbitrary word length, any subset R, and all twelve X6 directions; the finite tests cover the enumerated cases. The provenance deletion/rank operation language and all-144-active Euler–BRC ranking benchmark remain active separate scientific questions. Source publication and mathematical admission are distinct.

## 7. Next scientific question

Stage506-B: derive tighter adaptive/nonuniform halo intervals under restricted operation budgets and mixed DELETE/INSERT at multiple internal offsets, including public-provenance rank queries. Determine whether the actual reachable original-token set can be computed exactly from operation automata and yield smaller certificates than the symmetric ±h halo. Independently complete the same-inventory Euler–BRC rank/unrank time/bit/RSS benchmark pending from Stages 494–505.

Current service fact observed in this turn: the Site gateway reported CONFIGURED_NOT_LIVE_VERIFIED; the authenticated backend status call returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. Therefore no authenticated CLAIM, Result or Driver review is asserted for this author-side research.
