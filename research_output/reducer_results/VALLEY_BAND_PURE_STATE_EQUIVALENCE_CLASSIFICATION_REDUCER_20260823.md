# Valley Band Equivalence Reducer Results

## Terminal reducer verdict

- Researcher: `EM-VBSEQ-7021BF`
- Task: `RS-VALLEY-BAND-PURE-STATE-EQUIVALENCE-CLASSIFICATION`
- Result: **`EQUIVALENT_ONLY_AFTER_HYPOTHESIS_OR_SIGN_REPAIR`**
- Checker status: `PASS`
- Mismatch count: `0`

The reducer sought the smallest witnesses that distinguish an exact theorem from an overbroad packet claim. It minimized in the order `T`, orbit index, state, then perturbation name. The counterexamples below are logically independent of the large deterministic validation corpus.

## R1. Minimal canonical construction

For every nonsquare `T`, the canonical initializer is

`V_0=(1,-T,0), a_0=floor(sqrt(T))`.

Writing the standard complete-quotient state as `(m_n,d_n,a_n,d_{n-1})`, the minimal exact map after initialization is

`V_n=((-1)^n d_n,-(-1)^n d_{n-1},-(-1)^n m_n)` for `n>=1`.

The direct inverse is

`(m_n,d_n,d_{n-1},a_n)=(|C_n|,|A_n|,|B_n|,(s+|C_n|)//|A_n|)`.

The checker performed this round trip at all `99980` noninitial positions in the formal corpus.

## R2. Smallest refutation of the weak packet domain

`T=3` is the smallest positive odd nonsquare. The state

`V=(-2,1,-1)`

satisfies

```
C^2-AB = 3,
AB < 0,
|C| < sqrt(3),
A != 0.
```

The packet digit is `a=(1+1)//2=1`, but

`V'=(-3,-2,-3)`.

The result has `A'B'>0` and `|C'|>sqrt(3)`. The missing condition is the forward orientation `AC<0`; the full standard repair is

`sqrt(T)-|C| < |A| < sqrt(T)+|C|`

together with `AC<0` and the existing invariant/reality conditions. This is a material counterexample to the weak domain, but not to the repaired equivalence theorem.

## R3. Smallest wrong-direction quotient control

At the canonical `T=3` state after one step,

`V_1=(-2,1,1)`.

The correct digit is `(1+1)//2=1`. Replacing the numerator by `s-|C|` yields zero and a different next state. The checker rejects this at `(T,n)=(3,1)`.

## R4. Per-sign recurrence reducers

The intended update is

```
A'= +A a^2 +2C a +B,
B'= +A,
C'= +A a +C.
```

Each independent sign flip was rejected at its smallest found canonical state:

| Perturbation | Smallest `(T,n)` | State and digit | Failure |
|---|---:|---|---|
| flip sign of `Aa^2` | `(3,0)` | `(1,-3,0)`, `a=1` | expected `A'=-2`, got `-4`; invariant 5 |
| flip sign of `2Ca` | `(3,1)` | `(-2,1,1)`, `a=1` | expected `A'=1`, got `-3`; invariant -5 |
| flip sign of `B` term | `(3,0)` | `(1,-3,0)`, `a=1` | expected `A'=-2`, got 4; invariant -3 |
| flip sign of `B'=A` | `(3,0)` | `(1,-3,0)`, `a=1` | got `B'=-1`; invariant -1 |
| flip sign of `Aa` in `C'` | `(3,0)` | `(1,-3,0)`, `a=1` | reaches the opposite-orientation state `(-2,1,-1)` rather than the reference state |
| flip sign of `C` in `C'` | `(3,1)` | `(-2,1,1)`, `a=1` | expected `C'=-1`, got -3; invariant 11 |

The fifth perturbation is especially diagnostic: the polynomial invariant alone does not determine the orbit direction. State-map and sign hypotheses must also be checked.

## R5. Minimal symmetric/ambiguous nonterminal

For `T=5`,

`V=(1,-1,-2), a=4`

is repaired-reduced and maps to `-V=(-1,1,2)`. It is a one-cycle only after quotienting by global sign. It has no zero coefficient and is not terminal. This reducer separates cycle symmetry from a factor/termination event.

## R6. Square exception

For `T=9`, `s=3` and the standard first denominator is

`d_1=T-s^2=0`.

This is the genuine square-input exception and is outside the nonsquare theorem. No zero-denominator event occurs on the canonical nonsquare orbit.

## R7. Minimal modular-root degeneracies

All rows satisfy `C^2-AB=T`.

| State / modulus | Reduction modulo `p` | Exhaustive result |
|---|---|---|
| `(1,-3,0)`, `T=3`, `p=3` | invertible quadratic, `p|T` | one double root `t=0` |
| `(3,-1,1)`, `T=4`, `p=3` | `A=0`, `C!=0` | one linear root |
| `(3,-1,0)`, `T=3`, `p=3` | nonzero constant | no roots |
| `(3,-3,3)`, `T=18`, `p=3` | zero polynomial | all three roots |
| `(2,-1,1)`, `T=3`, `p=2` | constant one | no roots |
| `(2,-2,1)`, `T=5`, `p=2` | zero polynomial | both roots |

Together with ordinary split/nonresidue cases, these hit every branch of the proved root classification. The formal run compared analytic roots with all residue classes in `13602` state/prime cases.

## R8. Relation-semantic reducers

At the initialization for `T=N=5`, `D(t)=t^2-5` and the local witness is `t`:

| `t` | Signed value `D(t)` | Purpose |
|---:|---:|---|
| 2 | -1 | omitting the `-1` parity falsely resembles a square dependency and is rejected |
| 3 | 4=`2^2` | verifies square-factor half exponent |
| `+/-6` | 31 | verifies single-large-prime pairing |
| `+/-28` | 779=`19*41` | verifies a two-parallel-edge double-large-prime graph cycle |

For a general closed state, the analogous state-only right-hand side is `A D(t)`, not `D(t)`. The checker selected an actual relation for which dropping `A` fails the congruence and required rejection. It also mutated a witness and required rejection.

## R9. Formal non-reducer corpus

The reducer witnesses above are accompanied by, but do not depend on, the following broad checks:

- 20 SHA-256-derived balanced exact 80-bit semiprimes;
- 5,000 candidate/reference pairs per semiprime, `100000` total;
- paired-stream SHA-256 `cdfc900c1daaeaf21cd353795c72a5569cc0500e8403c0e1e2dd28e969ad607c`;
- 2,848,992 modular residue evaluations;
- 2,732 accumulated-matrix/local-band identity checks;
- 2,448 completely factored signed band relations;
- 256 verified even-exponent dependencies, 180 with nontrivial factors in the controlled small-composite corpus;
- zero mismatches.

## Reducer closure

No reduced witness refutes the repaired theorem. The weak packet claim is refuted at the mathematical minimum, while the repaired state map, form map, root cases, and relation semantics all have symbolic proofs and independent executable checks. The precise terminal classification is therefore:

**`EQUIVALENT_ONLY_AFTER_HYPOTHESIS_OR_SIGN_REPAIR`**.
