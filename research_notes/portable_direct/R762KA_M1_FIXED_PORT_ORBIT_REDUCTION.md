# R762KA — Exact one-inactive-Port orbit reduction and 15-profile stratification

Date: 2026-11-23. Scientific scope: unsigned six-axis composite Port–Euler observer, one inactive Port. Author-side exact combinatorial theorem; independent review **NOT_REVIEWED**.

Predecessor: R762JZ at `8dcd3e1a56d6db0b1608634177d3588d2a6f32fb:research_notes/portable_direct/R762JZ_M0_UNIVERSAL_42_THEOREM.md`, Draft PR #3004. Source P000 V5 and GLOBAL_KNOWLEDGE P000 V4 are held unchanged. Formal task context: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, not claimed by this scientific note.

## Typed model and result

Let `A={0,1,2,3,4,5}`, composite Port vertices `P=C(A,2)`, and 20 triadic support colors `S=C(A,3)`. Color `abc` permits edges between pair Ports `ab,ac,bc`. Fix inactive Port `m={0,1}`; only 14 remaining Ports may carry an Euler walk. Precisely the four colors `F={012,013,014,015}` are degenerate: each has **one** permitted edge, `0c--1c`; the other 16 colors retain three permitted edges.

A target specification is a disjoint ordered pair `(D,T)` of subsets of S with `|D|=5`, `|T|=7`. Declare multiplicity 1 for colors D, multiplicity 3 for T, multiplicity 2 for the other 8 colors. Its total event count is exactly `5+21+16=42`. This is a target inventory and does not assert an Euler circuit exists.

**Theorem KA.1 (exact orbit counts).** Fixing m, the group `H=Stab_{S6}(m)=S2 x S4` of order 48 partitions all `C(20,5) C(15,7)=99,768,240` labeled target inventories into exactly

```
426 orbits on D alone,
2,094,150 orbits on (D,T).
```

The 426 D orbits contain, respectively, 124, 189, 93, 18 and 2 classes with 0, 1, 2, 3, and 4 singleton colors in F. Their orbit-size distribution is `{4:2,8:2,12:34,24:148,48:240}`; weighted sum 15,504.

**Theorem KA.2 (joint profile counts).** Put `d=|D∩F|`, `t=|T∩F|`. Then `d,t>=0`, `d+t<=4`, giving **15** exact symmetry-invariant profiles. The following are numbers of H orbits, not numbers of valid Euler circuits:

| d | t | labeled specifications | H-orbits |
|---:|---:|---:|---:|
| 0 | 0 | 1,441,440 | 30,710 |
| 0 | 1 | 8,072,064 | 169,658 |
| 0 | 2 | 12,108,096 | 254,002 |
| 0 | 3 | 5,765,760 | 121,370 |
| 0 | 4 | 720,720 | 15,470 |
| 1 | 0 | 5,765,760 | 121,370 |
| 1 | 1 | 20,180,160 | 422,040 |
| 1 | 2 | 17,297,280 | 361,830 |
| 1 | 3 | 3,603,600 | 76,060 |
| 2 | 0 | 5,765,760 | 121,280 |
| 2 | 1 | 11,531,520 | 241,400 |
| 2 | 2 | 4,324,320 | 91,075 |
| 3 | 0 | 1,647,360 | 34,960 |
| 3 | 1 | 1,441,440 | 30,630 |
| 4 | 0 | 102,960 | 2,295 |
| **Total** | | **99,768,240** | **2,094,150** |

For each profile, the labeled count has the independent closed expression

```
L(d,t) = C(4,d) C(16,5-d) C(4-d,t) C(11+d,7-t).
```

## Proof by Burnside and exact coefficient extraction

The subgroup H has 48 elements: permutations preserving {0,1} setwise. Its action on the 20 colors preserves F. For any `h∈H`, let `O(h)` be the cycles of h on S, each of length `l`; a cycle lies entirely inside F or outside it.

A coloring of S by singleton `D`, triple `T`, or double `R` is fixed precisely if every h-cycle is monochromatic. Therefore the fixed target count is the coefficient

```
[x^5 y^7] product_{O ∈ O(h)} (1+x^|O|+y^|O|).
```

For each forced-color profile, replace each factor by
`(1+x^l u^(f l)+y^l v^(f l))`, where f=1 for cycles inside F and f=0 otherwise; take `[x^5 y^7 u^d v^t]`. The action preserves the prescribed edge legality and the inactive Port. Burnside's lemma then gives the orbit count after division by 48.

The seven possible induced color-cycle signatures and exact fixed-target numbers are:

| cycle signature on 20 colors | H elements | fixed targets per element |
|---|---:|---:|
| 1^20 | 1 | 99,768,240 |
| 1^8 2^6 | 7 | 95,040 |
| 1^4 2^8 | 9 | 9,520 |
| 1^2 3^6 | 8 | 0 |
| 1^2 3^2 6^2 | 8 | 0 |
| 2^2 4^4 | 12 | 0 |
| 2^10 | 3 | 0 |

Hence `(99,768,240 + 7*95,040 + 9*9,520)/48 = 2,094,150`. The weighted extraction above yields all 15 profile counts in the table. Applying the same argument to `[x^5] product(1+x^l)` yields 426 D-orbits. The separate exact script enumerates all 15,504 D directly and verifies both this count and the forced-profile distribution.

## Consequence, boundary and next research

R762JZ's 43-orbit classification is valid when all 15 Ports are active and the full S6 symmetry acts. Marking one inactive Port breaks that symmetry to H, so applying those 43 orbits unchanged is unjustified. The correct exact workload is 426 D representatives and, if T-stabilizers are also reduced, 2,094,150 joint representatives. Across all 15 possible inactive Ports, S6-conjugacy gives the same 2,094,150 orbit types; the total labeled (inactive Port,D,T) specifications are `15*99,768,240=1,496,523,600`.

This is a **symmetry and inventory classification only**. It proves neither existence nor nonexistence of an Euler witness in any profile; it does not infer signed native P000 triadic legality, full X6 Cell/Link/Port dynamics, source path order, nor BRC residual descent from the unsigned graph quotient. The symmetry quotient is used only for checking predicates which are demonstrated invariant under H; do not delete labeled source histories or joint directions.

**Next:** Build and verify a representative-level 42-event constructor with the four forced color edges, separately reporting legal endpoint counts, vertex positive-even degree, connectivity, and any exact failed case. Prioritize the smallest 2,295-orbit profile (d=4,t=0), then extend to the remaining profiles. On any apparent counterexample, independently check full event feasibility before inferring failure of a particular constructor.

## Reproduction and evidence

`R762KA_M1_BURNSIDE_VERIFY.py` computes the cycle classes, weighted Burnside coefficients, 15 profiles, labeled multinomial counts, and an independent direct D-orbit check, using exact integer arithmetic only. Reproduction: `python R762KA_M1_BURNSIDE_VERIFY.py` in Python >=3.10; prints total counts and writes `R762KA_M1_BURNSIDE_EVIDENCE.json`. Local author-side run: PASS, with 7 cycle classes, 15 profiles, 426 D-orbits, 2,094,150 joint orbits, 99,768,240 labeled targets. Independent mathematical review: NOT_REVIEWED.
