# R062 Stage 0 — Translated BRC Bridge Audit

Researcher-ID: `EM-R062-7C4A91`  
Status: `TRANSLATION_COVARIANCE_PASS`

## 1. Translation action

For a coordinate-vertex translation `R`, the frozen carrier implementation shifts every 3-scaled cell center by exactly `3R`.

For every typed path witness:

`tau_R : c(P,ij;x,y) -> c(P+R,ij;x,y)`.

Generator labels are unchanged. Hence every prefix trajectory is translated pointwise while its abstract word is unchanged.

## 2. Covariant bridge diagram

For each enrichment level `K in {Path,N,Boolean}`:

```text
K-BRC(P,ij)  -- tau_R -->  K-BRC(P+R,ij)
    |                         |
    | trace / terminal        | trace / terminal
    v                         v
T_{P;a,b}     -- tau_R -->  T_{P+R;a,b}
```

The checker verifies exact equality of relative prefix signatures across all seven starts and all trace cases with `a+b<=12` in all three sectors.

It separately audits five nontrivial translation vectors over the mandatory motif set `(1,1),(2,1),(3,2),(3,4),(4,3),(0,5),(5,0)`.

## 3. Preserved data

Translation preserves exactly:

- `Sigma_P^(ij)` start incidence, transported to `Sigma_{P+R}^(ij)`;
- concrete start vertex, by explicit translation rather than deletion;
- sector/component trace class `(ij;a,b)`;
- path witness count `binom(a+b,a)`;
- typed terminal endpoint;
- reverse-third same-endpoint/different-component distinction.

The bridge does not identify parallel translated lines. `P` remains part of `T_{P;a,b}^{(ij)}` and part of the typed path object.

## 4. Replay result

Main exhaustive bridge slice:

- translated starts: `7`;
- sectors: `3`;
- trace cases (`a+b<=12`): `1,911`;
- concrete paths: `172,011`;
- duplicate witnesses: `0`;
- translation mismatch: `0`;
- witness replay SHA256: `175c7f0efa6e62497dde5abbb65d354ddfc17a557f37640ee30260815cd68726`.

No floating-point comparison is used.
