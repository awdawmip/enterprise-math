# Actual typed floor-moment unit

Status: **AUTHOR_IMPLEMENTATION_WITH_BOUNDED_ACTUAL_EVIDENCE /
SHARED_CONTEXT / NOT_ADMITTED**.

The preceding `ACTIVE_WINDOW_FLOOR_MOMENTS.md` is the symbolic proof,
SHA256 `20a93f15f241f9c3220c031032cc2af697e4d4a448669f5b637396c1a05529d4`.
It remains unchanged. This unit executes its integer counting subproblem,
including negative affine coefficients. It does not execute a new phase
bank, infer an order, or claim full active-window Gram integration.

## Interface and source mapping

`typed_floor_moments.py` is frozen at SHA256
`633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`.
The public counting interfaces are:

```python
observer = TypedFloorMoments()
moments = observer.moments(n, m, a, b)
weight = observer.window_weight(H, V, P, R, r, d)
evidence = observer.evidence()
```

`moments` returns all ten integer values indexed by `(p,e)` for p+e<=3,
with n>=0, m>=1 and signed integer a,b. `window_weight` returns J_d from
equations (5) and (11), for positive integer interval sizes H,V,P and
counting modulus R, canonical r and |d|<P. The count identity allows
general positive sizes; a Shor adapter separately binds its actual
power-of-two sizes, original history, identity-window proof and paid
order/address certificate. In this module R is a counting parameter,
not a statement that any number has multiplicative order R.

All magnitude additions, comparisons, products and divisions use the
existing `Arithmetic` interface whose traces replay actual BRC full-adder
columns. Signed integers encode a sign and a nonnegative magnitude:
host sign selection/negation changes the encoding only. Magnitude
subtraction compares typed magnitudes in the correct order; negative
Euclidean division adds one to a nonexact quotient and computes m-r
through typed arithmetic. Thus negative division uses floor, not
truncation toward zero. The signed operation ledger records inputs,
outputs and the exact underlying arithmetic-operation indices.

The implementation normalizes signed a,b, evaluates a single child
geometry for all moments, and applies the six explicit degree-three
integer lattice-transposition formulas. It uses neither ordinary
`pow`, `%`, `//`, host magnitude polynomial evaluation, nor a numerical
spectral reference to obtain its mathematical values. Fixed-degree
loop indices, binomial constants, sign representation, equality tests,
cache keys and resource metadata are declared host wiring. Exact
division by 2 or 6 rejects a nonzero remainder.

For the two shifted floor functions, the weighted-x term deliberately
uses the original x=aj+b, not the shifted affine argument inside the
floor. This preserves equations (8)--(9). The three floor sets on each
slope may share memoized geometries; they are not separate exponential
expansions of the ten scalar recurrences.

`evidence()` retains the full arithmetic traces, signed-operation map,
all computed moment nodes and weight queries, source hashes and native
primitive binding. It is an execution record, not a newly implemented
hostile-input external certificate verifier. No claim is made that
an arbitrary edited evidence JSON can be trusted by reading its status.

## Declared bounded execution

`check_typed_floor_moments.py`, SHA256
`b7a8a4e5a1da34057c3f0fc7ec95e82961fb62cbe653cfff69360a37c1e354df`,
executed eight affine problems. All ten moments matched a separate
point-by-point enumeration using the same actual typed arithmetic:

| (n,m,a,b) | Recurrence digit replays | Enumeration digit replays |
|---|---:|---:|
| (0,1,0,0) | 0 | 0 |
| (1,1,-3,-2) | 838 | 138 |
| (7,5,3,-4) | 4,739 | 1,457 |
| (6,7,-5,9) | 3,307 | 1,315 |
| (8,3,11,-13) | 7,444 | 4,077 |
| (5,11,0,-23) | 1,558 | 1,781 |
| (9,13,2,1) | 2,062 | 1,650 |
| (7,5,3,8) | 5,599 | 1,944 |

The comparison is algorithmic cross-checking, not independent foundation
validation: both routes intentionally use the same admitted primitive.
It establishes 80 actual scalar equalities. The explicit route also
reconstructs each affine integer as m*floor+remainder through typed
products/addition and checks its Euclidean remainder range.

Four window weights were compared with all ordered pairs of the free
addresses, rather than with the same floor-moment formula:

| (H,V,P,R,r,d) | J_d | Recurrence digits | Enumeration digits |
|---|---:|---:|---:|
| (2,4,4,5,1,1) | 12 | 10,169 | 4,837 |
| (4,1,2,6,5,-1) | 6 | 15,217 | 1,123 |
| (1,4,2,3,0,1) | 5 | 5,475 | 668 |
| (2,4,2,1,0,-1) | 64 | 353 | 3,770 |

There were 160 actual pair tests. These cases cover an odd modulus with
both interval-overlap pieces, even modulus, V=1, H=1, R=1, negative
window displacement, negative affine offsets and both slope signs.
Nine malformed requests (including booleans and a float) were rejected
with zero typed operations. Sources were hashed before and after the
run and were unchanged.

## Cost and raw evidence

The complete run used **one actual native core receipt**, the cached
full-adder source from which the typed digit composition is built. It
does not mean that all the counting operations cost one arithmetic
step. The recurrence routes performed **56,761 digit replays** and the
bounded explicit routes performed **22,760**. Maximum observed integer
width was 15 bits and maximum recursive depth was 7. Recorded calculation
and evidence-capture time was approximately 0.92 seconds, excluding
subsequent JSON/gzip serialization and interpreter/import startup.

The tested aggregate recurrence cost is higher. The R=1 and constant
affine cases show local savings, but this bounded run is not evidence
of a general practical speedup. The asymptotic separation from a long
interval enumeration follows from the stated Euclidean proof and
applies only with its certified active-window premises and paid
period/address acquisition.

Complete original receipts and both calculation routes are in
`TYPED_FLOOR_MOMENT_RESULTS.json.gz`:

* uncompressed bytes: 6,633,010;
* gzip bytes: 315,082;
* uncompressed payload SHA256:
  `335ae611a3056ed40077d9f5995270bd36a7c1adb15c3d7e5cf5228529cdc82e`;
* gzip SHA256:
  `a1463c0b316b3b9a0e8e67dc89e3c0ac8a937c86944ba9506647083816da29bb`.

`TYPED_FLOOR_MOMENT_SUMMARY.json` is a compact index, not a substitute
for those raw receipts. Digit counters exclude host metadata, cache
allocation, serialization, receipt storage and general implementation
bit-operation internals; they are not a total wall-clock complexity
certificate. Separate operator/bank admission and a complete signed
Gamma comparison are still needed before integrating this scalar
module into an actual active-window sampler.

In particular, sparse nonzero readouts do not imply a short active
window for the current untruncated direct-word bank. A long identity
tail must be a property of the actual bound words, not an assumption
inferred from ideal small angles or from another Stage80 bank.
