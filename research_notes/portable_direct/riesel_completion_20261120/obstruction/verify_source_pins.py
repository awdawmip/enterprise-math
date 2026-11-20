#!/usr/bin/env python3
"""Verify the native BRC source files against the inherited Git blob IDs."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PROJECT_SOURCE_COMMIT = 'b1efc6c805661ed7b476e6e730107da6043176ee'
PROJECT_SOURCE_BLOBS = {
    'brc_transport.py': 'be1debe367263931bd5e93fd750be3ed54624fe1',
    'brc_histogram.py': '9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1',
    'brc_rational_holonomy.py': '2591640fe348da9cd7f293a957bea9ae92c82943',
    'brc_weighted_recurrent.py': '4e6b3132580e3cd70a20a0d8bd4d28792b961afb',
}


def verify_native_source_pins(source_dir):
    actual = {}
    for name, expected in PROJECT_SOURCE_BLOBS.items():
        data = (Path(source_dir)/'enterprise_math'/name).read_bytes()
        actual[name] = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        assert actual[name] == expected, (name, actual[name], expected)
    return {
        'project_source_commit': PROJECT_SOURCE_COMMIT,
        'project_source_blobs': actual,
        'native_source_blob_pins_verified': True,
        'pin_provenance': 'research_notes/portable_direct/riesel_mixed_20261119/results.json',
        'method': 'SHA-1 of Git blob header and exact file bytes',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, default=Path(__file__).resolve().parent.parent/'vendor_src')
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parent/'native_source_verification.json')
    args = parser.parse_args()
    result = verify_native_source_pins(args.source_dir)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))
