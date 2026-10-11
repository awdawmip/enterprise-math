# PCF7 固定 Source replacement 合同独立只读审计

**结论：现有 ordinary V1 replacement 不能把 RR-F97259D79B7E7EF3F69F 修成合法 operational Result。三个非法枚举与 V1 核心等式直接矛盾；仅替换当前认证封套不能解决。应先设计显式、限域的恢复合同，不实施、不解除 quarantine、不宣告研究或数学目标完成。** 这不是“所有 V1 replacement 都不可满足”；结论只针对该固定 RR 的修复要求。

审阅者 `/root/historical_control_compat_patch/compat_security_review`，共享上下文、非盲审阅，无这些 Source 模块的作者身份。独立只读子审阅者检查了 RR/contract/quarantine 数据声明；主审阅者检查完整 replacement 模块及 result validator、quarantine 消费路径，并在 parent 提供已获取模块后核验 public facade、receipt、prospective auth/DA 相关路径。全程仅本地读取和字节/AST 比较：没有导入或运行 Source 验证器、tests、native、会话、CLAIM、远端请求、部署或数学接管；只新增本报告。

## 固定证据与核验范围

Source 固定提交：`d829b7e48451584bf608ad1389261c95324a74d6`，由 Root/parent 提供。审阅者没有重新获取远端或验证 commit/tree；独立核验保存的 connector `structuredContent.content` 按声明 UTF-8 原文编码的 bytes，计算 `SHA1("blob " + length + NUL + bytes)`，要求等于 connector `sha`，并确认每个 display URL 指向该固定提交。代码 `.py` 与 connector 原文逐字节相等。未剥离换行、重序列化 JSON 或借旧 Source 字节冒充当前版本。

| 固定解码内容 | Bytes | SHA256 | Git blob SHA1 |
| --- | ---: | --- | --- |
| `research_result_control_replacements.py` | 12931 | `58495714d5d023f6574c09027c02d3d3686e94805af62084e1f0867a32eed3d8` | `ac85f8e8fa4a3e421fa5d7ffbc051c83e8dc7d8a` |
| `control_plane/research_result_records_impl.py` | 30257 | `97750366dfa7e34e2fa158c3ac885153807dd96c41f31b4b52e048f5c8a2e8c5` | `ddda3510b8e49f71e34ea0616bb0a4ca0fb96fce` |
| `control_plane/research_result_authority_fault_isolation.py` | 19181 | `eee09b8162d63725703fae0a8b125fdc1ed17bda03284533bb89b6c9d56f6b16` | `fac58c7bc3186fa2cf6f6c84f44196e851ea84cc` |
| exact RR | 3890 | `a926c55a1aaecac16e4d7e4ca575eb3a3e1dcb5452bf19245de213c4a7e63568` | `bba0267ffdc7b685517fec9ac809ab8fc715d408` |
| replacement contract | 1216 | `4c2180803821d9082bede5a00107efcb4373981ae8620ec99e86aadf497584e6` | `d64a2b6aadff55dba4d7f9d74f14a7a8e8fbed77` |
| Result authority quarantines | 68687 | `1f40e25bb40b3b749601108d3a921cd07dbc2efb13e8601dd6093d862e2d30a5` | `9b3e735e075353e1fdad4d7299cb2ba798622f2d` |

本地入口：[replacement 代码](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_control_replacements.py:29)、[result 实现](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_records_impl.py:299)、[authority isolation](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_authority_fault_isolation.py:299)、[精确 RR connector](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/WITHHELD_RESULT_FIXED_SOURCE_FULL.json)、[contract connector](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/research_result_control_replacement_contract.json.connector.json)、[quarantine connector](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/research_result_authority_quarantines.json.connector.json)。数据 ledger [ALL_RECOVERY_CONNECTOR_BYTES_VERIFIED.json](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/ALL_RECOVERY_CONNECTOR_BYTES_VERIFIED.json) 为 2584 bytes/SHA256 `e1e752bfa3c694cd2052d7ab45d6c8da8366d2b546c05e6d69f3204179acae8b`；合同/quarantine 解码 bytes 与 ledger 相符，RR pins 与 quarantine 精确条目相符。

## 严格失败路径

目标 RR 绑定 Task `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION`、publication `TP2-1C146C521C5946742C17`、execution `ER-E90FEF513B0AEE96C73E`、claim `CLM-PCF7FIX-0BFF2D2CD73646AD`、researcher `EM-PCF7FIX-B603FA`。原 frozen_at 为 `2026-09-17T05:24:00+00:00`；`terminal_verdict=SUCCESS` 是保存的历史声明，不等于当前 operational 终态或数学接受。

| 字段 | 原 RR 精确值 | 当前规范枚举包含该值 |
| --- | --- | --- |
| `method_harvest` | `BRC_TYPED_ZERO_FLAG_STATEMENT_REPAIR` | 否 |
| `independence_status` | `TASK_LOCAL_PROOF_PLUS_DETERMINISTIC_CHECKER_REPLAY_PLUS_EXHAUSTIVE_SMALL_STATEMENT_AUDIT` | 否 |
| `source_exposure_status` | `NONBLIND_DISCLOSED_TASK_RESEARCH` | 否 |

1. **保留三值，则新 Result 不合法。** [规范集合 37–48](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_records_impl.py:37) 不包含原值；[freeze 328–333](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_records_impl.py:328) 分别抛出 `invalid method_harvest`、`invalid independence_status`、`invalid source_exposure_status`。[原始 record audit 478–483](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_records_impl.py:478) 同样记录三项错误。CLI choices 在 652–654 行还会提前拒绝非法字符串。这里为静态逐字核验，不声称实际触发了 CLI/handler。

2. **改成合法三值，则 ordinary V1 replacement 边不合法。** [replacement `_CORE_EQUAL_FIELDS` 29–46](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_control_replacements.py:29) 包含这三个字段；[180–182](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_control_replacements.py:180) 对每项要求 `old.get(field)==new.get(field)`，否则产生 `control replacement changed core field <field>`。对任一非法原值 v：`new=v` 与 `new∈allowed` 的交集为空。复用 auth、增加 reason 或更换 Driver 均不能改变该等式。

3. **保持全部输出且只改封套也违反 V1 manifest 条件。** [198–209](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_control_replacements.py:198) 要求旧 manifest path 集合为新 manifest 的真子集；相等的五项 manifest 被拒为 `corrected output manifest must be a strict path superset`。共同输出的 Git blob/SHA256 均须不变。新增合法 scope 内的控制说明文件只能解决这个真包含条件，不能解决三枚举矛盾或 execution 身份；不得扩大 allowed_outputs 或添无关 artifact 作为规避。

4. **execution 身份是另一个阻断，不能由本审计接管修复。** [freeze 315–319](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_records_impl.py:315) 首先从 canonical `execution_map` 查 execution，缺失即 `unknown execution_record_id`；[142–150](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_records_impl.py:142) 没有建立 alias 的逻辑。精确 quarantine 记载 basis `BOUND_FROZEN_RESULT_FLAT_EXECUTION_RECORD`、raw error `unknown execution record`；[flat 分支 228–243](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_authority_fault_isolation.py:228) 反而要求该 execution 不在 canonical map，并仅用 frozen manifest 绑定 bytes 作诊断。本审计没有重跑 execution map；parent 主审负责这个当前事实与 writer route。不能复制 flat ER 到 nested 目录、补别名、重造旧 CLAIM/授权时间或把诊断绑定解释成执行许可。

5. **绕过 replacement 边直接加同 execution 新 RR 仍被拒。** [operational_results 299–317](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_authority_fault_isolation.py:299) 明确要求调用方先完成普通边验证；同 Task/publication/execution 的 surviving Result 必须是旧 RR 的 validated replacement 链 sink，否则报 `same-execution recovery lacks validated replacement authority`。所以“保留旧 quarantine 但插入一条清洁 sibling”不能偷渡为 same-execution repair；真正重新执行是不同证据与额外授权范围，不是本任务。

6. **quarantine 只扣留，不赋修复权限。** [97–107](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_authority_fault_isolation.py:97) 强制 nonoperational/history-preserved 和所有 grant flags false；[250–254](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_authority_fault_isolation.py:250) 比较完整 raw/bound 错误集合，不能扩大 suppression；[326–342](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_authority_fault_isolation.py:326) 返回 WITHHELD、`terminal=False`、`result=None`、`review=None`。不得改旧 RR/ER、移除 entry 或放宽 raw audit 使原声明复活。

## 现有认证能证明什么

[replacement `_authority_errors` 133–150](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_control_replacements.py:133) 要求 EM-DVR 格式、created_at，调用 `require_active_driver(driver_id, created_at, root)`，并比较 active DA record ID 与 source comment ID。这是 V1 边的一项 Source-backed Driver 校验，不是任意 SourceSteward 权限，也不能自行证明新的 write kind 已授权、当前登录 session 被该 DA 绑定、当前 Source HEAD/CAS 或真实审阅者已接受新三值。这里 created_at 是 row 字段；禁止通过设置历史时间绕过当前权限。

边本身还需两 RR immutable path/blob、同 core 与 return hashes、hard disposition 保留/扩展、不同 owner checkpoint、严格更晚 frozen_at、非空 reason、history-preserved/nonparallel、四项 grant false，以及 single-in/single-out acyclic chain（153–260）。这些检查不应在恢复分支中丢失。[`_raw_results` 103–105](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_control_replacements.py:103) 刻意读取历史原始 Result，不是 quarantine 后的 operational 视图。

Parent 随后提供当前 d829 的四个固定模块。审阅者独立比较 `.connector.json` 解码 bytes、本地 `.py`、blob、SHA256、URL 与 [AUTH_ROUTE_PINS.json](/workspace/em-owner-resume-20261011/pcf7-control-repair-audit/AUTH_ROUTE_PINS.json) 的全部四行，均一致。该 pins 文件本身为 2010 bytes/SHA256 `c6dceb9b7ba1a9f6d22cdee8e9d1c66bd2d6c22f43bbb6a01376cc56d4fb5024`。远端 GET 由 parent 执行，本审阅者只作本地独立 bytes/blob 核验：

| 补充固定源码 | Bytes | SHA256 | Git blob SHA1 |
| --- | ---: | --- | --- |
| `tools/research_result_records.py` | 31549 | `69de8175c570ef1d96185c09b1f954fa86c2c5f275e3818b591101e2d43b31b0` | `fe51fc57c4b2d9b85da43c53b1ac07f6d61d216d` |
| `control_plane/research_continuation_write_authority.py` | 10566 | `19bc716767b6d6f674c37f56edf6591e5130483a270187dd7e347fd1e2b0afff` | `8a4ae9ff6ed3511846c491bf4d7ba01a24b8b5d3` |
| `research_driver_authority.py` | 21010 | `93cae9f857fd4c77cd525298a7402baeb211298fa52a24fa8854e2f434ff54d2` | `7690dc6e58c551632087b0028a6aa00c3473b9f0` |
| `control_plane/research_continuation.py` | 59237 | `09678f4f1d91b440e154dae54ca72ac84d9df2c155a8f6e93acabdc2acd56fb1` | `8d1c8e5eefce59a458c5da07c32c0837d8f693c6` |

**当前 public freeze 的顺序不是修改底层 dict 即可写入。** [command_freeze_transactional 497–550](/workspace/em-owner-resume-20261011/pcf7-control-repair-audit/fixed-current-source/tools/research_result_records.py:497) 先安装 canonical write view、调用上述 freeze 构造，再 `require_freeze_authority`，补执行角色/旧贡献声明，构造并核 RESULT receipt，`require_valid_result_candidate` 后才 immutable transaction/postcheck；[693–699](/workspace/em-owner-resume-20261011/pcf7-control-repair-audit/fixed-current-source/tools/research_result_records.py:693) 绑定 canonical command。这是读取的 Source CLI/public facade 路径，不是已暴露、已调用的 authenticated transport writer 证明。

**当前 prospective Result auth 不支持给旧 PCF execution 套用新 Driver 封套。** [require_freeze_authority 39–77](/workspace/em-owner-resume-20261011/pcf7-control-repair-audit/fixed-current-source/control_plane/research_continuation.py:39) 在 write gate 启用时要求 current runtime state/events，以当前时间 `authorize_execution`，并精确比较 target Task、claim/publication/researcher/branch/taskbook binding，要求真实 execution session 和 host Source snapshot。新 Result receipt [100–137](/workspace/em-owner-resume-20261011/pcf7-control-repair-audit/fixed-current-source/control_plane/research_continuation_write_authority.py:100) 再从保存的 raw server comments 经真实 parser/auth/registered/reducer 重建 live ownership；claim、researcher 和 principal 必须等于新 record，dispatch 必须 LEASED、ownership_epoch 一致、session 合法。GOVERNANCE 分支还检查 RESEARCH_DRIVER/DA/session。当前 Root 的 DA 或其他 GOV claim 不能替代目标 PCF Task/publication/旧 researcher/claim 的这些绑定，更不能反向赋予历史写入权限。

**cutover 与 receipt 也不能作为修复豁免。** [receipt_error 77–95](/workspace/em-owner-resume-20261011/pcf7-control-repair-audit/fixed-current-source/control_plane/research_continuation_write_authority.py:77) 在 cutover 存在时，仅 exact 原路径且 bytes/blob 不变的 legacy entry 可以通过该 admission 层；漂移直接报 `immutable pre-cutover record bytes changed; cutover grants no repair authority`。新路径必须有同 schema/kind 的 canonical `write_authorization`、payload digest 和 40-hex Source snapshot。legacy admission 不豁免原 strict audit/quarantine；换 frozen_at 或改 record ID 不会取得 legacy 豁免。[build_receipt 24–57](/workspace/em-owner-resume-20261011/pcf7-control-repair-audit/fixed-current-source/control_plane/research_continuation_write_authority.py:24) 是本地 canonical payload/evidence 封装，文件 1–6 行明确不是 platform-signed chat identity，repo-owner 恶意伪造也不在其控制边界。

**现有 receipt 不是新 recovery kind 的通用授权。** `record_path` 使用 RESULT 路径、否则 REVIEW 路径；`receipt_error` 使用 RESULT principal/replay 分支、否则 Driver REVIEW/session/contribution 分支（45–51、100–160）。未见新 metadata-recovery record path/schema/principal/target-delta admission 分支。给 `build_receipt` 任意 kind 字符串或借 REVIEW 形状并不能创造该新能力。现有 REVIEW [require_review_authority 80–102](/workspace/em-owner-resume-20261011/pcf7-control-repair-audit/fixed-current-source/control_plane/research_continuation.py:80) 要 current active DA、真实 session 绑定和不重叠贡献声明；[DA active_authority_at 316–365](/workspace/em-owner-resume-20261011/pcf7-control-repair-audit/fixed-current-source/research_driver_authority.py:316) 按真实 source comment 顺序处理 REVOKE/succession，不能仅由旧 authority ID 或 body 声明绕过。

Public runtime [iter_results/iter_reviews 115–131](/workspace/em-owner-resume-20261011/pcf7-control-repair-audit/fixed-current-source/tools/research_result_records.py:115) 先 ordinary replacement/sink、精确 quarantine，再 receipt operational filter；[task_result_state 319–355](/workspace/em-owner-resume-20261011/pcf7-control-repair-audit/fixed-current-source/tools/research_result_records.py:319) 又对新 admission diagnostics 返回非终态 WITHHELD，并对 surviving Result 再做 strict audit。这些实际消费层也不能只删三枚举错误便绕过。

**保留的有限范围：** 未运行这些 guard、receipt、candidate preflight 或 transaction；没有获取 cutover/policy 全仓库、验证当前会话或执行完整 Source audit，也没有审 backend exposed role/ordinary/MCP route。policy/cutover 开关的实际值、canonical ER 当前全量 map、候选验证 helper 与 transport writer 由 parent 主审；本报告不对这些未读/未运行路径出 PASS。Root 当前角色只是路由、目标写权限不能由 Root DA/GOV claim 补齐的独立 transport 结论由 parent 主审提供，不假称本审阅者执行过该接口。

## 最小必要设计边界，尚不是实现或已授予的权限

若要保留 Task/publication/scope、原贡献、return 和共同 output bytes，同时修复控制元数据，必须先定义一种**显式 typed metadata recovery**（新 record/schema 或 V2 的专用 resolution），而不是无声删除 V1 的三个等式、增大全局 enum 集，或沿用 V1 resolution 却另给隐藏豁免。V1 原有行为保持不变；新机制至少需要以下合同：

- **精确 historical target 与错误边界：** 只对既有严格验证、精确 path/blob/SHA256 的 withheld RR 操作，绑定 immutable Task/publication/taskbook、claim/researcher/branch/base、return、每个旧输出及当前 quarantine/dependency pins。声明旧三值、拟新三值、变化理由和授权来源；变化集合精确为声明的控制字段，未知变化拒绝。保留历史 invalid bytes，不使其获得 retroactive validity。
- **元数据语义不能静默增强：** 新三值必须属于规范集合，逐项给出证据和显式审阅，不把长字符串自动截断或映射成更强的 independent/blind/tool 身份。`NO_TOOL_PAYLOAD`、`NOT_INDEPENDENT`、`NONBLIND_DISCLOSED` 是可能的保守候选，不是本报告替 Driver 作出的选择。若证据不足，仍保持 withheld。科学 payload、原贡献和数学 verdict 不得因 schema repair 提升；与 math 有关的 extra 字段也应保持精确值，不能仅依赖 V1 有限的 `_CORE_EQUAL_FIELDS`。lane/cohort/allowed-output scope 必须显式比较，不能只凭同 ER ID。
- **auth-only 与 artifact 延伸区分：** 零 artifact 的封套/metadata correction 若是合法用例，应由新的 typed 分支明文支持旧 manifest path/hash 相等；若仍要求 strict superset，则新增控制 artifact 必须在真实授权 scope 内且明确仅控制作用。两种都须保持公共科学 bytes；这不是豁免 output-scope 校验。
- **历史 execution reference 不可升格：** 该 flat ER 只能继续作 exact evidence reference。若新 record 需要 canonical execution 才能成为普通 Result，必须另有明确、当前授权且不造历史身份的 execution-provenance 合同；这是独立必要条件。未建立它之前，更窄的 typed re-attestation 只能保存控制诊断，不能进普通 Result map/operational sink，也不能解除 withheld。新 enum/边 schema 单独修改不够。
- **prospective writer admission：** 新 operation/write kind 必须有正式 Source validator、writer role/capability 与目标 scope 定义，真实当前 session/DA 绑定、当前固定 Source 与 actor 输入验证，并将 exact payload/record ID/target path/旧 pins/允许 delta 绑定到真实 admission；写前 current-head/CAS 检查与不可变创建必须 fail-closed。现有 freeze/review receipt、任意 reason 文本、Root 指令或外部全局知识都不能冒充这个新 kind 的授权。无需也不得 invent 签名 receipt 或 SourceSteward authority；应由实际已有合法机制能支持的能力定义推导，缺合同就停在设计。
- **消费顺序和审阅分离：** 新分支只有完整 validation/auth/admission 成立才参与 declared chain/sink；任何 failure 不隐藏旧 withheld。仍拒循环、分叉、same-execution sibling 绕过、目标/Source/dependency 漂移、未声明字段、授权撤销和 stale replay。保持历史 RR/derived reviews referenceable、nonparallel。独立新 Driver review 必须 pin 新 record，不能继承原 ACCEPTED 或把 control repair 解释为 Working Truth/Foundation/推广/后继触发。

## 旧 Driver review 不能复用

补充只读核验 [review audit connector](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/review_audit.connector.json) 解码为 34117 bytes/SHA256 `f6d6857a735221e172db6a7a2f6111157f2c64720eb8f122cf1ad81567fd5eb1`/blob `c640c38e574344f8db7af98ef415d4f51fec28fd`；[DR connector](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/DR-027ED0C06D7B6A76E0FF.json.connector.json) 为 1070 bytes/SHA256 `0b945b033568fa92f7b22beac432d8ab2ab23e04f3aea0fa63392bff6b68db95`/blob `ee18873c27f34100d9bafd94e081618493d99fe1`。两者 connector bytes/blob 均相符，URL 固定 d829。

原 DR 保存 ACCEPTED/terminal 声明，但精确 review-audit entry 是 `INVALID_IMMUTABLE_REVIEW_RECORD`，`operational=false`，错误 `review artifact digest drift`，明确只保留历史 disposition、不重绑当前 artifact。Result authority isolation [292–323](/workspace/em-owner-resume-20261011/pcf7-statement-correction-20261011/recovery/code/research_result_authority_fault_isolation.py:292) 还过滤该 withheld RR 的 derived review。原 DR accepted 不证明新 metadata 合法、新 repair 获权或新 RR 被接受。

## 后续验收应证明的最小正负矩阵

本审计没有运行这些测试；以下只是新合同提交前必须能说明的验收要求。

| 情况 | 必要结果 |
| --- | --- |
| 保留原三非法值、ordinary V1 refreeze | enum validator 拒绝 |
| 改合法三值、仍用 ordinary V1 edge | core field 等式拒绝，不能 silently exempt |
| 相等 manifest、仍用 ordinary V1 | strict-superset 拒绝 |
| 专用 recovery：exact target、声明三字段 delta、真实 fresh admission、全部科学 bytes/scope 不变 | 仅产生合同明示的控制记录；尚无 execution 合同则仍 nonoperational/withheld |
| 自动升级 independent/blind/tool，改 verdict/贡献/return/output/Task/pub/lane，未知 field delta | 拒绝 |
| 原 flat ER alias/移动索引、backdated DA/CLAIM、borrowed Driver/session、旧 freeze/review receipt | 拒绝；不造历史身份/权限 |
| 无 chain 同 ER sibling、分叉/循环、quarantine/dependency/currenthead 漂移 | 拒绝，旧 hold 仍可见 |
| 承用旧 ACCEPTED/invalid DR，repair 自动终态/Working Truth/Foundation/后继 | 拒绝；新 independent review 单独验证 |

审计到此完成并停止。没有撤销这个合法扣留，也没有数学结论更新。当前可交付的是明确失败路径与设计边界；不是可执行的修复、更不是权限绕过。
