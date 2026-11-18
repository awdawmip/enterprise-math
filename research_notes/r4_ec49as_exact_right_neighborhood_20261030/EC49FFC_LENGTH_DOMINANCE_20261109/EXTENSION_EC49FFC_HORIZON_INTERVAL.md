# EC49FFC extension — exact reusable-horizon intervals for complete BRC keys

Date: 2026-11-09 (Asia/Shanghai). Scientific input remains frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Scope: original forward-count-admissible operation words in the six-axis signed-native, nine-state BRC model; horizons H2 through H9. This theorem concerns operation-count feasibility; individual terminal observation labels additionally require the frozen DFA test.

## Theorem C — contiguous horizons and constant native length

For a fixed integer full BRC key `K=(x,y,z)` with `z>=1`, the original operation-count constraints at an integer horizon `h` are

```
#a=z-1, #e=z, #c+#d=x+y-h-1,
#f=h+1-y-2z, #g=h+1-x.
```

There exists a nonnegative integer solution for all six operation counts **if and only if**

```
max(x-1, y+2*z-1) <= h <= x+y-1.
```

Intersect this interval with `{2,3,4,5,6,7,8,9}` for the finite research horizon range. The admissible horizons for each key therefore form a contiguous integer interval, possibly empty, and at all such horizons the signed native microstep length is the same:

```
L_native(K) = 2*(x+y+z-1).
```

**Proof.** All operation counts are nonnegative precisely when `z-1>=0`, `x+y-h-1>=0`, `h+1-y-2z>=0`, and `h+1-x>=0`. Rearranging yields the displayed interval. Conversely, given any integer `h` in that interval, choose `#c=x+y-h-1` and `#d=0`; then all the displayed counts are nonnegative integers and sum to `h`. Theorem A gives the claimed native microstep length, independent of the selected horizon and operation ordering. No statement is made that any particular DFA output label persists across the horizons. QED.

## Complete exact finite check

The standalone standard-library program `VERIFY_EC49FFC_INTERVAL.py` was executed. It independently enumerated all nonnegative-count parameterizations with H2–H9, reconstructed the interval for each full BRC key, checked exact set equality against the enumerated horizon/key pairs, and checked the native-length algebra for each pair.

| Metric | Exact result |
|---|---:|
| Count-admissible horizon/full-key pairs | 294 |
| Distinct full keys (allowing `y=0`) | 164 |
| Strictly positive `x,y,z>0` horizon/key pairs | 270 |
| Strictly positive full keys | 140 |
| All-key count of keys admitting exactly 1,2,3,4,5 horizons | 80,49,25,9,1 |
| Strict-positive-key corresponding histogram | 56,49,25,9,1 |

The **unique** full key attaining five horizons in this finite window is `(x,y,z)=(6,4,1)`, whose allowed horizons are H5–H9 and native path length is exactly 20 signed microsteps. The four count-admissible horizon/key pairs with no nonzero final observer label remain separately typed; this theorem only classifies the operation-count and native-length layer.

## Reuse and next research unit

This interval law permits an exact key-inventory cache indexed by full `(x,y,z)`, retaining horizon-specific DFA label sets and ordered signed-native prefixes as separate data. Theorem B has independently established a 94-edge lower bound for all path counts with the identified full-B/full-L support pattern, inherited from EC49FEO's fifteen 22-word templates. Next EC49FFD enumerates inclusion-minimal rank-nine terminal signature supports outside those dominated patterns and applies the frozen DFA and native-prefix oracle to the remaining five-key candidates. Author-side exact theorem; formal CLAIM and independent Driver admission remain pending.
