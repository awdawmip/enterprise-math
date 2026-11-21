"""Regenerate the complete typed (size, embedding, cost, max absolute difference) catalogue."""
from pathlib import Path
import argparse, hashlib, json, sys
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--baseline', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
a = p.parse_args()
sys.path.insert(0, str(a.baseline.resolve() / 'bias'))
from plan_extended import catalog, checksum
assert checksum == '7a1ba8be4d450fc24c886aae475c9d29b53688c0ce06578a69ed140ff8b151e4'
rows = [(s, e, c, d) for (s, e), values in sorted(catalog.items())
        for c, d in sorted(values.items())]
text = str(len(rows)) + '\n' + ''.join(' '.join(map(str, row)) + '\n' for row in rows)
digest = hashlib.sha256(text.encode()).hexdigest()
assert len(rows) == 2339 and digest == '7cc8a7c76a5001da6886fa28507bb19856defe4f1de90eb045f3aca644388095'
a.output.write_text(text)
print(json.dumps({'typed_rows': len(rows), 'typed_catalog_sha256': digest,
                  'native_catalog_sha256': checksum}), flush=True)
