# R61 — Persistent sparse-label timestamp–phase index and age-centered interval certificate

Date: 2026-11-11. Scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34` (unchanged S23/AV). Research frontier: R60 Draft PR #2054, commit `4ddb14f194fa4d301e7fdff1133f19787f6c764d`; R59 PR #2051. This is independent author derivation/finite exact verification, not a formal shared-task Result or an accepted Foundation theorem. Scope is the labelled circle-rotation auxiliary observer, preserving original historical labels and source timestamps. P000 is unchanged.

## Definitions

Let 0<theta<1 be irrational, m>=1, and A_z the counterclockwise half-open circular arc from the history boundary {z theta} to the next phase-ordered history boundary, with original label z in {0,...,m-1}. For any finite distinct source set S subset {t in Z:t<j}, integer observer time j and phase x in R/Z, define tau_z(j,x,S) as min{j-t:t in S, {x-(j-t)theta} in A_z}, or EMPTY.

## R61-A — Persistent sparse-label source tree

Fix any integer anchor a. Maintain an immutable height-balanced search tree ordered by ( {(t-a)theta},t ), holding individual source timestamps and a subtree maximum timestamp in each node. For any query (j,x), put u={x-(j-a)theta}. The identity

  {x-(j-t)theta}={u+(t-a)theta}

implies

  tau_z(j,x,S)=j-max{t in S:{(t-a)theta} in A_z-u}.

A translated arc is the union of at most two sorted ranges. A persistent AVL tree gives worst-case O(log(n+1)) **word operations and new immutable nodes** for one source insert/delete, and O(s log(n+1)+s) word operations for s requested original labels. It preserves old roots under arbitrary version forks. Build from unsorted n sources and m boundaries in O(n log(n+1)+m log(m+1)) word operations; retaining U mutations costs O(n+m+U log(n+U+1)) words for all roots plus tree nodes. The range-max query examines at most two boundary paths and O(log n) fully covered subtrees, using cached subtree maxima. At m=1 the unique arc covers the circle; empty S gives EMPTY. For rational phases with collisions, break ties by original timestamp to retain identities. Query j must satisfy max S<j. The tested implementation uses persistent AVL path copying and explicit original labels.

## R61-B — Absolute-time translation invariance

For every integer L,

  tau_z(j+L,x,S+L)=tau_z(j,x,S).

Proof: the ages j-t are unchanged, hence so are phases, original-label membership and minima. Consequently, when S={j-H,...,j-1}, anchoring at j represents source phase indices {-H,...,-1}, independent of |j|. An anchor shared among persistent versions remains fixed; rebuilding onto a different anchor has a real O(n log n) construction cost.

## R61-C — Exact rational-enclosure phase-order certificate

Let theta lie in [p/q,(p+1)/q] within (0,1). For a finite index set E containing 0, for every nonzero d in E-E put r_d=(dp) mod q, between 0 and q-1. If

  min(r_d,q-r_d)>|d|       (for all nonzero d in E-E),

then all indexed fractional phases {k theta} (k in E) have one common strictly ordered circular arrangement throughout the entire enclosure. Proof: changing theta from p/q by at most 1/q changes d theta by at most |d|/q, strictly smaller than its distance to the nearest integer at p/q. No phase differences cross an integer; zero is among the indices and anchors the seam.

For frozen m=128,H=225 choose E={0,...,127} union {-225,...,-1}. There are 353 indices and 704 distinct nonzero differences, |d|<=352. With p=262204504569236716045286 and q=10^24, direct exact integer certification gives

  min over d (min(r_d,q-r_d)-|d|) = 1538749354821431426740 > 0.

This certifies the 225-source history-boundary order for every theta in the frozen rational interval. A particular observation x also needs a check that the moving queried phase does not cross a boundary; a phase-order certificate alone is not an arbitrary-x membership certificate.

## R61-D — Exact counterexample for an unbounded relative age

Take q=10^24, p=262204504569236716045286, m=2, j=q, S={0}, x=0. Two parameters strictly inside the same interval are theta_1=(4p+1)/(4q) and theta_2=(4p+3)/(4q). For age q, the source phase {-q theta} equals 3/4 and 1/4 respectively. Since 1/4<theta_i<3/4, original label z=1 receives the source at theta_1, whereas z=0 receives it at theta_2. These strict inequalities also yield disjoint open irrational parameter subintervals with different answers. Thus the fixed 10^-24 enclosure cannot certify all arbitrary ages; age-centered bounded windows retain the exact R61-C certificate.

## Bit-cost and observer/BRC scope

Word-level AVL counts are distinct from bit-level arithmetic: forming one phase residue requires multiplication/modulus of integers sized by q and |t-a|, tree comparisons include phase precision and timestamp bit length, and observer cost includes input transformation, parameter isolation, boundary sorting, tree construction, per-version updates, output, and any certification. A persistent tree is promising when a few labels are queried across many versions with arbitrary deletions. R59 static RMQ, R58 grouped checkpoints, R56 split-block and R49 caching remain comparators under matched workloads.

Typed BRC reuse: `REUSE_APPLIED` — the carrier is a source-identified finite set with original-history labels and future deletion; a latest-only quotient loses provenance needed for arbitrary deletion. This is not a positive-weight branch histogram or a new native X6 law.

## Actual validation and next question

The complete locally executed Python exact-integer program is CHECK_R61.py in the run bundle. Its independently implemented scan oracle verified 225 small rational cases, 3,375 version roots, 3,150 updates (including forks), 6,300 current and 1,575 historical-root queries, 900 AVL structural checks; two S23 interval endpoints each with 21 version roots and 126 sparse 3-label queries; all 704 exact interval differences, two exact drift witnesses, and 99 huge common-time translations. See R61_CERTIFICATE.json and R61_LOG.txt. No floating-point arithmetic was used.

R62: prove and test exact online anchor rebasing (amortized full bit cost), compare matched persistent/static/step-batch workloads and establish an x-aware membership stability certificate. Active S23 shared Owner/CLAIM and independent mathematical review remain to be confirmed.
