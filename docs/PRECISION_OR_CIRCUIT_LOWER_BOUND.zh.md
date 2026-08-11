# Formulaic Future-Law Execution 的 Exact OR-Circuit Lower Bounds

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Commuting-idempotent mask normal form 已经消除了 exponential law tables，但 resource analysis 还应继续追问：剩下的 work / depth 是否还能降低。

对 OR family，在 fan-in-two OR-only circuit model 中可以得到 exact lower bounds。同时它暴露一个新的 distinction：**materialize reusable normal form** 与 **只把一个 word one-shot 执行到一个 state** 的 optimal depth 不同。

## 1. Reusable word-effect materialization

长度 H 的 word 给出 H 个 k-bit generator masks。

若必须 materialize exact semantic effect mask，则 output coordinate i 是 H 个 input bits 的 OR。

### Depth lower bound

Fan-in-two circuit 中，depth d 的 node 最多依赖 `2^d` 个 inputs。

所以若一个 output 必须依赖全部 H 个 inputs：

`depth >= ceil(log2 H)`。

Balanced OR tree 达到该 bound。

### Work lower bound

一个 H-input OR 至少需要 H-1 个 binary OR gates。

不同 output coordinates 依赖互不相交的 variable sets。OR-only circuit 若把不同 coordinates 混在同一个 gate 中，会引入无法在后续消除的错误 positive dependency。

因此 k 个 coordinates 的 work lower bound 可以直接相加：

`work >= k*(H-1)`。

Coordinatewise balanced trees 同时达到 work / depth 两个 bounds。

所以 parent formulaic normalizer 对“必须输出 reusable effect mask”这个 task 是 jointly work/depth optimal 的。

## 2. One-shot state execution 可以 fuse intermediate

若 normalized effect 不需要被返回、存储、复用，task 只要求 updated state。

每个 output coordinate 是以下 H+1 个 bits 的 OR：

- current state bit；
- H 个 action-mask bits。

因此 exact one-shot lower bounds：

`work >= k*H`，

`depth >= ceil(log2(H+1))`。

把 state bit 与全部 action bits 放进同一 balanced tree 即可同时达到两个 bounds。

## 3. Staged normalize-then-apply 可能有 depth tax

Staged implementation：

1. H 个 action masks 先用 `ceil(log2 H)` depth normalize；
2. effect 再 OR 到 state，增加1 round。

因此 staged depth：

`ceil(log2 H)+1`。

Total work 仍是 `kH`，与 fused one-shot lower bound 相同。

Depth tax：

`ceil(log2 H)+1-ceil(log2(H+1))`。

该值永远只取0或1。

恰当 H 是2的幂时 tax=0；其他 H 则 tax=1。

所以当 effect 只使用一次时，强制 materialize intermediate effect 可能平白增加一层 pipeline depth。

## 4. Sharp H=20 example

k=5,H=20：

### Reusable effect materialization

- work：95 bit ORs；
- depth：5。

### Staged one-shot

- normalization+apply work：100；
- depth：6。

### Fused one-shot

- work：100；
- depth：5。

Fusion 在不增加 bit work 的情况下省掉一整层 execution depth。

## 5. Reuse 会反转 preference

现在让同一个 word effect 作用到 q 个 states。

### Materialize once，reuse q times

Normalize 一次：

`k*(H-1)` work。

Apply 到 q 个 states：

`k*q` work。

Total：

`W_materialized = k*(H-1+q)`。

### 每个 state independent fused

每个 state 支付 kH：

`W_fused=q*k*H`。

Materialization 精确节省：

`W_fused-W_materialized=k*(q-1)*(H-1)`。

q=1 时 saving=0；任何 q>1 且 H>1 时 saving 都严格为正。

所以 reuse count 是独立的 representation-resource coordinate。

## 6. Reuse 下的 parallel depth

若 q 个 state applications 可以在 common normal form 得到后并行执行，则 materialized depth 仍是：

`ceil(log2 H)+1`。

Independent fused executions 也可以彼此并行，其 depth 是：

`ceil(log2(H+1))`。

因此 materialization 最多支付1层额外 parallel depth，却可能在多 consumer 场景节省大量 duplicated work。

## 7. Intermediate state 既不天然是浪费，也不天然有价值

这个结果给项目中更一般 pattern 一个精确实现：

- intermediate representation 对 one-shot terminal computation 可能完全不需要；
- 同一个 intermediate 在 continuation / reuse 被 future language 要求时，可以变得很有价值甚至必要。

所以比较前必须说明 normal form 是：

- ephemeral；
- externally observable；
- cached for repeated execution；
- reused across many states / queries。

## 8. 与 answer-versus-state continuation debt 的关系

Earlier continuation theorem 在 semantic 层区分 terminal answer 与 executable future state。

本文是同一个 exact semantic law 内的 implementation-level analogue：对某个 one-shot query，reusable effect mask 与 fused state update 可以 semantic-equivalent，但是否 materialize intermediate 会改变 work/depth，并决定后续是否能复用。

两个 boundary 不能混为一谈，但共享同一 architecture lesson：intermediate 是否必须持久存在，取决于 future continuation semantics。

## 9. Lower-bound scope

Exact work proof 假设 fan-in-two **OR-only** circuits，且 k 个 coordinates 独立。

这不是 generic Boolean-circuit lower bound，也不声称对 arbitrary word-RAM、SIMD、unbounded-fan-in、hardware lookup、compressed instruction model optimal。

模型刻意保持足够窄，以便 lower bounds 完全精确、可复核。

## 10. Stage131 consequence

Stage131 representation resources 现在还必须加入 **materialization / reuse policy**。

同一个 exact formulaic future law 可以作为：

- reusable normalized operation；
- fused one-shot state update；
- shared normalized operation reused across many states。

它们在特定 query 下 semantics 可以相同，但 optimal execution circuit 不同。

## Owner-local assets

- `src/enterprise_math/or_circuit_execution_lower_bound.py`；
- `src/enterprise_math/or_normal_form_reuse_tradeoff.py`；
- 对应 tests；
- 本双语 theorem note。

## Prior-art / status

OR-tree lower bounds、circuit depth/work 与 common-subexpression reuse 都是标准既有 CS。P023/A2 保留 future-signature / precision ownership。本文只拥有 Stage131 materialization/reuse specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
