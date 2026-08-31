# Valley-band factoring reproducible benchmark ablation

## Claim card

- Researcher: `EM-VBBMK-A550CC`
- Task: `RS-VALLEY-BAND-FACTORING-REPRODUCIBLE-BENCHMARK-ABLATION`
- Owner branch: `research/valley-band-factor-benchmark`
- Hard target: `VALLEY_BAND_FACTORING_RELATION_YIELD_AND_COST_MODEL_REPRODUCIBLY_CLASSIFIED`
- Frozen source commit: `12725505c636449df7dd913ac06e581bf418b89c`
- Locked input: `research_inputs/VALLEY_BAND_PURE_STATE_AND_BENCHMARK_PACKET_20260823.md@f341b1347939e004e6d55c96e119c53337c0c9a0`
- Final classification: `INCONCLUSIVE_AFTER_VALIDATED_PARTIAL_MATRIX`

The hard target is **not closed**. The independent state/relation checker, point
implementation equivalence, corpus, rank-aware engine and a bounded partial
matrix are frozen and reproducible. The full threshold/repeat matrix, executed
QS context and an end-to-end factorization/crossover result are absent.

## Independence and firewall

This implementation was reconstructed from the single locked packet and
elementary continued-fraction algebra. No Valley source prototype, source
conversation, source diff, prior Lane1 mathematics, prior Lane1 code, or prior
Lane1 output was used. The execution node was reused after an unrelated Lane1
completion; that prior lane supplied no Valley prototype, source, or performance
context.

The corpus CSV contains known factors solely for generation validation and
post-run factor checking. `RunSpec`, multiplier scoring/pilots, relation
selection, GF(2) dependency selection and stopping receive no factor field. The
runner holds validation factors in a separate lookup and consults it only after
the collector returns. Every completed row records
`known_factor_used_in_decision=false`; all 31 post-run checks passed.

## Implementation Equivalence Ledger

Let `T=M*N` and start from the closed state

`(A_0,B_0,C_0)=(1,-T,0)`,

so `C^2-A*B=T`. With

`a=floor((floor(sqrt(T))+|C|)/|A|)`,

the transition

`A'=A*a^2+2*C*a+B`, `B'=A`, `C'=A*a+C`

preserves `C'^2-A'*B'=T` by direct expansion.

For the standard continued fraction of `sqrt(T)`, with complete-quotient state
`(m_i,d_i,a_i)`, induction gives

`A_i=(-1)^i d_i`, `C_i=(-1)^(i+1)m_i`,

with the same partial quotient. Bounded convergents
`x_{i+1}=a_i*x_i+x_{i-1} (mod N)` satisfy `x_i^2=A_i (mod N)` under the same
index convention. The independent reference CFRAC path and the closed path
therefore emit the same point value/root pairs.

For a state polynomial

`D(t)=A*t^2+2*C*t+B`,

if `x^2=A (mod N)` and `gcd(x,N)=1`, then

`r(t)=(A*t+C)*x^{-1} (mod N)`

satisfies `r(t)^2=D(t) (mod N)` because
`(A*t+C)^2-A*D(t)=C^2-A*B=T=0 (mod N)`. A nontrivial gcd encountered while
forming an inverse is already a valid algorithmic factor discovery. The full
band is the pre-registered intermediate range `1 <= t < a`; `t=a` is the point
endpoint.

For a factor-base prime `p` not dividing `A`, roots are

`t=(-C +/- sqrt(T))*A^{-1} (mod p)`.

Linear and degenerate cases are explicit. After exact division, every full or
recombined relation is rechecked as

`root^2 == product(p^e) (mod N)`

before insertion. The sign occupies its own parity column. Gaussian elimination
tracks rank and dependency combinations; every dependency reconstructs both
squares and tests `gcd(x-y,N)` and `gcd(x+y,N)`.

SLP pairs equal residual primes. DLP represents two-large-prime partials as
edges and converts graph cycles into complete relations. No raw relation count
is used as a substitute for rank.

## Corpus Freeze and Leakage Audit

The corpus was frozen before benchmark execution with seed
`EM-VBBMK-A550CC|2026-08-23|balanced-semiprimes|v1`. Each balanced semiprime is
generated from SHA-256 counter candidates, with exact half-width, top two bits
and odd bit set, followed by deterministic Miller-Rabin. Equal factors and
wrong-width products are rejected.

- 20 x 80-bit equivalence instances
- 10 x 96-bit benchmark instances
- 5 x 104-bit benchmark instances
- 3 x 112-bit benchmark instances
- exact fixed checkpoints F104, F112 and F128
- total rows: 41
- canonical row digest:
  `8897e83bff43616e52705a4640449f638505a35f46452ac00efada67885d7fd1`
- corpus CSV SHA-256:
  `f8a9e71eca6bb81c93afeffbf8f0bf35c39c60144b7e997d252c9f24f1f1029c`
- immutable config SHA-256:
  `6970dce467be91d889413c026ff13bdfb79901c40a4a7d18ef75caea5c6edf24`

The frozen grid includes point CFRAC, closed point, full bands at
32/64/128/256/512, adaptive holdout, multiplier holdout, none/SLP/DLP,
factor-base bounds 1200/2000/3200/5000, three sub-128 repeats, and fixed
104/112/128 checkpoints. No threshold was tuned from outcomes.

## Checker results

`verify.py` completed successfully after the matrix freeze:

- exact corpus regeneration: 41/41 rows;
- paired reference/closed equivalence: 20 instances x 5,000 steps = 100,000
  steps, combined digest
  `940b81dbc851ce525a2a4d2e77f5bb0a455ca02a7fa54e10e47a902f7618b1f3`;
- polynomial-root direct enumeration: 10,783 roots across 250 states and 5,750
  state/prime pairs;
- direct band-root congruence: pass;
- square-multiplier character classes: 500 prime checks, pass away from primes
  dividing the square multiplier; runtime state scaling was not identified;
- recurrence-sign, invalid-root, rank-vs-count and post-hoc-selection negative
  controls: all pass;
- point relation-stream and rank smoke: pass;
- full relation verification before every matrix insertion: enabled.

The 100,000-step enumeration is a reproducibility check, not a substitute for
the algebraic induction above.

## Rank-Aware Relation Analysis

Command:

```powershell
python experiments\valley_band_benchmark\runner.py --matrix frozen
```

The predeclared local checkpoint budget was 300 seconds. The process ended after
303.5011 seconds because timeout checks occur between orbit states and an
in-flight band can overrun.

| status | rows |
|---|---:|
| `MAX_STEPS` | 22 |
| `TIMEOUT` | 9 |
| `ERROR` | 0 |
| `NOT_RUN_BUDGET` | 49 |
| total | 80 |

All null, timeout and not-run rows remain in the run and aggregate CSVs. No row
was imputed or silently omitted.

## Three-repeat point result

R96-00, R96-01 and R96-02 each completed both paths three times at 60,000
candidates. Across all nine pairs, mathematical relation digests and rank
trajectory digests agreed exactly.

| instance | CFRAC median s | closed median s | ratio | full/rank/deps |
|---|---:|---:|---:|---:|
| R96-00 | 2.6123214 | 4.3993874 | 1.6841 | 23 / 22 / 1 |
| R96-01 | 2.6175474 | 4.4890566 | 1.7150 | 29 / 29 / 0 |
| R96-02 | 2.5986081 | 4.3776894 | 1.6846 | 30 / 30 / 0 |

Thus point semantics and relation yield are independently replicated, while the
closed-state implementation is locally slower in Python. These are completed
configurations, not successful factorizations.

## Fixed Threshold Ablation

Each threshold 32/64/128/256/512 ran once on R96-00 and timed out. It processed
25,714–32,273 band candidates and finished with full/rank 3/3. No threshold can
be ranked from censored equal-rank outcomes.

## Large-Prime Ablation

At threshold 256, one none/SLP/DLP ablation was completed as a timeout
diagnostic. None processed 439,847 total candidates and reached rank 30; SLP and
DLP each processed 36,974 and reached rank 3. DLP stored 223 edges and closed
zero cycles. Profiling locates the dominant local failure in untimed Python
cofactor primality/classification work. This refutes a speedup claim for this
implementation/run, but cannot refute the large-prime technique in general.

## Multiplier Holdout

The training-only multiplier procedure chose `M=13`. On held-out R96-06 it
completed 60,000 points with 29 verified relations, rank 29, no dependency and
no factor.

## Adaptive Policy Holdout

The adaptive policy used only the threshold-256 training row, opened
zero holdout bands, and timed out under SLP point-cofactor overhead at 33,426
points, 107 relations, rank 102 and five tested dependencies. It remained below
the frozen target of factor-base dimension 108 plus margin 8, and found no
factor.

## Fixed checkpoints and factor outcome

The exact F104/F112/F128 point diagnostics completed:

| checkpoint | point limit | full/rank/deps | factor-base dimension | factor |
|---|---:|---:|---:|---|
| F104 | 120,000 | 28 / 28 / 0 | 149 | null |
| F112 | 160,000 | 48 / 48 / 0 | 219 | null |
| F128 | 200,000 | 28 / 28 / 0 | 338 | null |

Closed and band variants at those sizes are `NOT_RUN_BUDGET`; this is a precise
diagnosis, not a 128-bit factoring result. Across all completed rows there were
11 tested dependencies and zero factors. All null factors are retained.

## CFRAC and QS Context Baselines

No native QS tool was present. A minimal same-language single-polynomial QS
context path was independently authored and pinned at SHA-256
`0a7aff7e3093bc011bff93dae74940c618160a2567758cc03f5747d78d68877e`.
It uses the same exact relation verifier and GF(2) extractor. All four planned QS
rows were `NOT_RUN_BUDGET`; therefore there is no measured CFRAC/QS ratio.
Language difference would have been none (CPython versus CPython). The context
must not be presented as optimized native QS.

## Per-Stage Cost Breakdown

At 96 bits the median marginal point cost was 43.538690 microseconds/candidate
for CFRAC and 73.323123 microseconds/candidate for the closed path. The largest
recorded `tracemalloc` peak was 14,804,351 bytes. Stage timers preserve state,
root setup, sieve, trial division, recombination, GF(2), and gcd time. A large
unattributed gap remains in LP runs, chiefly because cofactor primality checks
are outside the timed recombination block. The separate cost-model artifact
retains this gap explicitly.

## Prior-art audit and novelty boundary

Morrison and Brillhart's original 1975 CFRAC paper established continued-
fraction smooth-residue factoring and the factorization of `F_7`
([DOI record](https://doi.org/10.1090/S0025-5718-1975-0371800-5)). Pomerance's
publication record lists both analysis/comparison of factoring algorithms,
CFRAC implementation work, and the quadratic-sieve algorithm
([author bibliography](https://math.dartmouth.edu/~carlp/)). NIST's DLMF
places CFRAC, MPQS and NFS in the congruent-squares Type-II family
([DLMF 27.19](https://dlmf.nist.gov/27.19)). Boender and te Riele document the
single/double-large-prime variants, the graph-cycle interpretation, and the
dependence of crossover on parameters, hardware and implementation
([CWI paper](https://ir.cwi.nl/pub/1367/1367D.pdf)).

Accordingly, this report claims no novelty for continued-fraction relation
collection, QS, SLP/DLP, graph cycles, GF(2), multiplier scoring or intermediate
convergents. It contributes an independent checker and a reproducible local
partial ablation. The audit did not establish that the particular all-
semiconvergent “valley band” packaging is new; absence of an identified match is
not evidence of novelty.

## Threats, retained failures and next executable action

1. Execute the existing 49 `NOT_RUN_BUDGET` rows as a new, separately named
   continuation without merging them into this freeze.
2. Move cofactor primality/splitting into explicit stage timing and add
   inside-band deadline checks; do not rewrite the frozen results.
3. Obtain three uncensored repeats for every threshold and LP mode on multiple
   training and holdout instances.
4. Execute the pinned QS context on the same node, then optionally add a
   separately disclosed native-QS background run.
5. Complete closed-point and full-band diagnostics at F104/F112/F128.
6. Require rank target, nontrivial dependency and verified factor extraction
   before any factorization-success classification.

Until those steps are complete, the only valid terminal label is
`INCONCLUSIVE_AFTER_VALIDATED_PARTIAL_MATRIX`.

## Reproduction and validation

```powershell
python experiments\valley_band_benchmark\corpus.py --check
python experiments\valley_band_benchmark\verify.py
python experiments\valley_band_benchmark\aggregate.py
python -m py_compile experiments\valley_band_benchmark\core.py experiments\valley_band_benchmark\corpus.py experiments\valley_band_benchmark\verify.py experiments\valley_band_benchmark\qs_context.py experiments\valley_band_benchmark\runner.py experiments\valley_band_benchmark\aggregate.py
```

The frozen matrix command is recorded for regeneration, but rerunning it creates
a new timing sample and must not be silently substituted for the frozen CSV.

## Required artifact map

1. `research_output/VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_ABLATION_20260823.md`
2. `research_output/reducer_results/VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_ABLATION_REDUCER_20260823.md`
3. `experiments/valley_band_benchmark/`
4. `research_output/VALLEY_BAND_BENCHMARK_CORPUS_20260823.csv`
5. `research_output/VALLEY_BAND_BENCHMARK_RUNS_20260823.csv`
6. `research_output/VALLEY_BAND_BENCHMARK_AGGREGATES_20260823.csv`
7. `research_output/VALLEY_BAND_OPENING_COST_MODEL_20260823.md`
8. `research_output/VALLEY_BAND_BENCHMARK_ENVIRONMENT_20260823.json`
9. `research_output/evidence/VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_20260823.jsonl`

## Final Classification

`INCONCLUSIVE_AFTER_VALIDATED_PARTIAL_MATRIX`

Researcher-ID: EM-VBBMK-A550CC / RS-VALLEY-BAND-FACTORING-REPRODUCIBLE-BENCHMARK-ABLATION

Global-Knowledge-Sync: main@506eb72 / GLOBAL_KNOWLEDGE_V1
