# R004 精度起源——补充 26：matroid temporal retirement

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + MODULE-CUT TEMPORAL SPECIALIZATION`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_25.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 25 已证明 generic temporal instruction retirement 可能需要 anticipatory redundancy，因为 stagewise minimum hitting sets 不一定 nested。本补充对 exact-state Module Cut backend 给出一个 sharp positive specialization，并精确指出它何时再次失效。

## 1. Matroid cut translation

在 exact-state Module Cut Compiler 中，每个 suffix point i 都对应 reset-instruction ground set E 上的 representable matroid `M_i`。

deletion cuts 就是 `M_i` 的 circuits。retained reset set `S_i` 击中所有 circuits，当且仅当其补集

`H_i=E\S_i`

在 `M_i` 中 independent。

cardinality-minimum retained set 恰好对应 `H_i` 为 `M_i` 的 basis，因此

`|S_i|=|E|-r(M_i)`。

## 2. Future weakening = nested independent families

假设 suffix requirements 变弱，使

`I(M_i) subseteq I(M_(i+1))`。

任何 earlier safe/independent hidden set 在 later 仍 safe。特别地，`M_i` 的任意 basis `B_i` 在 `M_(i+1)` 中仍 independent。

由普通 matroid basis-extension theorem，`B_i` 可以扩成 `M_(i+1)` 的某个 basis `B_(i+1)`：

`B_i subseteq B_(i+1)`。

取补集即得

`S_(i+1) subseteq S_i`。

所以 no-reacquisition 与整条 chain 上的 stagewise cardinality optimum 完全兼容。

## 3. Exact retirement count

由于每个 stage 都使用 basis complement：

`|S_i|-|S_(i+1)|=r(M_(i+1))-r(M_i)`。

每新释放一个 independent hidden direction，就精确退休一个 primitive reset instruction。

因此对 unit instruction cost，temporal exact-state Module Cut problem 有 closed rank solution，不会出现补充 25 的 anticipatory-redundancy penalty。

## 4. 为什么这是特殊情形

该 theorem 同时使用两个 matroid facts：

1. adequacy 恰好等于 hidden complement independence；
2. 每个 independent set 都能扩成 basis。

Generic obstruction clutter 没有这两个性质。补充 20 的 Structural Target cuts 已经一般不 matroidal，所以此结果不能推广成整个 Representation Compiler 的母定理。

## 5. Nonuniform costs 会让 anticipatory tradeoff 回来

若 generator-specific holding costs 不同，最小化 retained cost 等价于最大化 hidden matroid basis 的总 weight。

Nested matroids 的 maximum-weight bases 一般不再 nested。

一个四元素 binary-representable example 已足够。

Early columns over `F_2`：

`(0,1),(1,0),(1,1),(0,1)`。

Later columns：

`(0,0,1),(0,1,0),(1,0,0),(0,1,1)`。

Early independent family 包含于 later independent family。取 element weights

`(3,2,1,3)`。

Early maximum-weight bases 是

`{0,1}` 与 `{1,3}`，

而 later 唯一 maximum-weight basis 是

`{0,2,3}`。

没有任何 early weighted-optimal basis 被 later weighted-optimal basis 包含。等价地，也不存在 later weighted-minimum retained set 是 early weighted-minimum retained set 的 subset。

因此：

`nested matroid + unit cost => nested stagewise optimum`，

但

`nested matroid + nonuniform cost !=> nested stagewise weighted optimum`。

一旦 resource axis 比 cardinality/rank 更丰富，anticipatory retention 就会重新出现。

## 6. Exhaustive representable-matroid pressure test

枚举 ambient dimension 最多三维的所有四元素 labeled binary-representable matroids，共得到 66 个 distinct independent-set systems。

其中有 **1,270** 对 ordered matroid pairs 满足 independent-family nesting。再遍历 positive element weights `{1,2,3}^4`，共得到 **102,870** 个 pair/weight instances。

- cardinality basis-extension theorem 在所有 nested pairs 上机械成立；
- **792** 个 nested pairs 至少存在一个测试 weight vector，使任何 early maximum-weight basis 都不能嵌入任何 later maximum-weight basis；
- 测试权重中共出现 **15,672** 个此类 nonnested weighted-optimum instances。

所以 weighted failure 即使在 binary-representable matroid family 中也非常常见。

## 7. Architecture consequence

Temporal compiler 必须像 typed future semantics 一样显式声明 resource objective。

- primitive cost 若只是 cardinality，可用 Module Cut rank + basis extension；
- 若 cost nonuniform、time-dependent、acquisition-sensitive 或 p-adic-depth-weighted，则除非另有更强 theorem，应回到 generic temporal cut-cover optimizer。

所以一句“minimum instruction set”在没有 cost model 与 acquisition policy 时数学上不完整。

## 8. Next frontier

下一条值得做的是 p-adic Structural Target retirement。那里 cuts 携带 missing-target modules 与 exponent depths，而不只是 ordinary matroid circuits。开放问题是：nested target-defect exact sequences 是否能给 depth-weighted repairs 一个 tractable temporal cost law，还是 extension data 会让 generic temporal optimization 重新完全出现。
