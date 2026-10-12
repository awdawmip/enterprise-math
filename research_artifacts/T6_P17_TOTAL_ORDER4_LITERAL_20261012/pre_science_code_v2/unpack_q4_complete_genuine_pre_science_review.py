#!/usr/bin/env python3
"""Strict byte-only recovery of the complete independent q4 pre-science review."""
import argparse, base64, hashlib, json, re, zlib
from pathlib import Path, PurePosixPath
def fail(message): raise ValueError(message)
def obj(pairs):
    out={}
    for k,v in pairs:
        if k in out: fail("duplicate JSON key")
        out[k]=v
    return out
def load(raw):
    return json.loads(raw.decode("utf-8"),object_pairs_hook=obj,parse_constant=lambda x:fail("nonfinite JSON"))
def sha(raw): return hashlib.sha256(raw).hexdigest()
def blob(raw): return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def b64(value):
    if not isinstance(value,str) or not value.isascii(): fail("base64 text")
    raw=base64.b64decode(value,validate=True)
    if base64.b64encode(raw).decode()!=value: fail("noncanonical base64")
    return raw
def require(test,message):
    if not test: fail(message)
def recover(path,output):
    outer_raw=path.read_bytes()
    require(len(outer_raw)<=1048576,"outer limit")
    p=load(outer_raw)
    require(p["schema"]=="T6_Q4_INDEPENDENT_COMPLETE_PRE_SCIENCE_REVIEW_LOSSLESS_CAPSULE_V1","schema")
    require(p["reviewer"]=="EM-DVR-F9E6BA" and p["review_only_no_scientific_construction"] is True,"review provenance")
    require(p["scientific_q4_result_or_native_acceptance"] is False,"scope")
    size=p["inner_json_bytes"]
    require(type(size) is int and 0<size<=4194304,"inner limit")
    raw=b64(p["payload_base64"])
    require(len(raw)==p["gzip_bytes"] and sha(raw)==p["gzip_sha256"],"gzip pin")
    decoder=zlib.decompressobj(31)
    inner=decoder.decompress(raw,size+1)
    require(decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail,"single gzip/EOF")
    require(len(inner)==size and sha(inner)==p["inner_json_sha256"],"inner pin")
    data=load(inner)
    require(data["schema"]=="T6_Q4_COMPLETE_REVIEW_ORIGINAL_BYTES_V1","member schema")
    pins=p["files"]
    require(type(pins) is list and len(pins)==p["original_count"]==60,"member count")
    index={x["path"]:x for x in pins}
    require(len(index)==60,"duplicate path")
    require(len(data["files"])==60,"member count")
    recovered=[]
    for x in data["files"]:
        name=x["path"]; pure=PurePosixPath(name)
        require(not pure.is_absolute() and str(pure)==name and all(re.fullmatch("[A-Za-z0-9_.-]+",t) and t not in {".",".."} for t in pure.parts),"safe path")
        pin={k:x[k] for k in ["path","bytes","sha256","git_blob_sha1"]}
        require(pin==index.get(name),"member/index join")
        val=b64(x["content_base64"])
        require(len(val)==pin["bytes"] and sha(val)==pin["sha256"] and blob(val)==pin["git_blob_sha1"],"original bytes/hash/blob")
        recovered.append((name,val))
    require(len({n for n,_ in recovered})==60,"duplicate member")
    require(sum(len(v) for _,v in recovered)==p["original_bytes"],"total bytes")
    require(not output.exists(),"fresh destination")
    output.mkdir(parents=True)
    for name,val in recovered:
        dest=output.joinpath(*PurePosixPath(name).parts);dest.parent.mkdir(parents=True,exist_ok=True)
        with dest.open("xb") as stream:stream.write(val)
    return {"originals":60,"bytes":p["original_bytes"],"exact_bytes_SHA_Gitblob_verified":True,"restored_code_executed":False,"scientific_q4_execution":False}
if __name__=="__main__":
    cli=argparse.ArgumentParser();cli.add_argument("capsule",type=Path);cli.add_argument("--output",type=Path,required=True)
    args=cli.parse_args();print(json.dumps(recover(args.capsule,args.output),sort_keys=True))

