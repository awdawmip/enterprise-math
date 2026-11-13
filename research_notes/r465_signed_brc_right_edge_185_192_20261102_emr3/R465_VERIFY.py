#!/usr/bin/env python3
"""R465 reproducible exact coefficients. Run within repository checkout.
Reuses pinned R464 fast integer multiplication and R463 E/O/R proof kernel.
"""
import sys,json,importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
OLD=BASE/'r464_signed_brc_right_edge_177_184_20261102_emr3'/'R464_REPRODUCE.py'
assert OLD.exists(), OLD
spec=importlib.util.spec_from_file_location('r464_source_reused',OLD)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
core=module.core
HASHES={
185:'d34a263640b720f9c054a1afa6faa9acd929e7f1f66c1dc89fa8abeb4f116766',
186:'06e4f181764a4ba3812ac9b460a2300445cd9a30d0f15885cd5328e954f21b5f',
187:'d965d976b938b7cbdb69ccfeda2a09341c71e21b3094f0a3edcd9e698cc655e9',
188:'959c2964ad14acaece650b6adc9c948d441325c0115eeaba18785511d190c3a8',
189:'c6597419bfe3bac18eaf9b53ad396770c5acda12d1e01e9b7ab2899a506afcc0',
190:'d3d46c200b29e61e36109bbee7c656e5fb9ad403b1073ec467de29771290d2cb',
191:'c8a528624b594f4c1f626f2b9f2ae0fcf2bdce2b58903ce7da3ac37b6139c58f',
192:'1492fa152a818b66a6cb421d5f5a5080414a14c8448a452153c6d1b46f6743bc',
}
def main():
    lo=int(sys.argv[1]) if len(sys.argv)>1 else 185
    hi=int(sys.argv[2]) if len(sys.argv)>2 else 192
    assert 185<=lo<=hi<=192
    regression=core.s_certificate(175)
    assert regression['sha256']=='5a68b3d2ced114ee7744e5a75b8553717314a3d0ea1b5b497b0739ba09847239'
    rows=[]
    for s in range(lo,hi+1):
        row=core.s_certificate(s,detail=True)
        assert row['sha256']==HASHES[s] and row['strict_positive_coefficients']==10*s+2
        rows.append(row)
        print('R465_CERTIFICATE_PASS',json.dumps(row,sort_keys=True),flush=True)
    out={'status':'R465_EXACT_PASS','range':[lo,hi],'rows':rows,
         'positive_coefficients':sum(x['strict_positive_coefficients'] for x in rows)}
    Path('R465_VERIFIED_'+str(lo)+'_'+str(hi)+'.json').write_text(json.dumps(out,indent=2)+'\n')
    print('R465_REPRODUCE_PASS',out['positive_coefficients'],flush=True)
if __name__=='__main__':main()
