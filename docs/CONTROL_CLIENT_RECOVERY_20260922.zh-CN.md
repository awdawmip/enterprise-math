# ��ʱ�ͻ��ˣ����������� Driver ����

## ��ͨ ChatGPT ��ֱ����ڣ�2026-09-22��

��ͨ ChatGPT Ĭ��ʹ�� [��ͨ�Ի�����ָ��](CHATGPT_ORDINARY_CONTROL.zh-CN.md) ��˽�� GitHub ������ڣ���Ҫ��ɼ�����Ŀ MCP ������ Source/Python ���������з���������ͬһ�׹淶�Ự��CLAIM��ִ�м�¼��Result �� Driver writer���ͻ��˲�����ȱ checkout/CLI ΪĬ��������Ҳ���ֹ�ƴ����ЩȨ����¼��P000 Ӧ�ӵ�ǰ��Ч�� `awdawmip/chatgpt-global-knowledge` ���ն�ȡ `projects/enterprise-math/P000_REALITY_FOUNDATION.json`����Ҫ�ڱ��ֿ��·����

����ڲ������о���ɫ����ѧ����Ȩ����ǰ����������ʷ�������ԡ���Ծ����Ȩ��׼���Ž��ճ�ִ�С��Ѵ��ڵ���Ŀ MCP/native ·���Կ��á���Ҫԭ��ʵ�黷������ѧ��������ȡ����ʵʵ��������֤�ݣ�������ڿ��ò�����ʵ������ɡ�


Status: `ACTIVE_CLIENT_GUIDANCE / NO_NEW_RUNTIME_AUTHORITY / NO_NEW_MATHEMATICS`
Effective: `2026-09-22`
Authority: current `control_plane/current_control_authority.json`, `research_dispatch_contract.json`, `control_plane/research_continuation.py`, and `docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md`. ���Ľ���������ڣ����޸�������Ȩ������֤�ݽ��ɹ��򡣺���Դ�������ȡ�

## 1. ֻ�ӱ��ι淶��ִ�ж��Ƿ���ɷ�

��ͨ ChatGPT ��˽�� `awdawmip/kimi-query-bridge` �ύ `em:control` / `EM_CHAT_CONTROL_V1` ��������һ�� JSON Χ�������ɷ���˵������� `research_control_dispatch.py` ��ȡ��ʵ���������ȶ��� Issue #240 ���ۿ��ա���ȷѡ���ֱ�� MCP/native ·���Կ��ã��� ChatGPT dispatch bridge ��Ϊ��ʽ����ģʽ������Ĭ����ڻ췢������ʡ���¼�������һ����״̬����Ҳ���ð��ϴ����졢���� latest receipt��������ȼ������ѱ���ȡ���ļ�����Ϊ�յ��ɵ�ǰ������֤�ݡ�

Ĭ�ϴ�**ԭ���� Issue**��ȡ `EM_CHAT_CONTROL_RECEIPT_V1`���˶� request_id��conversation_id��operation������������ժҪ���Լ��ڲ� bridge_receipt �� status��Source/�¼����պ� route����� COMPLETE ������ԭ���ɹ������� request ����������ȡ��ֻ����ʽʹ�þ� bridge ʱ�Ŷ� `control_plane/chatgpt_dispatch_receipts/<request_id>.json` �����ɺ�ͬ�˶� source_sha/kind/generated_at��������ʷ������·�����ı䵱ǰĬ����ڡ�

�ͻ��˱��뱣���������𣬲����� canonical ״̬�ֶΣ�

| ʵ�ʹ۲� | �����ȡ�Ķ��������� |
|---|---|
| `CLAIM_NEW_OWNER` | ���ڿ��ɷ�Ŀ�ꣻ�����صľ�ȷ����׼����Ԥ�졢������ʵ CLAIM �������ʤ�ߡ�����˵������ |
| `PREPARE_SUCCESSOR_CLAIM` | ����ǰ�� durable frontier��׼����ʵ��ִ���ߺ�ǰ�� CAS������������ |
| `VERIFY_SESSION_LIVENESS` | ���龫ȷ����CLAIM �Ļ������������Ҳ�����Զ���ռ���ɡ� |
| `SUPPORTED_NATIVE_LANE_ADAPTER_REQUIRED` | ���� lane ����Ȩ��ʹ������ר����ڣ�����ȫ�������� |
| ���� `NO_DISPATCH` | ֻ��˵����ִ�����ǵ� kind��ָ������ʱ���޿��ɷ�Ŀ�ꡣRESEARCH ������ GOVERNANCE��GOVERNANCE �������񲻵����޴��� RR�� |
| û�л�ִ����ȡʧ�ܻ������������� | ����ȡ�õ�ǰ״̬��ȱ�ľ�������������д�������� |
| ��ѡ�����񣬵�ȱ��ʵ��������������֤���� | �������� ID����ȷδ�굥Ԫ��ȱʧ������֤�ݣ���α�� BLOCK��DONE����ð�������� |

�о�Ա��ͨ�� ANY �� GOVERNANCE �������ȡ�� Driver Ȩ�ޡ�Driver ������鶳�� Result��review��follow-up���ټ�� GOVERNANCE ·�ɣ���������Ŀ��������ϰ�������ֹ���������������������κ��������ѡ���Ա��뾭����ǰ�淶��ڣ������˹����� selector��

### 1.1 ������ƥ����ظ��ɷ����ǡ��ٴ��о���

������ƥ��� canonical `RESEARCH` ��ִ�ٴη���ͬһ���񣬶����������һ���ѽ��ɵ� durable `CONTINUATION` ��ȷ��������ȫ��������

1. ��ѧ�����ף�֤����ʵ���о���Ԫ�Ѿ���ǲ���֤��֧��Ϊ `VERIFIED_COMPLETE`��
2. Ψһ `UNFINISHED` ��Ԫֻ������ canonical execution-record��Result freeze���̶� native ʵ�顢���� latest-main ȫ����֤��������ȷ�����ض�ִ�������Ķ�����
3. ���һ��ִ�������¾�ȷ durable frontier ����ȷ��¼��ǰͬ�� ChatGPT ִ������ȱ�ٸ�������
4. �Ը� handoff ������״̬��durable frontier�����������Լ������Ȩû�г��ֿ���֤�仯��

��ͻ��˲��ý�Ϊ���ٴ�֤�����������������ˡ����ظ����� CLAIM���ظ�����ͬ�� `CONTINUATION`�������Ѿ���ɵ��о�������󱨳� `NO_DISPATCH`����ʱ׼ȷ����Ϊ `CAPABILITY_MISMATCH_HEAD_OF_LINE`����������Ϊ��ǰ canonical Ŀ�꣬������ owner ״̬������ frontier����¼��ȱ�������ȴ������߱��������ĺϷ�ִ�������������µ� canonical dispatch state��Ҳ���ı��������ȼ���claimable����ѧ״̬�� Result ״̬��

��һ����ֻ����**ͬ��������������Ϣ claim��release ѭ��**������Ȩ�ͻ����˹����� canonical selector����һ������ƥ���ִ���������֣��Դӱ�����ʵ��ִ����� durable frontier ������ȡ��ͬһ��������µ���ѧδ�굥Ԫ��ǰ�ر仯�������仯ʱ��Ҳ������������ͨ canonical ���̡�

˽�� GitHub �����ԭ�� writer ����������ʵ����ִ�������仯�������ٽ�ƾ ChatGPT ����û�� checkout���� ER/Result �������ù���� mismatch������˲���ִ�еĿ�ѧʵ�顢ȫ����֤������ʵȨ�޴����԰����Ե�ǰ֤�ݱ�����

���� head-of-line mismatch �������������о���ֻ�о߱���ǰ source-backed Driver authority ���� `AUTHORIZE` �������õ� typed `research_task_delegation_scope` ʱ��Driver �ſ�ʹ������ canonical `assigned_research_task` ��ڣ���**��һ�����е�ǰ����**����������о�Ա��session�����������Լ��� publication��parent��assignment��CLAIM ������ʱ�Ž���û��������ȷ��Ȩʱ���������о�Ա��Ѳ��Ա����ͨ�ͻ��������������ȼ���α�� `BLOCKED`���޸����������ڶ� selector����ʱ������Ҫ��ʵ��������ʵ��������������

GOVERNANCE ͬ������� canonical ����Ŀ��ֻʣ���� latest-main checkout �е�ȫ��У�飬����ǰ Driver ����û�иû�����Ӧ��¼ `LOCAL_VALIDATION_PENDING`������ͨ���ظ� CLAIM��HANDOFF��α�� review������ AUTHORIZE ���ȱ MCP ��ͬ��Ȩ��ʧ���������չ��Driver �Լ������ɶ��������Ķ��� Result��review/follow-up ����������Ȩ���ڿ������

## 2. MCP ���� Driver д���Ψһִ��·��

`control_plane/research_continuation.py::require_review_authority` �ڱ��κ���Դ����Ҫ�󣺵�ǰ��ʵ������ִ�� session����ǰ source-backed ACTIVE Driver authority����Ȩ source_body �� reviewer_session_id ��ȷƥ�䡢��ʽ���������������� Result ���ߣ����������ص�����û��Ҫ�� session ������� MCP ǰ׺��Ҳû��Ҫ��ú����ĵ�����ֻ���� MCP ����

����Ⱥ˶Ա���ʵ�ʿ����������������һ�׼�� MCP ��ʹ����ԭ�� session��Driver activation��review ���ߣ��кϷ��������� Source ������ Driver ��ʹ������ԭ����Ȩ���̼� `tools/research_result_records.py review`��������Ϊȱ�� MCP ���߾���������ԭ��·��������Ȩ��������

����·��������ʵȡ�ñ��� Driver ��Ȩ��������ʵִ�лỰ��Դ�������� canonical writer ��ȫ����顣���ðѱ�������αװ�� MCP ����ǩ����ƽ̨��֤���ݣ����ý������� session��ID��key ���ѳ�����Ȩ���������� DA��RR��DR��write_authorization ����ſ��ձ�ǡ�MCP ר������ƾ֤��У����ʵ��ʹ�� MCP ʱ��Ȼ���á�

��ͨ GitHub �Ի���ʹ�÷����ԭ�� writer������ʵ��ԭ����֤��������Ȩ���Բ����ã�׼ȷ��¼ `LOCAL_VALIDATION_PENDING` ��ǰԭ�����󣬲�������ִ�еĻָ����ϡ�����ȷѡ��ı���·�������غϷ����� Source/����ȱʧ���Ǹ�·������ʵ���������ܾݴ˷��ѿ��õķ����·����������Ȩ���������ܽ����޸���ʾ�ʡ����� AUTHORIZE ���ۻ򴴽��� ID ���ƽ��������ɵĶ���֤�����ɱ���Ϊ�ݸ壬���ݸ岻������ʽ review��

## 3. CLAIM ��ɹ����Ӳ����ڸ�ʽ�����ٳɹ�

ʹ�õ�ǰ�淶������������Ԥ�죬�����ִλ��������ƴ�� Researcher-ID�����������ʵ��������۱��뱻 canonical reducer ����Ϊ��ʤ CLAIM ��ȡ��ִ��Ȩ��ignored CLAIM ����ͨ������ HANDOFF �����Ч����Ȩ��

�Ա������¼���������ʵ��֧�����棬���������� bytes ����Դ������Ϊ predecessor evidence����׷�ϷǷ�ִ��Ȩ������ʷ��ִ���µĺϷ�ִ��ֻ�����Ѻ���ɹ���������Сδ�굥Ԫ��������ԭ�����뱩¶��ʷ���������Χ�ڿɶ���Ļش�ʱ��ʹ�ù淶 Result writer �Ͷ��� HANDOFF ���� Driver ��飻��������ֻ�� CONTINUATION ������Ӧ�е� Result��

��ǰ��ֻʣ�̶� native ʵ�飬��������ɵ���ѧ������µ������о���Ҳ��Ϊ����ÿСʱ������������չ����û����ʵ native ���оͲ������Ѿ�������ͨ����֤��

## 4. Ѳ����޸����������

�����޸���֤ʵ�Ŀͻ��˴��󣺴�����ڡ���ʱ��ʾ��request/receipt ���á�����Ԥ����©�ʹ���״̬������������ǰԴ��ȷ��ȱ��ʱ���ύ���ع���֤����С�����޸ģ�������Ȩ�޻򽵵���ѧ�Ž����޸���ֱ𱨸棺������ʾ�ѷ������淶��ִ��ʵ�ʷ��ء�ִ�У�����Ƿ���ɡ�

2026-09-22 �����֤�ݣ�`EMREQ-CTRL-20260921T224737Z-DIAG-ANY-6C91B2`��generated_at `2026-09-21T22:49:12Z`��source `86d11cbe9631dac8b5d4b65f5cbc8cefa3c6a086`��940 �����ۣ���� `5768510032`��ʵ�ʷ��� `CLAIM_NEW_OWNER`��Ŀ��Ϊ P0 `RS-GOV-FOUNDATION-BACKFLOW / TP2-2C438651496A928ADCB7`�����ǵ��������������֤�ݣ�����������������������ִ�����ɡ�

��Ŀ�굱��ʣ������������ current-main �����е�����ԭ����֤����С������������������� R004��Ҳ������������ PR #444���˻���������δ�����οͻ����޸�������

2026-09-22 00:28Z ����Ѳ���ִ `EMREQ-CTRL-20260922T0026Z-RESEARCH-PATROL-1A6C3E` �ٴη��� `CLAIM_NEW_OWNER`��Ŀ�� `RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`���������� 5769197761 ���ѽ��� `CONTINUATION` ���Ѿ����᣺20-row ʵ�����Ϊ `VERIFIED_COMPLETE`��Ψһδ�굥Ԫ����Ҫ full-current-source host �� `GEN2_CURRENT_PUBLICATION_EXECUTION_AND_RESULT_FREEZE`������ǰͬ�� ChatGPT ������ȷû�иû�����������Ǳ��� `CAPABILITY_MISMATCH_HEAD_OF_LINE` ���׸���¼ʵ������Ӧ������ͬ��������ѭ�� CLAIM��CONTINUATION��Ҳ��Ӧ���о�Ա�������������ͨ����

���� PCF ����ȱ���� 00:28Z ����ʷ�������˺�ԭ��ͨ�о��Ի�ͨ���·���������� [Issue 35 �� typed continuation_prepare](https://github.com/awdawmip/kimi-query-bridge/issues/35#issuecomment-5770029180) �� [Issue 37 �Ļ�ʤ CLAIM](https://github.com/awdawmip/kimi-query-bridge/issues/37#issuecomment-5770049300)���ѿ���ô�ԭ��׼��/��ȡ���ƽ׶Ρ������ٰѾɡ�ȱ���� checkout���հ�Ϊ��ǰ������������������ݻ�ִ��֤����ʽ Result �Ѷ��ᡢ���� review ����ɻ��κο�ѧʵ��/ȫ�� gate ��ͨ����

ͬһ�� `GOVERNANCE` ��ִ `EMREQ-CTRL-20260922T0029Z-GOV-PATROL-4D7B2C` ���� `RS-GOV-FOUNDATION-BACKFLOW`���䵱ǰΨһ�ƽ������������� latest-main checkout ������ԭ��ȫ�� gate ����С Foundation/Common-Surface ����������ʵȷ�� Driver ��ǰ������Ե��� `LOCAL_VALIDATION_PENDING` ��������ȱ�ڣ������� MCP-only review authority��Ҳ���ǡ��� Driver ��������

��֤��Χ���Թ̶�Դ���� `require_review_authority` ��ԭ������ժ¼������ʽ������������ Driver authority��ִ�� 11 �������ԣ������� MCP ��ʽƥ�� session ����ͨ����ȱ��Ȩ���գ��� session��ȱ���������������ص������ܾ���������֤�ú�����Լ������ȫ����ԡ���ʵ��Ȩ���ա���ʽ review �� native ʵ��ͨ����

## 5. ������ǰ��ֻ�� pre_final

��ͨ GitHub �Ի�����ǰ��ָ�ϵ��� `pre_final`��������ʵ parent_liveness����ʽ�Ѷ���/��������󶨳ɹ� open/resume �� run_request_id ���Ӧ completion_request_id������ʽ run �� Driver ���Լ��� session_request_id����δ�����о� session ��ά���Ự�ſ���ά��ģʽ�������ȡ `receipt.result.final_allowed` �� `required_action`��false ʱ����ָ��������ע�ᡢfreeze��review��close �� pre_final ���� SUCCEEDED ���������������ջظ�������α���û�ֹͣ��Ӳ���ƻ�Ľ�ɫ���ƹ�ԭ��Ŀ�ꡣ��ѧ��֤����ѧ׼��߽粻�䡣
