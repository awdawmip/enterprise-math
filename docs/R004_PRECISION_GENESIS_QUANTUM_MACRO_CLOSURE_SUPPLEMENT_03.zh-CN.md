# R004 精度宇宙生成 —— Supplement 03：sharp finite measurement-dependence cost

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART SPECIALIZATION`  
Parent：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_02.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

Supplement 02 已证明：locality + measurement-setting independence 会阻止当前选定的 exact rational Bell target。本补充继续量化剩余逃逸路线：

> 如果继续保留 locality，但允许 latent seed distribution 随 joint setting pair 改变，那么为了复现这个 target，最少需要多少 setting dependence？

在下文明确给定的 max-total-variation normalization 下，答案精确为 `2/15`。

## 1. Setting-dependent local completion

继续使用十六个 deterministic local response tables

\[
\lambda=(A_0,A_1,B_0,B_1),
\qquad A_x,B_y\in\{-1,+1\}.
\]

现在允许每个 joint setting

\[
s\in\{00,01,10,11\}
\]

使用不同 latent distribution `mu_s`。

Response functions 仍然 setting-local；改变的只有 seed distribution 可以随 setting pair 变化。

定义 setting-dependence size

\[
\boxed{
M=\max_{s,t}\operatorname{TV}(\mu_s,\mu_t)
}
\]

其中 total variation 为

\[
\operatorname{TV}(p,q)=\frac12\sum_\lambda|p(\lambda)-q(\lambda)|.
\]

必须明确写出 normalization，因为 measurement-dependence 文献中存在多种相近约定。在 Bell model 中通过放松 measurement independence 保留 local deterministic response functions，本身已经是成熟先行工作 [SRC-HALL-2010-MEASUREMENT-INDEPENDENCE]。

## 2. Relaxed CHSH inequality

取 `mu_00` 作为 reference distribution。如果四个 correlations 全都用这一组 distribution 计算，普通 local CHSH 的绝对值不超过 `2`。

对任意 binary function `f(lambda) in {-1,+1}`，

\[
|E_p f-E_q f|
\le
\sum_\lambda |p(\lambda)-q(\lambda)|
=2\operatorname{TV}(p,q).
\]

实际 CHSH expression 与 `mu_00` reference expression 只在另外三个 setting terms 上不同；每一项最多变化 `2M`。因此

\[
\boxed{|S|\le2+6M.}
\]

### Integer form

若每个 setting distribution 都用总 weight 相同的非负整数 weights 表示，公共 total 为 `W`，并定义

\[
D=\max_{s,t}\sum_\lambda|w_s(\lambda)-w_t(\lambda)|,
\]

则

\[
M=\frac{D}{2W}
\]

且 relaxed inequality 精确变为

\[
\boxed{|N_{\mathrm{CHSH}}|\le2W+3D.}
\]

定理陈述和证明都不需要 floating-point optimization。

## 3. Rational singlet target 的 lower bound

Supplement 02 的 exact rational target 满足

\[
|S|=14/5.
\]

代入 relaxed inequality：

\[
14/5\le2+6M.
\]

所以

\[
6M\ge4/5
\]

进而

\[
\boxed{M\ge2/15.}
\]

因此，在这个 normalization 下，一个 setting-local pre-sampled model 不可能只靠“任意小”的 measurement-independence violation 恢复当前 target。

## 4. Exact denominator-60 witness：lower bound 是 sharp 的

R004 同时给出一个精确达到 equality 的 local completion。

按 `(A_0,A_1,B_0,B_1) in {-1,+1}^4` 的 lexicographic 顺序编号十六个 deterministic tables。只有 indices `2,3,5,7,8,10,12,13` 的 weight 非零。四组 equal-total rows 在这些 indices 上分别为：

- `00`：`(10,7,6,7,7,6,7,10)`；
- `01`：`(6,7,10,7,7,10,7,6)`；
- `10`：`(10,7,10,3,3,10,7,10)`；
- `11`：`(10,3,10,7,7,10,3,10)`。

每一行总 weight 都是

\[
W=60.
\]

任意两组 setting rows 的 L1 distance 都恰好为

\[
D=16,
\]

所以

\[
\operatorname{TV}=\frac{16}{120}=\frac{2}{15}.
\]

在对应 setting 上计算 local response 后，四张 observed joint-count tables 精确等于 Supplement 02 的 twenty-atom target 的 3 倍。因此得到同一个 observable target，并且

\[
|N_{\mathrm{CHSH}}|=168
=2\cdot60+3\cdot16.
\]

所以 relaxed inequality 与 measurement-dependence lower bound 同时饱和：

\[
\boxed{M_{\min}=2/15.}
\]

数值 linear program 只用于发现候选 witness，不进入证明。仓库里保存的是上述 explicit integer witness；正式验证只需要有限整数求和。

## 5. Operational no-signalling 严格弱于 local latent factorization

Twenty-atom rational target 的 marginals 完全 balanced。对每个固定 Alice setting `x`，她的 outcome counts 都是 `10/10`，且与 Bob 的 setting `y` 无关；Bob 也同样对固定 `y` 得到与 `x` 无关的 `10/10` marginals。

因此这个 finite target 在 observable 层是 exact **no-signalling**。

但与此同时，`|S|=14/5>2` 又证明不存在 setting-independent local latent decomposition。

于是 R004 得到一个 exact finite separation：

\[
\boxed{
\text{observable no-signalling}
\not\Rightarrow
\text{Bell-local latent factorization}.
}
\]

这对 geometry route 很重要。未来的 finite causal / space model 不能把“没有可控 signal 穿过 bridge”直接等同于 Bell locality 所需的更强 hidden-variable factorization。两者是不同 interface，必须分层表示。

## 6. 更新后的 generative-identifiability ladder

当前 finite hierarchy 变成：

1. arbitrary pre-sampling 可以穿过 deterministic towers；
2. arbitrary pre-sampling 可以穿过 finite rational stochastic kernels；
3. arbitrary pre-sampling 可以穿过 finite adaptive interventions；
4. setting-local + setting-independent pre-sampling 在 rational Bell target 上失败；
5. 保留 locality、放松 setting independence 后，只有付出 exact target-specific price `M=2/15` 才能恢复 completion；
6. 上述结果仍然没有排除 genuinely nonlocal completion 或其他 ontology change。

因此研究问题又进一步收紧。现在不再只是“还有没有 loophole”，而是：

> Enterprise Math 自己能够推导哪些 causal restrictions？违反每一条 restriction 的 quantitative resource cost 是多少？哪些 restriction 能被独立物理实验直接压力测试？

这已经比把“new information was created”当作无法解释的 ontological sentence 更接近一个可证伪研究程序。
