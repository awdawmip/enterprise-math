# PREFIX-941 — Quotient-first exact bit sieve for odd-core named XOR collisions

Date: 2026-11-19. Lane: 进取数论研究6. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Direct predecessor: PREFIX-940 (immutable source `997f12987c154983381d77c6fc66684b5eda6111`). Mode: independent auxiliary named-XOR observer, not a native X6 dynamical statement. Status: AUTHOR_PROVED / EXACT_SMALL_DOMAIN_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Theorem: quotient-first XOR inverse, without enumerating the first modulus

Fix arbitrary positive integers k, b, t, and nonnegative source indices i,j. Put H=2^j, Y=t*b+2^i. Define e=+1 if bit j of Y is 1, and e=-1 otherwise; set X=Y-e*H. Then for every positive integer a,

  (k*a XOR 2^j)-2^i=t*b

holds **if and only if** X is positive, divisible by k, and a=X/k. In particular each (k,b,t,i,j) admits at most one a; imposing an allowed modulus set Q simply requires a in Q. If a state bound N is imposed, also verify k*a<N and the flipped endpoint lies in [0,N). These are exact necessary and sufficient conditions in the declared auxiliary trace model.

Proof. Set Z=k*a. The XOR identity is Z XOR H = Z + (1-2 bit_j(Z))*H. Therefore Y=Z XOR H. Applying the involution XOR H again gives Z=Y XOR H. If bit_j(Y)=1, clearing the bit is exactly Y-H; if bit_j(Y)=0, setting it is exactly Y+H. Thus Z=Y-eH=X and a=X/k. Conversely the specified X is exactly Y XOR H, hence (X XOR H)-2^i=Y-2^i=t*b. Uniqueness follows from injectivity of multiplication by k on positive integers.

The two legitimate named traces are F_0^i=(0,2^i) and F_(ka)^j=(ka,ka XOR 2^j), with both start observations equal mod a and both end observations equal mod b. This construction is a sufficient noninjectivity certificate for an observed pair (a,b), preserving the source bit names i,j. It does not claim exhaustiveness of other collision families.

## Corollary: odd-core quotient parity

When k,a,b are positive odd integers, t is odd iff (i=0 and j=0) OR (i>0 and j>0). Indeed k*a is odd, XOR bit zero toggles parity while XOR higher bits does not; subtracting 2^i toggles parity precisely for i=0. Since b is odd, t has the resulting parity. This is an exact admissible quotient sieve for every odd core k.

## Reproducible bounded regression

An independent Python exact-integer checker compares two enumeration routes for k in {1,3,5,7,9,11,13}, a,b odd integers from 5 through 63, i,j from 0 to 5: (1) direct XOR, enumerate all b and solve positive t, (2) enumerate b,t,i,j and apply the theorem's unique inverse candidate. The two complete finite witness sets agree exactly for each k. Witness counts by k: 1156, 1611, 1544, 1516, 1680, 1552, 1487, respectively. All odd-core parity assertions pass. Every equality uses exact integer arithmetic, no tolerance.

This inverse formulation removes the need to enumerate a for fixed (b,t,i,j). It is not a measured wall-clock speedup claim; complexity and sparsity gains depend on the candidate scan and indexing strategy. A further improvement is to solve the divisibility and j-th bit restrictions as a union of exact residue classes before scanning b. The full p=32 strict-19-bit domain remains unenumerated by this checkpoint.

## Preservation and controls

No shared X6 CLAIM, formal Result, Review or GOV action is asserted. Previous active shared owner and this direct auxiliary research remain separate. Originating historical R6 SID `MCP-31edc522830749ad8775ca012e02ef30`, Researcher `EM-DIRECT-58C410`, Activity `RA-25432C4AAE9BF66A907F5115` are provenance; present-session protected authority requires its own live test. If Activity association is not presently authorized, retain this exact immutable source for later legitimate portable checkpoint with observed readback and CAS. No duplicate science upload needed.
