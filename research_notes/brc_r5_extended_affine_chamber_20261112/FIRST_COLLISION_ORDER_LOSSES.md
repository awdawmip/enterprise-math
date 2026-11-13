# R5 — first signed phase collision: exact labeled schedule-loss redistribution

Date: 2026-11-12 (Asia/Shanghai). Researcher-side exact rational finite computation, continuing [R5 extended affine-chamber theorem](RESEARCH.md), with identical frozen X, 15 labeled atoms, H, observer and scientific pins. The first positive and negative phase coincidences occur at `eta=x/12443` and `eta=-x/12397`, respectively, for `x=155682221/25142124560000000`.

## Exact result

At either event, the moving `q=15` threshold `(x-23 eta)/15` crosses the old fixed threshold `36x/n`, with `n=541` on the positive side and `n=539` on the negative side. These are the **first** crossings as `|eta|` increases from zero, so the two thresholds are consecutive phases.

Below/at/above refer to absolute perturbation magnitude, not the signed numerical order of eta. All figures count distinct legal permutations of the **same 15 labeled atoms** that are lost upon crossing a threshold in epsilon. They are integers, not asymptotic estimates.

| sign of eta | side of first crossing in |eta| | fixed phase drop | moving q=15 phase drop | combined drop |
|---|---|---:|---:|---:|
| + | `0<eta/x<1/12443` | 959,619,024 | 379,780,599,984 | 380,740,219,008 |
| + | `eta/x=1/12443` | one simultaneous event | 380,740,219,008 | 380,740,219,008 |
| + | `1/12443<eta/x<1/9959` | 648,765,504 | 380,091,453,504 | 380,740,219,008 |
| − | `0<-eta/x<1/12397` | 915,295,200 | 379,627,579,392 | 380,542,874,592 |
| − | `-eta/x=1/12397` | one simultaneous event | 380,542,874,592 | 380,542,874,592 |
| − | `1/12397<-eta/x<1/9913` | 915,295,200 | 379,627,579,392 | 380,542,874,592 |

At an exact collision the combined loss is listed in the moving-event column for convenience; it is a **single** event rather than two independent drops.

**New numerical observation:** crossing the *positive* collision transfers exactly `310,853,520` labeled schedules of loss from the fixed event to the moving event, while the *negative* collision produces **zero** redistribution. The total two-event drop remains constant separately for each sign. This is a direction-sensitive, fully scoped fact about the frozen hidden-fiber perturbation, not a general conservation law about arbitrary atom systems.

## Exact proof certificate and uniformity

For each nonempty subset `S`, compute its sign-specific first-zero affine minimum `tau_S(eta)=a_S+b_S eta` from the 28 exact transport coordinates. The preceding theorem proves these active minima remain fixed on the relevant perturbation ranges and that there is exactly one moving/fixed collision before the next listed phase. Thus the total order of subset-activation thresholds is constant in each of the four open parameter intervals.

For rational `eta` and `epsilon`, let
```
W(empty)=1;
W(S)=0 if tau_S(eta)<epsilon;
W(S)=sum_(a in S) W(S without a) otherwise.
```
Then `W(all 15 labels)` counts exactly the legal complete permutations, since each legal permutation is partitioned by its last label. For a phase value `theta`, take the exact rational midpoints before and after `theta` among the adjacent phase values; subtract the corresponding counts. This computes the precise loss caused by the phase without any floating point and without materializing `15!` orders.

The attached checker evaluates `eta/x=+1/13000` (before), `+1/12443` (at), `+1/12000` (after), and `-1/13000,-1/12397,-1/12000` for the negative event. It uses every 15-bit subset and complete 28-coordinate first-zero feasibility; the results are the exact integers in the table. Because the active affine minima and phase ordering remain unchanged in the specified open intervals, one exact representative per interval proves those same counts throughout each interval.

## Reproduction and evidence

- `VERIFY_FIRST_COLLISION_ORDERS.py.gz.b64`: Python standard-library exact checker; decode with `base64 -d VERIFY_FIRST_COLLISION_ORDERS.py.gz.b64 | gzip -d > VERIFY_FIRST_COLLISION_ORDERS.py`, and run from the stacked PR branch with `python VERIFY_FIRST_COLLISION_ORDERS.py`. It imports the unchanged original R5 parent `VERIFY_R5_SHARP_RAY.py`.
- Decoded SHA-256: `0c655fdfb9431e31b58ad6f3c7f9bea2bda1d96f949ac4434557fed417a09d96`.
- `EXACT_FIRST_COLLISION_OUTPUT.txt`: saved actual successful local execution with the same checker and `--local-fixture` (independently transcribed original rational X and atom coefficients); clean remote-byte execution of the ordinary import path remains a reproduction step.

## Next

Classify the other interior collisions `+1/9959,+1/6233,+1/4991,+1/4163,+1/3335,+1/3128` and `-1/9913,-1/6187` for direction-sensitive loss transfers, then analyze the triple simultaneous collision at the positive affine-minimizer boundary `+1/2507`.
