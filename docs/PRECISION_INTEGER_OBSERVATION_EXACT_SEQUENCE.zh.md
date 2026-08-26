# 整数观测正合序列与精度 Profile

状态：`RESEARCH BRIDGE / NONCANONICAL`

对整数 future-observation map

`O : Z^n -> Z^m`

设其 rational rank 为 `r`，Smith normal form 的非零 invariant factors 为

`d_1 | d_2 | ... | d_r`。

标准正合序列给出：

`ker O ~= Z^(n-r)`，

以及

`coker O ~= Z^(m-r) direct_sum Z/d_1 direct_sum ... direct_sum Z/d_r`。

这里包含三种数学性质不同的内容，其中只有两种直接属于 predictive precision。

## 1. state hidden directions

`n-r`

是 declared linear future language 看不见的 state fiber 自由秩，也就是 unresolved-state dimension。

当它降到 0 时，完整 future observation vector 已经能唯一地区分所有整数 states。

## 2. integer coordinate torsion

非单位 Smith factors `d_i>1` 描述 observable state lattice 在 declared integer observation coordinates 中的 non-unimodular embedding。

即使 hidden rank 已经为 0，这些 nonunit factors 仍然可以存在。此时 state 已唯一，但从 observation coordinates 做 integer-linear recovery 仍有同余 / denominator 结构。

full-rank observation map 存在整数线性 left decoder，当且仅当所有非零 Smith factors 都等于 1。

这就是 A2/P023 integer future-observability bridge 中的 coordinate-purification 轴。

## 3. free cokernel rank 是 observation interface excess，不是 state precision

free cokernel rank

`m-r`

属于 declared observation codomain，而不是 unresolved state。

如果向 future signature 中重复加入一条 observation，或者加入 integer-linearly dependent 的 observation，raw coordinate 数 `m` 可以增加，因此 `m-r` 也可以增加，但：

- state kernel 不变；
- 所有非零 Smith factors 不变；
- future-equivalence partition 不变；
- integer coordinate quality 不变。

所以以下量都不能直接叫 predictive precision：

`future words 数量`，

`raw future-signature vector 长度`，

以及单独的 free cokernel rank。

它们可以包含任意多冗余接口坐标。

## 4. 紧凑的整数线性 precision profile

对 declared linear future language，一个更稳健的代数 precision profile 是：

`(hidden_free_rank ; nonzero Smith factors)`，

也就是

`(n-r ; d_1,...,d_r)`。

解释：

- `n-r` 下降表示真正的 hidden state directions 被消掉；
- `n-r=0` 后，future refinement 仍可继续把 nonunit Smith factors 压向 1；
- 加入冗余 observation rows 可以完全不改变这个 profile。

这个 profile 对 state 与 observation 两侧的 unimodular 整数换基不变。

## 5. future row refinement

当 future language 通过**新增 observation rows**扩张时：

- rank 不会下降；
- state kernel 不会变大；
- 每个已经非零的 determinantal divisor 只能按整除关系下降；
- full rank 后仍可通过新增 rows 消掉 Smith torsion，而 state distinguishability 不再变化。

所以 integer-linear precision refinement 在同一个 Smith profile 中包含两个阶段：

```text
kernel-removal stage
    原来为 0 的高阶 determinantal divisors 变成非零

coordinate-purification stage
    已有非零 determinantal divisors 按整除关系向 1 下降
```

冗余 rows 可以对两阶段都没有任何影响。

## 6. 与更大诊断架构的关系

这条 exact sequence 细化了 Foundation-facing 五层 diagnostic：

- FIBER 在这里对应 `ker O`；
- IMAGE/COKERNEL 的整数坐标障碍对应 `coker O` 的 torsion 部分；
- raw observation-interface excess 对应 `coker O` 的 free 部分，它既不是 hidden state，也不应被误当成新增 predictive precision。

DOMAIN、RELATION、LEDGER 只有在其 declared semantics 真正能因子化为线性整数 state 时，才可编译成这里的 `O`。因此这条 exact sequence 是 specialization，而不是 P023 future-signature 的通用替代。

Smith normal form 与有限生成阿贝尔群正合序列都是标准 prior mathematics。项目价值在 precision interpretation，以及明确禁止把 signature length 当成 precision。
