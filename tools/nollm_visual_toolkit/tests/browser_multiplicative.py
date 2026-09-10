"""Chromium acceptance for the standalone Multiplicative Memory Field Lab."""
from __future__ import annotations
import argparse
import json
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nollm_visual_toolkit import multiplicative as m


def main() -> None:
    from playwright.sync_api import sync_playwright
    ap = argparse.ArgumentParser(); ap.add_argument('--out', type=Path, required=True); a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    html = m.multiplicative_html(a.out / 'multiplicative-65536.html', count=65536)
    requests=[]; errors=[]; checks=[]
    def ck(name, cond):
        assert cond, name; checks.append(name); print('PASS', name, flush=True)
    with sync_playwright() as pw:
        kw={'headless':True}; exe=os.environ.get('CHROMIUM_PATH','/usr/bin/chromium')
        if Path(exe).exists(): kw['executable_path']=exe
        browser=pw.chromium.launch(**kw)
        page=browser.new_page(viewport={'width':1500,'height':920})
        page.on('request', lambda r: requests.append(r.url)); page.on('pageerror', lambda e: errors.append(str(e)))
        page.set_content(html.read_text(encoding='utf-8'), wait_until='load')
        page.wait_for_function('NollmMultiplicativeLab.status().N===65536', timeout=30000)
        status=page.evaluate('NollmMultiplicativeLab.status()')
        default_status=dict(status)
        ck('full_65536_carrier_built', status['N']==65536)
        ck('finite_density_metrics', float(status['angularCV'])>=0 and float(status['radialCV'])>=0 and float(status['angularToIid'])>=0)
        ck('hybrid_near_iid_sector_scale', float(status['angularToIid']) < 1.5)
        page.locator('#frameOnly').click(); page.wait_for_timeout(100)
        frame_only_status=page.evaluate('NollmMultiplicativeLab.status()')
        ck('frame_only_is_strongly_anisotropic_in_finite_probe', float(frame_only_status['angularToIid']) > 10)
        page.locator('#hybrid').click(); page.wait_for_timeout(100)
        hybrid_status=page.evaluate('NollmMultiplicativeLab.status()')
        ck('prime_2_intrinsic_phase_zero', page.evaluate('NollmMultiplicativeLab.phaseCode(2)')==0)
        for p in (3,5,7,11,97,65521):
            ck('phase_code_'+str(p), page.evaluate('p=>NollmMultiplicativeLab.phaseCode(p)', p)==m.prime_phase_code(p))
        # exact carrier law on representative composites
        for a0,b0 in ((3,5),(4,11),(12,13),(17,19),(31,37)):
            prod=a0*b0
            ck(f'carrier_add_{a0}_{b0}', page.evaluate('(x)=>NollmMultiplicativeLab.phaseAccumulator(x[0]*x[1])===NollmMultiplicativeLab.phaseAccumulator(x[0])+NollmMultiplicativeLab.phaseAccumulator(x[1])',[a0,b0]))
        page.locator('#query').fill('3'); page.locator('#multiplier').fill('5'); page.locator('#trace').click()
        ck('multiplication_trace', page.evaluate('NollmMultiplicativeLab.status().trace.slice(0,5)')==[3,15,75,375,1875])
        page.locator('#alpha').evaluate('(e)=>{e.value="0.6";e.dispatchEvent(new Event("input",{bubbles:true}))}')
        ck('observer_alpha_changes_without_rebuild', abs(page.evaluate('NollmMultiplicativeLab.status().alpha')-0.6)<1e-12)
        page.locator('#seed').fill('123456789'); page.locator('#rebuild').click(); page.wait_for_function('NollmMultiplicativeLab.status().seed===123456789')
        ck('seed_rebuild', page.evaluate('NollmMultiplicativeLab.phaseCode(11)')==m.prime_phase_code(11,123456789))
        ck('no_page_errors', not errors)
        ck('no_network_requests', not requests)
        page.screenshot(path=str(a.out/'multiplicative_field.png'))
        browser.close()
    result={'schema':'NOLLM_MULTIPLICATIVE_BROWSER_ACCEPTANCE_V1','checks_passed':len(checks),'checks':checks,'page_errors':errors,'network_requests':requests,'records':65536,'browser':'Chromium via Playwright set_content','observations':{'default_hybrid':default_status,'frame_only':frame_only_status,'hybrid_restored':hybrid_status},'limits':['Not native iOS Safari certification.','Canvas is an observer; browser pixel overlap does not merge arithmetic identities.','Angular CV comparison is a finite observer diagnostic, not an asymptotic theorem.']}
    (a.out/'multiplicative_browser_acceptance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
