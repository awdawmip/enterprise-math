# Taskbook provenance gate 独立审计

结论：`INDEPENDENT_AUDIT_PASS_IN_SCOPE`，无阻断问题。
辅助维护工作包 `/root/exact_solver`；不构成正式 Driver review、数学采纳或发布授权。
审计 worktree：`D:/em/integration-owner-control-20260907`，基底 `16cc5663c191a73e997e3a973f589197d0694c89` 加 owner 当前维护增量。
本单元只新增本文，没有修改作者七路径、先前 38-test 源、生产权限、quarantine 或任何正式记录。

## 1. 冻结源码与实际语义

逐字节核对作者冻结摘要，并读新 checker 全文、三个测试文件、迁移报告，以及实际 record/fork/audit-only 验证依赖。

| 路径 | SHA256 / 状态 |
| --- | --- |
| `control_plane/check_taskbook_publication_provenance.py` | `5f86de1e6b0a04ffb318cebe338dba4d2cd48c70216a5be02dbd9bc970c9af85` |
| `.github/workflows/reference-integrity.yml` | `40db1865f198680ffbca817a5229e126872c8cc4ad8a1135c086fe1c0f839458` |
| `tests/test_taskbook_publication_provenance.py` | `7a26243d103f3ee0a130d56a9033552fb4dbfae84b9cb965d34653e152f64d1c` |
| `tests/test_research_task_registry_v2_compat.py` | `585a283c68f5e4d33ca2a6bb4ec6945e27a0bd5e908a0d7ee7b6323df46a524a` |
| `tests/test_v1_terminal_publication_provenance_unittest.py` | `cf1c7d6f8658b51dceb582ca20a58fefb19caaa8ff43150b63888434f3a6ae7f` |
| `research_notes/OWNER_TASKBOOK_PROVENANCE_GATE_MIGRATION_20260907.md` | `b4866221cd60626b0669634f63ab671e444068b7d1e1299e032f822ab3f0335e` |
| `control_plane/check_v1_task_registry_fault_isolated.py` | 已删除；基底 Git blob `b031766fa55194285c3b1a883d647c12756ef5cb` |

普通路径要求 record schema、task_id、POSIX 相对书路径、实际 Git blob 同时匹配，并要求 ACTIVE/既定 terminal state 与标准 V2 transaction。
不是仅凭 task_id 存在，也不是仅凭 transaction 字符串存在。
显式 retained 分支只能从已验证的 operational resolution 得到；单独向 predicate 传一个 retained-ID set 并不构成证书。
真正 gate 是 `audit(root)`，它先运行实际严格记录审计及既有精确错误隔离，再导出这些集合。

两个 `LEGACY_HANDOVERS` 分别绑定既有 manifest 的完整四字段行、固定 source commit/archive/schema/status、固定 record 和 book Git blobs。
新增第三个“同迁移 transaction”的记录不能进入该白名单。manifest 缺项、错行、record/book 漂移均导致失败。
R043 旧 head 的例外来自 `validated_quarantines` 的确切当前 fork 集；该分支仍核对标准 state、schema、task、路径及书 blob，
只提供 blocked 历史来源，不选择 operational head，不创建或延续 claim。它没有把 lineage-forward 行当作无条件 exact fork。

audit-only 来源不是直接相信行声明：`validated_rows` 检查固定 record/book pins、publication 所属 task/path、
nonoperational basis、直接 successor generation 或当前 fork membership、精确 envelope defect 与禁止权限 flags；
`audit_against` 再对实际错误集合拒绝 extra 和 stale/unused suppression。
本 gate 没有注册新 waiver，不能用同一个错误标签隐藏变化后的真实错误。

workflow 的实质差异只有原第 19 个 Python 命令及其说明替换为新 gate；文件末尾另补了换行。
旧 V1 mirror/schema/writer 检查随已授权物理迁移退役，没有用空 registry 或兼容 shim 冒充执行。

## 2. 独立实际检查

Python 为 `C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`，3.12.14。
真实运行 `-X utf8 -B control_plane/check_taskbook_publication_provenance.py`，退出码 0：
`PASS: published taskbooks have exact immutable publication provenance; no runtime authority granted.`

另有 11 项独立检查通过：

- 真实 TEMP 书/记录的八项入口检查：CLOSED provenance 可通过但无 current selection；同 task/blob 的另一文件路径为 orphan；
  task_id、blob、unknown state、伪造迁移 transaction 各自失败；重复 publication_id 失败；删除唯一记录后真 orphan 失败。
- 真实仓库三项检查：额外严格错误仍可见；移除一条已声明实际错误触发 stale suppression；
  R043 旧 head 的 historical key 存在，但 current map 缺席且 `operational.selection(...) is None`。

真实仓库里 `integrity.audit_task_records` 在 current-integrity 精确隔离后返回 129 条供 audit-only 层处理的错误，
其有效 audit-only 集恰为 129 条。这个数仅为本次诊断，不是新增白名单或未来固定期望。
作者 21 项测试的文件和断言已读；本文没有把作者的运行重标为独立运行，也未重复整套测试。
TEMP probe 仅 stub 全局 bootstrap，避免为合成根目录伪造无关全局治理文件；其 record/fork/audit-only 实现及文件字节均真实。
真实 repository CLI 已覆盖完整 bootstrap。

## 3. 明确边界

该 gate 保留原扫描域：`research_tasks/*.md` 中可解析且 `task_authority=PUBLISHED_REGISTERED`、base_state 非 DRAFT/BACKLOG 的书。
它不是对所有 Markdown 的语法或研究质量检查。已被记录引用的 malformed 书仍由严格记录审计拒绝。
terminal/blocked 来源可以有正确历史 provenance，而没有 current publication eligibility；这一区分由源码和独立检查共同确认。
本文不证明 GitHub Ubuntu CI 已通过，也不给 owner 其他维护路径或后续质量分片作背书。

## 4. 独立 TEMP probe 可接续源

以下代码在 worktree 根目录以该 Python 的 `-X utf8 -B -` 运行；只写拥有的临时目录并自动清理。
前八项为上述已执行 probe 的同一逻辑；最后三项读取实际仓库，不修改隔离注册表。

```python
import copy, json, tempfile
from pathlib import Path
from unittest import mock
from control_plane import check_taskbook_publication_provenance as g
import research_operational_publications as op

def write(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, sort_keys=True)+'\n', encoding='utf-8', newline='\n')

with tempfile.TemporaryDirectory(prefix='owner-provenance-independent-') as td:
    root=Path(td)
    book=root/'research_tasks/INDEPENDENT.md'
    book.parent.mkdir()
    meta={'task_id':'RS-INDEPENDENT-PROVENANCE','parent_objective_id':'OBJ-INDEPENDENT',
          'task_authority':'PUBLISHED_REGISTERED','base_state':'READY'}
    body='\n\n'.join('## '+s+'\n\nExplicit finite independent provenance fixture.'
                      for s in g.core.MANDATORY_BODY_SECTIONS)
    book.write_text(g.research_taskbook.render_taskbook(meta,body),encoding='utf-8',newline='\n')
    rec={'record_schema':g.core.RECORD_SCHEMA,'task_id':meta['task_id'],
         'registry_key':meta['task_id'],'parent_objective_id':meta['parent_objective_id'],
         'publication_id':'TP2-INDEPENDENT','record_state':'CLOSED','publication_generation':1,
         'publication_transaction':g.core.PUBLICATION_TRANSACTION_V2,
         'working_truth_granted':False,'canonical_promotion_granted':False,
         'taskbook_path':'research_tasks/INDEPENDENT.md','taskbook_blob_sha1':g.core.taskbook_blob(book)}
    rp=root/'research_task_records'/meta['task_id']/'TP2-INDEPENDENT.json'
    write(rp,rec)
    write(root/'templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json',{'schema':g.core.TASKBOOK_TEMPLATE})
    def audit():
        with mock.patch.object(g.bootstrap,'install'):
            return g.audit(root)
    assert audit()==[]
    assert meta['task_id'] not in g.fork.isolated_current_records(root)
    duplicate=book.with_name('SAME_TASK_AND_BLOB_OTHER_PATH.md')
    duplicate.write_bytes(book.read_bytes())
    assert any('SAME_TASK_AND_BLOB_OTHER_PATH.md' in e and g.ORPHAN_SUFFIX in e for e in audit())
    duplicate.unlink()
    for field,value,expected in [
        ('task_id','RS-FORGED','taskbook task_id mismatch'),
        ('taskbook_blob_sha1','sha1:'+'0'*40,'taskbook blob drift'),
        ('record_state','GHOST_STATE',g.ORPHAN_SUFFIX),
        ('publication_transaction','MIGRATED_FROM_V1_SHARED_REGISTRY',g.ORPHAN_SUFFIX)]:
        broken=copy.deepcopy(rec); broken[field]=value; write(rp,broken)
        assert any(expected in e for e in audit()),field
    write(rp,rec)
    other=root/'research_task_records/RS-DUPLICATE/TP2-INDEPENDENT.json'
    write(other,rec)
    assert any('duplicate publication_id' in e for e in audit())
    other.unlink()
    rp.unlink()
    assert any('no immutable publication record' in e for e in audit())

root=Path.cwd()
g.bootstrap.install(root)
raw=g.integrity.audit_task_records(root)
assert g.record_audit.audit_against(raw,root)==[]
extra='research_task_records/RS-INDEPENDENT/TP2-EXTRA.json: synthetic extra strict error'
assert extra in g.record_audit.audit_against(raw+[extra],root)
removed=sorted(g.record_audit.suppression_strings(root))[0]
assert any('stale or unused suppression' in e and removed in e
           for e in g.record_audit.audit_against([e for e in raw if e!=removed],root))
task='RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE'
records=g.core.iter_records(root)
record=next(r for r in records if r.get('publication_id')=='TP2-9D0A43C4F217B6E8C531')
key=(task,record['taskbook_path'],g.core.taskbook_blob(root/record['taskbook_path']))
assert key in g._blocked_fork_keys(root,records)
assert task not in g.fork.isolated_current_records(root)
assert op.selection(task,root) is None
print('PASS: 11 independent provenance checks')
```

最新共享 canonical lease 为 `main@ad231516dea09c6dd7108b94846f56a04d0b0f36`，
fetched `2026-09-07T10:21:35Z`、expires `2026-09-07T16:21:35Z`。
已在该相同 SHA 补读 bootstrap/manual/sync protocol/AGENTS；与旧 4fa7 入口的实际 policy 差异已复核。

Global-Knowledge-Sync: main@ad23151 / GLOBAL_KNOWLEDGE_V1
