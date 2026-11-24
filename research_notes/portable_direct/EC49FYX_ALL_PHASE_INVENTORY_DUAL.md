# EC49FYX addendum — all-phase exact asymptotic physical inventory law

Frozen auxiliary Boolean observer BRC16943 as in the companion packed multicover transport note at 3a42e1a171d3db7c557d136d4256747ef0724aff. Additional source actually reread: 10f0597c6c988fc0adcfbc8fda748367587745bb:research_notes/portable_direct/EC49FYU_UNIQUE_DEFICIENT_PREFIX.md. Use FYW's stable c_h=ceil((15h+6)/11) for h>=2 and FYU's exhausted-prefix uniqueness. No native physical interpretation or independent review claimed.

## New global lower bound

For every h>=2, the minimum physical column count M_h attaining m+c_h obeys

M_h >= 28h - 19c_h + 10.

In particular for all h>=4, combine with the companion packing upper bound:

ceil((23h-194)/11) <= M_h <= floor((23h+7)/11).

Thus lim_{h->infinity} M_h/h=23/11 over ALL positive integer h, not merely the phase h=4 mod 11. The lower bound is weaker than FYV on its exact phase; retain the sharper phase-specific result 23a+8<=M_(4+11a)<=23a+9 for a>=1.

## Proof

Assume a correct tree of depth <=m+c_h. Follow zeros to depth d=c_h+h-1, stopping earlier if all supports have >=h forced distinct hole columns. Such a prefix exists: while some support has b(U)<h, its minimal-hole state and a state with an extra hole are distinct compatible targets, so the path cannot end. Each next probe adds at most one forced hole for a given U; in particular if the next probe makes all supports saturated, some support is exactly at h, so that zero branch is still feasible. At depth d if no earlier saturation, FYU gives b(U)>=h-1 for all, with at most one b(U)=h-1. At earlier saturation all b(U)>=h. This handles the phases where the zero path need not exist all the way to d.

Let S_j denote the set of distinct queried rows on physical column j, and N the number of nonempty masks. Then N<=m and L=sum_j |S_j|<=d, even if the tree repeated a query. Define nonnegative support weights

(86,4), (101,8), (123,1), (281,2), (346,1), (394,9), (412,1), (460,1), (602,5), (673,9), (788,6).

They sum to 47, maximum 9. For EVERY nonempty ten-row mask S, the following exact integer inequality holds:

sum_{U:S intersects U} w_U <= 1 + 19 |S|.

Summing over physical columns, the left side is precisely sum_U w_U b(U), with each support hit counted only once per column, not once per row. By the prefix lemma it is >=47h-9. Hence 47h-9 <=N+19L<=m+19d. Rearrange to m>=28h-19c_h+10. Since 11c_h<=15h+16, this implies 11m>=23h-194. For the upper bound use h=4+11a+r, 0<=r<=10 and the companion B_r=(0,1,4,6,8,10,11,14,16,17,20), which yields 11(9+23a+B_r)-23h in (7,-5,5,4,3,2,-10,0,-1,-13,-3). Thus m=floor((23h+7)/11) always suffices. Squeeze proves the global slope.

The certificate was found using a numerical LP on all nonempty column masks, but the theorem uses only the following exact integer verification, not the floating optimization result. It represents a coupled physical-column/query-count certificate: the earlier row-cover dual alone cannot control packed inventory.

## Executed reproduction

```python
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
w={86:4,101:8,123:1,281:2,346:1,394:9,412:1,460:1,602:5,673:9,788:6}
assert set(w)<=set(F) and sum(w.values())==47 and max(w.values())==9
slack=[1-(sum(v for u,v in w.items() if s&u)-19*s.bit_count()) for s in range(1,1024)]
assert min(slack)==0
print('1023 exact masks; min slack',min(slack),'tight masks',[s for s in range(1,1024) if slack[s-1]==0])
B=[0,1,4,6,8,10,11,14,16,17,20]
print([11*(9+b)-23*(4+r) for r,b in enumerate(B)])
```

Output:
```
1023 exact masks; min slack 0 tight masks [1, 2, 3, 4, 8, 16, 64, 128, 144, 192, 256, 512]
[7, -5, 5, 4, 3, 2, -10, 0, -1, -13, -3]
```

Note on companion theorem: its precise positive-branch bound is max(6,L-k+5,c+L-k); the simplified c+L-k bound requires c>=6 or L-k>=1 when c>=5. All applications in this batch use c=6. No effect on the packed construction or its conclusions.

Status AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED. Next: sharpen bounded onset offsets, especially the one-column gap in phase 5; inspect the extra cross-boundary (0,1) merge with label-preserving adaptive continuation.
