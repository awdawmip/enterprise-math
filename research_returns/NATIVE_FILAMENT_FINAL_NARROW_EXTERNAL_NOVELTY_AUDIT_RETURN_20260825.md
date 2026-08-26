# Native Filament Final Narrow External Novelty Audit — Return

Task-ID: `RS-NATIVE-FILAMENT-FINAL-NARROW-EXTERNAL-NOVELTY-AUDIT`

Audit date: `2026-08-26`

Owner branch: `audit/native-filament-final-narrow-novelty-20260825`

Auditor: `OpenAI ChatGPT / GPT-5.6 Sol — independent external-literature auditor`

Literature-search cutoff: `2026-08-26`

## 1. Independence attestation

Before freezing this return I read only the governing taskbook and the allowed blind statement packet inside the repository:

- `research_tasks/NATIVE_FILAMENT_FINAL_NARROW_EXTERNAL_NOVELTY_AUDIT_20260825.md`;
- `research_inputs/NATIVE_FILAMENT_FINAL_NARROW_NOVELTY_BLIND_PACKET_20260825.md`.

I did **not** read PR #627, PR #632, branch `research/native-filament-generalization-theorem-package-20260824`, originating-researcher novelty opinions, package-specific proofs, or package-specific checkers before this freeze. The mathematical statements F1--F6 were treated as already independently replicated, exactly as required by the taskbook. The only additional inputs used were external literature and bibliographic/search metadata.

This is therefore a theorem-statement/literature-overlap classification, not a proof audit.

## 2. Verdict matrix

| Item | Required verdict | Classification basis |
|---|---|---|
| F1 — punctured split-hyperbola tangent bridge | `KNOWN_IMMEDIATE_COROLLARY` | Standard general-field parabola tangent parametrization and tangent-intersection formulas, followed by affine translation/elimination and the elementary difference-of-squares identification with a split hyperbola. No source located states the exact translated-two-parabola / distinct-tangent / translation-quotient = punctured-hyperbola package as a theorem. |
| F2 — finite-field sign quotient / breaker capacity | `KNOWN_IMMEDIATE_COROLLARY` | The hyperbola is a split rank-one torus/torsor with `q-1` points; a one-orbit action by a group of order four forces `q-1<=4`. This is immediate orbit-stabilizer/Burnside bookkeeping once the packet's correspondence is accepted. |
| F3 — odd-sector Joukowski lane quotient | `KNOWN_IMMEDIATE_COROLLARY` | `Lambda_s(a)=-s(a+c/a)`, `c=(2s)^(-1)`, is a scalar multiple of the standard Joukowski/Dickson two-to-one quotient. The involution `a -> c/a` and its fixed points give the stated image-cardinality formula directly. The centered lane target is package-specific bookkeeping, not a separately located literature theorem. |
| F4 — extremal saturation uniqueness | `NO_DIRECT_MATCH_FOUND` | Extensive Dickson/Joukowski, small-value-set, many-to-one, and prescribed-value-set searches found cardinality/classification results but no theorem classifying equality of this Joukowski image with the specific centered arithmetic-progression target under `q=2s-1` or `q=2s+1`, and no match to the `q|75` / `q|21` obstruction pattern. |
| F5 — longitudinal/transverse unique boundary closure | `NO_DIRECT_MATCH_FOUND` | Covering-system, arithmetic-dynamics and finite-field searches found no theorem coupling `k_*=2q_b-1` with the transverse pair `2s-1,2s+1` in the packet's simultaneous boundary equations. The displayed uniqueness is elementary algebra from the packet's assumed bounds, but no external theorem statement subsuming the exact matching was located. |
| F6 — final coupled selection statement | `NO_DIRECT_MATCH_FOUND` | Searches coupling parabola tangent incidence, split-torus quotients, Joukowski/Dickson value sets, centered-lane saturation and boundary capacity found no direct theorem statement. Literature covers the components in separate theories; no source located ties them to one geometry-selected scalar in the packet's way. |

### Package-level verdict

`KNOWN_COMPONENTS_ONLY`

Interpretation: F1--F3 lie at immediate-corollary/specialization strength relative to standard literature. F4--F6 were not directly subsumed by any theorem statement located in the audited literature set. Therefore the strongest permitted package-level literature sentence is:

> `NO DIRECT THEOREM-STATEMENT MATCH FOUND IN THE AUDITED LITERATURE SET`.

This sentence is a bounded search result only. It is **not** a priority, publication-originality, or first-occurrence claim.

## 3. Exact source mapping

### Source S1 — general-field parabola tangent parametrization

S. C. Choi and N. J. Wildberger, **The Universal Parabola**, *KoG* 22 (2018), DOI `10.31896/k.22.4`.

Relevant material: the paper develops the parabola over a general field of characteristic not two. In its standard parametrization, a point is written in parameter form and the corresponding tangent is given explicitly; the external point obtained from the tangents at two parameters has coordinates expressed by their product and sum. The paper also develops pole/polar and tangent geometry in this parametrization.

Mapping to F1:

- hypothesis `char(K)!=2`: matches the general-field setting used for the tangent formulas;
- translated copies of one parabola: obtained by an affine vertical translation of the standard model;
- concurrency of two tangents from one translate and one tangent from the other: obtained by substituting the standard tangent/intersection formula into the translated third tangent equation;
- hyperbola representation: then follows by the packet's elementary affine change of variables/difference-of-squares factorization;
- distinctness `u!=v`: becomes the deletion of the corresponding diagonal locus after the translation quotient.

What S1 does **not** provide: the exact two-translated-parabola statement, simultaneous-translation quotient, or theorem identifying that quotient specifically with `H_(B,C_i)\Delta_i`.

Verdict consequence: F1 is best classified as `KNOWN_IMMEDIATE_COROLLARY`, not as a direct theorem located in S1.

### Source S2 — split rank-one torus and finite-group orbits

Standard algebraic-torus fact: `G_m(F_q)=F_q^*` has `q-1` points, and a nonzero split hyperbola `ab=const` is a torsor/rescaling of `G_m`. Standard finite-group orbit-stabilizer/Burnside theory bounds every orbit of a group `G` by `|G|`.

A general reference for split tori is V. E. Voskresenskiĭ, **Algebraic Groups and Their Birational Invariants**, Translations of Mathematical Monographs 179, AMS, 1998. Burnside/orbit-stabilizer is a standard finite-group result and is explicitly conceded by the blind packet.

Mapping to F2:

- `R` is carried by `(x,y)->(y-x,y+x)` to a nonzero split hyperbola;
- therefore `|R|=q-1`;
- the independent sign group has order four;
- one orbit therefore implies `q-1<=4`, hence `q<=5`.

No nonstandard theorem is needed after the packet's correspondence is fixed. F2 is `KNOWN_IMMEDIATE_COROLLARY`.

### Source S3 — Dickson value-set cardinality

W.-S. Chou, J. Gomez-Calderon, and G. L. Mullen, **Value sets of Dickson polynomials over finite fields**, *Journal of Number Theory* 30(3) (1988), 334--344, DOI `10.1016/0022-314X(88)90006-6`.

The paper determines the cardinality of Dickson-polynomial value sets over finite fields. This is the classical value-set reference most directly adjacent to the packet's conceded Dickson/Joukowski component.

### Source S4 — two-to-one mappings over finite fields

S. Mesnager and L. Qu, **On Two-to-One Mappings Over Finite Fields**, *IEEE Transactions on Information Theory* 65(12) (2019), 7884--7895, DOI `10.1109/TIT.2019.2933832`; preprint `arXiv:1907.01066`.

Relevant material: systematic two-to-one criteria and constructions, including classical polynomial classes such as Dickson polynomials.

Mapping to F3:

- `Lambda_s(a)=-s(a+c/a)` is a degree-two/Joukowski-type quotient on `F_q^*`;
- its equality fibers are the orbits of `a -> c/a`;
- fixed points satisfy `a^2=c`, so their number is `1+chi(c)`;
- hence the number of orbits, and therefore the image size, is `((q-1)+(1+chi(c)))/2=(q+chi(c))/2`.

This is immediate involution-orbit counting. S3/S4 do not state the packet-specific centered lane set `J_s`, nor do they classify the inclusion/equality with that target. F3 is therefore `KNOWN_IMMEDIATE_COROLLARY` rather than `KNOWN_DIRECT_THEOREM`.

### Source S5 — rational functions with small value sets

D. Bartoli, H. Borges, and L. Quoos, **Rational functions with small value set**, *Journal of Algebra* 565 (2021), 675--690, DOI `10.1016/j.jalgebra.2020.08.039`.

Relevant material: the paper studies rational functions on `P^1(F_q)` with small value sets. Its introductory Theorems 1.1--1.2 relate very small/minimal value-set behavior, under stated hypotheses, to the corresponding function-field extension being Galois.

Overlap with F3/F4: strong on value-set cardinality and structural/Galois constraints. Missing: equality with a prescribed centered arithmetic progression, the dependence `c=(2s)^(-1)`, or the extremal relations `q=2s+-1`.

### Source S6 — prescribed sets for minimal-value-set polynomials

H. Borges and L. Reis, **Minimal value set polynomials**, *Advances in Mathematics* 482 (2025), Article 110627, DOI `10.1016/j.aim.2025.110627`; preprint `arXiv:2508.07113`.

Relevant material: the paper asks which subsets `S subseteq F_q` occur as value sets of minimal-value-set polynomials and classifies substantial families, with affine subspaces fundamental; it also gives further classification results and a general conjectural framework.

Overlap with F4: this is a particularly close recent source because it treats the *shape of the target set*, not merely its size. Missing: the packet's rational Joukowski map on `F_q^*`, the centered consecutive-residue target `J_s`, and the extremal parameter coupling `q=2s+-1`.

### Source S7 — 2025 monodromy treatment of small value sets

X. Deng, B. Xu, and Q. Zhu, **The small value set polynomials over finite fields and monodromy groups**, *Journal of Number Theory* 276 (2025), 139--161, DOI `10.1016/j.jnt.2025.03.008`.

Relevant material: monodromy/Galois methods for polynomials with small value sets, including classification consequences for minimal-value-set polynomials.

Missing for F4/F6: prescribed centered arithmetic-progression images, Joukowski involution parameters, parabola tangent incidence, and the packet's boundary equations.

### Source S8 — rational-function arithmetic progressions

G.-D. Hong and Z. L. Lim, **Three Term Rational Function Progressions in Finite Fields**, *International Mathematics Research Notices* (2025), `rnaf118`, DOI `10.1093/imrn/rnaf118`; preprint `arXiv:2401.01137`.

Relevant material: counts three-term configurations `x, x+F(y), x+G(y)` in subsets of `F_p` using rational functions.

Why it is only a false positive for F4: it concerns occurrence/counting of arithmetic-progression-like configurations generated by rational functions, not equality of a rational function's entire image with a prescribed arithmetic progression.

### Source S9 — covering systems

P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, and M. Tiba, **The structure and number of Erdős covering systems**, *Journal of the European Mathematical Society* 26 (2024), 75--109, DOI `10.4171/JEMS/1357`.

Relevant material: structure and enumeration of covering systems of the integers.

Missing for F5: there is no Joukowski/Dickson transverse boundary, no breaker-coprime capacity `k_*=2q_b-1`, and no simultaneous equations matching `k_*-4,k_*-2` to `2s-1,2s+1`.

### Source S10 — covering systems over global function fields

H. Li, B. Wang, C. Wang, and S. Yi, **On Erdős covering systems in global function fields**, *Journal of Number Theory* 266 (2025), 269--280, DOI `10.1016/j.jnt.2024.07.002`; preprint `arXiv:2402.03810`.

Relevant material: covering-system analogues and nonexistence bounds in global function fields.

Missing for F5: the packet's longitudinal/transverse finite-field/Joukowski matching mechanism.

### Source S11 — odd-modulus covering systems

C. Bispels, M. Cohen, J. Harrington, J. Lowrance, K. Pontes, L. Schaumann, and T. W. H. Wong, **A further investigation on covering systems with odd moduli**, preprint `arXiv:2507.16135`; journal metadata surfaced for *Discrete Mathematics* 349(7) (2026), Article 115013.

Relevant material: variants of the odd covering problem.

Missing for F5: again, no value-set/Joukowski boundary pair and no capacity relation of the packet's form.

### Source S12 — a geometry/value-set bridge that still does not match F6

S. Fukasawa, **Galois points and rational functions with small value sets**, preprint `arXiv:2111.06113` (2021).

Relevant material: connects plane-curve Galois points to rational functions with small value sets and separated-variable curves under group-theoretic hypotheses.

Why it is a close false positive for F6: it genuinely couples algebraic geometry and rational-function value sets, but the geometric side is Galois-point/plane-curve structure rather than translated-parabola tangent incidence; it has no centered Joukowski lane saturation or `s=3` boundary closure.

## 4. F1--F6 overlap analysis

### F1 — `KNOWN_IMMEDIATE_COROLLARY`

**Direct subsumption searched for:** a theorem simultaneously containing two translated parabolas, two distinct tangents on one copy, one tangent on the other copy, quotient by simultaneous translation, and identification of the resulting parameter space with a split hyperbola minus a diagonal locus.

**Found:** S1 gives the underlying general-field tangent parametrization and intersection formulas. Standard conic duality and split-hyperbola algebra supply the other conceded pieces.

**Not found:** a source stating the full F1 theorem package directly.

**Classification reason:** after S1, the packet's bridge requires only affine translation, elimination and the stated elementary change of variables. This is exactly the strength represented by `KNOWN_IMMEDIATE_COROLLARY`.

### F2 — `KNOWN_IMMEDIATE_COROLLARY`

**Direct subsumption searched for:** a named theorem identifying the packet's common-dual-value quotient and deriving the `q<=5` breaker capacity.

**Found:** the split-torus count `q-1` plus standard orbit-stabilizer/Burnside.

**Not found / not needed:** a specialized theorem. Once the group has order four and the set has `q-1` points, the bound is immediate.

**Classification reason:** no external originality content remains in the numerical implication after the packet's correspondence is accepted.

### F3 — `KNOWN_IMMEDIATE_COROLLARY`

**Direct subsumption searched for:** the precise map `Lambda_s`, its involution quotient, exact image cardinality, and its centered-lane saturation criterion.

**Found:** S3 and S4 cover the Dickson/Joukowski value-set and two-to-one framework. The exact image formula follows from the fixed points of `a -> c/a`.

**Not found:** a literature theorem formulated using `J_s` or the package's central-packet language.

**Classification reason:** the quotient/cardinality is a direct specialization; the target-set condition is package-specific bookkeeping. Therefore `KNOWN_IMMEDIATE_COROLLARY` is stronger and more accurate than `KNOWN_COMPONENTS_ONLY` for the mathematical core of F3.

### F4 — `NO_DIRECT_MATCH_FOUND`

Closest sources and why none subsumes F4:

1. **S3 (Chou--Gomez-Calderon--Mullen 1988):** determines Dickson value-set cardinality, not equality with a prescribed centered arithmetic progression and not the extremal constraints `q=2s+-1`.
2. **S5 (Bartoli--Borges--Quoos 2021):** characterizes structural/Galois behavior of rational functions with very small value sets, but does not prescribe the image as `J_s` or derive the packet's `q|75`, `q|21` obstructions.
3. **S6 (Borges--Reis 2025):** directly studies which sets can occur as minimal polynomial value sets; nevertheless its maps are polynomial MVSPs, and the classifications do not state the packet's Joukowski image/centered-interval equality under `q=2s+-1`.
4. **S7 (Deng--Xu--Zhu 2025):** recent monodromy classification work on small polynomial value sets, again without the specified arithmetic-progression target or extremal Joukowski coupling.
5. **S8 (Hong--Lim 2025):** concerns rational-function progressions inside subsets of finite fields, not the full value set of `a+c/a` being a specified progression.

Exact searches for the obstruction fingerprints `q divides 75`, `q divides 21`, `75` with `2s-1`, and `21` with `2s+1` produced no relevant Dickson/Joukowski theorem match.

Uncovered statement: the specific equality/inclusion problem for `Im Lambda_s` against `J_s` at the two prime extremal boundaries, together with the resulting uniqueness of `s=3`.

Guard: this uncovered status is only `NO_DIRECT_MATCH_FOUND`; it is not a publication-originality claim.

### F5 — `NO_DIRECT_MATCH_FOUND`

Closest sources and why none subsumes F5:

1. **S9 (Balister et al. 2024):** deep structural results on covering systems, but no finite-field value-set boundary or packet-style capacity matching.
2. **S10 (Li--Wang--Wang--Yi 2025):** covering systems in global function fields, but no `k_*=2q_b-1` / `2s+-1` simultaneous closure.
3. **S11 (Bispels et al. 2025/2026):** odd-modulus covering-system variants, but no Joukowski transverse lane or longitudinal breaker capacity.

Searches in arithmetic dynamics and deterministic/arithmetic percolation likewise produced no exact counterpart.

Important narrowing: the equations inside F5 themselves do not become externally deep merely because no source states them. Given the packet's assumptions, `q_b=s+2` and the finite solution under `q_b<=5` are routine algebra. The literature-audit residue is only the absence of a located framework that *already couples* the two independently supplied boundary mechanisms.

### F6 — `NO_DIRECT_MATCH_FOUND`

Closest sources and why none subsumes F6:

1. **S1 (Choi--Wildberger 2018):** supplies general-field parabola tangent geometry, but no finite-field Joukowski value-set saturation.
2. **S3/S4 (Dickson/Joukowski and 2-to-1 literature):** supply the finite-field quotient/value-set side, but no translated-parabola tangent incidence selected by the same sector scalar.
3. **S5/S12 (small rational value sets; Galois points):** these connect rational functions to algebraic-curve/Galois geometry, but not to the packet's tangent-concurrence hyperbola, centered lane set, or boundary-capacity equations.
4. **S6/S7 (2025 small/minimal value-set work):** substantially sharpen target-set/monodromy classification, but still do not contain the packet's cross-domain coupling.

Uncovered statement: one scalar fixed by the native tri-sector shell allocation simultaneously controlling F1, F3, F4 and F5 in the exact chain stated in F6.

Guard: the correct external statement is only that no direct theorem-statement match was found in the audited set.

## 5. Search log

### Search interfaces / source families

The audit used a freshness-enabled general web scholarly search interface and followed/indexed results from, among others, arXiv, ScienceDirect/Elsevier, Journal of Number Theory metadata, Advances in Mathematics metadata, IEEE/DBLP metadata, Oxford Academic, EMS Press, KoG/Hrčak, institutional publication repositories, and ResearchGate bibliographic/full-text index pages. Search was executed through `2026-08-26`, including targeted 2025--2026 recency searches.

### Exact or reproducible queries

The following queries were run; quotation marks shown here indicate phrase searches used in the query itself.

#### Conic/parabola tangent geometry

1. `"parabola" tangent concurrence translated parabola hyperbola geometry`
2. `"two parabolas" tangents concurrent hyperbola`
3. `"tangent" parabola parameter t1 t2 intersection coordinates conic`
4. `"intersection of tangents" parabola parameters t1 t2`
5. `"parabola" "tangents at parameters" intersection`
6. `"conic" duality parabola tangent parameter`
7. `"translated parabola" tangent concurrence geometry`
8. `"homothetic parabolas" tangents concurrence`
9. `"The Universal Parabola" tangent parabola`
10. `"Universal Parabola" "Theorem 7" tangents`
11. `"The Universal Parabola" Choi Wildberger 2018 tangent intersection parameters`

#### Split tori / inversion / sign quotients

12. `"split torus" "xy=1" algebraic group`
13. `"one-dimensional split torus" hyperbola xy=1`
14. `"G_m" hyperbola xy=1 inversion Weyl group`
15. `"multiplicative group" hyperbola xy=c finite field q-1 points`
16. `"Burnside lemma" orbit count finite group action finite set`
17. `"sign group" hyperbola finite field orbit`
18. `"algebraic torus" G_m finite field q-1 split torus`

#### Dickson / Joukowski / two-to-one value sets

19. `"Joukowski" finite field x+a/x value set`
20. `"x + a/x" finite field value set cardinality`
21. `"Dickson polynomial" "value set" finite field Chou Mullen Wassermann`
22. `"Dickson polynomials" "value set" formula finite fields`
23. `"Value sets of Dickson polynomials" Chou Gomez-Calderon Mullen`
24. `"Dickson polynomials" "value sets" Mullen Turnwald`
25. `"Dickson polynomials over finite fields" Lidl Mullen Turnwald value set`
26. `"The value set of Dickson polynomials" finite fields`
27. `"2-to-1" rational functions finite fields`
28. `"many-to-one" rational functions finite fields`
29. `"2-to-1 mappings over finite fields" Mesnager Qu`
30. `"two-to-one" mappings finite fields rational functions`
31. `"Joukowski map" finite fields rational function`
32. `"Chebyshev" finite fields x+a/x quotient involution`
33. `"x+a/x" finite field involution image`
34. `"x+a/x" "F_q" involution`
35. `"u+a/u" "finite field"`
36. `"x + a/x" Dickson polynomial finite field`
37. `"x+a/x" Dickson polynomial value set`
38. `"Joukowski" finite field "involution"`
39. `"On two-to-one mappings over finite fields" Mesnager Qu 2019 DOI`
40. `"Value sets of bivariate Chebyshev maps over finite fields" Kucuksakalli 2015`

#### Small/minimal value sets and prescribed target sets

41. `"minimal value set" rational functions finite fields`
42. `"small value set" rational functions finite fields`
43. `"value set" "arithmetic progression" finite field polynomial`
44. `"value sets" "arithmetic progression" finite fields`
45. `"polynomial value set" "arithmetic progression" F_p`
46. `"rational function" "arithmetic progression" finite field image`
47. `"Dickson polynomial" "arithmetic progression" value set`
48. `"Chebyshev polynomial" "arithmetic progression" finite field`
49. `"x+a/x" "arithmetic progression" finite field`
50. `"x+c/x" "arithmetic progression" finite field`
51. `"arithmetic progression" "value set" finite field rational function`
52. `"Dickson" "arithmetic progression" finite field`
53. `"Joukowski" "arithmetic progression" finite field`
54. `"minimal value set polynomials" 2025 finite fields Borges Reis`
55. `"The small value set polynomials over finite fields and monodromy groups" authors`

#### Exact extremal relations / obstruction fingerprints

56. `"q=2s-1" Joukowski finite field`
57. `"q=2s+1" Joukowski finite field`
58. `"q divides 75" Joukowski`
59. `"q divides 21" Joukowski finite field`
60. `"75" "2s-1" finite field`
61. `"21" "2s+1" finite field`
62. `"2s-1" "Dickson" polynomial finite field`
63. `"2s+1" "Dickson" polynomial finite field`
64. `"2s-1" "x+c/x"`
65. `"2s+1" "x+c/x"`
66. `"Dickson polynomial" centered arithmetic progression value set finite field 2025 2026`

#### Arithmetic dynamics / covering / percolation / capacity matching

67. `"deterministic arithmetic percolation" boundary capacity`
68. `"arithmetic percolation" deterministic number theory`
69. `"covering systems" boundary capacity arithmetic dynamics`
70. `"covering system" finite field value set Dickson`
71. `"arithmetic dynamics" Dickson polynomial finite field value set`
72. `"arithmetic dynamics" Joukowski finite field`
73. `"boundary capacity" arithmetic dynamics`
74. `"percolation" Dickson polynomial finite field`
75. `"On Erdős covering systems in global function fields" 2025 Journal Number Theory`
76. `"A further investigation on covering systems with odd moduli" 2026`
77. `"The structure and number of Erdős covering systems" JEMS`

#### Cross-domain coupling searches

78. `"tangent" Joukowski parabola finite field`
79. `"parabola" Joukowski Dickson finite field`
80. `"tangent incidence" "value set" finite field rational function`
81. `"conic" "small value set" rational function finite field`
82. `"parabola" tangent "Joukowski" finite field`
83. `"Joukowski" finite field value set 2025 2026`

## 6. Recommended wording for PR #627

Recommended replacement wording:

> The conic/tangent, split-torus/sign-orbit, and Joukowski/Dickson value-set ingredients used here are standard. In the final narrowed statement, F1--F3 are immediate corollaries or specializations of those classical components. An independent external-literature audit through 2026-08-26 located no direct theorem-statement match for (i) the centered-lane extremal classification at `q=2s+-1`, (ii) the simultaneous longitudinal/transverse boundary matching, or (iii) the full geometry-selected coupling of these mechanisms. The appropriate literature claim is therefore only: `NO DIRECT THEOREM-STATEMENT MATCH FOUND IN THE AUDITED LITERATURE SET`. No priority, first-occurrence, or publication-originality claim is made.

## 7. Claims that must be downgraded

1. **F1:** any claim that the punctured split-hyperbola tangent bridge itself is externally unprecedented must be downgraded to: `KNOWN_IMMEDIATE_COROLLARY` / classical tangent formulas plus elementary affine/torus packaging.
2. **F2:** any claim assigning external originality to the `q<=5` sign-orbit bound must be removed; it is an immediate orbit-size consequence once the correspondence is accepted.
3. **F3:** any claim assigning external originality to the involution quotient or formula `|Im Lambda_s|=(q+chi(c))/2` must be removed; it is a direct Joukowski/two-to-one specialization plus fixed-point counting.
4. **F4:** any claim stronger than `NO DIRECT THEOREM-STATEMENT MATCH FOUND IN THE AUDITED LITERATURE SET` must be downgraded. The audit does not establish priority or publication originality.
5. **F5:** any claim that the final numerical closure is externally deep in itself must be narrowed: the algebraic uniqueness follows routinely from the packet's assumed boundary relations and `q_b<=5`; only the exact *coupling of the two supplied mechanisms* lacked a direct literature match in this audit.
6. **F6 / package:** any `new theorem`, `first`, priority, or equivalent publication-originality language must be removed. The defensible statement is only that the audited literature set contains known components but no direct theorem-statement match for the full coupling.

## 8. Final classification

- F1: `KNOWN_IMMEDIATE_COROLLARY`
- F2: `KNOWN_IMMEDIATE_COROLLARY`
- F3: `KNOWN_IMMEDIATE_COROLLARY`
- F4: `NO_DIRECT_MATCH_FOUND`
- F5: `NO_DIRECT_MATCH_FOUND`
- F6: `NO_DIRECT_MATCH_FOUND`
- Package: `KNOWN_COMPONENTS_ONLY`

Maximum allowed external-literature conclusion:

`NO DIRECT THEOREM-STATEMENT MATCH FOUND IN THE AUDITED LITERATURE SET`

Hard target:

`NATIVE_FILAMENT_FINAL_NARROW_COUPLED_SELECTION_EXTERNAL_NOVELTY_INDEPENDENTLY_CLASSIFIED`

Status: `SATISFIED / RETURN FROZEN IN OWNER BRANCH`
