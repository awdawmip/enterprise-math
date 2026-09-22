# ��ͨ ChatGPT��ͨ�� GitHub �ƽ��о�

Protocol: `EM_CHAT_CONTROL_V1` �� English: [CHATGPT_ORDINARY_CONTROL.en.md](CHATGPT_ORDINARY_CONTROL.en.md)

��ͨ ChatGPT ʹ������ GitHub �����ύ���󣬷��������ü��� Enterprise Math ԭ�����Ƴ����ٰѻ�ִд��ԭ Issue��**�Ի����� Python��CLI��git clone������ checkout ��ɼ�����Ŀ MCP ���ߣ�Ҳ���л��� Work��** �Ի��Ը����о���֤���жϺ������������ƴ���ɹ���֤����ѧ��ȷ������ʵ�ʿ��ŷ�Χ�ȿ� `status` �� `enabled`��

## 1. ׼ȷ����������ʽ

�Ƚ����˻�֪ʶ�⵱ǰ��Ч `main` ���գ��ڸù̶� SHA ��ȡ `awdawmip/chatgpt-global-knowledge` �� `00_BOOTSTRAP.md`��`OPERATING_MANUAL.md` �� `projects/enterprise-math/00_EM_PROJECT_BOOTSTRAP.md`��**P000 ��׼ȷ�����ͬһ��֪ʶ�� repository��ͬһ�� SHA �µ� `projects/enterprise-math/P000_REALITY_FOUNDATION.json`��** ���� Enterprise Math ȫ���� P000 �ļ�����֮�󰴽�ɫ��ȡ��ǰ `awdawmip/enterprise-math` �Ŀ��ƺ�ͬ�;�ȷ����֪ʶ�⡢��ǰ���� Source�������о�֤�ݷֱ�̶������໥���ǡ�

��˽�� `awdawmip/kimi-query-bridge` һ�δ��� Issue���� `em:control` ��ǩ������Ϊ `[EM-CONTROL] <request_id>`��**���ı���ǡ��һ�� `json` ����Χ��**������һ�� JSON ���󣻲���˵�����֡������� JSON������Ϊֻ�� `status` ʾ����ʹ��ʱ�滻Ϊ���Ի��ȶ���ʶ���µ�Ψһ���� ID��

```json
{"schema":"EM_CHAT_CONTROL_V1","conversation_id":"chat-example-20260922","request_id":"status-20260922-example-01","operation":"status","payload":{}}
```

| �ֶ� | ���� |
|---|---|
| `schema` | �̶� `EM_CHAT_CONTROL_V1` |
| `conversation_id` | ���Ի���ѡ�ȶ��߼� ID��1�C160 �ַ�����ĸ/���ֿ�ͷ���������ĸ�����֡�`: / _ . -`������ƽ̨��֤���� |
| `request_id` | һ���߼�����Ψһ ID��1�C128 �ַ�����ĸ/���ֿ�ͷ���������ĸ�����֡�`_ . -` |
| `operation` | �±���ʵ�ʲ����� |
| `payload` | ֻ���ò��������ֶΣ�δ֪�ֶλ�ܾ� |
| `sha256` | **��ʡ�ԣ���ͨ�Ի�Ĭ��ʡ��**�����������Ǽ��㲢�ش�����ʽ�ṩ�������ܾ� |

ժҪ�㷨��ȥ�� `sha256` �󣬵ݹ��������������� JSON���� ASCII ԭ�� UTF-8����ĩβ���е� SHA-256���ͻ��˲���Ҫ���㣬�����ܲ¡��ظ� JSON ����NaN/Infinity��ƾ֤�ֶξ��ܾ����������˽�⼰������ GitHub actor������ʱ���ġ�ִ��ǰ˫��ָ�ƺͳ־û��ݵ�״̬��

������Ҫ�༭ Issue ���ġ�������ǩ��Ҳ��Ҫ��ͬһ�߼������½��ظ� Issue�������״�����Ҫ�󴴽������ʱ��һ������ 24 Сʱ�ڡ�ÿ�� conversation ��� 5 ��δ��������ͨ���𲽷��͡���ͨ payload ��� 16 KiB���淶 envelope ��� 32 KiB����֤��ʹ�÷�Ƭ�ϴ���

## 2. �ض���ֻ������

�״ε�Լ 30 ���ȡԭ Issue��ִ����Լÿ 15 ���顣�������ۺ� `EM_CHAT_CONTROL_RECEIPT_V1` �� `<!-- em-control:... -->` ��ǡ��˶� `issue_number`��`conversation_id`��`request_id`������� `request_sha256`���ڲ� `bridge_receipt` �� `operation`��`status`��`receipt`��`error`��`next_actions`��**��� `adapter_status=COMPLETE` Ҳ���ܰ�װ FAILED/OUTCOME_UNKNOWN������ʾ�о��ɹ���** ��ƥ���ڲ��ִ��ʵ�� Source readback Ϊ׼��

| operation | payload ���� | ��ѡ�ֶ�����; |
|---|---|---|
| `status` | �ޣ�`{}` | ���ز�������enabled����ǰ conversation ����Ự���������о�Ȩ�� |
| `dispatch` | �� | `kind`: `RESEARCH`��Ĭ�ϣ���`GOVERNANCE`��`ANY`����ѡ `priority`: `P0`��`P1`��`P2`��`P3`��ʡ�Ա�����ͨ·�ɣ���ʽ null �ܾ����˶�ԭ�� `selection_filter` |
| `pre_final` | `parent_liveness` ��������Ӧ·���ֶ� | ֻ������ԭ�����ջظ��ţ�ע�ᡢfreeze��review �� close �ɹ��������������ջظ� |
| `tasks` | �� | `limit` Ĭ�� 20��1�C100��`cursor`��`dispatch_state`����ҳ���÷��� cursor |
| `task` / `continuation` | `task_id` | ��ȷ����/���Ӱ������ִ�Ựʱ�����Զ��� |
| `artifact` | `packet_request_id`, `path` | `start_char=0`, `char_count=12000`����� 24000����`source_commit`��`related_start=0`�������ɹ��� continuation/artifact/publish_checkpoint ����ֻ��������֤�� |
| `receipt` | `target_request_id` | `start_char=0`, `char_count=12000`����� 24000������ȡ�� conversation Ŀ���ִ������ JSON ��ҳ |
| `reconcile` | `target_request_id` | Э���� conversation ���������δ֪Զ�˽�������ظ�ԭ���� |

���������ѯ�� payload Ϊ `{"task_id":"<ʵ�� Task-ID>"}`������ִ�� `receipt_truncated=true` ʱ�����µ�ֻ�� `receipt` �����ҳ���� `next_start_char` ���������� `sha256` �� `source_status`����ҳ���ı������������ʱ��������ȫ����`artifact` �������ֽڹ�ϣ����Ҳ�������Ի��Ѿ���������ҳ��

QUEUED/RUNNING/POSTING/RECONCILE ʱ������ԭ����OUTCOME_UNKNOWN ʱ�� `reconcile`������ ID ����д�롣ֻ��ʵ�ʹ淶 `NO_DISPATCH` ��֧�ֶ�Ӧ kind/ʱ�����ɷ���û�л�ִ��Ȩ�޴�������������Ծ owner ����� Result �����ǡ������񡱡�

## 3. ����Ự���о�Ա˳��

����ͬ conversation �Ự���� `status` �鿴����������Ϊÿ���������´�����ȷ����ִ��ʱ��`session_start` ����ͨ�о�Աʾ��Ϊ��

```json
{"schema":"EM_CHAT_CONTROL_V1","conversation_id":"chat-example-20260922","request_id":"session-20260922-example-02","operation":"session_start","payload":{"role":"RESEARCHER","research_mode":"TASK_RESEARCH","prior_contribution_ids":[]}}
```

`task_id` ��ʡ�ԣ����оɹ������ݣ��������� `prior_contribution_ids`��ʾ��������ֻ��ʾȷʵû�м������ס�Driver �� `role=RESEARCH_DRIVER`��`research_mode=RESEARCH_DRIVER`����ɫ/ģʽ��������һ�� conversation ͬʱֻ��һ��δ�رշ���Ự���������� session��Researcher/Driver ID��CLAIM��ER��publication/taskbook pin��generation ����Ȩ��**�Ի�ֻ��ǰһ�� request_id������ pin������ƴ���ݣ����� session_key��** ˽�� session key �����ڷ���������д GitHub��

�о�Աͨ��ִ�� `dispatch �� session_start �� prepare �� claim �� open �� artifact_upload �� publish_checkpoint �� freeze`��ÿ���������õ�ǰһ�� SUCCEEDED �����ʵ�������Լ����ע��� prepare �ɹ�������ȡ�� CLAIM��

| operation | payload ���� | ��Ϊ/ע�� |
|---|---|---|
| `prepare` | `dispatch_request_id` | ָ��ɹ� dispatch��������Ϸ� route ׼������ѡ `execution_branch` ֻ���� `main`��`allowed_outputs` ֻ��Ϊ�գ�ͨ��ʡ�� |
| `prepare_exact` | `task_request_id` | ָ��ɹ� task/continuation���ʺ�����ȷ Task����ִ��ԭ����ִ����������Ȩ��� |
| `claim` | `prepare_request_id` | ָ��ɹ� prepare/prepare_exact/continuation_prepare���˶���ʵ��ʤ CLAIM |
| `open` | `claim_request_id` | ָ��ɹ� claim��ȡ�õ�ǰִ����Ȩ��**�� open ���� ID ��������� `run_request_id`** |
| `resume` | `run_request_id` | ͬ�Ự�ָ����� open/resume���ɹ������� resume ���� ID���� generation ʧЧ |
| `artifact_upload` | `upload_id`, `filename`, `part_index`, `content` | `final=false` Ĭ�ϣ�ĩƬ���� true��ֻ�ݴ��ı�����ִ���ϴ����� |
| `publish_checkpoint` | `run_request_id`, `upload_request_ids`, `completed_units`, `current_unfinished_unit`, `next_action`, `do_not_repeat` | `release=false` Ĭ�ϣ��ɹ������� PROGRESS��`release=true` ���ڷ����� CONTINUATION ���ͷš�**׼�� freeze ʱ���� false** |
| `freeze` | `run_request_id`, `publication_request_id`, `return_filename`, `metadata` | publication_request_id ָ�� run �ĳɹ� publish_checkpoint��return_filename �������Լ����ļ��� |
| `session_close` | `reason` | �д��������󡢻�Ծ CLAIM ��δ�����ϴ�ʱ�ܾ����ȳ־û�/�Ϸ����� |

�ϴ��� `upload_id` �� `filename` Ϊ 1�C96 �ַ������ƣ���ĸ/���ֿ�ͷ��������ĸ�����֡�`_ . -`����Ŀ¼б�ܣ���ÿ���ļ��� `part_index=0` ����������������� 128��ÿƬ��� 16000 UTF-8 �ֽ��� JSON ת���ʾ������ 24000 �ֽڣ����ĳ�������СƬ�����ļ���� 1 MiB��һ����� 16 �ļ����� 4 MiB��ÿƬ���µ����� ID����ͬ�ļ���Ƭ���� upload_id/filename��`upload_request_ids` ��ÿ���ļ�**���һƬ complete �ɹ�����**�� ID������ upload_id��Ҳ����ȫ��Ƭ ID��

checkpoint �� `completed_units`��`do_not_repeat` ���ַ������飻`current_unfinished_unit`��`next_action` �Ƿǿ��ַ�������׼������ Result����ȷʣ�������ʽ��װ/������飬����١�ȫ����ɡ���֤�ݷ������ɷ��񷵻����� immutable blob URL�������á�branch@commit + path���Զ��崮��

`freeze.metadata` **ǡ����������о��߸�����ʵ֤����ȷ��д**����ԭ����ͬ��������/ȡֵ�����ܰѲ������� PASS ��ΪĬ�ϣ�

| metadata �ֶ� | ��������ʵ������ |
|---|---|
| `terminal_verdict` | �������鷶Χ��ʵ���վ��жϣ������游Ŀ����� |
| `hard_target_disposition` | ӲĿ��ʵ�����㡢δ��������޵��ж� |
| `unresolved_residue` | ��δ֤������֤����ɵĲ��༰��Χ |
| `method_harvest` | ʵ�ʷ����ջ�/�ɸ����������ȷȱʧ |
| `independence_status` | ��ʵ�������빱���ص���� |
| `source_exposure_status` | ��ʵ��Դ��¶/ä��״̬�������� ID ���� |
| `next_control_plane_recommendation` | ����ǰ�����ͬ�������/���ӽ��� |

���������Ȩ��ǰ run ���� ER����ȷ taskbook pin �� write_authorization��ԭ�� Result ͨ��׼�롢Source ���������� readback �󣬲ŷ� frozen HANDOFF���ϴ��ɹ����ݸ� RR������ pin ������Ȩ��ִ������ǰ���ᡣ�ɹ� freeze ���ǵȴ����� Driver review��������ѧ���ɡ�

## 4. ����ǰ�صĽ���

���� `continuation` �������� `artifact` �˶������/δ��/��/δ֪��Ԫ����������Ч�ɹ���`continuation_prepare` ��ǰֻ֧��**���й淶�ͷš��� live claim��runtime.dispatch_state=NEEDS_DISPATCH** ��ǰ�Σ���֧��ͨ���ͻ����Ա�ʧ����ռ��

���� `packet_request_id`���ɹ� continuation����`reason`����������� `persisted_checkpoint.state=SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED`��ֻ����������񱣴�ԭ frontier�������ܸ��ǡ��ɸ�ʽǰ�ػ��� `artifact_request_ids`����ʵ������ hash ����� artifact ���� ID ���飩�� `frontier_notes`��ǡ�� `completed_units`��`current_unfinished_unit`��`next_action`��`do_not_repeat`��������һ��֤�ݱ������ڰ�����֤�� last progress��������Դ�ɷ���̳С�׼���ɹ������� claim/open��������Դ/ר�� lane �� frozen/��Ծ״̬������·�ɴ���������ǿ�� reopen��

## 5. Driver ��ʽ���

ʹ�ö����� Driver conversation/��ʵ����Ự������ȫ���������ݣ��� ID ��֤�������ԡ�˳��Ϊ `session_start(RESEARCH_DRIVER) �� driver_activate �� continuation �� artifact(��ȷ Result��֤��) �� artifact_upload(��������� followup spec) �� driver_publish �� review`����������Ȩ�Ự����ʹ�ã����������

| operation | payload ���� | ��ѡ��/У�� |
|---|---|---|
| `driver_activate` | `reason` | `previous_authority` Ĭ�� null��Chat �ӿڲ�֧�ֽ���滻�ִ� Driver���� null �ܾ� |
| `driver_publish` | `upload_request_ids` | �Լ��Ự�ı��漰 followup spec ��������ϴ����� ID |
| `review` | `publication_request_id`, `result_request_id`, `review_filename`, `metadata` | `followup_spec_filename` ��ѡ�����״ι淶 review ��Ҫ�ѷ�����ԭ�� followup spec�������ÿ�ռλ���� |

`result_request_id` ����ָ�� Driver **�� conversation �ɹ��� `artifact` ����**����·��Ϊʵ�� `research_result_records/<Task-ID>/<Result-ID>.json` �������ײ��ֽ� hash �Ѻ��飻���� worker �� freeze ���󡣴� Result ��ҳ�����Ҫ���ݺ�����顣�ŷ�������ʵ�� artifact �Զ����� `result_id`��`expected_result_sha256`���Ի������� SHA��Ҳ���ֳ��������ֶΡ�

`review.metadata` ���� `disposition`��`destination_class`��`reviewer_contribution_ids`����ѡ `destination_ref_or_none`��Ĭ�� null���������� Driver ����֤�������������񲻻��Զ��� ACCEPTED ��ѡ���̡��淶 writer �Լ����ʵ ACTIVE DA��session һ�¡�Result ����/�����߸��롢���� Result �ֽڼ� HEAD �����󶨡����淢��������ʽ review����ʽ�ض�������˶�ʵ�� review/followup�������� PASS �Զ���������������Ƹ�Ŀ����ɡ�

## 6. �����������һ��

| ����/״̬ | ��һ���� |
|---|---|
| `ONE_JSON_BLOCK_REQUIRED` / `EXACT_CHAT_OPERATION_FIELDS_REQUIRED` | �˶Ե� JSON Χ��/�ֶα���ȷ��δ�������������� ID ��������༭�� Issue |
| `ENVELOPE_HASH_MISMATCH` / `CHAT_REQUEST_SHA256_MISMATCH` | ���� hash��ȷ�Ͼܾ����� ID ʡ�� sha256 |
| `PREREQUISITE_NOT_SUCCEEDED` | ��ԭ�������󵽳ɹ�����ȷʧ�ܣ��پ��������������� |
| `CHAT_SESSION_START_REQUIRED` | ����ɱ� conversation �� session_start������� key |
| `CHAT_ACTIVE_SESSION_EXISTS_USE_EXISTING_OR_CLOSE` | status �鿴���������лỰ��ȷ�����ʱ����ɽ����� close |
| `CHAT_DEPENDENCY_SESSION_MISMATCH` / `CHAT_RUN_SESSION_MISMATCH` | �˶Ա��Ự�����������ܸ��Ʊ��˵� request_id ��� generation |
| `STALE_EXECUTOR_GENERATION` / `CANONICAL_CLAIM_FENCED` | �ȶ���ǰ continuation��ֻ���Ϸ�����Ȩ�ָ������ط���д�� |
| `CHAT_CONTINUATION_REQUIRES_NATIVE_RELEASE_NO_LIVE_TAKEOVER` | ������ǰ owner/frozen ״̬���߹淶���ƻָ������������� |
| `COMPLETE_OWN_UPLOAD_REQUIRED` | ���ĩƬ final=true/complete ����ȷ�����Ƭ request_id |
| `EXACT_NATIVE_FREEZE_FIELDS_REQUIRED` | ����ǡ��������ʵ metadata������α�� PASS |
| `VERIFIED_RESULT_ARTIFACT_REQUIRED` | �ӱ� Driver continuation ʵ�ʶ�ȡ�Ϸ� Result artifact����ֱ���ύ�²� hash |
| `*_DISABLED` / Ȩ�޻�ԭ��׼����� | ��¼��������/Ȩ�޺� Task/δ�굥Ԫ����α����Ȩ�����ĳ� NO_DISPATCH |
| `OUTCOME_UNKNOWN` / `SUBMIT_UNKNOWN` | ����ԭ���󼰳ɹ�����ԭ Issue�� reconcile�������� ID�ظ�д�� |
| `receipt_truncated=true` | �� receipt ��ҳ��ȡ��������·��ժҪ������ԭʼ���� |

״̬/�����޸��������޸���ʷ�¼������� DA/ER/RR/DR��P000��FREE ����ǽ������Χ��Working Truth/Foundation����������֤������ȫ��������

## 7. ���ձ߽�

ֻ�� canary ʹ�� status����ȷ continuation/artifact����ʡ�� sha256����ҪΪ��չʾ��·�½���������ȡ��Ծ����򼤻�� Driver����ʽ�ջ�����ԭ����ǰ�Ϸ� dispatch/owner ���û���Ȩ�½��У��������֡��������������о���ʽ���ᡱ��Driver��ʽ��顱�͡���ѧ/ʵ����֤����

���������ƽӿڲ��ṩ���� shell��Ҳ�������ϴ�����ѧ���룻pinned spectralDNS/shenfun/MPI/FFTW��Lean ������ʵ������ʵ������������ָ��֤�ݡ�����ȱʧʱ����ǰ������Сδ�굥Ԫ�����ظ���ѧ���մ��������ý�ƾ�������/��ʾ��������ԭ��ͨ ChatGPT �����ճɹ���

## 8. ���ջظ�ǰ��ֻ�����

���ջظ�ǰ��ͨ��ͬһ GitHub ͨ���ύ `pre_final`���ɷ�����������׼�� Source �� `tools/research_runtime_guard.py` ԭ���оݡ�freeze/review �ɹ��� session_close �������� PRE_FINAL��`status=SUCCEEDED` ��ָ������ɣ������ȡ `receipt.result.final_allowed` �� `required_action`��false ʱ����ָ���������ü�鲻����ѧ��ִ��Ȩ�ޡ�

- ��ʽ�����Ѷ�����ѽ��ӣ������Ự�ɹ� open/resume �� `run_request_id`���ɹ� freeze �� release=true �� publish_checkpoint ��Ӧ `completion_request_id`���Լ� `parent_liveness`���Ѿ�����/�رյ���ʷ run �Կɼ�飬��������Ȩ�ѽ����о���������У����ʵ��ִ��session �� Source ִ����ͼ�����ӵ�ǰ Source �Ƶ���Ŀ���Ƿ�رգ��ͻ����� COMPLETE ���ܸ��ǡ�������ʽ״̬�ݲ�֧�֣���ð����ɡ�
- ����ʽ run �� Driver ���ƹ��������Լ��� `session_request_id` �� `parent_liveness`����ѡ `research_mode` ֻ��Ϊ `RESEARCH_DRIVER`���� Driver session ������ʽ run ʱ��������ʽ·����
- ���߼��Ự��δ�����о� session ��ά���������� `research_mode=CONTROL_PLANE_MAINTENANCE` �� `parent_liveness`������ɾȥ�����о��󶨽�����ά��·����

`parent_liveness` ������ʵԭ��Ŀ�꣬�ϸ�����˸������ֶΣ�`parent_objective_complete`��`user_requested_stop_pause_review_or_wait`��`parent_hard_blocker`��`platform_or_tool_hard_limit`��`independent_safe_work_exhausted`��`same_action_repeated_without_state_change`��`supported_alternative_available`��`parent_state_recomputed_without_change`�����зǸ����� `executable_next_actions`����ѡ���� `continuation_lease_active`������Ϊ��� final ���鹹�û�ֹͣҪ���Ӳ���ơ���ʽ��Ŀ�����״̬�� Source �����Ƶ���closure δ��ʵʱ��ȷ���� false ���޸�/�˶Զ����������ִ�е� Source pin �� evaluated-state hash��
