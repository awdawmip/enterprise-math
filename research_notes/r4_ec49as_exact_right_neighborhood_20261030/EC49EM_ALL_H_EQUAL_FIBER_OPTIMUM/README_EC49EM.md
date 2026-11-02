# EC49EM — All-horizon equal-positive-count native-prefix optimum

**Research date:** 2026-11-02. **Status:** AUTHOR_ANALYTIC_THEOREM / EXACT_INTEGER_CHECK_PASS / INDEPENDENT_SYMPY_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## 1. Exact question and frozen scientific scope

Continue EC49EL at commit 313f3d90fc9350d87d8bf9f713309935998c8619 (earlier EC49EK caa970c88315d55d1b1669589ef096a83c7d059b). Retain its frozen scientific inputs: GLOBAL_KNOWLEDGE_V1@773d538180bfb49e24cffeb35c3ee75eb0628e2e and Enterprise Math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. These are SCIENTIFIC pins, distinct from current behavioral rules.

The seven legal operations are signed-primitive native X6 paths:

    a=(-1,-1), b=(-2,-2),
    c=(1,2,-1,-2), d=(2,1,-2,-1),
    e=(3,1,1,-3), f=(1,-1), g=(2,-2).

Each future word of exactly h operations returns displacement +2 E1; hence #b=0 and #e=#a+1. The nine genuine seam-history atoms are

    (N,0),(N,1),(N,2),(A,0),(A,2),
    (B,0),(B,1),(AB,0),(BA,0).

A is adjacent (+E1,+E2); B is adjacent (+E2,+E1). The final observable is one of N,A,B,AB,BA (first A/B order). Each native positive step also contributes a symbolic strictly-positive weight in each of two independent multiplicative BRC channels. Words are distinct observation carriers even if their positive-count vector and numerical BRC monomial are equal.

For every h=2,...,H, require a set of words (all length h) which (i) all have the same complete six-axis positive native-step count within that h, and (ii) have nine-row terminal observation rank 9 over Q. Across words/horizons charge every *distinct ordered signed-primitive prefix edge* only once. Let U_equal(H) be the globally minimum total cost. Positive-count vectors are allowed to differ between distinct horizons.

**Main theorem. For every integer H >= 5,**

    U_equal(H) = 4 H + 30.                              (1)

In particular U_equal(9)=66. More strongly, any full-rank fixed-positive-count choice at h=9 that contains at least one c or d, when added to the mandatory h=2 tree, costs >=70. Therefore no 65-edge witness exists at h=9.

These are exact statements of the native-prefix accounting model, not claims about processor runtime, storage usage or physical Heartbeat evolution.

## 2. Multiplicity, length and the mandatory base

Set r=#a, q=#c+#d, u=#f, v=#g, #e=r+1. The return equation and native signed-primitive path length are

    h = 2r+1+q+u+v,
    L = 2h+2r+2q+2.                                    (2)

At h=2 the complete full-rank positive-count fiber is uniquely represented by the four words

    ce, de, ec, ed,

with p=(3,1,1,0,0,0). Their signed-primitive prefix tree has exactly 28 edges. Complete two-operation enumeration verifies that no different positive-count fiber or proper subset reaches nine-row rank 9. Denote its exact prefix set by T2. Thus every multi-horizon execution includes T2.

Every path with first letter c, d, or e shares at most eight of its earliest native prefixes with T2 (T2 contains four length-eight leaves). A path with first f or g shares exactly one earliest primitive edge; its second edge differs from the c/d continuation in T2. A path with first a shares no initial edge. Different first signed-primitive directions have disjoint subtrees.

## 3. Exact 12-signature rank lemma (finite algebraic certificate)

For q>=1, the reduced internal first-event state is in {A,B,AB,BA}, never N. A transfer signature is (tau,epsilon) with tau=0 for first a/e (neutral native initial direction), tau=1 for first c/f (+E1), tau=2 for first d/g (+E2), and epsilon in {A,B,AB,BA}. There are exactly 12 formal signatures. The EC49EL primitive-path quotient shows this pair determines the complete nine-history terminal transfer, independent of subsequent order not affecting the first A/B sequence.

**Rank lemma.** For any set S of q>=1 signatures, the joint terminal observation rank is 9 if and only if:

    (1,A) in S and (2,B) in S,
    ((0,A) in S or (2,A) in S), and
    ((0,B) in S or (1,B) in S).                          (3)

Equivalently, S contains one of the four inclusion-minimal rank-nine sets:

    I   {0A,0B,1A,2B}
    II  {0A,1A,1B,2B}
    III {0B,1A,2A,2B}
    IV  {1A,1B,2A,2B}.

Here 0A abbreviates (tau=0,epsilon=A).

**Exact proof of (3).** The four missing-signature families give left-null vectors of the 9x(5|S|) zero-one observation matrix, with rows in the nine-history order stated in §1:

    Exclude 2B:          (0,0,0,0,0,-1, 1,0,0)
    Exclude 1A:          (0,0,0,-1,1,0,0,0,0)
    Exclude both 0A,2A:  (0,0,0,0,-1,0,0,1,0)
    Exclude both 0B,1B:  (0,0,0,0,0,0,-1,0,1).

Direct native-transfer evaluation verifies each is a nonzero integer annihilator for every type left in its family. This proves necessity. For each of I–IV, select nine of its twenty observation columns: exact Bareiss elimination yields determinant -1 in all four cases (the column indices and raw transfer computation are included in the executed checker). This proves sufficiency and the rank lemma for the whole 12-signature universe without an infinite search. The executed JS checker additionally enumerates all 4095 nonempty type subsets; its modular full-rank test is exact over Q because every zero-one 9x9 minor has |det| <= 3^9=19683 < 1,000,003. An independent SymPy exact-rational check finds four minimal full-rank sets (each rank 9) and four maximal non-full-rank sets (each rank 8).

## 4. Primitive last-four divergence lemma

The operation-to-native-step code in §1 is prefix-free: no complete operation's signed-step sequence is a strict prefix of another. Consider two return words with the *same h and p*, same neutral-first category tau=0, but distinct internal first-event states epsilon=A and epsilon=B. Both have native length L.

**Lemma.** Their signed-primitive paths have longest common prefix of length at most L-4.

Indeed identical first L-3 primitive steps, decoded via the prefix-free alphabet, would have identical earlier complete operations and would already reveal the starting signed direction of any c/d occurring as late as the last four steps. Since c starts +E1 while d starts +E2, two such paths cannot have different first c/d event within their last three unseen steps. This contradicts epsilon=A versus B. Therefore the second neutral witness must introduce at least four distinct native-prefix edges after the first, provided the previous baseline tree ends earlier than L-4. Here h>=5 and q>=1 imply L>=14 and L-4>8, so those four edges are also outside T2.

A direct exhaustive signed-primitive regression for h=2..7 checked 3008 lexicographically nearest opposite-event neutral-fiber boundaries; the minimum new tail was four primitive steps. The lemma's all-h scope follows from the prefix-free proof, not this finite regression.

## 5. Universal lower bound for q>=1

Fix h>=5 and any full-rank fiber with q>=1. By (2) every word in it has the same native length

    L >= 2h+4.                                         (4)

Apply the four necessary rank-mask alternatives of §3. Each bound below counts only distinct prefix edges *not already in T2*; this remains valid even if further words share branches.

* I (0A,0B,1A,2B): choose one neutral, one +E1 and one +E2 initial-root path. Their different native first directions make their out-of-T2 tails disjoint, and each contributes >=L-8. By §4, the other neutral first-event path contributes >=4 more edges. Therefore extra >=3(L-8)+4.
* II (0A,1A,1B,2B): the 1B path cannot start c, because c itself creates internal A first; it must start f, sharing only one prefix with T2. A neutral and a 2B path begin in two other primitive root directions and each share at most eight prefixes. Therefore extra >=(L-1)+2(L-8).
* III (0B,1A,2A,2B): symmetrically, 2A must start g, giving the same bound (L-1)+2(L-8).
* IV (1A,1B,2A,2B): 1B requires an f-first path and 2A a g-first path. Their first native directions are distinct and each shares exactly one prefix with T2. Extra >=2(L-1).

Together with (4), every q>=1 full-rank choice contributes at least

    min(6h-8, 6h-5, 4h+6) >= 4h+2,   h>=5.              (5)

For h=9 these alternatives are 46,49,42, so q>=1 adds >=42 edges beyond the mandatory 28, for a total >=70.

## 6. q=0 lower bound and construction attaining equality

If q=0, the EC49EL fixed-fiber rank theorem requires u>=1 and v>=1. Thus a full-rank choice must have an f-first path and a g-first path. Both have length L=2h+2r+2 and distinct initial native directions; each shares exactly one edge with T2. Hence

    extra >= 2(L-1) = 4h+4r+2 >= 4h+2.                 (6)

For every h>=3 define the two genuine return words

    F_h = f e g f^(h-3),        G_h = g e f f^(h-3).

Both have positive-count vector (h,1,1,0,0,0), native length 2h+2, and displacement +2E1. Their transfer signatures are (1,N) and (2,N); their selected 9x9 integer terminal minor is -1, so they recover all nine history atoms. Both BRC channel monomials coincide within each horizon because the complete six-axis positive counts coincide.

For increasing h, F_h is a signed-primitive prefix of F_(h+1), and G_h is a prefix of G_(h+1). Their two trees share with T2 only the first +E1 or +E2 primitive edge, respectively. Consequently, T2 plus all F_h,G_h for h=3,...,H contains exactly

    28 + 2((2H+2)-1) = 4H+30

distinct primitive-prefix edges. This meets (5)–(6) for the maximum horizon H>=5, proving (1). Intermediate horizons automatically have the required rank 9 and equal-positive-count property.

At H=9: T2 has 28 edges; F_9 and G_9 have 20 native edges each and overlap T2 on one edge each; the union has 28+19+19=66 distinct prefix edges.

## 7. Reproducible evidence and limits

* VERIFY_EC49EM.js (Git blob named in publication receipt): independent V8 execution checks all 4095 nonempty rank-type subsets, finds exactly the four minimal rank-nine masks, computes four determinant -1 integer minors with BigInt Bareiss, completely enumerates the h=2 fiber/subsets, directly replays true signed-X6 histories, and checks F_h/G_h prefix cost and equal positive counts for h=3..30. EC49EM_EXECUTED.json is the actual output, not a guessed result.
* Separate independently executed Python standard-library regression: 4095 masks, 3008 nearest unlike-event neutral-fiber pairs over h=2..7, positive BRC multiplication, signed displacement and witness costs through H=25; PASS. Independently written SymPy rational-rank checker verifies four rank-nine minima and four rank-eight maximal nonfull sets, directly repeats h=2 and witnesses through h=12; PASS.
* Proof strength: the all-H>=5 statement comes from finite exact 12-signature algebra plus the structural prefix lower/upper bounds. Neither finite h tests nor a numerical optimization solver is extrapolated to infinity.
* Scope: no physical time evolution, arbitrary observer, tensor/slice generalization, global-across-all-h positive-count equality or processor-time complexity is claimed. The native six-dimensional substrate and P000 remain unchanged. Artifact publication does not constitute independent Driver acceptance.

## 8. Provenance and continuation

Historical scientific sources remain frozen as in §1. Behavioral/current project read snapshot for this author run: GLOBAL_KNOWLEDGE_V1 main@4c10a4e2334b18d778c8ba9ab80e6d356cbc8f10 and EnterpriseMath main@2257276362a3c515c128472b6c7c922d2bca3040. Verified P000 startup projection Git blob c6d4d2d79b09537bdae55253baef9c28583e44dc against original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE worldview preserved.

GitHub authenticated user awdawmip; project GitHub repository writable. Native Enterprise Math 0.6.11 research session attempt was rejected STATIC_READONLY_SCOPE_DENIED (operation_sent=false), and the active owner inventory returned CONTROL_QUOTA. No Source-native activity, CLAIM, Result or independent Driver disposition is asserted. The PR branch holds author-side portable research only.

**Next EC49EN.** Use the now-proved optimal trie to minimize the *combined* cost vector (native primitive edges, distinct BRC positive-count monomials, terminal observer matrix storage) over h=2..H; test whether fewer BRC monomials can be traded against higher prefix cost and whether the EC49EJ cross-horizon weight-alias families permit nontrivial amortization. Keep global-across-all-h equality of p distinct from within-horizon equality.
