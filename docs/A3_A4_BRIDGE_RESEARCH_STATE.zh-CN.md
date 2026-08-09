# A3 ↔ A4 Bridge — 当前研究状态

状态：`ACTIVE RESEARCH CHECKPOINT / 暂不提升为 FOUNDATION`  
范围：A3 relation-state ↔ A4 support/correspondence ↔ A2/P023 quotient-safety bridge 的续研入口

## 1. 归属与分支

- A3 owner：`research/core/relation-quotient`。
- A4 owner：`research/core/admissible-support-relations`。
- Bridge owner：`research/core/relation-support-bridge` / Draft PR #83。
- 一般 quotient-safety 母定理：A2/P023（`research/p023-composition-safe-collapse`）。
- 跨分支协调：Research Relay Issue #82。

Bridge 是 A3、A4 的消费者，不替代任何一方。不能因为某个 specialization 在这里有用，就把 A3 partition algebra、A4 arbitrary correspondence theory 或 P023 general factorization 吸进本分支。

## 2. 当前 bridge theorem chain

### B01–B03 — generator 与 quotient boundary

从 closed A3 weighted state

`Z_ij=m_j*c_i-m_i*c_j`

出发，先对 `Z_ij=0` 取 quotient，再定义

`x R_r y iff |Z_ij| <= r*m_i*m_j`。

由此生成一个受限的 A4 admissible-support family。A3 partition aggregation 下，universal fine support 会推出 coarse support，但逆命题因 signed cancellation 一般失败。

### B04–B06 — interpolation

A4 split-completeness 被转化为 represented intermediate states 是否存在。连续 unit states split-complete；`{0,2}` 在 `1+1` split 下失败。

### B07–B09 — integer metric 与 geodesic defect

生成 support family 精确等于整数 metric

`rho(x,y)=ceil(|Z_ij|/(m_i*m_j))`

的 radius filtration。

Global split-completeness 等价于 `rho` 正好是 radius-one graph 的 intrinsic shortest-path metric。`Gamma=d_G1-rho`（断开则为 infinity）就是 interpolation/geodesic defect。

### B10–B12 — endpoint MAY/MUST precision

对 coarse blocks `A,B`：

- `d^- = min rho` 是 all-radius MAY threshold；
- `d^+ = max rho` 是 all-radius MUST threshold；
- `(d^-,d^+)` 在有限重新编码意义下，是 combined endpoint language 的 task-minimal coordinate。

A3 direct aggregate threshold `bar rho` 是不同 observable：有 `bar rho<=d^+`，但与 `d^-` 不存在 universal order relation。

### B13–B20 — staged/two-stage Pareto state

对 endpoints `x,z`，每个 intermediate `y` 对应 cost `(rho(x,y),rho(y,z))`。Pareto-minimal antichain `F_xz` 精确表示所有 two-stage budget existence queries。

对 coarse blocks：

- `F^-` 是精确 staged-MAY frontier；
- `F^+` 是精确 staged-MUST frontier。

一步 thresholds 不能决定 staged semantics。

### B21–B23 — 任意 finite future depth

在 depth `k`，精确 existence state 是 represented chain-cost vectors 在 `N^k` 中的 Pareto frontier `F^(k)`。

若 support metric geodesic/split-complete，则对所有 finite depth：

`R_r1 ; ... ; R_rk = R_(r1+...+rk)`，

并且 `F^(k)` 就是 endpoint distance 的 weak-composition simplex。因此 geodesicity 是一个 finite-future existence-compression certificate。

### B24–B27 — exact support-language quotient

labeled integer metric state `(X0,rho)` 决定全部 generated primitive support relations 与任意 finite support word；反过来，完整 primitive support family 也能恢复 `rho`。

所以 `(m,c,Z)->(X0,rho)` 对 generated support language future-safe。

但它对更丰富 A3 partition aggregation 不 future-safe：已经有 same-metric A3 states 在相同 partition 下产生不同 coarse aggregate threshold 的明确反例。

### B28–B31 — online antichain compression

Existence frontiers 可以通过 exact antichain convolution 递归组合。对 future existence/budget queries，dominated prefix costs 可以永久删除，因为 concatenation 保持 dominance。

但该压缩不保留 witness count。

### B32–B40 — count-complete coefficient layer

Two-stage exact cost histogram `H(a,b)` 通过整数 prefix sum / finite-difference inversion，与全部 budgeted witness counts information-equivalent。natural-number support-matrix product 直接数 common targets；其 boolean support 才是 existence。

任意深度下，count tensors `H^(k)` 通过 non-negative-integer coefficient convolution 递归组合；positive support 再 Pareto-prune 就得到 existence frontier `F^(k)`。

即使 geodesicity 已经把所有 finite-depth existence semantics 压回 endpoint `rho`，witness multiplicity 仍然可能不同，因此 count-sensitive language 必须保存更丰富状态。

## 3. 当前 semantic state ladder

Bridge 当前并没有定义一个 universal precision scalar，而是定义了由 future language 索引的状态阶梯：

`A3 exact relation state (m,c,Z)`

→ `(X0,rho)`：完整 generated-support algebra

→ `H^(k)` / coefficient polynomial：fixed-depth witness-count semantics

→ `F^(k)` Pareto antichain：fixed-depth existence semantics

→ 更窄 query 的 threshold(s) 或 truth bit。

每个向下箭头只有在已经证明被删除信息不会影响 declared future language 时才合法。

## 4. 当前 A3 工作暴露出的独立 selector axis

A3 并行发展出了 guard-image lattice

`L_G=W(K_A)`，

用于表示 piecewise selector 的隐藏自由度。它与 support metric/frontier state 是不同类型的 hidden-information object。

- rank 0：guard visible / descends；
- full rank：每个 strict orthant 都 reachable；
- rank one：exact reachable patterns 化为一个 integer interval；
- arbitrary refinement 甚至可以出现 `exact -> non-exact -> exact`，因为 branch effect 可能先于 selector 暴露。

因此“更多精度”本身不是 semantic order。support-state 与 selector-state 只有在明确声明 product/interaction language 并重新证明 factorization 后才能组合。

## 5. Verification state

Supplements 01–10 已写入 ordinary finite/integer proofs。

已有 reference implementation 与 regression tests 覆盖：

- A3-generated support 与 partition cancellation；
- integer metric/geodesic defect；
- MAY/MUST threshold profiles；
- two-stage 与 coarse staged Pareto frontiers；
- arbitrary-depth existence frontiers；
- support-language metric quotient；
- recursive antichain convolution；
- two-stage 与 arbitrary-depth witness-count coefficient state。

独立会话内 bounded reconstruction 未发现不一致：

- 111,132 个 small weighted states：geodesic/split-completeness equivalence；
- 62,192 个 coarse profiles：staged MAY/MUST frontier semantics；
- 14,016 个 state-depth cases：recursive antichain / count convolution 对 direct path enumeration；
- 4,672 个 weighted states：histogram/prefix-count inversion。

这些只支持证明，不代替 repository CI。本研究会话仍不声称 direct checkout pytest 已通过，因为本地 execution environment 之前出现 GitHub DNS 解析失败。

## 6. Research Relay state

B40 以前的关键 bridge 结果已经回流 Issue #82，并按影响范围定向通知 P023、P018、A4/E001、P022。

继续本分支时必须：

1. 新 general abstraction 前读取最新 Relay；
2. 每个实质 stage 前读取 A3/A4/P023 当前 head；
3. 若 mother theorem 已存在，只在这里增加 specialization/corollary；
4. 正结果与 negative boundary 同等优先回流。

## 7. 当前 branch-integration state

Bridge 活跃期间，A3 base 又向前推进，新增 piecewise-affine quotient 与 guard-image-lattice 研究。Bridge 的 bilingual manifest 已语义吸收这些 dependency pairs，但 PR #83 仍可能需要 clean dependency sync/replay 才能恢复 mergeability。

禁止 force-merge 或覆盖 A3。若需要 restack，只 replay bridge-owned assets，并继续保留 A3 的发现归属。

## 8. 下一步高价值问题

1. **Count-aware online compression**：为选择性的 multiplicity language 找更小 recursive coefficient state；判断 coefficient distribution 何时还能安全聚合。
2. **Identity layer**：精确刻画 witness labels 何时可以删除而 counts 仍 future-complete，并与 A4/E001、P021 witness transport 接起来。
3. **Support × selector product language**：只有在明确 mixed operation algebra 下，才组合 `(X0,rho)` 与 A3 guard-image state，并求 coarsest compatible product quotient。
4. **P023 extraction**：区分哪些 B-results 只是 P023 worked specialization，哪些 arithmetic/metric statement 真正属于 bridge。
5. **A5/P022 specialization**：在实际 lattice/root-lattice geometries 上测 `Gamma`、missing exact splits 与 frontier complexity。
6. **Prior-art audit**：任何新编号或 Foundations 提升前，系统审查 metric quotient、antichain dynamic programming、abstract interpretation MAY/MUST、multiobjective path algebra、incidence/count semirings、automata/congruence 文献。

## 9. Promotion boundary

现在不要新增 `P` 编号，也不要把 bridge 提升进 `FOUNDATIONS`。

未来提升至少需要：

- 在 current main/A3 dependencies 上 clean replay；
- repository CI；
- prior-art/novelty boundary；
- A3、A4、A2 归属边界稳定；
- 证明整合后的 state-ladder principle 具有超出标准工具拼接的长期项目价值。
