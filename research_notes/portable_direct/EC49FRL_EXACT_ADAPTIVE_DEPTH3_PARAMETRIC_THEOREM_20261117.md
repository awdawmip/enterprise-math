# EC49FRL — Exact three-step native BRC identification and parametric terminal-count optimum

**Author research note, 2026-11-17.** Scientific predecessor: EC49FRK / PR #2627 / immutable commit 9ff13722b0ce429897fd542499bf597c825e139e. Frozen source pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Verification: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This is independent portable research, not an operational Result, CLAIM, Review or change to P000.

## Frozen universe and observer semantics

The static class-16943 universe comprises 310 original configurations with exact positive integer multiplicities, represented by 141 **full named** native-response profiles i. The **original** 228 physical observations have response V(q,i): 144 terminal IDs q=0,...,143 and 84 root IDs q=144,...,227. An adaptive exact-identifier queries physical IDs conditioned on previous response values, and must output each original named profile correctly. Compression in this note applies only to this explicitly declared finite static-observation horizon; it does not erase original X6 identity, joint-relation provenance, source ports or unspecified future operations.

Let m_i be the original multiplicity, with sum m_i=310. Define U_T, U_R as total terminal/root path queries over all 141 named profiles and M_T, M_R by weighting their paths with m_i. For a mixture prior p_i(lambda)=(1-lambda)/141+lambda m_i/310, and price ratio x=r/t, the exact expected total cost divided by t is

C(Q;x,lambda)/t = (1-lambda)(U_T+x U_R)/141 + lambda (M_T+x M_R)/310.

The 144-terminal response signatures have exactly 139 equivalence classes: 137 singletons and pairs P={8,139}, Q={46,140}; all four paired profiles have multiplicity one. They are separated by physical root observations 148,...,163. Consequently every exact tree has U_R>=4 and M_R>=4. Simultaneous equality forces root queries to occur once on each of the four forced profiles and on no others.

## Theorem A — minimum four physical queries for a fixed nonadaptive mixed palette

The exact minimum cardinality of a **fixed mixed** original-observation palette that identifies all 141 named profiles is **four**, attained by

J1 = {34,36,66,148}, with three terminal and one root IDs.

Another four-query witness is J2 = {117,132,153,161}, with two terminals and two roots. On the 9,870 distinct named-state pairs, each original physical query is represented by the exact set of pairs it separates. Exhaustive union of all C(228,3)=1,949,476 triples separates at most 9,866 of the 9,870 pairs, hence three never suffice. Checking all C(84,3)*144=13,720,896 three-root/one-terminal palettes and all C(84,4)=1,929,501 four-root palettes finds none identifying every profile. Zero roots cannot separate P or Q. Thus the only viable price classes for a four-element nonadaptive exact-identification palette are 1R+3T and 2R+2T.

For terminal price t>0 and root price xt with x>=1, the minimum **fixed nonadaptive palette cost** is exactly (3+x)t. Every exact palette needs at least four physical queries and at least one root, giving the lower bound, and J1 attains it. Among exactly four-query palettes with 0<x<=1, J2 minimizes cost, equal to (2+2x)t. This is a nonadaptive query-menu price result, distinct from adaptive expected cost.

## Theorem B — three is the exact minimum adaptive worst-case depth

For each of the 228 possible first physical queries, enumerate the non-singleton response cells. In every case at least one such cell cannot be separated into distinct singletons by any of the 228 possible second physical queries. The certificate stores one explicit bad cell for each first query. This proves impossibility of adaptive worst-case depth <=2.

The native decision trees A and B recorded in the exact certificate identify each of the 141 named states correctly, with worst-case depth **three** and U_R=M_R=4. Hence three is optimal even under the sharp root-mass constraint. All queries remain original physical IDs.

## Theorem C — full continuum prior frontier at minimum root mass and depth <=3

Consider the precise optimization class of native exact-identification trees with worst-case depth at most three and U_R=M_R=4. Define the minimum expected terminal-query count

F(lambda) = min_Q [(1-lambda) U_T(Q)/141 + lambda M_T(Q)/310], 0<=lambda<=1.

The **exact** value for every real lambda in this interval is

F(lambda) = min { (1-lambda)*296/141 + lambda*707/310, (1-lambda)*298/141 + lambda*688/310 }.

Put beta=620/3299. A tree A, beginning at terminal physical ID 140, has (U_T,M_T,U_R,M_R)=(296,707,4,4) and is optimal for 0<=lambda<=beta. Tree B, beginning at terminal physical ID 16, has (298,688,4,4) and is optimal for beta<=lambda<=1. At beta both tie. Both original-response trees are in the companion machine certificate and replay on every named profile.

**Load-bearing finite Bellman argument.** Under sharp root mass four, any root-query node can contain only one whole terminally indistinguishable pair P, one whole pair Q, or their union P∪Q. A root query on any other profile would exceed the lower bound, since every one of P∪Q must already incur a root query. At each other non-singleton state subset only terminal queries are eligible. Root queries that split each complete pair are exactly the native IDs 148,...,163. For a remaining subset S, weight vector w>0, and remaining depth d, define

f_w({i},d)=0, and f_w(S,0)=+infinity when |S|>1;

f_w(S,d)=min over eligible original splitting q of [1_(q terminal)*sum_{i in S}w_i + sum_{response cells S_a} f_w(S_a,d-1)].

Induction in d proves this dynamic program is exact for **all** trees within the stated root-floor and depth constraints. In particular, the first query must be one of 144 original terminals. Exhausting them and all their exact native response cells gives three endpoint checks:

* At lambda=0, minimum U_T=296, attained by A.
* At beta=620/3299, minimum [310*(3299-620)*U_T+141*620*M_T] = 307630980, attained by both A and B.
* At lambda=1, minimum M_T=688, attained by B.

The two candidate lines cross because 2(1-beta)/141=19 beta/310, giving beta=620/3299 exactly. For any competing fixed tree its cost difference from A or B is affine in lambda. The endpoint lower bounds imply A optimal on the whole real interval [0,beta] and B on [beta,1]. No discretization of priors is used in this continuum conclusion.

Including the identical sharp root contribution, the exact minimum normalized **total** expected cost in this constrained tree class, for all x>=0 and lambda in [0,1], is

C_floor3(x,lambda)/t = F(lambda) + x*[4(1-lambda)/141 + 4 lambda/310].

This provides an achievable upper bound on the unrestricted native Bellman value. It does not change the existing unrestricted five-tree theorem or assert that a root-floor tree is always unrestricted-optimal at every price.

## Exact finite evidence and independent validation

The new executed primary checker enumerated 1,949,476 mixed triples, 13,720,896 three-root/four-query palettes, 1,929,501 four-root palettes, and 228 adaptive two-query obstructions. It solved the exact root-floor depth-three weighted dynamic program at uniform, beta and multiplicity endpoints; its A/B trees were replayed on all 141 named profiles. An independent **bit-mask state-space dynamic program**, with a different subset representation, reproduced terminal minima 296 and 688. No floating-point comparisons enter the proof.

Primary certificate SHA256: 5584f8d07ce3a4c39533d6dba5eb61dbc84cd5ca98ee77ee9ee958e040b088f7. The complete portable archive includes the full JSON certificate (with 228 obstruction witnesses and two complete trees), both executed verifiers, frozen input files, logs, and a manifest.

Frozen original master: SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e. Original named-profile cost CSV: SHA256 a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. The inherited full-named native table is reconstructed through EC49FQI_NATIVE_DATA.py from these frozen originals; no scientific pin changed.

**Next research unit:** compare A and B with previously published unrestricted high-price candidate trees D and E by complete native query/path signatures. Determine whether the exact unrestricted price/mixture optimum can always be achieved with worst-case depth three, and classify the Pareto frontier of depth and expected root mass outside the sharp-root-floor slice. Preserve the full named observation interface and retain P000/ACTIVE world premises.

**Source/control:** the current native continuation read for topic RS-EC49AS returned FAILED / CANONICAL_REJECTED: unknown current immutable task publication. This note is independent portable science and makes no new current CLAIM, Result or Review assertion.