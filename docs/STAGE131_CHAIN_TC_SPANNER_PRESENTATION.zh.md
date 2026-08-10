# Stage131 — Source-Dependent Chain Shortcuts 作为 TC-Spanner Presentation

状态：`RESEARCH BRIDGE / NONCANONICAL`

translation-invariant jump-length model 只是一个受限 presentation class。一般 chain rule presentation 可以在不同 source positions 选择不同 transitive shortcuts。

这会继续扩张 storage/inference-depth frontier，并与标准 transitive-closure spanner 问题直接对齐。

## 1. Unrestricted exact chain presentation

对 chain vertices：

`0<1<...<n`，

semantic closure 包含所有 directed pairs：

`i->j`, `i<j`。

一个 exact stored presentation 可以从这些 transitive edges 中选择 subset E，只要最终 reachability relation 仍然是同一个 total order。

每个 adjacent edge

`i->i+1`

都被强制保留：中间不存在别的 vertex 可以替代该 comparable pair 的 reachability。

其余 edges 都是 optional execution shortcuts。

## 2. Storage 与 reusable inference depth

storage 就是：

`|E|`。

对任意 comparable pair `i<j`，记 `dist_E(i,j)` 为 stored graph 中最短 directed path length。

reusable worst-case inference depth 定义为：

`diam(E)=max_(i<j) dist_E(i,j)`。

这比只问 `x_0->x_n` 更强：它保证从**任意** chain premise 出发都能在 bounded rounds 内完成相应 closure。

对 translation-invariant jump set，diameter 正好退化为 parent coin-count depth，因为 shortest path 只取决于 distance `j-i`。

## 3. Exact TC-spanner identification

若 stored chain presentation 满足：

`diam(E)<=k`，

那么它就是标准 graph terminology 中 directed path / total-order closure 的 k-transitive-closure spanner。

因此 unrestricted Stage131 shortcut problem 不是新的 generic graph optimization 问题；它是标准 TC-spanner structure 在本项目 precision / presentation 语义下的重新解释。

## 4. Translation-invariant jump set 是 strict subclass

parent generation 只要选择 jump type ell，就会在**所有**合法 source positions 存同样 shortcut。

unrestricted presentation 可以只在真正有用的位置保留某条 long shortcut。

因此 source-dependent storage 可以严格改善 frontier。

## 5. One-shortcut exact diameter

从 n 条 adjacent edges 出发，再加一条 shortcut：

`a->b`, `b-a>=2`。

resulting diameter 精确为：

`D(a,b)=max{ b-1, n-a-1, n-(b-a)+1 }`。

三个 terms 分别表示：

1. `b-1`：终点位于 b 之前的 pair 无法使用 shortcut；
2. `n-a-1`：起点位于 a 之后的 pair 无法使用 shortcut；
3. `n-(b-a)+1`：跨越 shortcut 的最长 pair（例如0->n）只节省 `(b-a)-1` hops。

没有其他 pair 会更差。

## 6. Optimal one-shortcut theorem

假设希望 `D(a,b)<=d`。

closed formula 强制：

`b<=d+1`，

`a>=n-d-1`，

并要求 shortcut length：

`b-a>=n-d+1`。

前两条又给出：

`b-a <= 2d-n+2`。

所以必须：

`2d-n+2 >= n-d+1`，

即：

`3d >= 2n-1`。

因此任何 one-shortcut presentation 都满足：

`d >= ceil((2n-1)/3)`。

该 bound 可达到。取：

`d*=ceil((2n-1)/3)=floor((2n+1)/3)`，

`a=n-d*-1`，

`b=2n-2d*`。

则三个 diameter terms 全部 <=d*。

所以总共 n+1 条 stored rules 时的 exact optimum 是：

`D_one(n)=floor((2n+1)/3)`。

executable layer 对大量 n 与 brute-force shortcut placement 做交叉验证。

## 7. 最小 strict improvement over translation-invariant jumps

取 n=5。

### Unrestricted one-shortcut presentation

存五条 adjacent rules，再加：

`1->4`。

storage6，diameter3。

### Translation-invariant presentation at storage6

parent exact frontier 只有 `(6,4)`，没有 `(6,3)`。

所以同样 stored-rule count 下，source dependence 已经严格改善 frontier。

## 8. Exact small-n unrestricted frontiers

branch 枚举 n<=6 的全部 optional shortcuts。

Storage/diameter pairs：

### n=3

`(3,3), (4,2), (6,1)`。

### n=4

`(4,4), (5,3), (6,2), (10,1)`。

### n=5

`(5,5), (6,3), (8,2), (15,1)`。

### n=6

`(6,6), (7,4), (8,3), (10,2), (21,1)`。

与 translation-invariant parent 对照，n=5 开始就出现 strict saving。

## 9. n=1024 one-shortcut scale

adjacent basis：

1024 rules / diameter1024。

只增加**一条** source-specific shortcut，总 storage=1025 rules，exact optimal diameter 立即变成：

`floor((2*1024+1)/3)=683`。

constructive formula 会给出一条 explicit optimal shortcut。

反过来，translation-invariant jump-type family 若总共也只能多一条 positional rule，就只能选择 `{1,1024}`：它只帮助 endpoint，depth 仍是1023。

所以 source-local placement 本身就是 precision resource。

## 10. 与 richer jump families 的关系

一条 source-specific shortcut 只给 constant-factor diameter improvement。

parent two-length / geometric / binary families 会在多个 source positions 复制 useful scales，因此用更多 storage 换来更低 depth。

unrestricted TC-spanner class 可以同时结合两种思路：

- 选择多个 scales；
- 非均匀地放置；
- 只在需要位置保存 shortcuts。

这才是 Stage131 presentation optimization 的更大 search space。

## 11. Semantic interpretation

所有 shortcuts 都是 adjacent chain 的 semantic consequences，它们只服务 presentation/execution efficiency。

因此 chain 现在显式出现三层：

1. **semantic basis**：adjacent edges；
2. **restricted execution presentation**：global jump-length families；
3. **unrestricted execution presentation**：source-dependent TC-spanner shortcuts。

向外扩 representation class 会改变 storage/depth possibilities，但不会改变 closure law。

## 12. Rooted circuits 与 TC-spanner presentations

full rooted-circuit / transitive table 是同一 graph family 的 diameter1 endpoint。

adjacent basis 是 minimum-edge endpoint。

TC-spanner presentations 位于二者之间，提供 sparse bounded-diameter points。

因此 rooted-circuit 的“transitive redundancy”更适合解释成 broader exact presentation design space 的一个 extreme，而不是简单删除目标。

## 13. Prior-art boundary

Transitive-closure spanner 是 established graph theory：标准定义就是在 transitive closure 中选择 subgraph，保持相同 reachability，同时让每个 reachable pair 的 directed distance 有界。

Stage131 **不**主张该 generic object 或其算法为新数学。

项目特有映射是：

`TC-spanner edge budget / diameter`

对应

`stored derived implication budget / inference-round depth`，

并被放回 rooted-circuit precision architecture 中。

## 14. 下一前沿

source-dependent formulation 打开了更强问题：

- chain / wider poset 上 diameter k 的 exact minimum edges；
- weighted / nonuniform query costs；
- premise-dependent rule storage cost；
- DAG / circuit sharing 而不是 flat edge storage；
- multi-premise Horn closure 与 hypergraph shortcut；
- 从 observed query workload 动态编译 shortcuts。

这些应主动消费 TC-spanner / shortcut prior art，而不是从零重复推导。

## Owner-local assets

- `src/enterprise_math/stage131_chain_tc_spanner.py`；
- `tests/test_stage131_chain_tc_spanner.py`；
- `docs/STAGE131_CHAIN_TC_SPANNER_PRESENTATION.{en,zh}.md`。

## Prior art / status

TC-spanner、graph shortcut、directed diameter 与 transitive closure 都是标准既有数学/CS。Enterprise Math 的项目价值是 Stage131 presentation-precision 映射与 exact one-shortcut specialization。

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。