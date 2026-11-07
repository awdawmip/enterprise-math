# 动态缺席证据：复验包

先读 `RESULT.md`。一般结论的完整证明位于 `dynamic_proofs.md` 与 `coverage_geometry.md`；原核结果的紧凑索引是 `incremental/summary.json`。

## 目录

- `incremental/`：本轮维护器、三策略比较、保护接线及六份原始执行结果。
- `parent_bundle/`：上轮 `residual_batch_vacancy.zip` 的完整原始内容，包含原BRC、身份和门程序依赖；未改其已有文件。
- `check_coverage_geometry.py` 与 `coverage_geometry_checks.json`：精确覆盖的整数控制层检查，独立于原核运行。
- `PROVENANCE.json`：本轮来源、数学状态、查询及登记状态。
- `MANIFEST.sha256`：包内文件清单及内容摘要。

## 复验命令

在本目录运行，Python 3及标准库即可。本轮实际运行时为Python 3.12.14。

```bash
python3 incremental/check_incremental_vacancy.py costs --out incremental/costs.json
python3 incremental/check_incremental_vacancy.py regressions --out incremental/regressions.json
python3 incremental/check_incremental_vacancy.py audit --slots 1 --out incremental/audit_r1.json
python3 incremental/check_incremental_vacancy.py audit --slots 2 --out incremental/audit_r2.json
python3 incremental/check_incremental_vacancy.py omissions --out incremental/omissions.json
python3 incremental/check_incremental_vacancy.py protected --out incremental/protected.json
python3 check_coverage_geometry.py
```

核心原命令、额外缺席位读、业务身份位读分别计量。所有一般保证都使用报告明确列出的持有区间与观察来源条件。`protected` 验证两种门相位下的逐边界完整进入尝试，不等同于全部原语交错图。

本轮Source落点为 `awdawmip/enterprise-math:research_notes/chatgpt_direct/20261107_dynamic_vacancy_66978b96/`。项目仓库保存主报告、新证明、新代码与结果；完整原依赖随此ZIP交付。
