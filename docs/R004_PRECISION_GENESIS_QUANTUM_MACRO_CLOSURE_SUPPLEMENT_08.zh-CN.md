# R004 精度宇宙生成 —— Supplement 08：product factorization 与真正的 joint-coupling 边界

状态：`PROVED_WIP + EXECUTABLE_CHECKED + NEGATIVE_BOUNDARY + FOUNDATION_FEEDBACK_CANDIDATE`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_07.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

本补充修正 Supplement 07 末尾的临时 frontier：correlated、non-product action language **本身并不会**在 dynamics 与 observation 仍保持逐 component / product-valued 时强迫 joint representation。真正会破坏 factorization 的，是 observable 或 dynamics 的 cross-axis coupling。

## 1. Product-signature factorization theorem

令

`X = prod_i X_i`。

对每个 joint future action `a=(a_i)`，假设 transition 逐 component 作用：

`a.x=(a_i.x_i)_i`。

声明 observable 为完整 product vector：

`O(x)=(O_i(x_i))_i`。

令 `A` 为任意非空 joint action set。它可以高度 correlated，不需要是各 axis projection 的 Cartesian product。

定义 joint future signature：

`Sigma_A(x)=(O(a.x))_(a in A)`。

对 axis `i`，令

`A_i=pi_i(A)`，

并定义 marginal signature：

`Sigma_i(x_i)=(O_i(a_i.x_i))_(a_i in A_i)`。

### R004-COMP-T05 —— correlation-invisible product kernel

对两个 product states `x,y`，

`Sigma_A(x)=Sigma_A(y)`

当且仅当每个 axis `i` 都满足

`Sigma_i(x_i)=Sigma_i(y_i)`。

因此

`ker(Sigma_A)=prod_i ker(Sigma_i)`。

### Proof

若 joint signatures 相同，则对每个 `a in A`、每个 axis `i`，对应 observable coordinate 都相同。每个 `a_i in A_i` 至少出现在一个 joint action 中，因此所有 marginal signature coordinates 都相同。

反过来，若每个 marginal signature 都相同，则任意 joint action 下完整 product observable 的每个 coordinate 都相同，所以整个 observable vector 相同。∎

这里不需要 action labels 独立，也不需要 Cartesian-product language。

这只是初等 product-kernel mathematics，不能当作新的 generic theorem 主张。

## 2. 对 CRT translation compiler 的直接后果

对

`Z/MZ ~= prod_i Z/p_i^(K_i)Z`，

令 `T subset Z/MZ` 为任意非空有限 translation set；它不需要是 subgroup，也不需要是 CRT projections 的 product。

observable 取各 prime-power component 的完整 capped valuation vector。CRT 下 translation 逐 component 作用，所以 R004-COMP-T05 直接适用。

joint compiler 精确等于：

1. 把 `T` 投影到每个 prime-power component；
2. 每个 projected translation language 使用 Supplement 07 的单轴 p-adic trie compiler；
3. 把各 axis tokens 组成 tuple。

因此 exact class count 为

`C_T=prod_i C_(pi_i T)`，

其中每个 factor 都是单轴 trie class count：

`|C_i| + # deficit nodes_i`。

所以只要 observable 暴露完整 coordinate vector、dynamics 逐 component，joint action-label correlation 对 safe quotient 完全不可见。

Executable `precision_crt_translation_compiler.py` 已直接把该 compiler 与 literal joint future signatures 做 bounded 对照。

## 3. 为什么 Supplement 07 末尾的临时 open problem 消失

Supplement 07 末尾曾担心 correlated action subset 会让 axiswise compiler over-refine，因为某些 joint action combinations 根本不会发生。

在当前 full-vector observation 语义下，这个担心是错误的。

Future equivalence 要求每个实际允许 joint action 后的**每个 observable coordinate**都相同。只要一个 marginal action value 曾在任意 joint action 中出现，对应 axis equality 就已经被要求；缺失的 Cartesian combinations 并不会取消该 marginal requirement。

因此真正的边界不是

`correlated action labels -> joint state`，

而是

`required future outputs 或 dynamics 出现 cross-axis coupling -> potentially joint state`。

这条修正很重要，因为它阻止 compiler 架构仅仅因为 action metadata correlated 就过早引入 relation state。

## 4. 最小 coupled-observation counterexample

取 two-bit product state

`X=(Z/2Z)^2`。

Actions 逐 component XOR。把 full product observation 换成 coupled scalar：

`O(x_1,x_2)=x_1 x_2`。

考虑两个 joint action languages：

`A={(0,0),(1,1)}`

与

`B={(0,1),(1,0)}`。

它们满足：

- action count 都是 `2`；
- 第一 axis marginal action set 都是 `{0,1}`；
- 第二 axis marginal action set 也都是 `{0,1}`。

但 future-safe partitions 不同。

对 `A`：

`{{00},{01,10},{11}}`。

对 `B`：

`{{00,11},{01},{10}}`。

因此一旦 observable 耦合 axes，marginal action languages 与 action cardinality 都不足以决定 safe quotient。

真正产生差异的是 joint actions 如何把两个 axes 的 action values 配对。

所以：

`same action marginals + same action count != same safe quotient`

在 coupled observations 下成立。

## 5. 对 compiler 架构的直接含义

当前 R004 representation compiler 已经得到一条清晰 layering rule。

### 以下条件下 axiswise compiler 精确

- state 是 Cartesian / CRT product；
- dynamics 逐 component 作用；
- 声明 observable 暴露完整 component observables 的 product。

此时取得 marginal action languages 后，可以丢掉 action correlation。

### 以下情况可能必须 joint repair

- observable 混合多个 axes；
- transition 更新一个 axis 时使用另一个 axis；
- future language 要求跨轴 relation / witness identity，而不是独立 coordinate values。

这时缺失的信息不是另一位 valuation digit，而是**coupling state**。

这正是 A3 structured relation-state 与 A4 witness/correspondence machinery 开始成为候选基础工具的位置。R004 应消费这些 owner，而不能把 joint coupling 偷偷编码进 exponent tuple。

## 6. Validation

新增 executable assets：

- `precision_crt_translation_compiler.py`；
- `precision_product_language_factorization.py`；
- 对应 regression files。

Checks 包括：

- two-bit product 上 full product observable 的全部非空 joint action sets；
- modulo `6` 的全部非空 translation languages；
- modulo `12` 中 size 不超过 `3` 的所有 translation languages；
- equal action count + identical marginal action sets 的 coupled-observation 显式反例。

研究过程中先对多个小 CRT moduli 搜索 full-vector observation 下的 over-refinement counterexample，但一直失败；上面的 factorization theorem 解释了为什么这种反例根本不存在。

这些是 finite proof/executable checks，不是 Lean formalization，也不是 fresh full-repository CI。

## 7. Revised compiler frontier

当前 R004 compiler frontier 为：

`one p-power axis + arbitrary translations -> exact p-adic trie compiler`；

`multiple CRT axes + arbitrary correlated translations + full vector observation -> exact product of marginal trie compilers`。

真正剩下的 open problem 已经进一步变窄：

> **给定 finite coupled observable 或 coupled dynamics，能不能把 coarsest joint repair state 编译成 structured relation / witness normal form，而不是 opaque partition table？**

这个问题已经不再是纯 R004-local。它同时触及 P023 minimal repair、P024 action-language precision、A3 relation-state algebra 与 A4 witness/correspondence semantics。任何 mother theorem 都应通过正确 owner / Foundation 路线推进。
