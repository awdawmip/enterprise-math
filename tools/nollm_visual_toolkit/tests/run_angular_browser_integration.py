#!/usr/bin/env python3
"""Run actual offline Chromium pages; never substitute a mocked DOM.

Requires Playwright and Chromium. No installation/download is done by this script.
Use --chromium for a system binary. --baseline supplies the frozen original UI template.
The full repo's src may be used; the delivery bundle uses an explicitly labeled
BRC source slice, but the real toolkit package initializer is always executed.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import runpy
import json
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT/'tools/nollm_visual_toolkit'), str(ROOT/'src')]
from nollm_visual_toolkit import multiplication_lab as lab
from nollm_visual_toolkit.angular_dispersion import AngularDispersion

NEW_KEYS = {'angular_cv_squared_exact','angular_cv_role','angular_count_source','angular_exact_backend'}


def digest(value):
    raw=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--populations',type=int,nargs='+',default=[16,256,4096,65536],choices=[16,256,4096,65536])
    parser.add_argument('--chromium',default=shutil.which('chromium') or shutil.which('google-chrome'))
    args=parser.parse_args()
    from playwright.sync_api import sync_playwright
    raw=args.baseline.read_bytes()
    baseline_blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert baseline_blob=='e11e881dff2b1a1f259b260c4f7d85ec184dd41a','baseline source drift'
    template=runpy.run_path(str(args.baseline))['TEMPLATE']
    scenarios=[{'count':count,'state':{'layout':layout,'mode':mode,'scale':scale,'overrides':{}}}
        for count,layout,mode,scale in itertools.product(sorted(set(args.populations)),('polar','legacy'),('golden','rank','zero'),(0.5,1,3))]
    errors=[];requests=[];checks=[]
    with tempfile.TemporaryDirectory(prefix='angular-page-') as tmp, sync_playwright() as p:
        root=Path(tmp)
        kwargs={'headless':True,'args':['--no-sandbox']}
        if args.chromium:kwargs['executable_path']=args.chromium
        browser=p.chromium.launch(**kwargs)
        version=browser.version
        def new_page(html):
            page=browser.new_page(viewport={'width':1440,'height':1000},accept_downloads=True)
            page.on('pageerror',lambda e:(errors.append(str(e)),print('pageerror:',e,flush=True)))
            page.on('request',lambda request:requests.append(request.url))
            page.set_content(html,timeout=60000)
            page.wait_for_function('window.NumberFieldLab && NumberFieldLab.status().drawn>0',timeout=10000)
            return page
        for count in sorted({s['count'] for s in scenarios}):
            print('population',count,flush=True)
            payload=json.dumps(lab.make_payload(count),ensure_ascii=False,separators=(',',':'),allow_nan=False).replace('<','\\u003c')
            old_page=new_page(template.replace('__LAB_PAYLOAD__',payload))
            cases=[s for s in scenarios if s['count']==count]
            old_reports=[old_page.evaluate('(s)=>{NumberFieldLab.configure(s);return NumberFieldLab.report()}',case['state']) for case in cases]
            old_page.close()
            page=new_page(lab.build_lab(root/f'new-{count}.html',count=count).read_text())
            for case,old_report in zip(cases,old_reports):
                report=page.evaluate('(s)=>{NumberFieldLab.configure(s);return NumberFieldLab.report()}',case['state'])
                legacy={k:v for k,v in report.items() if k not in NEW_KEYS}
                assert legacy==old_report,('legacy drift',count,case['state'])
                expected=AngularDispersion.from_counts(report['angular_counts']).as_record(scale=10**6)
                assert report['angular_cv_squared_exact']==expected,('exact mismatch',count,case['state'])
                tag='EXACT_MODULAR_PHASE_BINS' if case['state']['layout']=='polar' else 'APPROXIMATE_ATAN2_BINS'
                assert report['angular_count_source']==tag
                rd=expected['readout']
                assert page.locator('#cv').inner_text()==rd['integer']+' / '+rd['scale']
                assert page.locator('#cvResidual').inner_text()=='+ '+rd['residual_numerator']+' / '+rd['residual_denominator']
                assert report['angular_cv_role']=='LEGACY_FLOAT_DISPLAY_NOT_EXACT_EVIDENCE'
                checks.append({'count':count,'state':case['state'],'legacy_report_sha256':digest(legacy),
                    'exact_record_sha256':digest(expected),'count_source':tag})
            print('18 paired scenarios done',count,flush=True)
            if count==256:
                print('roundtrips begin',flush=True)
                page.evaluate("NumberFieldLab.configure({layout:'polar',mode:'rank',scale:2,overrides:{5:12345},limit:127,selected:3})")
                page.wait_for_function('NumberFieldLab.status().drawn===128')
                before=page.evaluate('NumberFieldLab.report()')
                # Full JSON download uses the actual button, not a reconstructed object.
                page.locator('summary').click(timeout=10000)
                print('download begin',flush=True)
                with page.expect_download(timeout=10000) as pending:page.locator('#report').click(timeout=10000)
                download=pending.value;download.save_as(root/'report.json')
                exported=json.loads((root/'report.json').read_text())
                assert exported==page.evaluate('NumberFieldLab.report()')
                assert exported['angular_cv_squared_exact']==before['angular_cv_squared_exact']
                print('download done',flush=True)
                saved=page.evaluate('NumberFieldLab.exportHTML()')
                restored=new_page(saved)
                restored.wait_for_function('NumberFieldLab.status().drawn===128')
                assert restored.evaluate('NumberFieldLab.report()')==before
                restored.close()
                original=page.evaluate('NumberFieldLab.rawData()')
                assert original==lab.make_payload(256)['data']
                # Display-scale, camera and stacked view must not change phase-bin statistics.
                for change in ({'scale':0.5},{'zoom':2,'yaw':1},{'stack':True,'pitch':0.75}):
                    page.evaluate('(s)=>NumberFieldLab.configure(s)',change)
                    assert page.evaluate('NumberFieldLab.report().angular_cv_squared_exact')==before['angular_cv_squared_exact']
            page.close()
        # Gallery embeds a working page, rather than just containing replacement text.
        print('gallery begin',flush=True)
        gallery=lab.build_lab_site(root/'gallery',count=16).read_text()
        gallery_page=browser.new_page(viewport={'width':1440,'height':1000})
        gallery_page.on('pageerror',lambda e:(errors.append(str(e)),print('pageerror:',e,flush=True)))
        gallery_page.on('request',lambda request:requests.append(request.url))
        gallery_page.set_content(gallery)
        gallery_page.wait_for_function("document.querySelector('iframe').contentWindow.NumberFieldLab?.status().drawn===16")
        gallery_page.locator('a[href="multiplication.html#zero"]').click()
        report=gallery_page.evaluate("document.querySelector('iframe').contentWindow.NumberFieldLab.report()")
        assert report['angular_cv_squared_exact']['readout']['integer']=='63000000'
        assert report['angular_cv_squared_exact']['readout']['residual_numerator']=='0'
        gallery_page.close();browser.close()
    assert not errors,errors
    assert not requests,requests
    result={'schema':'M02_CHROMIUM_INTEGRATION_V1','baseline_template_blob':baseline_blob,'comparison':'live original frozen template versus migrated template; identical payload generator unchanged in this slice','browser':version,'entry':'actual generated HTML via Playwright set_content',
        'scenarios':checks,'legacy_unchanged':len(checks),'exact_python_brc_matches':len(checks),
        'json_download_roundtrip':256 in args.populations,'saved_html_reload':256 in args.populations,'source_data_unchanged':256 in args.populations,
        'display_changes_do_not_change_exact_statistic':3 if 256 in args.populations else 0,'embedded_gallery_preset':True,
        'page_errors':errors,'network_requests':requests,'not_claimed':['file-URL navigation','Safari/iOS','full Enterprise Math initializer','whole repository tests','independent review']}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='scenarios'},ensure_ascii=False,indent=2))
    return 0


if __name__=='__main__':raise SystemExit(main())
