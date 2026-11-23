# Riesel five-prime completion: exhaustive phase classification and fixed-trajectory costs

Researcher: `EM-DIRECT-970E1C` / `TASK_RESEARCH`  
Activity: `RA-D2EC212845B63844081F9A14`  
Continuation date: 2026-11-23 (Asia/Hong_Kong)

Status: author mathematical proofs, shared-context mathematical cross-checks, exact finite arithmetic and actual native BRC execution. No independent project Review, formal proof-checker acceptance or Foundation promotion is asserted. Source publication and Activity association are reported by their actual separate receipts.

## Main advance

The complete five-prime supplementary covering problem is now solved for the established old root class. Every such cover forces the primes 5 and 13 in opposite even-subsequence parities. Precisely three phase families remain, with **12 + 48 + 48 = 108 phase dictionaries**. The previous 12 nested-optimal dictionaries form only the first family. A full five-prime cover can use a basic pair that is not optimal at the two-prime intermediate stage.

This makes the predicate “supplementary cost equals five” an exact finite residue observation with a proved least additive period. Nevertheless, on one fixed trajectory of 29 specified prime readouts, every finite supplementary cost from six onward still occurs. Finite information can be sufficient for a specified budget predicate without determining unbounded covering complexity.

## Object and notation

The integer register is

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

with root parameter

\[
a_*=690786768637635218740714348513373826260012289
\]

and old prime dictionary

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,
673,1321,14449,29191,65537,6700417\}.
\]

Its product is

\[
M=1397394912916194098609132326092145093313722687204526281.
\]

Every positive odd root \(a\equiv a_*\pmod{2M}\) has the same complete P-readout trajectory. P covers all odd indices; the remaining even-index holes have density \(6/35\). Even-index terms are independently composite by

\[
F_{2u}(a)=(a2^u-1)(a2^u+1).
\]

Thus this whole root family already gives square Riesel coefficients. A hole of a specified prime dictionary is not a claim that the corresponding term is prime.

Let \(\delta_P(a)\) be the least number of primes outside P in a proper-prime cover of every term, with infinity if there is no finite cover. Let \(\tau(a^2)\) be the least total number of covering primes. The nontrivial branch is

\[
\mathcal B=\{a_*+6Mj:j\ge0\}.
\]

On the other two thirds of the old class, \(3\nmid a\) and \(\delta_P=1\). On \(\mathcal B\), the inherited four-channel gap proves \(\delta_P\ge5\).

The fixed X6 anchor, typed integer state, positive singleton BRC weight and multiplicity one remain unchanged. The native update is \(x\mapsto2x+1\), with even update \(x\mapsto4x+3\). The exponent counts arithmetic updates; prime readouts are observations of one state.

## Results and their scopes

| Note | New result | Exact scope |
|---|---|---|
| [global proof](global/proof.md) | Complete classification of every five-prime supplement, with 108 phase dictionaries | All old-class roots in \(\mathcal B\); all prime sizes and orders before analytic reduction |
| [observer proof](observer/proof.md) | Exact cost-five predicate, root count, least period and least positive root | Complete predicate \(\delta_P=5\) in the fixed old class; not all Riesel coefficients |
| [fiber proof](fiber/proof.md) | Sharp R0 and R1 residual-density staircases; finite-cost spectrum at one fixed 29-channel trajectory | Uniform bounds within the stated fibers, and \(\forall s\ge6\ \exists^\infty a\in R1\) with exact extra cost s and total cost \(20+s\) |
| [native execution](native/proof.md) | Four new representative integer trajectories, with all prescribed residual counts | Actual execution on the pinned native source; analytic completeness and optimality remain separate proofs |

### All five-prime phase families

Write \(n=2u\), let \(\varepsilon\) be the u-parity hit by 13 and missed by 5, and let \(r=c_{13}\bmod3\). The mandatory basic phases are

\[
c_5=1-\varepsilon\pmod2,\qquad
c_{13}\equiv\varepsilon\pmod2,\quad c_{13}\equiv r\pmod3.
\]

Only \(r=0,1\) occurs. The remaining fiber is \(u=u_0+6v\), with \(u_0\equiv\varepsilon\pmod2\) and \(u_0\equiv1-r\pmod3\).

| Family | r | Remaining fiber size modulo 35 | Last three primes | Required phase pattern | Dictionaries |
|---|---:|---:|---|---|---:|
| U/H1 | 0 | 13 | 11, 61, 331 | All three u-categories 0, 1, 4 modulo 5 | 12 |
| W/H1 | 0 | 13 | Any three of 19, 37, 73, 109 | All three v-categories modulo 3 | 48 |
| W/H0 | 1 | 23 | Any three of 19, 37, 73, 109 | All three v-categories modulo 3 | 48 |

Each phase row \((q,c)\) is realized by \(a\equiv\pm2^{-c}\pmod q\). Each dictionary therefore gives 32 CRT sign progressions, and infinitely many positive roots in each progression. These dictionary descriptions overlap; they are not disjoint root classes.

The all-prime proof first forces 5 and 13 by exact incidence inequalities. The remaining effective orders are \(\operatorname{ord}_q(2^{12})\); complete small factorizations and modular compatibility then force U or W. This proof uses no empirical prime-size cutoff. The prior four-channel gap also gives the independent necessary order bound \(\operatorname{ord}_q4\le70\) for any channel of a complete five-prime cover.

### Exact cost-five observer and minimum

Set

\[
U=\{11,61,331\},\quad W=\{19,37,73,109\},\quad
K=65\prod U=14436565,
\]

\[
L=K\prod W=80754838636615.
\]

In \(\mathcal B\), the predicate \(\delta_P(a)=5\) has exactly

\[
40693468800
\]

true root classes modulo L, with relative density

\[
\frac{8138693760}{16150967727323}.
\]

The relative density within the entire old class is one third of that. All nine prime coordinates are essential, so L is the least positive additive period in the branch parameter j.

The least positive root among **all** cost-five roots in the fixed old class is

\[
39741911323337250951212360989279347168190786597922987443929.
\]

Its coefficient is the square of this number. This strengthens the preceding result, which proved a minimum only within the nested-optimal subclass. The complete comparison uses 108 times 32, or 3456, CRT progression starts. It does not enumerate the roughly 80 trillion residues modulo L.

### Two fixed observation fibers

Define

\[
R0=\{a\in\mathcal B:a\equiv666303\pmod K\}.
\]

The five residues at \((5,13,11,61,331)\) are \((3,1,0,0,0)\). Its sharp uniform residual-density bounds for budgets zero through five are

\[
(216,108,39,26,13,0)/1260.
\]

Within R0, additionally fix the residues at \((19,37,73,109)\) to \((6,0,37,0)\). Equivalently,

\[
R1=\{a\in\mathcal B:a\equiv12926327728523\pmod L\}.
\]

This fixes all 29 specified prime trajectories. Its sharp uniform bounds for budgets zero through six are

\[
(432,216,78,52,26,13,0)/2520.
\]

The last positive gap is \(13/2520\). A nested optimal completion uses the two binary-phase primes 433 and 38737. A compact root attaining all six steps is provided in the fiber certificate and actually executed in the native note. Its minimum property is only among the classified nested-optimal six-channel roots in R1, not among all roots of cost six.

For every finite integer \(s\ge6\), infinitely many roots in R1 satisfy

\[
\delta_P(a)=s,\qquad \tau(a^2)=20+s.
\]

This follows by proving that the existing arbitrary-cost refinement and coprimalization construction retains all four new W coordinates. The proof preserves the quantifier order: different roots realize different costs. An ordinary root of infinite cost is not inferred.

## Reproduction and evidence

From this directory run:

```sh
python global/verify_global.py
python observer/verify_observer.py
python fiber/verify_fibers.py
python native/verify_native.py --source-dir /path/to/pinned_source
```

The global calculator checks 40,026 phase assignments after the analytic all-prime reduction and verifies the 108 surviving dictionaries over complete periods. The observer calculator compares 3456 CRT progression starts and counts all root classes by exact weighted category tuples. The fiber calculator checks the relevant full CRT class sets, sharp compact witnesses and the additional R1 residues of earlier exact-cost roots. It reuses their existing pairwise-gcd and native certificates instead of claiming a new execution of those unchanged calculations.

The new native calculation performs 6300 integer updates, 187740 quotient-remainder readouts, 126000 equalities with the old trajectory and 28980 additional fixed-fiber equalities. Its four period-count rows are recorded in the native note. The previous least-root native check is reused because the root and phases are unchanged; the new minimum property comes from the strengthened proof.

The global and observer verifiers use the Python standard library and self-contained small arithmetic inputs. The fiber and native scripts locate earlier certificates in the retained repository layout, with explicit path options available. Preserve the earlier `research_notes/portable_direct/...` paths when extracting dependencies. The native source directory contains the four pinned `enterprise_math` modules.

## Immutable scientific dependencies

| Commit | Path | Reused scientific scope |
|---|---|---|
| `e61a43115cf9dcbd0b3d8a746a5ac8086b8ca8fe` | `research_notes/portable_direct/riesel_mixed_20261119/certificate.json` | Old root, old prime dictionary, full old trajectory, native source pins |
| `af9e1a5e49386a28283781876e10742a71991036` | `research_notes/portable_direct/riesel_spectrum_20261121/gap/` | Old-hole calculation and branch lower bounds |
| `af9e1a5e49386a28283781876e10742a71991036` | `research_notes/portable_direct/riesel_spectrum_20261121/spectrum/` | Arbitrary finite-cost refinement, primitive-prime existence input, private-witness coprimalization and the cost-eight root |
| `a2ae4d93398425e67dacbb4c99b7f3a6755e5771` | `research_notes/portable_direct/riesel_observers_20261122/staircase/` | Universal density staircase and complete lower-budget equality cases |
| `a2ae4d93398425e67dacbb4c99b7f3a6755e5771` | `research_notes/portable_direct/riesel_observers_20261122/fixed_observer/` | Fixed 25-channel trajectory, exact-cost roots six and seven |
| `a2ae4d93398425e67dacbb4c99b7f3a6755e5771` | `research_notes/portable_direct/riesel_observers_20261122/native/` | Unchanged least-root native membership execution |
| `b1efc6c805661ed7b476e6e730107da6043176ee` | `src/enterprise_math/` | Frozen native BRC arithmetic substrate |

The four native Git blobs are `be1debe367263931bd5e93fd750be3ed54624fe1` (`brc_transport.py`), `9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1` (`brc_histogram.py`), `2591640fe348da9cd7f293a957bea9ae92c82943` (`brc_rational_holonomy.py`), and `4e6b3132580e3cd70a20a0d8bd4d28792b961afb` (`brc_weighted_recurrent.py`).

## Current rules and scientific boundaries

Current normative entrance reads began at `2026-11-23T02:16:55Z` (10:16:55 Asia/Hong_Kong), using global knowledge main `2632bb3f5c2192fc6cfffcfb3cafec56704838e3` and project main `5ed387d10c1fa5f69b7c4a51b840b1e4cf651892`. The canonical global bootstrap/manual, project index and project AGENTS route were followed; changed mathematical-research, continuation, journal and Activity policies were read as current rules. The current foundation router was checked for the continuation scope. Frozen scientific dependencies above retain their own identities.

The present result classifies a specific finite supplementary budget. It does not classify every Riesel number, every six-prime completion or every finite covering system. The least additive period is a statement about a named predicate; it does not identify the integer state or its joint cofactors with a finite residue tuple.

The unchanged original root's existence of a finite full cover remains unresolved in this work. Its previously proved lower bound of 1791 new primes is retained without a new window computation. Unbounded finite costs across roots do not establish infinite cost at a single ordinary root. The compact new examples have exact supplementary costs but no new equality claim for their total cover minima. Exact total costs belong to the separate coprimalized construction.

These files form one coherent continuation batch in the existing research Activity. The mathematical claims stand on the written proofs and proportionate exact calculations. Git publication, Activity association and independent review have distinct statuses.
