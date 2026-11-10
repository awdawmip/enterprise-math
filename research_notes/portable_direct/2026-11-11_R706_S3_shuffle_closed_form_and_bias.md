# R706 — Exact S3 shuffle histogram: closed form and two BRC mixing regimes

Date: 2026-11-11 Asia/Shanghai. Author-side UNREVIEWED research. Mother task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Frozen scientific input pin preserved: a72226e2430ffa4786321ac86e7f0c599d5f0389.

## Source, carrier and observation

This directly extends R703, research branch commit 879ebaaf4fbaf926b509c31cb1d47322105f6216, PR #2028, with its pinned V29 additive PASS/TRANSFER ledger, V38 based X6 loop packets, and V39 operation-safe (j,h) observer. Let A=(0,2,1), B=(1,0,2) be V38's two distinct involutive S3 frame holonomies, so c=AB and c^-1=BA are distinct 3-cycles. A^-1 and B^-1 are distinct oriented packet labels with the same respective frame holonomies; their transfer chains reverse. The typed BRC carrier retains packet identities, orientations, temporal order and provenance before the count-level observation. Counting here is the exact integer enumeration of packet-type orderings, not a physical randomness model or a claim of phase/amplitude cancellation.

R703 established that every ordering of the oriented multiset (k A, k A^-1, l B, l B^-1) has the same V29 complete additive event ledger and net transfer current j=0 in the based-packet grammar. The final S3 holonomy h is a future-relevant residual under V39 appended-loop observations. We calculate its COMPLETE histogram for every nonnegative k,l, without a dynamic-programming recurrence or enumeration of the words.

## Theorem 1: exact closed-form holonomy counts

Define C(k,l)=binom(2k+2l,2k) and

D(k,l) = sum_(r=0)^min(k,l) (k+l)! / [(k-r)! (l-r)! (2r)!].

Let W_(2k,2l)(g) be the number of words with exactly 2k A letters and 2l B letters, whose ordered product in S3 is g. Then for all integers k,l>=0:

    W(e)         = [C(k,l)+2 D(k,l)]/3,
    W(c)         = [C(k,l)-D(k,l)]/3,
    W(c^-1)      = [C(k,l)-D(k,l)]/3,
    W(odd g)     = 0.

All displayed results are integers. In particular D(k,l)=W(e)-W(c)>0, and if k,l>0 all three even states occur. For the oriented packet multiset used in R703, the exact count for each g is H_(k,l)(g)=binom(2k,k)binom(2l,l) W_(2k,2l)(g).

### Proof

In the formal group algebra Q[S3][[x,y]], summing all words gives F(x,y)=(1-xA-yB)^(-1). Extracting the coefficient at identity via the regular representation decomposition of S3 gives

    [e]F = (1/6) * [ 1/(1-x-y) + 1/(1+x+y)
                      + 2 tr( (I-x rho(A)-y rho(B))^-1 ) ].

A rational two-dimensional standard S3 representation of any two distinct generating transpositions is given by rho(A)=[[-1,1],[0,1]], rho(B)=[[1,0],[1,-1]]. Both square to I and rho(A)rho(B)+rho(B)rho(A)=-I. Thus K=x rho(A)+y rho(B) obeys K^2=(x^2+y^2-xy)I and tr(K)=0. Hence tr((I-K)^-1)=2/(1-x^2-y^2+xy).

For monomial x^(2k)y^(2l), each one-dimensional representation contributes C(k,l). The coefficient in (1-x^2-y^2+xy)^-1 is precisely D(k,l): all terms have degree two, so the relevant power is k+l; the number of mixed xy factors is even (2r), leaving k-r factors x^2 and l-r factors y^2. Their multinomial coefficient is the r-th summand of D. Therefore the identity count is (2C+4D)/6=(C+2D)/3.

All words have even permutation parity. Word reversal is a bijection taking each product to its inverse because A^2=B^2=e; hence W(c)=W(c^-1). Their common count is (C-W(e))/2=(C-D)/3. Finally every coarse word has binom(2k,k) choices of which A-positions are oriented A versus A^-1 and independently binom(2l,l) choices for B, giving the oriented multiplicative factor. QED.

## Theorem 2: exact contrast, balanced mixing and sparse persistence

Take the *uniform combinatorial counting measure* on coarse words. Write delta=D/C and p_g=W(g)/C. Then p_e=(1+2delta)/3, p_c=p_c^-1=(1-delta)/3 and total-variation distance from the uniform distribution on {e,c,c^-1} is exactly TV=2delta/3.

**Balanced k=l=n>=1:** D(n,n) is a nonnegative coefficient of (x^2+y^2+xy)^(2n), so D(n,n)<=9^n. The central binomial C(n,n)=binom(4n,2n)>=16^n/(4n+1). Consequently

    0 < delta(n,n) <= (4n+1)(9/16)^n,
    TV <= (2/3)(4n+1)(9/16)^n -> 0.

This is a proved exponentially decaying upper bound for the holonomy histogram's combinatorial bias in the balanced packet family.

**Sparse k=1, l>=1:** D(1,l)=(l+1)(l+2)/2 and C(1,l)=(l+1)(2l+1). Hence

    p_e = (l+1)/(2l+1) -> 1/2,
    p_c = p_c^-1 = l/[2(2l+1)] -> 1/4.

The packet-type ratio, not the total number of packets alone, controls whether the observed holonomy histogram approaches uniformity. The worst-case 2-bit exact repair of R703 remains necessary for every positive k,l because all three states occur, despite these different weights.

## Validation

Python 3 standard library script R706_VERIFY.py independently constructs S3 multiplication by exact integer tuple composition, uses arbitrary-precision integer DP to count every product, and compares the factorial-sum closed form for all 625 pairs 0<=k,l<=24. It also verifies support, totals, and the positivity/boundary cases. Exact run verdict: R706_S3_SHUFFLE_CLOSED_FORM_PASS. Selected exact output and the declared coverage are in R706_RESULTS.json. k=l=1 recovers the R703 oriented histogram (16,4,4); k=l=2 gives C=70, D=19 and coarse (36,17,17).

## Next executable unit

Intersect the R703 based-packet shuffle language with actual intermediate-time native X6 Link/Port, V20/V36 triadic update and V39 composition rules. Track (native Cell/active-triad state, V29 additive ledger, S3 holonomy) in a product-state automaton and compare reachable-word counts against H_(k,l). The exact discrepancy then measures the scheduler restriction on temporal BRC holonomy. A packet-level algebraic result is preserved as such until its intermediate event admissibility has been checked. This author-side note has no formal native CLAIM, Result or independent review.
