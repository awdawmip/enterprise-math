# BRC Multiplier Factor Bridge — Round 3

Status: `CLASSICAL-BRIDGE IDENTIFIED / SAFE PREFILTER TOOLIZED / BASIN-PHASE SHORTCUT NEGATIVE / NO FACTORIZATION SPEEDUP CLAIM`
Date: `2026-09-06`
Parent theorem note: `research_notes/BRC_MULTIPLIER_BASIN_THEOREMS_20260906.md`
Tool family: `T0_BRC` extension; classical difference-of-squares and quadratic-residue ingredients remain prior art.

## 0. Question

After the exact multiplier-basin laws are known, can the BRC multiplication
coordinates help factor an odd semiprime `N=pq`?

The relevant point-level quantity is a square-completion gap. This round
separates three claims:

1. the exact bridge from a square BRC completion gap to a factor witness;
2. whether basin-level support/Pell phase predicts useful multipliers;
3. whether a very small residue table can safely reject most impossible square
   gaps before an exact integer-square-root test.

The first bridge is classical multiplier Fermat / difference-of-squares
mathematics. The second is experimentally negative in the present sample. The
third is a real engineering optimization but not a new factorization theorem.

## 1. Important boundary: next-square BRC cost versus Fermat completion cost

The canonical point BRC state uses

`j=floor(sqrt(mN))`.

Its downward cost is

`C_-=mN-j^2`.

The Round-1 experimental addition readout is explicitly the *next-square* cost

`C_+=(j+1)^2-mN`.

If `mN` is already a square, canonical `C_+` is positive (`2j+1`).

For difference-of-squares factoring the relevant classical completion coordinate
is instead

`x=ceil(sqrt(mN))`,
`F_+(mN)=x^2-mN`.

Thus `F_+=C_+` when `mN` is non-square, but `F_+=0` when `mN` is already a
square. The executable tool keeps these semantics separate.

## 2. Exact classical factor bridge

Suppose

`F_+(mN)=b^2`.

Then

`mN=x^2-b^2=(x-b)(x+b)`.

Therefore

`gcd(x-b,N)` and `gcd(x+b,N)`

are exact candidate factor witnesses.

For `N=pq` with distinct odd primes and `gcd(m,N)=1`, any nontrivial successful
split can be assigned, after possibly exchanging p and q, as

`x-b=u p`,
`x+b=v q`,
`u v=m`.

Conversely, for a divisor split `uv=m`, if `up` and `vq` have the same parity,
then

`x=(up+vq)/2`,
`b=(vq-up)/2`

gives

`mN=x^2-b^2`.

This witness is the *immediate ceiling-square* hit exactly when

`(x-1)^2 < mN <= x^2`,

equivalently

`b^2 < 2x-1`,

or in the `(u,v,p,q)` coordinates,

`(vq-up)^2 < 4(up+vq-1)`.

So scanning multipliers is a rational balancing search: it tries to make

`u/v` close to `q/p`.

That is the classical multiplier-Fermat mechanism (and the same difference-of-
squares idea exploited in Lehman-style multiplication). BRC supplies a typed
cost interface; it does not create a novel factoring principle here.

For odd N, `m == 2 (mod 4)` cannot be a difference of two integer squares.
The modular prefilter below automatically subsumes this obstruction when its
2-adic component is present.

## 3. Finite semiprime benchmark

Reference population:

- 143 primes in `[101,997]`;
- every distinct pair `p<q`;
- 10,153 semiprimes;
- every multiplier `m=1..100`;
- 1,015,300 `(N,m)` candidates.

All arithmetic is exact integer arithmetic.

Observed:

- 29,798 candidate pairs had an exact square completion gap and yielded the
  corresponding difference-of-squares success in this coprime sample;
- 9,696 / 10,153 semiprimes had at least one immediate successful multiplier
  `m<=100`.

The 95.5% coverage is **only a bounded small-factor diagnostic**. It is not an
asymptotic success probability and not evidence of a better factoring
complexity.

The first successful multiplier is strongly related to factor ratio, exactly as
the classical balance equation predicts. On this sample:

| q/p band | semiprimes | hit by m<=100 | hit rate | median first m |
|---|---:|---:|---:|---:|
| `<1.1` | 976 | 973 | 99.69% | 1 |
| `1.1..1.5` | 2853 | 2399 | 84.09% | 35 |
| `1.5..2` | 2003 | 2003 | 100% | 15 |
| `2..4` | 3017 | 3017 | 100% | 16 |
| `4..8` | 1197 | 1197 | 100% | 7 |
| `>=8` | 107 | 107 | 100% | 9 |

This nonmonotone multiplier behavior is another warning that the signal is
factor-ratio matching, not a universal BRC basin preference.

## 4. Basin-level BRC phase is not a useful multiplier selector here

Round 2 proved, for fixed non-square `m` in the stable regime,

`H_m(k) in {a,a+1,a+2}`,
`a=floor(sqrt(m))`,

with the lowest class caused by sparse Pell endpoint resonances.

It was tempting to use `H_m(k)` or the endpoint resonance as a cheap selector
for which multipliers deserve the square-gap test.

The finite benchmark does not support that shortcut.

### Endpoint resonance

Aggregated over nonsquare multipliers:

- nonresonant: 22,439 successes / 905,115 candidates = 2.4791%;
- resonant: 233 / 8,655 = 2.6921%.

The raw lift is small and is multiplier/population confounded.

### Support class after controlling multiplier identity

For each nonsquare multiplier having both principal classes
`H=a+1` and `H=a+2`, compare the success rates within that same multiplier.

There were 39 usable multipliers. The median ratio

`rate(H=a+2)/rate(H=a+1)`

was

`1.005007...`,

and 23/39 ratios exceeded one.

A median lift of about one half of one percent is not a useful pruning rule in
this experiment.

**Round-3 kill decision:** do not use coarse basin support size or Pell endpoint
resonance as a factor-multiplier prefilter unless a stronger independent theorem
or new evidence appears. The relevant factor information remains in the
point-level completion gap.

This is a finite negative result, not a theorem of universal statistical
independence.

## 5. Small exact square-residue table

Before calling an exact integer square-root check on

`F_+(mN)`,

test whether its residue modulo `M` can be a quadratic residue.

Define the bitset

`Q_M[r]=1 iff r == z^2 (mod M) for some z`.

Then

`Q_M[F_+ mod M]=0 -> F_+ is definitely not a square`.

Every true integer square passes, so this filter has **zero false negatives by
construction**. Passing does not prove squarehood; exact `isqrt` equality is
still required.

### Table sizes and sample rejection

| M | square residue classes | uniform pass | raw bitset | sample survivors | sample rejection |
|---:|---:|---:|---:|---:|---:|
| 1008 | 64 | 6.349% | 126 B | 79,175 | 92.20% |
| 1440 | 84 | 5.833% | 180 B | 74,862 | 92.63% |
| 1680 | 96 | 5.714% | 210 B | 73,055 | 92.80% |
| 2016 | 112 | 5.556% | 252 B | 72,063 | 92.90% |
| 2880 | 144 | 5.000% | 360 B | 66,628 | 93.44% |
| 3600 | 176 | 4.889% | 450 B | 65,741 | 93.52% |
| **4032** | **192** | **4.762% = 1/21** | **504 B** | **64,294** | **93.667%** |
| 20160 | 576 | 2.857% | 2520 B | 46,372 | 95.433% |

All 29,798 actual square gaps passed every tested modulus: zero observed false
negatives, as required by the exact residue argument.

`M=4032=64*63` is a useful compact default: its *raw mathematical payload* is
only 504 bytes while it rejected 951,006 of 1,015,300 structured sample
candidates before an exact square-root check.

`M=20160` is a stronger optional table: about 2.5 KB raw payload and 95.43%
sample rejection.

The byte figures above are the packed bitset payload `ceil(M/8)`, not Python
object-memory measurements.

## 6. Relation to the user's earlier “small table” idea

There is a genuine >90% compression/filter phenomenon here, but its scope must
be stated correctly.

The table does **not** replace a table of semiprimes and does not by itself
factor N.

It replaces most *squarehood checks* by one modular lookup:

`BRC completion gap -> 504-byte residue bitset -> reject ~93.7% in sample -> exact isqrt only on survivors`.

Thus it is a safe prefilter on the factor-witness search, not a 90% compression
of the factorization problem itself.

## 7. Toolization

`src/enterprise_math/brc_square_gap_prefilter.py` adds the classical prefilter/completion facade:

- `DEFAULT_SQUARE_RESIDUE_MODULUS=4032`;
- `square_residue_mask`;
- `square_residue_count`;
- `passes_square_residue_filter`;
- `filtered_square_root`;
- `ceiling_completion_cost`;
- `ceiling_completion_square_witness`.

The bitset is cached and exact. The final square certificate remains integer
`isqrt` equality.

Regression tests add:

- exact residue-class counts for 4032 and 20160;
- no false negatives on bounded exact squares;
- exact agreement of filtered square root with ordinary integer-square testing;
- the already-square semantic boundary;
- an immediate difference-of-squares witness example.

The existing `brc_multiplier_basin.py` theorem tool is unchanged. The benchmark is reproducible in:

`experiments/brc_multiplier_factor_bridge.py`.

Evidence table:

`research_artifacts/brc_multiplier_square_gap_prefilter_20260906.csv`.

## 8. Reuse / novelty classification

- BRC cost state and multiplier basin: reuse/extension of `T0_BRC`.
- Difference of squares / multiplier Fermat / Lehman-style multiplication:
  **classical prior art; no novelty claim**.
- Quadratic-residue bitset square prefilter:
  **classical exact optimization**, composed with the BRC completion-cost
  interface.
- Coarse basin-phase multiplier selector:
  **negative finite result / do not promote**.

No Foundation or theorem-ledger mutation is justified by this round.

## 9. Next frontier

The next worthwhile BRC question is narrower:

Can the exact retained remainder/phase trajectory across a *sequence* of
multipliers provide a reusable residue signature that is not already equivalent
to standard modular arithmetic?

Required kill condition:

if every proposed phase signature factors through a cheap classical residue
vector `(N mod M_1,...,N mod M_r)` with no stronger witness or compression, record
it as a residue-calculus facade and stop pursuing it as a new factoring route.

That is the correct next test before any claim that BRC improves factorization.
