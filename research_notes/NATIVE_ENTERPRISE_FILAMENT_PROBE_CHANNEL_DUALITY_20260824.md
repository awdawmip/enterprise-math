# Native Enterprise filament codes: probe-channel duality and minimal small-channel glue

Status: `FREE_RESEARCH_EXACT_INFORMATION_TRADEOFF / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_FILAMENT_CHIRAL_DOUBLE_COVER_ACCESS_STRUCTURE_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_INTEGER_ARITHMETIC_GLUE_TWO_PROBE_DECODER_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_DUAL_SYNDROME_DISCRIMINANT_IDENTITY_20260824.md`.

## 1. Odd-channel observation model

Fix an odd prime

`q>max(3,k-1)`.

A length-k native filament packet reduces to one of two affine sheets

`C_k,q^chi=eta^chi+RS_q(k,2)`.

The hidden state has three pieces:

- affine intercept a;
- affine slope b;
- chirality `chi in {+1,-1}`.

The odd field forgets the two global arithmetic locks

`b=3R`,

`chi=(-1)^R`,

because 3 is invertible and a residue class R modulo q does not retain integer parity.

## 2. Pure spatial-probe threshold

Without external channel information:

- one probe does not determine `(a,b)`;
- any two probes determine one candidate on each chirality sheet, so chi remains perfectly hidden;
- any parity-mixed triple determines chi by the dual syndrome and then recovers `(a,b)`;
- any same-parity observation set, of arbitrary size, remains chirality-blind.

Thus the minimal pure spatial decoder is

`THREE PROBES WITH BOTH PARITIES`.

This is sharp.

## 3. One supplied mode bit lowers the threshold

If chi is supplied externally, the packet is one `[k,2,k-1]` affine MDS sheet.

Then any two distinct probes recover `(a,b)` and the full packet.

Therefore

`ONE MODE BIT + TWO PROBES`

is equivalent, for complete recovery, to

`ONE PARITY-MIXED TRIPLE`.

The third spatial probe is precisely a relational measurement of the missing C2 mode.

## 4. Integer arithmetic supplies the mode bit implicitly

For full integer values, no extra probe is needed.

Given two indexed values, the native conditions

`b=3R`

and

`chi=(-1)^R`

select one of the two odd-channel sheets uniquely.

Hence

`TWO INTEGER PROBES`

recover the complete infinite native filament sequence.

This is a strict threshold reduction from the odd-channel projection:

`ODD RESIDUE CARRIER: 3 MIXED-PARITY PROBES`,

`INTEGER NATIVE CARRIER: 2 ARBITRARY PROBES`.

## 5. Complementary roles of 2, 3 and index-distance integrality

Let the two probe positions be separated by

`d=j-i`.

### Same-parity pair

The chirality offsets cancel between the two probes.  Both signs produce the same shell candidate R.

Neither the q=3 slope condition nor index-distance divisibility distinguishes them.

The q=2 parity lock

`chi=(-1)^R`

is necessary and sufficient.

### Opposite-parity pair

Changing the sign changes the pre-slope numerator by exactly two.

There are two possible selectors:

1. exact divisibility by the index distance d;
2. the native q=3 slope lock `b=3R`.

Because opposite-parity positions have odd d, if `d>1` then `2d` cannot divide the difference2.  Since the true pre-slope numerator is divisible by `2d`, the false one is not.  Therefore every nonadjacent opposite-parity pair is already resolved by exact index-distance integrality.

If `d=1`, both pre-slopes are integral and differ by one; then exactly one is divisible by3.  Therefore channel3 is genuinely necessary for the adjacent opposite-parity pair and is the unique selector that works uniformly for every opposite-parity separation.

Freeze the precise form:

`SAME-PARITY UNIVERSAL GLUE = CHANNEL 2`,

`NONADJACENT OPPOSITE-PARITY GLUE = INDEX-DISTANCE INTEGRALITY`,

`ADJACENT OPPOSITE-PARITY GLUE = CHANNEL 3`.

## 6. Minimality ablations

### Remove channel 2

For every same-parity pair, the two chirality candidates remain indistinguishable in every odd modulus and under all slope/index divisibility conditions.

So channel2 cannot be replaced by any finite collection of good odd channels.

### Remove channel 3

Every nonadjacent opposite-parity pair remains decodable because its index distance rejects the false pre-slope candidate.

However adjacent opposite-parity pairs retain two integral pre-slopes differing by one, and parity alone does not select the correct one uniformly.  The multiple-of-3 slope law is then indispensable.

Thus channel3 is necessary for a decoder required to work for **arbitrary** two-probe placement, although it is not needed for nonadjacent opposite-parity pairs.

### Remove both

The full good-odd-channel family remains the two-sheet double cover, and the sharp carrier-only recovery threshold returns to a parity-mixed triple.

Therefore `{2,3}` is the minimal universal arithmetic channel set for arbitrary two-probe reconstruction; exact index distance supplies a third, geometric selector on nonadjacent opposite-parity pairs.

## 7. Channel/probe phase table

| available information | minimal guaranteed spatial probes | qualification |
|---|---:|---|
| one fixed chirality sheet | 2 | none |
| good-odd-channel two-sheet union | 3 | both parities required |
| union + channel2 | 2 for same-parity pairs | not universal for opposite parity |
| union + exact index divisibility | 2 for every nonadjacent opposite-parity pair | fails for adjacent pairs |
| union + channel3 | 2 for every opposite-parity pair | not universal for same parity |
| full native integer glue `{2,3}` | 2 | arbitrary distinct positions |

## 8. Prime-valued interpretation

For an actual prime island, two indexed prime values recover its native value trajectory only because the full integer values retain the small-channel and integrality glue.

Reducing those primes to a single large odd residue channel destroys this two-probe property and restores the hidden chirality double cover.

Therefore the value-level localization is genuinely multiscale:

- large odd channels carry the affine packet;
- channel2 carries parity chirality;
- exact index separation resolves nonadjacent parity bridges;
- channel3 quantizes adjacent parity bridges;
- their recoalescence restores the unique integer trajectory.

## 9. Boundary

Threshold access structures and Reed-Solomon interpolation are classical.  The research-specific content is the exact native tradeoff selected by the alternating-curvature filament and the distinct roles played by channels2,3 and discrete probe separation.
