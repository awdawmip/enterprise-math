"""Losslessly package the original per-block bytes as readable-transport text."""
import base64,gzip,hashlib,io,json,tarfile,textwrap
from pathlib import Path
A=Path(__file__).resolve().parent
R=A/"construction_full"
def sha(data): return hashlib.sha256(data).hexdigest()
def main():
    byte_manifest_path=A/"construction_input_byte_manifest.json"
    byte_manifest=byte_manifest_path.read_bytes()
    expected={x["path"]:x for x in json.loads(byte_manifest)["files"]}
    assert len(expected)==4000
    out=A/"block_archives";out.mkdir(exist_ok=True)
    groups=[];verified=0
    for first in range(0,4000,1000):
        last=first+999
        buffer=io.BytesIO();source={}
        with tarfile.open(fileobj=buffer,mode="w",format=tarfile.USTAR_FORMAT) as tar:
            for index in range(first,last+1):
                member=f"blocks/{index:05d}.json"
                path=R/member
                raw=path.read_bytes()
                record=expected["construction_full/"+member]
                assert len(raw)==record["bytes"] and sha(raw)==record["sha256"]
                info=tarfile.TarInfo(member);info.size=len(raw);info.mode=0o644
                info.uid=info.gid=0;info.uname=info.gname="";info.mtime=0
                tar.addfile(info,io.BytesIO(raw))
                source[member]=raw
        tar_bytes=buffer.getvalue()
        compressed=gzip.compress(tar_bytes,compresslevel=9,mtime=0)
        encoded=("".join(x+"\n" for x in textwrap.wrap(base64.b64encode(compressed).decode("ascii"),76))).encode("ascii")
        decoded=gzip.decompress(base64.b64decode(encoded))
        assert decoded==tar_bytes
        with tarfile.open(fileobj=io.BytesIO(decoded),mode="r:") as tar:
            assert set(tar.getnames())==set(source)
            for member in tar.getmembers():
                assert tar.extractfile(member).read()==source[member.name]
                verified+=1
        filename=f"blocks_{first:05d}_{last:05d}.tar.gz.base64.txt"
        path=out/filename
        if path.exists(): raise FileExistsError(str(path))
        path.write_bytes(encoded)
        groups.append({"path":path.relative_to(A).as_posix(),"first_block":first,"last_block":last,"file_count":1000,
                       "encoding":"BASE64_OF_GZIP_OF_POSIX_USTAR","encoded_bytes":len(encoded),"encoded_sha256":sha(encoded),
                       "gzip_bytes":len(compressed),"gzip_sha256":sha(compressed),"tar_bytes":len(tar_bytes),"tar_sha256":sha(tar_bytes),
                       "raw_member_bytes":sum(map(len,source.values())),"roundtrip_exact_files":1000})
    manifest={"schema":"R005_LOSSLESS_RAW_BLOCK_ARCHIVES_V1","source_byte_manifest_path":"construction_input_byte_manifest.json",
              "source_byte_manifest_sha256":sha(byte_manifest),"groups":groups,"total_files":4000,
              "all_original_bytes_roundtrip_verified":verified==4000,
              "scope":"Every original block file, including labels, endpoints, counts, maxima, rows, sequence digests and actual run timestamps. No prime sequence is inferred from its digest."}
    path=A/"block_archive_manifest.json"
    if path.exists(): raise FileExistsError(str(path))
    path.write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"files_verified":verified,"encoded_bytes":sum(x["encoded_bytes"] for x in groups),"groups":groups}),flush=True)
if __name__=="__main__": main()

