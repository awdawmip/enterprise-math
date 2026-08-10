# P025 补充 96 —— Ferrers Activation Area 作为双轴离散势函数

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-orbit-normal-stage91`  
依赖：P025 补充 93–95  
硬阻断：`NONE`

## 1. Stage 93 已经给出一个 scalar invariant

对 finite activation matrix

\[
B_{k,j}=\mathbf1_{\{\rho_j\ge T_k\}},
\]

Stage 93 定义 activation area

\[
\boxed{A:=\sum_{k=1}^s\sum_{j=0}^hB_{k,j}.}
\]

它就是 declared finite future grid 中 active threshold/node cells 的数量。

Stage 96 研究这个 scalar 在 Stage 94 两种 primitive axis extensions 下如何变化。

## 2. P025-T229 —— threshold-axis first difference

固定旧的 `h+1` 个 orbit nodes，插入一个 new threshold `T`。

设其 crossing depth 为

\[
j_T\in\{0,\ldots,h,\infty\}.
\]

new row 恰贡献 old nodes 中达到 `T` 的数量。因此

\[
\boxed{
\Delta_TA
=
\begin{cases}h+1-j_T,&j_T<\infty,\\0,&j_T=\infty.
\end{cases}}
\]

所以 threshold-centric crossing coordinate 正好是计算 threshold-direction area increment 所需的 local data。

## 3. P025-T230 —— orbit-axis first difference

固定旧 `s` 个 thresholds，追加一个 new orbit node。

令其 node rank 为

\[
r_{h+1}=\#\{k:\rho_{h+1}\ge T_k\}.
\]

new column 恰贡献 `r_{h+1}` 个 active cells，所以

\[
\boxed{\Delta_JA=r_{h+1}.}
\]

因此 node-centric rank coordinate 正好是计算 orbit-direction area increment 所需的 local data。

## 4. Directional coordinates 是同一个 potential 的 finite differences

Stages 93–94 已证明 crossing 与 rank coordinates dual，但 update locality 不同。

P025-T229–230 把它进一步收紧为

\[
\boxed{
\text{crossing depth controls }\Delta_TA,
\qquad
\text{node rank controls }\Delta_JA.
}
\]

所以两种 natural charts 可以被理解成同一个 scalar activation potential 的 directional first-difference coordinates。

这解释了它们的 axis locality，而无需把某一个 chart 宣布为 intrinsically preferred。

## 5. P025-D41 —— new corner bit

现在同时加入一个 new threshold `T` 与一个 new orbit node。

定义 new corner activation bit

\[
\boxed{c:=\mathbf1_{\{\rho_{h+1}\ge T\}}.}
\]

这是 newly inserted row 与 newly appended column 唯一共同新增的 cell。

## 6. P025-T231 —— mixed second difference 等于 corner bit

记：

- `A`：old area；
- `A_T`：threshold extension 后；
- `A_J`：orbit extension 后；
- `A_{T,J}`：两个 extensions 都完成后。

则

\[
\Delta_J\Delta_TA=(A_{T,J}-A_T)-(A_J-A),
\]

以及

\[
\Delta_T\Delta_JA=(A_{T,J}-A_J)-(A_T-A).
\]

所有 old-grid contributions 都相消，只剩 new corner。因此

\[
\boxed{
\Delta_J\Delta_TA
=
\Delta_T\Delta_JA
=c
\in\{0,1\}.
}
\]

这就是 exact **corner law**。

## 7. P025-T232 —— one biaxial extension 后的 area reconstruction

corner law 给出

\[
\boxed{A_{T,J}=A+\Delta_TA+\Delta_JA+c.}
\]

所以 enlarged activation area 可由四项重建：

1. old area；
2. threshold-axis first difference；
3. orbit-axis first difference；
4. 一个 new corner bit。

其余 cells 无需独立 accounting。

## 8. Active corner 的 exact working fixture

使用 Stage 93 的

\[
(q,p,m)=(3,41,2)
\]

state，thresholds 为

\[
\frac1{22},\frac12,1,11
\]

并观察到 depth 3。old activation area 是

\[
\boxed{A=9.}
\]

插入

\[
T=10.
\]

new threshold 在 depth 2 first crossing，所以四个 old nodes 中有两个 active：

\[
\boxed{\Delta_TA=2.}
\]

appended dyadic node 对 old thresholds 的 rank 就是 orbit-axis first difference。

由于 old final pressure 已经

\[
\frac{221}{22}>10
\]

且 orbit nondecreasing，new corner 必 active：

\[
\boxed{c=1.}
\]

executable layer 验证两种 mixed differences 都等于 1，并 exact reconstruct final area。

## 9. Inactive corner fixture

在同一 finite state 上插入极高 threshold，例如

\[
T=10^{100}.
\]

它在 old horizon 未达到，也高于 executable check 中使用的 next finite arithmetic pressure，因此

\[
\boxed{\Delta_TA=0,\qquad c=0.}
\]

mixed second difference 为 0。

这证明 corner law 是真实 Boolean local response，而不是恒等于某个常数。

## 10. Multi-threshold orbit jump 仍只产生一个 mixed corner

对

\[
(q,p,m)=(7,17,2),
\]

从 horizon 0 开始，old thresholds 为

\[
\frac12,1,2.
\]

appended exponent-four node 的 pressure 是 `13/6`，因此

\[
\boxed{\Delta_JA=3.}
\]

因为它同时跨过三个 old thresholds。

再插入 new threshold `T=3`。new node 没达到它，因此

\[
\boxed{c=0.}
\]

即使 orbit-axis first difference 很大，mixed second difference 仍只是一个 local corner bit。

## 11. P025-T233 —— extension diamond 有一个 scalar potential

Stage 95 证明 threshold / orbit semantic extension diamond commute。

Stage 96 进一步证明其 area increments 是一个 scalar potential 的 exact finite differences，并满足

\[
\boxed{\Delta_J\Delta_TA=\Delta_T\Delta_JA.}
\]

共同 mixed derivative 并不是简单的 0，而是记录 newly created corner cell。

所以 flat extension diamond 携带一个非平凡但完全 local 的 mixed response。

## 12. Stage 96 **没有**证明什么

scalar area `A` 是 aggregate invariant。Stage 96 **没有**证明 `A` 能决定 full activation matrix、Ferrers boundary、crossing depths 或 node ranks。

那种更强 collapse 需要 injectivity，不能由 potential law 自动推出。

下一 stage 必须主动测试这一边界，而不是默默把 scalar potential 当 sufficient semantic state。

## 13. 架构含义

exact lesson 是分层的：

- boundary state 保存完整 finite threshold semantics；
- crossing / rank charts 编码 directional local derivatives；
- activation area 是适合 aggregate update accounting 的 scalar potential；
- mixed derivative 是 new corner activation。

因此一个有用 scalar response law 并不等于它可以替代 underlying state。

这对任何 future precision calculus 中 state、coordinate、potential、local response 的分层都很重要。

## 14. Prior-art / novelty 边界

finite differences、scalar potentials 与 mixed-difference identities 都是 classical / general concepts。

P025 不单独主张这些 notions 新颖。

项目侧结果只是 exact arithmetic Ferrers instantiation 以及它作为 precision-state update law 的 interpretation。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 15. 可执行资产

新增：

- `src/enterprise_math/abc_dyadic_activation_potential.py`；
- `tests/test_abc_dyadic_activation_potential.py`。

executable layer 验证两个 first-difference formulas、active / inactive corner fixtures、mixed-difference commutation 与 exact area reconstruction。

## 16. 下一前沿

不存在硬阻断。继续：

1. 搜索同一 threshold grid、同一 horizon、相同 area 但 Ferrers boundaries 不同的 exact arithmetic collisions；
2. 若找到，把 `potential != sufficient state` 记录为 reusable negative boundary；
3. 识别哪些 future queries 在 scalar area 上是 safe 的；
4. 与 P024 response-law layering、P023 future-safe quotient language 对照；
5. 然后决定 Stage91–97 是形成新 Foundation Feedback Packet，还是只扩展 Stage90 packet。
