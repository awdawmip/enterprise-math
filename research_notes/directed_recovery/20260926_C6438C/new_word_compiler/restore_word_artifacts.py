"""Restore and verify complete byte-split evidence; no scientific propagation."""
from pathlib import Path
import argparse,gzip,hashlib,json

ROOT=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,default=ROOT/'restored_artifacts')
    args=parser.parse_args()
    manifest=json.loads((ROOT/'WORD_MANIFEST.json').read_text(encoding='utf-8'))
    args.output_dir.mkdir(parents=True,exist_ok=True)
    for artifact in manifest['complete_split_artifacts']:
        data=[]
        for part in artifact['parts']:
            path=(ROOT/part['path']).resolve()
            if not path.is_relative_to(ROOT.resolve()):
                raise ValueError('Part is outside this package')
            raw=path.read_bytes()
            assert len(raw)==part['bytes'] and hashlib.sha256(raw).hexdigest()==part['sha256']
            data.append(raw)
        raw=b''.join(data)
        assert len(raw)==artifact['bytes'] and hashlib.sha256(raw).hexdigest()==artifact['sha256']
        expanded=gzip.decompress(raw)
        assert len(expanded)==artifact['uncompressed_bytes']
        assert hashlib.sha256(expanded).hexdigest()==artifact['uncompressed_sha256']
        if Path(artifact['path']).name!=artifact['path']:
            raise ValueError('Invalid restored artifact name')
        target=args.output_dir/artifact['path']
        if target.exists() and target.read_bytes()!=raw:
            raise ValueError('Refusing to replace a different existing artifact')
        target.write_bytes(raw)
        print(json.dumps({'artifact':artifact['path'],'verified':True,'bytes':len(raw),'parts':len(data)}))

if __name__=='__main__':main()
