# R004 精度起源——补充 22：nonlinear defect bundle 与 A4 escalation gate

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + A4_ESCALATION_BRIDGE`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_21.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 20–21 已为 linear target 找到很强的 structured defect object：有限 p-group missing-target module。本补充关闭 arbitrary nonlinear target 的边界。正确 fallback 不是再造一个 scalar/module，而是回到项目既有的 A4-style support correspondence。

## 1. Canonical nonlinear target correspondence

设 `q:X->Q` 为任意有限 collapse，`t:X->T` 为任意 deterministic target。定义

`R_(q,t) subseteq Q x T`

使

`a R_(q,t) y iff exists x: q(x)=a and t(x)=y`。

等价地，

`R_(q,t)(a)=t(q^{-1}(a))`。

这就是 coarse world 看到的 exact target-uncertainty bundle。

当且仅当每个 fiber support 都是 singleton 时，target 才能下降成 coarse function。

## 2. Composition law

对任意 post-relation `S subseteq T x U`，future step S 之后的 exact coarse support 就是

`R_(q,t);S`。

这只是普通 relational composition。因此 arbitrary nonlinear target support 本来就属于 A4 correspondence/composition layer。

若 future language 只问 MAY support，`R_(q,t)` 已充分。若还要求 witness multiplicity、labels 或 witness identity，则 Boolean support 不够，必须使用补充 13 的 typed monoid/weighted relation compiler。

## 3. Group-valued target 与 derivative gate

现在设 X,T 为有限 abelian groups，q 是对 subgroup K 的 quotient。对 `k in K` 定义 discrete target derivative

`partial_k t(x)=t(x+k)-t(x)`。

若对每个 k，`partial_k t(x)` 都与 x 无关，定义

`phi(k)=partial_k t(x)`。

则 phi 自动是 group homomorphism：

`phi(k+l)=phi(k)+phi(l)`。

并且每个 coarse fiber 都满足

`t(x+K)=t(x)+im(phi)`。

因此 nonlinear support correspondence 可以压成

`coarse base value in T/im(phi) + uniform defect subgroup im(phi)`。

这正是 linear-module case 背后的 exact gate。若 q,t 本身都是 homomorphisms，则 `phi=t|_K`，补充 20 的 missing-target module 就是该 kernel-image defect 的有限对偶表示。

## 4. State-dependent defect bundle：cubic mod 8

取

`X=Z/8`, `q(x)=x mod 4`, `t(x)=x^3 mod 8`。

kernel translation 为 `+4`，但 target variation 依赖 coarse state：

- coarse 0：target support `{0}`；
- coarse 1：target support `{1,5}`；
- coarse 2：target support `{0}`；
- coarse 3：target support `{3,7}`。

所以不存在一个 global defect subgroup 同时表示所有 fibers。正确对象是 state-dependent A4 correspondence。

这说明真正的 nonlinear boundary 不是“fine 公式里有没有平方/立方”，而是 fiber behavior 是否依赖 coarse base state。

## 5. Common coset support 弱于 action semantics

即使每个 fiber support 都是同一个 subgroup 的 coset，也未必存在 uniform action defect。

取

`X=Z/6`, `K={0,2,4}`, `Q=Z/2`, `T=Z/3`。

构造 target，使 kernel translation `+2` 在 even coarse fiber 上表现为 T 中 `+1`，而在 odd coarse fiber 上表现为 `-1`。

两个 coarse fibers 的 MAY support 都完全相同：整个 `Z/3`。所以 support-level compression 会看到同一个 subgroup `H=T`。

但

`partial_2 t(x)`

对 even x 为 `+1`，对 odd x 为 `-1`。它依赖 basepoint，因此不存在一个 homomorphism `phi:K->T` 编码 target transport。

故

`common support coset !=> action/witness homogeneity`。

MAY-only task 可以使用 support compression；若 task 还必须执行 kernel actions 或保留 witness transport，则必须 fail derivative gate 并保留 richer typed semantics。

## 6. Defect representation ladder

当前 compiler 得到一条 fail-closed nonlinear target ladder：

1. **Linear / translation-homogeneous target**：使用 uniform group/module defect；p-adic linear case 使用 Structural Target missing-module 与 Smith profile。
2. **Support-coset target**：若只要求 MAY semantics，可以用 coarse-state coset bundle 压缩 A4 correspondence。
3. **Arbitrary deterministic target + MAY semantics**：使用完整 A4 support correspondence `R_(q,t)`。
4. **COUNT/LABEL/witness semantics**：使用 typed monoid/weighted relation state。

State type 由 declared future semantics 与最强已证明 structure gate 决定，绝不能根据公式长相猜。

## 7. Ownership boundary

Generic relations/correspondences 及其 composition 属于 A4；generic future-safe quotient minimality 属于 P023。R004 当前只提供 reduction/fail-closed dispatch rule：什么时候自己的 structured linear defect 可以使用，什么时候必须升级回 A4。

本补充刻意不创造名为“nonlinear defect algebra”的新 mother abstraction。canonical nonlinear object 早已存在于项目 relation/correspondence 层。

## 8. Next frontier

剩余真正困难的是 **typed defect composition across representation changes**。对 successive collapses / targets

`X -> Q -> R`，

什么时候 structured defect certificate 能在不重新打开 fine state 的情况下 transport/compose？Linear module defect、A4 correspondence、typed weighted relations 都各自有 composition law，但 mixed certificate calculus 必须保留每份 certificate 属于哪一层 semantics。
