"""Bounded Driver checks of the pinned adapter, reducer and numerical runtime."""
from pathlib import Path
import copy,hashlib,json,sys,zipfile
T=Path(r"D:/em/TEMP/r005-q78553-review-81273a-20260910")
A=T/"frozen_science/research_artifacts/R005_Q78553_CATALOGUE_050E43_20260910"
sys.path.insert(0,str(A))
import numpy as np,primesieve
from sieve_block import scan_block
from construct_catalogue import reduce_blocks,accepted_scanner
def sha(b):return hashlib.sha256(b).hexdigest()
manifest=json.loads((A/"isolated-primesieve-environment-manifest.json").read_text())
module_root=Path(primesieve.__file__).parent.parent
runtime_files=[]
for item in manifest:
 package=Path(item["path"]);data=package.read_bytes();assert sha(data)==item["sha256"]
 if package.name.endswith(".whl"):
  with zipfile.ZipFile(package) as z:
   tested=0
   for member in z.infolist():
    if member.is_dir() or not member.filename.endswith((".py",".pyd",".dll")):continue
    installed=module_root/member.filename
    assert installed.is_file() and installed.read_bytes()==z.read(member.filename),member.filename
    tested+=1
   runtime_files.append({"distribution":package.name,"sha256":sha(data),"installed_files_exactly_matching":tested})
 else:
  with zipfile.ZipFile(package) as z:
   installed=Path(sys.executable)
   assert installed.read_bytes()==z.read("python.exe")
   runtime_files.append({"distribution":package.name,"sha256":sha(data),"python_executable_matches":True})
assert primesieve.primesieve_version()==b"7.5" and np.__version__=="1.26.4"
cases=[(2,3,[2]),(3,4,[3]),(4,5,[]),(4,6,[5]),(2,4,[2,3]),(97,98,[97]),(98,101,[])]
for lo,hi,expected in cases:
 r=scan_block(lo,hi,916)
 assert r["prime_count"]==len(expected)
 assert r["first_prime"]==(expected[0] if expected else None)
 assert r["last_prime"]==(expected[-1] if expected else None)
 assert r["max_internal_gap"]==max([b-a for a,b in zip(expected,expected[1:])] or [0])
scanner=accepted_scanner();gap_start=1189459969825483
lo=gap_start-2;cut=gap_start+400;hi=gap_start+918
left=scan_block(lo,cut,916);right=scan_block(cut,hi,916)
bridge=(left["last_prime"],right["first_prime"]-left["last_prime"],right["first_prime"])
assert bridge==(gap_start,916,gap_start+916)
scanner.verify_consecutive_gap(scanner.GapRow(gap_start,916))
windows=[(1291005053866735-1000,1291005053866735+1000),(1294364244470160-1000,1294364244470160+1000)]
for lo,hi in windows:
 expected=[n for n in range(lo,hi) if scanner.is_prime_u64(n)]
 r=scan_block(lo,hi,916)
 assert r["prime_count"]==len(expected) and r["first_prime"]==expected[0] and r["last_prime"]==expected[-1]
 actual_digest=hashlib.sha256(np.asarray(expected,dtype="<u8").tobytes()).hexdigest()
 assert actual_digest==r["prime_sequence_sha256"]
blocks=[json.loads(p.read_text()) for p in sorted((T/"restored_blocks/construction_full/blocks").glob("*.json"))]
reduced=reduce_blocks(blocks,1291000000000000,1295000000000000,10**9)
stored=json.loads((A/"construction_full/construction_reduction.json").read_text())
for k,v in reduced.items():assert stored[k]==v,k
rejections=[]
for name,mutate in [
 ("missing_final_block",lambda rows:rows.pop()),
 ("duplicate_block_identity",lambda rows:rows.__setitem__(100,copy.deepcopy(rows[99]))),
 ("threshold_drift",lambda rows:rows[100].__setitem__("threshold",917)),
 ("overlapping_block_boundary",lambda rows:rows[100].__setitem__("lower_inclusive",rows[100]["lower_inclusive"]-1)),
]:
 bad=copy.deepcopy(blocks);mutate(bad)
 try:reduce_blocks(bad,1291000000000000,1295000000000000,10**9)
 except ValueError as exc:rejections.append({"case":name,"rejected":True,"reason":str(exc)})
 else:raise AssertionError(name)
out={"schema":"R005_DRIVER_BOUNDED_ADAPTER_AND_REDUCER_REVIEW_V1","status":"PASS","driver_id":"EM-DVR-81273A","runtime_files":runtime_files,"small_half_open_cases":len(cases),"known_real_916_bridge":bridge,"high_range_windows":windows,"unmodified_reducer_matches_all_frozen_fields":True,"rejected_corrupt_partition_cases":rejections,"full_production_sieve_replayed":False}
target=T/"checks/bounded-adapter-review.json";assert not target.exists()
target.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out))

