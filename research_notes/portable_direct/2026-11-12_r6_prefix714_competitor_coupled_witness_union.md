# PREFIX-714-R6 — Nonoverlapping exact Gamma-clock exclusion certificates

Date: 2026-11-12 (Asia/Shanghai).  
Scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d` (frozen).  
Parent: PREFIX-675, complete auxiliary BRC observer variance maximization.  
Dependencies: PREFIX-710 (correct Gamma completion-time kernel), PREFIX-712 (exact sparse 384² grid), PREFIX-713 (coupled-moment envelope and its 90 cells).  
Evidence: AUTHOR_DERIVED / EXACT_INTEGER_GAMMA_KERNEL / UNREVIEWED / NOT_ADMITTED.

## Main theorem: two independently certified witness sets combine

Let `N_p` be the frozen 189-row stopping count and, conditionally on `N_p=k`, `T_p ~ Gamma(k,1)`. Complete the two independent clocks, then define `Y(p,z)=max(T_p,T_z)`,
`mu=E[Y]`, `M2=E[Y²]`, `W=M2-mu²` and
`V_q=q² W-q mu` on `D=[0,1/2]²`. The two coordinates are an **external auxiliary statistical observer**, not an Enterprise-native X6 three-dimensional slice.

For all real `q>=2`, there exists an explicitly specified union of closed rational cells, with disjoint interiors, on which the strict inequality `V_q(e)>V_q(p,z)` holds for at least

```text
137278 / 147456 = 68639 / 73728 = 93.0976019965...%
```

of the full area of `D`; `e` is chosen independently for each certified cell from a finite witness family, rather than required to be the same for every cell.

For the entire real parameter interval `12<=q<=24`, at least

```text
137494 / 147456 = 68747 / 73728 = 93.2440863715...%
```

of `D` is certified to be strictly dominated. The respective remaining **uncertified** area fractions are at most `5089/73728` and `4981/73728`. These are exact area bounds for the explicitly certified finite unions, not estimates from sampled optimization points.

## A second kind of certificate: cell-dependent competitor

PREFIX-712 fixed `e0=(0,3/20)` and, on each fine rectangle `R=[a,h]`, used the monotone-moment upper bound

```text
U(R) = M2(h) - mu(a)^2.
```

Because `mu(x)>=mu(a)` and `M2(x)<=M2(h)` for `x in R`, for every rational competitor `e` and `t=1/q>=0`,

```text
F_t(e)-F_t(x) >= G(e,R,t)
G(e,R,t) = W(e)-U(R)-t*(mu(e)-mu(a)),
F_t = W-t*mu.
```

For each fixed cell and competitor, `G` is affine in `t`. Consequently:
- strict `G(e,R,0)>0` and `G(e,R,1/2)>0` imply strict dominance throughout all real `q>=2`;
- strict `G(e,R,1/24)>0` and `G(e,R,1/12)>0` imply strict dominance throughout all real `12<=q<=24`.

The competitor can vary between **cells**, since each conclusion compares that cell with a valid point of `D`. The exact finite candidate family used here is

```text
e0=(0,3/20)       [the inherited old comparator]
e1=(0,147/1000)
e2=(0,59/400)
e3=(0,297/2000).
```

No optimization or floating-point assertion about the family is needed for this theorem. The new exact checker reconstructs all 189 survivor-count rows and 9,529 nonzero count units, uses the correct independent Gamma maximum moment kernel from PREFIX-710, and evaluates the endpoint inequalities in `fractions.Fraction` arithmetic.

**20 new cells** pass both all-`q` endpoints with one of `e1,e2,e3`, whereas all 20 fail at least one old fixed-`e0` endpoint. Among the 40 strict inequalities, the minimum is **greater than `0.016584`**. The 20 cells are the exact indexed set `extra_all` in the accompanying checker and `PREFIX713_R6_MULTICOMPETITOR_RESULTS.json`.

A further **six new cells** pass both `q=12,24` endpoints using `e3`, whereas each fails the old fixed-`e0` range certificate. Their 12 strict inequalities have minimum **greater than `0.006139`**. They are the exact indexed set `extra_range`. Every fine cell indexed `(i,j)` represents the closed rectangle
`[i/768,(i+1)/768] x [j/768,(j+1)/768]`.

## Independent coexistence with the coupled-moment certificate

PREFIX-713 separately proved that its improved **coupled first/second moment envelope** certifies 90 additional cells for all real `q>=2`. It enumerated 45 off-diagonal representatives (all four children of 11 listed coarse parents, plus one specified child), then reflected them across `p=z`. Its proof controls the correlated increments of `mu` and `M2`, whereas the new method above changes the witness comparison point; the mechanisms are different.

The exact union checker performs these additional tests:

1. Expand the 45 published PREFIX-713 representative indices to the 90 fully ordered fine-grid cells. Check that all 90 have disjoint interiors from the 20 multi-competitor all-`q` cells, and separately from the six extra `q12..24` cells.
2. Recalculate `G(e0,R,t)` exactly on those 90 coupled-certificate cells at `t=1/24` and `t=1/12`. All 90 fail at least one of these old range endpoints. Therefore the 90 are **also new relative to PREFIX-712's range certificate**, not merely relative to its all-`q` certificate.
3. Recalculate the same two old range endpoints on the 20 all-`q` multi-competitor cells. All 20 already belong to PREFIX-712's old `12<=q<=24` certified union. Therefore adding them to the range count would double-count; they are used only for the all-`q` improvement.
4. The six extra range cells are distinct from the coupled set and each fails the old range certificate; their exact two-endpoint inequalities have already been rechecked with `e3`.

The resulting **finite disjoint union counts** are

```text
all real q>=2:
    137168 [PREFIX-712] + 90 [PREFIX-713 coupled]
       + 20 [new cell-dependent competitors] = 137278

real 12<=q<=24:
    137398 [PREFIX-712] + 90 [PREFIX-713 coupled, newly checked against old range]
       + 6 [new cell-dependent competitors] = 137494
```

The proof of the coupled envelope and of its 90 exact witnesses is inherited from the immutable PREFIX-713 source. The new checker re-executes the frozen Gamma kernel, all 26 new competitor-cell inequalities, disjointness, the cross-regime membership tests for 90+20 cells, and the exact final fractions. It performs a **targeted extension**, rather than re-running the complete PREFIX-712 grid search. All accepted inequalities are strict on the corresponding closed cells; shared cell boundaries have zero area.

## Exact computation and validation

Local Python standard-library `Fraction` execution returned

```text
Exact frozen rows: 189; nonzero cells: 9529
all_q_ge_2 new cells 20 minimum gap > 0.016584
q_12_to_24 new cells 6 minimum gap > 0.006139
ALL_CHECKS_PASS PREFIX713-R6
ALL_CHECKS_PASS PREFIX714-R6
  all_q_ge_2 = 68639/73728
  q12_to_24 = 68747/73728
```

Files:
- `PREFIX713_R6_MULTICOMPETITOR_CERTIFICATE.py` — direct exact new-cell verification, indexed lists, and old certificate rejection checks.
- `PREFIX713_R6_MULTICOMPETITOR_RESULTS.json` — all 26 new witness indices, selected comparators, and integer lower margins.
- `PREFIX714_R6_CERTIFICATE_UNION_CHECK.py` — full exact disjoint-union and range-membership checker, reusing the preceding file.
- `PREFIX714_R6_RESULTS.json` — exact union counts and remaining-area fractions.

The work remains author-verified, without independent mathematical review or remote CI execution. No native CLAIM/Result/Review is inferred from storage.

## Next discriminating unit

Evaluate the coupled-moment envelope on the **remaining uncertified** fine-grid cells of PREFIX-714, then apply per-cell adaptive rational competitors to the survivors. A full exact exhaustive scan, rather than the targeted 90+26 certificates, would quantify the additional area enabled by these two independent improvements. Next, certify stationary points or boundary/global inequalities on the remaining compact regions to advance PREFIX-675's actual optimizer localization. Preserve the frozen science pin; keep the auxiliary observer model distinct from native X6 geometry.
