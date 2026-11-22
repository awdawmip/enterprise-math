# X6 R122 — A universal three-halves exclusion envelope for small integer Ports

Date: 2026-11-23 (Asia/Shanghai). Status: **AUTHOR FINITE EXHAUSTIVE ARGUMENT / INTEGER REPLAY PASS / NOT INDEPENDENTLY REVIEWED**.

## Frozen scope and predecessor

This continues the conditional four-positive-real-weight, six-pair BRC integer observer in [R121](https://github.com/awdawmip/enterprise-math/blob/8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd/research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md). It uses exactly its four heights, physical Port, six pair gaps, and its 18-row universal *optimizer* bank. Native P000/X6 heartbeat dynamics and the R063 benchmark are independent; none of their frozen scientific inputs has been repinned.

For a nonzero integer direction a=(x,y,z), identify a and -a, set

q(a) = max(sum(max(a_i,0)), sum(max(-a_i,0))),

h(a) = (0, x+3y+6z, 3x+12y+30z, 7x+39y+126z),

g(a) = (|h1-h0|,|h2-h0|,|h3-h0|,|h2-h1|,|h3-h1|,|h3-h2|).

For positive weights w=(A,B,C,D), write s=(A+B,A+C,A+D,B+C,B+D,C+D),
F_w(a)=max_j g_j(a)/s_j, and eta_p(w)=min_{0<q(a)<=p} F_w(a).
The strict-near set N_p(w) consists of unoriented a with q(a)<=p and F_w(a)<(3/2) eta_p(w).

## Theorem — exact finite necessary envelope, integer Ports 1–10

Let B be the 18-row optimizer bank of R121. At each integer p in 1,...,10 define

C_p = {unoriented nonzero integer a : q(a)<=p and
       there is **no** b in B with q(b)<=p and 2 g_j(a)>=3 g_j(b) simultaneously for all six j}.

Then for every positive real w and every such p,

**N_p(w) is a subset of C_p.**

The exact C_p cardinalities are:

| p | Full feasible population | Excluded by six-gap three-halves domination | |C_p| |
|---:|---:|---:|---:|
| 1 | 6 | 5 | 1 |
| 2 | 27 | 23 | 4 |
| 3 | 73 | 66 | 7 |
| 4 | 154 | 142 | 12 |
| 5 | 280 | 266 | 14 |
| 6 | 461 | 442 | 19 |
| 7 | 707 | 692 | 15 |
| 8 | 1028 | 1012 | 16 |
| 9 | 1434 | 1414 | 20 |
| 10 | 1935 | 1915 | 20 |

Thus at Port 10 all 1,935 unoriented integer directions reduce to **20 candidates** for strict 3/2-nearness, with 1,915 universally excluded. Across all ten Port values, the union of all candidate lists contains **31 distinct integer directions** (individual Port lists need not be nested). Consequently, for all w>0 and 1<=p<=10 the near-direction count is at most 20. The bound is a valid uniform *upper* bound, not claimed sharp.

At Port 1, C_1={(1,0,0)}, and this vector is the R121 optimizer for every w>0. Therefore the exact strict-near set is **N_1(w)={(1,0,0)}** for every positive real weight vector.

## Proof

Every pair capacity s_j is positive. If there is a feasible bank row b with 2 g_j(a)>=3 g_j(b) for all j, division by the same positive capacity s_j gives g_j(a)/s_j >= (3/2) g_j(b)/s_j for each j. Taking maxima yields F_w(a) >= (3/2) F_w(b) >= (3/2) eta_p(w). Such a is excluded from the strict-near set for *all* physical positive w. Contraposition proves N_p(w) subset C_p.

For the finite census, q(a)<=10 implies -10<=x,y,z<=10. Enumerate every nonzero integer triple in this cube and retain the unique representative with first nonzero coordinate positive. At p=10 this gives exactly 1,935 unoriented directions. For each p=1,...,10, compute q and all six gaps by integer arithmetic, compare every feasible a against every feasible member of the **explicit** R121 bank using the six exact inequalities 2g_j(a)>=3g_j(b). This produces the table and all explicitly listed C_p in the attached JSON. An independent check within the executable compares the exclusion predicate from the 18-row bank with that from the **full** feasible population, at every p and for every direction: all agree. No floating-point or weight sampling is used. The inequality proof and the enumerated finite domain together establish the theorem for **all positive real weights**.

## Recalculation and limits

Run `node research_notes/portable_direct/x6_r122_small_port_near_exclusion_verify.js` from the project root. It emits the complete JSON certificate and fails if the population, C_p counts, R121-bank/full-population comparison, 31-union, or Port-10 exclusion tally differs. The researcher also independently recomputed the same counts and union using a separate Python integer enumeration before publishing.

This is a **necessary finite candidate envelope**, not a complete physical-weight realizability atlas; individual members of C_p may still be unable to occur as strict near-directions. The sharper full classification of all w>0 and the maximum attainable count at Ports 2–10 remain open.

## Provenance and next question

Source mathematical data: R121 committed at `8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd`; R119 height and Port definitions at `a025ec1bac8846cf684613aea7ed0d82dff6ba8b`. Current normative rules and P000/ACTIVE worldview were read separately; this theorem concerns only the explicitly stated conditional observer.

Next: decide physical-weight feasibility of each of the 31 surviving Port-specific candidate rows using the constrained capacities s_ij=w_i+w_j (rather than treating the six denominators as independent), and determine the exact maximal strict-near count for p=2,...,10.
