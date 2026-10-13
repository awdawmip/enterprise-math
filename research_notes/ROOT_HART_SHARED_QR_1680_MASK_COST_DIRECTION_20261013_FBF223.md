# Exact joint QR masks for the normalized 4kN Hart stream

Status: bounded algebraic direction / AUTHOR_REPORTED / no Native mathematical acceptance.
Driver and contributor: EM-DVR-FBF223; DA-A1DB35C00ED2F8C2A9FA; session MCP-cd5eefdde49843898b2a70c1af94d8dd.
Original Task: RS-SEMIPRIME-RESIDUAL-PRIORITY-HART-STREAMING-COST-AUDIT; publication TP2-7BCC256B5EA65F8D5085.
Original scientist EM-SEMIPRIME-1F8B9B, session MCP-0fc54865588849c28aa0a02ddb117f10, retains the claim/run. This note creates no Task, role, branch, claim, result or review.
Basis: HEARTBEAT_WORLD_NATIVE_X6. The calculation is an explicitly external integer/cost model; no Foundation, Working Truth, native propagation/readout bridge or ontology completion is claimed. Static algebra needs no additional time dimension; transport checkpoints retain their timestamps.
Exposure: directed, NONBLIND, contributing Root, not independent decisive review; prior-art/novelty UNKNOWN.

## 1. Exact scope

Let N be a positive odd integer, D=4N, a_k=ceil(sqrt(Dk)), and e_k=a_k^2-Dk. The public primary domain is 1<=k<=K=ceil(N^(1/3)), and the ordered priority stream uses the previously fixed (bucket,k) order. For any integer a define

P_N(a,k) = [a^2-4Nk is a square residue modulo each of 64,3,5,7].

This is only a necessary condition for an exact square, including zero. A failed predicate safely excludes exact-square/gcd success; a passed predicate does not certify a factor or exact square. We investigate a declared changed API in which paid certificates may omit proved nonproductive positions while preserving the relative order of possible successes. The earlier fixed unbatched complete-prefix fee lemma does not silently extend to this changed API.

No old numerical corpus, timing, root/solver/checker run or heldout result is used or repeated. All claims below follow by elementary modular algebra and CRT. Counts are counts of a FIXED-a residue mask, not measured selectivity along the dependent sequence (a_k,k).

## 2. QR64 reduction

The odd square residues modulo64 are exactly the eight residues congruent to1 modulo8. Necessity follows from the square of an odd integer. Sufficiency follows, for example, by taking odd representatives1,3,5,7,9,11,13,15: their squares cover1,9,17,25,33,41,49,57 modulo64.

If a is odd, a^2=1 modulo8 and N is odd, so

P_64(a,k) iff 1-4Nk=1 (mod8) iff k is even.

If a=2b is even, then e=4(b^2-Nk). A residue4z is a square modulo64 if and only if z is a square modulo16: any square representing4z must have an even root, whose half is the corresponding root modulo16, and conversely. Thus

P_64(2b,k) iff b^2-Nk modulo16 belongs to Q16={0,1,4,9}.

The value b^2 modulo16 depends on b modulo8, equivalently a modulo16, and lies in Q16. Consequently the QR64 predicate has period16 in a and in k, even though computing the full residual modulo64 might use a larger representative.

## 3. Joint periods

For m=3,5,7, a^2-4Nk modulo m has period m independently in a and k. Therefore

M=lcm(16,3,5,7)=1680

is a period of P_N in each independent argument: P_N(a+M,k)=P_N(a,k+M)=P_N(a,k). This is a valid period, not a claimed minimal period for every N.

The lower period is specific to the square-residue PREDICATE with D=4N; it does not replace the exact residual by a modulus, change a_k, or assert that the score/bucket/factor test is periodic. In particular, P_N(a_k,k) need not have k-period1680: a_{k+M} is a different integer and is not generally congruent to a_k moduloM. No independent-a mask density is transferred to the actual Hart prefix.

## 4. Exact fixed-row mask counts

Assume additionally gcd(N,105)=1. N is then invertible modulo16 and 4N is invertible modulo3,5,7. For each fixed a:

- Odd a: eight acceptable k residues modulo16, namely the even ones.
- Even a: four acceptable k residues modulo16, because multiplication by N is a bijection and Q16 has four residues.
- For m=3,5,7, the accepted k residues are (4N)^(-1)(a^2-Q_m), with cardinalities2,3,4 respectively. The Q_m include zero.

CRT gives exactly8*2*3*4=192 acceptable residues modulo1680 for odd a and4*2*3*4=96 for even a. The densities for that fixed-a mask are respectively4/35 and2/35. These equalities require the stated invertibility; for an N divisible by3,5 or7, the corresponding test behaves differently. Any public gcd/preprocessing shortcut is paid and shared with the baseline.

## 5. Exactly120 row masks under the invertibility condition

A mask depends on the five-valued QR64 row type: one type for odd a, and four types b^2 modulo16 in Q16 for even a. It also depends on a^2 modulo3,5,7, with2,3,4 possible square values. Hence at most5*2*3*4=120 masks occur.

They all occur, because the required a residue modulo16 and each square value modulo3,5,7 can be realized independently by CRT. They are distinct. Odd-a QR64 masks have eight positions modulo16; even masks have four. For even a, before multiplying by N^(-1), the four sets c-Q16 are

- c=0: {0,15,12,7};
- c=1: {1,0,13,8};
- c=4: {4,3,0,11};
- c=9: {9,8,5,0}.

These are distinct, and multiplication by N^(-1) preserves distinctness. For an odd prime m in{3,5,7}, distinct translates of Q_m are distinct: a nonzero translation stabilizing a nonempty proper subset of Z/mZ would, by cycling through the whole group, force that subset to be the whole group. Nonzero scaling is a bijection. Finally, a nonempty CRT product determines each factor by projection, so distinct row types give distinct joint masks. There are exactly120.

## 6. Storage and construction, with explicit costs

A full matrix indexed by a modM and k modM uses1680^2=2822400 bits, or352800 bytes before metadata/alignment. The deduplicated120 masks use120*1680=201600 bits, or25200 bytes. With independent rows of64-bit words, each row needs ceil(1680/64)=27 words=216 bytes, so the deduplicated payload is25920 bytes and the undeduplicated row-aligned payload is362880 bytes. A partially used final word must be masked when interpreted as a finite interval.

These figures are payloads, not total memory. Charge row-type indexing or residue arithmetic, descriptors, allocation, alignment, temporary storage, initialization, cache effects and any persisted/precompiled table under the declared accounting. Type computation for a_k cannot be free just because its output is small. Reducing N and a_k to small moduli still reads the required input operands under the declared bit/word model.

One explicit construction computes every cell of120 rows at1680 coordinates:201600 tiny-modulus predicate evaluations, plus initialization and writes. A sparser alternative enumerates accepted CRT tuples for each row. There are24 odd-row masks with192 accepted positions each and96 even-row masks with96 each, for a total13824 accepted coordinates. Initialize3240 row-aligned64-bit words, then compute the CRT coordinate and set its bit for each tuple. All inverses, residue-list construction, CRT products/additions/reductions, bit updates and loop/control operations are charged. The sparse construction is an algorithmic upper bound, not a claim that initialization, a CRT tuple or a bit write has zero cost.

Both constructions use only public N and the declared moduli. They do not use p,q or an uncharged success oracle. Cross-input caching must declare its validity key (the relevant N residues), storage, build amortization and misses; it cannot turn construction into an invisible free preparation cost.

## 7. Safe omission and order preservation

Suppose a correct paid generator produces candidate positions in the stipulated (bucket,k) order. For each candidate, a paid lookup or certificate proves P_N(a_k,k) false, or retains it. Any discarded candidate cannot have e_k equal to an integer square, since an integer square is a square residue modulo every modulus. Therefore the retained subsequence contains every possible exact-square/gcd success in its original relative order. Exact square and proper-gcd tests on the retained subsequence return the same first success as the full scalar consumer, provided all consumer effects relevant to success are the declared deterministic arithmetic tests.

This does not permit hiding non-arithmetic side effects or changing the completeness/coverage meaning of a result. A no-hit conclusion still needs coverage of every candidate either by a valid rejection certificate or by the retained tests, and failures/time/memory censoring retain their truthful statuses. A bit mask or a rejection table does not certify that arbitrary unknown a_k values belong to the indexed row.

## 8. Singleton-shell obstruction remains

For the primary K<=N domain, a_k<=2N, and the untruncated integer shell for a has width (2a-1)/(4N)<1. It thus contains at most one integer k; intersecting with1<=k<=K cannot add positions. A constant-exact-a shell cannot batch many primary candidates. Enumerating every integer a between the two endpoints reintroduces the already proved expensive inverse-row scan; the120-mask table does not remove that cost.

Different a values can share a modular row type, so masks may be reused AFTER those types have been established. That is ordinary shared predicate work. A genuine interval/bitset certificate skipping many k must also derive and pay for all necessary a_k type/boundary information without silently doing and hiding a full root or row scan. This note neither proves such a range construction impossible nor supplies it for free.

## 9. Consequence for research direction

The row masks give an exact algebraic ingredient for a paid shared/range-certificate scheme, with explicit table-construction/storage bounds. They are not the smallest representation for ordinary per-candidate filtering when the exact residual has already been computed; see Section10. The earlier scalar-consumer fee regions do not automatically apply to a genuinely changed implementation/API. Nor do the fixed-a densities establish a speedup on a correlated ordered Hart prefix.

If all candidate a_k/score/bucket work is still produced by the previously stipulated k-prefix scan, the prior no-fixed-power-gain bound remains about that producer class; constant small-modulus sharing alone does not erase the paid prefix requirement. Finite constant-factor improvements require a complete declared cost comparison, with table build and actual prefix behavior included.

The useful open unit is a genuinely paid range/bitset rejection mechanism and a proof of exact coverage/order and total cost. A bounded feasibility/no-go result is acceptable. Do not rerun old sample winners, retune the opened holdout, or mark the full seven-bit/ratio/population classification complete. The Task and mathematical mother stay OPEN, with the original owner retained.

## 10. Smaller universal lookup for an already computed residual

For an already computed e, the four necessary-condition predicates are exactly membership in Q_6720, the square residues modulo6720=lcm(64,3,5,7). The moduli are pairwise coprime, and CRT combines roots modulo them, so the universal set has12*2*3*4=288 residues. An uncompressed bit mask uses6720 bits=840 bytes=105 words of64 bits, independent of N. One explicit sparse construction enumerates288 CRT residue tuples, charges their CRT arithmetic and bit updates, and initializes105 words. Reading an embedded universal constant still pays preparation/load/storage under the chosen model; precompilation is not a free mathematical cost exemption.

For D=4N, only e=0 or1 modulo4 can occur. Write z=floor(e/4). Two smaller universal masks suffice:

- For e=4z, require z square modulo16,3,5,7. This has96 acceptable z residues modulo1680.
- For e=4z+1, require z even and4z+1 square modulo3,5,7. It has period210=lcm(2,3,5,7) and24 acceptable z residues per period. Equivalently it has192 acceptable residues if redundantly stored over1680.

The two rows use1680+210=1890 payload bits, requiring210+27=237 bytes when separately byte-packed, or(27+4)*8=248 bytes when separately aligned to64-bit words. A sparse construction initializes31 aligned words and charges96+24=120 accepted CRT coordinate writes plus all CRT arithmetic. They do not need per-N row construction or a modulo1680 a-row lookup. Their bitmap index still needs a paid reduction of z modulo the selected period, a paid choice of mask, and a paid bit load/test; obtaining exact e and z is not free. A redundant1680-bit representation of each row remains correct but uses420 payload bytes/432 word-aligned bytes.

Thus an ordinary consumer should compare the much simpler universal residual lookup before considering120 N-dependent a-row masks. The latter are relevant only if a proposed generator/certificate actually exploits the (a,k) structure to avoid otherwise necessary work. The universal lookup applies equally to the matched Hart/Fermat baseline. Any comparison must give the baseline the same permitted sieve implementation/preparation and charge failures, rather than treating a generic sieve optimization as a residual-priority advantage. No speedup is inferred without a complete cost comparison on the declared API.

## Durable dependencies

- Generator-independent conditional fee unit Source7f86ff058f45299b6fe4c67cdbab928206254b68, original scientist checkpoint028, release=false; full3 Source/5 originals independently coldverified.
- Controlled heldout Source07b8b0b877f9a8783fe82b40e3a0a715b86b0c60.
- Paid k-prefix producer bound Source6919a02ce0c010b0979ae81f8c779b074dae622f; Root contribution f3442022424e4cb50494f80d22c85350c4e74a93616d1b44ce051dc7d20db665.
- Literal inverse a-row bound Source077ab35ec10193646da08bf4fec7771e582eb46d.

This note is a new proof derivation, not a rerun of those artifacts and not a native Driver acceptance.
