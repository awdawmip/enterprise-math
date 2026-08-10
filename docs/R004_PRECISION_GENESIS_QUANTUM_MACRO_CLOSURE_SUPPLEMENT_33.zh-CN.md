# R004 精度起源——补充 33：primitive counter ISA gap

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + ISA-RESOURCE SPECIALIZATION`
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_32.zh-CN.md`

设 `M` 为 d 个 coupling-cell coordinates 上的 p-adic residual query module。

## 1. 两种 primitive instruction surface

**Cell-counter ISA。** primitive 只能保存单个 coupling-cell coordinate。第 j 个 coordinate 至少需要 depth

`e_j^cell = log_p |pi_j(M)|`，

总 state mass 为 `mu_cell=sum_j e_j^cell`。

**Aggregate-counter ISA。** primitive 可以直接在 witness 流中累计 arbitrary integer linear combination。此时最小 structural state 就是 module M 本身，

`mu_agg=log_p |M|`。

## 2. Exact ISA gap module

coordinate projections 给出 injection：

`M -> product_j pi_j(M)`。

定义

`G_ISA=(product_j pi_j(M))/M`。

则

`mu_cell-mu_agg = log_p |G_ISA| >= 0`。

因此 aggregate counter 相对 cell counter 节省多少，不是经验 benchmark，而是一个 exact finite p-group quotient。

若 residual module 是 `(1,...,1)` 生成的 diagonal line，cap 为 K，则 cell ISA 需要 d 个 full-depth counters，aggregate ISA 只需一个，精确节省 `(d-1)K`。

## 3. 边界

只有当 primitive execution environment 真能直接累计 declared integer linear combinations 时，aggregate ISA 才合法。若底层只能逐 witness cell 地址化，则 cell ISA 才是正确 capability model。因此 ISA 属于 typed future language，而不是后端实现细节。

## 4. 验证

已 exact 检查 3,200 个随机 residual modules，覆盖 p=2,3、K=1,2、dimension 1..4；全部满足 `mu_agg<=mu_cell`，其中 2,215 例为严格节省。
