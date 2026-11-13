# Stage457-B — no-short-POP, long-POP-below-m exact X6 BRC classification

Date: 2026-11-05. Scientific status: AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Sources and frozen assumptions

Predecessor: Stage456-B, Enterprise Math commit c678c1edc28ad05997bf580c35a1c979563f6d15, and its Stage457-B task packet. Preserve its frozen science: account-global commit bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math commit 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 original Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral norms are read separately.

Fix m,n with 2<=m<n. Let P,Q be distinct-source ordered words of lengths m,n over the subset {A=+E1,B=-E1} of the twelve primitive signed X6 directions. Both words begin/end A, have no neighboring B, and have respectively kP,kQ copies of B. Fix the entire original observation O=(m,n,V(P),V(Q),J(P),J(Q),K(P,Q)), with V the six signed native endpoint components, J each full directed 12-by-12 adjacency matrix, and K=sum_{i=1}^m [P_i=Q_i]. Set d=m-K. In this restricted family, (m,n,kP,kQ,d) fixes the entire observation fiber because V,J are determined by length and B count under isolated defects.

Allowed future labels are P/Q APPEND(z), any of the twelve signed primitive X6 directions, Q POP at most b times, and no P POP. The finite APPEND budgets may be any nonnegative integers. Every prefix is observed in O's full format, and a POP used on an appended letter consumes the same budget. Assume n-m < b <= n and c=n-b, so 0<=c<m. The 6D carrier/source identity and ordered histories are retained while the quotient is formed.

## Theorem 457.1 — exact future quotient for c<m

For c>=1 define the indexed repair key R=(Q_c, (P_{c+1},Q_{c+1}),...,(P_m,Q_m), Q_{m+1},...,Q_{n-1}). For c=0 let R=((P_1,Q_1),...,(P_m,Q_m),Q_{m+1},...,Q_{n-1}). Here Q_n=A is fixed. Tokens are ordered lexicographically by their ordered digits A=0,B=1.

For all members H,H' of the above fixed observation fiber, their entire labeled future observation trees coincide if and only if R(H)=R(H').

Proof of sufficiency. Q can delete at most b original steps. Therefore the first c original Q steps never cease to be a shared prefix of both original sources, and P never deletes any original step. The original hidden-prefix match count is recovered from O and R as K_0 - sum_{i=c+1}^m [P_i=Q_i]. All future positional match contributions outside indices 1..c compare indexed-visible original letters or explicit appended letters. Both lengths at every prefix are determined by the operation labels, so the hidden match subtotal is included exactly when both source prefixes still contain 1..c. All original Q edges that can be deleted have both endpoints among Q_c..Q_n (or Q_1..Q_n for c=0), and therefore their direction and J contribution are known; original P edges cannot be deleted. The six-component endpoint change, each 12-by-12 J histogram change, and each APPEND-generated edge are determined by original O, R, and the labels. Consequently all future observations are equal.

Proof of necessity. Consecutive Q POPs starting at length n reveal the deleted directed edges from successive changes in the full directed J_Q histogram. Starting with the known terminal letter Q_n=A and inducting backwards recovers Q_{n-1},...,Q_c, including Q_1 when c=0 (Q_1 is also fixed A). For each c<i<=m, execute Q POP repeatedly until its length first equals i-1. Its preceding match-count drop, from length i to i-1, is exactly [P_i=Q_i], and Q_i was recovered. Because P_i belongs to exactly {A,B}, the binary match bit identifies P_i. Thus every R coordinate is reconstructible from the tree. Both implications are established.

For this particular model equality of R is the exact observable quotient; this theorem does not claim every key letter varies independently on each fixed fiber.

## Theorem 457.2 — exact BRC Boolean support, integer mass, lex rank/unrank

With c>=1 the only unexposed original source letters are P_1..P_c and Q_1..Q_{c-1}; the entire Q_c..Q_n suffix is known in R. For a fixed known q=Q_c and f=P_{c+1}, define T_c(q,f;x,y,z) as the number of source-distinct paired prefixes of length c with exactly x P-defects, y Q-defects, z positional mismatches, Q_c=q, and no B-B transition at P_c to P_{c+1}=f. The prefix begins P_1=Q_1=A; Q's boundary Q_c to Q_{c+1} is checked in the visible key automaton. Construct T_c by a left-to-right integer transfer on (P defects, Q defects, mismatch count, last P letter, last Q letter), extending with all four legal pairs; the terminal transition checks q and f. For c=0 use the unique empty prefix and its mass one.

For each locally valid indexed key w, define vP=number of B among exposed P positions, vQ=number of B among exposed Q positions, vD=number of mismatches in exposed paired positions. Then its exact historical population is

M(w) = T_c(Q_c,P_{c+1};kP-vP,kQ-vQ,d-vD), for c>=1;

M(w) = [vP=kP][vQ=kQ][vD=d], for c=0.

These identities follow by a bijection between each completion of the hidden paired prefix and the unique full ordered source pair with the fixed exposed w. The hidden P terminal bridge is included, and there is no hidden Q-only gap because Q_c..Q_n is indexed-visible.

Use a visible-key deterministic automaton emitting singleton Q_c (if c>=1), each pair (P_i,Q_i) for i>c through m, and then singleton Q_i for i>m through n. It tracks i,vP,vQ,vD,adjacent last exposed letters, q and first exposed P letter. It rejects non-A original endpoints and adjacent B. At terminal state s, let S(s)=(1,M(w)) when M(w)>0, else (0,0); at other states S(s)=sum_{a legal next token} S(s+a). This suffix recursion is valid because its finite state contains every dependence of the hidden-prefix mass and future visible transitions. Its root supplies qF, the count of distinct supported keys, and |F|, the exact positive integer count of source-distinct original pairs. No enumeration of raw histories or all supported keys is required.

Lex rank(w) sums the first component of S over strictly smaller legal successor tokens at each prefix. Unrank(j) (0<=j<qF) descends through children in token order and subtracts skipped subtree support counts. Once S is cached, each rank or unrank takes O(n) transitions; exact population of the recovered key is M(w).

Put D=(kP+1)(kQ+1)(d+1). T and the visible S have O(n D) states/constant-branching integer operations (boundary bits contribute a constant factor), and O(n D) storage. qF and |F| are <=2^(m+n), so all arithmetic involves O(m+n)-bit nonnegative integers; with linear-time integer addition a conservative bit-operation upper bound is O(n^2 D). The ranking procedure does not output every key or its populations.

## Boundaries and actual execution

When b=n-m the boundary reaches c=m; Stage456-B's hidden Q_m bridge, and its optional Q-only gap for smaller b, supply the adjoining regime. Stage455-B's pP>=1 grouped architecture has the same hidden paired-prefix structure but requires the P POP-tail coordinates. Thus this is the pP=0, c<m completion of the earlier restricted two-source frontier. No other alphabet has been claimed here.

Implemented in STAGE457B.py (Python 3 standard-library integer DP), actual stdout STAGE457B_EXECUTED.json. An independent small-instance oracle enumerates source words, groups exact R keys and compares every supported key's mass as well as all ranks/unranks. Deterministic bounded-grid sampling gave 1,476 parameter cases, 633 nonempty fibers, 287 cases with c=0, and 3,716 individually checked supported key masses and rank inverses. All assertions passed. Large configurations without raw-history enumeration:

(m,n,kP,kQ,d,b)=(64,80,15,17,1,25): c=55, qF=88,060, |F|=5,061,384,194,832,966, cached states=69,099.
(64,80,15,17,1,60): c=20, qF=6,655,258,248,672, same |F|, cached states=96,798.
(92,126,20,25,3,64): c=62, qF=723,177,765,620,200, |F|=1,121,449,082,621,221,549,433,213,976, cached states=286,097.

All of these are precise positive source-counting results over the declared restricted original X6 ordered-step population; no physical time-evolution or phase-amplitude result is inferred.

## Remaining science

Implement a single pP=0 algorithm merging c<m with Stage456-B's c=m and hidden-gap cases, test equality at b=n-m, and then extend lex rank/unrank to pP>=1 with its P POP-tail. For input alphabets >2, test which future experiments identify a hidden opposite letter versus only equality and find an exact minimal multi-letter observer key. Preserve source, joint relation, adjacency and every relevant future operation.
