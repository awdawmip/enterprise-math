# Stage438-B — Exact joint future quotient in the protected-overlap X6 regime

Date: 2026-11-05. Classification: AUTHOR_SIDE_PROOF / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. Parent: Stage437-B at immutable research commit `e098cfb9417d3df15c89da6843dd4d110917d67a`, Draft PR #1736.

## Scientific inputs, carrier, observer

Frozen scientific pins: GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Normative rules are read separately from the current canonical main. The active P000/Heartbeat World has six native spatial axes (twelve signed primitive directions); these ordered paths are static X6 observer objects, not a claim about physical heartbeat evolution. All ordered path identities, multiplicities and matched-unit BRC branches remain typed by the declared observer/horizon.

Let D={±E_1,...,±E_6}. Two initial words P∈D^m,Q∈D^n carry ordered labeled directions. The **complete observed state** is

    O(P,Q)=(m,n,V_P,V_Q,J_P,J_Q,K),
    V_X=sum_i vec(X_i), J_X(a,b)=#{i:X_i=a,X_(i+1)=b},
    K=sum_{i=1}^{min(m,n)}[P_i=Q_i].

K is the exact count of positive unit-weight BRC match branches. The positive CWM recoalescence summary is (K,K,1) for K>0 and (0,0,0) for K=0; the full ordered-source provenance is retained as needed for future comparison. POP deletes the last direction; APPEND(d) adds any of all twelve directions. Each source has independent total POP/APPEND budgets (p_P,r_P,p_Q,r_Q), and all legal interleavings and all intermediate readouts are observed. Assume n≥p_Q+1≥1, m≥p_P+1, r_P,r_Q≥0, and

    m-p_P ≥ n+r_Q.   (protected overlap)

Thus no legal P operation modifies any original index ≤ n+r_Q, and Q never reaches beyond n+r_Q.

## Theorem 438.1 — exact *minimal* full-future classes on every present-O fiber

Write S_P=P_(m-p_P)...P_m and S_Q=Q_(n-p_Q)...Q_n (inclusive, one-based). For i≤n put b_i=[P_i=Q_i]. Define the exact repair key

    R_0=(S_P,S_Q, b_(n-p_Q+1),...,b_n),                       if r_Q=0;
    R_+=(S_P,S_Q, P_(n-p_Q+1),...,P_(n+r_Q)),                if r_Q≥1.

For any two histories (P,Q),(P',Q') with the same complete current O and the same budgets satisfying protected overlap, their **complete future observations coincide for every legal finite operation word if and only if their appropriate R_0 or R_+ keys agree.** Consequently the minimum number of full-future classes inside a current-observer fiber F is exactly

    q_F = |{R(P,Q):(P,Q)∈F}|,

and the optimal fixed-length class label has ceil(log2 q_F) bits. This is an observer/horizon-specific quotient. Restoring an individual original history additionally requires its within-class index.

### Proof: recoverability of own-source suffixes

For any nonempty word X, the identity

    V_X − ∑_(a,b) J_X(a,b) vec(a) = vec(X_last)

recovers its last signed native direction uniquely from the complete observed endpoint/adjacency. A POP transforms J by subtracting one edge (X_penultimate,X_last) and V by subtracting vec(X_last). The observed change in J identifies the penultimate direction, including when other equal edges occur. Iterating a source-only POP word of length at most p_X recovers precisely the original last p_X+1 directions. Thus full-future equivalence requires S_P=S'_P and S_Q=S'_Q. The recovery uses the one source's observations and does not assume cross-source matching.

### Case r_Q=0: exact equality-bit repair

Q can only POP. P always has length at least n and its initial first n letters never change. With t Q-POPs and any interleaving of P operations,

    K_t = K_0 − ∑_(j=n-t+1)^n b_j  (0≤t≤p_Q).

The last p_Q bits are read separately from consecutive differences of K along Q-only POP prefixes. Earlier overlap contributes the fixed aggregate K_0−∑lastbits. Equal S_P,S_Q determine every own-source V,J update and legality, while these b bits determine every future K. This proves necessity and sufficiency of R_0.

### Case r_Q≥1: full exposed P labels

Fix i∈[n-p_Q+1,n+r_Q]. If i≤n, Q can perform n−i+1 original POPs followed by APPEND(d) for any d∈D; if i>n, Q can perform i−n APPENDs with arbitrary prescribed letters. At the particular APPEND that fills index i, P is unchanged during this testing word, and the observed increment in K is [P_i=d]. Varying d over all twelve primitive directions identifies P_i uniquely. Hence full-future equivalence requires all P labels in the exposed interval to agree.

Conversely Q's initial removed suffix and all its newly appended letters are available from S_Q and the live appended stack. Every cross-comparison at an index ≤n−p_Q is a permanently shared original-prefix comparison, whose aggregate is recoverable from K_0 after subtracting the known comparisons above that index. Every comparison at larger indices uses the exposed P labels, the known Q suffix or an explicit newly appended letter. P's own operations leave all exposed P indices intact; S_P and the live appended stack determine own-source V,J updates. Therefore R_+ reconstructs K and all other observer components for every legal interleaving. The necessity argument above gives the reverse implication. QED.

## Theorem 438.2 — a parameter family where one extra APPEND changes the class count

Let A=+E_1, B=−E_1, C=+E_2, integers n≥p+2, p≥1 and m≥n+3. Set p_P=0, r_P=1, p_Q=p and let P(j)=A^(j−1) B A^(m−j), j=2,...,m−1; Q=C^n. The current full observer is identical across exactly m−2 such P histories: V_P=(m−2)E_1, J_P(AA)=m−4, J_P(AB)=J_P(BA)=1, K=0. Other J entries are zero, Q=C^n is uniquely fixed. These are all histories in the specified present-O fiber.

With r_Q=0, every P_i∈{A,B} differs from Q_i=C. Every repair key R_0 agrees, so

    q_F(p,0)=1,  M_0=m−2,  fixed code length=0 bits.

The sufficient Stage437 corridor retains the p original P directions at positions n−p+1,...,n, generating p+1 different corridor signatures on this same fiber. Hence it is strictly finer than the minimum future quotient.

With r_Q=1 (and m≥n+3), the exposed P interval is [n−p+1,n+1], containing p+1 positions. The defect B occurs either at one of those positions (p+1 singleton classes), or outside the interval (one class of population m−p−3). Therefore

    q_F(p,1)=p+2,
    class populations=(m−p−3,1,...,1) [p+1 singletons],
    fixed code length=ceil(log2(p+2)) bits.

The off-window population is ≥1 under the hypotheses. The same class counts arise by direct U-key ranking; rank 0 represents off-window, ranks 1..p+1 represent defect at index n−p+rank. To reconstruct a particular original P in the off-window class, retain an intra-class defect-position index. All counts are exact integers and retain positive BRC population multiplicity.

## Theorem 438.3 — sharp match-bit classes without Q APPEND

Keep the same P(j) and budgets p_P=0,r_P=1,p_Q=p,r_Q=0 but set Q=A^n and restrict the current complete fiber to K=n−1. Exactly the j=2,...,n histories occur. Their R_0 keys separate the p defects in positions n−p+1,...,n and merge the earlier defects. Thus

    |F|=n−1, q_F=p+1,
    class populations=(n−p−1,1,...,1) [p singletons],
    fixed code length=ceil(log2(p+1)) bits.

The distinct singleton classes are separated by the corresponding Q-only POP step's K decrement. Rank 0 denotes j∈[2,n−p] and rank t∈[1,p] denotes j=n−p+t. The optimal class code needs the within-class index j−2 to reconstruct a rank-0 original history. This provides a sharp equality-bit lower-bound witness.

## Exact computation and cost

Executable `REPRO_STAGE438B.js` exhaustively enumerates complete present-observer fibers over three initial directions A/B/C on five small parameter domains, then explores **every** legal operation word and all twelve native APPEND directions. It compares the full observation after **every operation prefix**, not only final K, with the above R key. Tested initial pairs total 39,878; all 5 domains agree with the theorem; 42 zero-Q-append parameter families and 18 one-Q-append transition families were additionally checked. The executed JSON records exact counts. All arithmetic uses safe exact JS integers in the tested finite domain. The infinite-parameter theorems above rest on the proofs, with computation as a cross-check.

Computing current O, the R key and its symbol/bit payload from raw P,Q takes O(m+n) word operations. The key adds at most p_P+p_Q+2 native symbols plus p_Q bits when r_Q=0, or p_P+p_Q+2+p_Q+r_Q native symbols when r_Q≥1 (duplicate suffix symbols may be merged). Future updates require O(1) direction comparisons and constant many bounded-integer updates per POP/APPEND, plus an O(r_P+r_Q) live stack. The fixed 144-entry J and six signed coordinates have O(log(m+n+B)) bit registers, B the total operation budget. Rank/unrank of arbitrary current-O fibers may require additional enumeration; only the explicit one-defect family has direct O(1) class rank from the identified defect position and O(m+n) source parsing. Minimal class length is an information bound and does not assert universal polynomial-time construction of an optimal codebook.

## Next unresolved unit

Stage439-B: remove the protected-overlap length inequality. Determine the minimal cross-source repair when both P and Q can move below each other's previous overlap boundary, including the consequences of P POP/APPEND followed by Q POP/APPEND. Seek the first explicitly verified case where the one-sided protected-key formula fails, and an exact joint alignment repair or smaller quotient. Preserve identity, original P000 and frozen science, provenance and unsigned/positive branch semantics; no automatic native task CLAIM or theorem admission follows from this author-side source.
