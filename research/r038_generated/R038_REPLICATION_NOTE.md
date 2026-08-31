# R038 Independent Local Replication Note

Researcher-ID: `EM-R038-6A7D21`

## Scope

This is a narrow R038-side replication, not a substitute for full R037.

The HCP graph was rebuilt from the ideal ABAB nearest-neighbor rule without calling R033 executable code:

- six in-layer triangular neighbors;
- from even layer, three offsets `(0,0),(-1,0),(0,-1)` to each adjacent odd layer;
- from odd layer, inverse offsets `(0,0),(1,0),(0,1)`;
- physical Gram matrix `[[1,1/2,0],[1/2,1,0],[0,0,2/3]]`.

## Result

Independent BFS shell sizes begin:

`r=1..7: 12, 44, 96, 170, 264, 380, 516`.

They agree exactly with R033 frozen formulas:

- even `r`: `(21r^2+4)/2`;
- odd `r`: `(21r^2+3)/2`.

Independent ball sizes agree with:

- even `r`: `(14r^3+21r^2+14r+4)/4`;
- odd `r`: `(14r^3+21r^2+14r+3)/4`.

The common exposed-edge law was also re-enumerated at small radii:

`E_out(r)=12(3r^2+3r+1)` for both FCC and HCP.

A previously seen non-source summary with a linear `3r` HCP shell remainder is therefore rejected. It is not the R033 frozen result.

## Additional exact moment reconstruction

Using the physical HCP Gram matrix, the direct BFS sum
`M2(r)=sum_{x in B_r}|x|^2`
matches the closed period-2 formula recorded in `R038_READOUT_ATLAS.json` through radius 18.

The closed formula can be derived from exact layer sums. For even vertical layer `k`, with `m=r-|k|/2`:

- point count: `3m(m+1)+1`;
- basal quadratic sum: `m(m+1)(5m^2+5m+2)/4`.

For odd `k`, with `m=r-(|k|+1)/2`:

- point count: `3(m+1)^2`;
- basal quadratic sum: `(m+1)^2(5m^2+10m+4)/4`.

Add `(2/3)k^2` times the layer count and sum over `-r<=k<=r`.

Classification: `EXACT_DERIVATION_PLUS_FINITE_MACHINE_REPLICATION`.
