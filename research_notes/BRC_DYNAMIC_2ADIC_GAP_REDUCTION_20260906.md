# BRC dynamic 2-adic gap reduction and retained-class boundary

Status: `PROVED STATE-DEPENDENT REDUCTION / BOUNDED MAXIMALITY WITNESSES / NO NEW FACTORIZATION COMPLEXITY CLAIM`
Date: `2026-09-06`
Parent: `t0.brc_multiplier_priority_jump`

## 1. Question

After the exact static reduction to multiplier residues `{0,1,3,5,7} mod 8`, can a known BRC state eliminate still more square-gap tests without losing a factor witness?

Yes, but the next reduction is **N-visible/state-dependent**, not another uniform multiplier residue deletion.

## 2. Dynamic reduction theorem

Let N be odd and suppose the exact BRC state at multiplier m gives

`x = ceil(sqrt(mN))`.

Assume `4|m` and x is even. If the completion gap is a square,

`y^2 = x^2-mN`,

then y is also even. Write

`m=4l`, `x=2X`, `y=2Y`.

Then

`lN = X^2-Y^2`.

Moreover `x=ceil(2sqrt(lN))=2X` implies

`X=ceil(sqrt(lN))`.

Finally, because N is odd,

`gcd(x-y,N)=gcd(2(X-Y),N)=gcd(X-Y,N)`.

Therefore every successful state with `4|m` and even ceiling root is redundant with the smaller multiplier m/4 and the same gcd factor.

The reduction may be repeated while the reduced multiplier is divisible by 4 and the correspondingly halved ceiling root remains even.

## 3. Exact state representative

The executable function

`odd_n_ceiling_state_scan_representative(m,x)`

performs that repeated reduction using only the multiplier and the already-known BRC ceiling root.

After reductions:

- landing in `m == 2 (mod 4)` returns `None`, because the difference-of-squares target is impossible;
- landing in `m == 4 (mod 8)` with an odd reduced ceiling root also returns `None`: a putative odd-odd square difference would be divisible by 8, contradicting v2(target)=2;
- returning a smaller multiplier means any success is redundant with that smaller immediate witness;
- returning the original multiplier means this 2-adic rule cannot eliminate the state.

`DirectMultiplierJumpState` exposes the same result as `state.scan_representative` and the Boolean readout `state.gap_test_is_irredundant`.

This does not change the static 62-candidate set. It is an optional exact filter after root/remainder transport and before modular/square gap testing.

## 4. Finite effect

Among the 62 static representatives in `1..100`, only the retained `0 mod 8` branch can be dynamically reduced by this rule. On random odd 64..2048-bit integers, a research harness found roughly 56 of the 62 states per N remained gap-test irredundant on average; about six additional gap tests were removed.

On the prior small semiprime population, inserting smaller representatives immediately reduced the mean number of gap tests before a hit from about 8.67 to 7.56, but increased mean BRC jump states from about 8.67 to 9.28. Therefore this is **not** promoted as a new default ordering policy. It is best treated as a zero-loss gap-test filter in long-stream or batch settings where the BRC state is already available.

These numbers are finite implementation diagnostics, not probabilistic theorems.

## 5. Why the whole 0 mod 8 branch cannot be deleted

The static mod-8 reduction is already sharp at the level of whole residue classes. Each retained class occurs as an actual first successful irredundant multiplier:

- residue 1: `N=15=3*5`, first hit `m=1`;
- residue 3: `N=33=3*11`, first hit `m=3`;
- residue 5: `N=69=3*23`, first hit `m=5`;
- residue 7: `N=87=3*29`, first hit `m=7`;
- residue 0: `N=527=17*31`, first hit `m=8`, with odd ceiling root 65.

Thus no one of `{0,1,3,5,7} mod 8` may be uniformly removed while preserving all immediate factor witnesses.

The even retained branch also survives a mod-32 refinement. Genuine first hits occur in all four multiples-of-8 residue classes:

- `m=8 mod 32`: `N=527`, first hit 8;
- `m=16 mod 32`: `N=6437=41*157`, first hit 16;
- `m=24 mod 32`: `N=16801=53*317`, first hit 24;
- `m=0 mod 32`: `N=39973=71*563`, first hit 32.

All four corresponding ceiling roots are odd, so the dynamic even-root reduction correctly leaves them alive.

These examples are bounded obstruction witnesses, not a theorem that no more sophisticated non-residue-based exact compression exists.

## 6. Strategic interpretation

The odd-N multiplier surface now separates into two exact layers:

1. **static 2-adic quotient:** raw multipliers -> residues `{0,1,3,5,7} mod 8`;
2. **dynamic BRC quotient:** within retained multiples of 8, even ceiling-root states reduce to smaller multipliers or impossibility.

The second layer depends on the retained BRC root/remainder state and therefore cannot be represented by an N-independent multiplier list alone.

This is another constructive example of the project's observer principle: the root/remainder state contains operational information that a static multiplier class does not.

## 7. Boundary

This is a constant-factor exact reduction of square-gap tests. It does not alter the Hart/Lehman `N^(1/3)` candidate horizon, does not imply RSA-scale factorization, and does not make a novelty-priority claim outside the present Enterprise derivation.
