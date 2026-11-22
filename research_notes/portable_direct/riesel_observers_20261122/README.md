# Riesel residue observers: exact optima, retained information, and a fixed-root lower bound

Researcher: `EM-DIRECT-970E1C` / `TASK_RESEARCH`  
Activity: `RA-D2EC212845B63844081F9A14`  
Continuation date: 2026-11-22 (Asia/Hong_Kong)

Status: author proofs, shared-context mathematical feedback, exact finite certificates and actual pinned native BRC execution. These artifacts do not claim an independent project Review, formal proof-checker acceptance, or Foundation promotion. Publication and Activity bookkeeping are recorded separately by their actual receipts.

## Results and their distinct scopes

Keep the old root

\[
a_*=690786768637635218740714348513373826260012289
\]

and the established twenty-prime dictionary P, with product

\[
M=1397394912916194098609132326092145093313722687204526281.
\]

The state is \(F_n(a)=a^22^n-1\). The fixed X6 anchor, integer-register type and positive singleton BRC update \(x\mapsto2x+1\) remain unchanged. Arithmetic indices are not physical time; prime readouts are not axes or native branches.

| Folder | Main result | Quantifier or limit |
|---|---|---|
| [staircase](staircase/proof.md) | Sharp residual-density staircase \((72,36,13,8,3,0)/420\) for budgets 0 through 5; all equality cases for budgets 1–4 | Every old-class root with \(3\mid a\), every new-prime set of the indicated budget; sharpness attained by one nested dictionary at one root |
| [observer](observer/proof.md) | Exact least Boolean periods 5, 65, K, K, K for the five specified optimization predicates, where \(K=14436565\); exact root counts and least nested-optimal root | Specific predicates only; nested optimality is not all additional-cost-five roots |
| [fixed_observer](fixed_observer/proof.md) | At the single observer residue \(a\equiv666303\pmod K\), every finite extra cost \(s\ge5\) and exact total cost \(20+s\) occur infinitely often | \(\forall s\ \exists^\infty a\), with all 25 prime-residue trajectories fixed; no infinite-cost ordinary root is inferred |
| [fixed](fixed/proof.md) | A specified 2056-term window of the unchanged original root has exact \(\alpha=\tau=1791\) | Any finite full-sequence cover requires at least 1791 primes outside P; total 1811 only if P is retained |
| [native](native/proof.md) | Actual native execution for all 12 optimal phase dictionaries and the least nested-optimal root | 5460 updates and 136500 prime readouts; mathematical completeness and minimality come from the separate proofs |

The original qualitative question is resolved at two precise levels. The small-budget optima have a complete explanation through compatible zero phases: the first two channels force a parity/mod-3 fiber, and the next two occupy its two largest mod-5 classes. The same finite observer does not determine full covering cost: one fixed 25-channel trajectory supports every finite additional cost at least 5.

## Numerical highlights

For roots in \(\mathcal B=\{a_*+6Mj:j\ge0\}\), let \(E_t\) mean that a supplement of at most t primes attains the universal density bound, and let N mean there is a nested chain attaining all bounds through budget 5.

| Predicate | Residue classes modulo \(K=14436565\) | Relative density in \(\mathcal B\) | Least positive period in j |
|---|---:|---:|---:|
| \(E_1\) | 11549252 | \(4/5\) | 5 |
| \(E_2\) | 1776808 | \(8/65\) | 65 |
| \(E_3\) | 733024 | \(733024/K\) | K |
| \(E_4\) | 25408 | \(25408/K\) | K |
| N | 384 | \(384/K\) | K |

The nested subclass has 12 phase dictionaries, 24 ordered prime/phase chains, and 384 root residue classes. Its least positive root is

\[
39741911323337250951212360989279347168190786597922987443929.
\]

The minimum claim is confined to N in the fixed old root class. It is not the least Riesel number, the least square Riesel coefficient, or the least root of additional cost 5.

The fixed-original-root certificate checks all 2112540 pairs in a 2056-term translated window, finds 1191 nontrivial gcd pairs, and supplies both a 1791-element pairwise-coprime set and a 1791-block common-gcd partition. It uses complete unfactored integer gcd packets, including all newly computed distances 1028 through 2055; there is no prime-size cutoff. Its additional native check has 460 actual projected updates.

## Reproduction

Run these from this directory:

```sh
python staircase/verify_staircase.py
python observer/verify_observer.py --output observer/observer_certificate.json
python native/verify_native.py --source-dir /path/to/pinned_source
python fixed_observer/verify_fixed_observer.py
python fixed/verify.py --prior-dir ../riesel_budget_20261120/fixed --source-dir /path/to/pinned_source
```

The two standalone arithmetic verifiers require Python standard-library modules only. The other verifiers also need the specified earlier artifacts at their existing repository-relative paths. The native source directory must contain `enterprise_math/brc_transport.py` and the other three pinned modules. An ancestor's `src` or `vendor_src` is discovered automatically when available; `--source-dir` chooses an explicit location.

The fixed-window verifier defaults to compiling `extend_packets.cpp` with C++17, GMP and OpenMP and recomputing all 1028 new packets. It then performs the complete certificate checks without an optimization solver. The prior 1027 packets remain an explicit verified dependency. `--reuse-new-packets` accepts an actual completed packet-generation output from the same research run and records that reuse rather than claiming a second independent computation.

The native and fixed-observer verifiers locate their earlier certificates by walking to the repository ancestor. Preserve the `research_notes/portable_direct/...` layout when reproducing from an extracted artifact set. The fixed verifier also supports an explicit `--prior-dir`. Each certificate retains its execution scope and distinction between new computation and reused evidence.

## Immutable scientific dependencies

| Commit | Path | Role |
|---|---|---|
| `e61a43115cf9dcbd0b3d8a746a5ac8086b8ca8fe` | `research_notes/portable_direct/riesel_mixed_20261119/certificate.json` | Old root, twenty-prime trajectory, exact holes, native source pins |
| `2feef401388e6e81a35dd8b0e66383f43561ad12` | `research_notes/portable_direct/riesel_budget_20261120/fixed/` | Unchanged fixed a, A, S and complete distance-1-through-1027 gcd dictionary |
| `af9e1a5e49386a28283781876e10742a71991036` | `research_notes/portable_direct/riesel_spectrum_20261121/gap/` | Earlier sharp four-channel proof and full native verification |
| `af9e1a5e49386a28283781876e10742a71991036` | `research_notes/portable_direct/riesel_spectrum_20261121/spectrum/` | All-cost refinement and private-witness coprimalization theorem; unchanged seed and cost-eight evidence |
| `b1efc6c805661ed7b476e6e730107da6043176ee` | `src/enterprise_math/` | Four frozen native BRC modules, exact blobs listed in `source_scope.json` |

The all-cost corollary reuses the preceding primitive-prime existence input; it does not replace that theorem by finite experiments. Current normative source reads and frozen scientific dependencies have separate identities in [source_scope.json](source_scope.json). Updating a control entry does not repin the scientific substrate.

## Evidence boundaries

The universal staircase and equality classification are analytic arguments using exact incidence formulas and complete small factorizations. Exhaustive phase enumeration checks the finite dictionary after the proof makes it exhaustive. The fixed-window result is certified by matching lower and upper witnesses using joint gcds, not by trusting a discovery optimizer. Actual native execution checks the chosen integer and observer semantics. None of these statuses implies independent Review or formal admission.

The old original root's full finite-cover existence remains unresolved. Unbounded finite costs across different roots are not an infinite cost at one ordinary root. The least periods certify only the named predicates; full integer, cofactor and joint-relation information remain available and are needed for the larger covering question.
