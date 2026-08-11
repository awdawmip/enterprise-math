# Prefix-Observable OR Semantics：Scan Work/Depth Pareto

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Prefix-observable boundary 已经先固定 semantic object：对 H 个 action masks，executor 必须输出全部 inclusive cumulative OR，而不是只返回 final terminal effect。

只有在这个 semantic requirement 已确定以后，才可以比较不同 execution representations。

两个 exact scan implementations 给出一条清晰的 work / depth / storage tradeoff。

## 1. Declared semantic output

给定 k-bit action masks：

`A_1,...,A_H`，

必须输出所有 prefixes：

`U_t=A_1 OR ... OR A_t`, `t=1,...,H`。

这正是 parent prefix-observable word semantics 的 cumulative-mask normal form。

任何只返回 `U_H` 的 representation 对当前 task 都 semantic insufficient。

## 2. Sequential streaming scan

计算：

`U_1=A_1`，

`U_t=U_(t-1) OR A_t`。

Resource counts：

- word-level binary OR gates：`H-1`；
- bit work：`k*(H-1)`；
- batch dependency depth：`H-1`；
- 除 output sink 外 extra working state：一个 k-bit current mask。

每个 prefix 可以在生成后立即 stream 出去。

## 3. Sequential scan 在 OR-only model 中全局 work-minimal

最终 required prefix `U_H` 本身就是 H 个 independent input masks 的 OR。

即使 earlier prefixes 完全不要求，fan-in-two OR-only circuit 也至少需要 `H-1` 个 word-level OR gates 才能得到这个 final output。

Sequential prefix chain 恰好使用这 `H-1` 个 gates，而每个 intermediate gate output 又正好是一个 required prefix。

因此完整 prefix-output task 不需要额外 OR work：sequential scan 碰到全局 word-gate lower bound。

但它并不 depth-optimal。

## 4. Prefix depth lower bound

Final H-input OR 的 fan-in-two depth 至少：

`ceil(log2 H)`。

所以任何 exact full-prefix circuit 的 critical-path depth 都不能低于该值。

Sequential H-1-gate chain 的 depth 是 H-1，因此 depth-optimal circuit 必须在别的 resource 上付代价。

## 5. Hillis-Steele parallel inclusive scan

使用 synchronized offsets：

`1,2,4,...`。

在 offset s 的 round，所有 `i>=s` 的 positions 计算：

`old[i] OR old[i-s]`，

且读取的是 previous round values。

令：

`r=ceil(log2 H)`。

Exact resource counts：

- parallel depth：`r`；
- word-level OR gates：
  `sum_j(H-2^j)=rH-(2^r-1)`；
- bit work：`k*[rH-(2^r-1)]`；
- 一个简单 synchronized double-buffer implementation 使用 `2H` working masks；
- final round 后全部 H 个 prefix outputs 同时可得。

Owner 对 exhaustive small mask families 把结果逐一与 sequential prefix semantics 对照。

## 6. Hillis-Steele 碰到 unavoidable depth lower bound

它的 synchronized rounds 精确为：

`ceil(log2 H)`，

与 final prefix 强制的 depth lower bound 相同。

所以它在 fan-in-two OR model 中 depth-optimal。

但本文**不**声称 Hillis-Steele 在所有 depth-optimal / near-depth-optimal prefix circuits 中 work 最少。Classical parallel-prefix networks 还有其他 size/depth points。

本文只锁两个 exact、容易审计的 extremal resource points。

## 7. Sharp H=8 comparison

H=8,k=5：

### Sequential

- word OR gates：7；
- bit work：35；
- depth：7；
- extra streaming working masks：1。

### Hillis-Steele

- word OR gates：`3*8-(1+2+4)=17`；
- bit work：85；
- depth：3；
- double-buffer working masks：16。

也就是多10个 word ORs 与更多 buffer storage，换4层 critical-path reduction。

## 8. Sharp H=20 comparison

H=20：

`r=5`。

### Sequential

- word OR gates：19；
- depth：19。

### Hillis-Steele

- word OR gates：`5*20-(32-1)=69`；
- depth：5。

即多50个 word ORs，换14层 batch critical-path reduction。

## 9. Terminal-only balanced reduction 不是当前 semantic task 的合法 Pareto point

Balanced reduction tree 只算 final mask 时，可以用：

- `H-1` word ORs；
- `ceil(log2 H)` depth；
- 1个 final output。

它看起来同时拥有 sequential work lower bound 与 parallel depth lower bound，资源极其诱人。

但它并没有输出 declared future language 要求的 H 个 prefix states。

所以它不是同一 semantic object 的更优 implementation，而是 parent boundary 中**更粗 terminal-only semantic language** 的 implementation。

这给出一个具体警告：不能把 semantic loss 混进 resource Pareto 后再称为 dominance。

## 10. Batch depth 与 streaming latency 是不同资源

若把 H 个 inputs 都视为 time0 已 available，sequential scan 的 batch critical path 是 H-1。

但如果 actions 按 causal stream 一条一条到达，同一个 scan 天然 online：

- 保留一个 current prefix mask；
- consume 下一 action；
- 做一次 OR；
- 立即 emit 下一 prefix。

所以它只有 O(1) extra state，每个 arriving action 一次 update operation。

Hillis-Steele 的 logarithmic depth 是 offline / batch parallel result，依赖整批 inputs 同时可访问与 synchronized rounds。

因此 execution-depth claim 必须声明测量的是：

- offline batch critical path；
- online per-arrival latency；
- total work；
- live working storage。

## 11. Prefix semantics 会改变 optimal representation question

对 terminal-only OR semantics，parent one-shot fused tree 已经足够。

对 full prefix semantics，每个 cumulative state 都必须暴露。Work-minimal structure 变成 sequential prefix chain；若要降低 batch depth，就必须使用真正 prefix network，并支付额外 work / storage。

所以 observation language 的改变不仅增加 semantic states，还会改变整个 execution-resource frontier。

## 12. Stage131 ordering discipline

完整顺序现在很明确：

1. 先声明 terminal vs prefix-observable semantics；
2. 求 exact semantic normal form；
3. 选择 execution model（online/offline、fan-in、working-memory assumptions）；
4. 只在实现同一个 semantic object 的 implementations 之间比较 work / depth / storage。

Terminal-only balanced tree 不能出现在 prefix-semantic Pareto frontier 中作为“支配点”。

## Owner-local assets

- `src/enterprise_math/prefix_or_scan_pareto.py`；
- `tests/test_prefix_or_scan_pareto.py`；
- 本双语 theorem note。

## Prior-art / status

Parallel prefix scan、Hillis-Steele network 与 OR-circuit lower bounds 都是标准既有 CS。P023/A2 保留 future-signature / precision ownership。本文只拥有 Stage131 prefix-semantic resource routing 与 exact resource accounting。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
