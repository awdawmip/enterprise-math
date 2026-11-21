# R762HU — Port/sign BRC half-history Gram kernel and monotone return ratios

Status: AUTHOR_PROVED / FINITE_CHECKED / NOT_REVIEWED. Scope: six-axis composite Port candidate only, frozen scientific input awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Continues R762HT@59eb4d4f939976458b060919315ef7043641f7eb and its positive Port/sign coefficient operators. This is not the primitive TRIADIC_CLOSURE_E dynamics, an independent review, or a formal Task Result.

## Definition (full source, not histogram quotient)

Let P be the 15 unordered axis pairs from X={0,...,5}. A step p->q is legal when |p intersect q|=1, with support s=p union q and composite signed Cell increment +/-h_s, h_s=sum(i in s)e_i in Z^6. Distinguish every step's order, Port endpoints, support and independent sign. Fix root p. Let a_r(p,q;v) be the nonnegative integer count of r-step signed paths from p to q with aggregate displacement v. Let K_m(p) be the count of m-step signed paths from p back to p with zero displacement. For r=0, a_0(p,p;0)=K_0(p)=1. This is a formal composite support readout: do not identify +/-h_s with a primitive 3-force balance event.

## HU1 — exact all-length Gram identity

For each integer r>=0,

\[
\boxed{K_{2r}(p)=\sum_{q\in P}\sum_{v\in\mathbb Z^6}a_r(p,q;v)^2.}
\]

Proof: cut each rooted signed 2r-step zero-displacement loop after r events at q. Its first half has displacement v; its second half has displacement -v. Reverse the second half in time and flip every sign: because Port adjacency is symmetric and support h_{p union q} is unchanged under reversal, this is a bijection with an r-step p->q half-history with displacement +v. Thus the two independent halves give an ordered pair in the same fiber (q,v), counted by the square. Every pair glues uniquely. All coefficients are positive source counts; no signed mass cancellation occurs. QED.

For the finer source histogram n of length 2r, define a_r(p,q;alpha,v) counting half-histogram alpha (20 support types, individual event positions ordered). The same bijection gives the exact convolution

\[
\boxed{J_p(n)=\sum_{\alpha+\beta=n}\sum_{q,v}
 a_r(p,q;\alpha,v)\,a_r(p,q;\beta,v).}
\]

Here J_p(n) counts rooted signed zero-return histories with support histogram n but no preassigned distinct occurrence IDs. The labeled version from R762HT is D(n)J_p(n), D(n)=product_s n_s!. In particular J_p(2alpha)>=sum_{q,v}a_r(p,q;alpha,v)^2, so any nonempty half-histogram realization provides a certified joint-source return of the doubled histogram. The histogram formula is a count of all compatible pairings, not a claim that a support histogram preserves ordering for later time/rotation operations.

## HU2 — strict log-convexity and exact limiting ratio

The directed signed Port step operator A acts on functions over P x Z^6 by counting the 16 elementary choices (8 adjacent q and 2 signed support increments). Its matrix is symmetric: reversing a signed step requires reversing the sign, which is also an allowed source. For delta at (p,0), K_{2r}(p)=||A^r delta||_2^2. Cauchy-Schwarz gives, for every r>=1,

\[
\boxed{K_{2r}(p)^2\le K_{2r-2}(p)\,K_{2r+2}(p).}
\]

The inequality is strict: choose one axis in p and make r+1 positive steps while keeping that axis in every Port, which produces an r+1 step path whose corresponding coordinate equals r+1. No r-1 step path can reach that same displacement. Hence A^{r-1}delta and A^{r+1}delta cannot be scalar multiples, so equality in Cauchy-Schwarz is impossible.

Each r-step source has 16^r choices, hence sum_{q,v}a_r(p,q;v)=16^r. There are at most 15(2r+1)^6 endpoint/displacement fibers. Cauchy-Schwarz applied to these nonnegative coefficients yields

\[
\frac{256^r}{15(2r+1)^6}\le K_{2r}(p)\le256^r.
\]

Thus K_{2r}(p)^{1/r}->256. Since positive K_{2r} are strictly log-convex, the successive ratios are strictly increasing, and their logarithmic Cesaro means converge to log(256). Therefore

\[
\boxed{\frac{K_{2r+2}(p)}{K_{2r}(p)}\nearrow256.}
\]

All assertions hold uniformly for every root Port by S6 relabeling symmetry. The upper/lower estimates are deliberately not a local-limit constant or a claim that the root return probability is asymptotic to a particular multiple of r^{-3}.

## HU3 — exact finite signed-closure census

A C++17 nonnegative-integer BRC dynamic program stores (endpoint, six signed components) after r events and computes the Gram squares. Results for root 01:

| r | m=2r | K_m(01) | Nonzero half-history fibers |
|---:|---:|---:|---:|
| 1 | 2 | 16 | 16 |
| 2 | 4 | 624 | 193 |
| 3 | 6 | 34,688 | 1,980 |
| 4 | 8 | 2,413,424 | 15,909 |
| 5 | 10 | 200,986,368 | 92,556 |
| 6 | 12 | 19,705,107,552 | 376,057 |
| 7 | 14 | 2,247,068,158,176 | 1,106,472 |
| 8 | 16 | 293,078,340,240,624 | 2,627,121 |
| 9 | 18 | 42,792,652,096,466,432 | 5,486,228 |

Every r layer also passed total positive source count = 16^r. The r<=4 values were independently matched against direct full-length 2r-step displacement-zero transfer, and m=4 was also checked by independent exhaustive depth-first walk generation (16^4 signed paths). The r=5..9 numbers are exact integer outputs of the half-history Gram implementation, without an independent second implementation. The all-r claims HU1-HU2 are established by combinatorial/inequality proofs, not inferred from this finite table.

Local command: g++ -std=c++17 -O3 -Wall -Wextra R762HU_GRAM_CHECK.cpp -o r762hu && ./r762hu. The portable source file records every finite case and fails on verification mismatch. No overflow occurs in the stated r<=9 range: source multiplicities fit uint64_t; Gram accumulation uses unsigned 128-bit integer. The 6-bit-per-axis coordinate packing is safe because the added six-vector components stay within [-18,+18] in all r<=9 verification paths, with offset 24.

## Provenance, preservation and next question

Prior exact parent: R762HT, PR #2897, commit 59eb4d4f939976458b060919315ef7043641f7eb; earlier HK Port witness and HR/HS Port feasibility remain separately pinned. Scientific task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; task frozen P000@a72226e2430ffa4786321ac86e7f0c599d5f0389. Current control receipt r3-20261121-1420-x6-control-continuation-v1 returned SUCCEEDED with runtime actor/claim null and execution_authorized=false; therefore this note is an independent non-CLAIM portable contribution. Historical author/Activity provenance is not reassigned.

Next discriminate the open separation question N_p(n)>0, all six support totals even, but C(n)=0. The new fine-histogram Gram convolution permits candidate pruning and a sharp lower bound for doubled realizable half-histograms, without dropping ordering, branch or signed displacement data. Native force/time/rotation lifting remains an independent obligation.