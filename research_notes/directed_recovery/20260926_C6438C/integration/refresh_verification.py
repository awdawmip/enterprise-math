"""Re-run only deterministic persisted-result verification after scope labels changed."""
import gzip, hashlib, json
from pathlib import Path
from complete_factorization import verify_factorization
from stage45.brc_loop_recheck import CALLS
ROOT=Path(__file__).resolve().parent
full=ROOT/'COMPLETE_RESULTS.json.gz'; summary=ROOT/'COMPLETE_SUMMARY.json'
data=json.loads(gzip.decompress(full.read_bytes()))
data['verified']=[verify_factorization(row) for row in data['examples']]
data['verification_replay_core_calls']=len(CALLS)
data['verification_replay_core_receipts']=CALLS
raw=json.dumps(data,sort_keys=True,separators=(',',':')).encode()
full.write_bytes(gzip.compress(raw,mtime=0))
brief=json.loads(summary.read_text(encoding='utf-8'))
brief['verified']=data['verified'];brief['verification_replay_core_calls']=len(CALLS)
brief['full_payload_sha256']=hashlib.sha256(raw).hexdigest()
summary.write_text(json.dumps(brief,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verified_results':len(data['verified']),'actual_replay_core_calls':len(CALLS)}))
