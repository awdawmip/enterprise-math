# PREFIX-512 — Exact W prefix on the native positive-b single-displacement fiber

Date: 2026-11-05 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Parent: exact BRC–KMP–first-source ranking of restricted signed five-axis paths inside native six-dimensional X6. Direct predecessor: PREFIX-511 (zero net displacement B/C W-prefix).

## Statement

Fix any integer m>=0 and an ordered native signed-step word on a/A,b/B,c/C,d/D,e/E with n=2m+1 and final signed displacement y=(0,+1,0,0,0). Its paired cancellation occupations p_i>=0 sum to m; there is one extra positive b. Preserve BRC observations V=p_b+2p_d+p_e, W=p_c+p_e, gate g in {aab,aba}, terminal KMP prefix q in {0,1,2,3}, and the first b/B versus c/C source tag t in {B,C}. There is no N-tag on this fiber.

For nonnegative integers A,C define the threshold-region prefix P(A,C;j) counting distinct integer observation pairs (W,V) with W<j realizable with p_a>=A and p_c>=C. Its exact support and prefix are:

    C<=W<=m-A, 0<=V<=2m-W-2A-C;
    J=max(0,min(j,m-A+1)-C);
    P(A,C;j)=J*(2m-2A-C+1)-J*(2C+J-1)/2.

Every V between the stated endpoints is realizable. Invalid rows are empty.

Define corrected R(A;j) for a first-B source when a positive b is required in the terminal gate suffix. Let h=m-A. When h<0, R is empty. When h>=0 its exact row support is

    W=0:         V=0,...,2h
    1<=W<h:      V=1,...,2h-W
    W=h>=1:      V=h
    other W:     empty.

With J0=max(0,min(j,h+1)):

    R(A;j)=P(A,0;j)-max(0,min(J0,h)-1)-h*[J0>h and h>=1].

For h=0, the prefix is 1 when j>=1, otherwise 0. Define Phi(k)=(k+1)(3k+2)/2 for k>=0, and 0 for k<0. The full R contribution is 0 if h<0, 1 if h=0, and Phi(h)-2h+1 if h>=1.

Exactly the following pair-support functions apply at each distinct (q,t), in order q=0,1,2,3:

    g=aab, t=B: P(0,0), P(1,0), P(2,0), R(2)
    g=aab, t=C: P(0,1), P(1,1), P(2,1), P(2,1)
    g=aba, t=B: P(0,0), P(1,0), R(1),   R(2)
    g=aba, t=C: P(0,1), P(1,1), P(1,1), P(2,1).

Here P(A,C) abbreviates P(A,C;j), R(A) abbreviates R(A;j). Counting the eight controller states separately gives an **O(1)-integer-operation exact W prefix** of the full B/C observer for every m,j, without a W-prefix index. Full state counts are

    S_aab(m) = Phi(m)+2Phi(m-1)+2Phi(m-2)+2Phi(m-3)+R(2;infinity),
    S_aba(m) = Phi(m)+2Phi(m-1)+2Phi(m-2)+Phi(m-3)+R(1;infinity)+R(2;infinity).

All arithmetic is exact integer arithmetic on BRC cancellation observations; bit complexity depends on operand length.

## Constructive proof

**Occupancies.** The surplus positive b contributes one native step but zero paired cancellation. For a fixed W choose p_e=0,...,W-C; then p_c=W-p_e>=C. With p_a=A, nonnegative p_b,p_d consume at most L=m-W-A, and p_b+2p_d attains every integer 0,...,2L (for an integer z choose p_d=floor(z/2) and p_b=z-2p_d). Translating these intervals by p_e yields the contiguous V interval displayed above. Summing row lengths over C<=W<min(j,m-A+1) proves P.

**KMP thresholds.** For q=1, a terminal positive a exists exactly when p_a>=1, and there is a negative A to separate any competing 'aa' suffix. For gate aab, q=2 requires two positive a, so p_a>=2; for gate aba, q=2 requires terminal ab, so p_a>=1 because the surplus positive b is always available. Either q=3 requires p_a>=2 and a terminal positive b. The q=0 controller is reachable with the appropriate first source; for B, the sole positive b word at m=0 has q=0, and at m>0 a non-prefix ending can be arranged; for C, a native c/C ending is available whenever p_c>=1. Tag C requires p_c>=1 and is realized by placing a c/C step before the required gate suffix.

**First-source ordering obstruction.** The terminal positive b of the aab q=3, aba q=2 and aba q=3 suffix may be the *only* native b/B step when p_b=0. If p_c>=1, some c/C primitive necessarily precedes that terminal b, so the first source is C, not B. For B as first source and a b-terminal suffix, either (i) p_b>=1, permitting a negative B to occur before every c/C step and retaining a positive b for the suffix, or (ii) p_b=p_c=0, so the terminal positive b is itself the first source. These alternatives are sufficient by placing all remaining steps before the terminal gate suffix; they are necessary from the first-source definition. A B-tag with terminal 'aa' (aab q=2) has no such obstruction. This proves the state-specific P versus R classification.

**Corrected row union.** For p_b>=1 and p_a>=A, the occupancy argument gives V in [1,2h-W-1] when 0<=W<h. For p_b=p_c=0, p_e=W and p_d ranges 0,...,h-W, giving V=W,W+2,...,2h-W. Their union is exactly the R support above. Compared with P(A,0), the missing V count per row is zero at W=0, one for 1<=W<h, and h at W=h>=1; summing these corrections proves R. Summing the disjoint controller labels (q,t) establishes the full-prefix and total formulas. QED for all m>=0.

An exact source-order witness: with m=2, p_a=1,p_b=0,p_c=1,p_d=p_e=0 and terminal gate aba suffix 'ab', the only native b is terminal, so a preceding c/C forces first source C. The occupancy thresholds alone would incorrectly assign q=2,t=B; R removes it.

## Executed validation

Two independently written executables, Python 3 and Node.js, iterated the ten original signed directions and updated native signed displacement, cancellation contributions V,W, KMP q, and the first source t, without using the proposed P/R formula to generate native states. Both fully checked both gates at odd n=1,3,5,7,9 (m=0..4), all 30 W rows, 459 joint states, and 70 W-prefix comparisons; separate analytic checks verified m=0..60 (4270 cases). Both returned ALL_CHECKS_PASS. Exact distinct-state totals by increasing odd n: aab = (1,7,25,62,122), aba = (1,8,29,70,134). The complete Node.js checker and its JSON output accompany this note in the same commit. These computations check the implementation; arbitrary-m validity rests on the constructive proof above.

## Next

PREFIX-513: settle y=(0,-1,0,0,0), where the surplus native negative B step cannot serve as the terminal KMP positive-b symbol. Then examine positive/negative c displacement and seek a four-sign uniform formula for |y_b|+|y_c|=1. Keep the original signed-source observer and primitive-append operation.

Source references: PREFIX-511 at 17743374c5ca4f21d0929ce642cbe97d5869e426; PREFIX-508/509/510; the frozen task source pin and current P000/ACTIVE world and research protocols. This is an independently published author-side result, not a formal CLAIM or review.
