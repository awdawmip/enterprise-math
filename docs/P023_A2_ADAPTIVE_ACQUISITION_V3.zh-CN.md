# P023 / A2 —— Adaptive Acquisition 与 Process Precision，v3

状态：`PROVED OWNER RESEARCH`  
归属：A2 future-compatible quotient  
依赖：A2 Precision Incidence Core v3、A2 Conditional Scheduling Core v3、P011 collision-spectrum calculus  
纪律：确定性 decision tree、ordered decision diagram、Kraft-type capacity bound、direct-sum argument 与 partition kernel 都属于成熟数学。本文的项目侧作用，是把这些结构与精确整数 repair cost / future-safe precision 接起来。

## 1. Final precision 不等于 acquisition complexity

令 `X` 为有限非空状态集，`T:X->Z` 为最终 target，`Q={q_i:X->A_i}` 为有限 primitive query language。固定整数 alphabet base `B>=2`。

在当前 compatible block `C` 上，query 实现 `r=|q(C)|` 个 answers，并支付

\[
\boxed{c_B(q\mid C)=L_B(r),\qquad L_B(r)=\min\{\ell:r\le B^\ell\}.}
\]

query 在 `C` 上恒定时成本为 0；当且仅当 `T` 在 `C` 上恒定时 target 已解决。

核心区分是

\[
\boxed{\text{answer precision}\preceq\text{strategy-transcript precision}\preceq\text{all-tools language-safe precision}.}
\]

## 2. A2-AA-T01 —— All-tools language-safe quotient

定义

\[
\boxed{E_{T,\mathcal Q}=\ker T\cap\bigcap_{q\in\mathcal Q}\ker q.}
\]

它是 target 与**所有 allowed queries** 都能够下沉的最粗静态 quotient。把 `X` 替换为 `X/E_{T,Q}` 不改变 acquisition problem：任意 reachable query-answer block 都是完整 signature classes 的并，而同 signature 内重复 raw states 不改变任何 realized query value 或 target constancy。

所以

\[
\boxed{E_{T,\mathcal Q}=\ker T\iff\text{每个 primitive query 都通过 target factorize}.}
\]

若该条件失败，最终 answer precision 对“模拟完整 primitive tool language”而言太粗。

## 3. Eager global state 与 lazy local refinement

`E_{T,Q}` 是 eager 的：在全空间中同时保存所有 query distinctions。adaptive strategy 是 lazy 的：在 typed context block `C` 上只调用一个局部 map `q|_C:C->q(C)`，不同 branch 可以调用完全不同的 future queries。

因此 chosen strategy 不需要一次性物化完整 Cartesian query signature。Global factorization 仍然是“一个静态 state 支持整个 allowed language”的正确条件；branch-local acquisition 只要求实际调用的 query 在当前 context 上合法。

## 4. A2-AA-T02 —— Strategy transcript sandwich

对 exact deterministic strategy `S`，令 `Tr_S(x)` 为最终实际 query-name / answer 序列，并记 `E_S=ker(Tr_S)`。则

\[
\boxed{E_{T,\mathcal Q}\subseteq E_S\subseteq\ker T.}
\]

左侧来自 deterministic strategy：完整 target/query signature 相同就必然走同一路径。右侧来自 exactness：target 是 terminal transcript 的函数。

所以 strategy 在“全部可用 process detail”与“最终 answer”之间选择一个中间 quotient。

## 5. Proof-transcript repair spectrum

对 target value `z`，令

\[
r_S(z)=\#\{\text{最终得到 answer }z\text{ 的不同 terminal transcripts}\}.
\]

定义

\[
\boxed{\mathcal P_k(S)=\sum_z\binom{r_S(z)}k.}
\]

这精确等于 final forgetting map `transcript -> answer` 的 P011 collision spectrum，因此 binomial inversion 可恢复完整 local proof-multiplicity distribution。

若所有 primitive queries 都通过 `T` 下沉，则 `E_{T,Q}=ker T`，sandwich 立刻强迫任何“target 一决定就停止”的 exact strategy 满足 `E_S=ker T`；此时每个 answer 只有一个 transcript class。

## 6. A2-AA-T03 —— 精确 adaptive Bellman recurrence

对 compatible block `C` 与 remaining queries `R`，记 `A_B(C,R)` 为最小 worst-case future symbol cost。若 `T` 在 `C` 上恒定，值为 0；否则

\[
\boxed{
A_B(C,R)=\min_{q\in R,\ |q(C)|>1}
\left[L_B(|q(C)|)+\max_{a\in q(C)}A_B(C\cap q^{-1}(a),R\setminus\{q\})\right].
}
\]

若没有任何 query path 能精确决定 target，则该值为无穷/未定义。整个 compiler 不使用 probability 或 expected cost。

## 7. A2-AA-T04 —— 整数 capacity lower bound

设 exact strategy 的 worst cost 为 `d`，terminal leaf `lambda` 的 path cost 为 `c(lambda)`。把每个 node 的局部 query answer 编成定长 base-`B` symbols 后，沿 path 串接得到 prefix code，因此

\[
\boxed{\sum_\lambda B^{d-c(\lambda)}\le B^d.}
\]

terminal transcripts 数不超过 `B^d`；exact leaf 又不可能含两个不同 target answers，所以

\[
\boxed{A_B(T;\mathcal Q)\ge L_B(|T(X)|).}
\]

## 8. 两种彼此独立的 acquisition defect

记 `N_ans=|T(X)|`、`N_tr=|Tr_S(X)|`。则

\[
\boxed{
d-L_B(N_{\rm ans})=
\underbrace{d-L_B(N_{\rm tr})}_{\text{tree/radix packing slack}}+
\underbrace{L_B(N_{\rm tr})-L_B(N_{\rm ans})}_{\text{transcript multiplicity slack}}.}
\]

两项可以独立非零。

四个 exact target states 配三个 singleton binary tests 时，`N_ans=N_tr=4`，但任何 allowed tree 都要 depth 3：纯 tree-packing slack 为 1。

另取 `T=(0,0,1,1)`、`Q1=(0,1,0,1)`、`Q2=(0,1,1,0)`。target 是两个 query answers 的 equality/XOR relation，两个 query 都必须使用。此时 4 个 transcripts 被最终合并成 2 个 answers；tree depth 精确为 2，tree packing tight，而 transcript multiplicity 独占 1 个 binary depth，spectrum 为 `(4,2)`。

## 9. A2-AA-T05 —— Presentation sensitivity

在上一四状态系统里，`(Q1,Q2)` 已经生成 exact four-state query partition。现在加入 bundled query `QT=T`。因为 `T` 本来就是 `(Q1,Q2)` 的函数，所以 information partition 完全不变，但 acquisition cost 从 2 降到 1。

因此

\[
\boxed{\text{相同 generated precision relation}\not\Rightarrow\text{相同 acquisition complexity}.}
\]

一个 query 可以在 partition 意义上 redundant，却在 algorithmic/interface 意义上极有价值。Primitive query presentation 与 precision closure 是不同资源。

## 10. Requirement language 与 tool language 单调方向相反

若 `T'` 比 `T` 更细：

\[
\boxed{A_B(T';\mathcal Q)\ge A_B(T;\mathcal Q).}
\]

若 `Q subseteq Q'`：

\[
\boxed{A_B(T;\mathcal Q')\le A_B(T;\mathcal Q).}
\]

所以更丰富的 **requirement language** 只能要求更多 distinction，而更丰富的 **tool language** 只能让同一 answer 更便宜或不变。若 direct target query 可用，则

\[
\boxed{A_B(T;\mathcal Q\cup\{T\})=L_B(|T(X)|).}
\]

## 11. A2-AA-T06 —— Adaptive / ordered / synchronous hierarchy

必须区分三种 acquisition model：

1. **adaptive**：next query 可以自由依赖当前 transcript；
2. **ordered interactive**：固定一个 global query order，每条 branch 可以 skip query、提前停止，但不能返回已跳过的 earlier query；
3. **stage-synchronous**：固定 global stage order；某 stage 一旦执行，同一 query stage 暴露给全部 unresolved contexts，alphabet 必须容纳其中最大 local branch count。

同一个 finite target/query system 满足

\[
\boxed{L_B(|T(X)|)\le A_{\rm adaptive}\le A_{\rm ordered}\le A_{\rm stage}.}
\]

每个不等号都可以严格，但由不同 finite witness 暴露不同 defect。

## 12. A2-AA-C01 —— 真正的 adaptive-order separation

在 Boolean cube `(x0,x1,x2,x3) in {0,1}^4` 上定义

\[
f=\begin{cases}
1-x_1,&x_0=0,x_2=0,\\
1-x_3,&x_0=0,x_2=1,\\
1-x_2,&x_0=1,x_1=0,\\
1-x_3,&x_0=1,x_1=1.
\end{cases}
\]

adaptive depth-3 tree 先问 `x0`：`x0=0` 后问 `x2`，再按 answer 问 `x1` 或 `x3`；`x0=1` 后问 `x1`，再按 answer 问 `x2` 或 `x3`。存在需要 3 个 variables 才能 certify 的 input，所以 depth 2 不可能。

任何 fixed variable order 都不能达到 3：若 `x0` first，`x0=0` restriction 强迫 selector `x2` 排在 `x1,x3` 前，而 `x0=1` restriction 强迫 selector `x1` 排在 `x2,x3` 前，global remaining order 冲突；若 `x1`、`x2` 或 `x3` first，则某个 restriction 留下 decision depth 为 3 的三变量 subfunction。

故

\[
\boxed{A_{\rm adaptive}=3<A_{\rm ordered}=4.}
\]

四个 binary variables 还是这种 separation 的最小规模：最多三个 variables 时，adaptive depth 3 已等于查询全部 variables；而 depth-2 tree 总能把 root variable 放第一，再把两条 branch 的 second variables 放后面并允许 branch-local skips，从而线性化。

## 13. A2-AA-C02 —— Storage lower bound 可以严格不足

四个 target states 与 singleton tests `A=(0,0,0,1)`、`B=(0,0,1,0)`、`C=(0,1,0,0)` 的 joint target 有 4 个 classes，binary storage depth 为 2。但任何 first query 都只分成 `1+3`，所以精确 adaptive strategy 需要 3：

\[
\boxed{2=L_2(4)<A_{\rm adaptive}=3.}
\]

这里所有 queries 都通过 target 下沉，所以 overhead 是纯 tree-packing defect。

## 14. A2-AA-T07 —— Capacity-tight balanced splitter criterion

假设所有 queries 都通过 target 下沉，并且当前 block 恰好含 `B^d` 个 target classes。adaptive acquisition 精确达到 storage lower bound `d`，当且仅当存在递归 tree，使每个含 `B^e` target classes 的 node 使用一个恰有 `B^ell` 个真实 answers 的 query，并且每个 child 恰有 `B^(e-ell)` 个 target classes。

必要性来自 capacity：每个 child 最多容纳 `B^(e-ell)` classes，children 最多 `B^ell` 个；parent 已经装满 `B^e`，因此所有不等式都必须取等。充分性由串接 exact local radix codes 得到。

对 binary queries，这就等价于每次都必须把当前 target classes **精确对半切开**。

## 15. A2-AA-C03 —— Ordered interactive 与 stage-synchronous 不同

取 8 个 states：

`A=(0,1,2,3,4,5,5,5)`，
`B=(0,1,1,1,2,3,4,5)`，
`C=(0,0,0,0,1,1,1,1)`，

target 为 `(A,B,C)`。ordered interactive `C,A,B` 可以 branch-locally skip 不需要的 middle query：`C=0` 时 `A` 已决定 `B`，`C=1` 时 `B` 已决定 `A`。所以 adaptive 与 ordered 都为 3。

但 synchronous stage 无法在两个 contexts 同时选不同 second query，最优为 5：

\[
\boxed{A_{\rm ordered}=3<A_{\rm stage}=5.}
\]

这也纠正了一次中间过强解释：之前把“non-skippable fixed order”误叫成标准 ordered interaction；该错误不会进入 owner theorem。

## 16. A2-AA-T08 —— Adaptive direct sum

给两个 finite acquisition systems `(X1,T1,Q1)`、`(X2,T2,Q2)`，构造 product `X=X1 x X2`、`T=(T1,T2)`，并只允许 component-local lifted queries。则

\[
\boxed{A_B(X,T;\mathcal Q_1\sqcup\mathcal Q_2)=A_B(X_1,T_1;\mathcal Q_1)+A_B(X_2,T_2;\mathcal Q_2).}
\]

所有 reachable compatible blocks 都保持 rectangle `C1 x C2`。component Bellman values 之和精确满足 product Bellman equation：left query 只改变 left block/cost，right optimum 完全不变，反之亦然。因此 exact product decomposition 是 research compiler 的 genuine fast path。

## 17. Proof history 是受控的 A1/A2 collapse

exact strategy 给出 quotient chain

\[
X/E_{T,\mathcal Q}\longrightarrow X/E_S\longrightarrow X/\ker T.
\]

第一步忘掉 tool language 中存在但 chosen strategy 未使用的 distinctions；第二步丢弃 proof history，只留 answer。P011 collision spectrum 可以精确作用于这些 forgetting maps。这只是 proof/process record 上的数学 quotient，不是物理 irreversibility claim。

## 18. Tool consequence

可靠 research compiler 以后至少要分开声明：

- **answer language**：最终 theorem/output 要知道什么；
- **primitive acquisition language**：允许调用哪些 exact queries/operations；
- **strategy tree**：各 context 实际调用什么；
- **encoding model**：adaptive、fixed ordered 或 synchronous stage；
- **retained proof history**：transcript 最后丢弃还是保留。

因此

\[
\boxed{\text{precision state}\ne\text{query-language complexity}\ne\text{strategy complexity}.}
\]

## 19. Prior-art boundary

Deterministic decision tree、ordered decision diagram、dynamic programming、Kraft-style coding bound、direct-sum reasoning、kernel 与 finite partition lattice 都属于前人数学；Enterprise Math 不主张这些 generic structures 的原创性。当前 owner result 的项目价值，在于把它们与 integer repair alphabet、future-safe quotient semantics、proof-transcript repair spectrum 与 theorem-lifting workflow 精确接起来。综合 packaging 的历史 novelty 仍未验证。

## 20. Executable specification

- `src/enterprise_math/a2_adaptive_acquisition.py`
- `tests/test_a2_adaptive_acquisition.py`

测试固定 four-bit adaptive-vs-ordered separation、three-variable minimality boundary、纯 tree-packing / transcript-multiplicity gaps、partition-redundant bundled-query speedup、balanced-split tightness、ordered-vs-stage separation 与一个 adaptive direct-sum witness。

## 21. Foundation-backflow boundary

这组结果已经成熟到足以形成 Foundation Feedback Packet，但不应直接改 `FOUNDATIONS`。当前最弱且已证明的 finite distinction 是

\[
\boxed{\text{最终 sufficient distinction}\ne\text{allowed proof/acquisition process 所需 distinction}.}
\]

任何关于 physical state、cognition 或 ontological information 的进一步解释，都必须增加独立 hypotheses。
