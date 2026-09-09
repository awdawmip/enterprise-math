"""Independent reference checks for the task-specific primesieve adapter."""
import array, hashlib, importlib.util, json, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from sieve_block import scan_block
from construct_catalogue import accepted_scanner
from primesieve.numpy import primes

def plain_sieve(n):
    a=bytearray(b"\x01")*(n+1)
    a[0:2]=b"\x00\x00"
    for p in range(2,int(n**0.5)+1):
        if a[p]:
            a[p*p:n+1:p]=b"\x00"*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if a[i]]

def reference_block(values,threshold):
    gaps=[(x,y-x,y) for x,y in zip(values,values[1:])]
    large=[{"start":x,"gap":g,"end":y} for x,g,y in gaps if g>=threshold]
    return large,max((g for _,g,_ in gaps),default=0),hashlib.sha256(array.array("Q",values).tobytes()).hexdigest()

def main():
    scanner=accepted_scanner()
    results=[]
    small=plain_sieve(100000)
    actual=[int(x) for x in primes(2,100000)]
    assert actual==small
    results.append({"check":"plain_independent_Eratosthenes_all_primes_through_100000","prime_count":len(small),"passed":True})
    a=1189459969825483
    windows=[(a-2000,a+916+2000),(1291005053866735-2000,1291005053866735+2000)]
    for lo,hi in windows:
        expected=[n for n in range(lo,hi) if scanner.is_prime_u64(n)]
        observed=scan_block(lo,hi,916)
        rows,max_gap,digest=reference_block(expected,916)
        assert observed["prime_count"]==len(expected)
        assert observed["first_prime"]==expected[0] and observed["last_prime"]==expected[-1]
        assert observed["large_internal_gaps"]==rows
        assert observed["max_internal_gap"]==max_gap
        assert observed["prime_sequence_sha256"]==digest
        results.append({"check":"independent_deterministic_u64_Miller_Rabin_every_integer","lower":lo,"upper_exclusive":hi,
                        "prime_count":len(expected),"large_gaps":rows,"matched_complete_sequence_sha256":digest,"passed":True})
    lo=a-2000;cut=a+400;hi=a+916+2000
    left=scan_block(lo,cut,916);right=scan_block(cut,hi,916)
    bridge={"start":left["last_prime"],"gap":right["first_prime"]-left["last_prime"],"end":right["first_prime"]}
    union=left["large_internal_gaps"]+right["large_internal_gaps"]+[bridge]
    union.sort(key=lambda r:r["start"])
    expected=[n for n in range(lo,hi) if scanner.is_prime_u64(n)]
    rows,_,_=reference_block(expected,916)
    assert bridge=={"start":a,"gap":916,"end":a+916}
    assert union==rows
    assert len(expected)==left["prime_count"]+right["prime_count"]
    results.append({"check":"known_real_916_gap_split_inside_composite_interior","cut":cut,"boundary_pair":bridge,"passed":True})
    value={"schema":"R005_PRIMESIEVE_ADAPTER_INDEPENDENT_VALIDATION_V1","all_passed":True,"checks":results,
           "scope":"Validates adapter semantics and representative high-range outputs; this is not full task-band coverage."}
    p=HERE/"pilot/independent-validation.json"
    if p.exists(): raise FileExistsError(str(p))
    p.write_text(json.dumps(value,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(value),flush=True)
if __name__=="__main__":
    main()

