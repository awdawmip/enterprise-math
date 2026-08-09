# Causal Recursive Dimension Generator —— 最小 Continuation State、二体 Coherence 与任意维生成

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE THEOREMS + EXECUTABLE REFERENCES`

归属：当前推导源位于 A3 `research/core/relation-quotient`。一般 future-equivalence / quotient 母理论仍归 A2/P023；carry/scale corollary 应回流 P018；geometry corollary 应回流 P012/P022。

本文纠正一个容易过早下结论的问题：

> pairwise coupling 全部正常、三体 joint state 仍失败，并不自动证明存在“绝对三体 primitive”。

固定有限维时，任何规则都可以通过保存足够多 prefix history 被顺序局部化。真正有意义的问题是：**为了让同一个低维 causal law 生成任意维，最小 continuation state 需要多复杂，以及二体 join 是否在该 state 上严格 coherent。**

## 1. Typed binary join kernel

令 `T` 为已经按完整剩余 future signature 压缩后的 continuation-type 集。

定义整数二体 join kernel：

\[
\boxed{
K(\alpha,\beta;\nu,\delta)\in\mathbb N_0.
}
\]

语义：一个 `alpha` witness 与一个 `beta` witness 拼接后，产生多少个 continuation type 为 `nu`、额外 integer grade shift 为 `delta` 的 joint witnesses。

这不是 tensor/matrix 的先验坐标。`K=0` 表示该 typed pairing 不存在，`K=1` 表示唯一 typed outcome，更大整数表示同 typed outcome 上有多个 joint causal states。

对 type-grade inventory `F,G`，composition 由直接 witness counting 给出：

\[
(F\star G)(\nu,E)
=
\sum_{\alpha,\beta,E_1,E_2,\delta}
F(\alpha,E_1)G(\beta,E_2)
K(\alpha,\beta;\nu,\delta)
\mathbf1[E=E_1+E_2+\delta].
\]

## 2. CRD-01 —— exact associativity / 三体 compatibility gate

三个 singleton types `a,b,c` 有两种 binary bracketing。

左括号：

\[
L_{abc}^{\nu,d}
=
\sum_{\mu,d_1+d_2=d}
K(a,b;\mu,d_1)K(\mu,c;\nu,d_2).
\]

右括号：

\[
R_{abc}^{\nu,d}
=
\sum_{\mu,d_1+d_2=d}
K(b,c;\mu,d_1)K(a,\mu;\nu,d_2).
\]

二体 law 能无歧义递归生成任意维的第一道硬门是：

\[
\boxed{
L_{abc}^{\nu,d}=R_{abc}^{\nu,d}
\quad\forall a,b,c,\nu,d.
}
\]

这里比较 exact `(continuation type, grade)` outcome，不能只比较总 cardinality。

若失败，定义 typed three-body compatibility defect 为逐 outcome 的 positive left-only / right-only multiplicity。左右缺口必须分开保存，避免 signed scalar cancellation。

### 推论

若 inventory composition 在 type kernel 上满足上述结合律，则有限个 factors 的 composition 与 binary parenthesization 无关。因此同一个 typed binary law 可以递归到任意 slot count；不需要另加 `n`-body composition rule。

## 3. 当前 coupling order 不是绝对 primitive arity

旧 causal-independence complex 中 minimal nonface 仍然有效，但其语义必须限定为：

\[
\boxed{
\text{current/exposed state language 下的 factorization-failure order}.
}
\]

它不是“任何 future-safe state enrichment 都无法二体化”的证明。

### parity 最小反例

三个二值 subsystems 只允许：

\[
000,\ 011,\ 101,\ 110.
\]

在 marginal-only language 下，每个 pair 都完全 factor，而 triple 不 factor，所以 exposed coupling order 为 3。

但引入一个不是人为标签、而是 future-relevant accumulated parity continuation type：

\[
\tau\in\{0,1\},
\qquad
\tau_{ab}=a\oplus b,
\]

并使用同一个 binary law：

\[
\tau\star x=\tau\oplus x,
\]

最后只接受 `tau=0`，就对任意维精确生成 even-parity constraint。

所以 parity 的：

- exposed coupling order = 3（对三个 slots）；
- recursive continuation type count = 2；
- absolute ternary primitive claim = false。

这要求以后所有“高阶 interaction/coupling”结论同时报告 state language / continuation complexity。

## 4. CRD-02 —— contextual continuation type 自动编译

普通 continuation type 若只包含“当前之后的内部动作”，仍可能不足以支持任意维 composition。

若 binary LEGO join 本身是允许 future operation，则必须把“与任意 partner 左拼 / 右拼”也纳入 future language。

对有限 raw state set `X` 和 deterministic raw composition `*`，为每个 partner `p` 加 causal actions：

\[
L_p(x)=p*x,
\qquad
R_p(x)=x*p.
\]

从当前 observation partition 开始，按：

\[
\operatorname{sig}_{t+1}(x)
=
\bigl(
\operatorname{obs}(x),
[L_p(x)]_t,
[R_p(x)]_t
\bigr)_{p\in X}
\]

有限细化到稳定。

稳定 class 就是 **contextual continuation type**。

### 定理

若 raw composition 本身 associative，则 contextual stable partition：

1. 是 composition congruence；
2. induced type operation well-defined；
3. induced type operation associative。

所以传统 quotient-monoid 不是基础，而是：

\[
\boxed{
\text{raw associative LEGO composition}
+\text{future contextual indistinguishability}
\to
\text{associative type shadow}.
}
\]

## 5. CRD-03 —— pair grade coherence

考虑 deterministic type join：

\[
a\star b.
\]

每次 binary join 产生 integer grade shift：

\[
\gamma(a,b).
\]

三体总 grade 与 bracketing 无关当且仅当：

\[
\boxed{
\gamma(a,b)+\gamma(a\star b,c)
=
\gamma(b,c)+\gamma(a,b\star c).
}
\]

差值：

\[
D_3(a,b,c)
=
\gamma(a,b)+\gamma(a\star b,c)
-\gamma(b,c)-\gamma(a,b\star c)
\]

是 exact integer three-body grade compatibility defect。

这条式子在传统数学中与 trivial-action 的 additive 2-cocycle 条件同形；在本路线中，coherence 是 causal reason，传统 cocycle 只是 proof/coordinate shadow。

## 6. P018 carry 是 coherent binary grade 的规范例子

base `B>=2`：

\[
a\star_B b=(a+b)\bmod B,
\]

\[
\boxed{
\gamma_B(a,b)=\left\lfloor\frac{a+b}{B}\right\rfloor.
}
\]

则：

\[
\gamma_B(a,b)+\gamma_B(a\star_B b,c)
=
\gamma_B(b,c)+\gamma_B(a,b\star_B c).
\]

原因可以完全在整数层理解：任意已经拼好的 block 始终满足

\[
\boxed{
\text{integer total}
=
\text{residue}+B\times\text{accumulated carry}.
}
\]

所以 carry 是：

> 使局部 residue join 可以 bracket-independently 生成任意多 unit 总量的 pair grade correction。

这给 P018 carry 一个新的 composition interpretation。

## 7. Grade baseline change 与结构 defect

若为每个 continuation type 改写 storage grade baseline：

\[
\tilde g=g+h(\tau),
\]

pair shift 变为：

\[
\boxed{
\gamma'(a,b)
=
\gamma(a,b)+h(a\star b)-h(a)-h(b).
}
\]

三体 compatibility defect `D_3` 不变。

因此“绝对 type grade 起点”可以改变，而 bracket-coherence defect 是更稳定的结构量。

## 8. CRD-04 —— continuation complexity 随维度的增长

固定 alphabet `A`、总 slot 数 `N`、最终 observation `O:A^N->V`。

对长度 `d` prefix `p`，定义它的完整 suffix-response signature：

\[
R_{N,d}(p)
=
\bigl(O(ps)\bigr)_{s\in A^{N-d}}.
\]

令：

\[
C_{N,d}=\#\{R_{N,d}(p):p\in A^d\},
\]

\[
\boxed{C_N=\max_d C_{N,d}.}
\]

`C_N` 是该固定 horizon/task 所需的最少 finite continuation labels 的 class-count complexity。

### 三个边界例子

#### parity

最终只读总 parity：

\[
C_N\le2
\quad\forall N.
\]

所以存在真正 dimension-independent finite-type law。

#### full word identity

最终 observation 保留完整 word：

\[
C_{N,N}=|A|^N.
\]

固定 finite type set 不可能无损承载任意维完整身份。

#### binary integer sum

最终 observation 只读 `sum(bits)`：

\[
C_{N,d}=d+1.
\]

finite label count 随 `N` 增长，但仍存在固定 integer schema：

\[
s' = s+x.
\]

所以必须区分：

- **finite-type uniformity**：`sup_N C_N < infinity`；
- **fixed integer-schema uniformity**：type cardinality 可以增长，但 update law / integer state schema 与 `N` 无关。

后一问题比 finite automaton 更宽，当前仍需继续形式化。

## 9. “绝对 n-body primitive”何时才有意义

若不限制 intermediate causal state 的复杂度，任何固定 finite-horizon joint rule 都可以通过保存足够多 history 顺序局部化。因此绝对 `n`-body primitive 声明本身缺少信息。

更严密的研究对象应至少包含：

\[
\boxed{
(\text{exposed coupling order},\ 
\text{minimal continuation complexity},\ 
\text{join coherence defect}).
}
\]

只有在指定了 state-schema / locality / dimension-uniformity 限制后，才能讨论某个 higher-order law 是否真正不可约。

## 10. 对密堆/FCC/HCP 路线的含义

本文件不声称已推出 FCC/HCP 的真实物理选择。

但它给出一个更合适的研究入口：

- 当前 local packing/contact support 可以相同；
- buried stacking relation 只有在会影响允许 future/observation 时才需要进入 continuation type；
- 绝对 A/B/C registry label 可以是 coordinate shadow；
- 真正要比较的是：最小 continuation state、允许 stacking actions、pair grade/coupling law 是否能 dimension-uniformly 生成完整 stacking family。

所以后续不再先把 FCC/HCP 当两个高维坐标对象硬塞进 core，而先测试其低维 stacking law 是否能通过 causal continuation state 生成。

## 11. 可执行资产

- `causal_recursive_join.py`
- `causal_contextual_join.py`
- `causal_grade_coherence.py`
- `causal_prefix_complexity.py`
- 对应 `tests/test_*`

现有相关资产：

- `causal_continuation_refinement.py`
- `causal_continuation_kernel.py`
- `causal_type_inventory.py`
- `graded_lego_fiber.py`
- `coupled_graded_fiber.py`

## 12. 当前 promotion 边界

以上是 research-branch exact finite/integer derivation + executable reference。完整 clean-integration CI、Lean formalization、prior-art novelty review 仍未完成。

特别地：

- contextual quotient / finite continuation refinement 与 automata/congruence 理论相邻；
- grade coherence equation 与传统 2-cocycle 条件相邻；
- 这些传统理论不作为项目原创主张。

当前项目特有研究问题是：能否用这些被因果生成的 shadows，把 dimension / coupling / carry / geometry 统一到一个 LEGO causal composition core 中。
