# R268 — Minimal residue-profile refinement of the six Boolean support classes

Date: 2026-11-18. Research status: AUTHOR_PROVED / EXACT_FINITE_RECURRENCE_CERTIFICATE / NOT_REVIEWED. Domain: fixed seven-source positive-rational auxiliary scalar model, s=67/169, modulus p=13, 63 labelled masks m=0,...,62, integer event k>=3. Frozen scientific input pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.

Provenance: direct continuation from R267 at 740c770d02c19ad4b9ffcb1720a08536ad615446 and its R267_six_price_cost_atlas.py model/recurrence. P000/ACTIVE worldview is unchanged. The results below concern an auxiliary modular observer and make no native typed-BRC equivalence assertion.

## Problem and formal observer

For each labelled source m, let q(m,k) be the integer-scaled source output defined by the R267 recurrence, and r_m(n)=q(m,n+3) mod 13, with n>=0. Its known verified common period is 2184. Define the **Boolean profile** B_m=(1[r_m(n)!=0])_(n>=0) and the **value profile** V_m=(r_m(n))_(n>=0) in F_13.

We seek the coarsest source-label quotient adequate for all future exact modular observations under the operations:
(1) event time advance n -> n+t with t>=0,
(2) translation by an arbitrary fixed a in F_13, and
(3) a zero test after the translation.
The source label, port and branch provenance remain typed fields in any native carrier; the quotient constructed here applies only to this explicitly declared auxiliary observation interface.

## Theorem A — 25 residue-profile classes and two-coordinate fingerprint

For the stated 63 labels:

* The Boolean profiles have exactly **7 distinct classes**, of which the all-zero class has 39 labels.
* The exact F_13 value profiles have exactly **25 distinct classes**. All 24 labels outside the all-zero Boolean class have pairwise distinct value profiles, and the 39 all-zero labels form one value-profile class.
* **The map m -> (q(m,3) mod 13, q(m,4) mod 13) determines the entire infinite profile V_m among these fixed 63 labels.** Equivalently, two masks have the same entire value profile iff their first two residues agree. One coordinate is insufficient on this collection; the exhaustive certificate finds the minimum discriminating prefix length to be exactly two.

Boolean class representatives, class members, and the number of distinct value profiles within each:

| representative | labels in Boolean class | exact value profiles | nonzero phases per period |
|---|---|---:|---:|
| 0 | 0,1,2,3,4,5,6,7,8,11,16,17,18,19,20,21,22,23,28,31,32,33,34,35,36,37,38,39,40,43,48,49,50,51,52,53,54,55,60 | 1 | 0 |
| 9 | 9,14,27,29,41,46,59,61 | 8 | 2028 |
| 10 | 10,25,30,42,57,62 | 6 | 1820 |
| 12 | 12,15,44,47 | 4 | 1872 |
| 13 | 13,45 | 2 | 1638 |
| 24 | 24,56 | 2 | 1456 |
| 26 | 26,58 | 2 | 2016 |

Thus the minimum fixed-length code indexing observable profile types is ceil(log2 7)=3 bits for Boolean support, versus ceil(log2 25)=5 bits for exact F_13 value profiles. These counts are *quotient type identifiers*, not the storage cost of independently retaining the original label, ports, paths or event counter.

### Proof

The frozen seven-source model specifies s=67/169, t(s)=(1691s-2615)/(2615s-3539), seven a_i and b_i, stationary pi_i and rho_i, weights w_j and the exact source expression for q(m,k). The accompanying program computes the first d_m integer-scaled residues directly with Python Fraction arithmetic, where d_m=1+popcount(m), and derives each source's monic integer recurrence from its characteristic polynomial. The 63 recurrence degrees sum to 249, with maximum degree 6.

For each source the program checks equality of the first d_m residues with those shifted by 2184. The monic recurrence then proves r_m(n+2184)=r_m(n) for **every** n>=0, by induction. Consequently exhaustive comparison of one complete 2184-position cycle is exhaustive comparison over the entire infinite time domain.

The program partitions these 63 period-vectors both by their Boolean supports and by their exact F_13 entries, and computes the first prefix length at which the latter partition is fully separated. Its exact finite outputs are the seven Boolean groups displayed above, 25 value groups, and distinguishing prefix length two. Because the model-to-recurrence construction is rational-exact, the period check uses complete d_m initial conditions, and partition comparisons enumerate every declared source, these finite calculations certify the infinite assertions under the stated model.

## Theorem B — Exact factorization criterion for translated-zero future tests

Let the future test family be Q_{t,a}(m)=1[r_m(t)+a=0 in F_13], for all t>=0 and all a in F_13. Then two labels are indistinguishable by **every** test Q_{t,a} iff V_m=V_{m'}.

Proof: equal value profiles plainly agree on every translated-zero test. If V_m differs at some t, take a=-r_m(t). Then Q_{t,a}(m)=1 and Q_{t,a}(m')=0. Thus the 25-profile quotient is both sufficient and minimal for this exact time-shift-and-translation test family. By Theorem A an offline lookup keyed by the first two reference-event residues retrieves the profile type and consequently every future test, with the event index supplied separately.

### Explicit Boolean-collapse obstruction

Labels 9 and 14 have the **same Boolean support profile at all future events**, but at the first reference event k=3 their residues are respectively 8 and 7. Translating by +5 mod 13 yields 0 for source 9 and 12 for source 14. Hence zero-testing after this permitted translation distinguishes them. A 7-type Boolean quotient cannot factor the translated-zero interface, even though it is sufficient for R267's original *untranslated* Boolean zero-only decision.

The necessary repair for this interface is the 25-class exact-residue profile code (5-bit fixed-width class identifier), plus the event phase; for source-typed native interfaces keep (original label, typed port, branch history, modular value) as separately declared and preserved data. Any later native quotient requires a genuine port/history-future congruence argument.

## Verification, reproduction and limitations

Run Python 3: `python R268_value_refinement.py`. It creates `R268_verification.json`. Arithmetic is exact Fraction for rational initialization and integer modular recurrence afterwards. Coverage: all 63 masks, 249 total recurrence taps, 2184 event residues per mask, recurrence-period equality on each mask's complete d_m base, exhaustive equality/support partitions, complete first-prefix partition check, and explicit translation counterexample.

The two-coordinate fingerprint is a classification result for these 63 fixed initial source sequences, not a universal two-dimensional dynamical representation and not a proof that arbitrary future BRC operations can be reconstructed from two values. The characteristic recurrence and lookup table constitute reproducible author evidence; independent review remains pending. The current work makes no change to the frozen science, P000, canonical claims or prior R267 cost theorem.

## Next problem

Construct a typed operator class acting on (label, port, branch history, residue) with an explicit port algebra and determine the coarsest future-congruence quotient. Seek an exact example where two sources with identical F_13 residues but distinct provenance are separated by an admissible native branch/port operation. Separately quantify the preprocessing/table and original-label cost when the 25-type cache is used, before claiming a net runtime speedup.
