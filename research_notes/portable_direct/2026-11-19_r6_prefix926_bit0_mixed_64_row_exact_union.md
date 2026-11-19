# PREFIX-926 — Exact bit-0 mixed zero/one-flip collision increment over 64 modulus rows

Date: 2026-11-19, 进取数论研究6. Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / TWO_INDEPENDENT_ENUMERATIONS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED. Based on PREFIX-919/920 (mixed collisions) and PREFIX-923/924/925 (capacity/zero-zero/same-start certificates).

## Exact model
Let p=32, N=2^32, Q={262145,262147,...,524287} (131072 odd moduli). A named trace is either Z_x=(x,x) or F_x^i=(x,x XOR 2^i), retaining x, type and source-bit name; a,b in Q and the observer is Phi_(a,b)(u,v)=(u mod a,v mod b).

The old three-family collision sets in Q^2 of ordered pairs are:
- B: b < 33 ceil(N/a) OR a < 33 ceil(N/b);
- Z: lcm(a,b) < N;
- S: some d in [1,31] has 2^d ≡ 1 or -1 (mod b) (same-start different flip sources).
PREFIX-925's exact total is |B union Z union S|=7,462,508,971.

## Theorem 1. Two exact i=0 zero/flip constructions
Let k>=1, A=ka.
- When A<N and b divides A-1, F_0^0=(0,1) and Z_A=(A,A) collide: start difference A=ka and endpoint difference A-1.
- When A+1<N and b divides A+1, F_1^0=(1,0) and Z_(A+1)=(A+1,A+1) collide: start difference A and endpoint difference A+1.

Both traces have valid endpoints and different names. Reversing time preserves trace type and the named source bit, exchanges the two observer ports, and certifies the reversed ordered pair (b,a).

## Theorem 2. Complete finite candidate generation
Fix the 64-element set R={400001,400003,...,400127}, all odd. Let T_R be all (a,b) in Q^2 with b in R certified by Theorem 1, together with the time-reversed ordered pairs.

For each b in R, any admissible A=ka obeys 1 <= k <= floor((N-1)/262145)=16383. Since b is odd, gcd(k,b)>1 excludes both A±1 congruences. For every remaining k, calculate inv=k^{-1} modulo b. Minus witnesses require a ≡ inv (mod b); plus witnesses require a ≡ -inv (mod b). The width of Q is only 262142, strictly less than every b in R, so each residue class contains at most one candidate a in Q. Check its parity, endpoint bound and actual congruence; no candidate is omitted. Deduplicate ordered pairs by index(a,b)=((a-262145)/2)*131072+(b-262145)/2.

Test B,Z,S separately for (a,b) and (b,a), since S depends on the *second* port while B,Z are symmetric. The 24 special moduli supporting S are obtained by the exact 31-step modular-doubling scan of every b in Q.

## Theorem 3. Exact counts (two independent computations)

| Exact certificate count | Value |
|---|---:|
| (b,k,sign) parameter witnesses before pair deduplication | 386,923 |
| Ordered T_R pairs including transposes, before old-family exclusion | 773,724 |
| Outside B union Z union S, with second port in R | 218,863 |
| Outside B union Z union S, with first port in R | 218,819 |
| Outside old union and meeting both orientation selectors | 122 |
| **|T_R \ (B union Z union S)|** | **437,560** |
| **|B union Z union S union T_R|** | **7,462,946,531** |
| **Complement in Q^2** | **9,716,922,653** |

The directed inclusion-exclusion calculation is 218863+218819-122=437560. Exact sorted uint64 pair keys, encoded little-endian, have SHA256 \`f8e594257de9a99aa6de4be42d9dde79ba0427a5105c60bfa715d92bd25a60e4\`.

An independent Python generator iterates k and inverts k mod b, constructing and checking the actual traces. A separately written C++17 verifier iterates all 64 x 131072 possible (a,b) inputs, inverts a mod b and checks the only two admissible k residues; it prints parameter=386923, edge=773724, cert=437560 and emits sorted IDs with the identical digest. Both are exact all-integer finite computations.

Concrete witness outside all three old families: a=500001, b=400001, k=4, A=2000004. F_1^0=(1,0) collides with Z_2000005=(2000005,2000005). The start gap is 4a=2000004 and the end gap is 5b=2000005. Both traces observe (1,0). Both B inequalities are satisfied (therefore no B), lcm(a,b)>=N, and no 1<=d<=31 has 2^d ≡ ±1 (mod 400001).

## Reproduction
- PREFIX926_R6_BIT0_RESIDUE_CENSUS.py: \`python3 PREFIX926_R6_BIT0_RESIDUE_CENSUS.py PREFIX926_R6_BIT0_RESIDUE_RESULTS.json\`.
- PREFIX926_R6_BIT0_RESIDUE_INDEPENDENT.cpp: \`g++ -O2 -std=c++17 PREFIX926_R6_BIT0_RESIDUE_INDEPENDENT.cpp -o prefix926 && ./prefix926 sorted_ids.bin && sha256sum sorted_ids.bin\`.
- PREFIX926_R6_BIT0_RESIDUE_RESULTS.json: expected exact counts and hash.

Scope: this new increment is *only* disjoint from B/Z/S; it has not been deduplicated against all earlier signed-power, other mixed-flip or complete-row certificates. Neither an auxiliary two-port observer nor a valid XOR collision implies an X6-native dynamical theorem without an explicitly proved typed embedding/readout and preservation of relevant residual provenance. P000 and the frozen scientific pin remain unchanged.

Next discriminating problem: extend the modular-inverse generator to more b rows and all source bits i, then union pair IDs with *actual* previous pair-set encodings; do not add aggregate totals without intersection data.