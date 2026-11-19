# PREFIX-948 — Adjacent-core determinant inversion, resonance, and exact k=21/23 intersection

**Date:** 2026-11-20. **Frozen scientific input:** \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. **Predecessor:** PREFIX-947A, immutable scientific note \`1d101e10df7c93cdcba84108435b7c36f252ecd3\`. Model: auxiliary named-XOR two-port observer with ordered odd moduli \`Q={262145,262147,...,524287}\`, source bits 0..18 and 32-bit legal endpoints. This is not a native signed-X6/Heartbeat/BRC dynamics claim. Status: AUTHOR_PROVED, TWO_INDEPENDENT_COMPLETE_FINITE_COMPUTATIONS_AGREE, UNREVIEWED, NOT_ADMITTED.

## Theorem 1 — exact two-core determinant inverse

Let k,a,b,t,T be positive integers, and suppose both named equations hold:

\`\`\`
(k*a XOR 2^j)-2^i=t*b,
((k+2)*a XOR 2^J)-2^I=T*b.
\`\`\`

Define signed bit changes \`s=1-2*bit_j(k*a)\` and \`S=1-2*bit_J((k+2)*a)\`, and put
\`c=2^i-s*2^j\`, \`C=2^I-S*2^J\`, \`m=T-t\`, \`d=2*t-k*m=(k+2)*t-k*T\`.

**Nonresonant case d != 0:** for fixed (k,t,T,i,j,I,J,s,S) there is at most one ordered modulus pair, determined exactly by

\`\`\`
a=(t*C-T*c)/d,
b=(k*C-(k+2)*c)/d.
\`\`\`

The candidate is a joint witness iff both fractions are positive integers in the allowed modulus set, the two actual source bits give signs s,S, and the endpoints obey the stated state bound. Thus nonresonant overlaps can be generated without enumerating any moduli.

**Resonant case d=0:** consistency requires \`(k+2)*c=k*C\`. If k is odd, gcd(k,k+2)=1, so \`t=k*r\`, \`T=(k+2)*r\`, \`c=k*h\`, \`C=(k+2)*h\` for integers r>0,h, and the solutions satisfy \`a-r*b=h\`, together with the original signed-bit conditions. No quotient inversion applies at d=0.

*Proof:* XOR with one bit is addition by its signed weight. The two equations become \`k*a-t*b=c\` and \`(k+2)*a-T*b=C\`. Integer linear elimination gives both numerator identities. When d=0, coprimality of the two odd cores gives the stated rank-one parameterization. Conversely the checked linear equations plus the actual bit signs imply the two original XOR equations.

## Theorem 2 — common diagonal background for odd cores

For any odd positive cores k and l, source bits in 0..J, and any set Q containing at most one odd representative per residue modulo \`M=2^(J+1)\`, a diagonal pair (a,a) has a named-XOR collision witness from each core whenever neither \`k*a\` nor \`l*a\` has all its low J+1 bits equal to 1. Choose i=j at any zero source bit, so the quotient is respectively k or l. For each odd core the *only* exceptional residue is \`a=-k^(-1) mod M\`; hence at least |Q|-2 such common diagonals exist, subject to the trajectory state bound.

With k=21,l=23,J=18 and the stated Q, exceptional residues are 274627 and 182361. Only 274627 lies in Q. Therefore **131071 common diagonals** arise from this generic resonance mechanism; a large part of the raw core overlap is not a distinctive off-diagonal joint relation.

## Exhaustive resonance classification for k=21 and k+2=23

PREFIX-947A already proved the exact quotient gap \`0<=m<=6\` in this full 19-bit domain; positivity and size give \`t<=42, T<=46\`. The only d=0 quotient pairs are (t,T)=(21,23),(42,46). The possible signed source terms \`2^i-s*2^j\` form a finite 722-choice list. Exhaustively checking \`23*c=21*C\` yields exactly **361** compatible signed-index pairs, every one with \`c=C=0\` (equal source positions and positive sign). There are 722 such parameter combinations across the two resonant quotient pairs. The (42,46) branch forces a=2b, excluded by the odd modulus domain; (21,23) gives exactly the diagonal family above. The compatible-term enumeration is separately checked by Python integer arithmetic.

## Two independent, complete, source-retaining computations

**Algorithm A** (\`PREFIX948_R6_DETERMINANT_JOINT_CPP.cpp\`): enumerates 150651076 nonresonant signed-bit/quotient configurations, with exact division, domain, sign, and original-equation checks; handles resonance explicitly; deduplicates uint64 pair IDs.

**Algorithm B** (\`PREFIX948_R6_DIRECT_DIVISOR_ROWS_CPP.cpp\`): independently builds a \`t*b\` divisor-lookup for every odd b in Q and t=1..46. It directly evaluates both XOR cores at all 131072 a and all 361 named source pairs, builds row bitmaps, and intersects them. It uses **neither the determinant formulas nor any previously saved W21/W23 sorted binary data**. Both full-domain runs produced the exact same complete sorted IDs byte for byte.

| Exact quantity | Value |
|---|---:|
| Core21 raw named witnesses (independent direct regeneration) | 19,691,842 |
| Core23 raw named witnesses | 16,675,790 |
| Core21 unique pairs | 15,682,891 |
| Core23 unique pairs | 13,041,372 |
| Nonresonant joint witness combinations | 8,711 |
| Nonresonant distinct modulus pairs | 6,204 |
| Resonant joint witness combinations | 10,541,739 |
| Resonant distinct modulus pairs | 131,071 |
| Pairs covered by both cases | 1, namely (262145,262145) |
| **Total distinct common modulus pairs** | **137,274** |
| **Diagonal common pairs** | **131,071** |
| **Off-diagonal common pairs** | **6,203** |
| **Total named joint witness combinations** | **10,550,450** |

The nonresonant joint-witness quotient-gap counts for m=0..6 are exactly \`[6,644,6513,1314,231,3,0]\`. The 10,541,739 resonant witness combinations have m=2. One off-diagonal explicit joint witness: (a,b)=(262145,274433); k21 (i,j,t)=(14,0,20), k23 (I,J,T)=(0,13,22). The forbidden diagonal (274627,274627) is absent from the full intersection.

Both new algorithms generated the same sorted \`uint64 little-endian\` pair-ID stream, where \`id=((a-262145)/2)*131072+(b-262145)/2\`; it contains 137274 IDs (1,098,192 bytes) and has SHA-256:

\`\`\`
54c35a06874167484f0028443be45d3b03e69bc3bdf0e64fc97cf371522f6223
\`\`\`

This independently reproduces PREFIX-947A's old intersection digest; the old binaries were not used in either new computation. Observed standalone calculation: Algorithm A 1.03 seconds, peak RSS 132824 KiB; B 3.99 seconds, peak RSS 145012 KiB (compilation, preparation, and downstream review excluded).

## Interpretation and next open problem

Precisely 131071/137274 = **95.4813%** of common pairs are diagonal. The **6203 off-diagonal** intersection pairs are the more informative cross-core joint-relation population for this auxiliary observer. No additional previously uncovered collision pairs are claimed; the prior conditional cumulative certificate total remains 7,597,037,839, and the mother objective \`B_fix,odd(32) in {19,20}\` remains open. Composite-core 21 is preserved as its own named joint observation direction, not erased in favor of factors 3 and 7.

Next: generalize and count rank-one resonance among other odd cores, then use CRT/grouped bit signs to reduce the nonresonant O(bit_positions^4 * quotient_window * gap_window) search, retaining named ports and verified off-diagonal coverage.

**Controls:** Original R6 provenance is researcher \`EM-DIRECT-58C410\`, SID \`MCP-31edc522830749ad8775ca012e02ef30\`, Activity \`RA-25432C4AAE9BF66A907F5115\`. This note does not assert active session capability, a new Activity association, a CLAIM, formal PROGRESS, independent Review, or acceptance. The previously safety-rejected PREFIX-946 publication was not replayed or rerouted.