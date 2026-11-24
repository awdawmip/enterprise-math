# R5 fifth noise chamber — exact two-error minimax, all 256 masks

**Frozen science pin:** `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
**Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Exact theorem

In the 101-budget, 256-mask frozen *derived scalar count observer*, an adaptive deterministic decoder can tolerate at most two **unmarked arbitrary corrupted readings**, with every intact reading obeying |y-N_h(k)|<=eta. For every real tau=2eta with

```
25845652773852463277015040000 <= tau
tau < 58182461585441404127941754880
```

the **exact minimum worst-case cumulative query budget is 2635**.

Together with the independently completed one-error proof in sibling directory `r5_fifth_chamber_f1_full_256_exact_20261117`, this establishes within the full fifth chamber:

```
C_0=735, C_1=1685, C_2=2635.
```

These three values equal `735+950*f` for `f=0,1,2`, with no claim yet for arbitrary f.

## Proof by exact endpoint minimax

Every exact count center is an integer. Increasing tau can only increase response compatibility, and this makes the minimum worst-case cost nondecreasing. For an arbitrary real tau<U, every admissible center-difference is <=U-1. Hence the exact full-population minimax at tau=U-1 is an upper bound for every tau in this chamber.

At the lower endpoint L, restrict the true state to the five masks (18,24,82,34,17). Exact finite minimax gives 2635, so it is a lower bound for all 256 masks and all tau>=L. At U-1, exact minimax over all 256 masks also gives 2635. Equality follows by monotonic sandwich.

## Certificate semantics

Let A_j be the bitset of hypotheses for which exactly j (0<=j<=2) readings are incompatible with their intact center interval. For an answer with center compatibility set S, define the next state by

```
A_0' = A_0 & S
A_1' = (A_1 & S) | (A_0 & ~S)
A_2' = (A_2 & S) | (A_1 & ~S)
```

with complements restricted to the current 256-bit universe. The final decision is unique when |A_0 union A_1 union A_2|<=1. The Bellman minimax recurrence ranges over the 101 permissible budgets and every maximal compatible response class. Equal-response-family queries are dominated by their cheapest budget; a query having a possible unchanged belief state cannot guarantee progress and is discarded. All other transitions decrease the bounded error-state potential; exact memoization exhausts the finite game.

Actual verifier evidence:
- Five-state lower endpoint L: **569** memoized Bellman states, 7 distinct query-answer families, value **2635**.
- Full 256-state high endpoint U-1: **408,149** memoized Bellman states, 12 distinct query-answer families, value **2635**.
- Source counts: all **25,856** entries at 101 budgets × 256 masks, frozen input SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.

Reproduce:
```
python VERIFY_R5_FIFTH_F2_ALL256.py EXACT_R5_ALL_101_BUDGETS.json
```

Expected output: `PASS_R5_FIFTH_CHAMBER_FULL256_F2_EXACT_2635`. The unchanged full count table is present in the prior R5 complete reproduction packages; its hash is mandatory. Python uses arbitrary-precision exact integers, no floating point or approximate search.

## Research continuation

Find the full 256-state f=3 exact value and either a uniform all-f policy with budget 735+950f or an exact counterexample. The f=2 equality is a finite theorem, not an infinite-f extrapolation. Original P000, source firewall and provenance remain intact. GitHub preservation of this material is independent from a canonical Task CLAIM, protected Activity checkpoint, Result or review.
