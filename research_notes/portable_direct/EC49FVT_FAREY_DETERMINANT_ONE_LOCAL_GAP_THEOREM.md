# EC49FVT — Exact determinant-one bottlenecks in the 11-adic certified rational-phase mesh

Date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECKED / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED. Frozen scientific input: BRC16943, unchanged. Parent: awdawmip/enterprise-math@cb3e0734b50b1ac302b005dbf307455e22880e08:research_notes/portable_direct/EC49FVS_DIVISOR_SATURATION_PHASE_MESH_THEOREM.md. This is a derived rational Bernoulli phase-observer calculation; P000 and X6 native semantics are unchanged.

## Statement and exact local formula

Use the inherited *complete projective mod-11 no-root* predicate C11(h,n) for positive integers, equivalently

    C11(h,n) = [(h mod 10,n mod 10) belongs to P] AND [(9h+10n) mod 11 != 0],

where P is the 44-pair mod-10 set reconstructed from the projective finite-field formula by the attached verifier. Define the **full certificate set**, not a selected-denominator submesh,

    S_H = {h/d : 0<h<d<=H, gcd(h,d)=1, C11(h,d-h)}.

For an integer H>=11, let m=floor((H-1)/2), and define

    L = max{a: 1<=a<=m, C11(a,a+1)},
    R = max{a: 1<=a<=m, C11(a+1,a)},
    N = max{n: 1<=n<=H-1, C11(1,n)},
    A = max{a: 1<=a<=H-1, C11(a,1)}.

**Theorem.** All four maxima exist. Write qL=2L+1, qR=2R+1, q0=N+1, q1=A+1. The two *consecutive* members of S_H straddling the uncertified rational 1/2 are exactly

    x_minus=(qL-1)/(2qL),       x_plus=(qR+1)/(2qR).

The first and last certified fractions are

    min S_H=1/q0,              max S_H=1-1/q1.

Their denominators satisfy

    H-5<=qL,qR<=H,   H-4<=q0<=H,   H-5<=q1<=H.

Consequently the exact certified gap across 1/2 is

    Ghalf(H) = 1/(2qL)+1/(2qR),   1/H <= Ghalf(H) <= 1/(H-5),
    lim_(H -> infinity) H*Ghalf(H) = 1.

The two endpoint gaps also satisfy

    1/H <= min S_H <= 1/(H-4),
    1/H <= 1-max S_H <= 1/(H-5).

These three distinguished bottlenecks have the sharp leading constant 1 in the scale 1/H, a new result orthogonal to the predecessor's global covering upper constant 1365/506.

## Exact finite certificate

C11 is separately periodic mod 110 in h,n because of its mod-10 and mod-11 clauses. Complete residue scans for a=0,...,109 yield:

| Residue predicate | Accepted of 110 | Largest cyclic step between accepted residues |
|---|---:|---:|
| C11(a,a+1) | 80 | 3 |
| C11(a+1,a) | 80 | 3 |
| C11(1,a) | 50 | 5 |
| C11(a,1) | 50 | 6 |

The companion program reconstructs P from the *original* projective expressions, including the collision point z=3; it verifies simplified vs direct tests for all 12100 positive exponent pairs 1<=h,n<=110, then verifies these four exhaustive residue certificates. It also checks C11(1,1)=false.

## Proof

1. In a periodic accepted-residue set with cyclic step at most g, the last accepted residue not exceeding a sufficiently large integer cutoff M is at least M-(g-1). For the first two rows set M=floor((H-1)/2), obtaining L,R>=M-2, so qL,qR>=H-5. For the third and fourth rows set M=H-1, obtaining N>=H-5 and A>=H-6; hence q0>=H-4 and q1>=H-5. Direct low residues ensure nonempty sets for H>=11.
2. Fractions L/(2L+1) and (R+1)/(2R+1) are reduced since adjacent integers are coprime. Their respective integer signed determinants 2h-d relative to 1/2 are -1,+1, so their distances to 1/2 are 1/(2qL),1/(2qR). They are the closest determinant-one certified fractions, since their admissible denominators are maximal.
3. Any other candidate h/d (d<=H) with |2h-d|>=2 has distance |2h-d|/(2d)>=1/H. Since qL,qR>H/2 at H>=11, both chosen candidates have distance <1/H. Thus they are the immediate certified neighbors. The reduced center 1/2 is uncertified, giving an *actual consecutive gap* of the stated exact length.
4. The candidate 1/q0 is certified. Every fraction with numerator >=2 has value >=2/H; q0>H/2 shows it is larger than 1/q0. Similarly every candidate with co-numerator d-h>=2 lies at least 2/H below 1, so 1-1/q1 is the largest certified fraction.
5. Substitute the four proven denominator bounds into the exact gap formulas. The limit follows by squeezing.

Unlike the earlier 65-denominator residue-mask construction, this argument uses the integer determinant and the preserved primitive numerator/co-numerator of the **entire** certificate set.

## Global Farey experiment and open question

The independent ascending Farey enumerator visits every reduced h/d with d<=H, filters by C11 and computes the exact maximum gap including 0 and 1:

| H | H × global maximum gap | Witness |
|---:|---:|---|
| 128 | 16128/15875 | 63/127 to 63/125 |
| 256 | 256/255 | 0 to 1/255 |
| 512 | 512/509 | 0 to 1/509 |
| 1024 | 1024/1023 | 511/1023 to 512/1023 |
| 2048 | 4190208/4186115 | 1023/2047 to 1023/2045 |
| 4096 | 4096/4095 | 0 to 1/4095 |
| 8192 | 8192/8189 | 0 to 1/8189 |

This motivates, but does not prove, the **global conjecture**

    lim_(H -> infinity) H * max_gap(S_H union {0,1}) = 1.

The rigorous current global upper bound remains 1365/506 from EC49FVS. A useful next route is a uniform primitive Farey-neighbor classification by signed determinants bh-ad for all small-denominator rational anchors, including coprimality and endpoint controls.

## Reproduction and provenance

Run the attached standard-library CPython3 verifier: 12100 projective crosschecks; four complete period-110 scans; theorem assertions at all H=11..1000; independent full reduced-fraction enumeration at H=11..180; seven complete Farey scans through H=8192. Output terminates ALL PASS. These finite computations audit the theorem; the infinite result uses the periodic-residue proof.

The Bernoulli-to-projective reduction, U/Gamma constants and frozen BRC16943 scientific inputs are inherited; separate mathematical Review, formal Result and admission remain outstanding. Research identity, RA/CLAIM and GitHub publication are tracked separately.
