# PREFIX-898 — Exact overlap-free zero/flip panel census: 6,967,420 new strict-19-bit BRC collision certificates

Date: 2026-11-18 (Asia/Shanghai). Research lane: 进取数论研究6. Prior scientific frontier: PREFIX-897. Existing provenance: Researcher-ID EM-DIRECT-E370C2, Activity RA-B79E898CC00D09F08FA2ABC5; the current shared X6 owner read was separately requested, not treated as authorization. Original scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d, unchanged.

Status: AUTHOR_PROVED / EXACT_DECLARED_FINITE_CHECKED / PARTIAL_INDEPENDENT_CROSSCHECK / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED. This is an independent named-source two-port BRC auxiliary. No native X6 task CLAIM, physical time reversal, P000 amendment, or mother-goal closure.

## 1. Exact model and inherited certificate

Let p=32, N=2^32, T=33N, Q={262145,262147,...,524287} with |Q|=131072. Legal named trajectories are Z_x=(x,x) and F^i_x=(x,x XOR 2^i), 0<=x<N and i=0,...,31. Observe Phi_(a,b)(u,v)=(u mod a,v mod b). Trajectory identity includes type, named source bit, direction, endpoints, and multiplicity.

PREFIX-897 gives an exact four-family collision-certified subset E of Q^2 with |E|=7,567,620,214. Define the old families explicitly: P={(a,b):ab<T}; H={(a,b):a in U or b in U}; ZZ={(a,b):lcm(a,b)<N}; Y={(a,b):33 ceil(N/a)>b or 33 ceil(N/b)>a}. Then E=P union H union ZZ union Y. U is the inherited disjoint 552-port family from PREFIX-895: the sixteen PREFIX-891 first-port members S, twenty-four odd single-axis obstruction moduli satisfying a | (2^h±1) for some 1<=h<32, and the two 256-member strips 400011..400521 and 480011..480521 (step 2). All sets here are exactly typed and finite.

## 2. New 64-row panel and a symmetry-lift counting theorem

Define the row panel R={510001+194j: j=0,...,63}, so |R|=64. An exhaustive integer membership check confirms R subset Q\U. Define D={(a,b) in R x Q : (a,b) not in E, and ZF_32(a,b)>0}, where ZF denotes a zero-step versus a named flip collision.

**Theorem 898-A (overlap-free panel/transposed-panel lift).** E is symmetric under swapping ports. The time-reversal involution (u,v,i) -> (v,u,i) preserves legal named zero/one-flip trajectories, and hence existence of ZF collisions under swapping a,b. Thus D^T is exactly as collision-certified and disjoint from E. Consequently

    |E union D union D^T| = |E| + 2|D| - |D intersect D^T|.

**Proof.** The map preserves Z and F trajectory types, since XOR is involutive, and exchanges the two observations. The sets P,H,ZZ,Y are symmetric. D and its transpose avoid E by construction. Inclusion-exclusion then gives the formula without double-counting any previously certified pair. QED.

## 3. Exact zero/flip endpoint decision and constructive witness

For odd a,b>1, if gcd(a,b)>1, no ZF collision exists: the common odd divisor would divide the single-bit difference ±2^i. Otherwise let r_i=(2^i * a^{-1}) mod b, 1<=r_i<b. A ZF collision exists iff for at least one i in {0,...,31}, either

    r_i*a <= N-1  [downward witness],
    or (b-r_i)*a + 2^i <= N-1  [upward witness].

This is the established PREFIX-891 endpoint-complete criterion, reused without novelty claim. In the first case set u=N-1, x=u-r_i*a and take (Z_x,F^i_u); in the second set u=N-1-2^i, x=u-(b-r_i)*a. Both constructed pairs satisfy x mod a = u mod a and x mod b = (u XOR 2^i) mod b. The proof of endpoint completeness uses the maximal admissible u for each source-bit sign, positive first-port shift k, the smallest positive residue of k modulo b, and complementation to account for a negative shift. The accompanying C++ program verifies the source bit, range, pair distinctness and both residues for every counted successful input.

## 4. Exhaustive finite census of D and its transpose

The exact checker enumerates all 64*131072 = 8,388,608 ordered pairs (a,b) in R x Q. Prior E membership is tested directly in the declared priority P,H,ZZ,Y. For each remaining pair the endpoint criterion is checked over all 32 named bits. Every successful input produces an actual legal witness; every such positive input is independently checked by the same program with ports reversed.

Previous-family classification within the panel: P=399,605; H outside P=35,008; ZZ outside P,H=72,240; Y outside P,H,ZZ=540. Total old-covered 507,393, leaving 7,881,215 previously uncovered pairs.

Among the previously uncovered 7,881,215 pairs, |D|=3,484,675, with downward first witnesses 1,760,251 and upward first witnesses 1,724,424. The exact R x R intersection |D intersect D^T|=1,930. Therefore 2*3,484,675-1,930 = **6,967,420** NEW different ordered modulus pairs are certified outside the four-family PREFIX-897 set. The revised exact five-family certificate is

    7,567,620,214 + 6,967,420 = 7,574,587,634,

and this specified union leaves 17,179,869,184-7,574,587,634=**9,605,281,550** ordered modulus pairs unresolved by these families. These figures are relative to this explicit four-family predecessor and should not be described as globally deduplicated against every unrelated historical certificate.

A directly checked first new witness is (a,b)=(510001,277929), x=2539033852, u=4294967295, i=27: Z_x and F^27_u are distinct and have first-port residue 248874 and second-port residue 152437. This input obeys ab>=T, lcm(a,b)>=N and both fiber inequalities fail, and neither port is in U.

## 5. Reproducibility and independent crosscheck

Full reproducible C++17 finite enumerator (every 64-row result, intersection, witness checks and assertions): research_notes/portable_direct/PREFIX898_R6_EXACT_ZF_OVERLAP_PANEL.cpp. Run from that folder:

    g++ -O3 -std=c++17 -Wall -Wextra PREFIX898_R6_EXACT_ZF_OVERLAP_PANEL.cpp -o prefix898
    ./prefix898 > PREFIX898_R6_EXACT_ZF_OVERLAP_PANEL_RESULTS.json

The committed JSON result includes every one of the 64 row counts, global tallies, actual witness and scientific source pin. The exact source C++ locally compiled and ran (about 1.6 seconds on this local runner), all assertions passed; the connector-published code blob was checked against the original local git-hash. No floating point or random sampling enters the finite census.

An independently authored Python program using built-in pow(a,-1,b) and pow(2,i,b), math.gcd, a separate definition of the old sets, and direct witness modulus comparison checked **eight whole first-port rows** (every eighth of the 64), 1,048,576 candidate pairs in total, with zero disagreements. This is partial independent algorithmic crosschecking, not a second complete 64-row scan. Files: PREFIX898_R6_INDEPENDENT_SAMPLE.py and PREFIX898_R6_INDEPENDENT_SAMPLE_RESULTS.json.

Observed exact independent row triplets (a, previous-uncovered, new ZF hits): (510001,122031,66268), (511553,123057,57061), (513105,121631,35115), (514657,119279,54202), (516209,124300,67038), (517761,124710,44806), (519313,124777,67041), (520865,125532,53985).

## 6. Information carrier and remaining frontier

The BRC carrier explicitly retains named source bit, transition type, directed endpoint states and both observation ports; the endpoint shortcut is an existence test, not a proof of equality of entire fibers or observation-preserving compression for arbitrary future operators. This is an auxiliary discrete finite observer. P000 remains the locked six-dimensional native spatial relation space with separately typed time, and no two-coordinate formula has been promoted to a complete three-dimensional slice or physical time-dynamics claim.

Next: on the 64-row panel, apply the already published anchored-FF and general-FF carry/CRT checks to pairs still outside E union D union D^T; examine whether any entire first-port row can be certified or whether a genuinely collision-free candidate survives. Then broaden or parameterize the panel while maintaining explicit union deduplication. The fixed odd-observer mother goal remains B_fix,odd(32) in {19,20}. No Result/Review or Foundation promotion is claimed.
