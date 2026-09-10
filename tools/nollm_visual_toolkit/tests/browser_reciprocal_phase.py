"""Focused Chromium acceptance for reciprocal-phase 11/16-bit pages."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from nollm_visual_toolkit import reciprocal_phase_lab as r


def main():
    from playwright.sync_api import sync_playwright
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    checks=[];errors=[];requests=[]
    def ck(name,cond):
        assert cond,name;checks.append(name);print('PASS',name,flush=True)
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        for bits,expected_occ,p2 in ((11,57342,256),(16,57339,8192)):
            html=r.build(a.out/f'reciprocal-{bits}.html',count=65536,phase_bits=bits)
            page=browser.new_page(viewport={'width':1400,'height':900})
            page.on('pageerror',lambda e:errors.append(str(e)));page.on('request',lambda req:requests.append(req.url))
            page.set_content(html.read_text(encoding='utf-8'),wait_until='load');page.evaluate('NumberFieldLab.preset("inverse")')
            page.wait_for_function('NumberFieldLab.status().drawn===65536')
            st=page.evaluate('NumberFieldLab.status()')
            ck(f'{bits}_mode_inverse',st['state']['mode']=='inverse')
            ck(f'{bits}_occupied',st['occupied_cells']==expected_occ)
            ck(f'{bits}_multiplication',st['exact_failures']==0)
            ck(f'{bits}_p2_tick',page.evaluate('NumberFieldLab.phase(2)')==p2)
            ck(f'{bits}_no_page_error',not errors)
            page.close()
        ck('no_external_requests',not any(x.startswith(('http:','https:')) for x in requests))
        browser.close()
    result={'schema':'NOLLM_RECIPROCAL_PHASE_UI_ACCEPTANCE_V1','checks_passed':len(checks),'checks':checks,'page_errors':errors,'external_requests':[x for x in requests if x.startswith(('http:','https:'))]}
    (a.out/'reciprocal_browser.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('TOTAL',len(checks),flush=True)

if __name__=='__main__':main()
