# 本轮增量复验包：目标定向补证与分组维护

主报告为源码目录的 `RESULT.md`，增量ZIP内对应 `RESULT_DIRECTED.md`。完整动态证明见 `directed_proofs.md`，首次界及控制复验说明见 `bounds/directed_bounds.md`。

## 依赖与布局

本轮沿用上轮完整复验包中的 `incremental/` 与 `parent_bundle/`，不重复打包其已有内容。

上轮依赖包：[dynamic_vacancy_evidence.zip](https://chatgpt.com/library?file_id=libfile_f3e9b409fb80819189e09f94a4aca75f&account_id=personal)。固定研究来源为 EM `fda5f43aca54cc1f3c56b3628ce972c2266589f2`。

先把上轮ZIP解压到一个目录，再把本轮 `directed_vacancy_evidence.zip` 解压到同一目录。两个包共同形成 `dynamic_vacancy_evidence/`；本轮写入的新文件名均不覆盖上轮报告、证据或依赖。

在形成的 `dynamic_vacancy_evidence/` 中，以下四个目录应并列：

- `parent_bundle/`：原BRC与三元程序依赖，来自上轮包。
- `incremental/`：上轮前缀缓存维护器，来自上轮包。
- `directed/`：本轮定向树、原核运行和结果。
- `bounds/`：本轮整数控制证明、检查器和结果。

## 运行

Python 3及标准库即可；实际执行版本为3.12.14。

```bash
cd dynamic_vacancy_evidence
python3 directed/check_directed_vacancy.py costs --out directed/costs.json
python3 directed/check_directed_vacancy.py pure_creates --out directed/pure_batch_comparison.json
python3 directed/check_directed_vacancy.py regressions --out directed/regressions.json
python3 directed/check_directed_vacancy.py audit --slots 1 --out directed/audit_r1.json
python3 directed/check_directed_vacancy.py audit --slots 2 --out directed/audit_r2.json
python3 directed/check_directed_vacancy.py omissions --out directed/omissions.json
python3 directed/check_directed_vacancy.py protected --out directed/protected.json
python3 bounds/check_directed_bounds.py
python3 bounds/check_directed_scale.py
```

`directed/summary.json` 是原核执行的紧凑索引。`bounds/` 中的完整值只用作测试回调与核对，结果明确标为控制层。原BRC命令、额外缺席读、业务身份读和控制事件分别计量。

所有新结果已有成功执行记录。交付目录另重跑纯创建比较和控制规模族，核对增量包与原依赖的接合；其余已完成检查复用原结果。
