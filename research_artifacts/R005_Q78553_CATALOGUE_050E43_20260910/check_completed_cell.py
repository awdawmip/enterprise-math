import hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
a=Path(__file__).resolve().parent
cell_index=int(sys.argv[1])
target=json.loads((a/"independent-prime-count-targets.json").read_text(encoding="utf-8"))["cells"][cell_index]
root=a/"construction_full"
rows=[]
for index in range(cell_index*1000,(cell_index+1)*1000):
    path=root/"blocks"/f"{index:05d}.json"
    raw=path.read_bytes()
    b=json.loads(raw)
    assert b["block_index"]==index
    assert b["lower_inclusive"]==1291000000000000+index*1000000000
    assert b["upper_exclusive"]==b["lower_inclusive"]+1000000000
    rows.append(b)
count=sum(b["prime_count"] for b in rows)
assert count==target["expected_prime_count"],(cell_index,count,target)
pairs=[{**b["max_internal_gap_witness"],"origin":"internal_maximum","block_index":b["block_index"]} for b in rows]
pairs += [{"start":x["last_prime"],"end":y["first_prime"],"gap":y["first_prime"]-x["last_prime"],
          "origin":"cross_block","left_block":x["block_index"],"right_block":y["block_index"]} for x,y in zip(rows,rows[1:])]
maximum=max(pairs,key=lambda r:r["gap"])
result={"schema":"R005_INDEPENDENT_TRILLION_CELL_COUNT_CHECK_V1","cell_index":cell_index,"lower_inclusive":target["lower_inclusive"],
        "upper_exclusive":target["upper_exclusive"],"block_count":len(rows),"observed_prime_count":count,
        "expected_prime_count":target["expected_prime_count"],"count_match":True,
        "first_prime":rows[0]["first_prime"],"last_prime":rows[-1]["last_prime"],
        "max_observed_gap":maximum,"large_internal_gap_count":sum(len(b["large_internal_gaps"]) for b in rows),
        "max_scope":"All consecutive pairs within this cell's complete observed prime sequence; cross-cell bridges are audited separately.",
        "checked_at":datetime.now(timezone.utc).isoformat()}
path=root/f"cell_{cell_index+1:02d}_count_check.json"
if path.exists(): raise FileExistsError(str(path))
path.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result),flush=True)

