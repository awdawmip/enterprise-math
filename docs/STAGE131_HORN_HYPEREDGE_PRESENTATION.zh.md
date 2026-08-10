# Stage131 — 超越 Unary TC-Spanner 的 Horn Hyperedge Shortcut

状态：`RESEARCH BRIDGE / NONCANONICAL`

unary chain 可以用普通 shortcut graph 表达，但 multi-premise closure rule 不行。一旦某个 conclusion 必须同时等待多个 premises，Stage131 presentation geometry 就从普通 shortest path 进入 hypergraph / AND-OR derivation geometry。

## 1. Horn rule 是 derivation hyperedge

finite Horn rule 写成：

`P => c`，

其中 P 是 nonempty premise set，c 是一个 conclusion。

rule 只有在 P 中**全部** premises 都已 available 时才能 fire。

若 d(x) 表示 atom x 最早出现的 synchronous round，则：

`d(c)=min_(P=>c) [1+max_(p in P)d(p)]`。

其中 `max` 是 conjunctive synchronization cost，`min` 则在多个可选 rules 中选最快的一条。

## 2. 为什么普通 graph shortcut 不安全

最小 witness：

`{a,b}=>c`。

若把它拆成 unary edges：

`a->c`, `b->c`，

就会把 AND 改成 OR，错误地让单独 `{a}` 推出 c。

因此 multi-premise Stage131 shortcut 必须把完整 premise set 作为一个 hyperedge / macro rule 保留。若不做 state expansion，ordinary TC-spanner distance 已不再是正确 semantic execution object。

## 3. Semantically derived Horn macro

candidate macro：

`P=>c`

若 c 已经属于 base closure `Cl(P)`，则它是 semantic safe 的 derived rule。

加入这类 macro 不会改变任何 seed set 的 closure operator；它只可能减少 derivation rounds。

owner 对 small atom systems 的全部 seed subsets 做 exhaustive closure-equality check。

## 4. 最小 multi-premise shortcut witness

Base rules：

`a=>p`，

`b=>q`，

`{p,q}=>z`。

从 seeds `{a,b}`：

- p,q 在 round1 出现；
- z 在 round2 出现。

加入 derived macro：

`{a,b}=>z`，

semantic closure 完全不变，但 z 变成 round1。

这就是 multi-premise 版本的 transitive chain shortcut。

## 5. Rule count 已经不够

unary rule 的 premise width 恒为1，因此 rule count 可以作为第一近似 storage measure。

Horn macro 却可能有几百、几百万个 premises。presentation 至少要同时记录：

- rule count；
- total premise-literal incidences；
- maximum premise width / fan-in；
- execution depth。

这些资源可以朝不同方向变化。

## 6. Balanced binary AND tree

取 `2^h` 个 leaf atoms。每个 internal node 都由两个 children 的 local binary Horn rule 推出。

local semantic basis 有：

`2^h-1`

条 rules，premise literals：

`2(2^h-1)`。

从全部 leaves 出发，root 与完整 closure 都需要 h 个 synchronous rounds。

## 7. Span-s macros

对 `2<=s<=h`，给每个 height>=s 的 node 加一条 derived macro：premises 是它正好向下 s 层的全部 descendants。

每条 macro premise width：

`2^s`。

新增 macro rule 数：

`M_rules(h,s)=2^(h-s+1)-1`。

新增 premise literals：

`M_lits(h,s)=2^(h+1)-2^s`。

当 s=1 时不新增 macro，因为对应 rule 与原 local binary rule 完全相同。

## 8. Exact root-depth law

一个 node 可以用 local rule 上升1层，也可以用 span-s macro 上升 s 层。

所以 height h 的 root 最短 derivation 会尽量使用 s-level jumps：

`D_root(h,s)=floor(h/s)+(h mod s)`。

形式上与 unary `{1,s}` coin-count recurrence 相同，但这里一次 s-jump 的 storage 不是一个 edge，而是 width `2^s` 的 conjunctive premise set。

## 9. Exact full-closure depth law

reusable full closure 必须把所有 internal nodes 都推出，而不是只要 root answer。

对所有 node heights 取 worst case，得到：

`D_full(h,s)=floor(h/s)+max(s-2,h mod s)`。

所以一个为 root readout 优化的 presentation，不一定为 complete reusable state 优化。

## 10. Giant root macro：sharp readout/state split

取 s=h。

只新增一条 macro：全部 `2^h` leaves 直接推出 root。

资源：

- extra rule count1；
- macro premise width `2^h`；
- root depth1；
- complete closure depth `h-1`。

因此一条 giant rule 可以让 declared root answer 立即得到，却几乎没有解决其余 reusable internal-state derivation。

这是 multi-premise 系统中

`readout shortcut != executable-state shortcut`

的 sharp witness。

## 11. Height-8 resource surface

exact points：

| span | total rules | total premise literals | max width | root rounds | full rounds |
|---|---:|---:|---:|---:|---:|
| 1 | 255 | 510 | 2 | 8 | 8 |
| 2 | 382 | 1018 | 4 | 4 | 4 |
| 3 | 318 | 1014 | 8 | 4 | 4 |
| 4 | 286 | 1006 | 16 | 2 | 3 |
| 8 | 256 | 766 | 256 | 1 | 7 |

span8 比 span4 的 total rules 与 total premise incidences 都更少，却拥有16倍 max fan-in，并且 full-state continuation depth 明显更差。

所以任何单一 storage scalar 都会丢失真实 tradeoff。

## 12. Root frontiers 都是真正 minimal premises

对 root，取它正好向下 s 层的全部 descendants，一共有 `2^s` 个。

这个 frontier 足以 derive root；移除任意一个 frontier atom，就会缺失一个必要 subtree，root 不再可导出。

因此每个 level frontier 都是同一个 root 的 inclusion-minimal premise set。

premise widths 覆盖：

`2,4,8,...,2^h`。

所以仅一个 conclusion 就天然拥有很多 rooted-circuit premises，而且宽度与 execution meaning 完全不同。

## 13. Rooted circuits 与 presentation resources

rooted circuits 记录 one-round conclusion access 的 minimal premise sets。

AND tree 解释了为什么该对象会比 local Horn basis 大得多：

- local rules 描述 law 如何 composition；
- rooted circuits 枚举“哪些 minimal premises 能一轮给出 conclusion”；
- macro presentation 只选择性缓存其中一部分 derived frontiers，用 storage 换 execution depth。

三者不能混成同一个“rule set”。

## 14. 从 graph spanner 到 hypergraph shortcut

unary chain TC-spanner 优化 sparse edges 与 path-length diameter。

Horn shortcut 则需要优化 hyperedges 与 min-max derivation depth，同时把 premise width / fan-in 纳入 cost。

下一自然对象应当是 Horn proof DAG、AND/OR circuit、hypergraph shortcut 与 multi-premise macro system，而不再只是 ordinary graph spanner。

## Owner-local assets

- `stage131_horn_hyperedge_presentation.py` / tests；
- `stage131_horn_resource_surface.py` / tests；
- `STAGE131_HORN_HYPEREDGE_PRESENTATION.{en,zh}.md`。

## Prior art / status

Horn forward chaining、hypergraph、AND/OR derivation 与 proof DAG 都是标准既有数学/CS。Enterprise Math 的项目价值是 Stage131 semantic-basis 与 hyperedge-presentation resource routing。

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。