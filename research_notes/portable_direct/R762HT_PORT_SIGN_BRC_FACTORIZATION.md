# R762HT — Positive BRC factorization: Port closure × six-axis sign balance

**Scope and authority.** New author-side proof under frozen Enterprise Math science at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Continues R762HK, R762HR and R762HS. Composite six-axis Port candidate, NOT a primitive P000 TRIADIC_CLOSURE_E theorem; independent mathematical Review = NOT_REVIEWED. No Task CLAIM, Result or Foundation promotion. Named Port histories and individual event provenance must be retained for subsequent time/rotation dynamics.

## HT1. All-length conditional factorization

Let X={0,1,2,3,4,5}, P=the fifteen named two-axis Ports, and S=the twenty named three-axis supports. A legal composite event moves between distinct Ports p,q sharing exactly one axis, with support s=p union q. Write h_s=sum_{i in s} e_i in Z^6. Fix a histogram n=(n_s) of m=sum_s n_s individually distinguished event occurrences; let D(n)=product_s(n_s!).

Rooted Port histories are sequences p_0,...,p_m=p_0 consuming every occurrence exactly once. Independent signs epsilon_t in {-1,+1} give displacement sum_t epsilon_t h_{s_t}. Define N_p(n) as the number of labeled rooted legal Port histories with p_0=p, C(n) as the number of zero-displacement sign choices for the n_s labeled occurrences, and J_p(n) as the count of their joint realizations.

Introduce commuting support markers y_s and Laurent displacement markers z_0,...,z_5. For vectors v, z^v=product_i z_i^{v_i}. Let the 15×15 matrices B and A have entries

  B_{p,q}(y) = y_{p union q} whenever |p intersect q|=1, else 0;
  A_{p,q}(y,z) = y_{p union q} (z^{h_{p union q}} + z^{-h_{p union q}}) on the same edges, else 0.

Let F_n(z)=product_s (z^{h_s}+z^{-h_s})^{n_s}. For every m>=0, including m=0:

\[
\boxed{N_p(n)=D(n)[y^n](B(y)^m)_{p,p}}
\]

\[
\boxed{C(n)=[z^0]F_n(z)}
\]

\[
\boxed{J_p(n)=N_p(n) C(n)
=D(n)[y^n z^0](A(y,z)^m)_{p,p}.}
\]

For all starting Ports, replace the matrix diagonal entry by its trace. The root/event-time seam is distinguished; no quotient by cyclic rotation or path reversal has been taken. Therefore a legal rooted sign-balanced realization exists exactly when N_p(n)>0 and C(n)>0. In the open coordinate-even signability problem, a genuine counterexample is a histogram with N_p(n)>0 and all six support totals even, but C(n)=0.

**Proof.** Expanding (B^m)_{p,p} gives a positive monomial for each admissible ordered rooted Port word. Extracting [y^n] picks exactly the words with support histogram n. Assigning the n_s distinct occurrence identifiers to their positions gives n_s! bijections for each s and the multiplier D(n). For any such word, the formal signed-displacement choices multiply to F_n(z), which is independent of the Port *ordering* after conditioning on the entire support histogram. The zero-coefficient counts all sign assignments without subtracting positive BRC weights. Consequently the joint count is the product N_p C and equals the stated coefficient of A^m. For m=0 the empty walk and empty sign choice each contribute 1. QED.

This is a precise conditional factorization of *counts*, not a claim that physical Port/Link order may be erased. It is valid for the declared composite candidate model with no extra native force, time, rotation or exposure constraints. Adding such constraints requires a new compatible weighted operator and a separate preservation proof.

## HT2. Exact rooted histogram DP and grouped positive sign count

For a fixed root p, let W_p(q,k) count paths from the current Port q to p using the remaining support histogram k. Define

  W_p(q,0) = 1 when q=p, otherwise 0;
  W_p(q,k) = sum_{q': |q intersect q'|=1, k_{q union q'}>0} W_p(q', k-e_{q union q'}).

Then N_p(n)=D(n)W_p(p,n). Memoization has at most 15 product_{s:n_s>0}(n_s+1) states and at most eight Port neighbors per state. This bound is exponential in the number of active support types, and exact integer bit cost must also be included; no universal polynomial-complexity claim for variable histograms is made.

The independent six-axis sign factor has an exact nonnegative binomial expansion:

\[
F_n(z)=\prod_s\sum_{j=0}^{n_s}
\binom{n_s}{j}z^{(2j-n_s)h_s}.
\]

Thus C(n) is obtainable by integer-state convolution over six-dimensional displacements without expanding every event separately. The formal negative exponents designate signed Cell displacements, not negative mass. Both factors preserve multiplicity of individual sources.

## HT3. Exact 14-event joint census, original R762HK Port witness

Consider the fixed-root walk

  01 → 15 → 12 → 25 → 24 → 04 → 05 → 03 → 04
     → 24 → 23 → 25 → 35 → 05 → 01.

Its support sequence is

  015,125,125,245,024,045,035,034,024,234,235,235,035,015.

Exactly five support types occur twice (015,125,024,035,235) and four occur once (245,045,034,234); hence D(n)=2^5=32. Exact integer computation gives:

| Observable | Value |
|---|---:|
| Unlabeled rooted Port words [y^n](B^14)_(01,01) | 422 |
| Labeled rooted Port histories N_01(n) | 13,504 |
| Zero-displacement sign choices C(n) | 104 |
| **Joint labeled, signed positive BRC outcomes J_01(n)** | **1,404,416** |

The existing HK flip-block polynomial has total coefficient 104, agreeing with C(n). The 422 Port-word and 1,404,416 joint-source counts are new for the *entire fixed-root support-histogram class*, not just the one sample ordering. Each of its 13,504 labeled Port histories permits exactly 104 zero-displacement sign assignments. Every item counted is distinguished by Port word, event IDs and sign choices.

For a two-event unit case with only support 015 twice and root 01, the intermediate Port can be 05 or 15. Hence W=2, D=2, N=4, C=2, J=8.

## Executed verification and limits

R762HT_CHECK.cpp was compiled with g++ -std=c++17 -O2 -Wall -Wextra -pedantic. It checked the fourteen legal Port transitions, the input histogram, Port DP=422 against a separate no-memo DFS=422, all 2^14 sign assignments=104 against grouped positive binomial convolution=104, and the two-event Port case. Actual stdout:

  PASS R762HT; W01=422; D=32; rooted_labeled=13504; C=104; joint=1404416; DFS_nodes=88983

This computational certificate covers the specified sample and does not prove universal signability; the all-length factorization itself has the elementary coefficient proof above. R762HT_EVIDENCE.json records the numerical scope and commands.

**Next unresolved frontier:** find a histogram with strictly positive *rooted connected* Port realization factor and zero balanced-sign factor despite even six-axis totals; or prove the two positive factors can never separate under those hypotheses. The earlier degree-even Port projector is only a necessary feasibility test; this operator enforces a continuous single Port itinerary. Retain frozen P000 and seek a genuine native TRIADIC_CLOSURE_E force/Cell/Link/Port/time/rotation lift separately.