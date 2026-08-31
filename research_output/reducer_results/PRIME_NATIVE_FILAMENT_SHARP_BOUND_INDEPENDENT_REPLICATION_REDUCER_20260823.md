# Reducer Result — Native Prime Filament Sharp Bound

Task-ID: `RS-PRIME-NATIVE-FILAMENT-SHARP-BOUND-INDEPENDENT-REPLICATION`

Researcher-ID: `EM-PNFREP-E2FE4E`

Input: `research_inputs/PRIME_NATIVE_FILAMENT_BLIND_REPLICATION_PACKET_20260823.md@123cfecb25b30fe2ff9d4fddf900b6e3f2569a7a`

Source comparison: `NOT_OPENED`

## Reducer Verdict

`SHARP_FINITE_BOUND_PROVED_AND_ATTAINED`

Sharp rolling-filament bound: `L_max=5`.

## Minimal dependency chain

1. Packet neighbor formulas expand to the six fixed-sector coordinate displacements
   `(1,0),(2,1),(1,1),(-1,0),(-2,-1),(-1,-1)`.
2. For a prime center greater than `3`, parity permits exactly four neighbor slots:
   - `r+sigma` even: `1,2,5,6`;
   - `r+sigma` odd: `2,3,4,5`.
   The other two labels are even and greater than `2`; hence five or six prime neighbors are impossible.
3. Exhausting all `3*12*6=216` local mod-6 states leaves exactly
   `sigma=1` and `c=t-floor((r+1)/2)=4 mod 6`.
4. Consecutive-shell adjacency plus next-center primality forces
   `t(r+1)-t(r)=(r+sigma) mod 2`, so the integer `c` is conserved.
5. Every maximal flower is the five-term trajectory window on shells `r-2,...,r+2`. Therefore an `L`-flower filament is an `L+4`-prime trajectory run.
6. For `sigma=1`,
   `Z_c(r)=B_r+c+floor((r+1)/2)+r`.
   The complete ten-shell residue table modulo `5` has a zero for every `c mod 5`. Every relevant label in an admissible maximal filament is greater than `5`, so ten consecutive trajectory primes are impossible. Thus `L<=5`.
7. The trajectory `(sigma,c,a)=(1,-2474,10686)` contains nine consecutive primes, producing five flowers and attaining `L=5`.

## Complete extremal residue channels

After combining the local condition `c=4 mod 6` with the nine-term mod-5 gaps, the only reduced channels are

- `(sigma,a mod 10,c mod 30)=(1,1,4)`;
- `(sigma,a mod 10,c mod 30)=(1,6,16)`.

There are six presentations modulo `a mod 30`, all listed in `research_output/PRIME_NATIVE_FILAMENT_RESIDUE_CHANNELS_20260823.csv`.

## Witness reducer

Coordinates:

`(10686,2869,1)` through `(10694,2873,1)` along conserved `c=-2474`.

Prime values:

`171283421, 171315481, 171347543, 171379609, 171411677, 171443749, 171475823, 171507901, 171539981`.

The five centers are shells `10688..10692`. Every adjacent flower pair overlaps in exactly four prime labels.

Endpoint composites:

- predecessor `171251365=5*34250273`;
- successor `171572065=5*34314413`.

Independent witness certificate digest:

`sha256:cdd0e8b8ba4e72ac0cbb21920a0c5c7b012c5392f5d1bd09c22992e18e075c6f`.

## Exceptions and kill tests

- No admissible maximal flower contains `2`, `3`, or `5`.
- Boundary centers are out of scope. Removing the guard exposes boundary flowers `(4,0,1)` and `(5,1,1)` in the bounded ablation; both are rejected by the exact admissibility predicate.
- A synthetic pair sharing four values but with nonadjacent centers is rejected.
- An adjacent synthetic pair with overlap three is rejected.
- Perturbing packet neighbor slot 2 by `+1` breaks the independent coordinate implementation.
- Replacing the forced transition by its complementary step breaks conservation of `c`.

No kill test produced an admissible longer filament or an uncovered residue channel.

## Reproduction

```powershell
python experiments\prime_native_filament_sharp_bound_independent_checker.py
```

Expected: exit `0`, `digest_matches=true`, digest

`a6be930a5920699f56a1b21d71cc3314d54732f5b31809236bedadc98ac80e9a`.

Finite search range `a=2..20000`, seed `0`, first witness after `380482` eligible candidates. The upper bound is proved by complete residue coverage, not by this finite search.
