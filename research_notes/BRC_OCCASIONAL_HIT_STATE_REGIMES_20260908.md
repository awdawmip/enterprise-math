# Preserve occasional BRC completion hits by state and measured cost

Researcher: `EM-HME-0CE4FD / TASK_RESEARCH`  
Status: proved elementary counting/parametrization, fixed toy witnesses and local timing evidence; research persistence only.  
Global context: `ca9cd753e298ccf9524393faf33047d9b5246d07`.  
Parent frontier: `200d53277c5d033bc229e4758d5fee28da8a5c2e`, state-separated BRC laws.

## 1. Retention criterion from current user steering

The current instruction is to pursue occasional fast successes rather than a universal solution, and not to organize the research around refuting routes with failure examples. Accordingly:

- retain a certified positive subfamily or measured local benefit;
- declare a small probe budget and stop at that budget;
- use unsuccessful observations to measure cost and coverage, not to reject the entire route;
- verify every claimed successful output;
- preserve setup cost, observation cost and the population definition alongside a speed claim.

This experiment contains fixed small-number observations and no target-input option. It executes one immediate square-completion observation per fixture, without multiplier search or a factor-search fallback. The active broader research objective remains open.

## 2. Exact reuse and observation contract

Reuse is applied to existing sources at the pinned parent frontier:

- `brc_multiplier_basin.point_cost_state`: `REUSE_EXECUTED` for exact `(J,R,A)` states;
- `brc_square_gap_prefilter.ceiling_completion_square_witness`: `REUSE_EXECUTED` on the positive families and the known-prime-product cohort;
- `brc_square_gap_prefilter.filtered_square_root`: `REUSE_EXECUTED` as an existing checked square-root kernel;
- `brc_opportunistic_shortcuts.RegimeShortcutLedger` and `ShortcutContext.shadow_tag`: `COMPOSE_APPLIED / REUSE_EXECUTED` to preserve the separate direction and size-band observations.

The existing [opportunistic portfolio](https://github.com/awdawmip/enterprise-math/blob/200d53277c5d033bc229e4758d5fee28da8a5c2e/research_notes/BRC_OPPORTUNISTIC_SHORTCUT_PORTFOLIO_20260907.md) already retains locally useful methods. This note adds state-specific positive evidence using those interfaces, rather than creating another general solver family.

For a nonsquare positive integer,

\[
N=J^2+R,\quad 1\le R\le2J,\quad a=J+1,\quad A=a^2-N=2J+1-R.
\]

`D` is the down-cost-cheaper population `1 <= R <= J`; `U` is the up-cost-cheaper population `J+1 <= R <= 2J`. The canonical collapse remains downward in both populations.

The sole event observed here is **immediate completion**: `A` is an integer square. Direction-only counts are aggregate statements. Checking the event on one input consumes its actual completion gap; it is not a root-only or residual-only oracle. Stationary squares are outside these counts and timing fixtures.

## 3. Positive completion counts in each direction

Every immediate completion is uniquely represented by

\[
R=2J+1-b^2,\qquad1\le b\le\lfloor\sqrt{2J}\rfloor.
\]

In `U`, the completion gap ranges from `1` through `J`; in `D`, it ranges from `J+1` through `2J`. Therefore the exact hit counts per complete basin are

\[
\boxed{H_U(J)=\lfloor\sqrt J\rfloor,\qquad
H_D(J)=\lfloor\sqrt{2J}\rfloor-\lfloor\sqrt J\rfloor.}
\]

Each population has `J` observations, so its conditional event frequency is the corresponding count divided by `J`. This is a positive counting law, not an inference about a cryptographic input distribution.

The full finite bands used to check the law give:

| Complete root band | Direction | Integer observations | Immediate completions | Frequency |
|---|---|---:|---:|---:|
| `16..128` | D | 8,136 | 382 | 4.695% |
| `16..128` | U | 8,136 | 879 | 10.804% |
| `129..255` | D | 24,384 | 730 | 2.994% |
| `129..255` | U | 24,384 | 1,687 | 6.918% |

The two directions remain separate in the existing ledger via `shadow_tag`; their aggregate average does not replace the individual records. Both directions retain positive hits.

## 4. A positive family for every fixed residual

For any fixed integer `r >= 1`, choose integers `b` such that

\[
b^2+r-1\equiv0\pmod2,\qquad
J=\frac{b^2+r-1}{2}\ge\max(r,3),\qquad N=J^2+r.
\]

Then `N` belongs to `D`, and

\[
(J+1)^2-N=2J+1-r=b^2.
\]

There are infinitely many eligible `b` of the required parity. Thus every fixed positive residual has an infinite positive family of immediate-completion states inside `D`. The statement is about integer constructions; it does not assert infinitely many semiprimes in any prescribed quadratic family.

The lower bound `J >= 3` makes the corresponding two integer factors nontrivial: `b^2 <= 2J` implies `b < J`, hence `J+1-b >= 2`. For example, the small known construction `493 = 17*29` has `J=22`, `R=9`, and completion gap `36`. The separate `U` example `2021 = 43*47` has `J=44`, `R=85`, and completion gap `4`.

The executable verifies 205 directly constructed positive members using `1 <= r <= 24`, `2 <= b <= 20`, and the unchanged completion-witness API. These are constructive fixtures, not a search for adverse inputs.

## 5. A fixed small semiprime cohort and the hidden-moment connection

Use all 406 distinct pairs of the 29 primes in `[101,251]`. All factors are known by construction and all products are below `2^16`. Only `N` enters the unchanged completion-witness API; known factors verify the returned witness.

| Initial direction | Toy semiprime observations | Verified immediate hits | Frequency |
|---|---:|---:|---:|
| D | 163 | 48 | 29.448% |
| U | 243 | 108 | 44.444% |

This selected small-factor range is its own population. Its frequencies must remain separate from the complete integer-basin frequencies and from any claim about large RSA inputs.

On a certified immediate-completion witness `(a,b)` for an odd distinct-prime product, the two nontrivial factors are the prescribed pair `a-b` and `a+b`. Consequently the earlier hidden coordinate has the **conditional** value

\[
S=p+q=2a=2(J+1).
\]

For the unnormalized third central moment of `{0,p,q}`, the previously verified formula then gives

\[
9M_3=2S^3-9NS.
\]

All 156 positive fixtures verify both `S` and this scaled moment, with an independent exact `Fraction` evaluation of the centered sum. This reconnects the state study to the hidden-moment direction on a certified success population. It reuses the classical completion channel; computing the moment is not a second source of information.

## 6. A measured small-range speed specialist

The timed experiment compares equivalent square-completion observation kernels on deterministic samples of 2,048 states from each complete-integer band/direction, followed by all 163 D and 243 U members of the known-prime-product cohort. It uses seven rounds in shuffled method order. Each method/round processes at least 16,384 observations: eight batch repetitions for the large samples, 101 for the 163-member cohort, and 68 for the 243-member cohort.

For this fixed experiment only, every completion gap satisfies `1 <= A <= 510`. A 22-entry dictionary stores exact roots of the squares in that interval. The harness cannot accept an external target or enlarge its fixture domain through a command-line parameter.

Three cost contexts are measured separately:

- **Gap already available:** compare lookup with native `isqrt(A)` followed by exact square verification.
- **Input observation included:** both paths first compute native `isqrt(N)` and the completion gap; then compare the same two square tests.
- **Witness verification included:** also form the two proposed factors, require the smaller to exceed one, and verify their product against `N`. This is the primary complete-path timing for the fixed fixtures.

The existing checked filter API is also measured, but the minimal native kernel is the main speed reference, so API validation overhead is not credited as a new mathematical gain.

Final recorded run, CPython 3.14.6 on the host Windows runtime:

| Fixed population | Direction | Native verified ns/input | Lookup verified ns/input | Native / lookup | Faster lookup rounds |
|---|---|---:|---:|---:|---:|
| Integer band `16..128` | D | 178.339 | 157.275 | 1.134x | 6/7 |
| Integer band `16..128` | U | 185.553 | 165.332 | 1.122x | 7/7 |
| Integer band `129..255` | D | 220.471 | 184.320 | 1.196x | 6/7 |
| Integer band `129..255` | U | 191.357 | 164.838 | 1.161x | 7/7 |
| Prime seeds `[101,251]` | D | 223.416 | 190.822 | 1.171x | 7/7 |
| Prime seeds `[101,251]` | U | 221.811 | 199.153 | 1.114x | 5/7 |

The table build median is 1,800 ns. Summing the Python dictionary/key/value object sizes gives 2,400 bytes. In this run, measured setup is recovered after roughly 50--90 verified input observations; the two known-prime-product populations give 56 and 80 observations. Import and logging costs are outside both timed kernels; setup is reported separately. The ledger preserves separate materialized-gap and verified-input records. Its saved cost is the measured replaced kernel cost, not speculative downstream work saved.

These measurements support keeping a warm, bounded small-gap lookup as a local specialist. They measure one completion attempt, including exact witness verification in the primary path, on the declared small fixtures; they do not establish a large-number factorization speedup. The fixture band, gap bound, setup amortization and host runtime are part of the result. A single cold observation is a different cost context. All raw rounds and the intermediate kernel timings remain in the certificate, including rounds where the lookup is slower.

## 7. Reproduction, artifacts and continuation

From the project root:

```powershell
python experiments/brc_occasional_hit_regimes_20260908.py --enterprise-root . --output-dir experiments
```

The JSON certificate records all seven timing rounds, 65,280 bounded gap classifications, 255 basin count checks, 764 unchanged point-state API checks, 205 positive constructed witnesses, and all 406 known-prime-product observations with 156 exact `S`/moment checks. Timing changes between runs are expected; exact counts and witnesses are the reproducible mathematical results.

No production dispatch, adaptive multiplier order, task registration or canonical theorem status is changed. The current durable positive results are the per-direction count law, the fixed-residual positive family, the conditional `S`/moment connection, and the measured bounded kernel specialization.

Next research should preserve this occasional-success criterion. A useful extension needs a specified success population and a cheap observable condition, with preparation and verification included in its cost contract. A miss records an uncompleted attempt and returns at its budget; it is not a universal impossibility conclusion. The full thread goal remains active.

