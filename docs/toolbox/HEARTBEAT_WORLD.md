# 心跳世界工具与定理库

状态：EXTRACTED_RESEARCH_LIBRARY_NOT_FOUNDATION。此次提取聚焦最新的“非周期切换进位→自动格闭包”研究段，不宣称覆盖项目全部历史成果。

[机器目录](../../research_toolkits/heartbeat_world.json)动态引用原工具登记和原定理台账；既有2个工具的17个接口与12项候选结论不另起编号、不复制成新的数学定理、不提升接纳等级。

| 需求 | 既有方法 | 入口和保证 |
|---|---|---|
| 已有格基，检查所有允许路径是否受控 | `t0.brc_switching_carry_lattice_ports` | `certify_lattice_ports`；保留有符号欠账，检查有限格端口；线性进位界不等于位移或质量界 |
| 未知格基，寻找共同结构并输出失败路径 | `t0.brc_common_lattice_search` | `find_common_lattice`、`find_phase_lattice`；返回格证书、真实预算越界词或SEARCH_LIMIT |

## 提取的候选结论

SW-001：非周期同均值斜率与无界欠账可以并存。
SW-002：限定U/V族中，时间与有符号欠账充分；Smith类型不保留方向。
SW-003：有限格端口给出不依赖合法路径长度的进位界。
SW-004：整数平均归一化时，共同不变格与全词有界等价。
SW-005：公平随机分支均值为零但均方欠账增长。
SW-006：三端口还账反馈允许非周期分叉下的整对平衡。

LS-001：最小可达格闭包。
LS-002：给定深度R的6R+1轮判定与真实路径反例。
LS-003：六个实际路径列保持格生成与反例来源。
LS-004：最多六个行列式余数相位，稳定包含成为双射。
LS-005：任意有限整数动作族、不受限切换时，全词进位有界与相位格族等价。
LS-006：q相位时6qR+1轮的有限预算界。

完整ID使用`HBW-SW-...`和`HBW-LS-...`。假设、证明段落和测试均由原台账解析，不能只引用本页简称。SW-004的适用范围由LS-004/005扩展，但保留旧证明和编号。

## 可运行入口

```sh
python tools/heartbeat_world_library.py tools
python tools/heartbeat_world_library.py theorems --query HBW-LS-005
python tools/heartbeat_world_library.py priority
python tools/heartbeat_world_library.py validate
PYTHONPATH=src python tests/test_heartbeat_lattice_search.py
PYTHONPATH=src python tests/test_heartbeat_switching_carry.py
```

`validate`只核对引用、ID、源文件摘要、接口语法与证明字段，不代替数学审稿或实测。`theorems`保留原记录；目录提取不是新证明。源版本发生变化时摘要检查会要求重新确认，不能把旧检验当作新版本的证明。

入口工具是只读目录解析器，不是新BRC数学族，也不分派任务。遵守[一级优先研究指令](../HEARTBEAT_WORLD_RESEARCH_PRIORITY.md)；维护任务所有权和FREE信息隔离。
