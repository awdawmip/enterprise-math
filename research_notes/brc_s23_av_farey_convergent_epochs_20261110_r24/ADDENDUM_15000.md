# R24 addendum — exact extension to n=15000

Date: 2026-11-10, frozen science `enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Observer and strict theta enclosure are *exactly* as in PROOF.md, with 128 fixed historical cuts. This addendum continues the latest R24 evidence from n=7621.

## New certified finite theorem

For all integer n from **7622 through 15000**, the risk R(128,n-128) has the initial value

`R(128,7621)=−43477+165817 θ`

and its consecutive exact increments are exactly:

| Newly added cut counts n | Count | Increment ΔR |
|---|---:|---|
| 7622–7687 | 66 | 3257θ−854 |
| 7688–7723 | 36 | 0 |
| 7724–7784 | 61 | 3257θ−854 |
| 7785–10877 | **3093** | 0 |
| 10878–10944 | 67 | 3257θ−854 |
| 10945–10980 | 36 | 0 |
| 10981–11041 | 61 | 3257θ−854 |
| 11042–14134 | **3093** | 0 |
| 14135–14201 | 67 | 2895−11041θ |
| 14202–14237 | 36 | 0 |
| 14238–14298 | 61 | 2895−11041θ |
| 14299–15000 | 702 | 0 (verified prefix; next break unresolved) |

At exact endpoints,

`R(128,14134)=−261247+996352θ` and
`R(128,14298)=R(128,15000)=109313−416896θ.`

Thus we now have **three successive 3093-step zero-risk plateaux** at n=4528..7620, 7785..10877 and 11042..14134, with certified intermediate growth blocks. The third growth-size error `2895−11041θ>0` is the error of the next continued-fraction convergent `2895/11041`, extending the prior series of errors `333−1270θ` and `3257θ−854`. This evidence motivates an exact symbolic jump generator.

## Proof and executed verification

The same exact maximal-gap split lemma in PROOF.md governs each insertion. `VERIFY_R24_EXTENSION.py` imports the published R24 proof checker and increases its certified cut bound to 15000. It checks each insertion's floor and circular order, both endpoint rational gap signs, maximality against **all** same historical arc subgaps, and consecutive risk coefficients against the 12-row table above. Exact endpoint comparisons establish each order and maximum decision on the **whole open rational interval** stated in PROOF.md. Independently, a fresh full-sorted-partition calculation is performed at 25 selected endpoints and interior points.

Executed values: 14,872 insertion updates from n=129..15000; 29,744 strict gap-sign tests and 1,018,754 maximum comparisons; 25 full partition reconstructions; `PASS_R24_EXACT_EXTENSION_THROUGH_15000`. The r24 base verifier checked 131 separate partitions through n7621. The extension is a new bounded finite certificate, not an asymptotic algorithm improvement. Mathematical independent review and native shared Task CLAIM are not claimed.

## Next

Extend the plateau n>=14299 to its exact next breakpoint using a symbolic continued-fraction denominator jump, retaining the source labels, maximal-gap multiplicities and future split destinations. Compare predicted blocks against another exact bounded verification; account for preprocessing and integer bit cost before algorithmic speed claims.
