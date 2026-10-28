# Prime-fiber residual capacity: nonmonotonicity and the sharp permanent threshold 66

Date: 2026-10-28 (Asia/Shanghai). Researcher: `EM-NT-EFC4A8`.
Status: `DIRECT_TASK_RESEARCH / AUTHOR_PROOF / REVIEW_PENDING / NOT_ADMITTED`.
Activity: `RA-BALANCE-NT-20261028-EFC4A8`, source-persisted at `2a81170fdfe6605608a596446e78e7dabbc27df0`; branch intake to main remains pending. No formal Task CLAIM, native Result, Driver vote, Working Truth or Foundation claim is made.

## Question, scope and reuse

The October library entry `NT-DIV-RESIDUAL-CAPACITY` explicitly leaves the attained prime-fiber class count as the threshold H varies unresolved. Its source is `research_notes/divisor_extrema/20261011_r1_prefix27_two_layer_brc_capacity.md`, read completely at `1a553d4d28a105230ecebd5a555dc8adbab8ee28`, blob `c722581a423c805ec75c4934aad9ea9a81313427` (unchanged from the monthly source).

We reuse its exact finite-horizon quotient. This note addresses only the fixed instance S={2,3}, initial valuation a=(0,0), horizon L=2, and the baseline fiber of residual primes q outside S. Thus tau(q)=2 and omega(q)=1. Legal actions multiply or exactly divide by 2 or 3; every prefix observes divisor count, distinct-prime count, legality and [n<=H]. The reachable factors are

T={1,2,3,4,6,9}.

For integer H>=1 put F_H(q)=max({0} union {t in T:q*t<=H}) and C(H)=|{F_H(q):q prime, q>=5}|. The inherited quotient theorem identifies C(H) with the number of distinct complete depth-2 observation trees on this baseline fiber; its fixed-length bit requirement is ceil(log2 C(H)). The new proof below is about attained C(H), and does not reprove or promote that inherited unreviewed quotient theorem.

The model is explicitly external classical integer arithmetic. It makes no native spatial or physical claim. P000, the six-axis signed Cell torsor, separately typed time and joint-relation preservation remain unchanged. The whole joint action tree is retained through the declared exact quotient; prime factor reconstructibility is not used to discard any observer. This is `REUSE_APPLIED` for the existing quotient and `COMPOSE_APPLIED` with classical prime-interval input, not a new global tool family. The current toolbox lookup found T4 finite-fiber capacity and the prime-toolkit facade; no tool is claimed executed merely from that match.

## Theorem 1: a larger H can require fewer residual bits

C(27)=5, with attained values {0,1,2,3,4}, whereas C(28)=4, with attained values {0,1,2,4}. Therefore ceil(log2 C(27))=3 but ceil(log2 C(28))=2.

Proof. Values 6 and 9 are impossible at both thresholds since q>=5. At H=27, q=29,17,11,7,5 realize 0,1,2,3,4 respectively. At H=28, q=29,17,11,5 realize 0,1,2,4. Value 3 would require 7<q<=28/3; the only integers in this interval are 8 and 9, neither prime. These account for every possible value in {0} union T. In particular monotonicity in H cannot be assumed, even at the level of required worst-case bits. QED.

## Theorem 2: exact full-capacity set and permanent threshold

For every integer H>=1,

**C(H)=7 if and only if 45<=H<=62 or H>=66.**

Thus the first full-capacity threshold is 45, but the smallest threshold after which capacity is permanently full is 66. At H=62 all seven states occur; at H=63,64,65 the state 6 disappears, so C(H)=6 there.

Proof. For consecutive t<u in T, a prime q realizes F_H(q)=t exactly on the integer interval

q*t <= H <= q*u-1.                                            (1)

The top value 9 occurs iff some q>=5 satisfies 9q<=H, hence iff H>=45. Value 0 always occurs by the existence of primes greater than H.

For 45<=H<=62, the following table supplies interval covers for every intermediate state. Every listed q is prime and outside S. Intervals follow directly from (1), and their unions cover the stated H range.

| State t | Prime witnesses q | Their H intervals |
|---:|---|---|
| 1 | 23,31,37 | [23,45], [31,61], [37,73] |
| 2 | 17,23 | [34,50], [46,68] |
| 3 | 13,17 | [39,51], [51,67] |
| 4 | 11 | [44,65] |
| 6 | 7 | [42,62] |

For H=63,64,65, state 6 would require H/9<q<=H/6. Each such interval is contained in (7,11), which has no prime. The other six states occur: q=5,11,17,23,37,67 realize 9,4,3,2,1,0, respectively, for all three thresholds. Consequently C(H)=6 on this gap.

For 66<=H<=225, use the following finite interval covers. The largest prime below is 113, whose primality is checked by trial division through 10; all other witnesses are also directly verifiable.

| State t | Prime witnesses q | Their H intervals |
|---:|---|---|
| 1 | 61,113 | [61,121], [113,225] |
| 2 | 31,43,61,89 | [62,92], [86,128], [122,182], [178,266] |
| 3 | 19,23,29,37,47,61 | [57,75], [69,91], [87,115], [111,147], [141,187], [183,243] |
| 4 | 13,19,23,31,43 | [52,77], [76,113], [92,137], [124,185], [172,257] |
| 6 | 11,13,19,23,31 | [66,98], [78,116], [114,170], [138,206], [186,278] |

The state 9 uses q=5; state 0 can use q=227 throughout this finite range.

For H>=226, apply Nagura's classical prime-interval theorem: for every real x>25 there is a prime q with x<q<6x/5. For each consecutive pair t<u in T choose x=H/u. Then x>=H/9>25, and u/t>=4/3>6/5. Hence

H/u < q < 6H/(5u) < H/t,

so this prime realizes the state t. Such q exceeds 25, so it is admissible. State 9 still uses q=5, and state 0 uses any prime greater than H. All seven states therefore occur for every H>=226. Together with the finite covers and the necessary bound H>=45, this proves the exact classification. Since H=65 fails and every H>=66 succeeds, 66 is the sharp permanent threshold. QED.

## External input, source exposure and novelty boundary

Nagura, J., *On the Interval Containing at Least One Prime Number*, Proceedings of the Japan Academy 28(4) (1952), 177–181, DOI [10.3792/pja/1195570997](https://doi.org/10.3792/pja/1195570997). The [primary five-page PDF](https://www.jstage.jst.go.jp/article/pjab1945/28/4/28_4_177/_pdf) was read through the web tool in this run; its introduction gives the x>25, 6x/5 form and pp. 180–181 state/prove the family of interval bounds. We use only this weaker, unambiguous x>25 form. No new prime-distribution theorem is claimed, and no large-N computation is substituted for its universal tail.

This is directed, source-exposed research. The monthly corpus and source intake found the H=100 seven-state example and the explicit open attained-capacity question, but no existing H=66 permanent-threshold proof in those inspected sources. This bounded search is not a literature-novelty certificate or a live canonical-task inventory. Research6 PREFIX315/316 is a different phase-budget/six-state BRC line and is not merged by filename resemblance.

## Validation and handoff

`prime_capacity_check.py` independently checks the two displayed interval tables, exact state sets for 1<=H<=225 using all relevant primes, and the finite nonmonotonic witnesses. It performs new small integer checks only; the old divisor-prefix enumerations and historical 72,090-pair checker were not rerun. The infinite tail is the paper argument above plus Nagura's theorem.

Unresolved: independent mathematical review; formal native intake if desired; the general C(H) question for arbitrary S,a,L and composite residual fibers; prime-gap effective bounds for tightly spaced reachable products. No parent research line or formal Task is closed. Recommended next step is independent review of this bounded unit, then service a different neglected number-theory subline before extending this already answered example.

Researcher-ID: EM-NT-EFC4A8 / TASK_RESEARCH
