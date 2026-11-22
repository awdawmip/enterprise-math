# 新成果进入、复用与中控台维护：独立实测

日期：2026-11-21。科学案例冻结于 `07fd94dcdc3765375d880d20fd22d122b2123037`。本次为知情工程维护与既有结果应用，没有生成Researcher、CLAIM、Activity或正式数学审查。

## 完整交付

- [独立报告与全部实际轨迹](https://github.com/awdawmip/Nollm/blob/c68557881b72cc9eee832181d68717c9dad72ff8/lab/nollm-lab/repository_memory/enterprise_math/intake_audit_20261121/REPORT.md)
- [后端、网关候选与发布步骤](https://github.com/awdawmip/em-research-mcp/blob/56c09c0e46e88218d0152a9405e3d9688f0aac0e/docs/NOLLM_INTAKE_RELEASE_20261121.md)
- [项目使用流程](../../../docs/RESEARCH_MEMORY_WORKFLOW.md)

Nollm #7提交 `c68557881b72cc9eee832181d68717c9dad72ff8`；后端 #112提交 `56c09c0e46e88218d0152a9405e3d9688f0aac0e`。当前EM分支保存本记录及启动使用指引，通用运行库继续归Nollm，服务适配归现有后端。

## 线上实际发生的事

在研究中控台v23上读到了刚产生的[R284CO固定原文](https://github.com/awdawmip/enterprise-math/blob/07fd94dcdc3765375d880d20fd22d122b2123037/research_notes/portable_direct/R284CO_SPECTRAL_WITNESS_RIGIDITY_20261121.md)及赢家索引证书。原结果状态为 `AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED`，定理首次提交于2026-11-21 03:00:58 UTC。

Host保存了 `PORT.spectral-witness.R284CO.20261121T031021.v1`，位置 `[0,2,1]`；正文和三个固定来源精确读回，之后字面检索命中。它保留冻结人口、64个有标签距离、重数、原第1秩恒零、63个唯一赢家与间隔条件，未写入后续测试答案。

两个独立新会话分别使用原生Surface入口和同场的字面检索，在相同真实理解与固定来源上完成局部+17条件题：只在原非见证点index0整行加17，其他行不变。两人都正确证明第2至64秩的赢家和最大值不变；第1秩变为index0独占17；全谱唯一最小见证集由63点增为64点。推导依赖原间隔至少64、赢家行未变和原第1秩恒零，不需要重跑完整有限枚举。

| 实际入口 | 线上材料调用 | 失败 | 紧凑JSON返回字节 |
| --- | ---: | ---: | ---: |
| 原生菜单/单一物理入口 | 13 | 1 | 24,566 |
| 同场辅助字面检索 | 4 | 0 | 9,806 |

原生组的失败为尝试未说明范围的页宽12；经邻格召回发现目标，随后回源3次。字面组因题面明确R284CO名称，1次find定位后show及2次回源。该比较支持按实际查询选择入口；它是一题同模型开发诊断，未测隐藏第二研究线，也不提供总token/账单收益。

## 候选已验证的修复

独立原生审计复现128/512格中心目标在原24逻辑页预算内可达；旧固定窄页3仍有耗尽。清缓存、旧游标、插入、修订、连接方向、目标同格peer和撤销恢复的受影响行为通过。

本次维护候选补齐 `em_memory_stitch`、`em_memory_unstitch` 和按原ID查看实际端点的 `em_memory_links`；保留同一锁和原读取/检查点写范围，不增加控制任务、身份或幂等账本。`show`增加 `current_scope=working_memory_field`、`source_freshness=not_checked`。canonical initialize及适用context manifest增加可选研究入口；walk描述明确next翻页和1..8页宽，SDK直接公开范围。

真实本地检查：原生既有3项回归及4组独立行为通过；本次links安装API1项、后端13项、网关schema/relay16项、真实JS→Python→Nollm跨进程集成1项均通过。网络Source使用明确固定fixture，生产场只保存有原来源的R284CO理解。没有用工具目录存在替代实际调用，也没有把本地候选标为线上。

线上实际仍为v23 build `em-sites-gateway-20261121-memory-coordinate-guide-r1`，后端0.6.11，runtime `220d3c8f3b47ab62d137c6dc2868be55b501c7f3f92c29f8b4570ab4fe06e3d1`。候选的运行库、后端、网关需按配套步骤发布，现有持久工作场继续复用。

## 剩余架构重点

新科学提交、Activity和Result目前没有自动形成Nollm理解。建议从现有Source Git增量派生待读候选，由Host按问题提炼，不默认注入全库。需要测试连续新提交的漏收、重复、修订和实际再利用成本。

有向桥始终是物理关系；目标修订后桥继续存在，Host仍须判断数学条件是否继续成立。跨线关系应保存可回源的对象对应、适用操作和条件，几何负责提供该现场。下一项区分性实验是不点名第二研究线的任务，随后加入真实前提更正，检查正确发现与失效撤回。

Source科学保存、工作理解、Activity/长期知识、Result/Review保持独立。入口改进不增加启动必读、不强制每次几何导航，FREE A保持阶段适用来源边界。中英文启动协议在本分支加入的是可选短路由；本报告不修改P000和数学接纳标准。
