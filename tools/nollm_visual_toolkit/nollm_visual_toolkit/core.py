"""Exact research data and explicitly typed observers (standard library only)."""
from __future__ import annotations
import csv
import hashlib
import io
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

SCHEMA = "NOLLM_VISUAL_DATA_V2"
VERSION = "0.3.0"
MAX_POINTS = 200_000
MAX_COORD = 1_000_000  # Ensures browser integer geometry remains exact.
MAX_SAFE = 2**53 - 1
HEX_DIRECTIONS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
FCC_AXES = ((1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1))


def integer(value: Any, name: str, limit: int = MAX_SAFE) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer, not {type(value).__name__}")
    if abs(value) > limit:
        raise ValueError(f"{name} exceeds the exact browser range ±{limit}")
    return value


def _json_safe(value: Any) -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("NaN and infinity are not valid data")
    if isinstance(value, int) and not isinstance(value, bool) and abs(value) > MAX_SAFE:
        raise ValueError("JSON integer exceeds the exact browser range")
    if isinstance(value, dict):
        if any(not isinstance(k, str) for k in value):
            raise ValueError("JSON object keys must be strings")
        for v in value.values():
            _json_safe(v)
    elif isinstance(value, (list, tuple)):
        for v in value:
            _json_safe(v)
    elif value is not None and not isinstance(value, (str, int, float, bool)):
        raise ValueError(f"Non-JSON value: {type(value).__name__}")


def validate(data: dict[str, Any]) -> dict[str, Any]:
    """Validate without coercion or dropping fields. IDs need not equal row numbers."""
    if not isinstance(data, dict) or data.get("schema") != SCHEMA:
        raise ValueError(f"Expected schema {SCHEMA}")
    kind = data.get("kind")
    if kind not in ("hex", "x6"):
        raise ValueError("kind must be 'hex' or 'x6'")
    rows = data.get("records")
    if not isinstance(rows, list) or not 1 <= len(rows) <= MAX_POINTS:
        raise ValueError(f"records must contain 1..{MAX_POINTS} objects")
    width = 2 if kind == "hex" else 6
    seen: set[str] = set()
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Each record must be an object")
        key = row.get("id")
        if not isinstance(key, str) or not key or len(key) > 256 or key in seen:
            raise ValueError("Record IDs must be unique nonempty strings of at most 256 characters")
        seen.add(key)
        coords = row.get("coord")
        if not isinstance(coords, list) or len(coords) != width:
            raise ValueError(f"{key}: expected {width} explicitly supplied coordinates")
        for x in coords:
            integer(x, "coordinate", MAX_COORD)
        if "n" in row:
            integer(row["n"], "n")
        if "layer" in row:
            integer(row["layer"], "layer", MAX_COORD)
        if not isinstance(row.get("fields", {}), dict):
            raise ValueError("fields must be an object")
    edges = data.get("relations", [])
    if not isinstance(edges, list) or len(edges) > 1_000_000:
        raise ValueError("Invalid relation list")
    for edge in edges:
        if not isinstance(edge, dict) or edge.get("source") not in seen or edge.get("target") not in seen:
            raise ValueError("Relation endpoints must refer to existing record IDs")
    _json_safe(data)
    return data


def canonical_bytes(data: dict[str, Any]) -> bytes:
    validate(data)
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def fingerprint(data: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(data)).hexdigest()


def read_data(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    if path.suffix.lower() == ".csv":
        # Meta and extra JSON columns make a CSV round trip lossless, including relations.
        text = path.read_text(encoding="utf-8-sig")
        first, sep, rest = text.partition("\n")
        if not sep or not first.startswith("#nollm-meta="):
            raise ValueError("CSV must begin with #nollm-meta=<JSON>; use the documented exporter")
        meta = json.loads(first[len("#nollm-meta="):])
        rows = []
        for row in csv.DictReader(io.StringIO(rest)):
            obj = json.loads(row["extra_json"])
            obj.update(id=row["id"], coord=json.loads(row["coord_json"]))
            rows.append(obj)
        meta["records"] = rows
        return validate(meta)
    return validate(json.loads(path.read_text(encoding="utf-8-sig")))


def write_data(data: dict[str, Any], path: str | Path) -> None:
    validate(data)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix.lower() != ".csv":
        path.write_bytes(canonical_bytes(data) + b"\n")
        return
    meta = {k: v for k, v in data.items() if k != "records"}
    with path.open("w", encoding="utf-8", newline="") as f:
        f.write("#nollm-meta=" + json.dumps(meta, ensure_ascii=False, separators=(",", ":")) + "\n")
        w = csv.writer(f)
        w.writerow(("id", "coord_json", "extra_json"))
        for row in data["records"]:
            extra = {k: v for k, v in row.items() if k not in ("id", "coord")}
            w.writerow((row["id"], json.dumps(row["coord"]), json.dumps(extra, ensure_ascii=False)))


def legacy_html(path: str | Path) -> dict[str, Any]:
    """Read a legacy JSON point table; never execute embedded JavaScript."""
    text = Path(path).read_text(encoding="utf-8")
    marker = "const P="
    if marker not in text:
        raise ValueError("No legacy const P= table found")
    table, _ = json.JSONDecoder().raw_decode(text.split(marker, 1)[1].lstrip())
    if not isinstance(table, list) or not table:
        raise ValueError("Empty legacy point table")
    rows = []
    for n, item in enumerate(table):
        if not isinstance(item, list) or len(item) != 4:
            raise ValueError("Legacy rows must contain [q,r,prime,v2]")
        q, r, prime, v2 = item
        if prime not in (0, 1):
            raise ValueError("Invalid legacy prime flag")
        rows.append({"id": str(n), "n": n, "coord": [q, r], "fields": {
            "prime": bool(prime), "v2": None if n == 0 else v2}})
    return validate({"schema": SCHEMA, "kind": "hex", "title": "Legacy radix-4 hex audit",
        "metadata": {"typing": "A2_IMPLEMENTATION_CARRIER_NOT_X6_NATIVE_IDENTITY",
                     "source_sha256": hashlib.sha256(Path(path).read_bytes()).hexdigest(),
                     "zero_v2": "null, not a finite valuation"}, "records": rows, "relations": []})


def demo_hex(count: int = 65536) -> dict[str, Any]:
    integer(count, "count", MAX_POINTS)
    if count < 1:
        raise ValueError("count must be positive")
    sieve = bytearray(b"\1") * count
    sieve[:min(2, count)] = b"\0" * min(2, count)
    for p in range(2, math.isqrt(count - 1) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:count:p] = b"\0" * (((count - 1 - start) // p) + 1)
    positions = [(0, 0)] * count
    rows = []
    for n in range(count):
        a, b = positions[n // 4]
        digit = n % 4
        q, r = -2*b + (digit & 1), 2*a + 2*b + (digit >> 1)
        positions[n] = (q, r)
        rows.append({"id": str(n), "n": n, "coord": [q, r],
                     "layer": (n.bit_length() + 1) // 2,
                     "fields": {"prime": bool(sieve[n]), "v2": (n & -n).bit_length()-1 if n else None}})
    return validate({"schema": SCHEMA, "kind": "hex", "title": f"Radix-4 / {count:,} integers",
        "metadata": {"typing": "A2_IMPLEMENTATION_CARRIER_NOT_X6_NATIVE_IDENTITY",
            "encoding": "F(4n+d)=2*R60*F(n)+(d&1,d>>1)",
            "layer_semantics": "synthetic radix digit depth; NOT Nollm physical layers",
            "zero_v2": "null"}, "records": rows, "relations": []})


def demo_x6() -> dict[str, Any]:
    from itertools import product
    rows = [{"id": f"x{i}", "coord": list(c), "fields": {"native_norm_sq": sum(x*x for x in c)}}
            for i, c in enumerate(product((-1, 0, 1), repeat=6))]
    return validate({"schema": SCHEMA, "kind": "x6", "title": "X6 signed test cube / 729 states",
        "metadata": {"typing": "SYNTHETIC_EXPLICIT_X6_TEST_DATA", "anchor": [0]*6,
            "warning": "Not a reconstruction of missing native coordinates for the hex demo"},
        "records": rows, "relations": []})


def hex_norm_sq(q: int, r: int) -> int:
    return q*q + q*r + r*r


def hex_distance(a: Iterable[int], b: Iterable[int]) -> int:
    q, r = (x-y for x, y in zip(a, b))
    return max(abs(q), abs(r), abs(q+r))


def rotate_hex(coord: Iterable[int], turns: int = 1) -> tuple[int, int]:
    q, r = coord
    for _ in range(turns % 6):
        q, r = -r, q+r
    return q, r


def cube_coordinate(coord: Iterable[int]) -> tuple[int, int, int]:
    q, r = coord
    return q, r, -q-r


def project_x6(coord: Iterable[int], axes: Iterable[int] | None = None) -> tuple[int, int, int]:
    c = tuple(coord)
    if len(c) != 6:
        raise ValueError("X6 projection requires all six components")
    if axes is not None:
        selected = tuple(axes)
        if len(selected) != 3 or len(set(selected)) != 3 or any(i not in range(6) for i in selected):
            raise ValueError("Choose three distinct axes in 0..5")
        return tuple(c[i] for i in selected)
    # A declared display convention, NOT the completed global native-to-FCC bridge.
    return tuple(sum(c[i]*FCC_AXES[i][j] for i in range(6)) for j in range(3))


def collision_groups(data: dict[str, Any], axes: Iterable[int] | None = None) -> list[dict[str, Any]]:
    validate(data)
    bins: dict[tuple[int, ...], list[str]] = defaultdict(list)
    for row in data["records"]:
        point = project_x6(row["coord"], axes) if data["kind"] == "x6" else tuple(row["coord"])
        bins[point].append(row["id"])
    return [{"position": list(p), "ids": ids} for p, ids in sorted(bins.items()) if len(ids) > 1]


def neighborhood(data: dict[str, Any], record_id: str, radius: int = 1) -> list[str]:
    validate(data)
    integer(radius, "radius", MAX_COORD)
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    by_id = {r["id"]: r for r in data["records"]}
    if record_id not in by_id:
        raise KeyError(record_id)
    center = by_id[record_id]["coord"]
    def dist(row: dict[str, Any]) -> int:
        if data["kind"] == "hex":
            return hex_distance(row["coord"], center)
        return sum(abs(a-b) for a, b in zip(row["coord"], center))
    return [row["id"] for row in data["records"] if dist(row) <= radius]


def trajectory(data: dict[str, Any], start_n: int, multiplier: int, steps: int = 8) -> list[str]:
    validate(data)
    integer(start_n, "start_n")
    integer(multiplier, "multiplier")
    integer(steps, "steps", 10000)
    if steps < 1:
        raise ValueError("steps must be positive")
    by_n: dict[int, str] = {}
    for row in data["records"]:
        if "n" in row:
            if row["n"] in by_n:
                raise ValueError("Trajectory is ambiguous: n is not unique")
            by_n[row["n"]] = row["id"]
    result, visited = [], set()
    n = start_n
    for _ in range(steps):
        if n not in by_n or n in visited:
            break
        result.append(by_n[n]); visited.add(n); n *= multiplier
    return result


def q16(n: int, weight: int = 2731) -> tuple[int, int]:
    integer(n, "Q16 input", 65535)
    integer(weight, "Q16 weight", 65536)
    if n < 0 or weight < 0:
        raise ValueError("Q16 values must be nonnegative")
    return divmod(n * weight, 65536)


def profile(data: dict[str, Any], axis: int | str) -> list[dict[str, Any]]:
    validate(data)
    width = 2 if data["kind"] == "hex" else 6
    if axis != "s" and (isinstance(axis, bool) or not isinstance(axis, int) or axis not in range(width)):
        raise ValueError("Invalid profile axis")
    if axis == "s" and data["kind"] != "hex":
        raise ValueError("s is an A2 carrier coordinate only")
    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in data["records"]:
        c = row["coord"]
        level = -c[0]-c[1] if axis == "s" else c[axis]
        grouped[level].append(row)
    return [{"level": k, "count": len(rows),
             "prime_count": sum(r.get("fields", {}).get("prime") is True for r in rows),
             "ids": [r["id"] for r in rows]} for k, rows in sorted(grouped.items())]


def html(data: dict[str, Any], path: str | Path) -> Path:
    """Generate one self-contained local HTML; no CDN or external service."""
    validate(data)
    payload = canonical_bytes(data).decode("utf-8").replace("<", "\\u003c")
    template = Path(__file__).with_name("workbench.html").read_text(encoding="utf-8")
    text = template.replace("0.2.0", VERSION).replace("__PAYLOAD__", payload).replace("__FINGERPRINT__", fingerprint(data))
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path