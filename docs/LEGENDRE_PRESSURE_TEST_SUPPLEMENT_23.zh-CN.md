# Legendre 压力测试 — 补充 23

状态：`PROVED RESEARCH NOTE`  
范围：least-prime shell identity 与 stripped-cofactor root 之间的 directed precision geometry  
依赖：P018 all-power two-basin quotient theorem、P017 exact p-rough cofactor windows、P023-S12 directed repair geometry  
纪律：这是 finite square-basin state representations 的结构定理，不证明 Legendre 猜想，也不单独规定全局最优 factoring algorithm。

## 1. 同一 composite states 上的两个 task coordinates

对 composite state

\[
k^2<n<(k+1)^2,
\]

写

\[
p=\operatorname{spf}(n),
\qquad
q=n/p.
\]

比较两个 retained task coordinates：

\[
P(n)=p
\]

以及

\[
R(n)=R_2(q).
\]

`P` 记录 least-prime shell；`R` 记录 exact stripped cofactor 的 integer square-root basin。

P023-S12 给出两个不同的 directed repair factors：

\[
\rho(P,R)
\]

表示已经知道 factor identity 后再加入 root 的成本；

\[
\rho(R,P)
\]

表示只保留 root 后重新恢复 factor identity 的成本。

这两个方向没有理由具有相同成本。

## 2. L064-A —— Factor-to-root repair 全局至多 binary

状态：`PROVED`。

对每个至少包含一个 composite state 的 square basin，

\[
\boxed{
\rho(P,R)\le2.
}
\]

等价地，一旦 least prime `p` 已知，stripped cofactor root 最多只需要一个额外 binary repair symbol。

### 证明

固定一个 least-prime shell `p`。

该 shell 中每个 state 都写成

\[
n=pq,
\]

且 `n` 全部位于同一个由 `k` 标记的 source square basin 中。

暂时忘掉 p-rough 条件，对整个 source basin 使用 P018 all-power quotient theorem 的 exponent `2`、divisor `p` 特例。它给出

\[
R_2\!\left(\left\lfloor\frac np\right\rfloor\right)
\in\{j_p,j_p+1\}
\]

其中 base target root `j_p` 只依赖 `k,p`。

在真实 `p` shell 上，`n` 被 `p` 整除，所以

\[
\left\lfloor\frac np\right\rfloor=q.
\]

p-rough realizability filter 只会删除 quotient states，不可能制造第三个 root value。因此每个 `P=p` block 最多只与两个 `R` blocks 相交。

取最大 incidence degree 即得

\[
\rho(P,R)\le2.
\]

∎

## 3. L064-B —— binary 上界是 sharp 的

状态：`PROVED BY EXPLICIT WITNESS`。

取

\[
k=18,
\qquad
p=7.
\]

两个状态

\[
329=7\cdot47
\]

与

\[
343=7\cdot49
\]

都位于

\[
(18^2,19^2)=(324,361),
\]

而且最小素因子都为 `7`。

但

\[
R_2(47)=6,
\qquad
R_2(49)=7.
\]

因此同一个 factor block 实际碰到两个 root blocks，于是该 basin 中

\[
\boxed{
\rho(P,R)=2.
}
\]

所以全局 one-bit 上界不能再加强为 zero repair。

## 4. L064-C —— 反向至少可以需要八个 symbols

状态：`PROVED BY EXPLICIT WITNESS`。

在

\[
k=1737,
\qquad
R=45
\]

时，同一个 cofactor-root fiber 同时包含以下八条真实 least-prime shells：

\[
\boxed{
1429,1439,1447,1451,1459,1471,1481,1489.
}
\]

显式 witnesses 为：

| `p` | prime cofactor `q` | `n=pq` | `R_2(q)` |
|---:|---:|---:|---:|
| 1429 | 2113 | 3019477 | 45 |
| 1439 | 2099 | 3020461 | 45 |
| 1447 | 2087 | 3019889 | 45 |
| 1451 | 2081 | 3019531 | 45 |
| 1459 | 2069 | 3018671 | 45 |
| 1471 | 2053 | 3019963 | 45 |
| 1481 | 2039 | 3019759 | 45 |
| 1489 | 2027 | 3018203 | 45 |

表中所有 `p,q` 都是素数，满足 `p<q`，且每个乘积都位于

\[
(1737^2,1738^2)
=(3017169,3020644).
\]

所以每个乘积的 least prime factor 都是对应的 `p`，而全部 stripped cofactors 都位于 root basin `45`。

因此

\[
\boxed{
\rho(R,P)\ge8.
}
\]

可执行全 basin 审计进一步显示，在这个 `k` 上 `8` 实际就是最大值。

## 5. Directed binary depth 的不对称

使用 S12 的 base-two depth

\[
d_2(E,F)=L_2(\rho(E,F)),
\]

L064-A 与 `k=1737` witness 给出

\[
\boxed{d_2(P,R)=1,}
\]

而

\[
\boxed{d_2(R,P)=3.}
\]

所以同一对 task coordinates 的 directed binary symbol depth 可以相差三倍。

这是 S12 “precision geometry 在 symmetrization 前天然有方向”的严格数论实例。

## 6. Raw-envelope 的反向 burden 已证无界

补充 21 已证明：如果删除 p-rough realizability filter，把每个 exact cofactor-window label 都当成可能状态，则沿 square-of-square diagonal，root-to-factor raw burden 无界。

因此

\[
\boxed{
\sup \rho(R,P)_{\rm raw}=\infty.
}
\]

对**真实** least-prime shells，补充 22 已经把 diagonal unboundedness 精确归约为两个 restricted Goldbach slices，但该无界性仍保持开放。

当前层级因此是：

- factor-to-root actual repair：全局至多 `2`；
- root-to-factor actual repair：显式 witness 已至少达到 `8`，是否无界仍开放；
- root-to-factor raw-window repair：已经严格证明无界。

## 7. 这个不对称为什么影响 P017 recursion

一旦 least-prime shell 已经知道，继续压到 cofactor root 是 uniformly bounded 的：最多只剩一个 bit 的 residual root ambiguity。

反向则本质不同。root collapse 可以把很多不同 factor shells 合并在一起，之后若 recursion 仍需要 shell identity，恢复它可能需要大得多的 alphabet。

因此

\[
\boxed{
\text{factor 已知}\to\text{root}
\quad\text{uniformly cheap},
}
\]

而

\[
\boxed{
\text{root 已知}\to\text{factor identity}
\quad\text{未必 cheap}.
}
\]

这给出一个 theorem-level 理由：当后续 recursion 仍需要 shell identity 时，不应在保留 identity 之前过早做 aggressive root compression。

## 8. Scheduling 边界

这个 directed inequality **不能**单独证明完整算法永远应该先求 least-prime identity 再求 root。

S14 已说明，总 acquisition cost 取决于完整 task family 与当前 context。最初得到 `P` 的成本可能与最初得到 `R` 的成本不同。

L064 只证明：当其中一个 coordinate 已经知道后，向另一个 coordinate 转换的 conditional cost 是怎样的。

因此必须区分：

\[
\boxed{
\text{cheap conditional repair}
\neq
\text{globally optimal first task}.
}
\]

## 9. 可执行规范

- `src/enterprise_math/p017_directional_root_factor_precision.py`
- `tests/test_p017_directional_root_factor_precision.py`

回归在较宽有限范围验证 `rho(P,R)<=2`，固定 sharp `k=18,p=7` two-root witness，并检查 `k=1737` 的精确 directed factors `2` 与 `8`，从而得到 binary depths `1` 与 `3`。

## 10. 工具反哺

这条结果再次闭合 research-tool loop：

\[
\boxed{
\text{P018 two-basin transport}
\to
\text{P023 incidence geometry}
\to
\text{P017 directed precision theorem}.
}
\]

因此 abstract repair metric 不是单纯 bookkeeping。它暴露了原 quotient-window 语言里没有明确写出的真实数论 state-compression 不对称。
