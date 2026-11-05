# PREFIX-520 — Free S4 phase-orbit coordinates and exact four-STAR return recurrence

Date: 2026-11-06 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Researcher-ID: EM-X6-C08B62; Research-Activity-ID: RA-30009FD3EDE391E13FF10B23.
Task: RS-X6-NATIVE-ROTATION-DYNAMICS, independent author-side progress, not an authenticated CLAIM, Result or Review.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Immediate predecessors: PREFIX-518 (candidate four-STAR pivot switching, a51bb9bf8071f90d95e0e0ffa956dde8f27901fa) and PREFIX-519 (24-frame BRC/KMP orbit, bfadaef7382c782f04638930b2ccd7e8c3e1516c).

## Problem, carrier, and limits

For the candidate four-STAR switch relation of PREFIX-518, classify its 48 incoming directed phase states under the K4/S4 chart relabeling, reduce the transition rule without discarding phase identities, and count exactly how many closed directed phase histories exist at arbitrary macrostep length. Each admissible macroedge still has two distinct native signed-X6 shortest BRC microtraces; branch identity and indexed intermediate Cells must not be collapsed when those observations are requested. This is an exact symbolic candidate relation, not a discovered physical rotation-selection law.

Use the frozen STAR triples S_A={L1,L3,L6}, S_B={L1,L4,L5}, S_C={L2,L3,L5}, S_D={L2,L4,L6}; K4 edge labels are L1=AB, L2=CD, L3=AC, L4=BD, L5=BC, L6=AD. A directed state is (S,prev,current), with prev/current adjacent signed unit phases in S. Neighbors of +Li are negative phases on the other two axes of its STAR, and conversely. Three exits are: continue within S without immediate backtracking (one) or switch to the second STAR containing the unsigned current axis (two). Each macroedge a->b has inner (-a,b) and outer (b,-a) primitive signed paths and corresponding intermediate Cells P and P+a+b.

## Theorem 1 — two free regular S4 phase orbits

The set of 48 directed phase states splits into exactly two regular orbits under S4, distinguished by the sign sigma of current. Each orbit has 24 states, and every state has trivial stabilizer.

Proof: A K4 vertex permutation preserves STAR incidence, unsigned-edge adjacency, and signed phase signs. For fixed sign sigma, choose the base state b_sigma=(A, -sigma L3, sigma L1), writing L1=AB and L3=AC. Any directed state with current sign sigma can be obtained by moving the STAR vertex A and the ordered pair of two distinct incident edges (L3,L1) to its STAR vertex and its ordered pair of distinct incident edges (prev,current). This uniquely specifies a permutation of the four K4 vertices, because the fourth vertex is the unused vertex. Thus the orbit contains all 24 states of that sign, with unique transporter g in S4. The two signs cannot mix because label permutations preserve sign. QED.

Use the unique representation s=g b_sigma. Invariantly label its three outgoing phase ports by transporting the ordered canonical exits from b_sigma (port 0 stay, ports 1/2 switch). In zero-based STAR/axis indices and signed phases +/-1..+/-6, the canonical bases are b_+= (0,-3,1), b_-=(0,3,-1). Canonical successor states are, respectively:

sigma=+: ((0,1,-6),(1,1,-5),(1,1,-4)).
sigma=-: ((0,-1,6),(1,-1,4),(1,-1,5)).

The composition of two group elements is their action composition. If r_(sigma,j) is the unique group element mapping b_(-sigma) to the canonical port-j successor of b_sigma, the exact transition is

  (g,sigma) --j--> (g composed with r_(sigma,j), -sigma).

For lexicographically enumerated permutations of (A,B,C,D) the indices of r_(+,j) are (4,8,10), and those of r_(-,j) are (4,10,8). These indices are enumeration-dependent; the group elements are canonical once bases/ports are fixed. In particular, 48 distinct state identities are retained as a 24-element group coordinate plus one bit, while the *transition rule* needs only six canonical phase-port templates. This is a factorization of the transition table, not a claim that 48 states were reduced to two distinguishable states. The extra inner/outer beta bit remains available at every macroedge; the native intermediate Cell is still exactly recoverable. S4 covariance of the port labels follows from uniqueness of g.

## Theorem 2 — exact infinite closed-phase recurrence

Fix any incoming directed phase state s. Let a_m be the number of admissible length-2m phase itineraries (the port choices, not inner/outer microbranch choices) that return exactly to s. The number is independent of s and satisfies

  a_0=1, a_1=0, a_2=5, a_3=28, a_4=297,

  a_(m+5)=5a_(m+4)+26a_(m+3)+78a_(m+2)+135a_(m+1)-243a_m    for m>=0.

There are no odd-length directed returns. When each macroedge's two native shortest microbranches are distinguished, the number of length-2m labeled closed phase histories equals 4^m*a_m.

Proof: Every allowed phase edge reverses the current sign; therefore odd returns are impossible. By the first theorem, the S4 action is free and transitive on each 24-state sign orbit and preserves all three outgoing phase exits. Global sign negation also preserves the relation. Therefore every state's even-length diagonal return count agrees.

Index the positive sign orbit by 24 permutations h, and form the integer matrix B of two-step phase counts: B[h,k] is the number of the 3*3 port pairs going from h b_+ to k b_+. This is a fully specified 24x24 nonnegative integer matrix, constructed by the six canonical templates and the K4 incidence above. Each row sums to 9; all entries are counted with multiplicity. Let

  q(x)=(x-9)(x-1)(x+3)(x^2+2x+9)
      =x^5-5x^4-26x^3-78x^2-135x+243.

The accompanying self-contained exact-integer certificate constructs B from all states, checks all 576 entries of q(B) against zero using literal integer matrix multiplication, and independently checks the first return coefficients by direct 48-state dynamic programming. This is a finite exhaustive proof of a matrix identity for the explicitly defined finite matrix, not an extrapolation from a sampled sequence. It gives q(B)=0 and hence the displayed recurrence for a_m=(B^m)[id,id] for *every* m>=0. Direct enumeration gives the listed initial values. For each phase itinerary, the two microbranch choices at each of its 2m edges are independent and distinct as labeled histories, giving 2^(2m)=4^m. QED.

The ordinary generating function is thus exactly

  sum_(m>=0) a_m z^m
  = (1-5z-21z^2-75z^3-108z^4)/
    (1-5z-26z^2-78z^3-135z^4+243z^5).

The first terms are 1, 0, 5, 28, 297, 2360, 22381, 198996, 1794257. A 5x5 Hankel determinant of the first nine terms is -44718096384 != 0, so there is no scalar constant-coefficient linear recurrence of order <=4 on this complete sequence. The displayed order five is minimal over the rationals.

For instance, length 4 has five closed phase itineraries and 5*2^4=80 labeled inner/outer microhistories. Length 6 has 28 phase returns and 28*2^6=1792 labeled microhistories. Their observations can still collide after quotienting by BRC/area/KMP; they are counted here as **distinct provenance-labeled paths**, not distinct compressed observers.

## Certificate, scope and next exact question

Run: python research_notes/portable_direct/prefix520_four_star_return_certificate.py

Exact stdout: research_notes/portable_direct/PREFIX520_EXACT_EXECUTION.json (captured). Result: ALL_CHECKS_PASS. The certificate checks 48 canonical states, 24 S4 permutations, 288 local primitive microtrace continuations, 3456 port-equivariance instances, 576 entries of q(B)=0, direct returns through length 30, global sign symmetry and the nonzero integer Hankel determinant. Only integer arithmetic is used; no floating point, physical simulator or mathematical admissions are implied.

Reused BRC theorem: two native shortest paths per C6 macroedge from the frozen microtrace paper and PREFIX-518, with branch identities retained. New work: exact free-orbit coordinatization, S4 group cocycle and infinite closed itinerary enumeration. The 24-frame KMP orbit of PREFIX-519 is **not** discarded: its future-frame-sensitive content is not established redundant by phase-state equivariance. The symbolic microtrace choice word may be composed with the existing KMP/BRC orbit without rescanning past steps, but establishing any smaller future-operation-safe KMP observer remains an open separate problem.

PREFIX-521: On the same 48-state admissible language, explicitly test whether any proposed quotient of the 24-frame KMP orbit is a right congruence under all allowed future microtrace continuations. Seek the smallest equal-quotient/different-future-output witness, or construct and prove a sufficient relative-frame finite transducer. Also compare this candidate S4 switch relation with native arbitrary-triad C6 generators from the frozen task; nothing above selects physical rotation.

Sources: frozen f42f2906d77f24085c123f3ccfe9667d41caa96d: p000_reality_foundation.json and research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md; current docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context, docs/PORTABLE_RESEARCH_PROTOCOL.md, research_priorities/research_method.json, P000/ACTIVE worldview, mathematical and BRC global policies; PREFIX-518/519 as cited. Project Source keeps author-side result distinct from formal task CLAIM/Result/independent Review/Admission.
