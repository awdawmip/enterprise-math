# Exact QR/CRT prefix indexing and the paid complete-list boundary

Researcher-ID: EM-FACTOR-970540
Task: RS-FACTOR-BLIND-QR-CRT-PREFIX-INDEX-COST
Publication: TP2-F3369CF79B942BBC9DAB
Session: MCP-b6aba12a49e84046ab11d813a23ee7fe
Claim: MCP-a6baacb6070abdd7582abcd3
ER: ER-F46739EDA4DECD65B13A
Run: RUN-3e88eea0c4a31243f94a6958, generation1
Open request: crt-prefix-worker-20261013-005-own-open
Status: AUTHOR RESEARCH RETURN / NEGATIVE_BOUNDARY / PENDING GENUINE DRIVER REVIEW
Parent: OBJ-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE remains OPEN.
Basis: HEARTBEAT_NATIVE_X6 stays fixed; N, offsets, finite fields, CRT lists and costs are declared external observer models and grant no native-state or ontology bridge.

The exact two-list interface is computable without a joint M-cell table. Its complete preprocessing, storage, queries and certification are charged below. For the pure squarefree odd QR conjunction, materializing every nontrivial group list and inspecting every survivor in a length-L prefix nevertheless has uniform paid cost at least L exp(-O(log L/log log L)). This rules out a fixed positive power improvement for this declared representation and traversal. It proves neither a universal factorization lower bound nor a lower bound for rank-only, compressed, shared, batched or early-success methods. No novelty claim is made for CRT, meet-in-the-middle, pair counting or heap merging.

## 1. Public inputs and exact query contract

Input is an odd integer N>1 and a finite public list of distinct odd primes. One concrete deterministic selection rule is the first m odd primes, where m>=0 is a declared public parameter; generating and validating them is paid per instance. The algorithm never uses hidden factors or the true successful offset to choose m or the partition. Other deterministic public-N selection rules are covered by the mathematical bound after their actual selection cost is paid.

Compute c=ceil(sqrt(N)). Perfect-square recognition is paid; a separate factoring call may return that certified trivial branch, while an exact index query may continue. For every selected prime p compute gcd(N,p). When 1<gcd(N,p)<N, a factoring call may return the paid factor-revealing branch. If gcd(N,p)=N, it is not reported as a proper factor. Exact index queries in this return have the declared coprime precondition; a noncoprime input returns a typed NONCOPRIME_UNSUPPORTED_INDEX response unless the proper-factor branch was requested. The coprime theorem does not claim a lower bound on those earlier factor successes. In the supported index case M is the prime product and gcd(N,M)=1. M=1 is allowed. Define

    R_p={r mod p : (c+r)^2-N is a square modulo p, including zero}.
    F_N(t)=1 iff t mod p belongs to R_p for every selected p.
    C(L)=#{0<=t<L : F_N(t)=1}, L>=0.

For an integer U, rank_N(U)=0 if U<0 and C(U+1) otherwise. Thus the Task's inclusive endpoint is explicit. select_N(j), for integer j>=0, is the zero-based j-th nonnegative accepted offset. Negative or noninteger indices are domain errors. In the coprime pure-QR model S=product |R_p|>=1, so unbounded select has no absent answer. A bounded select_N(j;U) returns None when U<0 or j>=rank_N(U), otherwise the same selected offset. Rank/select describe necessary square conditions; they do not certify that the integer residual is a square or that a nontrivial factor has been found.

Construct the square-residue bitset modulo p by enumerating s^2 mod p, 0<=s<p, then enumerate r and test the exact shifted predicate. This deterministic local extraction includes zero and needs no oracle for a modular root of N. Its full p-bit table and accepted-residue entries are charged. It may be expensive and is not represented as an optimized root-extraction breakthrough.

## 2. CRT representation, rank, select and ordered enumeration

Partition primes deterministically into disjoint groups of moduli P,Q, with PQ=M and gcd(P,Q)=1. Greedy cardinality balancing is only a heuristic, not a theorem that a balanced partition exists. Construct complete group survivor lists A subset [0,P), B subset [0,Q) by the usual incremental CRT:

    r_new = r + R*((a-r)*inverse(R mod p) mod p).

At each step the old modulus is R and the new local residue is a. This produces each compatible tuple once and a unique residue modulo Rp. It proves soundness, completeness and absence of duplicates by induction and CRT injectivity. Write S_P=|A|, S_Q=|B|, S=S_P*S_Q. An empty group is modulus1 with a virtual singleton {0}; allocate and charge no imaginary cell for that singleton.

For nonempty groups set

    U={Q*inverse(Q mod P)*a mod M : a in A},
    V={P*inverse(P mod Q)*b mod M : b in B}.

The modulus1 contribution is simply zero, with no inverse call. The map (u,v) -> (u+v) mod M is a bijection onto all complete wheel survivors. In particular, uniqueness holds even when ordinary sums wrap at M. Sort both arrays when using the two-pointer variant; sorting is paid.

For 0<=h<=M put F(B0)=#{(u,v):u+v<B0}. Since 0<=u+v<2M,

    C(h)=F(h)+F(M+h)-F(M).                         (1)

Indeed the disjoint accepted ordinary-sum intervals are [0,h) and [M,M+h). Boundary h=0 gives zero, while h=M gives S. With L=qM+h and 0<=h<M,

    C(L)=q*S+C(h).                                 (2)

A two-pointer routine computes F(B0) in O(S_P+S_Q) comparisons/additions: start i=0,j=S_Q-1; if U[i]+V[j]<B0, all entries through j satisfy the threshold, add j+1 and increment i; otherwise decrement j. Each index moves only in its permitted direction. F(M) can be paid once and cached for subsequent ranks on this SAME instance. This is per-instance reuse, not free cross-instance preprocessing.

The alternative binary-search form sums, for each u, V counts in [0,h-u) when u<h and [M-u,min(M,M+h-u)). They are disjoint, so no residue is counted twice. This needs O(S_P log(S_Q+1)) comparisons; exchanging groups gives the reverse option. After charging the sorting/caching chosen, a rank can use the least of these certified bounds. No optimality is claimed for the old binary-search implementation.

For select, divide j=qS+j0, 0<=j0<S. Binary-search h in [1,M] for the least h with C(h)>j0; then select_N(j)=qM+h-1. Such h exists because C(M)=S and C is monotone. Minimality proves it is precisely the required index. Unbounded j is included in arithmetic width.

For ordered traversal, each fixed-u row lists (u+v) mod M with V sorted. Split at lower_bound(V,M-u): the wrapped tail precedes the nonwrapped head. This is a sorted row. Append its next-period copy by adding M, and merge these S_P rows with a heap, stopping at L. CRT uniqueness proves no tied residue/output duplicates. All accepted offsets are emitted once in increasing order; the resulting candidate order is exactly the ascending QR-filtered Fermat order. Optimizing the same traversal in the matched comparator eliminates any supposed ordering advantage.

Exact query pseudocode after the paid preparation is:

```text
PAIR_LESS(B0):
    i=0; j=len(V)-1; answer=0
    while i<len(U) and j>=0:
        if U[i]+V[j]<B0: answer+=j+1; i+=1
        else: j-=1
    return answer
PERIOD_PREFIX(h):
    return PAIR_LESS(h)+PAIR_LESS(M+h)-cached_PAIR_LESS_M
RANK(U_endpoint):
    if U_endpoint<0: return 0
    q,h=divmod(U_endpoint+1,M)
    return q*S+PERIOD_PREFIX(h)
SELECT(j):
    require integer j>=0
    q,j0=divmod(j,S)
    h=least integer in [1,M] with PERIOD_PREFIX(h)>j0
    return q*M+h-1
BOUNDED_SELECT(j,U_endpoint):
    require integer j>=0
    if j>=RANK(U_endpoint): return None
    return SELECT(j)
```

Preparation stores sorted weighted U,V and computes cached_PAIR_LESS_M once, all paid. The U array name is distinct from the scalar inclusive U_endpoint.

## 3. Complete per-instance cost ledger

Let B_* be at least the bit length of max(2,N,M,L,(j+1)M,p_max+1) for the actual requested operations, putting p_max=2 for an empty prime list. For rank-only omit the irrelevant j term; for unbounded select it MUST be included. Also allow counters through S<=M and C(L)<=L. Use ordinary schoolbook arithmetic as a concrete conservative implementation: B-bit addition/comparison O(B), multiplication/division O(B^2), Euclidean gcd/inverse and binary-search integer square root O(B^3). These are sufficient upper bounds, not optimal bit-cost claims.

The complete paid ledger is:

| Stage | Concrete charged bound or quantity |
|---|---|
| Input read, square recognition, c | Read all input bits; O(B_*^3) for integer root and recognition |
| First-m public prime generation | Trial-divide all odd candidates through p_max; O(p_max^(3/2) B_*^2) conservative work |
| Supplied-prime validation | Sort/duplicate/odd checks and sum_p O(sqrt(p) B_*^2) primality trial divisions; no unverified “prime” labels |
| gcd(N,p), M construction | O(m B_*^3) including charged products and Euclidean checks |
| Local QR sets | O(sum_p p B_*^2) work; p-bit square bitsets and all accepted residues are paid |
| Complete partial CRT lists | At most O(m(S_P+S_Q) B_*^2 + m B_*^3) work, plus E actual entries written; intermediate cardinalities are no larger than each complete final list |
| CRT weights | O(B_*^3+(S_P+S_Q)B_*^2); empty group incurs no inverse or artificial array |
| Sort/cache | O((S_P log(S_P+1)+S_Q log(S_Q+1))B_*) comparisons; F(M) O((S_P+S_Q)B_*) if selected |
| One rank | Period division/product O(B_*^2) plus O(B_* min(S_P+S_Q,S_P log(S_Q+1),S_Q log(S_P+1))) under the selected paid arrays |
| One select | O(log(M+1)) rank-threshold calls, plus j/S and qM arithmetic O(B_*^2); charge wider B_* for large j |
| Ordered full-prefix enumeration | O((S_P log(S_Q+1)+S_P+C(L)log(S_P+1))B_*) heap/search work, plus every output and inspection |
| Integer square certification | For every inspected t, form z=(c+t)^2-N; integer-root and equality check O(B_*^3), then gcd/equality/factor verification on successful squares, also charged |
| Memory | Conservative O((sum p+S_P+S_Q+m)B_*) bits plus output buffering if retained; streamed outputs still incur write cost |

One can release old local bitsets after group generation and avoid retaining all outputs, but cannot omit work already performed. Heap comparisons and writing B-bit offsets are never constant-time bit operations. Even if a rank answer is small, its preprocessing remains charged. There is no across-instance table reuse or unproved amortization here. The finite lower bound below uses only positive constant entry/inspection charges, which are smaller than these actual bit costs; the ledger does not pretend that this lower bound equals a tight bit upper bound.

## 4. Uniform prefix theorem and complete-list paid obstruction

Let k be the number of primes, a_p=(p+chi_p(N))/2, S=product a_p, delta=S/M, chi_p(0)=0. The shift by c is a residue permutation. Counting (x-y)(x+y)=N over F_p gives sum_x chi_p(x^2-N)=-1; there are 1+chi_p(N) zero residuals. Hence the zero-inclusive accepted count is exactly a_p>=1. Sorting the distinct odd primes p_i gives p_i>=i+2, and therefore

    delta>=2^(1-k)/(k+2),     M>=(k+2)!/2.             (3)

These statements hold for every subset and the empty product.

The sole classical deep input is the prime Kloosterman bound |sum_(u!=0)e_p(Au+B/u)|<=2sqrt(p) when p>2 and A,B are nonzero. I actually read Gergely Harcos's entire 14-page author-hosted proof, including Theorem1 and its exact nondegenerate parameters. [Harcos, Weil's bound for Kloosterman sums](https://users.renyi.hu/~gharcos/weil.pdf). This is a checked author exposition, not a claim that I read Weil's original 1948 article.

For the same Gauss sum tau, character expansion and completion of the square give the signed exact identity

    sum_x chi_p(x^2-N)e_p(hx)
      =sum_(u!=0)e_p(-Nu-h^2/(4u)).                  (4)

The two chi(u) factors and the SAME tau cancel. For h!=0 both Weil parameters are units. At h=0 the sum is -1 directly, so no degenerate application is made. The zero-inclusive indicator is

    I_p(x)=(1+chi_p(x^2-N)+1_(x^2=N))/2.

Its Fourier coefficient H_p(0)=a_p, while |H_p(h)|<=sqrt(p)+1 for h!=0. Thus |H_p(h)|/a_p<=2/(sqrt(p)-1)<=5/sqrt(p), valid at p=3 as well.

CRT factorizes the composite Fourier coefficient, with local frequency h*(M/p)^(-1) mod p. For h!=0 mod M let d=M/gcd(h,M). Retain local means at primes dividing h; apply the nonzero estimate only at primes of d:

    |H_M(h)|<=S*5^omega(d)/sqrt(d).                 (5)

Fourier inversion for any shift c and any positive integer L is exact. The frequencies of conductor d are h=(M/d)b, gcd(b,d)=1. A geometric sum at frequency b/d has magnitude <=1/(2||b/d||). Pairing b,d-b and enlarging units to all 1<=b<d bounds their sum by d(1+log d). Consequently

    |C_L(c)-delta L|
      <=delta(1+log M)sum_(d|M,d>1)5^omega(d)sqrt(d)
      <=delta*6^k*sqrt(M)*(1+log M).                (6)

The last inequality uses product_(p|M)(1+5sqrt(p))-1<=6^k sqrt(M). This conductor argument covers L<M honestly; complete-period density alone cannot do so. M=1 gives C_L=L with no Fourier remainder.

Assume each NONTRIVIAL group has its complete list materially constructed for this instance and each accepted prefix offset is separately inspected. Let E be the number of real list entries. If both groups are real, E>=S_P+S_Q>=2sqrt(S); if one group is virtual modulus1, E>=S>=sqrt(S). For M>1, therefore E>=sqrt(S). For M=1 both can be virtual, E=0, but C_L=L. With fixed positive entry and inspection prices lambda,mu and separate additive operations,

    W>=lambda E+mu C_L(c).                          (7)

No virtual entry is charged, no balanced partition is presumed, and no operation is counted twice.

Put K=max{j>=0:(j+2)!/2<=L^2} and
Phi(L)=(6sqrt(2))^K*(K+2)*(1+2log L). Then uniformly for EVERY chosen M,

    W>=min(lambda,mu)*L/Phi(L).                     (8)

Proof for M<=L^2: k<=K by (3). Set D=6^k sqrt(M)(1+log M). If D<=L/2, (6) gives C_L>=delta L/2>=L/[2^k(k+2)], sufficient for (8). Otherwise M>1 and

    sqrt(S)=sqrt(M delta)
      > L/[sqrt(2)(6sqrt(2))^k sqrt(k+2)(1+log M)]
      >= L/Phi(L).

Here use log M<=2log L, k<=K and sqrt(2(K+2))<=K+2. Storage alone supplies the bound; a positive prefix count is not assumed. At M=1 use mu L.

Proof for M>L^2: take the shortest sorted-prime prefix R_j>L^2. R_(j-1)<=L^2 implies j<=K+1, WITHOUT bounding total k. Its accepted count exceeds L^2/[2^K(K+3)] by (3); every remaining a_p>=1, so S is at least that count. Thus E>=sqrt(S)>L/[2^(K/2)sqrt(K+3)]>=L/Phi(L). This covers super-polynomial M and arbitrarily large total prime count. L=1 has K=0,Phi=2; either a real entry or an inspection covers the bound.

Finally K=O(log L/log log L), so log Phi=O(log L/log log L) and

    W>=L exp(-O(log L/log log L))=L^(1-o(1)).         (9)

This excludes a fixed positive power improvement for complete required partial lists AND complete survivor inspection. Constant or subpolynomial gains are permitted. For Fermat through the true endpoint take L=T+1; choosing actual M does not use hidden T. A factor found earlier or a gcd success is outside this full-prefix traversal theorem. Any method avoiding a REQUIRED nontrivial full group list needs another proof; an allowed virtual mod1 group alone does not remove a method from this theorem.

## 5. Actual prior-art and matched-comparator judgment

The primary comparison is bounded to genuinely read documents, not a literature-completeness or novelty claim.

William B. Hart, [A one line factoring algorithm](https://wrap.warwick.ac.uk/id/eprint/54707/1/WRAP_Hart_S1446788712000146a.pdf), J. Aust. Math. Soc.92(2012),61–69, DOI10.1017/S1446788712000146, was read in full from the Warwick version of record (nine article pages plus archive cover). Section2 iterates multipliers and certifies squares/gcds; Section3 uses small-modulus square screening. Section5 explicitly accounts for matched trial work and interpreter overhead. Our fixed-N offset stream differs from that multiplier loop, while square screening and its paid-certification requirement have clear antecedents. Its timings and heuristic exponent are not imported as measurements or theorems about our prefix model.

Richard Schroeppel and Adi Shamir, [MIT-LCS-TM-147](https://hdl.handle.net/1721.1/148974), January1980, was actually read in full from the MIT archive text, with the heap sections checked against PDF text. This is their original technical report, not an assertion that the 1981 SIAM version of record (DOI10.1137/0210033) was read. Section3, printed pages13–15, implements online sorted pair streams by retaining one item per row in a heap and advancing that row after extraction. Printed page1 expressly suppresses polynomial factors in exponential complexity; those factors cannot disappear from our ledger. The row mechanism matches our implicit pair stream. Its monotone ordinary composition does not itself prove cyclic modular rows, CRT uniqueness or prefix rank/select; Section2 supplies those arguments. CRT contributes a bijection of compatible local tuples, not a new information source about hidden factors. The index omits the JOINT M-cell table while retaining full partial lists; that change is real, but free setup or balance is not.

The matched comparator uses the SAME N,c,prime selection, pure QR predicate, survivor order, arithmetic widths, gcd/square certification, per-instance preprocessing and allowed reuse. A straightforward streaming Fermat scan incrementally forms z(c+t) and uses the same local screens; an equally optimized wheel comparator may use precisely the CRT index of Section2. It then has identical preprocessing, rank and output costs. Thus renaming this known mechanism offers zero ordering or information advantage against that comparator. The new scoped statement (8), rather than encoding compression or old toy timings, closes this particular complete-list/full-traversal cost escape.

No finite benchmark advantage is claimed. Rank-only and select-only are exact supported queries, but neither is automatically factor certification, and (8) is not applied to them alone. A new retrieval model omitting nontrivial complete lists, or a legitimate within-instance amortized query regime, is a distinct prospective cost question.

## 6. Real timing, contributions, preserved evidence and next unit

The earlier prototype, its 3043 tiny-query checks, original 600/1400 corpus, 63 checks and auxiliary reports remain frozen inherited evidence. None was rerun here and none is described as EM-FACTOR-970540's postclaim experiment. Old prototype and auxiliary actors remain UNKNOWN / DIRECTED_NONBLIND. Root supplied the direction, candidate discrepancy/paid-bound formulas and two-pointer rank alternative; Root aliases disclosed in my actual session are EM-DVR-FBF223,EM-DVR-4C90FB,EM-DVR-C1A1D9,EM-DIRECT-E1F2B6,EM-DIRECT-FA0C27,EM-DIRECT-49ADE6. They are contribution overlap, not my identity.

The inherited prefix lemma was prepared before my formal open by /root/backlog_geo6_followup_unit (UNKNOWN/directed nonblind). The nonauthor auxiliary paper reviewer also disclosed pre-freeze constant and virtual-entry feedback; that report is helpful evidence, NOT a clean-room or Native decisive review. My actual post-open work is full primary-text reading/verification, checking the complete inherited deduction, resolving exact query endpoints and virtual groups, the paid bit ledger, comparator integration and this scoped research return. I share Root context and claim no blind independence.

Taskbook own006 actual artifact is complete and hash-verified. Root has additionally saved the inherited lemma and directed auxiliary review at actual Source50b50b784151b27379f9ee8a0253783805e6c90d, under research_notes/FACTORBLIND_IMPLICIT_CRT_PREFIX_WEIL_COST_20261013_FBF223/; the lemma remains d52df511d3e591fed210c231f0e8da7c8d3aedf6d9125656ad45dc4062340885 (14442B) and the auxiliary review 067cf1444295dac7a80e85ebc3f9ebd65ebe3c0a4a08bddb31b11f0f1dccf121 (9739B). Their preparation preceded my claim and their later Source custody is disclosed. The initial continuation packet exposes only Taskbook/publication; own007 declared-RR artifact was definitively rejected ARTIFACT_NOT_IN_CONTINUATION_PACKET. The four exact declared immutable Source references were instead cold-read through connected GitHub with unrestricted/nonblind Task scope, complete bytes and SHA/blob checked. This is recorded; no failed artifact is claimed successful. The raw original RR verdict/disposition and operative accepted DR are unchanged.

Task hard-target disposition: SATISFIED_WITHIN_DECLARED_SCOPE. Required output1 has the exact query model, deterministic construction, correctness and pseudocode; output2 has the complete paid bit/space ledger; output3 has the actual primary comparison and explicit duplication limits; output4 has the scoped uniform obstruction and its remaining boundary. This is the author's evidenced Task-local judgment, pending genuine independent review, not a native Task-completion record.

Verdict: NEGATIVE_BOUNDARY for the full materialized required-group-list/full-survivor-inspection route, with exact rank/select proof and complete paid ledger delivered. This does not grant S1,S2,S3, broad all-N-derived impossibility, Foundation, Working Truth, or parent completion. The next mathematical unit is an exact retrieval/count contract that avoids at least one required nontrivial complete list, followed by full construction/bit-cost analysis and the same optimized comparator. Do not rerun the old frozen experiments or re-prove the already accepted fixed-period/explicit-table bounds. Genuine independent Driver review remains required; Root's mathematical contributions must not be cleared by changing aliases.

