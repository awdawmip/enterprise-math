#!/usr/bin/env python3
"""Independently unpack/validate R5: 91 triple-phase classes x 12 primitive orders.
The exact packed 1092 pairs are in ALL91_JETS_U16LE.b64. Python 3 stdlib only.
Data order: d-major (sorted W), then m ascending; each pair is unsigned 16-bit
little-endian (R_m(w), w*R'_m(w)) modulo that order's witness prime.
"""
from pathlib import Path
import base64, hashlib, struct, io

A={0,54,55,56,57}; B={0,60,61,62,63}; C={0,37,38,39,40,41,42}
W={7:(10039,5580),9:(10009,5783),11:(10099,792),13:(10037,5992),
   16:(10177,1750),17:(10099,4343),19:(10223,2301),23:(10259,4778),
   25:(10151,7216),27:(10099,2017),31:(10169,1836),37:(10139,1802)}
EXPECTED_BINARY_SHA256='2a728abf89c6d6756b738458ac0e47499f2e0b6ef64d44aa217354ca4ff5175a'
EXPECTED_CSV_SHA256='d6a91c4a44a0075e30a12aab9d69a3d1d5a1decb15f640f5e39b7c5217e52fe5'

def main():
    raw=base64.b64decode(Path(__file__).with_name('ALL91_JETS_U16LE.b64').read_text().strip(), validate=True)
    assert len(raw)==91*12*4==4368
    assert hashlib.sha256(raw).hexdigest()==EXPECTED_BINARY_SHA256
    ms=[m for m in range(1,79808+1) if m%58 in A and m%64 in B and m%43 in C]
    assert len(ms)==91 and ms[0]==2492 and ms[-1]==79808
    output=io.StringIO(newline='')
    output.write('m,d,prime,root,R0,DR0,pole,witness\n')
    off=0
    for d,(p,w) in W.items():
        assert (p-1)%d==0 and pow(w,d,p)==1
        assert all(pow(w,k,p)!=1 for k in range(1,d) if d%k==0)
        pole=314//d-213//d
        for m in ms:
            r0,dr0=struct.unpack_from('<HH',raw,off);off+=4
            assert 0<=r0<p and 0<=dr0<p
            witness=int(pole>=3 and (r0!=0 or (pole>=4 and dr0!=0)))
            assert witness==1,(m,d,r0,dr0,pole)
            output.write(f'{m},{d},{p},{w},{r0},{dr0},{pole},{witness}\n')
    assert off==len(raw)
    assert hashlib.sha256(output.getvalue().encode()).hexdigest()==EXPECTED_CSV_SHA256
    print('ALL CHECKS PASS: 91 phases x 12 roots = 1092 complete nonzero jets')
    print('binary_sha256=',EXPECTED_BINARY_SHA256)
    print('csv_sha256=',EXPECTED_CSV_SHA256)
    print('m min max=',ms[0],ms[-1])

if __name__=='__main__': main()
