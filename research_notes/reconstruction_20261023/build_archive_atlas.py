"""Index theorem excerpts and executable interfaces without executing archives.

Input: the preserved two extracted volumes and their original JSON manifest.
Output distinguishes searchable source claims from reviewed mathematical results.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import zipfile

CLAIM = re.compile(r'^(?:#{1,6}\s*)?(?:\*\*)?(?:Theorem|Lemma|Proposition|Corollary|定理|引理|命题|推论)(?:\s|[0-9一二三四五六七八九十（(.:：—-])', re.I)


def clean(text):
    return re.sub(r'https?://\S+', '[source-link-in-private-archive]', text)


def extract_claims(text):
    lines = text.splitlines()
    found = []
    for i, line in enumerate(lines):
        if not (CLAIM.match(line.strip()) or
                line.startswith('#') and re.search(r'定理|引理|命题|推论|Theorem|Lemma', line)):
            continue
        selected = [line]
        for following in lines[i+1:i+17]:
            if following.startswith('#') or re.match(r'\s*(?:\*\*)?(?:证明|Proof)[.：:\s]', following, re.I):
                break
            selected.append(following)
        excerpt = clean('\n'.join(selected).strip())[:1800]
        found.append((i + 1, excerpt))
    return found


def describe_tool(name, data):
    text = data.decode('utf-8-sig', errors='replace')
    result = {'language': 'python' if name.endswith('.py') else 'c++',
              'source_syntax': 'NOT_CHECKED', 'functions': [], 'classes': [],
              'imports': [], 'main_entry': False}
    if name.endswith('.py'):
        try:
            tree = ast.parse(text)
        except (SyntaxError, ValueError) as error:
            result['source_syntax'] = 'PARSE_FAILED'
            result['parse_error'] = str(error).splitlines()[0][:180]
            return result
        result['source_syntax'] = 'AST_PARSE_PASS_NOT_EXECUTED'
        result['functions'] = [n.name for n in tree.body
                               if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))][:40]
        result['classes'] = [n.name for n in tree.body if isinstance(n, ast.ClassDef)][:20]
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(n.name for n in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module)
        result['imports'] = sorted(imports)
        result['main_entry'] = '__main__' in text
        result['module_doc'] = clean(ast.get_docstring(tree) or '')[:600]
    else:
        result['main_entry'] = bool(re.search(r'\bint\s+main\s*\(', text))
        result['classes'] = re.findall(r'\b(?:struct|class)\s+([A-Za-z_]\w*)', text)[:20]
        result['imports'] = re.findall(r'#include\s*[<"]([^>"]+)', text)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recovery-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads((args.recovery_root/'math1/math_remaining_440_manifest_20261023.json').read_text())
    claims, tools, packages = {}, {}, []
    occurrences = {'claim': 0, 'tool': 0}
    for entry in manifest['packages']:
        matches = list(args.recovery_root.glob('math*/original_zips/'+entry['filename']))
        if len(matches) != 1:
            raise ValueError('expected exactly one original: '+entry['filename'])
        raw = matches[0].read_bytes()
        if len(raw) != entry['bytes'] or hashlib.sha256(raw).hexdigest() != entry['sha256']:
            raise ValueError('archive bytes differ from original manifest')
        count_claim, count_tool, documents = 0, 0, []
        with zipfile.ZipFile(matches[0]) as archive:
            for info in archive.infolist():
                name = info.filename
                if info.is_dir() or not name.endswith(('.py', '.cpp', '.cc', '.cxx', '.md', '.txt')):
                    continue
                data = archive.read(info)
                ref = {'package': entry['filename'], 'member': name,
                       'member_sha256': hashlib.sha256(data).hexdigest()}
                if name.endswith(('.md', '.txt')):
                    text = data.decode('utf-8-sig', errors='replace')
                    heading = next((clean(line) for line in text.splitlines() if line.startswith('#')), '')
                    if heading:
                        documents.append({'member': name, 'heading': heading[:240]})
                    for line, excerpt in extract_claims(text):
                        ident = hashlib.sha256(excerpt.encode()).hexdigest()
                        claim = claims.setdefault(ident, {'id': 'CLAIM-'+ident[:16],
                            'status': 'SOURCE_EXCERPT_NOT_REVIEWED', 'excerpt': excerpt, 'occurrences': []})
                        claim['occurrences'].append({**ref, 'line': line})
                        occurrences['claim'] += 1
                        count_claim += 1
                else:
                    ident = ref['member_sha256']
                    tool = tools.setdefault(ident, {'id': 'TOOL-'+ident[:16],
                        'status': 'ARCHIVAL_CANDIDATE_NOT_EXECUTED', **describe_tool(name, data), 'occurrences': []})
                    tool['occurrences'].append(ref)
                    occurrences['tool'] += 1
                    count_tool += 1
        packages.append({'package': entry['filename'], 'sha256': entry['sha256'],
                         'claim_excerpt_occurrences': count_claim, 'tool_occurrences': count_tool,
                         'documents': documents})
    args.output.mkdir(parents=True, exist_ok=True)
    for filename, records in [('theorem_claims.jsonl', claims.values()), ('tools.jsonl', tools.values())]:
        (args.output/filename).write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in records))
    (args.output/'packages.json').write_text(json.dumps(packages, ensure_ascii=False, indent=2)+'\n')
    summary = {'packages': len(packages), 'distinct_claim_excerpts': len(claims),
               'distinct_tool_sources': len(tools), 'occurrences': occurrences,
               'packages_with_claims': sum(p['claim_excerpt_occurrences'] > 0 for p in packages),
               'packages_with_tools': sum(p['tool_occurrences'] > 0 for p in packages),
               'python_parse_failures': sum(t['source_syntax'] == 'PARSE_FAILED' for t in tools.values()),
               'scope': 'Direct members of all original packages; nested ZIPs remain original artifacts. Headings and excerpts are retrieval aids, not a proof count or claim of admission.'}
    (args.output/'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
