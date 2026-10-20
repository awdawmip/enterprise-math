# FINAL_REPORT.zh — Claude/RH 证明传闻独立复跑

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`  
Driver: `EM-DVR-7Q4K2C`

# 最终状态

\[
\boxed{\texttt{SOURCE\_FOUND\_NOT\_FULL\_RH\_CLAIM}}
\]

## 一、直接回答

\[
\boxed{\text{目前能够锁定的“Claude RH”第一手对象，不能从头跑成 RH proof。}}
\]

原因不是“数学界没承认”，而是更基础：

**最强 Claude-specific 第一手对象本身明确没有声称证明 RH。**

Coleman / Claude Fable 5 的 V6 canonical paper 把 RH 标成 `OPEN`，把
\[
\det_\zeta(L^2_{\Phi,K}^{reg}-(z^2+1/4))=C\Xi(z)
\]
标成尚未关闭的 determinant bridge，并公开记录其直接 eigenvalue route 因 counting mismatch 而失败。

所以，若传闻指的是 Claude V6，那么“Claude 已证明 RH”在 source level 就已经发生了升级/误传。

## 二、Claude V6 路线能跑到哪里？

可独立跑通：

1. regulated coupling 的 weighted symmetry；
2. `sigma>1/2` 时 Hilbert–Schmidt；
3. bounded/compact perturbation 不改变 `n^4` 主谱阶；
4. 因而
   \[
   N_H(\Lambda)\sim\Lambda^{1/4}.
   \]

若希望特征值为
\[
\gamma_n^2+\frac14,
\]
Riemann–von Mangoldt 要求
\[
N_{\rm target}(\Lambda)
\sim
\frac{\sqrt\Lambda}{4\pi}\log\Lambda.
\]

两者的比值发散。

因此：

\[
\boxed{
\text{frozen bounded square-difference operator cannot have the full Riemann-zero spectrum.}
}
\]

这是一条已闭合的**负定理**，不是数值拟合意见。

它不排除一个本质不同的 unbounded / prime-carrying / trace-formula operator；但那需要新的数学。

## 三、如果传闻实际来自“Claude 辅助了一篇声称证明 RH 的论文”呢？

最强公开对象之一是 Avi Gershon 2026 v1。

该论文致谢明确说 Claude Opus 4.6 参与 computation / review / Lean 4 formalization，而论文作者声称无条件证明 RH。

这条 proof 的最早未闭合梁是 Lemma 8；但我们进一步找到了一根可以**直接证明已经断裂**的梁：

\[
\boxed{\text{Lemma 10 — Spectral-gap factorisation}}
\]

论文自己定义
\[
g(z)=\sum_{m\ge0}\gamma_m z^m
\]
为 entire，却声称 Hadamard factorization 导出
\[
\gamma_m
=
R_1\rho_1^m+R_2\rho_2^m
+O(\delta_3^m\rho_1^m),
\qquad \rho_1>0.
\]

entire 函数的 Taylor 系数必须满足
\[
\limsup |\gamma_m|^{1/m}=0.
\]

上述非零指数主项却强迫
\[
\limsup |\gamma_m|^{1/m}=\rho_1>0.
\]

矛盾。

所以这不是“还需要补细节”，而是：

\[
\boxed{\texttt{FALSE\_LEMMA}}
\]

它下游承担 spectral-gap reduction、universal unitarity、全体 Toeplitz determinant positivity 和最终 TP∞/Laguerre–Pólya closure，因此完整 RH chain 断裂。

## 四、spectral determinant fallback 复跑

Yamaguchi v3 试图通过 Gram Jacobi self-adjoint operator 和 determinant ratio 得到 RH。

致命节点出现在 Hadamard rigidity：

它把
\[
F(z)=\xi(1/2+iz)
\]
直接写成
\[
F(z)=\xi(0)\prod_k(1-z^2/\gamma_k^2),
\]
理由是把所有非平凡零点配成
\(1/2\pm i\gamma_k\)。

但若
\[
\rho=\beta+i\gamma,
\]
对应的 \(F\) 零点是
\[
z=\gamma-i(\beta-1/2),
\]
只有在 \(\beta=1/2\) 时才是实数。

所以它在建立 spectral divisor equality 之前已经把全体 zeros 参数化成 critical-line zeros。

分类：

\[
\boxed{\texttt{CIRCULARITY}}
\]

self-adjointness 本身救不了这一步；缺失的正是 Hilbert–Pólya 的 spectral bridge。

## 五、negative control

CIPHER/RTSG 的公开 adversarial archive 已经把自己的 RH functional bridge 判为失败：

- bridge equation 最终退化成 `1=1`;
- positivity route 出现反例/负值；
- 核心 self-adjoint spectral construction 仍开放。

本次 verifier 在不知道它“应该失败”的数学层面上，同样把 bridge 识别成 tautology/circularity。

因此：

\[
\boxed{\text{negative-control verifier calibration = PASS}}
\]

## 六、有没有 surviving theorem？

有。

### Claude V6 surviving negative theorem

对 frozen bounded square-difference kernel：

> Hilbert–Schmidt / bounded compact coupling 不能把 `n^4` 谱计数改造成 squared Riemann-zero 的 `sqrt(Lambda) log Lambda` 计数。

这条是严格可复用的 route-exclusion theorem。

### Gershon route

本次失败证书**没有**反驳其所有有限计算或 TP2/log-concavity 子结果。它只说明这些子结果不能通过当前 Lemma 10 链条升级成 TP∞ / RH。

因此保留：

`finite certificates / TP2 claims = SURVIVE THIS ATTACK, NOT PROMOTED TO RH`.

## 七、精度优先翻译结果

精度世界把 RH 验证拆成：

```text
finite zero/divisor cells
    +
finite height
    +
declared future operations
    ↓
uniform safe extension theorem
    ↓
unbounded height/refinement
```

这使 Candidate B 的问题尤其清楚：

有限 interval certificates 并不坏；坏的是把有限状态扩展到所有未来 `r,n` 的 uniform bridge。Lemma 8 / 10 正是承担这件事的压缩梁，而它们没有闭合。

Candidate A 的 counting mismatch 更强：它在有限分辨率下也保持，因此不是 continuum 幻觉造成的失败。

Candidate C 的 entire equality 则是典型的无限压缩语言；有限 ratio samples 永远不能替代 exact divisor identity。

## 八、Formalization 决策

没有制造 `EnterpriseMath/RH/` 空壳，也没有把 candidate bridge 作为 axiom/sorry 塞进 Lean。

原因：最值得 formalize 的 load-bearing lemma 已经被经典数学直接判 false；formalizing a false theorem with assumptions would降低而不是提高证据质量。

Formal status:

- written counterargument: `CHECKED_CLASSICALLY`;
- finite executable stress tests: `EXECUTABLE_CHECKED_LOCAL`;
- Lean: `NOT_CREATED_BY_DESIGN`.

## 九、最终问题的严格答案

### “Claude 所谓 RH proof 到底能不能从头跑通？”

\[
\boxed{\text{不能。}}
\]

更精确地说：

1. 我们锁定的最强 Claude-specific RH source **根本没有声称完整 proof**；
2. 其直接谱路线有 rigorous counting obstruction；
3. 一个真实存在、明确致谢 Claude 的 full-RH preprint 在 Lemma 10 出现明确 FALSE_LEMMA；
4. 一个独立 spectral-determinant full claim 在 exact divisor bridge 处 circular；
5. negative control 被 verifier 正确判失败。

### “最早在哪一个不可替代的 load-bearing lemma 处断裂？”

对不同 source 必须分别回答，不能伪造一个统一 proof：

- Claude V6: `A_DET_BRIDGE` 从未被证明；direct eigenvalue realization 被 counting mismatch 关闭。
- Gershon full claim: **Lemma 8 最早未闭合；Lemma 10 是最早被本次复跑直接判假的 load-bearing lemma。**
- Yamaguchi fallback: Hadamard-rigidity 的 real-zero factorization 是 hidden RH assumption。

本次 Failure Certificate 选择 Gershon Lemma 10 作为最硬的“第一根已证断梁”。

## 十、任务后完成度

| 模块 | 任务前 | 本轮 |
|---|---:|---:|
| Claude-RH source provenance | 10% | **100% for strongest located object; unique rumor origin unresolved** |
| exact proof reconstruction | 0% | **100% through fatal node for fallback full claims** |
| proof dependency graph | 0% | **100%** |
| independent mathematical rerun | 0% | **100% through first fatal node** |
| adversarial verification | 0% | **100% through first fatal node** |
| precision-first translation | 0% | **~70%** |
| formal load-bearing verification | 0% | **classical false-lemma certificate; Lean intentionally N/A** |

## 十一、后续真正值得推进的研究对象

不是继续问“Claude 有没有证明 RH”，而是分离三个数学对象：

1. **V6 route-exclusion theorem** 能否推广到更大的 compact/relative-compact perturbation class；
2. Gershon 中独立于 false Lemma 10 的 TP2 / finite Toeplitz 结果是否有值得保存的新 weaker theorem；
3. 是否存在一个真正不使用 target zero divisor 的 determinant/divisor bridge criterion，可被精度优先语言表达成 uniform future-safe certificate。

当前没有数学 HARD_BLOCK；只是原始 rumor 的唯一传播起点没有被唯一锁定，这不妨碍本次证明复跑结论。
