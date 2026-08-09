# P023 —— 标签删除与 image separation，补充 08

状态：`PROVED`  
归属：A2 / P023 future-compatible quotient  
来源压力：P017 L054/L052/L055 与 P024 future-safe precision  
纪律：集合像、单射、decoder 存在性与子集单调性都属于初等成熟数学；这里提炼的是可复用的 zero-repair 与 realizability-audit 接口。

## 1. 辅助标签什么时候真的可以删掉

把带标签状态写成

\[
(i,x),
\qquad x\in S_i,
\]

其中 `i` 是 shell / factor / residue label，`x` 是继续保留的坐标。

future-safe 问题不是“这个标签曾经有没有用”，而是：经过所有声明的后续映射以后，它是否仍然能从保留状态中唯一恢复。

## 2. 设置

令带标签状态空间为

\[
S=\{(i,x):x\in S_i\}.
\]

当前删除映射为

\[
E(i,x)=x,
\]

并令

\[
G:X\to Y
\]

为后续确定性映射。

定理中的 `S_i` 指每个标签下的**真实 admissible states**。如果手里只有更大的 envelope，正确的单向逻辑见第 7 节。

## 3. P023-S8-T01 —— 当前标签删除判据

状态：`PROVED`。

`E` 在带标签状态空间上单射，当且仅当

\[
\boxed{S_i\cap S_j=\varnothing\qquad(i\ne j).}
\]

### 证明

若两个标签共享同一个保留状态 `x`，则 `(i,x)` 与 `(j,x)` 是不同 tagged states，却被删除映射送到同一值。反之，若真实 shell sets 两两不交，则保留坐标相等会强迫标签相等，继而 tagged state 相等。∎

### 含义

当保留坐标本身已经决定 shell identity 时，显式 label 就是冗余状态维度。

## 4. P023-S8-T02 —— 后续映射后的标签恢复

状态：`PROVED`。

存在 decoder

\[
D:G\!\left(\bigcup_iS_i\right)\to I
\]

满足

\[
D(G(x))=i\qquad(x\in S_i)
\]

当且仅当

\[
\boxed{
G(S_i)\cap G(S_j)=\varnothing
\qquad(i\ne j).
}
\]

### 证明

若存在共同 future image，则 decoder 必须在同一个值上返回两个不同标签，矛盾。若 images 两两不交，则每个 reachable output 只属于唯一 shell image，据此定义 decoder 即可。∎

所以 future-safe label deletion 正是一个 image-separation test。

## 5. P023-S8-T03 —— 标签恢复弱于完整状态恢复

状态：`PROVED`。

映射

\[
H(i,x)=G(x)
\]

在完整 tagged state space 上单射，当且仅当同时满足：

1. 不同 shell images 两两不交；
2. 每个限制 \(G|_{S_i}\) 都是单射。

### 证明

跨 shell collision 会破坏标签恢复；shell 内 collision 即使不丢标签，也会合并不同细状态。两类 collision 都不存在时，完整 tagged state 才能唯一恢复。∎

因此

\[
\boxed{
\text{label 可恢复}
\not\Rightarrow
\text{完整状态可恢复}.
}
\]

## 6. P023-S8-T04 —— 声明 context 下的安全标签删除

状态：`PROVED`。

给定声明 context family

\[
\mathcal G=\{G_c:X\to Y_c\}_{c\in C},
\]

要使标签删除后在每一个 context 输出上仍可恢复，充要条件是

\[
\boxed{
G_c(S_i)\cap G_c(S_j)=\varnothing
\quad\text{对所有 }c\text{ 与 }i\ne j.
}
\]

任意一个非空 overlap 都是 zero repair 失败的精确见证。

## 7. P023-S8-T05 —— admissibility-filtered envelope principle

状态：`PROVED`。

设真实 admissible shell 不方便直接处理，但知道一个外包络

\[
S_i\subseteq U_i.
\]

则对任意确定性映射 `G`，

\[
G(S_i)\subseteq G(U_i).
\]

因此

\[
\boxed{
G(U_i)\cap G(U_j)=\varnothing
\Longrightarrow
G(S_i)\cap G(S_j)=\varnothing.
}
\]

### 证明

集合像保持子集关系。若更大的 image sets 已经不交，它们的子集当然也不交。∎

### 逻辑方向

逆命题一般不成立。envelope overlap 只能证明一个**候选 collision**，它可能在 realizability / admissibility filter 后完全消失。

所以安全的研究规则是

\[
\boxed{
\text{envelope 不碰撞可向下传；envelope 碰撞不能向下传。}
}
\]

当同时存在粗 candidate 与精确算术 envelope 时，应该做三层审计：

\[
\text{candidate superset}
\supseteq
\text{exact envelope}
\supseteq
\text{actual admissible state}.
\]

## 8. P017 L054 的重解释

在 open square basin 中，真实 least-prime shell coordinate set 是

\[
S_p(k)=
\{n/p:\ k^2<n<(k+1)^2,\ \operatorname{spf}(n)=p\}.
\]

它的精确 raw cofactor envelope 是

\[
U_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}p\right\rfloor
\right].
\]

L054 证明 `k>=4` 后所有 envelopes `U_p(k)` 两两不交。因为

\[
S_p(k)\subseteq U_p(k),
\]

T05 立即推出真实 shell coordinate sets 也两两不交。因此从 `k>=4` 起，least-prime label `p` 是 stripped cofactor `q` 的函数。

固定 shell 内还有 `n=pq`，所以一旦由 `q` 解码出唯一 shell，也能恢复 composite state。

## 9. Root projection 与 P017 三层结构

后续如果只保留

\[
G(q)=R_2(q),
\]

必须区分三个对象：

1. L052 扩大后的 candidate root pair；
2. exact raw cofactor window 的 root image；
3. `p`-rough least-prime shell 实际实现的 root image。

L055 证明更强的中间层结论：不同 lower-band **exact-window** root images 从 `k>=9` 起不交；真实 shell images 作为子集立即继承。

两层确实不同。`k=6` 时，exact `p=3` window 只有通过 `q=16` 才能命中 root 4，但 `3*16=48` 的最小素因子是 2，因此 root 4 并未被 `p=3` shell 真实实现。

所以 actual-image discipline 必须包含 admissibility filter，而不能只保留 exact interval endpoints。

## 10. Repair 的含义

若真实 images 相交，也不应该自动恢复整个原标签。真正需要补回的只是足以拆开**真实冲突 fibers**、并满足声明 task 的最粗 repair。

zero-repair fast path 为

\[
\boxed{
G(S_i)\cap G(S_j)=\varnothing\ \forall i\ne j
\Longrightarrow
\text{shell-label repair cost}=0.
}
\]

P023 补充 09 在 zero repair 失败时进一步给出有限最小 alphabet 的精确计量。

## 11. 研究工具流程

面对 shell、residue、geometric sector、collision mode 等辅助标签：

1. 写出真实 admissible fine sets `S_i`；
2. 若只方便得到 envelopes `U_i`，必须显式记录 `S_i subset U_i`；
3. envelope disjointness 只能作为充分证书；
4. envelope overlap 时，先过滤到真实 admissible states，再宣告 collision；
5. 对每个声明 future map 作用于真实集合；
6. actual images 仍不交，就删除标签；
7. 否则只在真实 overlaps 上编译最小 repair。

可执行资产：
- `src/enterprise_math/label_erasure.py`
- `tests/test_p023_label_erasure.py`
- P017 特化：`src/enterprise_math/p017_actual_root_separation.py`

## 12. 前人工作与新颖性纪律

“images 两两不交当且仅当 label decoder 存在”以及“集合像对包含关系单调”都属于初等集合论，不是新数学。

Enterprise Math 的价值在于把它们固定成 future-safe precision 的研究编译器，并特别用于防止把 candidate/envelope collision 错升格成不可实现状态之间的真实 collision。
