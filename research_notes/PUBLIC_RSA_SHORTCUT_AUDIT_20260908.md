# Public RSA Challenge Opportunistic Shortcut Audit — 2026-09-08

Status: `FINITE PUBLIC-INPUT AUDIT / ZERO HITS / CURRENT NEIGHBOR-SQUARE LINE PAUSED`

## Scope

Publicly listed unfactored RSA challenge numbers from RSA-260 through RSA-2048 were tested with the current low-cost opportunistic shortcut stack only. No long-horizon factorization, GNFS, or open-ended search was attempted.

Inputs: 31 challenge moduli currently listed as unfactored in the public RSA-number table:
RSA-260, RSA-270, RSA-896, RSA-280, RSA-290, RSA-300, RSA-309,
RSA-1024, RSA-310, RSA-320, RSA-330, RSA-340, RSA-350, RSA-360,
RSA-370, RSA-380, RSA-390, RSA-400, RSA-410, RSA-420, RSA-430,
RSA-440, RSA-450, RSA-460, RSA-1536, RSA-470, RSA-480, RSA-490,
RSA-500, RSA-617, RSA-2048.

## Exact probes

1. Current complete irredundant odd-N multiplier set for `m<=100`: 62 multipliers.
2. Existing 13-squarefree-kernel opportunistic prefix in `m<=1000`: 98 multipliers.
3. `t0.brc_neighbor_square_lift_shortcut` with ordinary horizon `H=100`, compressed local power-of-two neighbor window `D=64`, and `all_levels=True`.

All square completions were exact integer tests. The local-neighbor candidate generator is exact for the declared `(H,D)` regime.

## Result

- `m<=100` exact multiplier-Fermat factor hits: `0/31`.
- kernel13 prefix factor hits: `0/31`.
- compressed `H=100,D=64` neighbor-square factor hits: `0/31`.
- Only RSA-260 generated any beyond-100 local-neighbor candidates.
- RSA-260 has `N mod 1024 = 983`, giving the unique signed local distance `d=41` on the `N+41` side and `v2(N+41)=12`.
- The beyond-horizon power-of-two levels produce `m=105` and `m=169`.
- Both induced square-test values are rejected already by the first BALANCED quadratic-residue stage (mod 4032), hence no exact `isqrt` is required in the production path.
- The other 30 public challenge numbers generate no beyond-100 candidate at all for this exact `D=64` compressed branch.

Therefore the current local neighbor-square/divisor-layer execution line has no hit on the public challenge set.

## Decision

Per the user-requested stop rule:

`PUBLIC RSA AUDIT ZERO HIT -> PAUSE THIS RESEARCH LINE`.

Do not enlarge `D`, do not increase the ordinary multiplier horizon because of this audit, and do not infer a negative theorem from the finite sample. Retain the tool in the opportunistic portfolio as a near-zero-cost exact free option for future inputs.

This audit does not make any claim about the security of RSA or about asymptotic factorization complexity.
