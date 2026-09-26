"""Run the fixed K33 simulator and unchanged CF-only factorization path."""
import argparse,gzip,hashlib,json,random
from pathlib import Path
from cf_universal_factorization import factor_integer_cf_universal,verify_factorization

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--N',type=int,required=True)
    ap.add_argument('--attempts',type=int,help='explicit per-node cap; may weaken probability guarantee')
    ap.add_argument('--failure-bits',type=int,default=16)
    ap.add_argument('--seed',type=int,help='seeded software replay; otherwise external system randrange')
    ap.add_argument('--out',required=True)
    args=ap.parse_args()
    rng=random.SystemRandom() if args.seed is None else random.Random(args.seed)
    result=factor_integer_cf_universal(args.N,rng,failure_bits=args.failure_bits,max_attempts=args.attempts)
    result['execution_random_source']={'kind':'external_system_randrange' if args.seed is None else 'seeded_software_demonstration',
        'seed':args.seed,'physical_Born_rule_claimed':False}
    verified=verify_factorization(result)
    raw=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    path=Path(args.out);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw)
    print(json.dumps({'N':args.N,'status':result['status'],'prime_factors':[(p['prime'],p['exponent']) for p in result['prime_factors']],
      'unresolved':result['unresolved'],'verification':verified,'full_result_path':str(path.resolve()),
      'payload_sha256':hashlib.sha256(raw).hexdigest()}))

if __name__=='__main__':main()
