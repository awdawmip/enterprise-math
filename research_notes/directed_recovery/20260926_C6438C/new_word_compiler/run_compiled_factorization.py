"""CLI for the complete/partial variable-native-word factorization algorithm."""
from pathlib import Path
import argparse,gzip,hashlib,json,random
from compiled_factorization import factor_integer_compiled,verify_factorization
from stage79.phase_compiler import encode

def read_result(path):
    raw=Path(path).read_bytes()
    if str(path).endswith('.gz'):
        raw=gzip.decompress(raw)
    return json.loads(raw)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--N',type=int,required=True)
    ap.add_argument('--failure-bits',type=int,default=16)
    ap.add_argument('--attempts',type=int)
    ap.add_argument('--compiler-pairs',type=int,default=256)
    ap.add_argument('--unbounded-compiler',action='store_true')
    ap.add_argument('--observer-bits',type=int,default=48)
    ap.add_argument('--seed',type=int)
    ap.add_argument('--resume-cursors-from',type=Path)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    cursors=None
    if args.resume_cursors_from:
        saved=read_result(args.resume_cursors_from)
        source=saved.get('result',saved)
        cursors=source['native_word_compiler']['phase_cursors']
    rng=random.SystemRandom() if args.seed is None else random.Random(args.seed)
    result=factor_integer_compiled(args.N,rng,failure_bits=args.failure_bits,
        max_attempts=args.attempts,
        compiler_pair_budget=None if args.unbounded_compiler else args.compiler_pairs,
        observer_start_bits=args.observer_bits,phase_cursors=cursors)
    verified=verify_factorization(result)
    output={'result':result,'deterministic_verification':verified,
        'random_interface':'system randomness' if args.seed is None else 'seeded software demonstration',
        'random_source_physically_certified':False,
        'seed':args.seed,'source_entrypoint':str(Path(__file__).resolve())}
    raw=json.dumps(encode(output),sort_keys=True,separators=(',',':')).encode()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_bytes(gzip.compress(raw,mtime=0) if args.out.suffix=='.gz' else raw)
    print(json.dumps({'N':args.N,'status':result['status'],
        'prime_factors':result['prime_factors'],
        'unresolved':result['unresolved'],'deterministically_verified':verified['verified'],
        'stochastic_budget_verified':verified['stochastic_budget_verified'],
        'payload_sha256':hashlib.sha256(raw).hexdigest(),'output':str(args.out.resolve())}))

if __name__=='__main__':main()
