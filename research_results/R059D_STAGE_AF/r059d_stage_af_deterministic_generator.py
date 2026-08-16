#!/usr/bin/env python3
"""R059D Stage AF deterministic derived-data and candidate generator.

This script has two deliberately separated roles:
1. derive AF jump/state observables from the frozen pre-candidate radius/word ledgers;
2. run the N-only J candidate as a forward autonomous integer recurrence.

It does NOT query the orthogonal source-circle Q oracle at candidate runtime and does
NOT claim to generate B or the boundary word.
"""
import json,base64,zlib,lzma,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(name):
    o=json.loads((ROOT/name).read_text())
    codec=o.get('codec') if isinstance(o,dict) else None
    if codec:
        raw=base64.b64decode(o['compressed_payload_b64'])
        if codec=='zlib+base64': raw=zlib.decompress(raw)
        elif codec=='lzma+base64': raw=lzma.decompress(raw)
        else: raise ValueError(codec)
        assert hashlib.sha256(raw).hexdigest()==o['uncompressed_sha256']
        return json.loads(raw)
    return o

def n_j_candidate(R=512):
    """Forward-autonomous N-only candidate. Integer arithmetic only."""
    j=0; out=[]
    for r in range(1,R+1):
        u=3*j+2; v=3*r
        if 3*u*u + 6*u*v - v*v <= 0:
            j+=1
        out.append(j)
    return out

def derive():
    radius=load('R059D_STAGE_AF_RADIUS_LEDGER.json')
    words=load('R059D_STAGE_AF_BOUNDARY_WORD_REGISTRY.json')
    ix={name:i for i,name in enumerate(radius['fields'])}
    out={'schema':'R059D_STAGE_AF_DERIVED_REPLAY_V1','N':{},'C':{}}
    for arm in ('N','C'):
        rows=radius[arm]
        B=[x[ix['B']] for x in rows]; J=[x[ix['J']] for x in rows]
        dB=[B[0]]+[B[i]-B[i-1] for i in range(1,len(B))]
        dJ=[J[0]]+[J[i]-J[i-1] for i in range(1,len(J))]
        d2B=[dB[0]]+[dB[i]-dB[i-1] for i in range(1,len(dB))]
        KB=[r for r in range(2,len(B)+1) if d2B[r-1]!=0]
        KJ=[r for r in range(2,len(B)+1) if dJ[r-1]!=0]
        out[arm]={'K_B':KB,'K_J':KJ,'B_512':B[-1],'J_512':J[-1],
                  'DeltaB_max':max(dB),'DeltaJ_hist':{str(v):dJ.count(v) for v in sorted(set(dJ))},
                  'word_rows':len(words[arm])}
    out['N_J_candidate']=n_j_candidate(512)
    return out

if __name__=='__main__':
    print(json.dumps(derive(),sort_keys=True,separators=(',',':')))
