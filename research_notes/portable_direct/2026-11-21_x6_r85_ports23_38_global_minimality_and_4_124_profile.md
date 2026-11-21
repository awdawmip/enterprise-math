# X6 R85 — 23–38 Port 的全整数域最小六元核，及 4–124 Port 的最小基数相图

Date: 2026-11-21 (Asia/Shanghai).
Scientific status: EXACT_FINITE_GLOBAL_UNIQUENESS_CERTIFICATE + PREDECESSOR_SYMBOLIC_SUFFICIENCY / AUTHOR_CHECKED / NOT_INDEPENDENTLY_REVIEWED.
Frozen P000: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.

## 1. Question and exact statement

R82 established six-vector sufficiency for each arbitrary positive real four-channel weight vector in the conditional degree-four BRC histogram model for Port ranges 23–26 and 27–38. It proved indispensability within the listed cores, leaving a precise stronger question: could a different feasible integer direction replace a listed core member, permitting a global uniformly sufficient family of fewer than six directions?

This note answers that question.

Let q(a), v(a), six pairwise gaps g_ij(a), F(a;w) and eta*(p,w) have exactly the definitions and quantifier order of R82/R84: nonzero a in Z^3, q(a)<=p, arbitrary w=(A,B,C,D)>0 and one unknown common additive offset. Two directions a and -a are identified.

**Theorem R85.** For every integer p with 23<=p<=38, the **minimum cardinality among all fixed feasible integer-difference direction families** that compute eta*(p,w) exactly for every positive real w is

\[
\boxed{N(p)=6.}
\]

For 23<=p<=26 the sharp family is

S22 = {(3,-4,1),(6,-4,1),(9,-5,1),(10,-5,1),(15,-6,1),(21,-7,1)}.

For 27<=p<=38 it is

S27 = {(3,-4,1),(6,-4,1),(9,-5,1),(10,-5,1),(15,-6,1),(24,-14,3)}.

**Corollary (R84 + R80–R83 + R85, at their declared observer scope).** The exact minimum cardinality profile for EVERY integer 4<=p<=124 is:

| p | Globally minimum number N(p) |
|---|---:|
| 4 | 5 |
| 5 | 7 |
| 6 | 9 |
| 7–8 | 10 |
| 9 | 11 |
| 10 | 12 |
| 11–15 | 5 |
| 16–42 | 6 |
| 43–48 | 7 |
| 49–124 | 8 |

Core membership may change while N(p) stays constant, including the 22-Port, 27-Port and 39-Port exchanges. This is a mathematical synthesis of the exact published author-side certificates of R80–R84, not a claim of an independent review of every predecessor.

## 2. New proof of global irreplacability

R82's established pointwise gap-domination plus the exceptional-vector symbolic lemma proves, for every positive real w, that its six members achieve eta*(p,w) for all Port counts in each interval. To establish *absolute minimum size*, it is enough to show every member separately attains a **unique global unoriented minimum** for some positive integer w, against the entire integer difference lattice q(a)<=p.

At the endpoints p=26 and p=38 we exhaustively check every integer triple in [-p,p]^3, subject to q(a)<=p, and retain one sign representative. These finite domains contain exactly 31,031 and 95,133 nonzero unoriented directions. For each of the six core members we calculate the exact objective with BigInt cross-product arithmetic and assert exactly one equal minimizer and zero strictly better competitors. The exact witnesses are:

| Member a | Weight profile w=(A,B,C,D) | Unique optimum F |
|---|---|---:|
| (3,-4,1) | (18,12,1,1) | 9/19 |
| (6,-4,1) | (1,1,1,24) | 12/25 |
| (9,-5,1) | (1,1,6,12) | 6/13 |
| (10,-5,1) | (1,1,1,1) | 1/2 |
| (15,-6,1) | **(7,1,1,15)** | **3/8** |
| (21,-7,1), only p=23–26 | (1,179,153,15) | 9/154 |
| (24,-14,3), only p=27–38 | (163,165,1809,388) | 3/986 |

The critical new witness is **(7,1,1,15)** for a=(15,-6,1). R82's previous candidate weight (1447,167,166,1850) also gave an optimum, but at both endpoints it tied with the distinct feasible direction (21,-10,2). The new weight removes this tie: the exact next-best distinct direction costs 9/22, strictly greater than 3/8. No alternate integer difference ties the new optimum.

The other five weight profiles for each endpoint are likewise checked over the complete integer domain; all have exactly one global unoriented minimizer.

Suppose a fixed candidate collection were sufficient for every w but omitted one s from the corresponding S22 or S27. At the strict-winner profile of s, the collection's optimum would be strictly greater than the true eta*, contradiction. Therefore every member is necessary; the R82 six-member sufficiency provides the matching upper bound, proving N(p)=6 at both endpoints.

For an intermediate integer p in the respective interval, every winning s remains feasible from the interval's first Port count onward; any competing integer direction available at intermediate p was already checked at the interval's upper endpoint. Its strict uniqueness is inherited. R82's sufficiency holds throughout the interval. Thus the same global minimum cardinality holds for **all** p=23–38, not only the endpoints. QED.

## 3. Saved exact audit and limits

Execute:
node research_notes/portable_direct/x6_r85_ports23_38_global_minimality_verify.js

This standalone JavaScript enumerates both complete finite integer domains, computes integer moment gaps, compares fractions with BigInt cross-products, and asserts six strict unique global winners at each endpoint. The matching persisted result certificate lists all optimal and next-best exact fractions:
research_notes/portable_direct/x6_r85_ports23_38_global_minimality_results.json.

Python Fraction independently evaluated the two complete domains and exposed the former tie at (1447,167,166,1850); the new improved witness was separately tested. The theorem's weighted sufficiency portion cites the R82 pointwise-coverage and exception proof, while this R85 independent finite test strengthens *minimality*. Neither the source P000 V5 nor the native X6 event/heartbeat reconstruction question was altered.

## 4. Next research

The entire finite-Port 4–124 minimum-cardinality question is now closed within the stated conditional BRC histogram model, subject to the declared author-side proof/certificate status. The principal numerical extension is the independent integer-cone verification of the R72 28-candidate coverage and R79 high-Port nine-core for all p>=125. The separate native transfer task is to preserve named Cell/Link/Port, branch history, whole triadic closure and time-evolution fibers, including future-operation invariance, rather than silently replacing native states by histograms.

Formal Source CLAIM/PROGRESS and historical Activity linkage remain separate from this portable scientific GitHub publication.
