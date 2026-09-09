"""Driver recomputation of the frozen finite evidence; no production sieve rerun."""
from pathlib import Path
from datetime import datetime
from math import isqrt
from bisect import bisect_right
import array,gzip,hashlib,json,re,sys
T=Path(r"D:/em/TEMP/r005-q78553-review-81273a-20260910")
A=T/"frozen_science/research_artifacts/R005_Q78553_CATALOGUE_050E43_20260910"
B=T/"restored_blocks/construction_full/blocks"
def load(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(b):return hashlib.sha256(b).hexdigest()
def dt(s):return datetime.fromisoformat(s.replace("Z","+00:00"))
LOW=1291000000000000;HIGH=1295000000000000;WIDTH=10**9
BAND=(1291005053866735,1294364244470160)
paths=sorted(B.glob("*.json"));assert len(paths)==4000
bm=load(A/"construction_input_byte_manifest.json")
expected={Path(x["path"]).name:x for x in bm["files"]}
assert set(expected)=={f"{i:05d}.json" for i in range(4000)}
run=load(A/"construction_full/run.run.json")
assert run["exit_code"]==0 and run["argv"][run["argv"].index("--workers")+1]=="3"
for channel in ["stdout","stderr"]:
 rec=run[channel];raw=(T/"frozen_science"/Path(rec["path"])).read_bytes()
 assert len(raw)==rec["bytes"] and sha(raw)==rec["sha256"]
runmeta=load(A/"construction_full/run_manifest.json")
assert (runmeta["lower_inclusive"],runmeta["upper_exclusive"],runmeta["block_width"],runmeta["threshold"])==(LOW,HIGH,WIDTH,916)
for name,digest in runmeta["source_sha256"].items():assert sha((A/name).read_bytes())==digest
blocks=[];maxima=[];internal=[];zero_large=0
for index,path in enumerate(paths):
 raw=path.read_bytes();row=load(path);f=expected[path.name]
 assert sha(raw)==f["sha256"] and len(raw)==f["bytes"]
 assert row["block_index"]==index and path.name==f"{index:05d}.json"
 assert (row["lower_inclusive"],row["upper_exclusive"])==(LOW+index*WIDTH,LOW+(index+1)*WIDTH)
 assert row["threshold"]==916 and type(row["prime_count"]) is int and row["prime_count"]>=2
 assert row["lower_inclusive"]<=row["first_prime"]<row["last_prime"]<row["upper_exclusive"]
 assert row["first_prime"]%2==row["last_prime"]%2==1
 assert re.fullmatch("[0-9a-f]{64}",row["prime_sequence_sha256"])
 assert (row["library_primesieve"],row["python_binding_primesieve"],row["numpy_version"],row["python_version"])==("7.5","2.3.0","1.26.4","3.9.13")
 assert dt(row["started_at"])<=dt(row["completed_at"])<=dt(run["completed_at"])
 if index:assert dt(row["started_at"])>=dt(run["started_at"])
 assert row["elapsed_seconds"]>0
 w=row["max_internal_gap_witness"]
 assert row["first_prime"]<=w["start"]<w["end"]<=row["last_prime"]
 assert w["end"]-w["start"]==w["gap"]==row["max_internal_gap"]
 maxima.append(dict(w,block=index))
 for g in row["large_internal_gaps"]:
  assert g["end"]-g["start"]==g["gap"]>=916 and g["gap"]<=w["gap"]
  assert row["first_prime"]<=g["start"]<g["end"]<=row["last_prime"]
  internal.append(g)
 if w["gap"]<916:assert row["large_internal_gaps"]==[];zero_large+=1
 else:assert w in row["large_internal_gaps"]
 blocks.append(row)
pilot=load(A/"pilot/1e9.json");actual0=dict(blocks[0]);actual0.pop("block_index")
assert actual0==pilot
bridges=[{"start":l["last_prime"],"end":r["first_prime"],"gap":r["first_prime"]-l["last_prime"],"left":i,"right":i+1} for i,(l,r) in enumerate(zip(blocks,blocks[1:]))]
assert len(bridges)==3999 and all(x["gap"]>0 and x["gap"]%2==0 for x in bridges)
count=sum(b["prime_count"] for b in blocks)
pairs=sum(b["prime_count"]-1 for b in blocks)+len(bridges)
assert count==114956492689 and pairs==count-1
all_large=sorted(internal+[x for x in bridges if x["gap"]>=916],key=lambda x:x["start"])
task_large=[x for x in all_large if BAND[0]<=x["start"]<=BAND[1]]
maximum=max(maxima+bridges,key=lambda x:(x["gap"],-x["start"]))
assert all_large==[] and task_large==[]
assert (maximum["start"],maximum["end"],maximum["gap"])==(1292271366466303,1292271366467033,730)
assert BAND[0]<=maximum["start"]<=BAND[1]
assert blocks[0]["first_prime"]<=BAND[0]<BAND[1]<blocks[-1]["last_prime"]
download=(T/"independent_tos_prime_counts.txt.gz").read_bytes()
assert sha(download)=="4b98cbfffa074b533ecbb4b793ddb3a315cfa567626169611f5c432384950042"
raw=gzip.decompress(download)
assert raw==(A/"tos-primecount-1d12.txt").read_bytes()
assert sha(raw)=="7b45f7135e4faffaca258b274f23b4d5e015da25c0907c24d117de68bc461257"
pi={};original_lines=[]
for line in raw.decode("utf-8").splitlines():
 # The published three columns are x, exact pi(x), and approximate li(x).
 # Parse the third column explicitly but use only the integer second column.
 m=re.fullmatch(r"\s*(129[1-5])d12\s+(\d+)\s+(\d+\.\d+\.{3})\s*",line)
 if m:
  x=int(m.group(1))*10**12;assert x not in pi;pi[x]=int(m.group(2));original_lines.append(line)
assert len(pi)==5
cells=[]
for i in range(4):
 lo=LOW+i*10**12;hi=lo+10**12
 observed=sum(b["prime_count"] for b in blocks[i*1000:(i+1)*1000])
 assert observed==pi[hi]-pi[lo]
 cell_max=max(maxima[i*1000:(i+1)*1000]+bridges[i*1000:(i+1)*1000-1],key=lambda x:x["gap"])["gap"]
 cells.append({"lower":lo,"upper":hi,"observed":observed,"pi_difference":pi[hi]-pi[lo],"max_gap":cell_max})
assert [c["max_gap"] for c in cells]==[720,730,720,726]
reported=load(A/"construction_audit.json")
reduction=load(A/"construction_full/construction_reduction.json")
assert reported["prime_count"]==reduction["prime_count"]==count
assert reported["all_pair_count"]==reduction["all_pair_count"]==pairs
assert reported["cross_block_pair_count"]==reduction["cross_block_pair_count"]==3999
assert reported["all_gaps_at_least_916"]==reduction["all_gaps_at_least_threshold"]==[]
assert reported["global_max_observed_gap"]["gap"]==reduction["max_gap"]==730
cat=load(A/"catalogue.json");unattested=load(A/"catalogue.unattested.json")
assert cat["coverage_start"]==BAND[0] and cat["coverage_end"]==BAND[1]
assert cat["rows"]==[] and cat["rows_sha256"]==sha(b"")
assert cat["complete_for_gap_ge"]==916 and cat["max_gap_bound"]==730 and cat["completeness_attestation"] is True
assert (cat["max_gap_bound_start"],cat["max_gap_bound_end"])==(blocks[0]["first_prime"],blocks[-1]["last_prime"]-1)
old=dict(cat);old.pop("attestation_basis");old["completeness_attestation"]=False;assert old==unattested
basis=cat["attestation_basis"]
for key,name in [("construction_audit_sha256","construction_audit.json"),("independent_witness_verification_sha256","independent_witness_verification.json"),("run_manifest_sha256","construction_full/run_manifest.json")]:
 assert basis[key]==sha((A/name).read_bytes())
report=load(A/"independent_witness_verification.json")
certs=[load(A/rec["path"]) for rec in report["certificates"]]
assert len(certs)==7
for rec,cert in zip(report["certificates"],certs):assert sha((A/rec["path"]).read_bytes())==rec["sha256"]
limit=isqrt(max(c["end"] for c in certs));assert limit==35981714
flags=bytearray(b"\x01")*(limit+1);flags[0:2]=b"\x00\x00"
for prime in range(2,isqrt(limit)+1):
 if flags[prime]:
  start=prime*prime;flags[start:limit+1:prime]=b"\x00"*(((limit-start)//prime)+1)
primes=array.array("Q",(n for n in range(2,limit+1) if flags[n]));del flags
assert sys.byteorder=="little" and len(primes)==2203176
basis_sha=sha(primes.tobytes())
assert basis_sha==report["reference_basis_sha256"]=="57adea8a8361a8aa0c62803f4b3e25efc6df7c3bbf040beae76a352f4f19a3c6"
endpoint_checks=[];odd_count=0
for cert in certs:
 lo,hi,gap=cert["start"],cert["end"],cert["gap"]
 assert hi-lo==gap and lo%2==hi%2==1
 endpoints=cert["endpoint_primality_certificates"];assert [p["n"] for p in endpoints]==[lo,hi]
 for ep in endpoints:
  n=ep["n"];cut=bisect_right(primes,isqrt(n));assert ep["trial_limit"]==isqrt(n) and ep["tested_prime_count"]==cut
  assert ep["last_tested_prime"]==primes[cut-1] and ep["basis_sha256"]==basis_sha
  tested=0
  for prime in primes:
   if prime*prime>n:break
   assert n%prime!=0,(n,prime)
   tested+=1
  assert tested==cut
  endpoint_checks.append({"n":n,"trial_limit":isqrt(n),"tested_primes":tested,"prime":True})
 witnesses=cert["odd_interior_factor_witnesses"]
 assert [w["n"] for w in witnesses]==list(range(lo+2,hi,2))
 for w in witnesses:assert 1<w["factor"]<w["n"] and w["factor"]*w["cofactor"]==w["n"] and w["cofactor"]>1
 odd_count+=len(witnesses)
 even=cert["even_interior"]
 assert even=={"first":lo+1,"last":hi-1,"step":2,"count":gap//2,"factor":2}
 assert len(witnesses)+even["count"]==gap-1==cert["all_interior_count"]
out={"schema":"R005_DRIVER_INDEPENDENT_FROZEN_EVIDENCE_AUDIT_V1","driver_id":"EM-DVR-81273A","status":"PASS","block_count":4000,"source_bytes_reconstructed":3513720,"all_block_byte_digests_match":True,"all_4000_internal_maxima_below_916":zero_large==4000,"reused_billion_block_exactly_once":True,"count":count,"pairs":pairs,"cross_block_pairs":3999,"cross_cell_gaps":[bridges[i]["gap"] for i in [999,1999,2999]],"maximum":maximum,"all_threshold_rows":all_large,"task_threshold_rows":task_large,"task_band":list(BAND),"covered_start_interval":[blocks[0]["first_prime"],blocks[-1]["last_prime"]-1],"independently_redownloaded_count_table_sha256":sha(download),"pi_original_rows":original_lines,"cells":cells,"witness_count":7,"reference_basis_count":len(primes),"reference_basis_sha256":basis_sha,"endpoint_checks":endpoint_checks,"odd_factor_witnesses_verified":odd_count,"production_sieve_rerun":False,"numpy_or_libprimesieve_used_by_this_audit":False,"scope":"Recompute frozen record observer and exact prime/factor witnesses; finite recorded enumeration with the pinned production implementation remains the coverage premise."}
target=T/"checks/independent-frozen-evidence.json";assert not target.exists()
target.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,ensure_ascii=True))
