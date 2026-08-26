# E001/E002 — 预测 Boolean 接触桥

状态：`ACTIVE CROSS-ROUTE ENGINEERING NOTE`  
范围：E001 coarse-contact 候选在单方向 gap 运动下，由 E002/P023 预测商编译  
依赖：E001 `Contact_d(g) iff g<d`；E002 第六阶段有限预测商编译器

## 1. 目的

E001 此前已经发现：当前 coarse contact bit 一般并不 future-sufficient。两个正 gap 细节现在都可能满足 `g<d`，但在同一个 gap 更新后产生不同 contact 结果。

本桥把这个反例提升为精确的 horizon-indexed 结果。它**不**定义 rebound、材料响应或完整碰撞动力学。这里的未来观测语言只有

`CONTACT / SEPARATE`。

## 2. 从 contact fiber 向外分离

固定 contact 精度 `d>=1` 与一个正 separating step `a>=1`：

`g -> g+a`。

对当前 contact gap `0<=g<d`，定义首次退出 sample

`tau_out(g) = ceil((d-g)/a)`。

在所有早于 `tau_out` 的 sample 上 contact 仍为真；从 `tau_out` 开始为假。

对 horizon `h`，所有晚于 `h` 的退出时间统一属于一个终端未来类别。因此最粗 predictive rank 为

`rho_out,h(g) = min(tau_out(g), h+1)`。

整个 coarse contact fiber 内的精确类别数为

`C_out(h) = min(h+1, ceil(d/a))`。

任意未来下的 Boolean-contact 类别数因此为

`C_out(infinity) = ceil(d/a)`。

所以原来的 `d` 个 fine integer gap 对这个 query 并不一定都要保留。当 `a=1` 时，任意未来 contact history 最终会暴露每个 gap；当 `a>=d` 时，所有当前 contact gap 都在下一 sample 退出，因此即使看任意未来，整个 contact fiber 仍只有一个 predictive class。

## 3. 从 separated shell 向内闭合

现在固定一个 separated shell：

`g=d+j`, `0<=j<R`,

以及一个正 closing step：

`g -> max(0,g-a)`。

首次进入 contact 的 sample 为

`tau_in(j) = floor(j/a)+1`。

对 horizon `h`，最粗 predictive rank 为

`rho_in,h(j) = min(tau_in(j), h+1)`，

而宽度 `R` 的 separated shell 中，精确 predictive 类别数为

`C_in(h) = min(h+1, ceil(R/a))`。

任意未来类别数为

`C_in(infinity) = ceil(R/a)`。

所以同一个 Boolean 边界两侧具有相同的有限 horizon 结构：最小状态就是一个 capped first-boundary-crossing time。

## 4. 与旧 E001 反例的关系

取 `d=3`、separating step `a=1`、horizon 1。

`g=0` 与 `g=2` 当前都属于 coarse contact。一步更新后：

- `0 -> 1` 仍 contact；
- `2 -> 3` 变为 separate。

所以当前 contact bit 在 horizon 0 时只有一类，但一旦声明一步未来，就必须分成

`C_out(1)=min(2,3)=2`

类。

这正是此前 E001 future-sufficiency 失败，现在被嵌入一个完整类别数定律。

## 5. 编译器重建

通用第六阶段编译器只获得：

- 一个有限 gap state set；
- 一个饱和 separating action `g -> min(G,g+a)`；
- observation `g<d`；
- 已声明 horizon。

它并不知道上面的闭式。

测试要求：在有界整数域上，编译器与初始 contact fiber 相交的 block 数必须精确等于

`min(h+1, ceil(d/a))`。

稳定编译器 block 数必须等于 `ceil(d/a)`。

所以该桥是预测商编译器的跨域证伪测试，而不是碰撞领域自己复制一套 future-sufficiency 逻辑。

## 6. 精度依赖 query，但并非任意

对 Boolean contact 未来，保留坐标可以缩成 capped boundary-crossing time，它可能远小于完整 gap detail。

但这**不**意味着所有碰撞问题都可以删除 gap 信息。

如果未来 response law 还读取任何附加状态，例如：

- 精确 penetration/clearance；
- impact phase；
- velocity 或 momentum；
- material/deformation state；
- response direction 或 rebound magnitude；

那么已声明未来语言更丰富，必须重新编译。这里证明的 Boolean-contact quotient 只对 Boolean-contact language 安全。

## 7. 工程解释

该结果给有限世界引擎提供一个实际规则：

1. 先声明 collision query 与未来 motion language；
2. 编译或推导该语言下的最小 predictive state；
3. 只有当未来操作真正读取完整 gap/position detail 时才保留它；
4. 当声明的 horizon 或 response language 扩大时再 refinement。

对单方向 gap 运动，精确闭式可以避免枚举每个 fine gap：

`fine gap -> capped time-to-contact-boundary`。

这是 task-relative state compression，不是声称 physical gap 对所有可能未来操作都不再存在。

## 8. 可执行资产

- `src/enterprise_math/predictive_contact.py`
- `tests/test_predictive_contact.py`
- `experiments/e001_e002_predictive_contact_probe.py`

测试会独立比较闭式与直接 Boolean future signature，并与通用有限预测商编译器交叉验证。

## 9. 下一批压力测试

1. 同时允许 closing 与 separating action，推导任意 motion word 下的 predictive partition；
2. 加入 response bit/rebound state，测量超出 contact alone 后精确需要增加多少精度；
3. 从 scalar gap 提升到 vector position，但只观察 pairwise collision predicate；
4. 将 compiler-generated collision quotient 与 E001 手工 contact/carry summary 比较；
5. benchmark compiled Boolean-collision state 与完整 fine-coordinate simulation。
