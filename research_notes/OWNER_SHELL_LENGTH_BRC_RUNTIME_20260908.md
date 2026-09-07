# 平方壳消费者的 BRC 算术迁移

状态：`LOCAL_RUNTIME_MIGRATION_PASS / INDEPENDENT_FINITE_AUDIT_PASS / TOOLBOX_INTEGRATION_CANDIDATE`。
这是已有候选 `candidate.x6.quadratic_shell_max_shortest_length` 的执行器迁移，不改变其全 N 定理、经典来源、原生 X6 定义或正式采纳状态。

## 已有来源与实际复用

旧执行器固定在本地 `9c8ba08cb82f0d071dfd91c0bdcf17f8220f08c6`，等树远端来源为 `5eddb6ea23761d928197b3d8227a5b42a7975a34`。旧 helper SHA-256 为 `c77bc6342eb5c78072ccea1b70dc0ee90a6dd7676aab4d3de1aa9928c2f67065`。旧证明、独立证明审计、61 例结果 JSON 和原验证器均未改写。

恢复研究时读取了 `exact_arithmetic_runtime_policy.json` V2。其要求实际求商、余数、整除判断和整数根经过 BRC；仅携带未求值的 DIV/ROOT 不触发求值。历史数值资料不会因此自动成为错误定理，但本次新增消费者不能把直接 `Fraction`、`isqrt`、`//` 或 `%` 当成已完成 V2 迁移的原生证据。

实际执行覆盖查询 `exact_arithmetic BRC division root collapse symbolic DIV shell shortest length`，首个可执行模块命中 `module:exact_arithmetic`。复用状态为 `EXTEND_EXISTING_TOOL / REUSE_APPLIED`：直接调用既有 `division`、`root`、`brc_evaluate_division` 和 `brc_evaluate_root`，不新建有理数包装器，不把底层商余或 root primitive 绕接到本消费者。

当前 `src/enterprise_math/exact_arithmetic.py`、`signed_brc.py`、`x6_signed.py` 和算术政策在研究源与已经验证的 main `86a04d17cbffd687b1ef74ab4990cf6b2b7e093a` 之间无差异；这些依赖的文件字节未被本次编辑。

## 计算边界

- 上界的平方根、六轴平衡分解、奇偶与模 8 判断、三平方搜索界、候选平方根、Hadamard 的四整除均经过 BRC facade。
- 原先对负数差值取余的比较改为分别对两个非负整数求余再比较；不把负整数输入自然数 facade。Hadamard 四个分子必须先满足原证明的非负条件，才求非负四分之一。
- 最短词数仍是原 signed BRC 的 multinomial `k! / product(abs(z_i)!)`。先保存整数分子和分母，再用 BRC 商余轨迹证明余数为零。当前证书不再调用旧 `signed_brc` 中直接整除的两个 multiplicity 函数。
- 原 signed endpoint、L1 词长、平方读出、共同深度和二十张可逆联合切片继续使用原坐标与纯整数接口。辅助平衡中心 b 仍不等于原生 common-depth。

原五个 API 的数学返回内容保持原义。新增 `upper_length_evaluation(N)` 显式返回标量上界及轨迹；旧 `upper_length` 仍可返回整数，调用者也可传入 `arithmetic_trace` 列表接收轨迹。独立调用 reduction、construction 和 endpoint verification 时会返回自己的轨迹；组合证书只保存一份共同账本，避免重复嵌套。

完整证书 schema 更新为 `owner_shell_length_endpoint_v2`，增加算术政策、轨迹和 facade 源摘要。轨迹逐条保留输入、商余、坍缩值或根盆地边界。超过 2048 bit 的轨迹整数用 `{encoding: hex, value: ...}` 无损编码；这不是小数近似，不改变解释器的十进制位数限制。

原搜索预算和词数读出预算保持原义。词数超预算或十进制转换受限时仍保留已核验端点和精确 factorial 表达式，不把资源不足报告成数学不存在。轨迹记录有额外线性存储成本；没有声称这项迁移加速搜索或保证快速位复杂度。

## 本地核验

实际运行 `validate_brc_runtime.py`：

- 原 61 个公式分支选例、signed N=25、零壳、输入类型和资源边界通过；选例端点、r/t、common-depth 与词数和冻结旧输出逐项一致。
- 1,641 条 BRC 除法／开根轨迹独立按整数重构关系与盆地不等式核验；改写任一种轨迹的余数都会被拒绝。
- 用拒绝执行的替身守住两个旧 multiplicity 函数，当前被检查的证书路径仍通过，确认没有把直接除法藏到旧依赖中。
- 大整数轨迹可精确 JSON 序列化；6000 事件词数的十进制读出仍报告原资源边界；全局十进制转换限制保持 4300。
- 对 helper 与新增验证器执行现有算术静态 gate：`PASS (2 files)`。静态 gate 不递归依赖，因此上述调用边界审查与动态守卫是独立必要的证据。

验证器只检查本次明确计算路径和单条算术轨迹。它不是任意第三方整份证书 envelope 的认证器，轨迹自洽也不能替代端点与原始输入的绑定或全 N 解析证明。

冻结的新 helper SHA-256：`31c09afd186ecc86d608fdfeb3b014091f22a3b40bcbdc32d568fe0c0db8aa18`。
新验证器：`956126dae579767e65dd9f4f80ab04947a8cc1bdbaa9e34c6e41125dea2a21ec`。
新验证输出：`c4b454f6b84ed774d8471d685106c143ebea98d689c28cf7aba1ae9817d4fae9`。

## 独立审查与可复现包

独立审查未发现实质缺陷。另选未进入旧 61 例的 N=60/61，通过只用整数加法的末轴递推独立得到词数 51459408000 与 651819168000；60 次实际 facade 调用与保存轨迹逐条、按序一致。额外核对负 Hadamard 分子在求商前被拒绝、搜索预算、2048/2049 bit 编码边界及五类坏轨迹拒绝。

可复现包在 `experiments/owner_shell_length_20260907/brc_runtime_independent_20260908/`。`review.py` 支持仓库路径位置参数，默认从包位置定位；历史比较使用公开等树 baseline `5eddb6ea23761d928197b3d8227a5b42a7975a34`，不要求其他读者拥有仅本地的 9c8 提交。最终脚本只重放原两例与错误注入，没有重跑 61 例或新增数学审稿。

包内脚本、实际 JSON、独立报告的 SHA-256 分别为 `013ca7d3cb7f7164a166ddad3cbd80c5b3fc18a00fe88944c37159100a98ab4c`、`9d485a64cc490ce8ee60b502279bdcc82f6dc522e92d1b2b40d30e6175eb788d`、`e12793f3a41eed96afcf12e148075cab59420be170f3ce535614a88d0afdeac4`。发布前补齐了脚本与报告末尾 LF；独审者确认 AST 相同，并在最终脚本上实际重放原两例及边界，JSON 绑定此次真实执行。原 portable 包和旧 TEMP 独审包均原样保留。

目录仍是候选路由；本次审查不授予正式 task、Driver review、Foundation 或 main 数学采纳。目录更新和远端发布以其各自的实际提交回读为准。

Global-Knowledge-Sync: main@982a440 / GLOBAL_KNOWLEDGE_V1
