# C88: independent review of uniform optimization and inventory designs

Reviewed by the endpoint subtask, independently of the root author of the
two reviewed notes. This review checks the new arguments and coefficients;
it does not re-run or re-certify C87's earlier numerical certificates.

Reviewed files:

* `UNIFORM_POSITION_OPTIMIZATION.md`
* `POSITION_DESIGN.md`

The source formulas were compared directly with C82 `HIGH_PRECISION.md`,
C82's two-readout normalization, the current moving-endpoint bridge, and
C85's endpoint identity.

## 1. Uniform high-precision tail

The proof of equation (1) passes the following checks.

1. Adding the middle mark can only remove collisions, even at an auxiliary
   endpoint with independent phases. Thus
   `1-Fθ(a) ≤ 1-F2(a) ≤ min(1,21/(4π²a))` holds on the whole closed position
   interval. This is a common integrable majorant after `a=t^20`.
2. The C82 negative moment away from `d=0` is independent of position.
   Choosing `s>1/20` makes its `O(L^(-2s))` contribution uniformly negligible
   after multiplication by `L^(1/10)`.
3. The source-tail substitution has outer weight `x^(-41/80)` and upper
   limit proportional to `L^(1/10)x^(121/80)`, as in C82. Taking `supθ`
   before extending the inner integral to infinity is justified by the
   common majorant; its remaining integral tends to zero by dominated
   convergence.
4. The replacement `R=1±εδ` multiplies the limiting coefficient by
   `(1±εδ)^(-1/20)`. Its difference from one is controlled using the uniform
   bound on `Iθ`, so the final `δ→0` step is also uniform.
5. `2∫₀¹x^(-41/80)dx=160/39`; the displayed `W` has the correct factor.

No rate in the original inventory `c` is obtained by this argument, and the
reviewed note correctly excludes such an inference.

## 2. Continuous-position optimization

The uniform tail and C87's stated strict concavity imply the maximum and
minimum formulas (6)--(7), without any exchange of a non-uniform extremum
and limit. If the uniform tail error is `e(L)`, comparison with an endpoint
gives `Iθ-I0≤2e(L)/W`. The chord estimate

`Iθ-I0 ≥ 2(I_(1/2)-I0) min(θ,1-θ)`

then gives the claimed quantitative bound
`dist(θ,{0,1})≤e(L)/(W(I_(1/2)-I0))`. Every minimizing position tends to the
unique maximizer of `Iθ`, namely `1/2`, by compactness and strictness.

The low-precision optimizer calculation also has the correct quadratic
factor: for `h=θ-1/2`, the leading coefficient loss is at least
`κ3 M_(3/2) h²/√2`. An `O(L⁴)` uniform remainder therefore yields
`h=O(√L)`. Neither regime proves an exact optimizer at every finite `L`,
and the reviewed note does not claim this.

## 3. Integer inventory constructions

For `A→∞`, `A=o(√c)`, the floor construction `B=⌊c/A⌋` has relative
rounding error tending to zero and gives

`D∼√A`, `A/D∼√A`, `A/B∼A²/c`, `B/c∼1/A`.

Thus it satisfies the new bridge's hypotheses. Its critical precision
`(7/4)log₂c+(1/2)log₂A+o(1)` is correctly normalized.

The more general choice `h=min(A,√(c/A))`, `B=⌊c/h⌋` also works for every
`A→∞`, `A=o(c)`: both terms defining `h` diverge,
`Ah/c≤√(A/c)→0`, and `A/√h≥√A→∞`.

For `A∼c^α`, `B∼c^β`, the exponent of `A/D` is
`α+(β-1)/2`, giving precisely `2α+β>1` as the bridge's sufficient power
condition. The two examples were checked separately:

* `(α,β)=(1/4,3/4)` gives `A/D∼c^(1/8)` and coefficient `15/8` in `p_*`.
* `(α,β)=(1/5,4/5)` gives `A/D∼c^(1/10)` and coefficient `37/20` in `p_*`.

The compact-`L_c` statement correctly handles integer precision rounding
without claiming that `L_c` itself converges along every integer inventory.

## 4. Strict information gain

The endpoint integral is normalized as
`F0(a)=2∫₀¹ℓF2(a/ℓ)dℓ`. Since `F2` is nondecreasing and tends to one,
while `F2(a)<1` at each finite positive `a`, its integrand is everywhere at
least the baseline and strictly larger on a positive-length interval.
Thus `F0(a)>F2(a)` is valid for all `a>0`.

The full two-readout uniqueness rate is bounded above by its near rate.
Combining that bound with the uniform three-readout limit and the uniform
two-readout near limit gives the displayed `liminf_c inf_α` lower bound
(9), with the infimum in the claimed order. Positivity follows because
`J>0` almost everywhere. No existence of a full two-readout limit is needed.

For `a≥1`, substitution of the exact two-readout tail gives
`F0(a)=1-7/(2π²a)`, gain `7/(4π²a)`, and remaining-ambiguity ratio `2/3`.
All three coefficients are correct. The note appropriately distinguishes
this local ratio from the full-source high-precision ratio `40/41`.

## 5. One wording clarification

In `POSITION_DESIGN.md`, the phrase "任何固定内点设计" in the actual
integer-experiment comparison should read "任何固定有理内点设计" when
invoking the existing C84 bridge. C84 proves the native bridge for fixed
rational `θ`; the auxiliary functions and their comparisons are defined
for all real `θ∈(0,1)`. This clarification does not alter a displayed
formula or a new proof. The root author was notified before publication.

Apart from that scope wording, no mathematical gap or coefficient error
was found in the reviewed new claims. The cross-reference filenames were
explicitly outside this mathematical review's scope.

## 6. Subsequent strengthening and resolution of the scope wording

The bridge subtask independently suggested a sharper low-precision
optimizer rate. This reviewer checked that improvement against the full
endpoint transition proof and incorporated it into
`UNIFORM_ENDPOINT_TRANSITION.md`, Section 7:

1. The global `O(L⁴)` remainder first places every maximizing position in
   `[1/4,3/4]` for sufficiently small `L`, using the previously established
   `O(√L)` bound.
2. On that fixed interior interval the transition proof's equation (12)
   has a uniform `O(a³)` remainder. Since `J` is bounded, its hypothesis
   `a=L²J≤min(θ,1-θ)` holds everywhere for small `L`.
3. Integration gives a uniform `O(L⁶)` remainder on the interval. The
   comparison with the midpoint now gives `h²L³=O(L⁶)`, and hence

   `|θ_L-1/2|=O(L^(3/2))`.

The earlier `O(√L)` estimate remains a valid intermediate localization;
the stronger rate requires only this bootstrap, without differentiating
the remainder.

The subsequently added `bridge/GENERAL_MOVING_POSITION.md` removes the
old rational-position limitation for actual integer sequences. Its
theorem permits arbitrary moving `A/B`, provided
`A(B-A)/√(cB)→∞` and the stated outer-gap and compact-precision conditions
hold. For each fixed real `θ∈(0,1)`, choosing integer
`A=⌊θB⌋` with `B≫c^(1/3)`, `B=o(c)` satisfies these hypotheses and gives
`A/B→θ`. The new proof handles rational near-resonances as well as
irrational limits. In particular, its two homogeneous coefficients
`-15a+240b` and, when `a=16b`, `(1125/16)b` correctly establish the stated
nondegeneracy of every nonzero `aB1+bB2` combination along the adapted flow.

Accordingly, the wording clarification in Section 5 is resolved once the
actual-inventory comparison cites this new general bridge; it no longer
needs the former fixed-rational qualifier. This is an added theorem's
scope extension, not an extension inferred from C84 alone.

## 7. Adjacent-middle full-inventory gain without branch elimination

The new `ADJACENT_MIDDLE_GAIN.md` was reviewed separately after the preceding
checks. Its conclusion does not require `A/D→∞`, and the proof correctly
retains this distinction from the full-inventory bridge.

* The displayed source-coordinate region
  `6/7<A₀<29/25`, `A₀≠1`, `11/10<d<4` agrees with the explicitly supplied
  single-macroscopic-preimage region in C83 `CRITICAL_TRANSITION.md`,
  Section 6. Since `A₀<4` and `d<4`, its inverse source coordinates satisfy
  `0<y<x<1`. A positive-area closed ball inside a regular part of this
  region supplies a suitable compact `K` with boundary of area zero.
* On that `K`, the uniqueness of the macroscopic `(G,B1)` preimage already
  forces every possible endpoint-matching competitor into the local
  branch. Both the two-readout and three-readout near limits therefore
  equal their full-competitor source contributions on `K`. No such upgrade
  is asserted for source points outside `K`.
* For each individual integer source arrangement, uniqueness under the
  shared endpoint reads implies uniqueness after adding the middle read.
  The per-source gain is nonnegative on the entire catalog. Hence the
  total gain is at least the gain from `K`, with both contributions divided
  by the same total catalog size. This justifies the localized lower
  bound without any subtraction of unrelated restricted catalogs.
* Uniform convergence of both localized contributions gives the claimed
  `liminf_c inf_α` bound. The integrand `F0(L²J)-F2(L²J)` is strictly
  positive on `K`, so `g(L)>0`. Its continuity and compactness of a fixed
  positive `L` interval give a strictly positive minimum for rounded
  precision sequences; no full-catalog three-readout limit is used.
* For `A=1` and `B=⌈c^β⌉`, `1/3<β<1`, all near-bridge hypotheses hold.
  The exact identity
  `p_*(c,B)-p_*(c,1)=-(1/2)log₂B` confirms the comparison with the
  user-supplied C78 subcritical adjacent-pair theorem. The adjacent pair
  `(c,c+1)` and the baseline outer pair `(c,c+B)` are different
  experiments, and the reviewed note keeps them distinct.

The review found no full/near confusion, phase-origin mismatch, coefficient
error, or unsupported claim of a complete `A=1` full-inventory limit.
For an entirely explicit invocation of the localized limits, `K` should be
described as having boundary of area zero, as provided by the closed-ball
choice above. The C78 premise was checked against the user's supplied
statement, not claimed to have been independently re-proved here.
