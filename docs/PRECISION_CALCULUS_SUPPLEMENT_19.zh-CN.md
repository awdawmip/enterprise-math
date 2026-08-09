# P018 —— 有限精度证明演算：补充 19

状态：`ACTIVE RESEARCH NOTE`  
范围：binary/multi-ary operation congruence、有限 contextual closure、规范最小 exact quotient refinement、最小 detail 大小，以及 P018-Q117 在有限 finitary 情形下的答案  
依赖：P005、P009、P018-T150–T168  
前人工作边界：congruence、quotient algebra、elementary/term-context congruence test、syntactic congruence，以及 equivalence 内最大 congruence 均属于成熟 universal algebra。见 `docs/PRIOR_ART_P018_PREDICTIVE_CLOSURE.zh-CN.md`。[SRC-SLOMINSKI-1974-GREATEST-CONGRUENCE] [SRC-BURRIS-SANKAPPANAVAR-1981-UA] [SRC-CLARK-DAVEY-FREESE-JACKSON-2004-SYNTACTIC]

---

## 1. 从 unary predictive closure 推进到 operation language

Supplement 18 已解决有限 unary 问题。对一个 deterministic endomap

\[
F:X\to X
\]

和 observation

\[
O:X\to Y,
\]

future-observation refinement 会求出 `ker(O)` 内最大的 `F`-compatible equivalence。

P018-C17 明确保留了 multi-ary 情形。binary operation

\[
\mu:X\times X\to X
\]

可能依赖任一输入中的 hidden detail；多个 operations 还会形成“分别研究单个 operation 时看不到”的 **mixed contexts**。

因此真正的一般对象不是某个 generalized carry scalar，而是：对该 precision state 被要求支持的 operation language，求它的 congruence closure。

令

\[
\Sigma=\{\mu_s:X^{k_s}\to X\}_{s\in S}
\]

为有限 state set `X` 上的有限 finitary operation signature，并令

\[
E=\ker(O).
\]

---

## 2. P018-T169 —— Exact multi-ary descent 当且仅当 kernel 是 congruence

状态：`PROVED / EXECUTABLE / PARTIALLY LEAN-FORMALIZED`

对一个 `k`-ary basic operation

\[
\mu:X^k\to X,
\]

以下两条等价：

1. 公式

   \[
   \bar\mu(Ox_1,\ldots,Ox_k)
   :=O(\mu(x_1,\ldots,x_k))
   \]

   在 `O` 的 image 上 well-defined；
2. 只要每一个输入坐标 observationally equal，

   \[
   O(x_i)=O(y_i)\quad(1\le i\le k),
   \]

   输出也 observationally equal：

   \[
   \boxed{
   O(\mu(x_1,\ldots,x_k))
   =
   O(\mu(y_1,\ldots,y_k)).
   }
   \]

也就是

\[
\boxed{E=\ker(O)\text{ 与 }\mu\text{ compatible}.}
\]

若 `O` surjective 到 `Y`，则 `Y` 上的 descended operation 唯一。

对整个 signature `Sigma`，所有 basic operations 都能 exact descent，当且仅当 `E` 是 `Sigma`-congruence。

这是经典 quotient-algebra 数学。P018 得到的精确含义是：

> **一个 precision state 对某个声明的 operation language 是否 autonomous sufficient，恰好取决于它的 precision equivalence 是否是该语言的 congruence。**

当要求 exact operation closure 时，floating tolerance 或 error budget 不能替代这个 well-definedness 条件。

---

## 3. P018-T170 —— 只检查单坐标 elementary translations 就足够

状态：`PROVED / EXECUTABLE / BINARY CORE LEAN-FORMALIZED`

对 `k`-ary operation `mu`，固定除第 `i` 个坐标外的所有输入，得到 elementary one-hole translation：

\[
\tau(z)
=
\mu(a_1,\ldots,a_{i-1},z,a_{i+1},\ldots,a_k).
\]

对 equivalence relation `R`，`mu` 的 full `k`-coordinate compatibility 等价于每个这样的 elementary translation 都保持 `R`。

非平凡方向只需要有限 telescoping。若

\[
x_i\,R\,y_i
\quad\forall i,
\]

逐个替换坐标：

\[
\mu(x_1,\ldots,x_k)
\;R\;
\mu(y_1,x_2,\ldots,x_k)
\;R\;\cdots\;R\;
\mu(y_1,\ldots,y_k).
\]

由 `R` 的 transitivity 得到 full compatibility。

所以在 `X` 和 signature 都有限时，multi-ary congruence 问题可以降成一个有限的 unary one-hole translation family。

---

## 4. P018-T171 —— Contextual closure 是 precision equivalence 内最大的 congruence

状态：`PROVED / CLASSICAL SYNTACTIC-CONGRUENCE SPECIALIZATION`

令 `T_1(Sigma)` 为：所有 basic operations 在任意固定 state parameters 下产生的 elementary one-hole translations。令 `M(Sigma)` 为这些 translations 与 identity 在 composition 下生成的 monoid。

定义

\[
\boxed{
\operatorname{Ctx}_\Sigma(E)
=
\{(x,y):
(c(x),c(y))\in E
\text{ for every }c\in M(\Sigma)\}.
}
\]

则：

1. `Ctx_Sigma(E)` 是 equivalence relation；
2. `Ctx_Sigma(E) subseteq E`；
3. 它被所有 elementary translations 保持，因此被所有 basic operations 保持；
4. 所以它是 `Sigma`-congruence；
5. 若 `R subseteq E` 是任何其他 `Sigma`-congruence，则所有 contexts 都保持 `R`，故

   \[
   R\subseteq\operatorname{Ctx}_\Sigma(E).
   \]

因此

\[
\boxed{
\operatorname{Ctx}_\Sigma(E)
=
E\text{ 内最大的 }\Sigma\text{-congruence}.
}
\]

这就是经典 syntactic-congruence construction 在当前 finite-precision 记号下的表达，不主张历史优先权。

---

## 5. P018-T172 —— 有限 context-refinement recurrence 可以算出 closure

状态：`PROVED / EXECUTABLE`

令

\[
R_0=E.
\]

对任意 equivalence `R`，定义一步 refinement：

\[
\boxed{
\Gamma_\Sigma(R)
=
R
\cap
\bigcap_{\tau\in T_1(\Sigma)}
\tau^{-1}(R).
}
\]

递推定义

\[
\boxed{R_{n+1}=\Gamma_\Sigma(R_n).}
\]

每个 `R_n` 都是 equivalence relation，而且

\[
R_{n+1}\subseteq R_n.
\]

更关键的是：

\[
\boxed{
R_{n+1}=R_n
\iff
R_n\text{ 是 }\Sigma\text{-congruence}.
}
\]

固定点被所有 elementary translations 保持；由 T170 得到 full multi-ary compatibility。反方向则因为 congruence 本身被每个 translation 保持。

`R_n` 也可以理解为：在所有长度不超过 `n` 的 elementary-translation compositions 下仍 observationally indistinguishable 的 state pairs。它是有限的 **operation-context depth**，把 Supplement 18 的 future-time depth 推广到 operation language。

---

## 6. P018-T173 —— 有限 contextual closure 至多经过 `N-c0` 次 strict refinement

状态：`PROVED / EXECUTABLE`

设

\[
N=|X|
\]

且原 observation partition `E` 有 `c_0` 个 blocks。

每一次 strict step

\[
R_{n+1}\subsetneq R_n
\]

都会真正细化 partition，因此至少增加一个 block；equality 有 `N` 个 blocks，而且必然是 congruence。

所以第一 fixed-point depth `h_Sigma` 满足

\[
\boxed{
h_\Sigma\le N-c_0.}
\]

有限情形不需要 infinite term limit。

可执行压力测试中包含一个四状态 binary algebra，恰好达到该上界。

---

## 7. P018-T174 —— 稳定的有限 relation 正是 syntactic/contextual congruence

状态：`PROVED / EXECUTABLE`

令 `R_*` 为 T172–T173 得到的第一个 stable partition。

因为 `R_*` 是 congruence 且 `R_* subseteq E`，由 T171 最大性：

\[
R_*\subseteq\operatorname{Ctx}_\Sigma(E).
\]

反过来，contextual congruence 位于 `R_0=E` 内，并被所有 elementary translations 保持，因此归纳得到

\[
\operatorname{Ctx}_\Sigma(E)\subseteq R_n
\quad\forall n,
\]

特别地，

\[
\operatorname{Ctx}_\Sigma(E)\subseteq R_*.
\]

故

\[
\boxed{R_*=\operatorname{Ctx}_\Sigma(E)=\operatorname{Syn}_\Sigma(E).}
\]

于是经典上可以由无限 contexts 描述的对象，在有限 `X` 与有限 signature 下被压成一个有显式界的 finite state refinement。

---

## 8. P018-T175 —— Closure quotient 是规范的最小 exact operation state

状态：`PROVED STRUCTURAL CONSEQUENCE / EXECUTABLE`

因为 `R_*` 是 `Sigma`-congruence，每个 basic operation 都能 descent 到

\[
X/R_*.
\]

又因为 `R_* subseteq ker(O)`，原 observation 也能通过该 quotient factor。

现在取任何其他 exact quotient-state refinement `R`，满足

\[
R\subseteq\ker(O)
\]

且使 `Sigma` 内全部 operations well-defined。则 `R` 是 `Sigma`-congruence，所以 T171 给出

\[
R\subseteq R_*.
\]

因此 `X/R` 的 states 数不少于 `X/R_*`，并且它可以继续 quotient 到 canonical closure quotient。

所以

\[
\boxed{X/R_*}
\]

是保持原 observation、同时支持完整声明 operation language 的 coarsest / fewest-state exact quotient refinement。

这是一个 **state sufficiency theorem**；它不声称每种计算协议都必须逐字编码完整 state label。

---

## 9. P018-T176 —— 最小 uniform detail alphabet 有精确大小

状态：`PROVED / EXECUTABLE`

若我们要求修复后的 state 写成

\[
\boxed{(O(x),D(x))}
\]

其中 `D(x)` 来自一个可复用的有限 detail alphabet `D`。

对每个 observation value `y`，令

\[
m_y
=
\#\{R_*\text{-blocks contained in }O^{-1}(y)\}.
\]

同一 observation fiber 内不同 `R_*` blocks 必须拿不同 detail labels，所以

\[
|D|\ge \max_y m_y.
\]

不同 observation fibers 之间可以复用 label，所以 `max_y m_y` 又足够。

因此

\[
\boxed{|D|_{\min}=\max_y m_y.}
\]

这给 `(coarse,detail)` state representation 一个 exact finite information count。

---

## 10. P018-T177 —— Unary predictive closure 正是单 operation 特例

状态：`PROVED STRUCTURAL IDENTIFICATION`

若 signature 只有一个 unary operation `F`，它的 elementary translation family 只有 `F`，于是 recurrence 变成

\[
R_{n+1}=E\cap F^{-1}(R_n),
\]

这正是 Supplement 18 的 finite future-observation recurrence。

所以

\[
\boxed{
\text{predictive closure}
=
\text{unary signature 下的 contextual congruence closure}.
}
\]

unary 与 multi-ary 不是两套理论；前者只是 operation-language closure 的最简单情形。

---

## 11. P018-T178 —— Exact radix-quotient addition 强制保留完整 remainder

状态：`PROVED / EXECUTABLE`

定义

\[
Q_r(n)=\left\lfloor\frac nr\right\rfloor,
\qquad r\ge2.
\]

把自然数 addition 作为 operation language。

取同一 quotient fiber 中两个不同 states：

\[
x=qr+u,
\qquad y=qr+v,
\qquad 0\le u<v<r.
\]

选择 additive one-hole context

\[
\boxed{c_t(z)=z+t,\qquad t=r-1-u.}
\]

则

\[
Q_r(x+t)=q,
\]

但

\[
Q_r(y+t)=q+1.
\]

因此同一完整 quotient fiber 内**任意两个不同 residues 都能被某个 addition context 区分**。

于是 `ker(Q_r)` 内最大的 addition congruence 就是 equality：

\[
\boxed{
\operatorname{Syn}_{+}(\ker Q_r)=\Delta.
}
\]

每个完整 quotient fiber 都必须留下 `r` 个不同 substate labels。由 T176，

\[
\boxed{|D|_{\min}=r.}
\]

规范选择

\[
D(n)=n\bmod r
\]

因此不只是方便：在支持任意 exact addition、且 state 写成 `(Q_r(n),D(n))` 的 per-state refinement 中，小于 `r` 个 detail labels 不可能成立。

一旦保留 residues `u,v`，carry

\[
\kappa_r(u,v)=\left\lfloor\frac{u+v}{r}\right\rfloor
\]

就是 derived interaction data，而不是额外独立的 per-state coordinate。

所以此前 carry 路线可以进一步压成：

\[
\boxed{
\text{remainder = minimal operand state detail; carry = derived cross-input transport.}
}
\]

---

## 12. P018-T179 —— 支持更多 operations 只可能要求更多 detail

状态：`PROVED / EXECUTABLE`

若

\[
\Sigma\subseteq\Sigma',
\]

任何 `Sigma'`-congruence 自动也是 `Sigma`-congruence，因此同一 observation equivalence 内的最大 congruences 满足

\[
\boxed{
\operatorname{Syn}_{\Sigma'}(E)
\subseteq
\operatorname{Syn}_{\Sigma}(E).
}
\]

扩大允许的 operation language，只能让 exact state representation 更细，绝不能成为丢弃 detail 的理由。

这给 **context-dependent precision** 一个严格数学形式：

> state 的最低充分精度，不只取决于“现在能观察到什么”，还取决于“这个 state 必须 exact 支持哪些 operations”。

这与项目 `value + precision + context` 的研究 ontology 直接一致，但本补充并不修改受保护的 worldview 文件。

---

## 13. P018-T180 —— Contextual closure 对 observation 单调并保持 meet

状态：`PROVED / EXECUTABLE`

固定 operation signature。若

\[
E_1\subseteq E_2,
\]

则

\[
\boxed{
\operatorname{Syn}_\Sigma(E_1)
\subseteq
\operatorname{Syn}_\Sigma(E_2).
}
\]

更细的 static observation 不可能得到更粗的 exact contextual state。

更强地，对任意 observation equivalence family：

\[
\boxed{
\operatorname{Syn}_\Sigma\!\left(\bigcap_i E_i\right)
=
\bigcap_i\operatorname{Syn}_\Sigma(E_i).
}
\]

证明：右侧是位于所有 `E_i` 内的 congruence，因此位于其 intersection 内；反过来，intersection 内最大的 congruence 必然位于每个 `E_i` 内的最大 congruence。

所以 product / multi-channel observation refinement 与 contextual closure 兼容：先分别 closure 后 intersect，或者先组合 observation 再 closure，得到相同 final exact equivalence。

---

## 14. P018-C18 —— 分别做 operation closure 后简单取交并不能处理联合语言

状态：`COUNTEREXAMPLE / MIXED-CONTEXT BOUNDARY`

T180 的 observation meet preservation **不能**误解成 operation-signature 也有同样规则。

取

\[
X=\{0,1,2,3\}
\]

与 observation partition

\[
E=\{\{0,1,2\},\{3\}\}.
\]

定义两个 unary operations：

\[
f=(0,0,1,0),
\qquad g=(0,3,0,0),
\]

例如 `f(2)=1`、`g(1)=3`。

只看 `f` 时，`E` 已 closed：

\[
\operatorname{Syn}_{\{f\}}(E)=E.
\]

只看 `g` 时：

\[
\operatorname{Syn}_{\{g\}}(E)
=
\{\{0,2\},\{1\},\{3\}\}.
\]

所以两个单独 closure 的 intersection 仍识别 `0~2`。

但 mixed context

\[
g\circ f
\]

会把它们分开：

\[
g(f(0))=0,
\qquad g(f(2))=3.
\]

因此联合 closure 是 equality：

\[
\boxed{
\operatorname{Syn}_{\{f,g\}}(E)
\subsetneq
\operatorname{Syn}_{\{f\}}(E)
\cap
\operatorname{Syn}_{\{g\}}(E).
}
\]

所以 combined operation language 所需的 exact state，不能一般性地通过“每个 operation 独立 closure 后取交”得到。**Mixed nested contexts 必须进入计算。**

---

## 15. P018-T181 —— P018-Q117 在 finite finitary quotient-state refinement 意义下解决

状态：`RESOLVED FOR FINITE STATE + FINITE FINITARY SIGNATURE`

对有限 state space、有限 finitary operation signature 和 finite-precision observation，令全部 declared operations autonomous 所需的 canonical exact state refinement 是：

\[
\boxed{
\text{反复做 elementary-context partition refinement，直到第一个 fixed point。}
}
\]

该结果：

- 至多经过 `N-c0` 次 strict refinement；
- 正好等于原 observation equivalence 内经典 greatest/syntactic congruence；
- 使所有 basic operations exact descent；
- 是保持原 observation 的 coarsest / fewest-state exact quotient refinement；
- 对 `(observation,detail)` state coordinate 给出最小 uniform detail alphabet `max_y m_y`；
- 把 Supplement 18 的 unary predictive closure 包含为特例。

因此 P018-Q117 在**有限 finitary algebra 的 quotient-state sufficiency 意义下**得到解决。

---

## 16. P018-C19 —— 最小 exact state 不等于最小 transport encoding 已被解决

状态：`DESIGN BOUNDARY`

T175–T181 确定的是最小 exact **state quotient/refinement**。它们并不证明每种 operation 实现都必须用同一种表示传输或重新计算完整 refined-state label。

radix addition 已经说明二者不同：

- full residue 是不可避免的 per-operand state detail；
- carry 是 compact derived interaction term；
- exact state theorem 与 exact transport/cocycle theorem 回答的是不同问题。

对一般 algebra，noncongruent coarse observation 在 underlying state distinctions 已由 `Syn_Sigma(E)` 固定后，仍可能存在比“完整 interaction table”更紧凑的 structured extension / transport law。

因此 finite finitary 情形下，下一问题不再是“最小 exact state 是什么”。新的问题是：

> **Q119 —— 什么时候 contextual state refinement 可以通过 structured、composable 的 interaction data（carry/cocycle-like 或其他结构）高效实现？其最小 transport complexity 是什么？**

不预设所有这种结构都属于 cohomology。

---

## 17. Executable pressure tests

新增：

- `src/enterprise_math/contextual_closure.py`
- `tests/test_contextual_closure.py`

测试覆盖：

1. 已经 congruent 的 quotient operations；
2. noncongruent binary quotient 细化到 equality；
3. 一个达到 `N-c0` 上界的 binary example；
4. two-state binary operation tables 与 binary observations 的穷举；
5. 对 candidate congruence partitions 的 maximality；
6. operation-signature monotonicity；
7. C18 strict mixed-context counterexample；
8. independent observation channels 的 meet preservation；
9. radix-quotient addition 中所有测试 residues 的 context separation；
10. empty operation language，此时 contextual closure 正确退化成 static observation partition。

---

## 18. 当前 foundational feedback

finite-precision hierarchy 现在可以进一步收紧为：

\[
\boxed{
\text{static observation equivalence}
\to
\text{declared operation signature}
\to
\text{contextual/syntactic congruence closure}
\to
\text{minimal exact state}
\to
\text{optional structured transport data}.
}
\]

这把此前容易混在一起的三个问题拆开：

1. **观察者现在能区分什么？** —— static precision。
2. **在全部允许 operation contexts 下，哪些 distinctions 必须永久保留？** —— exact state sufficiency / congruence closure。
3. **充分 state 之间的 interactions 怎样才能高效编码？** —— carry/cocycle/transport layer。

第二个问题在 finite finitary algebra 中已经有 canonical finite answer。第三个问题仍开放，不能再通过机械地把每个 defect 都叫作 cocycle 来回答。
