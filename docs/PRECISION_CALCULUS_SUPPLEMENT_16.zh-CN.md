# P018 —— 有限精度证明演算：补充 16

状态：`ACTIVE RESEARCH NOTE`  
范围：带标签扩展 merger time、kernel filtration 精确重建、高阶子集首次合流时间、P011 时间谱重建，以及与 P012 图几何的边界  
依赖：P010、P011、P012、P018-T129—T142、P020  
前人工作边界：hierarchy / dendrogram / ultrametric 的一般等价属于成熟数学，见 `docs/PRIOR_ART_P018_COALESCENCE.zh-CN.md`。本文研究的是进取数论 deterministic finite 接口，不主张一般 hierarchy-ultrametric 对应本身为原创。

---

## 1. 下一步为什么应该减少底层，而不是继续增加对象

Supplement 15 留下了三个时间分辨对象：

- 带标签 kernel filtration，记录**谁**发生合流；
- pairwise 首次合流时间 `tau`，记录一对历史**什么时候**第一次合流；
- P011 逐步 collision polynomial，记录每一阶**有多少**新合流子集。

一个自然但危险的下一步，是给每个 triple、quadruple 乃至更高有限集合再引入独立的首次合流时间对象。

更正确的问题应当是：

> deterministic pairwise merger time 是否已经决定所有高阶 common-fiber 事件？

答案是肯定的。

---

## 2. 带标签扩展 merger time

对确定性 endomap

\[
F:X\to X,
\]

定义

\[
\boxed{
\bar\tau_F(x,y)
=
\begin{cases}
\min\{n:F^{[n]}x=F^{[n]}y\},&\text{若这样的 }n\text{ 存在},\\
\infty,&\text{否则}.
\end{cases}}
\]

这里加上横线，是为了与 Supplement 14 只定义在单个 eventual-coalescence class 上的有限 `tau` 区分。

这是一个**带标签**对象：数值必须继续附着在具体 state pair `(x,y)` 上。擦掉标签会丢失信息。

---

## 3. P018-T143 —— 有限子集的首次共同合流时间等于最大 pairwise merger time

状态：`PROVED / EXECUTABLE`

设 `A` 是同一个 eventual-coalescence class 内的有限非空子集。定义其首次 common-fiber 时间：

\[
\tau_F(A)
=
\min\{n:\ F^{[n]}x=F^{[n]}y\ \text{对所有 }x,y\in A\}.
\]

对 singleton 定义 `tau_F(A)=0`。

则

\[
\boxed{
\tau_F(A)
=
\max_{\{x,y\}\subseteq A}\tau_F(x,y).
}
\]

### 证明

记所有 pairwise merger time 的最大值为 `N`。

在时间 `N`，`A` 中每一对历史都已经合流，因为 equality 一旦出现，在任何更晚的共同 deterministic suffix 下都继续保持。因此 `A` 中所有元素在第 `N` 步的 image 相同，所以

\[
\tau_F(A)\le N.
\]

反过来，如果 `A` 在时间 `n` 已经全部位于同一 fiber，则 `A` 中任意 pair 在时间 `n` 也位于同一 fiber，所以每一个 pairwise 首次合流时间都不超过 `n`。因此

\[
N\le\tau_F(A).
\]

两边合并得到等号。∎

### 后果

在 deterministic dynamics 下，不存在独立的高阶 first-merger-time 信息：

\[
\boxed{
\text{所有有限子集 merger time 都由 pairwise merger time 决定。}
}
\]

这是一个底层最小化结果，而不是再创造新 primitive 的理由。

---

## 4. P018-T144 —— 对 merger time 做阈值化可精确重建每个 kernel level

状态：`PROVED / EXECUTABLE`

回忆

\[
K_n=\kerpair(F^{[n]}).
\]

由 first merger time 的定义以及 equality 的后续保持性，严格有

\[
\boxed{
(x,y)\in K_n
\iff
\bar\tau_F(x,y)\le n.
}
\]

其中 `infinity <= n` 约定为 false。

因此，一个带标签扩展 merger-time 对象通过阈值化即可恢复每个有限时间的 kernel relation。

同样：

\[
\boxed{
(x,y)\in K_\infty
\iff
\bar\tau_F(x,y)<\infty,
}
\]

其中 `K_infinity` 表示 eventual coalescence relation。

---

## 5. P018-T145 —— 带标签 merger-time matrix 与完整 kernel filtration 无损等价

状态：`PROVED STRUCTURAL EQUIVALENCE`

T144 已经说明可以由 `bar tau` 重建整条递增关系族

\[
K_0\subseteq K_1\subseteq\cdots.
\]

反过来，若已知带标签 kernel filtration，则可恢复

\[
\boxed{
\bar\tau_F(x,y)
=
\min\{n:(x,y)\in K_n\}
}
\]

若该集合为空，则定义为 `infinity`。

所以

\[
\boxed{
\text{labelled kernel filtration}
\quad\longleftrightarrow\quad
\text{labelled extended pairwise merger-time matrix}
}
\]

只是两种无损表示。

这**不**意味着 `bar tau` 在本体上比 Pair/kernel 更原始。Pair/kernel 仍然是无减法的静态关系层；`bar tau` 是把整条时间 filtration 压缩成一个带标签时间坐标对象。

---

## 6. P018-T146 —— 所谓带标签高阶 time complex 不包含新的 deterministic 时间信息

状态：`PROVED NEGATIVE / MINIMALITY RESULT`

假设试图为每个有限非空子集 `A` 单独保存 first common-fiber time `tau_F(A)`。

T143 给出

\[
\boxed{
\tau_F(A)
=
\operatorname{diam}_{\bar\tau_F}(A)
:=
\max_{x,y\in A}\bar\tau_F(x,y)
}
\]

当 `A` 跨越不同 eventual-coalescence components 时，该值就是 `infinity`。

因此整个 labelled higher-order merger-time complex 都只是 pairwise matrix 的确定函数。

所以 P018-Q109 在底层最小化意义上得到一个否定性解决：

> deterministic common-fiber history 不需要独立的高阶 time object；带标签 pairwise merger time 已经足够。

高阶**计数**仍然有价值，但它不是新的 merger-time ontology。

---

## 7. P018-T147 —— P011 的 degree-k collision 数等于子集 merger time 的阈值计数

状态：`PROVED / EXECUTABLE`

固定有限带标签 observation set `H`。在时间 `n`，一个 `k` 元子集 `A` 对 P011 的 `J_k(F^[n]|_H)` 有贡献，当且仅当 `A` 的全部历史都位于 `F^[n]` 的同一 fiber。

由 T143–T144，这严格等价于

\[
\tau_F(A)\le n.
\]

因此

\[
\boxed{
J_k(F^{[n]}|_H)
=
\#\{A\subseteq H:|A|=k,\ \tau_F(A)\le n\}.
}
\]

取相邻两个时间之差，就得到精确 first-merger distribution：

\[
\boxed{
[t^k]\Delta_n(t)
=
\#\{A\subseteq H:|A|=k,\ \tau_F(A)=n\}.
}
\]

因此 P018-Q110 对所有有限 `k` 都得到解决，而不仅是 pair。

当 `k=2` 时，它退化为 pairwise `tau=n` 的带标签 unordered pair 数量。

---

## 8. P018-T148 —— 带标签 pairwise merger-time matrix 可重建完整时间分辨 P011 spectrum

状态：`PROVED SYNTHESIS / EXECUTABLE`

由 T143，每个 subset time 都是其 pairwise entries 的最大值。由 T147，P011 的每一阶系数都是“最大 pairwise entry 不超过某时间阈值”的子集计数。

因此，在有限带标签 observation set `H` 上，矩阵

\[
\boxed{
(\bar\tau_F(x,y))_{x,y\in H}
}
\]

可以重建：

1. 每一个 finite-time kernel partition；
2. 每一个有限 subset 的 first-merger time；
3. 每一个时间的全部 `J_k`；
4. 每一个 step increment polynomial `Delta_n(t)`；
5. 在 P020 finite saturation 成立时的最终 stabilization collision spectrum。

所以此前

`kernel = who; tau = when; Delta K = how many`

可以进一步精炼为：

- 完整的**带标签时间结构**在 pairwise `bar tau` 层已经足够；
- kernel filtration 是它的阈值表示；
- P011 spectrum 是从它派生出来的整数聚合 observable。

---

## 9. P018-C12 —— collision-spectrum trajectory 不能反向恢复 labelled merger time

状态：`COUNTEREXAMPLE / INFORMATION BOUNDARY`

取带标签有限状态集

\[
H=\{0,1,2,3\}.
\]

考虑两个确定性映射：

\[
F(1)=0,
\quad F(0)=0,
\quad F(2)=2,
\quad F(3)=3,
\]

以及

\[
G(2)=0,
\quad G(0)=0,
\quad G(1)=1,
\quad G(3)=3.
\]

一步之后，两者的 fiber-size multiset 都是

\[
\{2,1,1\},
\]

并且此后保持固定。因此它们完整的 P011 collision-polynomial 时间轨迹完全相同。

但是 labelled first-merger matrix 不同：

- 对 `F`，pair `{0,1}` 在时间 `1` 合流，而 `{0,2}` 永不合流；
- 对 `G`，pair `{0,2}` 在时间 `1` 合流，而 `{0,1}` 永不合流。

因此

\[
\boxed{
\text{time-resolved collision spectra 不能恢复 labelled merger history。}
}
\]

这就是为什么 aggregate P011 polynomial 不能取代 Pair/kernel 层。

---

## 10. P018-T149 —— 全局扩展 merger time 是 extended ultrametric

状态：`PROVED / ESTABLISHED HIERARCHICAL PATTERN`

允许取值 `infinity`。则在整个状态集上：

\[
\bar\tau_F(x,x)=0,
\qquad
\bar\tau_F(x,y)=\bar\tau_F(y,x),
\]

并且

\[
\boxed{
\bar\tau_F(x,z)
\le
\max(\bar\tau_F(x,y),\bar\tau_F(y,z)).
}
\]

其中每个有限整数都小于 `infinity`。

若右边两项都是有限值，Supplement 14 T130 已证明该不等式；若任意一项为 `infinity`，不等式自动成立。

所以一个 deterministic many-to-one history 自己就能产生带标签的**扩展整数 ultrametric**，而无需预先假定一个 metric background。

在 P020 条件下，T132 又把其有限距离 components 精确识别为 canonical stabilization map 的 fibers。

一般 hierarchy/ultrametric 对应属于成熟前人工作，本文不主张该抽象现象为进取数论原创。

---

## 11. P018-C13 —— P012 primitive graph distance 与 merger-time ultrametric 是不同结构

状态：`COUNTEREXAMPLE / DESIGN BOUNDARY`

取自然坐标上的一般确定性 endomap

\[
F(n)=n//2,
\]

并只为比较取普通 nearest-neighbor graph distance

\[
d_G(x,y)=|x-y|.
\]

则

\[
d_G(8,9)=d_G(7,8)=1,
\]

但

\[
\tau_F(8,9)=1,
\qquad
\tau_F(7,8)=4.
\]

所以相同 graph distance 不推出相同 merger time。

进一步：

\[
d_G(7,8)=1<7=d_G(0,7),
\]

却有

\[
\tau_F(7,8)=4>3=\tau_F(0,7).
\]

因此两种距离连最直观的单调次序关系在一般情况下也不成立。

重要类型警告：这里重复使用 `n -> n//2` 只是把它当作一般 deterministic endomap 构造反例，**不是**把同一个 P005 typed scale-projection arrow 反复作用；P009 的 type-erasure 警告继续完整有效。

所以 P012 graph distance 与 coalescence ultrametric 必须继续保留为两条不同几何路线，除非未来在额外假设下证明明确 compatibility theorem。

---

## 12. 对底层逻辑的反哺

时间/不可逆性层现在可以在不损失带标签 deterministic 信息的情况下进一步压缩：

\[
\boxed{
\text{typed State + deterministic evolution}
\to
\text{Pair/kernel filtration}
\longleftrightarrow
\text{labelled extended merger-time matrix}
\to
\text{higher collision spectra}.
}
\]

中间两个对象角色不同：

- kernel filtration 的前提更弱，直接保留 relational meaning；
- `bar tau` 把整条时间 filtration 压缩为一个带标签 integer/infinity 坐标对象。

P011 statistics 是下游聚合，因此不能反过来代替 labelled layer。

这是一次 primitive 的减少：deterministic higher-order merger time 不需要另设独立底层结构。

---

## 13. 可执行压力测试

新增：

- `src/enterprise_math/merge_time_complex.py`
- `tests/test_merge_time_complex.py`

压力测试包括：

1. finite subset 首次共同合流时间等于最大 pairwise merger time；
2. 对 labelled pair times 做 threshold 精确重建每个被测试的 kernel level；
3. degree-`k` collision increment 等于 first common time 正好等于该 step 的 labelled `k`-subset 数量；
4. higher subset time 不增加超出 pair times 的新信息；
5. 相同 graph distance 可以拥有不同 coalescence time；
6. graph distance 与 merger time 不满足最直观的单调关系；
7. 完全相同的 time-resolved collision spectra 可以隐藏不同 labelled merger histories。

---

## 14. 下一步开放问题

### P018-Q112 —— labelled merger time 在 precision atlas 下是否不变

当两个合法 mixed-radix charts 表示同一个 underlying precision fiber 时，确定它们诱导的 labelled kernel filtration 与 merger-time matrix 在什么条件下 conjugate / invariant。

### P018-Q113 —— operation scheduling 与 merger-time geometry

Supplement 13 已说明 local defects 可以在 outer endpoint 上精确抵消。研究这种 cancellation 如何重新排列 pairwise first-merger times，以及哪些性质在 chart change 下保持。

### P018-Q114 —— P017 certificate filtration

检验 P017 的 local-support information 能否被组织成有限 filtration，并定义 first certificate-validity time；前提是完整保留现有 Legendre 各条路线，并禁止把 proof-state aggregation 与 physical irreversibility 直接等同。

### P018-Q115 —— nondeterministic boundary

对 relation / correspondence，pair 一次相遇后可能沿不同 branch 再次分开。研究 kernel/merger-time compression 的哪一部分还能保留，哪一部分必须重建。

---

## 15. 当前结论

对 deterministic evolution，带标签 pairwise extended merger-time 对象已经对整个 time-dependent indistinguishability structure 完备：

\[
\boxed{
K_n
=
\{(x,y):\bar\tau_F(x,y)\le n\}.
}
\]

每个有限高阶 common-fiber time 都是其 pairwise diameter；在有限 observation 上：

\[
\boxed{
[t^k]\Delta_n(t)
=
\#\{A\subseteq H:|A|=k,\ \tau_F(A)=n\}.
}
\]

因此 deterministic irreversibility 不需要分别为 pair merger、高阶 merger time、collision spectrum 设置彼此独立的 primitive。带标签 Pair/kernel history 是基础；extended merger time 是其无损时间坐标；P011 spectrum 是同一结构的有限整数摘要。
