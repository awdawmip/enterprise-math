# R695 → R696 接续：S₆ 协变四分支的最小端口修复

日期：2026-11-10。母任务 `RS-X6-TRIADIC-CLOSURE-DYNAMICS` / `TP2-8B7E13C5904A2D6F1142`。真实 Researcher-ID `EM-X6-4CD0A8`；Activity `RA-D3A13475811F6BBB37DEA88B`。科学源保持 `a72226e2430ffa4786321ac86e7f0c599d5f0389` 与 R462 pin `18783e01e3646c72b7aab3b16d3f565e83e6446f`。

**已证：** R695 使用仅含两力有符号轴标签的输入，得到非空协变第三轴补全最少4支（每种第三符号）；R696 让附加端口许可状态 `A⊆I\{i,j}` 随 S₆ 协变变化，则每个非空 A 唯一的规范化 BRC 核是在允许第三轴上等权 `1/|A|`，空集为 HALT。16种完整许可子集给出16个不同的带标签后继核（含 HALT），精确最小编码4位；在仅允许单元素许可的确定性族中需要4个状态（2位），实现最小的协变选轴。R696 通过全部30×16×720=345600个群作用核配置检查，验证标记 `R696_S6_PORT_MASK_KERNEL_EXACT_PASS`。

**来源和执行：** `R695_PROOF.zh-CN.md`、`R695_VERIFY.py`、`R695_EVIDENCE.json`、`R696_PROOF.zh-CN.md`、`R696_VERIFY.py`、`R696_EVIDENCE.json`；`python R695_VERIFY.py && python R696_VERIFY.py`。都是精确整数/分数，无浮点与随机性。当前属于作者侧候选组合证明，尚未将 A 对应到真实原生 V29/V39 动力学、没有独立 Driver 审核或正式 Result。

**下一最小单元：** 查阅冻结的真实 X6 Link/Port 占据与许可接口，给出实际可执行的 `A(z,ports,M,j)` 及其逐事件更新，不预先假定抽象掩码可独立取全部16态。核验协变、三非零力闭合 `TRIADIC_CLOSURE_E`、V29 守恒账本、V39 有来源的回路流和 BRC 未来观察充分性。若实际许可限制 A 的取值，按原生可实现的子族重新分类。

**控制：** 原生 dispatch 于 2026-11-10T13:23:10Z 给出 `CLAIM_NEW_OWNER`、Owner=`taskbook/unassigned`；本研究目前只完成作者侧项目 GitHub 持久化和会话/活动 Source 登记，不声称正式 CLAIM/Result/Review 或活动语义 checkpoint。
