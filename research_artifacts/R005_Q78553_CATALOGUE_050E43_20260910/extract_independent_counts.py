"""Extract only the independently published pi values used by this exact run."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
source=HERE/"tos-primecount-1d12.txt"
raw=source.read_bytes()
expected_sha="7b45f7135e4faffaca258b274f23b4d5e015da25c0907c24d117de68bc461257"
assert hashlib.sha256(raw).hexdigest()==expected_sha
wanted={k*10**12 for k in range(1291,1296)}
values={}
lines=[]
for line_number,line in enumerate(raw.decode("utf-8").splitlines(),1):
    parts=line.split()
    if len(parts)>=2 and parts[0].endswith("d12") and parts[0][:-3].isdigit():
        x=int(parts[0][:-3])*10**12
        if x in wanted:
            if x in values: raise ValueError("Duplicate count boundary")
            values[x]=int(parts[1])
            lines.append({"line":line_number,"x":x,"pi_x":values[x],"original_line":line})
assert set(values)==wanted
cells=[]
for x in sorted(values)[:-1]:
    upper=x+10**12
    assert x>2 and upper>2 and x%2==0 and upper%2==0
    cells.append({"lower_inclusive":x,"upper_exclusive":upper,"pi_lower":values[x],"pi_upper":values[upper],
                  "expected_prime_count":values[upper]-values[x],
                  "boundary_conversion":"Both integer endpoints are even and >2; pi(U)-pi(L) equals the prime count in [L,U)."})
output={"schema":"R005_INDEPENDENT_PRIME_COUNT_TARGETS_V1",
        "source_url":"https://sweet.ua.pt/tos/primes/1d12.txt.gz",
        "source_page":"https://sweet.ua.pt/tos/primes.html",
        "source_decoded_sha256":expected_sha,
        "source_compressed_sha256":"4b98cbfffa074b533ecbb4b793ddb3a315cfa567626169611f5c432384950042",
        "source_relevant_original_rows":lines,"cells":cells,"expected_total_count":sum(x["expected_prime_count"] for x in cells)}
path=HERE/"independent-prime-count-targets.json"
if path.exists(): raise FileExistsError(str(path))
path.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")
print(json.dumps(output),flush=True)

