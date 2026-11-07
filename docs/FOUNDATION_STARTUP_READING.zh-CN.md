# Source 基础读取包

状态：`ACTIVE / GENERATED-READING IMPLEMENTATION / NO_NEW_MATHEMATICS`

[英文版本](FOUNDATION_STARTUP_READING.en.md)

## 来源与含义

`tools/build_em_foundation_startup.py` 使用同一份已核字段映射，离线生成两种确定性的读取投影：

| 配置 | 输出 | 使用角色 |
|---|---|---|
| `ordinary_research` | `definitions/EM_FOUNDATION_STARTUP.json` | TASK、Driver、Steward、已冻结 FREE B |
| `free_phase_a` | `definitions/EM_FREE_A_FOUNDATION_STARTUP.json` | FREE A |

明确的必需关系包含 P000、心跳世界、残差保真、联合关系保留及全局 Weighted-BRC 类型。普通链接不自动成为必需依赖。最终 Cell 地址和进一步的精确空间、时间、工具细节保持各自实际的条件触发。

读取包不成为新的来源权威。每个 `normative_payload` 分组标明来源 `path`，其 `values` 用准确 JSON pointer 对应复制的完整值，保留条件、例外和嵌套字段。来源元数据与实际 Git blob 标识说明输入；构建时间戳及随时变化的 HEAD 不进入输出。全局仓库的 P000 V4 投影有不同的规范主源，不能替代这组 Source 关系。

当前行为、控制规则与科学输入分别读取。保留已有任务或发现候选冻结的科学版本；后续控制规则更新不能自动替换这些输入。

## 构建与检查

在实际包含五份所需来源的工作副本根目录执行：

```sh
python3 tools/build_em_foundation_startup.py --write
python3 tools/build_em_foundation_startup.py --check
python3 -m unittest discover -s tests -p test_em_foundation_startup.py
```

`--write` 先完成全部输入的解析、必需依赖求解和分类，再写任一生成文件。来源缺失、损坏、schema 改变或出现未分类字段时，不发布声称完整覆盖的新包，保留旧输出；原规范来源及独立工作继续可用。`--check` 报告缺失或失配，不修改文件。可选 `--report PATH` 输出维护者使用的完整覆盖映射，不能与角色读取同时使用。

退出码：成功为 `0`，生成文件失配为 `1`，来源、输入、输出错误或读取不可用为 `2`。测试与构建报告是维护证据，不新增研究者登记或启动门槛。

## 按角色读取及回退

```sh
python3 tools/build_em_foundation_startup.py --read ordinary_research
python3 tools/build_em_foundation_startup.py --read free_phase_a
```

本地读取器核对实际科学输入，复用对应的生成包；只有缓存缺失或过期时，可以在内存中从已分类来源重建适合该角色的内容。`--scientific-inputs PATH` 接受可选 JSON 映射，列出精确来源路径和要求的 Git blob；失配不会更新冻结版本。输入及实际接收上下文未变化时复用本地验证，不增加远程自证流程。

无法取得可分类的输入时，FREE A 只收到简短的不可用结果，不收到混合来源原文、遗漏字段目录或构建报告详情。使用同科学版本的有效 A 包，或现有精确且阶段允许的来源读取，并保留真实暴露情况。其他独立工作继续。普通角色可读取其所需版本的准确规范原文。

仅能使用连接器的读取者面对的是两个独立完整文件。按实际角色、所需科学版本读取相应文件；不能先获取混合普通包，再让模型忽略已经接收的内容。当前 FREE 角色、反锚定和原始基础路由分别读取；其入口正文把 B 专属目录移到 B 阶段参考，不在 A 中枚举。

## 问题形成后的精确读取

独立形成的问题实际包含相关类型化结构时，可在候选冻结前使用精确定义、适用条件和必要工具资料。全量目录、成果比较和去重仍在 B 阶段。问题与来源的对应记录在已有笔记中。

本地读取器接受一项精确请求：

```sh
python3 tools/build_em_foundation_startup.py --lookup /path/to/request.json
```

```json
{
  "question_formed": true,
  "structure_relevant": true,
  "path": "definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md",
  "selector": "2. Positive weighted branch carrier"
}
```

这是为已经形成的有限正权分支问题准备的维护示例，不是向 A 阶段推荐研究问题。无需候选冻结字段。两个布尔值表达调用者对真实问题和相关性的判断；读取器不独立证明起源、上下文清洁、数学正确性或新颖性。

首个适配器支持精确定义章节，以及 `src/enterprise_math/brc_weighted.py` 中的正权分支工具符号 `CWMState`、`cwm_from_positive_weights`、`is_positive_path_realizable`。工具选段包含所需的同模块静态源码依赖，不返回完整模块或无关工具目录。可选 `source_blob` 固定该具体来源。这些 selector 属于维护说明，不作为主题菜单预装进 A 包。

问题尚未形成或结构不相关时返回 `NOT_TRIGGERED`。未支持的 selector 不自动改为整文件回退；使用现有阶段适用的精确读取方式，或根据具体需求扩展这个小适配器。已支持的 selector 不是研究问题或工具许可的穷尽清单。

## 覆盖与真实测量

完整字段分类留在维护报告中。FREE A 接收现行必需值、最少来源标识和通用的条件读取说明。当前强制前提自身可能含有此前术语或结果；这些前提保持原义，读取包不认证上下文清洁，也不抹去既有暴露。

静态包大小只度量明确文件的字节，不度量工具包装、宿主注入、缓存复用、完整角色和控制链、首次实质工作耗时或端到端上下文上限。保留真实原始样本，只在任务、科学输入、角色及冷／热条件对应时比较；否则报告已测绝对值和缺少的证据。
