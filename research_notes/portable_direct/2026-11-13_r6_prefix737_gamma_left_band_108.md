# PREFIX-737-R6 — 108 newly excluded Gamma cells by exact left-band subdivision

Date: 2026-11-13 (Asia/Shanghai). Parent question: PREFIX-675, global maximum of the frozen 189-row BRC stopped-count **independent-Gamma auxiliary observer**. Scientific input stays pinned at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; current behavioral rules do not repin it. Researcher: `EM-DIRECT-9A5215`, Activity `RA-6123672379A281E0307FB9D7`.

## Exact continuous-cell theorem

Let `Y=max(T_p,T_z)` for the two independent unit-rate Gamma clocks under the pinned stopped-count distribution, `mu=E Y`, `M2=E Y^2`, `W=M2-mu^2`, and `V_q=q^2 W-q mu`. Set the witness `e=(0,73/500)`.

For **every real `q>=2`**, all `p,z` in any closed 384-grid cell with
`40<=i<58, 76<=j<79`, where the cell is
`[i/384,(i+1)/384] × [j/384,(j+1)/384]`, and all corresponding transposed cells,

```
V_q(e)-V_q(p,z) > 17 q² > 0 .
```

These 54 upper cells and their 54 distinct transposes contain no global maximizer of this auxiliary Gamma objective, at any real `q>=2`.

## Proof and exact lower-bound mechanism

The published PREFIX-731 frozen integer recurrence proves coordinatewise nondecreasing `mu` and `M2`. For any closed rectangle `R=[a,c]×[b,d]`, put
`L=mu(a,b)`, `U=M2(c,d)-L²`, `Delta=W(e)-U`.
For `t=1/q ∈ (0,1/2]`, the comparison divided by `q²` is bounded below by
`Delta-t(mu(e)-L)`; its affine minimum over `[0,1/2]` is
`G(R)=min(Delta, Delta-(mu(e)-L)/2)`.

Divide each of the 54 fine-grid cells into **four closed 768-grid subcells** and take the minimum of their four `G` values. Every exact rational minimum exceeds 17. The *smallest* integer floor of `10^6 G` is **17,346,039**, at `(i,j)=(40,76)`; hence the uniform strict inequality follows throughout all cells, including boundaries. Gamma-pair symmetry supplies the transposes. The JSON stores all 54 lower-bound floors, 18 per j-row; the Python file recomputes them exactly.

## Nonoverlap and certified union

For each of the 54 cells the original PREFIX-712 witness `e0=(0,3/20)` has the **old, unrefined 384-cell** envelope `G_old<=0`. As a containing 192-cell has an envelope no larger than its child, these cells are outside both PREFIX-712 coarse and adaptive accepted sets. Original frozen GitHub JSON files for PREFIX-713 coupled, PREFIX-713 multicompetitor, PREFIX-716 and PREFIX-718 were read, their source-defined coordinate sets reflected and intersected with the 108 cells; every intersection was empty. PREFIX-733-A/B, 735 and 736 index rectangles are geometrically disjoint. Thus 108 cells are newly certified relative to the PREFIX-736 author-union:

```
140484+108 = 140592 cells out of 384²=147456,
certified fraction 140592/147456 = 2929/3072 = 95.345052083333...%,
outside current certified union = 6864 cells.
```

This union arithmetic inherits the author-level, not independently admitted, historic exclusion certificates.

## Executed validation and exact limits

Local Python 3 integer/Fraction computation reconstructed all 189 survivor rows and all 9,529 nonzero count positions from the frozen width predicate. The center and witness moment numerators reproduced the four published PREFIX-731 SHA256 digests; 54/54 quartered intervals passed the exact rational strict bound, with the minimum floor above. A separate authorized GitHub read of four historic original JSON files confirmed zero additional coordinate overlap. Local output: `ALL_CHECKS_PASS PREFIX737-R6`. Local exact checker used an equivalent reconstructed kernel; **the composite publication script importing the actual checked-in PREFIX-731 module and the four historical JSON files has not been fully rerun end-to-end**. This is an author computation and proof, pending independent review. It does not alter the native X6/P000 three-dimensional slice ontology.

## Next precise question

Continue the left band to `j>=79` with bounded-memory, cache-clearing exact scans, targeting new complete cells and full-source composite regression; then tighten the remaining candidate region and locate actual Gamma maximizers. Keep independent shared-task CLAIM/Result/Review semantics separate.
