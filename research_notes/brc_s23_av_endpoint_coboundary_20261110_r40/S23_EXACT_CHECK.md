# R40/S23 exact owner saturation at a trillion-step source horizon

At frozen S23/AV theta, with rational enclosure
`262204504569236716045286/10^24 < θ < 262204504569236716045287/10^24`,
historical cut count `m=128`, source upper endpoint `J=10^12+128`, source window length `N=10^9`, R40 endpoint-coboundary selector yields **all 128 exact historical last-source labels** and matches R39's independent Euclidean Floor Sum selector 128/128.

The last-surviving-source ages `J-t_k` are exactly the following set, with no repeated ages:

`{1,2,...,106} ∪ {143,144,...,164}`.

There are exactly 36 omitted ages, `107..142`. Hence the most recent 164 source indices cover all 128 historical owner arcs, whereas the most recent 163 cover exactly 127. This is a **specific exact saturated-window observation** for the frozen S23 rotation at this J, not a statement that all horizons have the same missing-age positions.

The exact last-source index vector (owner order follows phase-sorted historical cuts) has SHA-256
`5b97af4166df200fa720773b542d2e3c84164a89d567c60fc5543ed4d1f71ae7`,
serialized as `json.dumps([last[k] for k in range(128)],separators=(',',':'))`.
The attached `VERIFY_R40_S23.py` regenerates this vector and exact cross-check from the co-located `VERIFY_R40.py` source. Observed result:

```
S23 exact J 1000000000128 N 1000000000 owners 128 max_age 164
age intervals [1,106] and [143,164]; missing [107,142]
distinct thresholds 139 certified scalar floor endpoints 35816 independent Euclidean sums 7920
last-source-owner-vector SHA256 5b97af4166df200fa720773b542d2e3c84164a89d567c60fc5543ed4d1f71ae7
PASS_R40_FROZEN_S23_TRILLION_LAST_SOURCE_128_128
```

These source labels are preserved individually in the exact computation. The test does not substitute for the separate 298-affine-risk-run re-integration planned in R41; it establishes the related last-source selection primitive at the specified large J and N.
