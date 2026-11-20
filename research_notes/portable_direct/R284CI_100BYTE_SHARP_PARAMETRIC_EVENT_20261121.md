# R284CI — Sharp event-order radius and 100-byte compiled Port-fiber index

Date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED. This is portable independent continuation of frozen R284CH, not a formal Task CLAIM, Result, review, X6-native theorem, or change to P000.

## Exact frozen mathematical input

Keep the prior 34-bit Port observer and no repinning: p=17179869143, D=(1120832,6,13,1651128), Z=(0,390139,394465,1497639). The 65536 candidate matrices have C_ij in {1,2}, with F(C)=det(diag(D)-C-Z_1 E_01-Z_2 E_02-Z_3 E_03) modulo p. The selected six lower coordinates are (C_10,C_11,C_12,C_20,C_21,C_22). For each of 64 keys k let the exact circular covering arc A_k have start a_k and unreduced width w_k as proved in R284CE. Define Sigma_rho(y)={k:dist_circle(y,A_k)<=rho}. Its 128 zero-radius ENTRY/EXIT events and original 976-byte index are those of R284CH.

Frozen science pin: awdawmip/enterprise-math@f16d56afb972886b65d65bb5c0a48cec29bf32cc:research_notes/portable_direct/R284CH_PARAMETRIC_128_EVENT_PORT_INDEX_20261121.md. Full codeword SHA-256 b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4; historical 976-byte index SHA-256 af2d3ec14228af03eb9658a3301c732e3025d69f007e7e971da404f80c5fb155.

## Theorem 1 — 100-byte exact serialized coefficient representation

Let k be a six-bit key and I_m(k)=1 iff (k & m)=m. Both the start modulo p and the exact (unreduced) width satisfy

a_k = sum_{m in T} alpha_m I_m(k) (mod p),    w_k = sum_{m in T} beta_m I_m(k),

with exactly the 13-supported mask set T={0,1,2,4,8,10,12,16,17,20,32,33,34}. The coefficient pairs are the exact six-bit Boolean Moebius transforms of all 64 determinant extremizer pairs; the independently obtained pairs reproduce R284CE exactly. Every alpha lies in [0,p) and therefore fits 34 unsigned bits. beta_0=390497532 fits 29 unsigned bits; the other 12 beta values lie in [-67108864,67108863] and fit 27-bit signed two's complement. A fixed-mask-order little-endian bit stream therefore represents all coefficients exactly in

13*34 + 29 + 12*27 = 795 bits = 100 bytes including five unused high padding bits.

Decode its pairs, synthesize all 64 arcs, sort their 128 ENTRY/EXIT events once, and sweep the labeled 64-bit masks. This reconstructs the identical R284CH 976-byte index and supports eight-comparison binary-search query at any admissible radius. The local checker verifies the exact 976-byte byte stream against its frozen SHA-256. Storage comparison is **100 bytes of persistent coefficient payload versus 976 bytes of persistent compiled event payload**, a factor of 9.76, trading additional startup computation and RAM for persistent bytes. It does NOT count the shared mask set T, fixed observer constants, decoder program, workspace/cached index, or initial construction time. R284CE's zero-per-arc-data alternative remains available.

## Theorem 2 — sharp radius of the fixed 128-event ordering

Let the original sorted events be b_i with motion s_i in {-1,+1}, with ENTRY moving by -rho, EXIT by +rho. In a circular sorted event list, a first order collision as rho grows must come from an adjacent EXIT followed by ENTRY: their gap g closes at rho=g/2. All other adjacent motion patterns have constant or increasing separation. Exhaustively evaluating the 128 exact zero-radius events gives **40** such closing adjacent pairs, the smallest closing gap

g_min=4,226,124,

attained by EXIT key 45 at 6,594,783,455 and the following ENTRY key 8 at 6,599,009,579 (zero-based sorted indices 43,44). The nearest event motion toward the chosen zero cut would reach it only at rho=23,581,912. Hence no event changes order, collides, or crosses the zero cut on the entire *real* interval

0 <= rho < 2,113,062.

Within this interval, the same 128 open-cell masks from rho=0 and the same equality handling (union of the two neighboring masks for a closed arc endpoint) recover Sigma_rho(y) for **every real circular observation y**. The first-collision threshold is sharp for the fixed unchanging event-order template: at rho=2,113,062 its adjacent boundary pair collides. At rho=2,113,063, the explicit test point y=6,596,896,517 yields the former-order lookup mask 0x8100 but the correct direct-circle mask 0x200000008100. This refutes extension of the *same fixed-order template* beyond the collision; it does not rule out rebuilding the index.

The larger radius is an **index correctness range for Sigma_rho**. It does not extend R284CG's exact-codeword signature stability beyond rho<591.5, or full-matrix correction beyond rho<29.5. A coarse fiber signature can vary at higher radius even while it is computed exactly.

## Reproduction / boundaries

Using Python standard-library exact integers and doubled integer positions for half-integer radii, the checker recomputes 64 extremizer arcs and their Moebius coefficients, packs and round-trips all 100 bytes, reconstructs and compares the full prior 976-byte index SHA, checks all 65,536 frozen codewords (SHA-256) and 262,144 exact codeword query cases at rho=0,591,2,113,061,2,113,061.5; checks another 512 exact shifted boundary queries; verifies the closing pair census, exact cut margin, and a concrete post-threshold counterexample. Finite enumerations certify the integers/bit widths/events; the real-radius theorem follows from piecewise-affine event motion and the exact absence of collisions, not from sample-point extrapolation.

Companions: R284CI_compact_extended_event_checker.py and R284CI_compact_extended_event_certificate.json in this directory. The published source is a reproducible author checker, not independent review. The 100-byte coefficient-pack SHA-256 is 61a0f876e1d007231c044894ffa251dce607ea2019a6942d5979ab439094870d.

## Next questions

Benchmark end-to-end time, startup cost, memory including constructed index, and repeated queries, comparing 100-byte compiled coefficients, the R284CH 976-byte precompiled index, the R284CE zero-stored-arc route, and conventional full-codeword search. Explore fixed-order topology past the first collision using local event swaps or dynamic interval structures, while preserving distinct claims for exact query and noise-stable signatures. Investigate direct inversion of the remaining unobserved matrix coordinates without assuming that coarse signatures preserve the complete state or future operations.

Control/provenance: this work records the historical EM-DIRECT-20B766 and RA-617F40704F37299B15489DCA association only as provenance; a currently authenticated session binding and any Activity mutation must be verified separately. No live owner or formal Task CLAIM is assumed.
