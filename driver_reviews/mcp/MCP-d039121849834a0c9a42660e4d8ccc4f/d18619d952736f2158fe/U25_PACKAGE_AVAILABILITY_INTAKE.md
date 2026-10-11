# U25 package availability intake

状态：**PARTIAL_BYTE_RETRIEVAL / NO_SCIENTIFIC_REVIEW / NO_NATIVE_TASK_OR_IDENTITY_CREATED**  
日期：2026-10-11。这是实际 Driver 的只读 evidence-intake 输入，不是数学审核或接受；本轮没有执行任何研究源码、实验或全 suite，也没有远端写入、建立 session/claim、接管其他 chat 或联系他人。

## 结论与范围

已从 GitHub connector 取回 U25 七项 declared dependencies 中四项的实际完整源码，并核验 bytes、raw-byte SHA256 和带 Git blob header 的 SHA-1；四个 blob SHA-1 均精确匹配 U25 pins。U25 声明的五个包文件、其余三项依赖和 U24 实际消费/接触实现，在本次授权 workspace 与 connector Source 摄取中尚未定位/取回。

**GitHub 404 只说明指定 repository blob endpoint 在本次读取中未能取回该对象；不是 conversation package 不存在的证明。** `CONVERSATION_PACKAGE_WITH_SEVEN_PINNED_DEPENDENCIES` 是 checkpoint 中的包位置声明，不是可解引用的 Source URL。本轮未获得该原 conversation package 的实际可访问文件引用，因此未把其他文件拼装成“完整 U25 包”。

Source pinned read：`awdawmip/enterprise-math@7f3671187aca1c041294766fa4704715698e3dc6`。沿用已核验 GK commit `dfa87940e18c6e4b8017bb0d01e20fe878a2189e` 和 P000；没有以 Sites manifest 的旧 GK static bundle 覆盖它。本文没有新增或弱化 P000、公理、模型消费规则或数学结论。

## 已取回的四项 U25 依赖

所有以下 SHA256 都是本轮对实际 UTF-8 源字节计算；Git blob SHA-1 的计算是 `SHA1("blob "+decimal_bytes+NUL+raw_bytes)`，不是 raw-byte SHA-1。树中的相同 blob 值与本轮实测同时匹配，故四项报告裸 pins 的 digest kind 已得到实际确认。

| 文件 | 实测 bytes | 实测 raw-byte SHA256 | 实测/匹配 Git blob SHA-1 |
|---|---:|---|---|
| [local_latent.py](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/local_latent.py) | 8248 | `fc98fd83ee409bfaedd12dae634f63416d1cd779a3f27e58a06b841fb3cb482b` | `67408af5b977bed7295f7225cdd3f550c41b9729` |
| [connected_retention.py](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/connected_retention.py) | 7879 | `25aa7780fad05cd0c5fcfa0611b43069af0640fb2cfd2bd97acb11f55cd3ac39` | `569e6171d0052fbfd41cf007b09a8327b339228b` |
| [packet_router.py](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/packet_router.py) | 8724 | `2e1beb9c510cd8235633e33f41d3e3d93ce20665b9d72847d6a13b1d15cda582` | `7465f5aa16cbb8fba61ba4be80f8a6884b879c53` |
| [brc_weighted.py](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/brc_weighted.py) | 9635 | `4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f` | `3f205696709e847909958a153f8fe10d3f6b70f0` |

Source 路径：

- `research_notes/chatgpt_direct/20261008_cell_u9_local_latent_4b7e62/local_latent.py`
- `research_notes/chatgpt_direct/20261008_cell_u8_connected_retention_5e91c4/connected_retention.py`
- `research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/packet_router.py`
- `src/enterprise_math/brc_weighted.py`

GitHub `fetch_blob` 按 exact digest 取回；上述路径是在 pinned Source 树中确认的同一 blob。只核验字节身份，不把源码存在、相同摘要或本文静态引用计作科学运行/审核。workspace 子代理另独立定位到现成 `/workspace/enterprise-math` 中的 packet_router 和 brc_weighted 实际文件，bytes/SHA256/blob 均相同；这不是新增实验。

## U25 声明的包文件：精确缺失清单

U25 current note directory 的完整 Contents 返回只有 `RESULT.md` 和 `CHECKPOINT.json`，tree `6807f5362cbc5a382fc6ed345a98ac419f633f5e`。README 路径 fetch 返回 404。下列五项按 checkpoint 明示的 Git blob SHA-1 分别调用 `GitHub.fetch_blob`，全部返回 repository blob endpoint 404：

| 声明文件 | 声明 bytes | 声明 raw-byte SHA256 | checkpoint 明示 Git blob SHA-1 |
|---|---:|---|---|
| `NOTE.md` | 18364 | `e8ff8202157b42cc93f1855704433c968f27768cdd6a160164402efa5cbcda6c` | `a42fd158e08e96ecfa01826fc328496c69aec3d0` |
| `release_flux.py` | 17907 | `5473366d81bee9e04d7ef5bdcdf3dc3d58ba1d5ed589e31f6a3b39f844f3ffb7` | `b906929703dfbd5c31a1c4355dfd33ddf15d8d5e` |
| `check_u25.py` | 7867 | `54c91cc8389e37a68436cd46f11ba227162b8702ad7bda50ff74500212ea8a31` | `7bf7d0e1368f938912e9a8e4c0b760a789b0c3d2` |
| `evidence/results.json` | 10579 | `3d783942543bda0d1b6b28838686247d89738d4fec1e6c2f10aa13ddf7d62407` | `c49d0775fc038f6e392c331359e4b9a808a896cf` |
| `evidence/full_trace.json.gz` | 43898 | `77b3eb3d1b3cfe7f58f661939f4005642b7978841a61986049342e46b39d5526` | `7e51de295308d6ba147e5c7972970e657c2c850f` |

这些是**声明值**，没有该文件实际字节，不能写成实测匹配。解压 trace 的声明 143596 bytes / SHA256 `7ffa249fe489d1f943f1c305da8837b5577aa9e006ac6e1a19b182b5f65a7c96` 同样未核验。活动仍为 `activity_id=null`、科学独立审核仍为 false；保持原状态。

尚未取回的 U25 三依赖：

- `residual_contact`，报告裸 pin `6160eb24cda9ef576d2972ef45df8e16e9fe67a4`：以 Git blob SHA-1 候选值调用返回 404；实际 bytes/SHA256 和报告该裸 pin 的 digest kind 未在本轮确认。
- `contact_network`，报告裸 pin `5f89fe162f230c5ce31c317bda17089935f1c7fc`：以 Git blob SHA-1 候选值调用返回 404；实际 bytes/SHA256 和报告该裸 pin 的 digest kind 未在本轮确认。
- `mobile_junction`，报告裸 pin `37931d40d7a2edc36889366d4766c83319eef0e7`：以 Git blob SHA-1 候选值调用返回 404；实际 bytes/SHA256 和报告该裸 pin 的 digest kind 未在本轮确认。

## U24 实际资源消费：已取得叙述，真实执行代码仍缺

完整取回 U24 `RESULT.md` 与 `CHECKPOINT.json`，其 note directory 同样只有这两项，tree `de3f1ffd9a42943e9d6bf49210ffbe147a73f0c5`。

- [U24_RESULT.md](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/U24_RESULT.md)：10264 bytes；本轮 SHA256 `2f97982803ae8c5c7e334e4c7b4f531c19121505fad32266ccd0edef7970d325`；Git blob `38d59ffcd4c5671dafe4393aca586c08a409c41b`。
- [U24_CHECKPOINT.json](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/U24_CHECKPOINT.json)：2467 bytes；本轮 SHA256 `af58c6608c567e7b33cb120057d83edb9b8995d0add72317705ffd042a31d7c4`；Git blob `b84148c2e7260fa5b34380f227fe67874de832ab`。

[报告第12行](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/U24_RESULT.md:12)明示：BC 释放后 record1 在 B；执行不变 U9 `material()` 将 degree1 的 B 沿 vacant transverse native edge grow，**同一 released record 被用作 AB 的新 prefix**；总词长从3变4、四 records 均 bound，BC endpoints 不再相邻，原固定几何 repair proposal 暂时不 eligible。报告也明示 inverse 可恢复 B/source path/free record 并 recapture，故不能把它改写成永久陷阱或全局不可能。这个段落仍是未独立审核报告的陈述。

实际取回的 [U9 local_latent.py:83](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/local_latent.py:83)可直接静态引用：`material()` 对 incident first leg 在 grow 时 prepend `p^1`，在合法 shrink 时删除 prefix，然后更新 actor Cell。这个文件的该接口没有 free-record identity/location/capacity 字段；它本身不是 U24 `ContactInventory` 的完整资源账与配送实现。

U24 以下三项声明源码/证明文件按 exact checkpoint Git blob 取回均返回 404：

| 声明文件 | 声明 bytes | 声明 raw-byte SHA256 | Git blob SHA-1 |
|---|---:|---|---|
| `NOTE.md` | 17162 | `502ce43a9d86deb5570f99f1bfde80040e56e582b21d8ea7c9925b8d1436681f` | `368ed12837467c50d8085628f01083de59dc71c1` |
| `transport_repair.py` | 10287 | `7658be3d6a62250570beb8723a7b36133225ef7da0c2bd734557cf8221e024b2` | `468371af72c570900a0557b7b0400fc6631d593c` |
| `check_u24.py` | 9994 | `6faaf2820b91009383ccf11dcc0e3520ba27c107a83d35e5a40bc0a3dd09e116` | `1fe64914a6644f728167face06b29c17ece98533` |

U24 八代码链额外的 `repair_reserve` 裸 pin `95426d4c2b3b0060c3f166696cf950eb7c0bb83f` 也按 blob 候选读取返回 404；同样不把未经确认的 digest kind 或代码字段补造。报告中具名 `cell_closure_u24_evidence.zip` 没有给出可解引用 URL，本次查过的 Source 树路径及 workspace 搜索没有定位它。实际 `ContactInventory.toggle`、transport wrapper 的 record identity/free/held/bound 与 motion 消费对应仍待原包。未重跑已完成 U24 全 suite。

## U11 仅作邻接背景，不能替代 U24 缺失代码

额外取回 [U11_resource_lift.py](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/U11_resource_lift.py)，来源：
`research_notes/chatgpt_direct/20261008_cell_u11_resource_reaction_c7e4a1/resource_lift.py`。
实测9675 bytes，raw-byte SHA256 `68d4f298d058332a237ce9b3747abfb36484569800e4107b23fb57212cb323fd`，Git blob `0a7e0890eb08dc722d2e85fb3ad1a7b2d6b29621` 匹配 connector metadata。

该文件[开头](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/U11_resource_lift.py:1)明确限定为 isolated material grow/shrink transaction，非所有 U9 channels 的 distributed implementation；其 source-defined inventory/transaction 可在[第69行](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/U11_resource_lift.py:69)与[第129行](/workspace/em-owner-resume-20261011/u25-package-intake/retrieved/U11_resource_lift.py:129)读到。它提供 per-occurrence token、free phase、reservoir Cell，以及 reserve/carry/attach/detach/release 的有限事务字段。本文只报告这些实际源字段，不采纳为新的 U25/U24 规则，不据此证明固定库存 lift 可行或不可行，也不将其源码替代缺失的 ContactInventory。

## 搜索记录与缺失结论的边界

本次只读范围：

1. workspace 的相关文件名、代码 pins、明确报告/归档名字定位；实际找到 packet_router/brc_weighted；旧本地 Source tree 元数据中的 local_latent/connected_retention 指针只作定位线索，不取代本轮 connector 实际源码。
2. pinned Source root shallow tree 完整返回219条；完整递归 research_notes subtree 返回4097条、`truncated=false`；额外 artifact/research_artifact/src/experiment/research_toolkit 子树分别返回6/1783/302/499/1条，均 `truncated=false`。这些已读子树没有定位缺失包的实际路径。
3. 整仓 recursive tree 请求曾返回 `Transport closed`，因此**不以该失败请求证明全仓负结果**。不是所有根目录/历史/其他 conversation 均已遍历。
4. GitHub code search 的5个限定查询 `CONVERSATION_PACKAGE_WITH_SEVEN_PINNED_DEPENDENCIES`、`8C4D71`、`cell_closure_u24_evidence.zip`、`release_flux.py`、`ContactInventory` 均返回空列表。索引搜索有限且可不完整，不把空结果当不存在证明。

本地证据：

- [SEARCH_AND_BLOB_RECEIPTS.json](/workspace/em-owner-resume-20261011/u25-package-intake/SEARCH_AND_BLOB_RECEIPTS.json)：保留 actual error/read receipts。
- [TREE_SEARCH_EVIDENCE.json](/workspace/em-owner-resume-20261011/u25-package-intake/TREE_SEARCH_EVIDENCE.json)：保留已读 subtree/directory 元数据；2542645 bytes，SHA256 `e871493d47255c389856fc6fb941b47a2d36cf2ccd0858c77c236bf7e62e8764`。这是本地序列化证据摘要，不冒充 Source tree Git object digest。
- [LOCAL_BYTE_MANIFEST.json](/workspace/em-owner-resume-20261011/u25-package-intake/LOCAL_BYTE_MANIFEST.json)：全部实际取回文件及本地证据的实测摘要。
- [RETRIEVED_SOURCE_RECEIPTS.json](/workspace/em-owner-resume-20261011/u25-package-intake/RETRIEVED_SOURCE_RECEIPTS.json)和[U11_BACKGROUND_RECEIPT.json](/workspace/em-owner-resume-20261011/u25-package-intake/U11_BACKGROUND_RECEIPT.json)：完整 connector 字节返回保留。

## 最小下一步输入

A 单元已有四个依赖的真实字节，但尚未通过“完整科学包与资源规则输入齐全”门。最小补齐仍是：**U25 五个 package files；U25 三个未取回 pinned dependencies；U24 实际 NOTE/transport_repair/check_u24/ContactInventory 与其 repair_reserve 对应；原完整包的可解引用来源及 manifest。**

实际 Driver 可据此保持科学审核未开始/未通过，使用准确文件名、bytes 与 digest 请求原包进入已授权可访问源，再按字节验证后进入 B。当前范围的合法停车是**“本次授权源中未定位完整 conversation package 与所列实际实现”**，不是全局不存在、内核无解、数学审核失败或母目标已关闭。

