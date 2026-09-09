"""Preserve exact downloaded factual tables using lossless UTF-8 transport."""
import base64,gzip,hashlib,json,textwrap
from pathlib import Path
A=Path(__file__).resolve().parent
out=A/"source_inputs";out.mkdir(exist_ok=True)
items=[
("tos-gaps-t0.txt.gz","https://sweet.ua.pt/tos/gaps/t0.txt.gz","7227a85c31cbfc16e4bbd5588d4b3bb1a9c11e360d558745cc55e73b9f5d11b7"),
("tos-primecount-1d12.txt.gz","https://sweet.ua.pt/tos/primes/1d12.txt.gz","4b98cbfffa074b533ecbb4b793ddb3a315cfa567626169611f5c432384950042")]
rows=[]
for name,url,expected in items:
    raw=(A/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==expected
    text=("\n".join(textwrap.wrap(base64.b64encode(raw).decode("ascii"),76))+"\n").encode("ascii")
    target=out/(name+".base64.txt")
    if target.exists():raise FileExistsError(str(target))
    target.write_bytes(text)
    assert base64.b64decode(text)==raw
    decoded=gzip.decompress(raw)
    rows.append({"path":target.relative_to(A).as_posix(),"original_compressed_name":name,
                 "decoded_name":name[:-3],"source_url":url,
                 "original_successful_transport":"PowerShell Invoke-WebRequest with default Windows TLS certificate validation",
                 "compressed_bytes":len(raw),"compressed_sha256":expected,
                 "decoded_bytes":len(decoded),"decoded_sha256":hashlib.sha256(decoded).hexdigest(),
                 "encoded_bytes":len(text),"encoded_sha256":hashlib.sha256(text).hexdigest()})
target=A/"source_input_manifest.json"
if target.exists():raise FileExistsError(str(target))
target.write_text(json.dumps({"schema":"R005_SOURCE_INPUT_TRANSPORT_V1","files":rows},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"source_input_files":len(rows),"all_roundtrip_exact":True}),flush=True)

