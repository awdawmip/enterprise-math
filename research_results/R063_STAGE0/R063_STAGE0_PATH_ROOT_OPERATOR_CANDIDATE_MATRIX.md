# R063 Stage 0 — Path-root operator candidate matrix

Task: `RS-R063-STAGE0-PATH-VALUED-SQUARE-ROOT-2500-DISCOVERY`  
Researcher: `EM-R063S0-E7DD7A`

| Candidate | Construction | N=2500 complete? | Extras? | Classification |
|---|---|---:|---:|---|
| C0 | ordinary scalar `N -> sqrt(N)` | No | No | Retains only scalar radius/norm magnitude; loses component, trace, provenance, path multiplicity. |
| C1 | brute `a^2+b^2=N` inverse fiber | Yes by definition | No | Verification oracle only; set-valued restatement, not accepted as discovery. |
| C2 | `N(beta)=r`, then `alpha=beta^2` | false | 0 | Exact norm-preserving lift but incomplete here; missing branches are preserved below. |
| C3 | factor `r`, enumerate divisor-scaled canonical Euclid/Gaussian channels `r=k(m^2+n^2)`, then `k(m+nJ)^2` | true | 0 | Complete for square native norms by the scaled primitive Pythagorean theorem; regression passes through `r<=512`. |
| C4 | direct Gaussian prime allocation for norm `N=r^2` | true | 0 | Complete constructive factorization route; same canonical root fiber as C3, with Gaussian exponent-allocation provenance. |

## Classified C2 negative result

N=2500 C2 missing branches (derived only after discovery freeze by the verifier): `[[30, 40], [40, 30]]`.  
N=2500 C2 extras: `[]`.

Across the non-customized square regression the first C2 failure is at `r=3`. This C2 failure is a **classified candidate limitation**, not a checker error.

## Inverse fiber versus discovery

`INVERSE_NORM_FIBER` names a set by the target equation. `SCALAR_ROOT_FACTORIZATION_GENERATOR` constructs the members from integer/Gaussian factorization and exact exponent or Euclid-channel choices. C3/C4 are therefore constructive discovery operators; C1 is only the post-freeze completeness oracle.
