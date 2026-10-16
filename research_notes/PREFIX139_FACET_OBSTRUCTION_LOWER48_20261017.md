# PREFIX-139 — Facet obstruction for the four-coordinate two-sum basis (UNREVIEWED)

Status: AUXILIARY_EXACT_INTEGER_PROOF / LOCAL_DUAL_VERIFICATION_PASS / NOT_ADMITTED / FORMAL_CLAIM_NONE.
Date: 2026-10-17.
Global read pin: awdawmip/chatgpt-global-knowledge@c065a1c01dd3e854a3d1d7b0f14bb54fb7a39725; P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.
EM scientific Source read pin: awdawmip/enterprise-math@2a4da83cda3ef45333270a1c233c827b18f78e25.
Research continuation of unreviewed PREFIX-138. This is not a formal Task, Result, CLAIM, Driver review or native P000 claim.

Let Delta_n^d={x in Z_{>=0}^d:sum x_i=n} and beta_d(b)=min{|S|:S subset Delta_b^d and S+S=Delta_{2b}^d}, with unordered pairs allowed to use the same element.

THEOREM (locally proven): 48 <= beta_4(8) <= 61. The 61-profile covering witness and all 969 target decompositions are inherited without change from PREFIX-138. The previous lower bound was 45.

Lemma: beta_3(8)=21. A literal 21-vector basis covers all 153 targets; a complete unrestricted exact recursive search rejects every <=20 subset. The search starts with 9 forced profiles (pure vertices and seven-one profiles), branches on all unordered decompositions of an uncovered target, and prunes only when the remaining number of new unordered pairs, a*r+r*(r+1)/2, is smaller than the uncovered count, or a required pair exceeds the remaining state budget. Memoization is by the exact selected bitmask. The C++ implementation visits 3936 calls (3191 distinct bitmasks) for budget 20, finding no completion, while an independently written Python program confirms the same 3191 distinct bitmasks. Both find a completion at budget 21. Detailed source and witness are in the local handoff package. This facet lemma is a finite computer-assisted proof.

Proof of the 48 lower bound: A complete S subset Delta_8^4, size k, restricts on each coordinate-zero facet to a Delta_8^3 two-sum basis, so each facet population n_i>=21. The six edges each contain 2 pure vertices and e_ij interior selected profiles, with 4<=e_ij<=7: the edge target has 17 possible sums and any <=5 edge profiles yield at most 15 unordered sums. With E=sum e_ij, counting face incidences gives sum_i n_i >= 12+2E.

Let P_4(S) be the number of unordered pairs in S (repetition allowed) whose sum has all four coordinates positive. Inclusion-exclusion over pairs supported on the zero-coordinate faces yields the exact equality
P_4(S)=C(k+1,2)-sum_i C(n_i+1,2)+sum_{i<j} C(e_ij+3,2)-4.
For e in {4,5,6,7}, C(e+3,2)<=8e-11. For n>=21, C(n+1,2)-231>=4(n-21). Therefore:
sum_edges C(e_ij+3,2)-sum_faces[C(n_i+1,2)-231]
<=8E-66-4 sum_i(n_i-21)
<=4(sum_i n_i-12)-66-4 sum_i(n_i-21)
=222.
It follows that P_4(S)<=C(k+1,2)-706. But the number of target vectors in Delta_16^4 with all coordinates positive is C(15,3)=455; all must be represented. Thus P_4(S)>=455. For k<=47 the upper bound is C(48,2)-706=422<455, contradiction. Hence k>=48.

This is a standalone exact finite additive-basis conclusion. Under the precise inherited PREFIX-133 auxiliary unit-edge positive BRC fixed-cut normalizer, its consequence is 48<=N_physical,cut<=61 and rank_N0(H)=4, so the cut cost minus rank is between 44 and 57. No unrestricted automaton minimization or native X6 Cell transfer is asserted. Actual proof scripts, 21-vector facet witness, the inherited 61-vector witness, 969 decompositions and checksum log are in the separately preserved local ZIP, pending remote Source bytes publication and independent Driver audit.

NEXT PREFIX-140: Prove >=16 unavoidable collisions among four-positive unordered pair sums for a hypothetical 48-state basis (or obtain a sharper support-four capacity), which would lift the lower bound to 49; independently continue searching for a verified <=60-profile witness. The existing 60-profile near miss lacks three specified targets and does not prove existence.

Control read: GitHub identity awdawmip; native task inventory CONTROL_QUOTA; native session_start STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Current live Owner and valid CLAIМ are not verified. This note, if committed, is an UNREVIEWED BRANCH artifact only and must not be treated as formal acceptance.
