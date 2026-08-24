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

## 5. Orthogonal roles of 2 and 3

The two small channels resolve complementary probe geometries.

### Same-parity pair

The chirality offsets cancel between the two probes.  Both signs produce the same shell candidate R.

The q=3 slope condition cannot distinguish them.

The q=2 parity lock

`chi=(-1)^R`

is necessary and sufficient.

### Opposite-parity pair

Changing the sign changes the shell numerator by exactly two.

The q=2 divisibility condition is unchanged, but modulo3 exactly one sign has slope divisible by3.

Thus the q=3 lock

`b=3R`

is necessary and sufficient.

Freeze:

`SAME-PARITY TWO-PROBE GLUE = CHANNEL 2`,

`OPPOSITE-PARITY TWO-PROBE GLUE = CHANNEL 3`.

## 6. Minimality ablations

### Remove channel 2

For every same-parity pair, the two chirality candidates remain indistinguishable in every odd modulus and under the slope-multiple-of-3 condition.

So channel2 cannot be replaced by any finite collection of good odd channels.

### Remove channel 3

For every opposite-parity pair, the two sign candidates differ by a shell shift of `+-1/(3d)` at the rational level.  Without enforcing 3-divisibility, the parity condition alone does not provide the universal sheet selector.

So channel3 is the unique uniform first-order slope glue for opposite-parity pairs.

### Remove both

The full odd-channel family remains the two-sheet double cover, and the sharp recovery threshold returns to a parity-mixed triple.

Thus `{2,3}` is the minimal universal arithmetic glue set for arbitrary two-probe reconstruction.

## 7. Channel/probe phase table

| available information | minimal guaranteed spatial probes | parity condition |
|---|---:|---|
| one fixed chirality sheet | 2 | none |
| odd-channel two-sheet union | 3 | both parities required |
| union + channel2 only | 2 for same-parity pairs; not universal | same parity |
| union + channel3 only | 2 for opposite-parity pairs; not universal | opposite parity |
| full native integer glue `{2,3}` | 2 | none |

## 8. Prime-valued interpretation

For an actual prime island, two indexed prime values recover its native value trajectory only because the full integer values retain the 2/3 glue.

Reducing those primes to a single large odd residue channel destroys this two-probe property and restores the hidden chirality double cover.

Therefore the value-level localization is genuinely multiscale:

- large odd channels carry the affine packet;
- channel2 carries parity chirality;
- channel3 carries native slope quantization;
- their recoalescence restores the unique integer trajectory.

## 9. Boundary

Threshold access structures and Reed-Solomon interpolation are classical.  The research-specific content is the exact native tradeoff selected by the alternating-curvature filament and the separate, indispensable roles played by the arithmetic channels 2 and3.
