# EC49EXE — Seven-window complete Pareto frontier and universal four-observer theorem

**Date:** 2026-11-03. **Classification:** AUTHOR_ANALYTIC_PROOF / EXACT_WITNESS_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. Parent: EC49EXD at e37684f32e337948071f0ee17c53ad78ecb59861; Draft PR #1730.

**Immutable science pins:** GLOBAL_KNOWLEDGE_V1@773d538180bfb49e24cffeb35c3ee75eb0628e2e; enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Current project and account behavioral rules were independently read at verified canonical main snapshots. Preserve P000/ACTIVE worldview and joint-observer path provenance.

## 1. Original finite symbolic model

Seven ordered operations on signed native spatial X6 steps:
- a=(-1,-1), b=(-2,-2)
- c=(+1,+2,-1,-2), d=(+2,+1,-2,-1)
- e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).

At each horizon h=2,...,H choose returning operation words of length h, all with signed native displacement (+2,0,0,0,0,0), and all with one identical *complete six-component positive primitive step count* p_h. Their nine-state seam-history to five terminal observation buckets (N,A,B,AB,BA) must have rank nine over Q. Preserve ordered primitive paths, branch provenance, full p_h and exact observer signatures separately. A full positive cache key p indexes the strictly-positive paired symbolic BRC factors (product of x_i^p_i, product of y_i^p_i). E counts distinct nonempty native ordered signed primitive prefixes, M counts globally distinct full keys p_h, S counts distinct nine-to-five transfer signatures. Optimize (E,M,S) under Pareto dominance.

The complete eight-word h2 return universe has a unique rank-nine positive-key fiber: ce,de,ec,ed, sharing p0=(3,1,1,0,0,0), with exactly 28 signed primitive prefix edges and exactly four essential signatures T4. For all proper T4 subsets of sizes k=1,2,3 the exact rational ranks equal respectively 3,5,7, while all four have rank 9. These facts were independently executed with rational Gaussian elimination and modular one-hot column elimination; the latter uses modulus 1,000,003 and the relevant 9x9 integer minors have absolute value at most 3^9, ensuring rank-nine equivalence.

## 2. Main new theorem EC49EXE-1

**For every integer H>=2 and every eligible family of returning words with global S<=4, E>=8H+12.** Sharp equality is achieved by the four words ce g^(h-2), de g^(h-2), ec g^(h-2), ed g^(h-2) at every horizon h=2,...,H, with exact resources

    (E,M,S)=(8H+12, H-1, 4).

**Proof of global lower bound.** Because the mandatory h2 core already uses all four T4 observer signatures, an S<=4 solution must have all four T4 transfer types at every subsequent horizon (fewer than four have rank at most seven). So at every h>=3 at least four distinct returning h-operation words share one positive cache key. The seven operation native step codewords are prefix-free: each has at least two primitive steps and the first two steps of different operations differ. Thus a completed h-operation word cannot be a prefix of a shorter complete operation word.

Fix two distinct h-operation words with equal full positive counts. If they differ before the last operation, their signed native paths diverge before the final operation and their last two primitive prefix edges are disjoint. If they share the first h-1 operations, equality of full positive counts forces their last operations into the same *positive-count class*. The only nonsingleton classes are {a,b} and {c,d}; within both classes, the *first signed primitive step* distinguishes the operation: -1/-2 respectively +1/+2. Hence their final two primitive edges are again distinct. Four compulsory words therefore contribute at least eight new signed primitive prefix edges at every h>=3, beyond any completed earlier horizon. The compulsory h2 core contributes 28. Hence E>=28+8(H-2)=8H+12.

**Sharp construction.** Appending g=(+2,-2) to the four h2 templates does not change native displacement or the four seam-history transfer signatures; it increases the complete positive key by one unit on native axis E2. Thus p_h=(3,h-1,1,0,0,0), all four signatures have rank nine, and every new horizon contributes *exactly* eight native prefix edges, with a distinct p_h. This reaches the bound for every integer H>=2. The theorem is proved structurally; executed finite witnesses for H2..H64 (Python) and H2..H40 (independent Node.js) corroborate the structure.

**Corollary (previously open):**

    min {E | H=7,M=6,S<=4} = 68, attained at (68,6,4).

The lower bound applies to every S<=4 H7 solution, regardless of M, and the construction has exactly M=6.

## 3. Complete H7 Pareto frontier EC49EXE-2

Combining EC49EXE-1 with immutable exact author-side predecessor proofs EC49ET/EC49EU/EC49EV/EC49EW/EC49EXC/EC49EXD/EC49EP/EC49EM gives the *complete* nondominated set:

    P7 = {(58,5,6), (68,6,4), (72,4,6), (80,5,4),
          (86,3,6), (92,4,4), (116,2,6), (116,3,4)}.

Exact lower/attained upper bounds by cache strata:
- M=2: S<=4 infeasible; S<=6 E=116 (EC49ET).
- M=3: S<=4 E=116 (EC49EU), S<=6 E=86 (EC49EV).
- M=4: S<=4 E=92 (EC49EW), S<=6 E=72 (EC49EXD).
- M=5: S<=4 E=80 (EC49EXC), S<=6 E=58 (EC49EP/EC49EM).
- M=6: S<=4 E=68 (new); S<=6 is dominated by M5/S6 E=58.

The completed per-fiber T4/T2 nine-rank classification in the predecessor research shows that nondominated solutions use S=4 or S=6; M=1 cannot cover h2..h7. All listed points have native returning-word constructions with certified lower bounds in the referenced predecessors, except the new (68,6,4), whose direct proof and witness are above. The eight triples are pairwise nondominating, independently checked by both programs. Formal mathematical admission and native Driver review remain separate.

## 4. H8 minimum cache count EC49EXE-3

For any returning operation word, let the operation multiplicities be a,b,c,d,e,f,g. Signed native return gives b=0, e=a+1. Put q=c+d and full positive key p=(u,v,w,0,0,0), where w=e>=1. Then:

    u=q+2w+f,  v=q+g,  h=u+v-q-1,
    0<=q<=min(u-2w,v).

Consequently a single p can support a horizon h only if

    max(u-1, v+2w-1) <= h <= u+v-1.

These integer inequalities are also sufficient for constructing nonnegative occurrence counts in this finite operation language. The compulsory h2 key (3,1,1) supports h2 and h3 only. If all H8 horizons used at most two keys, a second key would have to cover both h4 and h8. Supporting h4 implies u<=5 and v+2w<=5, so v<=3; then hmax<=u+v-1<=7, a contradiction. Thus M>=3 at H8.

The known H7 M2/S6 witness (EC49ET) extends to h8 with words fegfggff and geffgfgf (each h7 terminal word followed by neutral f); all h2..h8 rank checks and full-key equality pass. Its measured resources are exactly

    (E,M,S)=(120,3,6).

Hence the **minimum H8 BRC key count is exactly M=3**. The E=120 point is a verified *upper bound*, with exact minimal E at M=3/S<=6 remaining to be determined.

## 5. Executed evidence and reproduction

Python standard library checker VERIFY_EC49EXE.py and independently written V8/Node.js checker VERIFY_EC49EXE_INDEPENDENT.js were executed on 2026-11-03. Both PASS with (68,6,4) for H7, (120,3,6) for H8, compulsory base 28 edges, rank subsets 3,5,7,9, and pairwise H7 Pareto nondomination. Actual execution reports EC49EXE_EXECUTED.json and EC49EXE_INDEPENDENT_EXECUTED.json exist in the author-side complete evidence archive together with both exact source files and SHA256 manifest. Full archive digest:

    f493ef3940e88c5592d1f801f80ac5694bea111f68f6e53e7b7557794fd28542

VERIFY_EC49EXE_PORTABLE.js in this publication is a concise separately reproducible V8 reference checker. The symbolic all-H result relies on the stated structural argument, and the complete Pareto relies also on inherited exact finite certificates, not on checking a finite sample of H values.

## 6. Identity, permission, next problem

Actual GitHub identity: awdawmip; project GitHub permission: push/admin true. Native Enterprise Math gateway 0.6.11 reported research_authority_granted=false. Authenticated active Owner inventory returned CONTROL_QUOTA, thus active Owner is unconfirmed. No new native CLAIM, Research Result or independent Driver Review/admission asserted by this author-side GitHub publication.

Next EC49EXF: determine exact min E for H8,M=3,S<=6, from the certified M=3 lower bound and feasible E=120 upper bound. Use the horizon-support interval to classify eligible positive-key schedules, preserve full ordered signed X6 paths and rank-nine observer signatures, and extend earlier exact integer prefix-OR-mask DP. Secondary: complete H8 S<=4 resource strata, starting from the certified all-H minimum (76,7,4).