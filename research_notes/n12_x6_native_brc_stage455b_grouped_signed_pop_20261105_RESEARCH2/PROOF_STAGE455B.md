# Stage455-B: grouped exact BRC support and arbitrary signed two-source POP quotient

Date: 2026-11-05. Classification: AUTHOR_SIDE_PROOF / EXACT_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Mother objective: retain the exact path/provenance BRC quotient for native ordered X6 histories with boolean support, exact positive integer populations, and complete labeled future observers.
Frozen scientific pins: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 original blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Behavioral context read separately on 2026-11-05 at global main f650ae9cb25a7f2b6feef55720ae682a49381963 and EM main 6c79349416f88dbd1732507746011ebee28dcd34.
Previous frontier: Stage453 exact indexed binary repair theorem and Stage454 single-source signed probe/equality-bit theorem (author-side, PR #1736).

## Model
P,Q have original lengths 2<=m<n and signed native letters. The complete observer O after every legal operation prefix includes lengths, each full signed six-component endpoint V, each full 12-by-12 directed native adjacency J, and the number of positionwise matches K. The carrier is a source-distinct ordered pair: a population counts ordered original histories, not equivalence classes. Only original A/B data are restricted in Theorem 455.1; future APPEND directions are all twelve signed native directions, as in Stage453.

## Theorem 455.1 (implemented): nonenumerating C/T/U exact class support and integer population
Assume original A=+E1,B=-E1, both endpoints A, B internally isolated and nonadjacent. Fix kP,kQ B counts and d=m-K. Take arbitrary nonnegative POP/APPEND budgets pP,pQ,rP,rQ with pP>=1. Set a=min(pP,m), b=min(pQ,n), c=min(m-a,n-b)<m, t=min(n,m+rP), u=max(1,n-b), g=max(0,u-t-1).

The Stage453 indexed repair key consists of P predecessors [max(1,m-a),m-1], Q predecessors [max(1,n-b),n-1], P cross-alignment indices [c+1,m], Q cross-alignment indices [c+1,t]; repeated positions are coalesced. Under Stage453's exact future-iff theorem, each distinct supported indexed key is exactly one future-equivalence class.

There is a deterministic C/T/U transfer calculating qF and total source-distinct population |F| without enumerating any original history or any visible repair key. Proof: every paired index c+1,...,m is visible. The hidden paired indices form prefix 1,...,c, and hidden Q-only indices form at most one gap t+1,...,u-1. Coordinates at c that appear in either predecessor tail are conditioned as visible boundary letters. The prefix and gap are disjoint, so all connection constraints lie in constant-size boundary letters.

A left-to-right deterministic visible-letter automaton C counts *distinct indexed repair strings* grouped by summary sigma=(visible P/Q B counts vP,vQ, visible paired mismatch count vD, exposed boundary coordinates at c, first paired letters at c+1, Q letters on both sides of the possible gap, recent visible letters). The transition emits 0/1 original letters at visible positions, enforces endpoint A and isolated B whenever successive visible positions are adjacent, and increments an exact integer multiplicity C(sigma). No hidden choices are emitted by C.

T_sigma(bp,bq,dd) is the count of hidden paired-prefix assignments with those defect and mismatch counts, endpoints P1=Q1=A and the visible boundary constraints; compute via a four-state pair-letter integer transfer. U_sigma(j) is the number of hidden Q-only gap assignments with j B and with both visible neighbors respected, via a two-state integer transfer. U(0)=1 for an empty gap.

The population of every key with summary sigma is
M(sigma)=sum_y T_sigma(kP-vP,y,d-vD)*U_sigma(kQ-vQ-y).
Consequently qF=sum_sigma C(sigma)*[M(sigma)>0] and |F|=sum_sigma C(sigma)*M(sigma). T and U count exactly the independent hidden runs and C counts each visible key once; this proves the formulas. Stage453 future-iff is the explicit dependence for calling qF a future-class count.

The executed BigInt implementation uses O(N^3) stored counters/boundary states per visible position and O(N^4) state transitions over N=max(m,n) indices. A constant set of cached prefix T transfers costs O(N^4), Q gap U O(N^2), and directly summing T states over all terminal C summary states gives the conservative O(N^6) **exact integer arithmetic** upper bound. Counts fit O(N) bits because they count subsets of at most 2^(m+n) binary history pairs; schoolbook arithmetic yields conservative O(N^8) bit operations (dictionary-key management additionally polynomial). This is an upper bound for this implementation, not an asymptotic sorting claim.

Executed small oracle: 1100 deterministic binary parameter cases, of which 440 have nonempty fibers, with 7685 total original pairs and 6265 total supported classes across cases. Each case compares aggregate grouped qF and |F| to an independent brute enumerator over all original history pairs and repair labels; all pass. Executed large cases from grouped transfer (no raw-history enumeration):
(64,80,15,17,1,10,5,3,0) => c=54,t=67,u=75,g=7, qF=31992, |F|=5061384194832966.
(64,80,15,17,1,24,10,8,5) => c=40,t=72,u=70,g=0, qF=271596675, |F|=5061384194832966.
(92,126,20,25,3,12,9,7,4) => c=80,t=99,u=117,g=17, qF=59991909, |F|=1121449082621221549433213976.

## Theorem 455.2: exact POP-only two-source quotient for arbitrary native signed alphabet
Now let original P,Q use any finite subset of the twelve signed X6 unit directions, require fixed terminal letters P_m=Q_n=A, fix *the complete original observation* O, and allow at most a=min(pP,m), b=min(pQ,n) POPs on each respective source. Both APPEND budgets are zero. Set c=min(m-a,n-b). Then two original ordered histories in the same O-fiber have identical complete labeled future observation trees iff these three pieces agree:
R_POP=(P[max(1,m-a):m-1],Q[max(1,n-b):n-1],([P_i=Q_i]) for i=c+1,...,m).
The notation includes indexed coordinate positions and omits fixed terminal A.

Sufficiency: all original steps removed by POP and corresponding directed edges are determined by those two predecessor tails and fixed terminal letters. Starting from O recovers the native endpoints and complete J at every prefix. If lengths remaining are L_P,L_Q, the match count equals K_initial minus the known match bits for i=min(L_P,L_Q)+1,...,m, since min(L_P,L_Q)>=c. This reconstructs the full observer after every operation prefix.

Necessity: consecutive POPs expose each removed directed edge through the difference in the native full J, recovering predecessor letters backward from the original terminal A; a final singleton's signed endpoint difference is also visible. For each i>c, at least one source can be POPped to length i-1 (P if m-a<i, else Q if n-b<i), leaving the opposite original source long enough. The K decrement gives the exact equality bit [P_i=Q_i]. Every key component is therefore recoverable from legal labeled future observations, establishing iff.

Strict signed witness: A=+E1,B=+E2,C=+E3; P=AAAAA, Q1=ABACAAA, Q2=ACABAAA. Both pairs have the same initial full six-dimensional V, complete 12x12 J and K=3. All five original matched-position bits are identical. Three consecutive Q POPs remove a directed C->A edge versus B->A edge, so complete J diverges. Thus in this POP-only two-source model equality bits alone cannot replace the Q-side exposed predecessor tail. This complements Stage454's immobile-Q result, where some Q raw letters were safely collapsed to match bits.

The independent signed finite checker uses full six-component vectors and 144-entry J, A/B/C with isolated non-A steps, fixed A endpoints, m=3..5, m<n<=7, all POP budgets a=0..m,b=0..n. For 299 configurations it checks two-sided iff on 13076 multi-history initial observation fibers, 47234 aggregate history occurrences and 96199 unordered within-fiber pairs. All pass. The universal claim uses the proof above; the finite check is exactly scoped.

## Source evidence and next question
Executable code: STAGE455B.js; actual observed output: STAGE455B_EXECUTED.json (two JSON reports, exact decimal BigInt strings). Neither code nor exact integer enumeration establishes formal independent admission. The grouped engine currently covers pP>=1 (c<m); the c=m zero-P-POP boundary, support-oracle rank/unrank, and fully bilateral signed POP+APPEND probe repair are the next three concrete units. A follow-on should first extend c=m correctly when Q_m lies in the hidden paired prefix and may couple to the hidden Q-only gap, test a small complete O-fiber, then derive key/raw-history rank/unrank with explicit bit costs. All claims are static native six-axis path-observer statements, not a physical time-evolution or a three-dimensional-slice dynamical identification.

Research activity: RA-B90455AA8319540A20CA8E93, Researcher-ID EM-DIRECT-B198FA. Session Source record exists; formal task owner, CLAIM and independent Driver acceptance require their own authority.
