# Symbolic review and typed call graph

Reviewed source: `DIFFERENCE_AUTOCORRELATION.md`, SHA-256 `c0c3765fce7d07f383f1ebfcb514dd8483485944bfeb202d024dd21e69205cbf`.

Conclusion: no substantive mathematical defect found. This is a shared-context, source-specific symbolic review, including a read of the frozen `TypedFloorMoments` API. No host numerical reference, scientific execution, new provider query, implementation, or formal admission was performed for this review. The completed endpoint stage is unchanged.

## Tail count and polynomial checks

For `0<s<=U`, the tail `x in [0,P-s)` splits at `U-s` and `U`. Its two positive portions have length `U-s` each and its negative portion has length `s`, giving `P-3s`. For `U<=s<P`, that whole tail has positive `w(x)` and negative `w(x+s)`, so its sum is `-(P-s)=s-P`. These are integer counts with half-open endpoints. At `s=U` both expressions are `-U`.

Over a full period the positive and negative lengths give `P-4s` for the first half and `4s-3P` for the second. The overlap length is `(H-q-1)P+(P-s)` for `s>0`, with a nonnegative number of full periods because `d<L` implies `q<H`. Combining this with the tail gives exactly the two stated formulas. At `s=0`, the overlap instead consists of `H-q` full periods, and the low formula gives this directly. No fictitious tail is added.

Substitution of `s=d-Pq` in the low expression yields

    HP + (4H-2)Pq + 4dq - 4Pq^2 + (1-4H)d.

The branch difference is

    2(2(H-q)-1)(2s-P),

which expands to the draft's five terms. The coefficient of `Pq` is `(8-8H)`, including both separate `4Pq` contributions; omitting one would be an error, but the draft retains both. The zero at `s=U` makes either branch correct there.

There are useful symbolic endpoint checks. At the highest bit `H=1`, the two tails give the direct correlation of one square-wave period. At the lowest bit `U=1`, the only residues are `s=0,1`; the formulas reduce respectively to `A(d)=L-d` and `A(d)=-(L-d)`. Thus the generic expression reduces to `(-1)^d(L-d)` as required. These checks are algebraic substitutions, not executed test values.

## Delta reductions

Since `P=2U` and `0<=s<P`, the quantity `delta=floor((d+U)/P)-floor(d/P)` is zero for `s<U` and one for `s>=U`. For each summand, writing the unshifted quotient as `q`,

    Delta(q)   = delta,
    Delta(q^2) = (2q+1)delta,
    Delta(q^3) = (3q^2+3q+1)delta.

Therefore

    2 Delta(q^3)-3 Delta(q^2)+Delta(q) = 6q^2 delta.

The divisions by two and six in the draft are exact. Multiplication by the external progression index `j` gives the corresponding `j*q*delta` identity without changing the quotient. No `q^3*delta` or degree-four moment is needed. All required table entries have `p+t<=3`: `(0,1)`, `(1,1)`, `(0,2)`, `(1,2)`, `(0,3)`, plus the unweighted entries such as `(1,0)` already returned by the same API.

The weighted quantities `S_d`, `S_dq`, `S_ddelta`, and `S_dqdelta` follow by distributing `d=b+a*j`. Substituting them in the expanded low formula and its delta correction gives every term of the stated `SumA`, with the same sign and coefficient. The unweighted term `n*H*P` appears once per progression, not once per moment table.

## Alias orientation and range boundaries

The nonnegative difference branch is `d=r+jR`, starting at `j=0`. The negative difference branch has strictly positive magnitudes `d=R-r+jR`, also starting at zero. Since `0<=r<R`, the latter head is always positive. For `r=0`, only the first branch includes zero, while positive multiples of `R` need both orientations. For even `R` and `r=R/2`, the two lists of magnitudes coincide, but they represent different signed differences: both contributions must be added. Computational reuse of an identical progression is permissible only with the explicit doubled contribution retained.

For any nonnegative head `b`, `b>=L` means the progression is empty. Otherwise `L-1-b>=0`, and `1+floor((L-1-b)/R)` is exactly the number of admissible terms. The formula includes the last allowed integer displacement and excludes `d=L`. These facts also handle `R=1`, `R=L`, `R>L`, a zero head, and a nonzero head at the interval boundary. An empty progression can return the exact zero additive identity without requesting a moment table.

The negative-displacement identity here is specific to the real scalar product `w(x)w(y)`: exchanging the ordered endpoints preserves that product. It does not reverse noncommuting matrix products or replace the transposition rule for a general seed. The combined scalar result retains the old raw normalization `4^(-g)`.

## Concrete actual-typed API mapping

The frozen source `TypedFloorMoments`, SHA-256 `633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`, already supplies `add`, `sub`, `mul`, `floor_div`, `exact_div`, `total`, and `moments(n,m,a,b)`. Its moment output is a dictionary indexed by `(p,t)`, and its signed arithmetic is backed by the existing actual full-adder composition. No new numerical propagation primitive is required.

A feasible explicit call graph is:

1. Validate the frozen strict integer contract. Build `U=2^k` and `H=2^(g-k-1)` by actual typed doubling, then `P=add(U,U)` and `L=mul(H,P)`. Precompute the common polynomial coefficients using the same signed typed operations. Public loop lengths and fixed moment indices are wiring, not unrecorded numerical answers.
2. Form the heads as the given `r` and actual `sub(R,r)`. For each head, compute `z=sub(sub(L,1),b)`. If its recorded sign is negative, return zero for this empty branch. Otherwise call `floor_div(z,R)` and set `n=add(quotient,1)`. This avoids a host-computed progression length.
3. Request `M=moments(n,P,R,b)` and `M_plus=moments(n,P,R,add(b,U))`. Positive `R`, the power-of-two modulus, and potentially larger coefficients/offsets are all covered by the existing normalized floor-moment contract.
4. Obtain each needed `Delta[p,t]` with actual subtraction. Construct the two halves and the one sixth through `exact_div`, preserving their remainder-zero checks and receipts. Form `S_d` as `add(mul(b,n),mul(R,M[1,0]))`: the existing table already contains `sum j`, so a separate computation of `n(n-1)/2` is unnecessary. Form the three other weighted sums with actual multiply/add operations.
5. Evaluate the ten displayed terms with typed signed multiplication and `total`. Add both orientation contributions with actual addition. Retain negative answers and the unchanged denominator exponent. A highest/lowest endpoint shortcut remains a separately identified route; do not silently relabel its old certificate as this direct formula.
6. Bind the complete input, source/proof hashes, scales, heads, empty/nonempty decisions, `n`, both moment-table parameters and outputs, delta reductions, exact divisions and outer-expression operation ranges. Replay must rebuild this chain from the inputs, including both orientations, rather than trusting a supplied branch, table, or coefficient.

The frozen runner records recursive moment nodes and aggregate requests/cache hits. A wrapper should additionally retain its top-level table parameters and outputs so cached and newly computed table uses both have explicit provenance. The final certificate must retain the entire underlying integer evidence. No table entry or division may be filled with an untraced host calculation.

## Cost interpretation

There are at most four **top-level table requests** for the two nonempty progressions, each returning all ten total-degree-at-most-three moments. There can be many recursive nodes and signed arithmetic operations within one request. In particular, the frozen implementation computes all ten moments even when a formula uses only a subset; the unused computation must not disappear from the resource account.

Compared with the frozen one-window path, the direct formulation changes the moment modulus from `R` to `P` and normally reduces six possible initial table requests (three for each affine slope) to at most four. It also replaces the unsigned weight construction with a signed polynomial combination. This is a plausible practical improvement for some interior inputs, not a proven uniform cost reduction.

There are clear countervailing costs. When `U mod R=0`, the existing affine-weight routine uses a constant-count early return and requests no moments; the direct formula may still do substantial table and cancellation work. Different quotient bit lengths, Euclidean depths, repeated subproblems and cache hits can dominate the nominal table count. Endpoint formulas already require only one or two interval counts and no moments. An implementation should preserve those options, measure complete production and replay digits, and report regressions as well as savings. Neither formula discovers the counting period/address or compresses arbitrary full-matrix correlations.

The reviewed result is ready for a separately versioned implementation under the current actual-typed contract. This review does not authorize or assert a completed execution. The first comparison can use the same hash-bound 31 historical answers without rerunning the old exhaustive science; any additional fixture must be separately declared.

Global-Knowledge-Sync: main@bd2873d / GLOBAL_KNOWLEDGE_V1
