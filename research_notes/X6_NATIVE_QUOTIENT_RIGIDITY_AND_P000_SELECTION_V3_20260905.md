# X6 Cell quotient rigidity：保持四个三轴片时只剩一个二元选择

Status: `DERIVED / EXACT / QUOTIENT_CLASSIFICATION / P000-SELECTION-GATE`
Date: `2026-09-05`
Depends on: `X6_NATIVE_UNIVERSAL_CELL_COMPLETION_V2_20260905.md`

## 1. Setup

令 universal Cell endpoint group

`G = G6^cell ~= Z^2 x Z/2`

且 `t` 为唯一非零 torsion element。

对四个已建立的三轴 slice，令 `G_v` 为其忠实 local Cell subgroup。已经证明

`G/G_v ~= Z/2`

且

`G = G_v x <t>`。

现在允许实际 full Cell endpoint model 额外加入 native cross-slice return relations。群论上等价于取某个 subgroup

`N <= G`

并令

`Q=G/N`。

为了不破坏任何已验证三轴 Cell geometry，要求每个 restriction

`G_v -> Q`

仍然 injective；等价于

`N intersect G_v = {0}`

对四个 v 均成立。

## 2. Quotient rigidity theorem

**定理。** 满足上述 local-slice fidelity 的 `N` 只有

`N={0}`

或

`N=<t>`。

### 证明

任取 `n in N`，固定任意 slice v。

因为 `G/G_v ~= Z/2`，所以

`2n in G_v`。

又因为 `N` 是 subgroup，

`2n in N`。

local fidelity 给出

`N intersect G_v={0}`，

故

`2n=0`。

因此 N 的每个元素都是 G 中的 torsion element。可是

`Tor(G)=<t> ~= Z/2`。

所以

`N <= <t>`，

只有 `N=0` 或 `N=<t>` 两种。证毕。

这说明：一旦要求四个当前三轴片都精确保真，任何进一步 global Cell identification 都不能连续地、任意地增加；唯一可再压掉的信息就是 companion `t`。

## 3. 两个剩余模型

### Model U — two-sheet universal completion

`Q_U=G ~= Z^2 x Z/2`。

每个 slice 的 ordinary visible endpoint 有一个二元 fibre：

`{g,g+t}`。

一个 local min-zero triple 加一个 sheet bit 恢复 full Cell。

### Model C — companion-collapsed quotient

`Q_C=G/<t> ~= Z^2`。

因为

`G=G_v x <t>`，

每个 `G_v -> Q_C` 都不只是 injective，而且是 isomorphism。

所以在 Model C 中，任意一个三轴 slice endpoint state 已经足以表示整个 full Cell endpoint state；不存在 universal two-sheet information。

## 4. 与 P000 `SLICE_OBSERVATION != FULL_CELL_STATE` 的关系

P000 当前冻结：

- `THREE_AXIS_SLICE != FULL_ENTERPRISE_SPACE`；
- `SLICE_OBSERVATION != FULL_CELL_STATE`；
- omitted spatial coordinates are not nonexistent coordinates。

若把这里的 `SLICE_OBSERVATION != FULL_CELL_STATE` 采用**信息不完备/非单射**的 operational reading：

`ORDINARY_3AXIS_CELL_OBSERVATION_IS_NOT_STATE_COMPLETE`，

则 Model C 被立即排除，因为其中 `G_v -> Q_C` 是同构；唯一剩下 Model U，故

`X6_native endpoint state = torsor(G6^cell)`。

这是一个严格条件定理：

`LOCAL_SLICE_FIDELITY + SLICE_OBSERVATION_NONINJECTIVE -> NO_EXTRA_QUOTIENT -> X6=G6^cell`。

如果旧 P000 语句只被解释为“观察类型与 full-state 类型名称不同”，而不承诺信息非单射，则不能单凭 `!=` 符号排除 Model C。不能把 type inequality 偷换成 information loss theorem。

因此当前最后一个语义门槛已被压缩为：

`Does P000's slice-not-full invariant mean a slice endpoint observation is genuinely not state-complete?`

项目文本中“slice 可以忽略其余空间坐标”“omitted coordinates != nonexistent coordinates”强烈支持 non-state-complete reading；但在正式 Foundation promotion 时应把该语义直接写成 machine invariant，而不是依赖自然语言猜测。

## 5. 六轴 distinctness 的额外诊断

若杀掉 t，则三组 K4 opposite axes 在 Cell endpoint action 上成对相同：

`AB=CD`, `AC=BD`, `AD=BC` in `Q_C`。

这并不逻辑上自动消灭它们作为不同 path/trace labels 的身份，所以不能单靠 P000 axis count 证明 Model C 矛盾；same endpoint transition 与 same native line 仍是不同观察者。

但它说明 Model C 把六轴 endpoint action 压成三对完全重合的动作，而 Model U 保留六个 distinct one-step endpoint generators 与 12 个 distinct directed neighbours。

这是选择 Model U 的结构证据，但不是独立于 slice-information invariant 的证明。

## 6. 收敛状态

在“actual X6 是 universal completion 的 endpoint quotient，且四个局部三轴 Cell 片必须 faithfully survive”这一自然模型类中，数学自由度已经完全分类：

`X6 candidate set = { G, G/<t> }`。

不存在第三种 quotient completion。

因此后续研究不应继续搜索连续参数或任意 hidden state quotient；只需要把 P000 的 slice-observation 语义精确化为 information-preserving / information-losing contract，即可在此模型类内唯一决定 X6。
