# Complete budget-eight classification and observer on the fixed R3 fiber

Research continuation, 24 November 2026 (Asia/Hong_Kong).

Researcher-ID: `EM-DIRECT-970E1C / TASK_RESEARCH`  
Research-Activity-ID: `RA-D2EC212845B63844081F9A14`

This batch continues the [fixed-43-channel finite-spectrum source](https://github.com/awdawmip/enterprise-math/blob/5cfe4d64429f284232029341c6ba774e2eb6f727/research_notes/portable_direct/riesel_eight_spectrum_20261124/README.md). The historical R3 root progression and all its 43 complete residue-value trajectories are retained exactly.

The native object is the full typed integer register at a fixed Heartbeat X6 anchor, with positive singleton BRC weight and multiplicity one: x_0=a^2-1, x_(n+1)=2x_n+1 and F_n(a)=a^2 2^n-1. Prime coordinates observe that state; the full integer and joint cofactor relations remain available. Let delta_P denote supplementary prime-cover cost and tau unrestricted total cost.

## 1. Complete eight-prime classification

Every complete supplement of at most eight primes on R3 has exactly eight primes and contains 5 and 13. It contains **both or neither of 19 and 73**. The exactly-one case is impossible. The [prefix proof](prefix/proof.md) gives an all-prime residual-mass argument for this dichotomy and the entire zero-W branch. The [tail proof](tail/proof.md) classifies the retained-prefix branch.

| Branch | Final structure | Phase dictionaries | Signed CRT descriptions |
|---|---|---:|---:|
| Retain 19,73 | 38737, 487824887233, two opposite mod-eight channels | 30 | 120 |
| Retain 19,73 | 38737, 246241, both order-216 channels | 2 | 8 |
| Retain 19,73 | 38737 and three modulo-ten channels | 24 | 192 |
| Omit 19,73 | All four effective-period-seven primes, then two effective-period-fourteen primes | 720 | 46,080 |
| Omit 19,73 | All four effective-period-seven primes, then two effective-period-thirty-five primes | 6,336 | 405,504 |
| Total | | **7,112** | **451,904** |

The descriptions may overlap as root sets. Each has infinitely many ordinary positive integer realizations in R3, with exact delta_P=8. The new zero-W branch is essential: the budget-seven forced prefix does not persist unchanged at budget eight.

After 5 and 13, write n=8+12v. The remaining v residues modulo 35 form five occupied rows modulo seven, with sizes 2,3,3,3,2. The zero-W branch must use all four primes {29,43,1429,5419} on four different rows. The last row is either split into its opposite modulo-fourteen lifts, or, when it contains two points, those two points are covered separately modulo 35. Full prime inventories are established by complete factorizations, exact order checks and deterministic recursive n-1 primality certificates.

The [prefix calculator](prefix/verify_zero_branch.py) and its [certificate](prefix/zero_branch_certificate.json) verify the exact residual geometry and an explicit 157-digit zero-W root, including 15,360 CRT starts of its stated subfamily. The [auxiliary inventory certificate](prefix/auxiliary_inventory_certificate.json) retains every recursive prime witness. The [tail calculator](tail/verify_tail_eight.py) and [certificate](tail/tail_eight_certificate.json) retain all 56 retained-prefix patterns and their exact root categories.

## 2. Global minimum root of cost eight

The [minimum theorem](minimum/proof.md) proves that the least positive a in the entire R3 fiber with delta_P(a)=8 is the following 146-digit integer:

```text
25391491002591320391732108159477707323814206756039394016382357924666368039179689189103105696777816709091120408108658618711788120139363377072408503
```

Its supplement is {5,13,19,73,38737,487824887233,1153,193}. It has a=885 modulo 1153 and a=63 modulo 193. The total-cover conclusion for this compact root is tau(a^2)<=28.

The [calculator](minimum/verify_minimum.py) compares all 320 retained-prefix CRT starts. The minimum has R3 progression index 63,706. It then checks every smaller positive root: among k=0,...,63705, none activates all four compulsory period-seven primes of the other branch. Their active-count histogram is (21939,31370,10276,121,0). This excludes the entire remaining branch and upgrades the minimum to all of R3. The [certificate](minimum/minimum_certificate.json) retains the complete CRT comparison and finite exclusion evidence.

## 3. Exact complete budget-eight observer

The [observer theorem](observer/proof.md) identifies exactly 31 free prime coordinates. Let T8 be their product. For any positive N,

\[
\boxed{[a]_N\text{ determines }\delta_P(a)\le8\text{ on }R_3
\iff T_8\mid N.}
\]

The same equivalence holds for the entire future F_n(a) modulo N. All 31 coordinates are individually essential. Their largest base-two order is 420, giving

\[
\boxed{\Omega_8(R_3)=\widehat\Omega_8(R_3)=420.}
\]

The exact natural frequency of cost eight in R3 is approximately

\[
0.0000435545391699103709469567710912452495191598684430.
\]

The count uses inclusion-exclusion within each phase group and between the two branches, not the sum of overlapping CRT descriptions. Full integer numerator, denominator, root-category tables and the four J/Z states are in the [observer certificate](observer/eight_observer_certificate.json), regenerated by the [standard-library calculator](observer/verify_eight_observer.py).

The 12-coordinate retained-prefix observer alone has maximum order 360 and decides its own restricted predicate. The additional nineteen coordinates are required for the complete budget. The full observation has 74 prime coordinates when the fixed 43 are also counted; one composite modulus packages the 31 additional coordinates.

## 4. Finite exact 8/9 witnesses and the price of keeping the prefix

The two primes 209924353 and 4261383649 have exact base-two order 432. On the residual coordinate they cover w=0 and w=8 modulo twelve. Together with the seven fixed active supplementary channels of R3 they give a common nine-prime cover.

This nine-cover can be imposed alongside any of the 31 observer counterfactuals. Each essential-coordinate pair consists of ordinary integer roots of exact costs eight and nine, with all other specified coordinates held fixed. The separate explicit pair with all twelve retained-prefix coordinates zero also has finite exact costs eight and nine.

For the cost-eight member of that pair, no eight-prime dictionary retaining {5,13,19,73} exists, while the displayed nine-cover retains them. Thus the minimum supplementary cost under that retained-prefix constraint is exactly nine, compared with unrestricted supplementary cost eight. The same root pays exactly one extra prime if that prefix is required.

## 5. Actual native execution

The [native note](native/proof.md), [script](native/verify_native_minimum.py) and [certificate](native/native_minimum_certificate.json) record the globally minimal root on one complete covering-predicate period of length 10,080:

| Operation | Actual count |
|---|---:|
| Native one-step BRC updates | 10,080 |
| Native two-step composed evaluations | 5,040 |
| Individual native prime quotient/remainder readouts | 453,600 |
| Joint 45-radix native readouts and recompositions, each | 10,080 |
| Direct comparisons of the fixed 43 coordinates | 433,440 |

The selected route's uncovered counts are (1728,864,312,208,104,52,26,13,0). The final full integer has 11,047 bits. All actual divisor hits are proper; all 28 selected dictionary primes have saved private witnesses. The separately computed full residue-value period is 60,480; the new native run executed the complete covering period of 10,080.

The four scientific modules remain frozen at commit b1efc6c805661ed7b476e6e730107da6043176ee. The readouts preserve independent prime cofactors and the joint mixed-radix cofactor; the full integer is recomposed at every step.

## 6. Reproduction

From this component root:

```sh
python prefix/verify_zero_branch.py
python tail/verify_tail_eight.py
python observer/verify_eight_observer.py
python minimum/verify_minimum.py
python native/verify_native_minimum.py --source-dir /path/to/pinned_source
```

The first four calculators use only the Python standard library. The native calculator additionally uses the four frozen modules documented in its proof. [Prefix review](reviews/prefix.md) and [minimum/native review](reviews/minimum_native.md) record collaborative checking without repeating the large computations.

## 7. Scope and continuation

This closes the preceding full-eight-classification and global-minimum questions for the fixed historical R3. Its already-proved finite supplementary spectrum remains exactly {8,9,10,...}, with infinitely many exact-total-cost realizations for each s. The earlier uniform order bounds (9/16)2^b through 105*2^b keep their original R1/R2 scopes.

Current questions include the full cost-nine classification and its least R3 root, exact unrestricted total cost of the new compact minimum, sharp general observer constants, and the original a_star finite-cover question. The old 1,791-prime lower bound for a_star remains a finite bound.

Normative sources were verified at 2026-11-24T07:32:48Z (15:32:48 Asia/Hong_Kong), EM a88e3e001275269cae93c40d77e6984b1ef2970f and GK 874e3ce7d661407b072f7d8fe04c50d54d0e1963, and reused within their valid read lease. The applicable AGENTS entry, P000, Heartbeat World, joint-relation preservation, residual fidelity and research/Activity rules remain in scope. All new results are author proofs with shared-context collaborative checking and the explicitly stated execution. Independent project Review and formal acceptance are not claimed.
