# Blind branch assignments: finite classification

Status: exact combinatorial progress; not the final raw freeze and not a reconstruction verdict.

Researcher: EM-HODGEH0O-82EF42. Task: RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-BRANCH-PATTERN-COMPLETION. The actual authorized claim is `chatgpt-rb-blind-20260908-1943ccc582e1463bbcef0c6ab3c7db1b`.

Only the two task-whitelisted mathematical sources at `c73816d3552b4247861e12e476101e94a4a2ce5a` have been read. Their exact whole-file pins are in `source_binding.json`. No originating formula, coefficients, basepoint, twist, period, or replay was used. The historical checker was read, not executed. The earlier exclusion of the six-point block is retained as a cited premise, not rerun.

## 1. Labels and allowed equivalences

Write the elliptic quotient as C: t^2 = R^3 - 3R, with origin O. Its six double-cover branch points are

T = {O, T0=(0,0), Tplus=(sqrt(3),0), Tminus=(-sqrt(3),0)},

Pplus=(-2,i sqrt(2)), Pminus=-Pplus.

These are algebraic-curve coordinates in the task model, not a redefinition of the six native spatial axes. The certificate's branch labels have this exact order. Target labels have order 0, 1, lambda, infinity.

The target branch set at this fixed lambda has automorphism group V4. The exceptional larger groups would require j=0 or j=1728, excluded by the whitelisted frozen j value. The four permutations are the identity and the three double transpositions. They lift to translations by target two-torsion and preserve the elliptic differential. Full S4 is permissible only as a relabeling that also carries lambda through its anharmonic values. It is not 24 automorphisms of the fixed-lambda problem.

The source branch-set automorphism group over the fixed coefficient field is exactly {identity, [-1]}. Here is a proof, including the distinction needed for the ODE. Every automorphism of C has form z -> u z + Q, with u in {1,-1,i,-i}. Since u permutes T=C[2], its image is T+Q. If Q is not in T, this coset has four points disjoint from T and cannot fit into the two-point set {Pplus,Pminus}; hence Q is in T. The remaining pair must map to itself, so u Pplus + Q = epsilon Pplus with epsilon in {1,-1}, and therefore u(2Pplus)=epsilon(2Pplus).

The tangent duplication formula gives the unevaluated exact value x(2Pplus)=-49/8: the slope is 9/(2 i sqrt(2)), its square is -81/8, and subtraction of twice -2 gives the displayed value. This is a paper identity; no quotient or root was numerically evaluated by the checker. In particular 2Pplus is finite with nonzero x, excluding u=+/-i, which negates x. It is not two-torsion: its x is neither 0 nor +/-sqrt(3), as the integer comparison 49^2 != 3*8^2 verifies. Thus Q=+/-2Pplus is not allowed, leaving Q=O and u=+/-1.

The surviving nontrivial source automorphism sends t to -t and exchanges Pplus/Pminus. It preserves the cover branch set and lifts with w -> +/-i w. But it sends the zero divisor t=-k of the fixed differential to t=k. The permitted parent reduction has k != 0, so these divisors are disjoint. Consequently this source involution does not preserve the fixed-k ODE problem up to differential scaling. The fixed-parameter computation retains both partners. No semilinear or Galois quotient is asserted; possible transported-parameter relations have not been used to remove candidates.

## 2. Complete counts

For 4+2+0+0, choosing the pair determines the unlabelled partition: 15 choices. Assignment of its two differently sized occupied blocks to four target labels gives 12 possibilities, hence 180 labelled assignments. For 2+2+2+0 there are 15 perfect matchings of six points, with 24 distinct assignments of three pairs to four labels, hence 360 assignments.

| Equivalence retained | 4+2+0+0 | 2+2+2+0 | Meaning |
| --- | ---: | ---: | --- |
| None | 180 | 360 | All labelled assignments |
| Fixed target V4 only | 45 | 90 | Candidates retained for fixed lambda and fixed k |
| V4 and source sign involution | 33 | 54 | Cover geometry only; not fixed-ODE reduction |
| S4 label transport only | 15 | 15 | Lambda must be transported |
| S4 label transport and source sign | 11 | 9 | Coarse unmarked cover geometry only |

For a direct check of the last line, the source sign fixes seven of the 15 pairs (six pairs inside T, and the Pplus/Pminus pair); the other eight give four orbits. It fixes three matchings (the P pair and one of the three T matchings); the other twelve give six orbits. Thus the two counts are 7+4=11 and 3+6=9.

For the V4-plus-sign line, the identity-source elements give 180 and 360 fixed assignments only for the identity target element. Source sign alone fixes 84 and 72 assignments. A nontrivial target double transposition fixes none even when combined with the source sign, since the four T coordinates of a row would have to be fixed labels. Dividing the two totals by the eight-element group yields 33 and 54. These rational notations are mathematical cardinalities, verified in code through actual orbit construction rather than division evaluation.

## 3. Actual finite certificate and limits

`scripts/check_rb_blind_branch_patterns_20260908.py` constructs the assignments from pairs or perfect matchings. Independently, it enumerates all four-label words of length six and filters their occupancy counts. Exact set equality is checked. Each group action is then checked to partition that set without omitted or overlapping members. The JSON records every representative, orbit size and SHA256 of the complete sorted orbit. A replay recomputes all members.

The actual write run passed with certificate SHA256 `a83524c6b9b8cb6e00561c014e7129c614e9b1c46eedcbd9c9e79f2ff5ee89a0`. The selected static V2 gate passed for this one new script. The computation uses integers, tuples, finite sets, permutations and hashes only. There were zero quotient, remainder, root or BRC evaluations. A native arithmetic migration of the historical SymPy checker is not claimed.

This settles assignment coverage at explicitly stated symmetry levels. It does not show any assignment has a square-class lift, a Riemann--Roch solution, an ODE solution, a basepoint, a degree-six map, or a period normalization. Those are subsequent gates. No raw freeze or unblinding has occurred.
