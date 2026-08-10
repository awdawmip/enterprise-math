# p-adic 精度对偶：隐藏 FIBER 谱与 IMAGE 可解深度

状态：`RESEARCH BRIDGE / NONCANONICAL`

prime-power observation precision 在仿射正合序列两端形成了一套很清楚的对偶结构。

## 1. FIBER 侧：kernel-growth spectrum

对整数 observation map O，设 hidden free rank 为 h，非零 Smith factors 为 d_i，并记

`a_i=v_p(d_i)`，

`kappa_e=log_p |ker(O mod p^e)|`。

则

`kappa_e=e*h + sum_i min(e,a_i)`。

离散 slope 为

`s_e=kappa_e-kappa_(e-1)=h + #{i:a_i>=e}`，

因此

`s_e-s_(e+1)=#{i:a_i=e}`。

完整的无限 precision-growth curve 可以精确恢复 free hidden rank 与所有正的 p-primary Smith-depth multiplicity。

但只观察到 exponent E 的有限 ladder，无法区分真正 free 的 hidden direction 与深度 `K>=E` 的有限 p^K torsion。两者可以在整个已观测精度范围内拥有完全相同的 kernel-growth curve。

## 2. IMAGE 侧：target 的 p-divisibility height

对 affine target equation

`A x=b`，

定义

`eta_p(b)=sup {e>=0 : A x == b (mod p^e) 可解}`。

它就是 target class `[b]` 在 `coker A` 中的 p-divisibility height。

- exact reachable target：对每个 p 都有 `eta_p=infinity`；
- finite p-primary image obstruction：eta_p 有限；
- prime-to-p 的有限 torsion，即使 exact 不可达，对这个 p 也可能 `eta_p=infinity`；
- free cokernel component 对每个固定 p 的 eta_p 都有限。

有限 solvability ladder 必须是 true-prefix / false-suffix。若到 exponent E 仍未看到 failure，只能推出

`eta_p>=E`，

不能推出 `eta_p=infinity`。

## 3. sharp IMAGE finite-depth mimic

固定 prime p 与深度 K，取同一个 scalar map

`A=p^(K+1)`，

比较 targets

`b_good=p^(K+1)`，

`b_bad=p^(K+1)+p^K`。

第一个 target exact reachable；第二个 exact unreachable。

但对所有 `e<=K`，两组 equation data 在 `p^e` 下完全相同，因此整个 modular solution set 在有限 ladder 内完全一样。只有到 exponent `K+1` 才分开。

## 4. 对偶的有限精度 no-go

现在正合序列两端各有一条平行的 impossibility statement。

### FIBER no-go

有限 p-adic observation ladder 无法证明持续存在的 hidden direction 真的是 free，而不是比当前精度更深的有限 torsion。

### IMAGE no-go

有限 p-adic solvability ladder 无法证明持续可解的 target 真的是 exact reachable，而不是存在比当前精度更深的 image obstruction。

更强的 finite-modulus 版本同样成立：任意有限 modular experiment family 都只有一个 lcm precision ceiling；在这个 ceiling 之外，可以存在 exact integer lifts，在 free/torsion structure 或 exact target reachability 上不同，却通过全部已声明 modular tests。

## 5. 什么条件能让有限实验变成判定性实验？

有限 modular / p-adic evidence 只有在额外加入独立的上界或更强 observation language 后，才能变成决定性的。

例如：

- 已证明所有相关 Smith valuation / torsion depth 都不超过 K；
- 已证明 target-class p-divisibility depth 有上界；
- 能直接访问 exact integer state；
- 新增一个已知超过剩余 obstruction depth 的 modulus/refinement。

若已经有合法的 p-primary depth bound K，那么 precision level `p^(K+1)` 足以排除该轴上所有更深的有限 mimic。

没有这种 bound 时，“目前尚未看到 failure”只是在给所需精度提供下界，不是在证明 infinity 或 exactness。

## 6. precision-world 解释

这只是整数 identifiability 结论，不是关于自然界一定存在 hidden variable 或 obstruction 的形而上主张。

它只说明：

> **在有限 observation precision 下，一个 exact world property 与一个更深的有限近似可以 operationally indistinguishable。要主张 exact reachability 或 genuinely unbounded hidden structure，必须提高精度，或者拥有独立的深度上界。**

这里使用的 Smith normal form、p-adic valuation、cokernel divisibility 与 congruence 都是标准既有数学。项目价值在于把它们组织成 IMAGE/FIBER 的 precision 对偶架构。