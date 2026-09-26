# Shor closure audit: actual interface gap and same-precision repair

Researcher: EM-DIRECT-0C08F0. Research activity: RA-40F334CAC4876C16B82B0215.
Mode: directed, shared author context; not an independent review or admission.
Frozen input: Stage87 bundle HEAD `0852cad130c1d877174d235687cf60c19f318c58`.
Global canonical read: `6dff66ce260d85fc0244598cae4c527ccc133e4f`.
P000 and `ACTUAL_TYPED_BRC_ONLY` remain unchanged. No remote write by this agent.

## 1. The actual scope already excludes several suspected shortcuts

`stage78/shor_benchmark.py:prepare_and_modexp(N,a,t)` receives only N, a, t;
controlled powers are repeated squares of a modulo N. It does not receive the
unknown order or factorization. It retains the complete work labels until the
declared terminal observer. `classical_postprocess` checks every returning
exponent, evenness, and actual gcd factors. It expressly does not call a verified
returning exponent the minimal order.

`stage80/PROOF.md` already states a uniform extended-space operator bound,
including all residual modes, and its transfer to arbitrary common terminal
readout and fixed postprocessing. Its verification program computes all bins
and sums the accepted-factor subset. Thus "no error-to-success-rate bound" is
not the outstanding gap. A fixed bad base can have zero factor probability
without implying a simulation error. The source also explicitly does not claim
polynomial-time classical simulation or an autonomous native spatial circuit.
Those cannot be used as purported contradictions to its narrower theorem.

What was absent from the original benchmark was an explicit online single-shot
terminal instrument and retry/base-selection interface. This is addressed by
the other two agents' single-control-bit/instrument work, not by this audit.

## 2. A real input-dependent boundary: zero lower root endpoint

The generic fixed-word bank inherits `stage79.dyadic_parameters(max_m,32)`.
Its intervals describe the positive algebraic branch satisfying

    p x^2 + 2 x - p = 0,

computed only by the unchanged actual positive BRC path probe. The frozen bank
used in the original 12 cases contains m=2 through 10; none of those cases is
invalidated by the following deeper-input audit.

The unchanged 32-bit interface first asserts at **m=33**. Exact evidence:

    m=32: [lower, upper] = [2/2^32, 4/2^32]
    m=33: [lower, upper] = [0,       2/2^32].

The root remains positive; its certified *lower grid endpoint* becomes zero.
`dyadic_parameters` wrongly requires that endpoint itself to be strictly
positive for this extended domain. The next call also disallows p=0. This is an
interface-domain failure, not a mathematical failure of the fixed grid.

`precision_audit.py` reproduces the first failure through the original functions
and confirms the unchanged production function raises `AssertionError`. The
completed run used **1953 actual BRC kernel calls**. All earlier stages passed
the original assertions. `RESULTS.json` retains every exact interval.

## 3. Same-precision extension and proof

`zero_endpoint_extension.py` changes only the closed endpoint contract:

1. For p=0, the same polynomial is 2x and its unique nonnegative root is exactly
   zero. Return [0,0]. The actual inherited positive BRC observer verifies its
   value at x=0 and x=2^-32. No numeric root or trigonometric reference is used.
2. For p>0, call the original `root_bracket` unchanged.
3. Admit `0 <= lower <= upper < 1`. Retain the full interval and its width. Do
   not set the unknown root to zero, remove a residual, or call an unresolved
   tiny phase exactly known. The positive midpoint remains an admissible input
   to the existing fixed-word existence/error theorem.

Let r(p) denote the nonnegative root. Implicit differentiation on 0<=p<=1 gives

    r'(p) = (1-r(p)^2)/(2 p r(p)+2),  0 <= r'(p) <= 1/2.

The formula extends at p=0 by the same polynomial relation (r'(0)=1/2).
Monotonicity preserves interval inclusion. With grid spacing h=2^-32, rounding
the lower and upper roots outward enlarges width by less than 2h. Consequently

    width_m <= width_(m-1)/2 + 2h <= 4h.

The original interval/error induction therefore remains valid with a zero
lower endpoint. At every finite stage the ideal root is still positive and the
upper grid endpoint is positive, so the midpoint is positive. This extends the
typed BRC interface without changing the grid or the physical gate family.

The completed same-32-bit regression through m=34 used **1955 actual BRC kernel
calls**, with exact intervals and kernel provenance in `ZERO_ENDPOINT_RESULTS`.
Its target phase error budget for t=34 is

    sum_(m=3)^34 (35-m) width_m = 481/2^31.

Conditionally reusing the existing B=64 fixed-word theorem gives dilation

    4 L_34 / 2^32 = 1056/2^31,  L_34=528,

and combined bound **1537/2^31 < 1/1000000**. This last bound is a theorem-level
reuse, not a report that a 34-phase bank, 34-control-bit circuit, or new Shor
reference ran. The frozen main verification bank and old source were untouched.
No increase of target_bits or vector_bits was executed in the completed runs.

A preliminary launch was interrupted when the parent clarified the precision
constraint; it produced no completed certificate and is not evidence for any
claim. The completed scripts below use only the original 32-bit grid.

The extension prevents the domain assertion for deeper phases; it does not
guarantee an arbitrary t meets any requested error tolerance. Every requested
t must still carry the actual summed interval and dilation bound. A positive
interval width cannot be renamed exact resolution.

## 4. Review of the stronger streaming route

The proposed scheduling change is consistent with the frozen gate semantics:
prepare just one control bit, apply its modular-power permutation, apply its
history-controlled fixed phase words, perform its final H4, and measure it.
The same spectator and all residual modes stay in the circuit.

The change is justified because modular powers on the work register commute,
future-control preparation commutes with earlier operations that do not inspect
that future control, and the two spectator Hadamards within a round cancel
without discarding or resetting it. After that control's last H4, all remaining
uses of it are diagonal controls, so its computational projector commutes with
the remaining circuit. This is a terminal-instrument contract, not permission
to later coherently revisit the measured control.

**Ordering caveat:** history-conditioned phase words must keep the original
control-index order. The real Stage80 residual-bearing words for distinct phase
levels need not commute merely because the ideal target rotations commute.
The factor multiplying a work permutation in a one-round Kraus expression is
an ordered product, not an unordered ideal phase sum.

The resulting single-history state can use O(N D) rational amplitude slots,
with D the retained internal mode count, instead of initial Q=2^t control
enumeration. This is a real representation improvement. It is not a statement
that the *whole current implementation* takes O(N D) memory or time:

- `modular_columns` allocates a dense 2^w by 2^w graph, w=ceil(log2 N), before
  obtaining the permutation through the BRC kernel. Storage is Theta(N^2).
- The byte-verified `recurrent_mass_power(W,1)` performs both I*W and W*W using
  its dense `_multiply`, with no sparse-zero skips. That is Theta(N^3) rational
  operations per uncached table, plus coefficient bit costs.
- The table cache and number of distinct modular powers must be included.
- Rational numerator/denominator bit lengths grow; an amplitude-slot count is
  not a bit-complexity bound. Full primitive-word peak cost differs from the
  certified macro-word boundary cost.
- Enumerating every terminal history for verification still visits 2^t leaves.
  The production single-shot path must not call that verifier internally.
- N is itself exponential in the input bit length; O(N D) is not poly(log N).

## 5. Sampling and retry boundary

Exact conditional branch weights may be non-dyadic even though unconditioned
amplitudes have dyadic denominators. The sampler must use its explicit external
unbiased random-bit contract; a seeded pseudorandom test demonstrates path
replay, not a physical randomness theorem. Rejection sampling is almost surely
finite, not bounded in worst-case random-bit count. A finite bit/time budget
must return an explicit incomplete outcome without silently conditioning on
acceptance.

For the same adaptive retry/base-selection policy, if matched-history trial j
has a uniform kernel TV bound epsilon_j, the R-trial transcript TV is at most

    1 - product_j(1-epsilon_j) <= sum_j epsilon_j

(replace epsilon_j by min(1,epsilon_j) when necessary). Any deterministic factor
success event inherits this bound. It does not create a positive success
probability for a permanently bad fixed base. Exact gcd validation precludes
reporting a wrong nontrivial divisor even when the simulated law is imperfect.

## Reproduction

    python -S precision_audit.py --output RESULTS.json --activity RA-40F334CAC4876C16B82B0215
    python -S zero_endpoint_extension.py --output ZERO_ENDPOINT_RESULTS.json --activity RA-40F334CAC4876C16B82B0215

Run from this directory or use absolute script/output paths. Set
`BRC_STAGE87_SOURCE` to the recovered immutable Stage87 source directory, or
place that source in the sibling `stage87-source` directory beside `adversarial`.
The source pin above and kernel verification remain mandatory. They do not mutate
the source reproducer, control plane, original bank, or historical results.

Global-Knowledge-Sync: main@6dff66c / GLOBAL_KNOWLEDGE_V1
