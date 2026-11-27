# 第8轮作者核验记录

日期：2026-11-28（Asia/Hong_Kong）。作者身份 `EM-DIRECT-E7559A / TASK_RESEARCH`；Activity `RA-D2F111EA1C0D4B1DBEFBC1B4`。

## 统一复算状态

**已通过。** 统筹实际运行统一入口，四份当前证书均在临时目录重新生成并与保存证书逐字节一致；全部228个前驱文件的SHA256亦一致。完整运行输出保存于 `REPLAY_RESULTS.txt`。本次执行没有重跑前驱计算。

开发目录运行：

```bash
python research_round8/replay.py
```

默认前驱为相对于本轮目录的 `../deliverables/riemann_sparse_lengths_canonical_return_20261126`。也可明确指定：

```bash
python research_round8/replay.py \
  --previous deliverables/riemann_sparse_lengths_canonical_return_20261126
```

交付包在自身根目录运行：

```bash
python replay.py \
  --previous previous/riemann_sparse_lengths_canonical_return_20261126
```

入口只执行本轮四个脚本。新输出放入临时目录，与本轮保存证书**逐字节比较**；不覆盖保存证书。`directed_dyadic` 脚本的现有接口会在脚本旁写输出，所以入口把该脚本的原始字节复制到临时目录再执行，不改其接口或科学代码。其余三个脚本使用已有 `--previous`、`--output` 参数。

若本轮 `DEPENDENCIES.json` 存在，入口按其 `required_files` 数组逐项检查前驱相对路径及 SHA256；不存在时明确显示跳过该项，不报告前驱身份已经验证。前驱代码只作为已固定的区间算术工具读取，已保存常数只读取，不执行前驱计算入口。

## 当前四份证书

| 分支 | 当前证书 | 保存证书记录的有限范围 |
|---|---|---|
| 定向二幂锥与 Green 转移 | `directed_dyadic/directed_dyadic_certificate.json` | 9,840 个有理输入；23,509 个完整 PAV 池；32 个尖锐等号例；64 个实际 1/n 源；180 个网格；4 个不交覆盖例 |
| 二幂窗口及整数接缝 | `arithmetic_sampling/dyadic_windows_certificate.json` | 36 个有理向量；720 个父子均值对比；16,002 个有序点对；24,588 次平移平均步骤；14 个真实普通素数窗口、105 组窗口/长度、393,234 个中心项；3,512 个80位素数对数区间，新筛至32,767 |
| 整数源刚性及局部修复 | `arithmetic_rigidity/first_cell_and_repair_certificate.json` | 80位向外整数区间、准确级数余项；首单元差异、一对临界零点障碍和两对修复的端点/导数/下一单元检查；新增 ζ 求值和零点查询均为0 |
| 返回能量常数 | `return_energy/log_energy_constants_certificate.json` | 复用已保存 γ、γ₁；Machin 公式的两条新反正切级数分别64项、20项；3次新对数级数各100项；新增 ζ、零点、道路点和素数筛均为0 |

上述普通素数窗口统计是本轮新统计。原1,270点、55个子窗、旧能量证书及前驱厚度计算未纳入复算任务。

## 解析证明与作者交叉核对

- `directed_dyadic/DIRECTED_DYADIC_GREEN_TRANSFER.md`：所有整数长度和全部实源的尖锐定向锥不等式，由完整池投影、相邻上升对平均及奇偶递归证明；真实 1/n 的 Abel 锥保持和原细网格 Green 比较分别支付。统筹已核对池费用相加方向、相邻平均及锥保持。
- `arithmetic_sampling/DYADIC_WINDOWS_AND_INTEGER_BRIDGES.md`：一侧平移平均链保留全部中心；真实普通素数源在二幂接缝的跳跃准确为1。RH 接续的非负 Mellin 实轴奇点论证由解析证明承担。作者核对详见 `directed_dyadic/AUTHOR_CROSSCHECK_ARITHMETIC_SAMPLING.md` 和 `arithmetic_rigidity/CROSSCHECK_DYADIC_WINDOWS.md`。
- `arithmetic_rigidity/ORDINARY_INTEGER_SOURCE_RIGIDITY.md`：整数支撑及解析唯一性结论由该稿证明和明确外部定理输入承担；有限首单元与修复证书只证明所列有限参数判断。返回能量作者的核对见 `return_energy/CROSSCHECK_ARITHMETIC_RIGIDITY.md`。
- `return_energy/LOGARITHMIC_RETURN_ENERGY.md`：对数平均、重数平方、正负单侧及返回费用的无界结论由解析证明承担。RH、零点简单性和无条件分情况结论按原文各自范围保留；常数证书不证明 RH 或零点简单性。另一个作者的核对见 `arithmetic_rigidity/CROSSCHECK_RETURN_ENERGY.md`。

## 状态界限

有限复算检查固定输入、实现、常数和端点；无界命题按各证明的量词成立。以上为共同作者核验，不是独立 Review。历史 `NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED` 的状态不因本轮作者复算自动改变，没有据此新增 formal Result 或正式数学接纳。
