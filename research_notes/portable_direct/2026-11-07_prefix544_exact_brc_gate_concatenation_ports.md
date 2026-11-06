# PREFIX-544 — Exact BRC–gate concatenation ports and information-loss witnesses

Date: 2026-11-07. Independent author-side mathematical note. Project: Enterprise Math / RS-X6-NATIVE-ROTATION-DYNAMICS. Scientific input frozen at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Predecessors: PREFIX-539 (first-axis BRC cocycle); PREFIX-542 (phase-only gate transform); PREFIX-543 (initial-bit boundary repair). This is a restricted candidate in the native X6 research setting, not a change to P000.

## Exact question and carrier

Which boundary coordinates suffice for exact concatenation of phase-and-branch path segments when the observer reads first-axis BRC cancellation p and target gate count H? In the earlier single-segment phase-only observer the (p,K,E) histogram suffices to reconstruct gate-count distributions, but compositional continuation may inspect ports and terminal branch bits.

The frozen STARs are A=(1,3,6), B=(1,4,5), C=(2,3,5), D=(2,4,6). There are 48 directed signed phase states i=(STAR,previous,current), three legal next phases for each i, and one independent new branch bit c=0 OUTER or c=1 INNER on each step. Gate target T=(A,+L1,-L3) is not its own successor.

Put sigma(i) in {-1,0,1} for the signed first-axis direction of the current component, epsilon(i)=|sigma(i)|, and r=sigma(s) for the complete path's original root. The PREFIX-539 exact BRC edge cocycle is

tau_r(i,j) = [epsilon(i)+epsilon(j)-|sigma(j)-r|+|sigma(i)-r|]/2.

For all legal frozen edges and each r, tau_r is 0 or 1. With preceding bit b and new bit c, the edge gate increment is g(b,j,c)=1 if and only if b=c=1 and j=T. Thus p=sum(tau_r) and H=sum(g) for the whole labeled path, including the externally chosen initial bit.

Allowed future operations: legal concatenation, chosen INNER/OUTER bits, and native successor-slot selection. These observations have exact integer multiplicities; their carrier retains phase, bit and sign information until a future-safe quotient is proved.

## Theorem 1 — exact compositional 96-port transfer

For each fixed root parameter r in {-1,0,1}, index 96 ports by (i,b) with i one of 48 phases and b one of two branch bits. Over Z[q,z], define

M_r[(i,b),(j,c)] = q^{tau_r(i,j)} z^{g(b,j,c)} if i->j is legal, and 0 otherwise.

For every rooted phase s, initial bit beta and integer d>=0,

P_s^(beta)(d;q,z) = e_(s,beta)^T M_{sigma(s)}^d 1.

For all m,n>=0,

M_r^(m+n)=M_r^m M_r^n.

Consequently a prefix represented by its exact polynomial histogram keyed by (terminal phase, terminal bit, accumulated p, accumulated H), with its original r retained as an external parameter, composes exactly with every allowed legal future path.

Proof: a length-d labeled native path is precisely a sequence of legal adjacent ports. Its product weight has exponent sum(tau_r) for q and sum(g) for z. The cocycle's sum telescopes to the original BRC endpoint formula, while every gate occurrence uses exactly its preceding/new bits. Splitting any path after m edges gives exactly one pair of paths with the same shared port, and gluing matching-port fragments is inverse. Thus weighted path multiplication and the matrix identity hold for every m,n. QED.

This gives an exact **sufficient** interface for the declared observer and future language. A 96-port representation does not by itself prove that all its states are pairwise inequivalent under every smaller observer language.

## Theorem 2 — exact BRC rebasing for a separately rooted suffix

For a suffix from phase u to phase v, let p_a be its BRC edge sum computed using local reference sign a, and p_r the sum for the root sign r of the entire concatenated path. Then for any suffix length,

p_r = p_a + Delta(r,a;u,v),

Delta(r,a;u,v) = [|sigma(u)-r|-|sigma(v)-r|+|sigma(v)-a|-|sigma(u)-a|]/2.

In particular, if the suffix was independently rooted, use a=sigma(u). Proof: sum tau_r along the suffix. The epsilon terms remain unchanged while the absolute-value differences telescope to the two endpoints. Subtract the expression with a. The difference is precisely Delta. This identity has integer values for legal native paths. QED.

Hence an independently rooted suffix histogram can be combined with an earlier prefix after preserving its endpoints and the original root-sign parameter and applying this deterministic correction.

## Theorem 3 — three concrete composition-fiber witnesses

**(A) Final branch bit.** Root s=(A,+L3,-L6), initial bit beta=0. Follow the legal first edge to i=(A,-L6,+L1), selecting terminal bit either 0 or 1. Both one-step prefixes have identical (p,K,E,H)=(0,0,0,0), root and terminal phase. Append the SAME legal edge i->T with new bit 1. Both add BRC 1, but gate increment is 0 for terminal bit 0 and 1 for terminal bit 1. Therefore the (p,K,E,H) quotient that erases the final bit is not safe under this legal one-step continuation.

**(B) Terminal phase.** Root s=(A,+L6,-L3), initial bit 0. The legal first steps ending in i=(A,-L3,+L1) or j=(C,-L3,+L2), each with new bit 0, both have (p,K,E,H)=(0,0,0,0), and matching terminal bit. Apply the SAME successor-slot-0 future operation with new bit 0. The next phases are respectively (A,+L1,-L6) and (C,+L2,-L5). The BRC increments are respectively 1 and 0. Thus phase erasure is unsafe for this future-operation language, even if the terminal bit is retained.

**(C) Original BRC root parameter.** With root (A,+L6,-L3), choose the one-step prefix ending in (A,-L3,+L1). Take the suffix edge (A,-L3,+L1)->(A,+L1,-L6). Its own local sign is +1, giving local BRC increment 0; the original root sign is 0, giving full-path increment 1. Theorem 2 computes Delta=1 exactly. Thus adding locally rooted BRC counts without the endpoint/root correction fails even on one edge.

These are exact legal path witnesses. For broader Cell, ordered-branch and provenance observers, native carriers are preserved separately; these theorem statements concern the specific rooted p/H observer and its declared composition language.

## Executed exact certificate

Companion file PREFIX544_compact_port_certificate.py uses the already published PREFIX543_boundary_moment_certificate.py native transition and original endpoint implementation, with the same scientific model pin. Run in the same directory:

~~~sh
python3 PREFIX544_compact_port_certificate.py 10
~~~

The executed certificate returns ALL_CHECKS_PASS. It verifies 6,336 polynomial prefix/suffix gluing equalities for 48 roots, two initial bits, and all m+n<=10; 672 independent rooted/bit/depth comparisons with the native endpoint BRC formula at depths 0..6; and 52,416 exact root-rebasing equalities across all phase paths of length 0..5 and all root parameters. It asserts the concrete one-step witnesses above. Calculations use exact integer counts and the typed local BRC cocycle. All-length assertions are proved algebraically; the bounded tests check the frozen implementation and witness bytes.

## Next research: PREFIX-545

Construct and certify the smallest justified observer quotient of the 96-port automaton under a declared future language. Compare aggregate all-continuation scalar equivalence with phase/bit-resolved future operations, obtain distinguishing continuation lengths for any contested quotient, and test resulting compressed symbolic computation. The mother objective continues to concern full native six-axis rotation dynamics; preserve Cell, branch provenance and joint structure when required by their observers.

Source scope: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Native backend status operation returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false; formal owner and Researcher-ID unconfirmed, no formal CLAIM/Result/Review.