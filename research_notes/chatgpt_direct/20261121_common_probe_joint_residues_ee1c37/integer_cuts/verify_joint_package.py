"""Portable replay of the two FINAL joint fractional certificates.

Supply the immutable predecessor proof package with --previous. The bundled
integer XOR verifier is an unchanged copy of the root verifier already used in
this research. This entry point writes fresh receipts only under --work.
"""
from pathlib import Path
from hashlib import sha256
import argparse,json,subprocess,sys

HERE=Path(__file__).resolve().parent
FINAL_HASHES={
    1:'8989c9ab239b1a8d3c6d37c371fb0de856975cf21fc16722b1bcd72bcff6c323',
    2:'f411ba7d7d45af6f4ca8531d36563bb712a9aca7e9561651e741a7b816396969',
}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--previous',type=Path,required=True,help='complete predecessor proof package containing fractional/proof/verify.py and fractional/next_cuts/discovery_common.py')
    p.add_argument('--work',type=Path,required=True,help='separate directory for replay receipts and the compiled XOR checker')
    p.add_argument('--witness-dir',type=Path,default=HERE/'all_joint_exact')
    a=p.parse_args();a.work.mkdir(parents=True,exist_ok=True)
    for f,digest in FINAL_HASHES.items():
        assert sha256((a.witness_dir/f'cover_{f}.json').read_bytes()).hexdigest()==digest
    for name in ['fractional/proof/verify.py','fractional/next_cuts/discovery_common.py']:
        assert (a.previous/name).is_file(),name
    # All arithmetic checks below are exact. No LP solver is used in replay.
    modular=a.work/'modular_and_stars.json';xor=a.work/'xor.json'
    subprocess.run([sys.executable,str(HERE/'verify_recovered.py'),
                    '--delivery-root',str(a.previous.resolve()),'--directory',str(a.witness_dir.resolve()),
                    '--frames','1','2','--require-stars','--output',str(modular.resolve())],check=True)
    subprocess.run([sys.executable,str(HERE/'portable/verify_integer_xor.py'),
                    '--witness-dir',str(a.witness_dir.resolve()),'--parallel-module',str(HERE/'parallel_family.py'),
                    '--frames','1','2','--work',str((a.work/'xor_binary').resolve()),
                    '--output',str(xor.resolve())],check=True)
    mr=json.loads(modular.read_text());xr=json.loads(xor.read_text());frames=[];native=set()
    for f in [1,2]:
        m=next(r for r in mr['frames'] if r['frame']==f);x=next(r for r in xr['frames'] if r['frame']==f)
        assert m['all_stars_satisfied'] and x['verified']
        assert m['witness_sha256']==x['witness_sha256']==FINAL_HASHES[f]
        doc=json.loads((a.witness_dir/f'cover_{f}.json').read_text())
        native.update(map(int,doc['core_masks']));native.update(int(r['mask']) for r in doc['weights'])
        frames.append({'frame':f,'sha256':FINAL_HASHES[f],'positive_noncore_classes':len(doc['weights']),
                       'star_checks':sum(101-int(r['mask']).bit_count() for r in doc['weights']),
                       'modular_indexed_cuts_covered':m['represented_index_checks'],
                       'xor_indexed_cuts_checked':x['indexed_cuts']})
    result={'all_verified':True,'frames':frames,'distinct_positive_native_classes':len(native),
            'scope':'The same two exact fractional points pass every declared family; indexed counts include duplicates.'}
    (a.work/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
