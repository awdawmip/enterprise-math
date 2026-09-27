# Endpoint-bit signed-gap identities

Status: symbolic derivation only; no new arithmetic execution, cost measurement, or formal admission. The source is the completed single-window identity at EM `56b191519b036c6890cae328c3b3812fbc1debb7`, `research_notes/directed_recovery/20260927_C6438C/qft_signedgap/ONE_WINDOW_REDUCTION.md` (SHA-256 `ee13a8d8bc03dd8359f3a3a3d80ac7cfdc9a0094f19deeb2af91189d75a42095`). This is a separately versioned successor; the original sources/evidence remain frozen.

For integers g >= 1, 0 <= k < g, R >= 1 and 0 <= r < R, let L=2^g and

    K(g,k,R,r) = sum_{0 <= x,y < L, y-x = r (mod R)} (-1)^(bit_k(x)+bit_k(y)).

Let T(M,R,r) count all ordered pairs in [0,M)^2 satisfying y-x = r (mod R). With M=qR+u, 0 <= u < R,

    T(M,R,r) = R*q^2 + 2*q*u + max(u-r,0) + max(u-(R-r),0).

This is the existing unsigned interval-count contract. If A is the set of integers with bit k equal to zero and J counts constrained pairs in A x A, the previous four-block proof gives K=4J-T(L,R,r). These endpoint cases simplify J without a floor-window query.

## Highest bit

For k=g-1, A=[0,L/2). Therefore

    K(g,g-1,R,r) = 4*T(L/2,R,r) - T(L,R,r).

This holds for every positive R, including R=1 and nonunit/even moduli. It uses two interval-count queries and no floor-window query. Negative K is retained. The normalization is still 4^(-g), not a normalization of the signed count itself.

## Lowest bit, even modulus

For k=0, the sign is (-1)^(x+y)=(-1)^(y-x). If R is even, every admissible difference r+jR has parity r. Thus

    K(g,0,R,r) = (-1)^r * T(L,R,r),       R even.

One interval count suffices; the parity is a signed branch, not a discarded negative result. No modular inverse, order discovery, or numerical phase computation enters this proof.

## Lowest bit, odd modulus

For k=0, A consists of x=2a with 0 <= a < H=L/2. The pair constraint on A becomes 2(b-a)=r (mod R). When R is odd it is equivalent to b-a=r_half (mod R), where

    r_half = r/2            if r is even,
             (r+R)/2       if r is odd.

In both cases r_half is an integer in [0,R), and 2*r_half=r (mod R). Multiplication by two is bijective modulo odd R, so this is an equivalence rather than a one-way filter. It includes R=1, where r=r_half=0; an inverse modulo one is not requested. Therefore

    K(g,0,R,r) = 4*T(H,R,r_half) - T(L,R,r),       R odd.

Two interval counts suffice. When g=1 both endpoint identities apply and must agree by their definitions. A dispatcher can give the highest-bit case priority and use the lowest-bit branch otherwise. Interior bits retain the frozen one-window formula without claiming an endpoint shortcut.

## Execution and certificate contract to test

Create a new source/schema that pins the frozen one-window and interval-count implementations. Validate exact non-Boolean integer inputs and the complete range contract before creating arithmetic work. Use actual typed magnitude arithmetic for L,H,r_half and interval operations, and the existing signed typed outer arithmetic for multiplication by four, subtraction and the parity sign. Host code may select the finite branch; it must not supply an unrecorded numerical oracle. Preserve every intermediate receipt and source binding. Replay must choose the same branch from the declared input and check the complete result; accepting a caller's claimed branch or result is insufficient.

Record per branch: full input, identity identifier, typed construction of relevant powers/half-residue, interval receipts, outer signed operations, final K, unchanged raw denominator exponent 2g, and actual cost counters. A wrong branch identifier, wrong r_half, incorrect sign, altered interval record, Boolean input and wrong source need meaningful negative controls. Do not repeat the whole prior experiment merely to regenerate old answers: compare with its fully read, hash-bound actual evidence and pay separately for any newly introduced cases.

The first bounded test can reuse all 31 prior residue outputs over the nine frozen tuples, including the interior-bit fallback. All production/replay/negative-control costs must be retained separately. A branch-local operation saving is not a timing result; report the actual new digit costs. Existing one-window production is 137,611 digits across these fixtures; exhaustive comparator history is 76,977. Neither number implies a general asymptotic ranking or a Shor speedup.

## Limits and continuation

These identities reduce an already polynomial-bit scalar query to simpler existing interval queries on endpoint-bit families. They do not handle general Walsh masks, arbitrary multi-gap convolution, paid period/address discovery, or growth of full-matrix correlations. They preserve every incoming/outgoing matrix coordinate when eventually used as a scalar factor; they do not authorize state compression from agreement on one vector.

A dialogue can independently verify the three set/parity arguments from this file, refine the certificate contract, or find analogous sign partitions. Numerical validation remains a separate evidence claim. No tool or host requirement is imposed on this symbolic continuation.

Global-Knowledge-Sync: main@bd2873d / GLOBAL_KNOWLEDGE_V1
