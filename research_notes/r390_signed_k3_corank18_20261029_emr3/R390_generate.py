#!/usr/bin/env python3
"""R390 reproducible source builder. Uses R389 immutable raw signed K/J implementation.
Run in research_notes/r390_... alongside research_notes/r389_... .
Produces r390_exact.py, r390_symbolic.py, r390_certify.py. Then run the
symbolic and certificate programs in that order. No network or floating signs.
"""
from pathlib import Path

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'r389_signed_k3_corank17_20261029_emr3'
assert SOURCE.is_dir(), 'R389 source directory required beside R390'

def convert(name,replacements):
    s=(SOURCE/name).read_text()
    s=s.replace('r389_', 'r390_').replace('R389_', 'R390_').replace('R389','R390')
    s=s.replace('CORANK17','CORANK18').replace('corank-17','corank-18').replace('corank 17','corank 18')
    for old,new in replacements:
        assert old in s,(name,'missing source marker',old)
        s=s.replace(old,new)
    dest=HERE/name.replace('389','390')
    dest.write_text(s)
    return dest

convert('r389_exact.py',[
    ('def eval_at(theta,r=17):','def eval_at(theta,r=18):'),
    ('corank r=17','corank r=18'),
])
convert('r389_symbolic.py',[
    ('R=17','R=18'),
    ('assert len(out)==35 and len(tur)==33','assert len(out)==37 and len(tur)==35'),
    ('comb(34,17),18','comb(36,18),19'),
    ('**34','**36'),
    ('C34 = 129644790*(30-16theta)^34','C36 = 477638700*(30-16theta)^36'),
])
convert('r389_certify.py',[
    ('len(C)==35 and len(T)==33','len(C)==37 and len(T)==35'),
    ('F(1859526,1000000),F(1859527,1000000)','F(1863973,1000000),F(1863974,1000000)'),
    ('T[16]','T[18]'),
    ('j==17','j==19'),
    ('T17','T19'),
    ('assert total==476','assert total==504'),
    ('list(range(18,35))','list(range(19,37))'),
    ("'r':17", "'r':18"),
    ('35-entry finite raw-D signed K3 corank-18','37-entry finite raw-D signed K3 corank-18'),
    ('eta17','eta18'),
    ('(1859526/1000000,1859527/1000000)','(1863973/1000000,1863974/1000000)'),
])
print('R390_SOURCE_GENERATED')
