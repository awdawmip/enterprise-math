# R260A — first prime-square obstruction to the R258 one-mask quotient

Date: 2026-11-18. Author-computed exact counterexample; **NOT_REVIEWED**. Scientific input remains frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Statement

Fix the R258 seven-source positive rational **auxiliary scalar** model, `s=866/2197`, `J=3327364117`, `T=3975468120`, `K=36933000`. Let `q_(m,k)=JT^k h_(m,k)/K`, with its original mask label m. R260 proved that modulo 13 all 63 labelled sequences are constant scalar multiples of mask 9, for every k>=3. This one-mask constant-linear reconstruction **cannot be lifted to modulo 13^2=169** (and no different single mask can replace it modulo 169).

The first two event residues, from exact R259 characteristic recurrence and integer bases, are:

| mask | q_(m,3) mod169 | q_(m,4) mod169 |
|---|---:|---:|
| 9 | 96 | 139 |
| 10 | 18 | 113 |

Their two-by-two determinant is

`96*113 - 139*18 = 8346 ≡ 65 = 5*13 (mod 169)`,

hence nonzero modulo 169. If both mask-9 and mask-10 sequences could be reconstructed from any **one** labelled mask b by fixed scalars a,c in Z/169Z at every time, this determinant would be identically zero (two scalar multiples of the same vector). Contradiction. Thus at least two separate labelled channels are necessary for full constant-linear reconstruction modulo 169, while exactly one suffices modulo 13.

For a direct witness against lifting the chosen mask-9 quotient, `96^{-1}≡125 (mod169)` gives the unique coefficient matching mask 10 at k=3, namely `18*125≡53`. But at k=4, `53*139≡100≠113`; the residual is `13 mod169` and vanishes after reduction modulo 13.

## Evidence and scope

The companion script imports R260's exact integer/rational reconstruction and verifies the four displayed residues, determinant, inverse, and non-lifting coefficient with integer modular arithmetic. These are exact calculations at fixed s, not a floating experiment. The result demonstrates a **typed higher-precision residual**: a mod-13 observer quotient cannot be promoted to mod-169 simply by keeping its old one-mask basis. It does not establish the minimum number of generators over Z/169Z, future all-zero events modulo 169, or any native signed BRC transfer.

Next: compute a provably minimal generating set for the full 63-channel sequence module over Z/13^2 Z using Smith invariants or a direct module certificate; identify which extra labels recover the first p-adic residual layer.
