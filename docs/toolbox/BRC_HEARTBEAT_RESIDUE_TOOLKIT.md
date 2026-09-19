# 心跳世界 BRC 余数、可证合并与接触观察工具包

状态：`EXTRACTED_EXECUTABLE_CANDIDATE / LOCAL_VALIDATED / NOT_FOUNDATION`
日期：2026-09-20
归属：`T0_BRC`；复用已有预测划分模块，不新建顶层工具族。
定理清单：[THEOREM_LEDGER.json](../../research_notes/heartbeat_brc_library_20260920_AD0416/THEOREM_LEDGER.json)
证明与实验：[RESEARCH_NOTE.md](../../research_notes/heartbeat_brc_library_20260920_AD0416/RESEARCH_NOTE.md)

“心跳世界”仍指进取原生 X6 六轴离散空间加单独类型的一维时间。此包操作的是相对某个实际 Cell 的六个有符号整数位移，不是最终非负 Cell 地址；余数、剩余时限、接触状态不增加空间轴。倍率2、模4、某个周期只是实验参数。

## 工具选择

| 需求 | 接口 | 保留什么 | 不承诺什么 |
|---|---|---|---|
| 分支依赖有限余数，余数分区在后续作用下封闭 | `ResidueLayout`, `ResiduePacket` | 入口/出口余数、时间、权重与仿射作用对应 | 任意占用反馈、全部路径身份 |
| 判断几个通道可否合并 | `certify_port_quotient`, `refine_port_partition` | 指定后续算子族的作用直方图或二阶矩传递 | 任意未来操作都安全；全部表示中的最小内存 |
| 合并后精确传递分布矩 | `QuotientMomentPacket` | 各保留类别的总权重、一阶矩、二阶矩 | Cell 占用、最高分、过去的碰撞历史 |
| 两个带标签位置在剩余 h 个单位相对步内的接触观察 | `ContactState`, `contact_push` | 可在时限内分辨的相对位移，远区 FAR，递减时限 | 多体排斥模型、同步两步、速度未知、无界时间有限状态 |

工具位置：

- `src/enterprise_math/brc_residue_port.py`：原研究模块逐字节提取。
- `src/enterprise_math/brc_residue_quotient.py`：本轮新增合并证书与二阶矩执行器。
- `src/enterprise_math/brc_contact_horizon.py`：本轮新增有限时限接触观察适配器。

原生工具索引采用两个 `research_method_inventory_addenda/*.json` 条目。既有 `tools/enterprise_toolbox.py` 自动加载 addenda，无需新建路由器或改写大注册表。条目的候选状态不授予独立审查、Working Truth 或 Foundation 状态。

## 使用示例：先证明可以合并，再计算

```python
from enterprise_math.brc_residue_port import ResidueLayout, block_swap, fiber_moments
from enterprise_math.brc_residue_quotient import refine_port_partition, QuotientMomentPacket

layout = ResidueLayout((4, 1, 1, 1, 1, 1))
f = block_swap(layout, axis=0, scale=1, origin=0)
g = block_swap(layout, axis=0, scale=2, origin=1, start=1)
cycle = f.then(g).then(f.at(3)).then(g.at(4))  # 实际耗时6，不是免费跳跃
classes = refine_port_partition((cycle,), mode="moment2")
# 得到余数 {0,3} 和 {1,2} 两组。
compiled = QuotientMomentPacket.compile(cycle, classes)
point = (1, 0, 0, 0, 0, 0)
state = compiled.aggregate(fiber_moments(layout, {point: 1}))
state = compiled.apply(state, start=0)
# 此证书只覆盖 cycle。换成 f 或 g，必须重新检查；不能继承旧证书。
```

`effects` 模式比较目标类中的完整“正权重—仿射作用—重数”直方图；`moment2` 模式只比较其28×28二阶矩算子。后者允许更强压缩，但不能冒充前者。

## 使用示例：有限时限相遇

```python
from enterprise_math.brc_contact_horizon import ContactState
s = ContactState.from_pair((0,0,0,0,0,0), (1,0,0,0,0,0), remaining=2)
assert not s.contact
s = s.advance((-1,0,0,0,0,0))  # 相对位移改变一格
assert s.contact
```

两个输入来自同一次随机选择还是独立选择，必须由实际联合分支提供；不能从两个边际分布擅自构造配对。

`FAR` 表示当前指定时限内不可能到达接触点，不表示位置为零、分支不存在或信息被物理销毁。它不能被解码回任意精确远处位置。若要增加时限，必须回到完整状态重新编码，不能凭空从 FAR 恢复细节。

每拍允许两个粒子各走一步时，相对速度上限改变；本工具会拒绝把长度2的相对步当作一个单位步。粗交换必须展开成已声明的原始步及方向/剩余步数状态，不能略过这些约束。

## 验证

```bash
PYTHONPATH=src python tests/test_brc_heartbeat_toolkit.py
python tests/verify_residue_port.py  # 仅独立bundle中的原研究回归入口
```

新12组检查与旧13组回归分别记账。旧13组不是本轮新发现。没有独立数学评审、Lean证明、全仓库集成、生产Nollm执行或语义效果评测。

## 发布边界

当前包是可应用于项目的增量候选工具库，不是 `enterprise-math main` 的完整克隆。GitHub只读能力下必须保留 `REMOTE_PENDING`；本地提交与上传Drive都不能替代GitHub主干读回。包内发布计划携带新增路径和字节哈希，应用前检查现有路径，拒绝覆盖并发作者的不同内容。
