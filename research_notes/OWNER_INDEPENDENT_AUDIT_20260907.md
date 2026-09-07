# Owner 独立数学与恢复器审计

Researcher-ID: EM-OWNER-AUDIT-20260907 / TASK_RESEARCH

本文件是 owner 委派的有界独立审核笔记，不是正式 Driver review、task publication、claim、Working Truth 或 Foundation 提升记录。复用 owner 已验证的 `GLOBAL_KNOWLEDGE_V1@ccd838a220b00ad44a7f5375fffeee8aa6afaaa0` 与源快照 `enterprise-math@ef1893382eb1dcfcd773e19882569e9ff072a8ee`。未重启 FREE 发现流程；审核前已经看过冻结候选，故不作独立发现申报。

## 1. 结论与分级

| 对象 | 审核结论 | 边界 |
|---|---|---|
| 一般正/负支点下界与三轴七支点唯一性 | `PROVED_DERIVATION`：归纳有效 | 非负有限空间质量，固定单射坐标，全部有标签 raw 边缘；不是路径/相位/内部状态恢复 |
| 当前 X6 上八对八边缘盲区 | `EXACT_NEGATIVE_OBSTRUCTION` | 四活动轴合法 Cell 矩形；不把复合位移当新原生方向 |
| 四轴 cylinder 的未来操作失败 | `EXACT_FINITE_CHECK + DIRECT_ARGUMENT` | 已声明的总体筛选操作；四状态 T6 载体，不能外推全部 native dynamics |
| complementary join 与有限线性约束归约 | `PROVED_DERIVATION` | 非负性保证无遗漏；候选数不等于原支点数 |
| 当前 `recovery.py` | 有精确验证闸门的非canonical prototype | 不保证第三方 LP 对每个合法输入成功或及时终止；已知可行输入仍可能被拒绝 |
| 新颖性 | `DERIVED_NOT_AXIOM / NO_NOVELTY_CLAIM` | 本审核未作全库或外部穷尽检索；候选自报 trade 先例，不把应用或重述算作新公理 |

数学候选没有发现反例或归纳缺口。工程审核发现并推动修复了可变坐标输入，以及直接等式 LP 返回错误结果的问题。修复后的恢复器对输出实行非负性及全部原始 BRC 边缘表精确复核；这保护证书正确性，但不证明求解器完备性。

## 2. 归纳与七支点条件逐项检查

设有限支持 `f` 在 `A_1 × … × A_n` 上取有理值，所有至多 `k` 轴边缘为零。

1. `k=0` 是总和零。非零且总和零必有正、负项，故每种符号至少一个支点。
2. 对 `k>0`，非零支持含至少两个点，故某个坐标 `j` 至少有两个非零切片。固定 `j=b` 后，每个至多 `k-1` 轴边缘，正好是原 `J∪{j}` 零边缘在 `b` 的切片；没有把整体零和误当逐片零和。
3. 对每个非零切片使用归纳，再以切片支持不相交相加，得到两种符号各至少 `2^k` 个位置。维数随归纳减少仍满足 `k-1≤n-1`。`k=n` 情况的非零前提事实上不可能，不构成反例。
4. 若初始只给恰 `k` 轴边缘，可有限求和取得所有较低阶边缘。即便坐标值域无限，此步骤仍只含有限个非零项。

对任意有限非负竞争分布 `ν`，`f=μ-ν` 的正支点包含在 `supp(μ)` 内。`|supp(μ)|≤7` 与 `k=3` 的正支点至少八个矛盾，因此 `μ=ν`。**未要求 `ν` 同样只有七个支点**。比较对象支持之外作零数组延拓只用于证明，不创造合法 Cell。

有理权重重数不当作新支点：例如同一 Cell 的两条分支权重 `2/3`、`5/7`，空间质量是 `29/21` 且空间支持数为一。这已进入回归测试。差数组中的负号仅用于比较两个正分布；`(-1)^(x0+x1+x2+x3)` 的负读出也只是带符号观察值。二者都不是负物理分支质量。

## 3. 坐标与原生类型

已直接核对 `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` §§2–5。当前前提确为 anchored `AFFINE_TORSOR(Z^6)`，坐标零是所选 Cell anchor，六轴 signed unit steps 合法。故四轴十六点矩形合法；无需宣告它们属于单个三轴 slice，更无需用普通欧氏 90° 解释原生正交。

定理读取的是 raw 三坐标值。等价修复必须保留**同一条读出中的配对数据** `(can3, common_depth)`，不是把两者拆成独立且失去关联的统计表。原生 `can3` 单独减去共同最小值，所有六轴共同加一后仍给相同二十个读出；`0^6` 与 `1^6` 单支点分布已经构成反例。恢复器不能从输入值本身判断调用者是否事先错误地做过 can3，因此 raw 类型是调用契约，不是自动检测能力。

原候选区分了空间中心身份、branch identity 与全部 decorated state；该区分必须保留。即使所有空间质量被唯一恢复，也不能把 branch labels、path history 或时间信息恢复计入结论。

## 4. 观察器与 BRC/T6 实际复用

`observer_certificate.py` 导入并实际执行 `WeightHistogram.from_weights` 及 `total_mass/count/dominant_mass/dominant_degeneracy/prime_valuation_terms`，不是只把工具名写入元数据。完整 weight histogram 相等蕴含其中 CWM 与 valuation readout 相等；它不恢复丢失的跨表 branch 匹配。

对所有三轴选择，四活动位至少有一位未观察；翻转该位给偶、奇两侧纤维一一配对。因此每个三轴纤维单位权重直方图相同。四轴 cylinder `x0=x1=x2=x3=0` 却在偶侧保留一个单位分支、奇侧保留空总体，总质量是 `1` 与 `0`。正值 cylinder 已足以给出未来不下降的证书，不依赖把 signed interaction 当作质量。

T6 调用也是真实执行：有限总体状态为 `{even, odd, origin, empty}`，初始观察三类，筛选是幂等映射。`even~odd` 的像落到不同观察类，故 `operation_descends=False`；`stable_family_partition` 精确细化为四类。最粗稳定性只属于此四状态载体及该映射的重复操作，不能提升为全 X6 上最小修复。

独立于候选自带检查脚本，本审核用直接有限求和检验了十五种活动轴 × 四种 signed 平移/非单位坐标间距，共六十个矩形：三轴表比较 `1200` 次，四轴各地址 cylinder 检查 `960` 次，全部符合结论。另枚举三位二值载体上 `3^8=6561` 个 `{-1,0,1}` 数组，得到三张一轴零边缘的非零数组 `32` 个，两种符号的最小支持均为 `2`。这只是低阶有限校验，不是一般归纳证明。

输入审核曾复现 `Branch('x', coordinate_list)` 在构造后仍随外部 list 修改而变动。owner 已在 `__post_init__` 将其转为 tuple 后验证和固化。当前回归确认该问题修复。分支重复标签、bool 坐标、非整数坐标、非正/float/bool 权重、重复/越界观察轴等常见非法输入被拒绝。

还发现 Python 字典键相等会使 `(False,1,2)` 与 `(0,1,2)` 被原来的集合检查混同。owner 已为恢复器加上轴标签 tuple 与严格 int 类型检查；新增拒绝回归后再次运行全部十三项通过。

## 5. complementary join 与唯一证书正确性

令 `P`、`Q` 分别为三轴 `(0,1,2)`、`(3,4,5)` 的正质量地址集合。任何非负可行 `ν` 的正支点 `z` 都必须满足 `z_P∈P`、`z_Q∈Q`：否则该坐标纤维应为零，却含一个正质量点。六坐标由互补地址对唯一拼合，所以

`supp(ν) ⊆ P×Q`，`|P×Q|=|P||Q|≤s²`

其中最后一个界使用生成分布有 `s` 个不同空间支点，每张边缘最多 `s` 个正地址。再用全部二十张表的正地址筛选只会删去不可能的点，不会删去任意可行竞争分布的支点。

因此在有限候选集上设置 `x_z≥0` 与全部非零纤维质量等式，是精确可行性归约。未显式建立零纤维行并非缺漏：候选筛选已保证没有候选落入任何零纤维。候选预算检查在 join 构造前执行，预算超出明确不作数学无解推断。

RREF 参数化 `x_p=b_p-Σ R[p,j]t_j` 正确，free variables 本身是原始空间质量，故默认 `t_j≥0` 合法。pivot 非负条件是 `Σ R[p,j]t_j≤b_p`，符号没有反转。末列 pivot 是不相容证书；满列秩而唯一线性解有负项也确证无非负解。第三方 LP 自称 infeasible 不被当作这些代数证书。

成功输出先过非负质量检查，再重新构造正 `Branch` 并实际调用 BRC-backed `all_three_axis_tables` 与完整输入作精确相等检查。成功且空间支持 `<8` 时，一般定理给出对**所有有限非负竞争分布**的唯一性证书；`≥8` 仅给 `FEASIBLE_UNIQUENESS_UNCLASSIFIED`，没有误把充分条件的否命题当作歧义证明。

## 6. 第三方 LP 缺陷与保留的限制

在本机 `SymPy 1.14.0` 上，直接等式调用存在可独立复现的错误。最小清晰样例是

```python
linprog([0, 0, 0], [[0, 0, 0]], [0],
        [[1, 1, 0], [1, 0, 1], [0, 1, 1]], [1, 1, 1])
```

真实唯一解是 `(1/2,1/2,1/2)`，实测返回 `(0,1,0)`，第二行残差 `-1`。所以问题不能仅解释为冗余等式：三条等式本身独立。

原七支点 demo 的 `84×11` 矩阵 rank 为 `11`，直接 LP 违反 `55` 行；八支点 demo 的 `88×16` 矩阵 rank 为 `15`，直接 LP 违反 `63` 行。仅选择原独立行仍失败。RREF 后送全部等式能修复这两个 demo，但更大的真实可行输入仍有反例。

owner 当前实现使用：满列秩直接精确解；欠定先检查自由变量零；必要时只让 LP 处理自由质量不等式；全部结果仍精确复核。这个修改使本轮四个 demo 成功，并消除原直接等式调用造成的错误证书风险。

但参数不等式 LP 也不保证成功。固定 seed `2026090709` 的前十四个正质量 binary-six 输入中，十三个通过精确复核，另一个有二十一个单位支点、join `64`、rank `42`，第三方 solver 产生四个负 pivot 质量；当前恢复器正确报 `ArithmeticError('solver returned negative mass')`。其原等式残差本来为零，所以**只查等式而不查非负性也不够**。具体总体固化在测试的 `FEASIBLE_SOLVER_STRESS`。

有限记录见 `research_notes/owner_independent_solver_audit_20260907.json`。十三个通过输入中有三个欠定，自由变量数分别为 `1/3/1`。曾尝试扩展至六十四例，但出现长时间无完成的求解；为保持有界审核已终止该独立 probe，未将该轮计作完成，也不作六十四例统计。这里没有修补第三方库，没有据有限成功宣告普遍终止性或求解完备性。

## 7. 可重跑的精确回归

新增独占文件 `experiments/owner_joint_observer_20260907/test_recovery.py`，实测 `13 tests / OK`：

- 固定 seed `2026090717` 的 `56` 个 signed、非均匀有理、`1–7` 支点输入，全部精确恢复并核对 join≤s²。
- 十五种活动轴各删除偶侧八点中的一个，共 `120` 个七支点边界例，全部精确恢复。
- 八对八同边缘不误给唯一性；can3 深度边界；重复 Cell 聚合；零分布。
- 缺少表、非法地址/质量、等总质量却不相容的方程、预算拒绝的正确分类。
- 可变坐标防护、恶意 LP 参数拦截、LP 伪 infeasible 不被提升为数学无解证书。
- 已知可行的二十一个支点 solver stress 必须返回精确可行解，或明确拒绝未经验证的解；不能返回错误证书或错误无解结论。

本机复现命令（仅当前进程依赖路径，无项目依赖修改）：

```powershell
$env:PYTHONPATH = Join-Path $env:TEMP 'em-owner-math-deps'
python -X utf8 experiments/owner_joint_observer_20260907/test_recovery.py
```

## 8. 审核时对象指纹与权限边界

| 文件 | SHA256 |
|---|---|
| `research_notes/OWNER_FREE_CANDIDATE_20260907.md` | `2FC21DFB799A5183B57E50E44F99D268530B63C8D4B87A965BB8EBFC12E0B7C6` |
| `experiments/owner_joint_observer_20260907/observer_certificate.py` | `93A2F2775EC919BC747FB339C52730F0EBA7DE99BED5DFFBA89A0FD1B1459D4D` |
| `experiments/owner_joint_observer_20260907/recovery.py` | `D9584135A9F20458161096B0901C2DE8CE281B3D27385AC0E2F7C57F3E059395` |
| `experiments/owner_joint_observer_20260907/test_recovery.py` | `959DA81CA43475E7703576EB82AFA631FA6FF6FA49BA4867945D764CDCCBDABE` |
| `research_notes/owner_independent_solver_audit_20260907.json` | `92B924F3BFEEAFEFA8E82FD6696E450FB7BC7C3B512CBA4E7AD37665AB821265` |

本审核仅新增此笔记、独立测试与有限求解记录，未修改他人实现、共享定义、官方 task/claim/review 或研究状态；实现修理由 owner 独立完成。后续归档若对象内容改变，这里的指纹应被视为本次审计快照，不能当成新版本审计覆盖。

Researcher-ID: EM-OWNER-AUDIT-20260907 / TASK_RESEARCH

Global-Knowledge-Sync: main@ccd838a / GLOBAL_KNOWLEDGE_V1

Owner persistence note: files normalized to LF; output writers now request LF explicitly. Root reran all 14 adapter tests and all three certificate programs successfully, then refreshed the fingerprints above. Mathematical content is unchanged.
