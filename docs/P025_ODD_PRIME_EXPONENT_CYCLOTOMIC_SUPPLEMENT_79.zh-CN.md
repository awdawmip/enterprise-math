# P025 补充 79 —— 奇素数指数的分圆压力与同余精度

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 72、76–78  
硬阻断：`NONE`

## 1. 立方机制并非指数三的特例

设

\[
\ell\ge3
\]

为奇素数，并设

\[
p>q\ge3
\]

为不同的奇素数。对于 complements 为

\[
p^\ell,\ q^\ell
\]

的同指数 low-capacity atom，Stage 72 的精确 denominator 为

\[
\ell(p+q).
\]

因此 sum / difference 两个 projective atom 为

\[
\boxed{
\rho_{\ell,+}
=\frac{m(p^\ell+q^\ell)}{\ell(p+q)},
\qquad
\rho_{\ell,-}
=\frac{m(p^\ell-q^\ell)}{\ell(p+q)}.
}
\]

当 `ell=3` 时，这正是 Stage 75–78 已研究的 cube atoms。

## 2. 非线性分圆因子

由于 `ell` 是奇素数，

\[
p^\ell-q^\ell=(p-q)\Phi_\ell(p,q),
\]

以及

\[
p^\ell+q^\ell=(p+q)\Phi_{2\ell}(p,q).
\]

记

\[
L_-=p-q,
\qquad
F_-=\Phi_\ell(p,q),
\]

以及

\[
L_+=p+q,
\qquad
F_+=\Phi_{2\ell}(p,q).
\]

`L_+`、`L_-` 都是偶数，而两个非线性分圆因子都是奇数。

标准的素数指数分圆 gcd 恒等式给出

\[
\gcd(L_\pm,F_\pm)\in\{1,\ell\}.
\]

如果 `ell` 出现在非线性因子中，普通 LTE 给出其 valuation 恰为 1。因此例外素数 `ell` 可以和线性因子重叠，却永远不能为非线性 multiplicity residual 提供重复度。

## 3. P025-T154 —— residual 的精确重组

令

\[
g_\pm:=\gcd(L_\pm,\ell)\in\{1,\ell\}.
\]

因为 `L_±` 与 `F_±` 的公共 support 至多只有这个一次出现的素数 `ell`，multiplicity residual 精确重组为

\[
\boxed{
m(p^\ell\pm q^\ell)
=g_\pm\,m(L_\pm)\,m(F_\pm).
}
\]

从而

\[
\boxed{
\rho_{\ell,\pm}
=
\frac{g_\pm m(L_\pm)m(F_\pm)}{\ell(p+q)}.
}
\]

这是指数三 centered residual 分解在任意奇素数指数上的对应形式。

## 4. P025-T155 —— threshold-one activation 强迫非线性分圆重复

先假设 `F_±` squarefree，则

\[
m(F_\pm)=1.
\]

因为 `L_±` 是偶数，

\[
m(L_\pm)=\frac{L_\pm}{\operatorname{rad}(L_\pm)}
\le \frac{L_\pm}{2}.
\]

又有 `g_±<=ell`。因此 sum branch 满足

\[
\rho_{\ell,+}
\le
\frac{\ell (p+q)/2}{\ell(p+q)}
=\frac12.
\]

对于 difference branch，因为 `p-q<p+q`，甚至有

\[
\rho_{\ell,-}<\frac12.
\]

所以

\[
\boxed{
\rho_{\ell,\pm}\ge1
\Longrightarrow
F_\pm\text{ 必为 nonsquarefree}.
}
\]

因此每一个被激活的奇素数同指数 atom，都必须在**非线性**分圆因子中包含重复 multiplicity。单靠线性因子永远无法承载 hard state。

这也强化了 Stage 76 对 cube-difference branch 的原始表述：在 threshold one 下，那里同样必然需要非线性重复。

## 5. P025-T156 —— repeated primes 必为 `1 mod 2ell`

设 `r` 是 `F_-` 或 `F_+` 的 repeated prime divisor。

例外素数 `ell` 不能重复，所以 `r!=ell`，且 `r` 与 `pq` 互素。令

\[
x=pq^{-1}\pmod r.
\]

对于 `F_-`，`x` 的精确阶为 `ell`；对于 `F_+`，其精确阶为 `2ell`。因为 `r` 为奇素数，两种情形都得到

\[
\boxed{2\ell\mid r-1}.
\]

因此

\[
\boxed{r\equiv1\pmod{2\ell}.}
\]

特别地，每个 repeated cyclotomic prime 都满足

\[
r\ge2\ell+1.
\]

当 `ell=3` 时，这正好恢复 Stage 76 的 `r=1 mod 6` support law。

## 6. P025-T157 —— 局部 root class 数为 `ell-1`

固定 repeated prime power

\[
r^e\mid F_\pm,
\qquad e\ge2.
\]

模 `r` 时，difference branch 的允许 ratio 是 primitive `ell`th roots；sum branch 则是 primitive `2ell`th roots。两者数量均为

\[
\varphi(\ell)=\varphi(2\ell)=\ell-1.
\]

由于 `r` 不整除 `ell`，这些 roots 都是 simple roots，并且每一个都唯一 Hensel lift 到任意 `r^e`。因此 full repeated prime power 上的局部 ratio state 恰有

\[
\boxed{\ell-1}
\]

个 residue classes。

若 repeated support 含 `k` 个不同素数，full repeated modulus 为

\[
M=\prod_{i=1}^k r_i^{e_i},
\]

则 CRT 给出恰好

\[
\boxed{(\ell-1)^k}
\]

个允许的 labelled ratio classes modulo `M`。

Stage 77 的二叉 `2^k` state 因而正是 `ell=3` 的特化。

## 7. P025-T158 —— projective pressure 强迫 congruence precision

假设

\[
\rho_{\ell,\pm}\ge T,
\qquad T\ge1.
\]

由精确 residual 公式，

\[
m(F_\pm)
\ge
\frac{T\ell(p+q)}{g_\pm m(L_\pm)}.
\]

由于 `g_±<=ell` 且 `L_±` 为偶数，sum branch 得到统一下界

\[
\boxed{m(F_\pm)\ge2T},
\]

而 difference branch 得到严格下界

\[
\boxed{m(F_-) > 2T}.
\]

特别地，`k>=1`。

令

\[
R_{\rm rep}=\prod_{i=1}^k r_i.
\]

因为

\[
m(F_\pm)=\frac{M}{R_{\rm rep}}
\]

且每个 repeated `r_i>=2ell+1`，所以

\[
\boxed{
M
\ge
(2\ell+1)^k m(F_\pm)
\ge
2T(2\ell+1)^k
}
\]

（difference branch 保留严格性）。

于是 modulo `M` 的允许 ratio class 密度满足

\[
\boxed{
\frac{(\ell-1)^k}{M}
\le
\frac1{m(F_\pm)}
\left(\frac{\ell-1}{2\ell+1}\right)^k
\le
\frac1{2T}
\left(\frac{\ell-1}{2\ell+1}\right)^k.
}
\]

这就是 Stage 79 的核心 pressure / precision law：

> projective pressure 越大，就自动强迫越高的同余精度；并且每增加一个独立 repeated cyclotomic prime，允许的 ratio 密度至少再乘一个 `(ell-1)/(2ell+1)`。

## 8. 超越立方的精确校准

### 五次幂 sum

取

\[
(q,p)=(37,59),
\qquad \ell=5,
\]

有

\[
\rho_{5,+}=\frac{31}{30}>1,
\]

并且

\[
\Phi_{10}(59,37)=31^2\cdot8501.
\]

重复素数满足

\[
31\equiv1\pmod{10},
\]

且 modulo `31^2` 恰有

\[
5-1=4
\]

个局部 ratio classes。

### 五次幂 difference

取

\[
(q,p)=(19,29),
\qquad \ell=5,
\]

则

\[
\rho_{5,-}=\frac{121}{48}>1,
\]

且

\[
\Phi_5(29,19)=5\cdot11^3\cdot271.
\]

例外素数 5 只出现一次；真正 repeated prime 为

\[
11\equiv1\pmod{10}.
\]

### 七次幂

当 `ell=7` 时，精确 activated examples 出现 repeated prime

\[
29\equiv1\pmod{14},
\]

局部 root classes 数为 6，与一般定理完全一致。

## 9. 架构含义

Stage 72 与 76–78 找到的序列是

\[
\text{exponent shell}
\to
\text{cyclotomic support}
\to
\text{root-of-unity congruence state}.
\]

Stage 79 证明这不是 cube-specific trick。对每个奇素数指数，future query“这个 equal-exponent atom 是否发生 projective activation？”都会强迫一种 theorem-native congruence precision；其 branching 与 modulus growth 都由指数显式决定：

\[
\boxed{
\text{local branching}=\ell-1,
\qquad
\text{repeated-prime modulus}\ge(2\ell+1)^2.
}
\]

每个 repeated prime 的净 modulus-per-class compression 至少为

\[
\boxed{
\frac{(2\ell+1)^2}{\ell-1}.
}
\]

当 `ell=3` 时就是 `49/2`，恰好是 Stage 78。

因此随着指数增大，局部 residue branch 数确实变多，但被强迫的 modulus 增长更快；净 congruence state 反而更具选择性，而不是更粗。

## 10. Prior-art / novelty 边界

分圆分解、gcd 恒等式、LTE、乘法阶、Euler phi 计数、Hensel lifting 与 CRT 都是经典前人数学。

P025 **不**主张这些组成部分的新颖性。项目侧候选贡献只是：把这些已知工具与精确 projective low-capacity atom 组合成上述 pressure-to-congruence-precision law。历史新颖性仍标记为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/abc_odd_prime_exponent_cyclotomic.py`；
- `tests/test_abc_odd_prime_exponent_cyclotomic.py`。

可执行层对 `ell=3,5,7` fixtures 检查 exact residual recomposition、例外素数 valuation 边界、`1 mod 2ell` repeated support、observed root order、CRT class count，以及 pressure 驱动的 modulus / density 不等式。

## 12. 下一前沿

不存在硬阻断。继续：

1. 把 Stage 78 的 finite incidence envelope 与 Stage 79 的 threshold-dependent `M` 下界直接合成；
2. 判断对所有可能 repeated moduli 求和后，接近 `1/T` 的 pressure tail 是否仍能保留，还是会被 signature multiplicity 吃掉；
3. 与偶指数四比较：difference branch 在 nonlinear factor squarefree 时仍可能由 centered linear-factor multiplicity 激活；
4. 只有在把 cyclotomic-specific arithmetic 压成最小抽象命题后，才把 pressure-to-precision law 回流 A2/P023。
