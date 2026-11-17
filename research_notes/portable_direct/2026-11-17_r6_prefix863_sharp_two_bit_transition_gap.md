# PREFIX-863 — Sharp universal two-bit gap for fixed odd two-read full-transition observers

Date: 2026-11-17. Role: auxiliary TASK_RESEARCH / BRC named-source observer.
Scientific input: frozen pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`; predecessor PREFIX-861/862. Source of mathematical models: PREFIX-861/862 at immutable GitHub commits 727d6ca2dee6f707e3dd3cabba600d2c21b12bc8 and 77cb8fcf7c4583af5325bcfc229941b321b25612.
Status: AUTHOR_PROVED + EXACT_FINITE_CERTIFICATE; NOT_INDEPENDENTLY_REVIEWED; NOT_ADMITTED. Auxiliary provenance-preserving source observer, not native X6 event admission.

## Model and optimization domain

For an integer p>=1, a complete named binary state is x in {0,1}^p, encoded without bit loss as U(x)=sum_{i=0}^{p-1} 2^i x_i in {0,...,2^p-1}. A legal ordered heartbeat transition (u,v) is a no-op (v=u) or flips exactly one named bit, so v=u xor 2^i. Both old and new states are unknown beforehand. The ordered fixed-modulus observation is (u mod q1, v mod q2), with odd integers q1,q2>=3 chosen in advance and the same for all histories. We demand recovery of the entire ordered transition, including both states, which source flipped, and sign. There are exactly T_p=2^p(p+1) possible ordered transitions.

Let B_fix,odd(p) be the minimal peak width B= max(ceil(log2(q1+1)),ceil(log2(q2+1))) among all such pairs with injective ordered-transition observations. Let L(p)=ceil((p+log2(p+1))/2). Counting gives B_fix,odd(p)>=L(p), because a B-bit pair produces at most 2^(2B) transcripts. This lower bound is valid even if an adaptive scheme is allowed, but B_fix,odd is the nonadaptive odd-modulus optimization stated here.

## Theorem 863-A (uniform sharp constant)

For EVERY integer p>=5,

    L(p) <= B_fix,odd(p) <= L(p)+2.

Furthermore B_fix,odd(5)=6=L(5)+2 and B_fix,odd(7)=7=L(7)+2. Thus the universal additive constant 2 cannot be reduced to 1 within the stated fixed odd-modulus two-read model.

### Explicit construction and exact decoder

Put N=2^p. Let h(g) be the least d>=1 with 2^d == +1 or -1 modulo odd g>1. Select

    g(p)=11 if p=5; 19 if p=7; otherwise 3^(1+ceil(log_3 p)).

For the first two cases h(11)=5 and h(19)=9, respectively. For powers of three, h(3^s)=3^(s-1), so h(g(p))>=p. Let a be the least positive ODD integer with g a(a+2)>=N. Set

    (q1,q2)=(g a, g(a+2)).

For any legal trajectory, delta=v-u is among E_p={0} union {+2^i,-2^i:0<=i<p}. Distinct members of E_p give distinct residues modulo g because h(g)>=p (PREFIX-861-B). Therefore r2-r1 mod g identifies delta exactly. Since a is odd, gcd(a,a+2)=1, hence lcm(q1,q2)=g a(a+2)>=N. Generalized CRT with v congruent to r1+delta (mod q1) and v congruent to r2 (mod q2) gives the unique 0<=v<N. Then u=v-delta; the ordered named transition is recovered. This proves the observer has no collisions for every p.

### Uniform quantitative bound for p>=15

For the least odd a above, with X=N/g, elementary odd rounding yields a+2 < sqrt(X)+4, hence

    q2 < sqrt(g N)+4g.

For g=3^(1+ceil(log_3 p)) one has g<9p. Consequently

    q2+1 < 3 sqrt(p N)+36p+1.

For all integer p>=15, (36p+1)^2 < p*2^p. The base p=15 is 292681 <491520. If it holds for p, use
36(p+1)+1 <= (36p+1)(p+1)/p and (p+1)/p <=2 to obtain the next case by multiplying the squared inequalities. Thus 36p+1 < sqrt(pN) and

    q2+1 <4 sqrt(pN).

Therefore B=ceil(log2(q2+1)) <= ceil((p+log2 p)/2)+2 <= L(p)+2.

### Exact small range p=5,...,14

Here is the full integer verification table (the first two rows with p=5 and p=7 use the stated exceptional g values):

| p | g | (q1,q2) | counting lower L | constructed B | gap |
|---:|---:|---|---:|---:|---:|
|5|11|11, 33|4|6|2|
|6|27|27, 81|5|7|2|
|7|19|57, 95|5|7|2|
|8|27|81, 135|6|8|2|
|9|27|135, 189|7|8|1|
|10|81|243, 405|7|9|2|
|11|81|405, 567|8|10|2|
|12|81|567, 729|8|10|2|
|13|81|891, 1053|9|11|2|
|14|81|1215, 1377|9|11|2|

This proves the uniform upper bound for the remaining ten p-values, including p=5 and p=7.

### Exact optimality witnesses at p=5 and p=7

A complete finite enumeration uses ALL ordered odd (q1,q2) with 3<=qj<=2^B-1. For each legal transition (u,v), it computes (u mod q1,v mod q2); if two distinct ordered transitions give the same pair, that modulus pair is disqualified. For p=5 at B=5, there are 15^2=225 ordered candidate pairs and zero collision-free pairs. At B=6, (11,33) is injective. For p=7 at B=6, there are 31^2=961 ordered candidates and zero collision-free pairs. At B=7, (27,127) is injective. Monotonicity in B eliminates all smaller widths. This establishes exact optimality, and hence sharpness of additive constant 2.

The same finite method also yields B_fix,odd(6)=6 with (25,63), B_fix,odd(8)=7 with (57,95), B_fix,odd(9)=8 with (57,209). Lower-width complete scans cover respectively 225, 961 and 3969 ordered odd modulus pairs. These are additional regression checks, not assumptions in the universal proof.

## Reproduction and evidence scope

Companion program `PREFIX863_R6_SHARP_TWO_BIT_GAP_CHECK.js` runs exact BigInt arithmetic for the explicit g/a/CRT sufficient conditions over p=1..128, directly enumerates every permitted ordered transition for p=1..12, and exhaustively tests every ordered odd modulus pair at one below the verified optimum for p=5..9. The output `PREFIX863_R6_SHARP_TWO_BIT_GAP_RESULTS.json` contains the concrete bound table, enumeration counts, witnesses and exact assertion status. Infinite-p coverage comes from the proof above; the finite tests independently exercise its boundary arithmetic.

The two residues are a declared two-heartbeat observation carrier: the decoder reconstructs full named old/new source identity and ordered transition, so all future operations that depend only on this recovered transition can act on the reconstructed states. A physical heartbeat readout with multiplicative coefficient c_t can use this normalized observer if c_t is known and invertible modulo the selected odd moduli. Native X6 Cell/Link/Port source and permission preservation remain a separate mapping problem.

## Next precise question

Determine the exact B_fix,odd(p) for p>=10 with certified finite search or sharper analytic arithmetic; test whether the two-bit overhead persists in the ADAPTIVE second-modulus model (not decided by the fixed-pair exhaustive certificates), and whether any native X6 observer has a typed, provenance-preserving realization of these source transitions.
