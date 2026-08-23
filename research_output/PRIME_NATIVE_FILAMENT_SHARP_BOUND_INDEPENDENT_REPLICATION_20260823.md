# Native Prime Filament — Sharp-Bound Independent Replication

Task-ID: `RS-PRIME-NATIVE-FILAMENT-SHARP-BOUND-INDEPENDENT-REPLICATION`

Researcher-ID: `EM-PNFREP-E2FE4E`

Frozen source commit: `12725505c636449df7dd913ac06e581bf418b89c`

Locked packet ref: `123cfecb25b30fe2ff9d4fddf900b6e3f2569a7a`

Independent checker result digest: `sha256:a6be930a5920699f56a1b21d71cc3314d54732f5b31809236bedadc98ac80e9a`

## 1. Executive Summary

The sharp nonexceptional bound is **five flowers**. More precisely, every admissible rolling overlap filament has length

`L <= 5`,

and this is attained by an exact five-flower witness whose nine union labels are independently certified prime.

The proof is local-to-global. Packet algebra identifies the six neighbor slots with coordinate displacements

`(1,0), (2,1), (1,1), (-1,0), (-2,-1), (-1,-1)`

at fixed sector. Parity leaves exactly four prime-eligible neighbor slots. A complete mod-6 state classification then forces every maximal flower into physical sector `sigma=1` with

`c = t - floor((r+sigma)/2) = 4 (mod 6)`.

Consecutive maximal flowers can therefore roll only by

`t(r+1)-t(r) = (r+sigma) mod 2`,

which conserves the integer `c`. Each maximal flower is exactly a five-term window on that trajectory, so a filament of length `L` is equivalent to `L+4` consecutive prime trajectory labels.

For `sigma=1`, the trajectory label is

`Z_c(r) = B_r + c + floor((r+1)/2) + r`.

Its residue sequence modulo `5` has period `10`, and for every `c mod 5` at least one of the ten residues is zero. A valid maximal filament contains no label `5`, so ten consecutive trajectory primes are impossible. This proves `L+4 <= 9`, hence `L<=5` globally. The witness supplies nine consecutive primes and closes sharpness.

### Sources Read Before Freeze

Mathematical input was limited to:

- `research_inputs/PRIME_NATIVE_FILAMENT_BLIND_REPLICATION_PACKET_20260823.md@123cfecb25b30fe2ff9d4fddf900b6e3f2569a7a`.

Process-only inputs were the account bootstrap/manual/sync protocol, repository `AGENTS.md`, and this exact taskbook. No maximal-flower or filament source note, script, witness, residue table, free-research branch, PR diff, or source theorem content was opened.

During connector setup, a generic recent-commit query exposed only the title `journal: capture six-lane prime research taskbook dispatch`. No body, diff, theorem statement, numerical bound, residue channel, or witness was exposed. This title-only procedural exposure did not supply mathematical information and is recorded here rather than hidden.

### Outcome-Blindness Statement

The bound `5`, the two extremal residue families, and the witness below were derived and frozen without reading the withheld result. No source comparison was performed. This report stops at the source-comparison boundary.

## 2. Certified Claims

### Exact definitions used

For `r>=4`, `sigma in {0,1,2}`, and `2<=t<=r-2`, set

`B_r = 1 + 3r(r-1)/2`,

`N(r,t,sigma)=B_r+t+sigma*r`.

The ordered neighbor list is exactly the six-label list in the locked packet. A maximal prime flower has prime center `>3` and exactly four prime neighbors. A rolling filament is a consecutive-shell sequence of such flowers with adjacent centers and prime-set overlap exactly four.

### Lemma 1 — coordinate form of all six neighbors

Direct expansion gives

| Packet slot | Coordinate |
|---:|---|
| 1 | `(r+1,t,sigma)` |
| 2 | `(r+2,t+1,sigma)` |
| 3 | `(r+1,t+1,sigma)` |
| 4 | `(r-1,t,sigma)` |
| 5 | `(r-2,t-1,sigma)` |
| 6 | `(r-1,t-1,sigma)` |

For example, `B_(r+2)-B_r=6r+3`, so slot 2 equals

`B_(r+2)+(t+1)+sigma(r+2)=N(r,t,sigma)+6r+4+2sigma`.

The other five identities follow from

`B_(r+1)-B_r=3r`, `B_(r-1)-B_r=-3r+3`, and `B_(r-2)-B_r=-6r+9`.

Thus only slots 1 and 3 can be adjacent centers on shell `r+1`, and sector `sigma` is conserved by carrier adjacency in the interior.

### Lemma 2 — five or six prime neighbors are impossible

Let `epsilon=(r+sigma) mod 2`. The center is odd because it is prime and greater than `3`. Slots 2 and 5 have even offsets and hence odd labels. Slots 1 and 6 have offset parity `epsilon`; slots 3 and 4 have offset parity `epsilon+1`.

- If `epsilon=0`, only slots `1,2,5,6` can be prime.
- If `epsilon=1`, only slots `2,3,4,5` can be prime.

The other two labels are even. The outer forbidden label exceeds the center, while the inner forbidden label is at least `N(3,1,0)=11`; hence neither can equal `2`. Therefore every admissible prime center has at most four prime neighbors. Five and six are impossible, with no admissible small-prime exception.

A center is maximal exactly when the center and all four parity-eligible neighbors are prime.

### Local-State Classification

Modulo `6`, `B_r` has period `4`; all carrier residues and parity eligibility are therefore determined by

`(sigma, r mod 12, t mod 6)`.

The checker exhausts all `3*12*6=216` states. Exactly 12 survive the requirement that the center and four eligible neighbors be coprime to `6`. They are all and only

`sigma=1`,

`c=t-floor((r+1)/2)=4 (mod 6)`.

For each `r mod 12` there is one surviving `t mod 6`; both shell parities occur. The complete 12-row table is in `research_output/PRIME_NATIVE_FILAMENT_RESIDUE_CHANNELS_20260823.csv`.

No state was discarded by sampling: the 216 states are the full period.

### Lemma 3 — exact rolling transition and conserved coordinate

An adjacent center on shell `r+1` is either slot 1, with `t'=t`, or slot 3, with `t'=t+1`. The next center must itself be prime. Lemma 2 makes slot 1 eligible only when `epsilon=0`, and slot 3 eligible only when `epsilon=1`. Hence

`t'-t=epsilon=(r+sigma) mod 2`.

Since

`floor((r+1+sigma)/2)-floor((r+sigma)/2)=epsilon`,

the integer

`c=t-floor((r+sigma)/2)`

is conserved exactly, not merely modulo an integer.

The trajectory gap is symbolically

`Z_c(r+1)-Z_c(r)=3r+sigma+epsilon>0`.

Thus trajectory labels are distinct and strictly increasing.

### Lemma 4 — flowers are five-term trajectory windows

For `epsilon=0`, the five prime coordinates in packet order are slots `1,2,5,6` plus the center; after sorting by shell they are trajectory shells `r-2,r-1,r,r+1,r+2`. For `epsilon=1`, the prime slots are `2,3,4,5`, and the same five-shell statement holds.

Consequently two consecutive maximal flowers are the windows

`{Z(r-2),...,Z(r+2)}` and `{Z(r-1),...,Z(r+3)}`.

Their intersection has exactly four values. Conversely, any admissible run of `L+4` prime trajectory labels produces `L` consecutive maximal flowers. Therefore

`rolling filament of length L <=> admissible prime trajectory run of length L+4`.

### Global Obstruction or Counterexample

The local classification fixes `sigma=1`. Write

`Z_c(r)=B_r+c+floor((r+1)/2)+r`.

Modulo `5`, `Z_c(r)` has period `10` in `r`. The complete table is:

| `c mod 5` | `Z_c(0),...,Z_c(9) mod 5` | zero shells mod 10 |
|---:|---|---|
| 0 | `1 3 2 0 0 4 0 0 2 3` | `3,4,6,7` |
| 1 | `2 4 3 1 1 0 1 1 3 4` | `5` |
| 2 | `3 0 4 2 2 1 2 2 4 0` | `1,9` |
| 3 | `4 1 0 3 3 2 3 3 0 1` | `2,8` |
| 4 | `0 2 1 4 4 3 4 4 1 2` | `0` |

Every block of ten consecutive shells covers every residue modulo `10`, so it contains a trajectory label divisible by `5`. In an admissible maximal filament the lowest possible trajectory label is at least

`N(2,1,1)=7`.

Thus the divisible label is greater than `5` and composite. No ten-term prime run exists. Lemma 4 gives the global theorem

`L+4<=9`, hence `L<=5`.

The only nine-term zero-free channels modulo `5` are:

- `a=1 (mod 10)`, `c=4 (mod 5)`;
- `a=6 (mod 10)`, `c=1 (mod 5)`,

where `a` is the first trajectory shell in the nine-term window. Combining with `c=4 (mod 6)` yields exactly

- `(sigma,a mod 10,c mod 30)=(1,1,4)`;
- `(sigma,a mod 10,c mod 30)=(1,6,16)`.

Expanded modulo `30`, these are the six rows `a=1,11,21` with `c=4` and `a=6,16,26` with `c=16`. These are every surviving extremal residue/presentation channel; the CSV records their full mod-15 words and forced divisible predecessors/successors.

### Sharp witness

Take

`sigma=1`, `c=-2474=16 (mod 30)`, `a=10686=6 (mod 10)`.

The nine trajectory coordinates and labels are:

| shell | `t` | label |
|---:|---:|---:|
| 10686 | 2869 | 171283421 |
| 10687 | 2870 | 171315481 |
| 10688 | 2870 | 171347543 |
| 10689 | 2871 | 171379609 |
| 10690 | 2871 | 171411677 |
| 10691 | 2872 | 171443749 |
| 10692 | 2872 | 171475823 |
| 10693 | 2873 | 171507901 |
| 10694 | 2873 | 171539981 |

All nine are prime. The five flower centers are the middle coordinates, on shells `10688,...,10692`. Their complete packets are:

| center coordinate | ordered six neighbors | sorted five-prime packet |
|---|---|---|
| `(10688,2870,1)` | `171379608 171411677 171379609 171315481 171283421 171315480` | `171283421 171315481 171347543 171379609 171411677` |
| `(10689,2871,1)` | `171411677 171443749 171411678 171347544 171315481 171347543` | `171315481 171347543 171379609 171411677 171443749` |
| `(10690,2871,1)` | `171443748 171475823 171443749 171379609 171347543 171379608` | `171347543 171379609 171411677 171443749 171475823` |
| `(10691,2872,1)` | `171475823 171507901 171475824 171411678 171379609 171411677` | `171379609 171411677 171443749 171475823 171507901` |
| `(10692,2872,1)` | `171507900 171539981 171507901 171443749 171411677 171443748` | `171411677 171443749 171475823 171507901 171539981` |

Every consecutive pair has adjacent centers and set intersection exactly four. The preceding and following trajectory labels are

`171251365 = 5*34250273`,

`171572065 = 5*34314413`,

so this particular nine-prime run is maximal at both ends.

Each witness label was checked by deterministic 64-bit Miller–Rabin during search and, independently, by complete odd trial division through `floor(sqrt(n))`. The square-root limits range from `13087` to `13097`; the largest check tests 6548 odd divisors. Witness-certificate digest:

`sha256:cdd0e8b8ba4e72ac0cbb21920a0c5c7b012c5392f5d1bd09c22992e18e075c6f`.

### Small-prime and boundary exceptions

There are **no exceptions inside the packet's admissible domain**:

- `2` cannot occur as a relevant prime label;
- `3` cannot occur in an admissible maximal flower;
- the only interior occurrence of neighbor label `5` in the small-prime ablation is `(r,t,sigma)=(4,2,0)`, whose center is `21`, so it is not a flower;
- after the complete local classification, every actual maximal flower has `sigma=1` and all five prime labels are at least `7`.

Boundary coordinates are excluded exactly by `2<=t<=r-2`; no theorem is asserted outside that guard. As a negative control, removing the guard and scanning shells `4..300` finds boundary flowers `(4,0,1)` and `(5,1,1)`, the first containing label `5`. They are not exceptions to the theorem because neither center is admissible. The checker fails if they leak into the interior predicate.

### Final Classification

`SHARP_FINITE_BOUND_PROVED_AND_ATTAINED`

The hard target `NATIVE_PRIME_FILAMENT_SHARP_BOUND_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED` is met independently, with sharp bound `5`.

## 3. Reproducible Evidence

Run from the repository/lane root:

```powershell
python experiments\prime_native_filament_sharp_bound_independent_checker.py
```

Expected exit code: `0`.

Expected digest:

`a6be930a5920699f56a1b21d71cc3314d54732f5b31809236bedadc98ac80e9a`.

The checker exposes seed `0` and search start-shell range `2..20000`. It enumerates admissible extremal channels in ascending `(a,c)` order and finds the witness after `380482` candidates. The search establishes attainment only; it is not used for the global upper bound.

Exact finite-state and cross-check ranges:

- local proof table: all 216 states `(sigma,r mod 12,t mod 6)`;
- global obstruction table: all five `c mod 5` rows and all ten shell residues;
- extremal channels: all eligible `(a mod 30,c mod 30)` states;
- direct offset versus coordinate-delta implementation: every one of 37209 interior centers on shells `4..160`;
- direct flower predicate versus five-term trajectory implementation: the same range;
- boundary ablation: shells `4..300`;
- small-prime ablation: shells `4..30`, testing `2,3,5`;
- witness primality: complete odd trial division, separate from the search's Miller–Rabin path.

The exhaustive residue computations are complete periodic proofs. The larger coordinate ranges are implementation cross-checks, not substitutes for those proofs.

### Ablation Matrix

| Ablation | Result |
|---|---|
| all sector slots | all 216 local states checked; only physical `sigma=1` survives |
| both shell parities | both survive, with complementary prime slot words |
| cyclic sector renaming | exact equality under transported labels for shifts `0,1,2` |
| naive untransported `sigma` shift | rejected; each nonzero shift leaves zero primes in the witness window |
| orientation reversal | equivariant under `(r,t,sigma)->(r,r-t,2-sigma mod 3)` with slot permutation `1<->3`, `4<->6` |
| `2,3,5` | none occurs in an interior maximal flower |
| boundary guard | two out-of-domain flowers found by the bounded negative-control scan and correctly rejected |
| share four, nonadjacent centers | rejected by adjacency gate |
| adjacent centers, overlap three | rejected by overlap gate |
| neighbor slot 2 perturbed by `+1` | direct/coordinate implementations disagree, so control is detected |
| transition replaced by complementary step | conserved `c` changes, so control is detected |

The cyclic and reversal statements are presentation **equivariance**, not literal invariance of the fixed numerical allocation under changing `sigma` or `t` without transporting labels.

Evidence typing is separated in:

- proof evidence: this report and reducer;
- exhaustive finite-state evidence: CSV plus checker;
- witness evidence: checker witness certificate;
- comparison evidence: none, because source comparison was not opened.

## 4. Failed Attempts and Null Results

- Modulo `3` alone gives no global length bound: the surviving sector/channel avoids divisibility by `3` along the whole trajectory. It is a local classification tool, not the capacity obstruction.
- A direct census to shell `5000` found no witness. This was retained as a null search checkpoint and was not misreported as nonattainment. Extending the same deterministic search to shell `20000` found the certified witness at start shell `10686`.
- Treating sector cycling as literal numerical invariance fails. The correct statement transports the allocation and is equivariant.
- Boundary flowers exist if the packet's interior guard is removed, so silently extending the theorem to boundary cells is invalid.
- Finite trajectory searches were deliberately not used to prove `L<=5`; only the complete mod-5 cover closes the global obligation.

## 5. Conjectures and Open Problems

No conjecture is needed for the sharp finite bound. This task does not claim infinitely many length-five witnesses, historical novelty of the nine-prime tuple, or an intrinsic status for the presentation coordinate `c` outside the frozen carrier.

The natural distribution question—whether either extremal congruence family contains infinitely many nine-prime windows—is a classical prime-tuple question and remains out of scope.

## 6. Next Steps

The independent return is frozen. The responsible Driver may review repository closure and, only after preserving this freeze, compare against the withheld source. Any later source comparison must be typed as comparison evidence and cannot strengthen the independent classification retroactively.

No source reconciliation was performed by this researcher.
