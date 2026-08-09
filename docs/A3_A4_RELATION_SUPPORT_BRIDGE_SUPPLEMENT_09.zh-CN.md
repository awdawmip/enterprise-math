# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 09

状态：`ACTIVE RESEARCH NOTE`  
范围：two-stage common-target witnesses 的精确 count-complete state，以及与 A4/E001 incidence algebra 的关系

## 1. Existence frontier 不是 count-complete

Stage 08 已证明 Pareto pruning 对 existence/budget semantics future-safe，但会删除 witness multiplicity。现在寻找更丰富 language 的精确有限状态：

> 对每个 endpoint pair 和每个 budget `(r,s)`，到底有多少 represented intermediate states 满足 two-stage constraints？

继续在有限 zero-relation quotient `X0` 与整数 metric `rho` 上工作。

## 2. B32 — exact witness-cost histogram

对 endpoints `x,z` 定义

\[
\boxed{
H_{xz}(a,b)
=
|\{y\in X_0:\rho(x,y)=a,\ \rho(y,z)=b\}|.
}
\]

只有有限多个 `(a,b)` 的 coefficient 非零。

定义 budgeted witness-count function

\[
\boxed{
N_{xz}(r,s)
=
|\{y:\rho(x,y)\le r,\ \rho(y,z)\le s\}|.
}
\]

则

\[
\boxed{
N_{xz}(r,s)
=
\sum_{a\le r}\sum_{b\le s} H_{xz}(a,b).
}
\]

因此完整 all-budget witness-count language，就是 exact cost histogram 的二维 prefix-sum transform。

## 3. B33 — 精确整数 Möbius inversion

约定任一 index 为负时 `N(r,s)=0`。则

\[
\boxed{
H(a,b)
=
N(a,b)-N(a-1,b)-N(a,b-1)+N(a-1,b-1).
}
\]

所以完整 count-query function 与 histogram 可以只用整数加减法彼此精确恢复。

因此，在有限重新编码意义下，

\[
\boxed{H_{xz}}
\]

就是一个 endpoint pair 的完整 two-stage **witness-multiplicity** budget language 的 P023 task-minimal information coordinate。

当不同 witnesses 落在 dominated 或重复 cost positions 时，它严格比 existence frontier 更丰富。

## 4. B34 — existence frontier 是 histogram 的 Pareto shadow

令

\[
\operatorname{supp}H_{xz}
=\{(a,b):H_{xz}(a,b)>0\}.
\]

则 Stage-05 existence frontier 精确等于

\[
\boxed{
F_{xz}
=
\operatorname{ParetoMin}(\operatorname{supp}H_{xz}).
}
\]

所以 count-complete state 到 existence state 的投影包含两个不可逆步骤：

1. 忘掉正 coefficient 的具体大小，只保留 support；
2. 再删除所有 dominated support points。

这从结构上解释 B31，而不是把 B31 留成一个孤立反例。

## 5. Generating polynomial

把 histogram 打包成有限二元整数 polynomial：

\[
\boxed{
P_{xz}(u,v)
=
\sum_{a,b}H_{xz}(a,b)u^a v^b.
}
\]

`u^a v^b` 的 coefficient 就是 exact staged cost `(a,b)` 的 represented intermediates 数量。

`P_xz` 与 `H_xz` information-equivalent；它只是一个方便的 algebraic representation，不是新本体。

这与 P011 使用整数 generating polynomial 编码 multiplicity spectrum 的方法存在明显共同模式，但 variables 与语义不同。当前 lineage 应标为 `COMPOSABLE_INDEPENDENT / SHARED_COEFFICIENT_ENCODING_PATTERN`，而不是 `SAME_MOTHER`。

## 6. B35 — natural-number matrix product 给出 common-target witness counts

对 radius `r`，令 `M_r` 为 `R_r` 的 `0/1` matrix：

\[
(M_r)_{xy}=1[xR_ry].
\]

由于 A3-generated support family 对称，

\[
\boxed{
(M_rM_s)_{xz}
=
N_{xz}(r,s).
}
\]

natural-number matrix product 计算的是

\[
\sum_y 1[xR_ry]1[yR_sz],
\]

正好等于 represented intermediate/common-target witnesses 的数量。

对结果 booleanize 就恢复 A4 staged existence：

\[
\boxed{
(x,z)\in R_r;R_s
\iff
(M_rM_s)_{xz}>0.
}
\]

这把 bridge 直接接到了 E001/A4 incidence algebra：common-target truth 是整数 witness-count product 的 positive support，而 matrix entry 本身保留 multiplicity。

## 7. 严格 information hierarchy

固定 endpoint pair 与 two-stage language：

\[
\boxed{
\text{labeled witness identities}
\Rightarrow
H/P
\Rightarrow
F
\Rightarrow
\text{single query bit}
}
\]

每个箭头都相对于更丰富 future language 删除信息。

- `H/P` 保留所有 budgeted witness counts，但不保留 witness labels；
- `F` 保留所有 budgeted existence answers，但不保留 counts；
- one bit 只保留一个 declared budget query。

哪个箭头是合法 collapse，完全由 future language 决定。

## 8. 重新看 B31

System A 的 normalized states 为 `0,0.9,2`，System B 为 `0,0.9,1.1,2`。对 endpoints `0,2`，二者存在性 frontier 相同：

\[
F=\{(0,2),(2,0)\}.
\]

但 histograms 不同，因为 System B 在 cost `(2,1)` 处多了一个 coefficient。因此 `N(2,2)` 分别是 `3` 与 `4`。

histogram 恰好检测到了 Pareto compression 删除的那部分信息。

## 9. 跨路线后果

### A4/E001

generated symmetric subclass 现在与 E001 common-target calculation 出现相同的基本 incidence pattern：整数 matrix multiplication 数 common targets，boolean support 给 existence。

### P011

两条路线都使用整数 coefficient encodings 表达 multiplicity data。不要把语义理论直接合并，但可以在结构正确时复用 generating-function 与 inversion 技术。

### A2/P023

当 future language 从 existence 改为 count 时，coarsest repair 会改变。这是一个直接证明：“same geometric support” 不等于 “same sufficient state”。

### P018

只有当 witness multiplicity 是 declared observable 时，count loss 才属于需要修复的 precision loss；否则保存 counts 是无用 detail。

## 10. Prior-art discipline

二维 histogram、prefix sums、Möbius/inclusion-exclusion inversion、incidence matrices 与 natural-number matrix products 都是成熟工具。当前项目特有的研究目标，是把它们精确放入 task-relative A3→A4→P023 state hierarchy，并明确连接已有 E001/P011 multiplicity routes。

## 11. Executable reference

reference layer 新增：

- exact `(a,b)` witness histograms；
- budget prefix-count evaluation；
- 从所有 budget counts 反演恢复 histogram；
- sparse polynomial coefficient representation；
- 通过 support-matrix products 计算 common-target witness-count matrices。
