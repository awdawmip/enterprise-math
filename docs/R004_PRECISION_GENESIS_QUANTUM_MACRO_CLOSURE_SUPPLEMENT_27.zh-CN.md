# R004 精度起源——补充 27：structural defect diamond 与 premature-collapse debt

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + P-ADIC INTERACTION LAW`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_26.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 20、23 已把 linear Structural Target defect 做成 exact p-adic module，并证明其 mass 沿 nested chain 可加；补充 24 又确定了 semantic last use。本补充把二者接成一条二维定律：**current representation 看见什么**与**remaining future 还需要什么**，通过一个 canonical finite p-group 发生交互。

## 1. 两条轴

令 `R=Z/p^K`。使用 row-submodule coordinates：

- `U=Row(A)`：current/finer observation；
- `U' subseteq U`：coarser observation；
- `W=Row(B)`：stronger target requirement；
- `W' subseteq W`：weaker remaining target requirement。

Structural Target defect 为

`D(U,W)=(U+W)/U`。

对有限 p-group 定义 `mu(M)=log_p|M|`，于是

`delta(U,W)=mu(D(U,W))`。

有限 subgroup 满足

`|U+W||U cap W|=|U||W|`，

故

`delta(U,W)=mu(W)-mu(U cap W)`。

所以 target defect 就是 target structure 中尚未包含在 observation-target intersection 里的部分。

## 2. 相反方向的单调性

若 observation 变粗：

`U' subseteq U`，

则

`delta(U',W)>=delta(U,W)`。

若 remaining future target 变弱：

`W' subseteq W`，

则

`delta(U,W')<=delta(U,W)`。

representation loss 与 semantic retirement 在同一个 defect coordinate 上沿相反方向运动。

## 3. Observation-loss increment modules

在 target W 仍 live 时，把 observation 从 U coarsen 到 U'，新增 target defect 为

`J_W=(U cap W)/(U' cap W)`。

对 weaker target W'：

`J_(W')=(U cap W')/(U' cap W')`。

存在 canonical injection

`J_(W')->J_W`。

因为若 `U cap W'` 中元素在模 `U' cap W` 后变零，它同时属于 W'，故实际上已在 `U' cap W'` 中。

定义 **structural interaction module**：

`I=J_W/J_(W')`。

它有 explicit form：

`I ~= (U cap W)/((U' cap W)+(U cap W'))`。

故

`0 -> J_(W') -> J_W -> I -> 0`。

## 4. Target-retirement increment modules

在 observation U 下把 target 从 W 弱化成 W'，移除的 defect 为

`L_U=(U+W)/(U+W')`。

在 coarser observation U' 下则为

`L_(U')=(U'+W)/(U'+W')`。

存在 natural surjection

`L_(U')->L_U`。

其 kernel canonical isomorphic 于同一个 interaction module I。因此

`0 -> I -> L_(U') -> L_U -> 0`。

所以同一个 finite p-group 同时量化：

- stronger target W 仍 live 时才会出现的**额外 observation-loss defect**；
- observation 已经 coarsened 后，target retirement 才能释放出的**额外 target-defect benefit**。

## 5. Four-point law

取 p-exponent mass：

`mu(J_W)=mu(J_(W'))+mu(I)`，

`mu(L_(U'))=mu(I)+mu(L_U)`。

等价地：

`delta(U',W)+delta(U,W')-delta(U,W)-delta(U',W')=mu(I)>=0`。

这是 nested observation/target submodules 上的 exact four-point cross-supermodular law。

补充 20 已证明 defect 作为 arbitrary hidden-coordinate set 的函数，一般既不 submodular 也不 supermodular。这里没有矛盾：只有切换到正确 typed coordinates `observation submodule x target submodule` 后，才重新出现更强结构定律。

## 6. Premature-collapse debt

假设 target distinction `W/W'` 很快就会 dead。

若在 target retirement **之前**先 coarsen observation，新产生的 defect 为 `J_W`。

若先把 target 弱化成 W'，再执行完全相同的 observation coarsening，只需付出 `J_(W')`。

提前 collapse 的 exact additional price 是：

`mu(I)=mu(J_W)-mu(J_(W'))`。

因此 I 是一个 typed **premature-collapse debt module**。

最小例子在 `F_2^2`：

`U=W=<e_1>`, `U'=W'=0`。

只要 `e_1` 仍是 live target direction，删掉 observation 中的 e1 就产生 1 bit structural defect；若先让 target 退休该方向，同一个 later observation collapse 成本为 0。

在 `Z/2^K` 上取 `U=W=<2^t e_1>`，interaction depth 为 `K-t`；该 penalty 是真正 p-adic depth，而不是只有 rank-one。

## 7. 与 backward semantic liveness 的连接

补充 24 说：certificate distinction 在最后一次 future-sensitive use 之前不能 erase。

本补充增加 resource theorem：

> 即使 early collapse 以后可以 repair，只要它发生在 semantic last use 之前，就会产生精确的 interaction-module debt I。

所以 compiler 现在同时拥有：

- live distinction 不该提前 collapse 的 correctness 理由；
- 若硬要提前 collapse 并稍后 repair，需要支付多少 p-adic structural cost 的 exact 数学。

## 8. Validation

Independent exact checks 包括：

- **6,000** 个 small 2/3-power ambient modules 上的 random subgroup rectangles：defect intersection identity、两条相反单调性、nonnegative four-point interaction 全部成立；其中 657 个 interaction 严格正；
- **1,500** 个额外 random p-group rectangles：observation-loss 与 target-retirement short exact sequences 的 exponent masses 全部匹配；
- **900** 个 random rectangles：explicit interaction quotient profile 与 `L_(U')->L_U` kernel profile 完全一致，不只是 cardinality。

这些是 finite exact WIP checks，不是 fresh full-repository CI 或 canonical-main claims。

## 9. Prior-art 与下一 frontier

有限 subgroup product/intersection cardinality、modular-law quotient identities 与 butterfly/second-isomorphism style arguments 都是 prior algebra。R004 当前 project-local addition 是把其共同 quotient 解释成 typed compiler 中 representation loss 与 future target liveness 的 interaction。

下一步真正值得攻的是 **multi-target interaction**。若 future 同时有多个 target modules `W_1,...,W_m`，premature-collapse debt 能否沿 target overlap 做 Möbius/inclusion decomposition，同时避免 shared structure double-counting？任何这类分解都必须保持整数/module-valued，也不能在 subgroup lattice 不 distributive 的地方偷偷假设 distributivity。
