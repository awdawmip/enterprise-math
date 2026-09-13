#!/usr/bin/env python3
"""Validate a canonical final Cell address supplied as JSON on stdin."""
from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from enterprise_math.cell_address import FinalCellAddress

def main() -> int:
    try:
        address = FinalCellAddress.from_json(sys.stdin.read())
    except (ValueError,TypeError,OverflowError) as exc:
        print(json.dumps({"valid":False,"error":str(exc)}))
        return 2
    print(json.dumps({"valid":True,"address":address.to_wire()},separators=(",",":")))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
