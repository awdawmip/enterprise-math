from pathlib import Path
import hashlib, json
p=Path(__file__).resolve().parent
files=[]
for f in sorted(p.iterdir()):
    if f.is_file() and f.name!='TV_MANIFEST.json':
        b=f.read_bytes()
        files.append(dict(path=f.name,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob_sha1=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()))
out=dict(status='AUTHOR_UNREVIEWED_NOT_ADMITTED',activity='RA-CAAAC604CB513AEA8BBC1DFC',cf_source='58e689cbebb73b0ceaedfc33e5daebad34d0ca48',files=files)
(p/'TV_MANIFEST.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
