# PROOF_DAG.zh — Claude/RH 传闻与 fallback 证明依赖图

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`

## 0. 顶层终点

\[
RH \iff \Xi(z)=\xi(1/2+iz)\text{ 的全部零点都为实数}.
\]

这一步是标准等价，不是证明的新内容。

---

## A. Claude/Fable V6 谱算子路线

```text
RH
↑
all zeros of Xi are real
↑
[OPEN] detζ(L²_{Φ,K}^{reg}-(z²+1/4)) = C Xi(z)
  + exact multiplicities
  + no extra zeros/poles
  + spectral completeness
↑
self-adjoint / domain-correct L²_{Φ,K}^{reg}
↑
Hilbert–Schmidt regulated coupling, σ>1/2
```

独立复跑同时给出一条**负向支路**：

```text
diagonal d_n = n^4 + O(n^2)
+
bounded/compact K
⇒ λ_n = n^4 + O(n^2)
⇒ N_H(Λ) ~ Λ^(1/4)

but intended λ_n = γ_n² + 1/4
⇒ N_target(Λ) = N_zeta(sqrt(Λ-1/4))
   ~ (sqrtΛ/(4π)) log Λ

Λ^(1/4) != sqrtΛ logΛ
⇒ exact eigenvalue bijection impossible for this bounded-coupling realization
```

节点分类：

- `K_sigma^reg Hilbert-Schmidt`: `CANDIDATE_LEMMA` → **REPRODUCED**
- self-adjoint domain statement: `CANDIDATE_LEMMA` → **partial / source marks proposed in canonical paper**
- determinant equality: `CANDIDATE_LEMMA` → **OPEN**
- counting mismatch: `STANDARD_THEOREM` + independent reconstruction → **CLOSED NEGATIVE**
- numerical eigenvalue matching: `NUMERICAL_EVIDENCE` only.

因此 Candidate A 从来没有形成一条完整的 RH proof chain。

---

## B. Xi kernel / TP∞ / Toeplitz route（Gershon v1）

```text
RH
↑
Xi ∈ Laguerre–Pólya / coefficient sequence PF∞
↑
D_r(n) > 0 for all r,n
↑
DJ unitarity:
  Σ_s |log Θ_s(n)| < μ_1(n), every n
↑
global tail / spectral separation
├── Lemma 8: uniform level-r smoothness / curvature inheritance
├── Lemma 10: Taylor-coefficient “spectral gap” expansion
├── Lemma 11: reciprocal-coefficient dominant-zero tail
└── finite interval certificates
```

### B-L8 — earliest unclosed load-bearing node

论文声称高层 tilted potentials 继承至少同样的 Bakry–Émery 曲率，从而
\(\sup_s C_s\le1\)。

分类：`CANDIDATE_LEMMA / UNPROVED_LEMMA`.

给出的文字没有推导出
\(W_p^{(s)''}\ge W_p''\)；数值检查 \(s\le40\) 不能替代全局命题。

### B-L10 — earliest demonstrably false load-bearing node

论文先定义

\[
g(z)=\sum_{m\ge0}\gamma_m z^m
\]

并明确称 \(g\) 为 entire；随后从 Hadamard factorization 推出

\[
\gamma_m
=
R_1\rho_1^m+R_2\rho_2^m
+O(\delta_3^m\rho_1^m),
\qquad \rho_1=1/|z_1|>0.
\]

这对 \(g\) 的 **Taylor coefficients** 不成立。

最短反证使用 Cauchy–Hadamard：

\[
g \text{ entire}
\Longrightarrow
\limsup_{m\to\infty}|\gamma_m|^{1/m}=0.
\]

若上述展开中首个非零项 \(R_1\rho_1^m\) 存在，则

\[
\limsup |\gamma_m|^{1/m}=\rho_1>0,
\]

矛盾。

Hadamard 零点乘积控制的是零点结构；倒数函数 \(1/g\) 在满足条件时可由部分分式产生“极点倒数的指数和”，但这不是 \(g\) 本身的 Taylor 系数。

分类：`FALSE_LEMMA`.

该节点直接供给 spectral-gap reduction 和全局 Region C1，因此其下游 universal positivity 失效。

### B-L11 — circularity/incompleteness

对 \(1/g\) 的 reciprocal coefficients 使用部分分式本身可以是合法方向，但论文随后把全部相关 poles/zeros 写成

\[
\rho_m=-1/t_m^2
\]

并以 critical-line zeta ordinates \(t_m\) 排列。若此处意在覆盖 \(g\) 的**全部**零点，则正是在使用要证明的实零点结构。论文自己的 Remark 19 也承认用 critical-line zero spacing 推出正增长“并非独立证明”。

分类：`CIRCULARITY / MISSING_COMPLEX_ZERO_CONTROL`.

### 有效但不足的支路

- TP2 / strict log-concavity：即使成立，也只是必要条件；
- 有限 \(d,n,r\) interval certificates：`COMPUTATIONAL_FACT / EVIDENCE_ONLY`;
- 这些节点不能推出 `TP∞`。

---

## C. Yamaguchi Gram Jacobi / spectral determinant route

```text
RH
↑
zeros of F(z)=xi(1/2+iz) equal real spectrum of self-adjoint J∞
↑
D_N(z) / F(z) → c != 0 locally uniformly
↑
trace / logarithmic-derivative convergence
↑
Hadamard product representation
```

致命 circularity 出现在 Hadamard-rigidity 证明内部。论文写：

\[
\xi(1/2+iz)
=
\xi(0)\prod_k(1-z^2/\gamma_k^2)
\]

并解释为“pairing zeros at \(1/2\pm i\gamma_k\)”。

但在不假设 RH 时，若
\(\rho=\beta+i\gamma\) 是非平凡零点，则 \(F(z)=\xi(1/2+iz)\) 的对应零点为

\[
z=\gamma-i(\beta-1/2),
\]

一般是复数；不能先写成全部实数 \(\pm\gamma_k\)。

因此该 factorization 已把 RH 作为零点参数化假定进去。之后

\[
F'/F=\sum_k \frac{2z}{z^2-\gamma_k^2}
\]

重复同一假定；“分子分母在 poles 处同阶消失，因为 limit zero sets coincide”又再次使用目标结论。

分类：`EQUIVALENT_TO_RH / CIRCULARITY`.

---

## D. CIPHER/RTSG negative control

```text
historical claimed functional bridge
↑
B* K + K(B-1)=0
```

公开 adversarial archive 的结论：

```text
at zeta zeros, bridge reduces via functional equation to 1 = 1
```

所以它不提供 spectral confinement。

分类：
- historical bridge: `CANDIDATE_LEMMA`
- adversarial diagnosis: `NEGATIVE_CONTROL_PASS`.

本 verifier 也独立把这种结构判为 tautological/circular，因此负控校准通过。

---

## DAG 总结

当前 DAG 没有任何从标准前提到 RH 的闭合路径。

最强 Claude-specific Candidate A 在 source level 就把 RH 标成 OPEN；  
最强 full-claim-with-Claude-assistance Candidate B 在 Lemma 10 有明确 FALSE_LEMMA；  
fallback Candidate C 在 determinant bridge 内直接循环假定 critical-line zero parameterization；  
negative control D 被正确判 FAIL。

机器版见 `PROOF_DAG.json`。
