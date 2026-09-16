# RSA-270：离散导数尖峰定理与 BRC 进位自动机（第 3 轮：坐标系/BRC/离散理念）

Progress-Event-ID: `rsa270-discrete-spike-carry-automaton-6d4e8b`
At: `2026-09-06T17:00+08:00`
Scope: `enterprise-math / RSA-270 / shortcut hunt (Enterprise coordinates + BRC + discrete philosophy)`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journals 5d8a2c/3c9b7d; P000 assumed`
Kind: `PROGRESS / EXACT THEOREMS`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Round 3 of the shortcut hunt, explicitly using the three frameworks: Enterprise coordinate system, BRC philosophy, discrete philosophy. No factor obtained.

### 1. Discrete-derivative spike theorem (exact, verified)

The profile `P(u)` is `{0,2,4}`-valued on a step-2 lattice. Its forward discrete difference `dP(e) = P(e) - P(e-2)` has exactly four nonzero jumps:

- outer pair (N-only): `dP(-(N-1)/2) = +2`, `dP(+(N+3)/2) = -2`;
- inner pair (factor-bearing): `dP(-(S-2)/2) = +2`, `dP(+(S+2)/2) = -2`.

The inner jump pair sits at `-(A-1), +(A+1)` with `A = S/2` (Fermat midpoint, the Enterprise native axis-difference reading of the plateau boundary). Hence: **factoring <=> locating the inner jump pair of the discrete derivative**; the outer pair is exactly computable from N. Verified on 5 synthetic semiprimes (PASS; an earlier test-rig off-by-one in the loop start and the expected jump positions were corrected).

RSA-270: inner jumps at `e = -(A-1), +(A+1)` with `A = 8 mod 36` (from `S = 16 mod 72`); outer jumps at `e = +-(N+1)/2` = `+- 116554265172203772263818828455340262072809906240152724521474305984247959122567891433944184659288558209106959634286329157456530336313455677013804896583170813346973298098213872136943300938448156734352029533373451561955374138803274324575960406349654883293757367728297496604` (exact, N-only).

### 2. BRC carry automaton of the addition N + (S+1) = sigma(N)

Digit towers (computed exactly):

- 2-adic (unconditional): pair-classes `1,2,4,8,16,32,64,128` per digit (x2), S-classes `1,1,1,2,4,8,16,32`;
- 3-adic (prior p,q=2 mod 3): pair-classes `1,3,9,27` (x3), S-classes `1,1,2,4`.

BRC reading: the addition collapse (carry quotient) **erases exactly 1 bit of S per digit beyond the forced depth** (`a=3`, `b=2`); the forced lattice `S = 16 mod 72` is the initial carry-free segment; pair-space grows geometrically while S-space doubles per digit — the collapse's information-loss rate is exactly 1 bit/digit. This is the discrete-theory formulation of the 7c4d1f forced-lattice and 9f3b12 residue ladder: all three coincide.

### Status

The three frameworks converge on one object: the single scalar `S` (equivalently `A = S/2`, equivalently `sigma(N)`). Every observable family derived so far — torsion ladder, moments, mod-collapses, coarse-grains, truncations, zero sets, discrete-derivative spikes, carry automata — is an exact function of `S` whose N-only computable part is exactly `S = 16 mod 72` (~6.17 bits). RSA-270 factorization is **not achieved**; no route to sub-`O(sqrt(N))` recovery of `S` exists in any of the tested frameworks, and the wall is identical to the QR/`phi(N)`-mod hardness boundary. No exhaustive or traditional algorithm was used.

## Artifacts

- Script: `rsa270_spike_carry.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T161500+0800-rsa270-zero-set-gcd-classification-3c9b7d.md`.

## Next

The exact-identity/coordinate/BRC/discrete surface is now fully enumerated and closed; the same blocking condition (no known sub-`O(sqrt(N))` N-only recovery of `S`; RSA-270 publicly unfactored) has persisted across this goal's consecutive rounds. See the blocked assessment in the goal state.
