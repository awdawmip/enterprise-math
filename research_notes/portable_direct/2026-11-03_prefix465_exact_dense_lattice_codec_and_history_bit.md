# PREFIX-465 — Exact dense finite-horizon X6 BRC weight codec and conditional-history repair

2026-11-03 Asia/Shanghai. Author-side proof + exact executable witness; UNREVIEWED / NOT_ADMITTED.
Continuation: PREFIX-464 (1598c9f35d369b1b8b1e8f7ce3134776bf47f271). Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Source: P000 native X6, ACTIVE Heartbeat World and joint-relation preservation; current portable research/behavioral rules. Scope: 11 native eligible steps `+e1, ±e2,...,±e6`, strictly positive rational **individual path-product weights**, ordered-path integer multiplicity, chart-relative X6 coordinates. No phase/amplitude interpretation or physical time claim.

## Input and weight signature

Fix letter weights `+e1=1`, positive signed axes e2..e6 `(6,12,18,24,36)`, and all their negative counterparts weight `1`. For a path of length m, let s be its +e1 count, y∈Z⁵ the signed net displacements on e2..e6, and p=(m-s-Σ|y_i|)/2 the sum of opposing-pair counts p_i. Put u=(p_2,p_3,p_4,p_5) with u_i≥0, Σu_i≤p. The exact valuation signature from PREFIX-463/464 is

`A=p_2+2p_4+p_5, C=p_3+p_5`.

Individual word weight at (m,s,y,A,C) is exactly
`W=(∏_{i=1}^5 rho_i^max(y_i,0))·6^p·2^A·3^C`,
where rho=(6,12,18,24,36).

## Theorem A — Exact feasible lattice semigroup, all p≥0

`S_p={(A,C)∈Z²: 0≤C≤p, 0≤A≤2p−C}`,
and `|S_p|=(p+1)(3p+2)/2`.

Proof: the four occupation generators for (A,C) are (1,0),(0,1),(2,0),(1,1). Every representation using at most p generators satisfies the inequalities. Conversely choose any integer point satisfying them and set `d=max(0,A−2(p−C)), R=A−d, c=floor(R/2), a=R mod 2, b=C−d`. Then d≤C, R≤2(p−C), all a,b,c,d are nonnegative, and a+b+c+d=C+ceil(R/2)≤p. Their generator sum is (A,C). For each C there are 2p−C+1 options for A, yielding the formula. QED.

## Theorem B — Exact finite-p optimal fixed-width scalar code

Let `offset_p(C)=C(2p+1)−C(C−1)/2` and `D_p(A,C)=offset_p(C)+A`. The code bijects S_p to the consecutive integers `0..n_p−1`, where `n_p=|S_p|`. Decode by binary search for largest C with offset_p(C)≤D and A=D−offset_p(C). Hence exactly `(n_p−1).bit_length()` bits suffice, and fewer fixed-width bits cannot distinguish n_p signatures (pigeonhole).

The previous rectangular mixed-radix box has (2p+1)(p+1) slots. For p=16 the new code has 425 slots, exactly 9 bits, versus 561 slots, 10 bits; p=32: 1617 versus 2145, 11 versus 12 bits. The 2×4 integer signature matrix contains columns (1,0),(0,1), so its image lattice is Z² and Smith invariant factors are (1,1). A lattice basis change alone cannot capture the **finite bounded semigroup shape** responsible for the saving. Dense encoding uses one integer quadratic prefix and additions; decoding uses O(log p) integer comparisons. There is no precomputed O(n_p) lookup table.

## Theorem C — Minimal one-bit structural residual for a conditional future

Declare a future language G: first letter unrestricted; for every later step the letter +e1 is permitted only if the immediately preceding letter was +e2; the other ten letters are permitted. The observable is the exact endpoint/product-weight/multiplicity histogram over all legal future extensions.

Attach a Boolean state b=1 iff the last letter is +e2 (empty prefix b=0, with a known m=0 exception). The state (m,s,y,A,C,b) is sufficient for G over **all future horizons**. At each append, the eligibility of +e1 depends only on b; update the new b to 1 iff the appended letter is +e2. Update (s,y,A,C) by the known native signed step and add the relevant pair-signature column precisely when an opposite-sign pair is formed. Homogeneous positive product weights are reconstructed from the stated formula. Induction on extension length proves exact descent.

Minimality witness: words `(+e2,+e3)` and `(+e3,+e2)` both have m=2, s=0, y=(1,1,0,0,0), p=0, A=C=0, and product weight 72. Only the second permits +e1 next. Their distinct future readouts require at least two state labels; one bit suffices. This repair is *observer and operation typed*: different provenance-sensitive futures may have other state requirements.

## Reproducible finite checks, evidence and costs

The companion Python stdlib script exhaustively checks the occupation-to-lattice correspondence, explicit occupancy witness, dense encoding and decoding for all p=0..24, plus boundary probes at p=32,64,128,1024. It executes the exact dense-key 11-branch conditional BRC path recursion through m=7. For m=0..5 it independently brute-enumerates every ordered word, testing the complete (endpoint, Fraction exact product weight, b) integer histogram against dynamic aggregation. At m=7, 11,660,641 legal ordered words aggregate to 23,453 states under G. Log terminates ALL_CHECKS_PASS.

The bit result is signature-only; endpoint, multiplicity, state/bool and metadata costs are additional. The numeric experiment is a typed positive-weight path count on native X6, not a native Shor phase or physical-residual computation. General input-weight factorization/valuation preprocessing and stream repacking cost remain as in PREFIX-463/464. Formal project CLAIM/Review/Admission were not obtained.

Next PREFIX-466: compute minimal finite automaton quotients for broader explicitly typed conditional provenance languages; find exact joint bounded-horizon lattice/automaton encoders, and measure their input transformation/repacking costs. Independently keep the all-degree polynomial observation-rank question open.
