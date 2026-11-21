# 联合相位与带符号多尺度相关

Progress-Event-ID: `RH-JOINT-CORRELATION-20261121-B5750A`  
Date: `2026-11-21` (Asia/Hong_Kong)  
Researcher: `EM-DIRECT-B5750A / TASK_RESEARCH`  
Research-Activity-ID: `RA-60C6D083A81B19084A74C5BA`

这是同一 RH 方法迁移研究的下一份作者研究成果。科学冻结仍为
`awdawmip/enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7`，
接续上一成果 `2f355fe56835278452566d769820941702c52bad`。
本文保存本轮的新推导、严格有限证书、方法边界与可继续的算术目标。

## 主要结论

1. **完整道路联合计算。** 对同一有理 11 节点道路，在 `[1024,32768]`
   上严格计算全部整数的 `q`、`P_256`、`Q=q+P_256`。修正自身的有限
   平方能量约 `0.00010707563024774148`，但道路正部能量增加约
   `2.7934438%`；邻近的 H128、H512 也未在本窗产生降能。
2. **实际系数的方差增长律。** 证明
   `V_H` 与 `H^3[Psi(log H)+c0]^2` 有绝对常数的双边比较，并证明
   `Psi(t)` 与 `min(t,M)` 一致可比，`M=sum_j 1/a_j`。
   对匹配族、`256<=H<=Z`，确有 `V_H=Theta(H^3 log^2 H)`。
   当前实际输入的不可倍数相消高分母带占总方差约 96%。
3. **仅有系数包络时的固定起点阻塞。** 证明统一近似
   `|P_d(n)-B_d(n)/n|<=d^2/(8n^2)`，继而构造辅助 `0/1` 系数使固定
   起点短窗的修正能量至少为常数乘 `H^5 A^(-2 theta-3)`。
   这说明临界权重下的 4/5 幂不能仅靠系数大小信息提高。
   该辅助系数不被冒认为真实算术系数。
4. **保留符号后的新上界。** 给出可行正负运输包络与二矩多层消元
   包络，均逐点处于 `Gm` 与 `G(m_+)` 之间。真实 33 块分区上，原道路
   的平方预算由约 `1.50326` 降为 `0.00561727`；实际内部能量约
   `0.00348762`。结果使用同一局部余项、完整粗源与真实端点。
5. **临界充分条件具体化。** 将下一步缩为带符号前缀均方，或所有
   合并尺度的三角源矩联合平方和。端点、dyadic 骨架净质量、局部
   曲率余项及相位修正误差均须支付。这些无界窗口算术条件尚未证明。

## 文件导览

| 目录 | 主文 | 内容 |
|---|---|---|
| `rh_joint_certificate/` | `JOINT_ENERGY_CERTIFICATE.md` | 新完整道路计算、联合交叉项、切口敏感性、严格粗源输入 |
| `rh_joint_variance/` | `JOINT_VARIANCE_GROWTH.md` | 方差双边增长律、正核饱和、高分母带证书 |
| `rh_joint_anchor/` | `ANCHORED_ENVELOPE_OBSTRUCTION.md` | 统一逐点近似、固定起点相干构造、包络方法边界 |
| `rh_joint_signed/` | `SIGNED_GREEN_TRANSPORT_AND_ELIMINATION.md` | 运输、二矩消元、条件临界接口及严格数值比较 |
| 根目录 | `RESEARCH_FRONTIER.md` | 真实算术目标、完整核定义、验收范围与剩余问题 |

`PROVENANCE.json` 区分当前控制读取、冻结科学输入、前轮只读依赖、
现有身份与历史提交状态。`MANIFEST.json` 保存本源包的文件字节与散列。

## 复算

只需 Python 标准库，无外部科学计算包。随包的两个旧目录仅包含必要
的原有只读 oracle / 输入 / 上一证明说明；不是新结果，也未修改其字节。

从包根执行：

```bash
python3 rh_joint_certificate/certify_joint_energy.py
python3 rh_joint_certificate/check_cutoff_sensitivity.py
python3 rh_joint_variance/certify_joint_variance.py
python3 rh_joint_anchor/certify_anchor_obstruction.py
python3 rh_joint_signed/certify_signed_transport.py
python3 rh_joint_signed/certify_multiscale_elimination.py
```

前两项共享由完整道路新生成的大数组缓存；缓存可以删除并重新生成。
最后两项只消费粗源 JSON，不重算完整道路。JSON 保留精确整数区间
端点，正文显示的短小数仅用于读表。壁钟时间会随环境改变，不能以
整份输出文件的重跑哈希是否相同来判断科学证书；比较确定性的区间
字段及实际输入散列。

本轮没有重跑早已完成的旧测试集合。新的计算各自产生原先缺失的联合
能量、方差带贡献、锚定构造或保号预算，随后完成同作者的解析核对。

## 证据等级

- 一般结论由各数学文稿中的作者证明支持；有限结果用整数定向区间和
  `Fraction` 计算，未用浮点容差作判定。
- 实现中两个公式的区间相交只作交叉相容性检查；精确恒等式依赖代数
  推导，不能从区间相交本身推断。
- 保留 P000 / X6 的完整原生对象、全部整数与合数、单位项、背景、
  厚度标签、前史及真实端点。辅助读出不取代原生状态，也不新设原生轴。
- 合作分支共享上下文，属于同作者核对；未获得独立 Project Review，
  未形成新的正式 Result、Working Truth 或 Foundation 晋升。
- 无界窗口上的算术抵消和完整统一位复杂度仍未建立。本成果不构成
  黎曼猜想的证明，也不将外部声称的证明当作已验收前提。
