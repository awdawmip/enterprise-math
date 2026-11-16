# R5 — Complete seven-declaration lift of a negative-residual FULL_HIST corner

Scientific pins and model are as stated in this directory's `RESEARCH.md` (frozen GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`). This extends `REVERSE_CORNER_RECTANGLE.md` from a two-dimensional tail-only declaration family to **every real seven-dimensional declaration vector**.

## Theorem (constructive all-real pointwise inclusion)

Let the FULL_HIST source flow be
`x=(g,a,b,u,v,w,z)=(1,1,1,0,9/40,0,0)`, with historical residual `R=-9/10` and two stopping times `T_P=T_Q=129/40`. For every `d in [0,1]^7`, there exists a **single** legal seedless LR flow `y` and legal `d' in [0,1]^7` such that

`W(x,d)=(e_P,e_Q,T_P,T_Q)=W(y,d')`.

The same seedless flow works for the entire declaration cube:

`y=(1,19/20,19/20,0,11/40,0,11/130)`.

Direct use of the frozen rational affine mass formulas yields
`M(x)=(67/720,27/80,0,5/36,0,27/80,67/720)`, and
`M(y)=(121/1200,513/1600,1/40,257/2400,1/40,513/1600,121/1200)`.
Both masses are Q-normalized and have likelihood-ratio first moment one; `R(y)=0`, and both times are `129/40`.

## Exact seven-by-seven stochastic Blackwell kernel

Index the LR keys `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)` from 0 through 6. Define a row-stochastic kernel K from the seedless y stopping key i to the FULL x stopping key j. Unlisted entries are zero:

- row 0: `K[0,0]=335/363`, `K[0,1]=405/6292`, `K[0,3]=241/18876`;
- row 1: `K[1,1]=1`;
- row 2: `K[2,1]=27/65`, `K[2,3]=38/65`;
- row 3: `K[3,3]=1`;
- row 4: `K[4,3]=38/65`, `K[4,5]=27/65`;
- row 5: `K[5,5]=1`;
- row 6: `K[6,3]=241/18876`, `K[6,5]=405/6292`, `K[6,6]=335/363`.

All entries are nonnegative, and every row sums exactly to one. The **stronger** column identities, all exactly rational, are

`sum_i M_i(y)*K[i,j]=M_j(x)` and
`sum_i r_i*M_i(y)*K[i,j]=r_j*M_j(x)` for every `j=0..6`.

Consequently choose `d'_i=sum_j K[i,j]*d_j`. Row stochasticity makes every d'_i a legal declaration for *every real* d. The column Q identities give `e_Q(y,d')=e_Q(x,d)`; the column P identities give `1-e_P(y,d')=1-e_P(x,d)`. Two times already agree, proving the full four-observer equality. This is **not** a convex combination of multiple seedless flows; a single fixed seedless flow y dominates the complete experiment x under a Q/P-calibrated stochastic garbling.

## Derivation of the rational kernel

Keep the original tail Q mass `67/720` at each extreme source y key 0 and 6; keep the direct middle-pair masses `513/1600` at y keys 1 and 5. Each x key 1 and 5 still needs `D=27/1600` additional Q mass. Fill the x key 1 from y key 0 with `5D/13` and y key 2 with `8D/13`: their source likelihood ratios `1/10` and `3/4` average exactly to target `1/2`. Reflect the construction at key 5 using y keys 6 and 4. Transfer all remaining symmetric tails and near-middle mass to x key 3 (LR=1), together with y's own center. The leftover low/high masses occur in mirror pairs and thus give conditional mean likelihood ratio one. Dividing these exact nonnegative Q transfers by source masses M_i(y) gives the K rows above.

## Evidence and scope

`VERIFY_REVERSE_ALL.py` is a standalone Python-standard-library `Fraction` checker. It checks both flows, both times, residuals, all seven exact Q column sums, all seven exact P moment columns, nonnegativity, seven stochastic rows, plus 128 deterministic declaration vectors. `OUTPUT_REVERSE_ALL.txt` captures its actual stdout. Exact equalities of the rational kernel prove the result for the **entire real cube**, not only these 128 diagnostics.

This solves a full extreme-history negative-R corner, in addition to the earlier all-real R>=0 halfspace; it does **not** settle the remaining R<0 continuum or full pointwise image equality. It does not establish native X6 physical dynamics. Author-side theorem and code are executed and reproducible but await independent review and original Source research authority. The service's backend identity/version mismatch prevents confirming native R5 owner/CLAIM.

## Next exact unit

Target negative-residual FULL_HIST flows with `u,w` at other extreme values (e.g. `g=a=b=1` and `u,w in {0,27/80}` with `v=9/40,z=0`), then the interior R<0 domain. Search for one *single* time-matched seedless flow whose Q/P experiment Blackwell-dominates each target, represented by a finite rational nonnegative kernel. If such a flow exists, it immediately lifts all its declaration vectors. If it fails, find an actual global nonconvex four-observer witness, not merely a failed kernel for one candidate y.