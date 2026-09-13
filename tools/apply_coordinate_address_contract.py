#!/usr/bin/env python3
"""Idempotent, allowlisted adoption of the public nonnegative address contract.

Existing raw-coordinate mathematics, P000 axioms, historical proofs, and scalar
APIs are preserved. --apply modifies only the listed current routing surfaces;
--check enforces their common contract and records no new mathematical truth.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = 'coordinate_address_contract.json'
MANIFEST = 'coordinate_contract_migration_manifest.json'
MARK = '<!-- EM_FINAL_CELL_ADDRESS_CONTRACT_V1 -->'
PROOF_HASH = '2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02'
JSON_PATHS = [
    'p000_reality_foundation.json', 'project_definition.json',
    'packet_path_foundation.json', 'native_semantics_admissibility.json',
    'relational_axis_convention.json', 'three_dimensional_relational_axis_convention.json',
    'definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.json',
    'definitions/enterprise_coordinate_system_and_brc_bridge.json',
    'research_common_surface.json',
]
MD_PATHS = [
    'PROJECT_DEFINITION.md', 'PROJECT_DEFINITION.zh-CN.md',
    'README.md', 'README.zh-CN.md', 'GEOMETRIC_TOOL_REFOUNDATION_POLICY.md',
    'PACKET_PATH_FOUNDATION.md', 'RELATIONAL_AXIS_CONVENTION.md',
    'THREE_DIMENSIONAL_RELATIONAL_AXIS_CONVENTION.md',
    'definitions/00_CURRENT_NATIVE_FOUNDATION.md',
    'definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md',
    'definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md',
    'definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md',
    'definitions/P000_SIX_AXIS_PAIRWISE_ORTHOGONALITY_20260905.md',
    'definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md',
    'definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md',
]
IMPORT_PATHS = ['src/enterprise_math/__init__.py','EnterpriseMath.lean']
EDIT_PATHS = JSON_PATHS + MD_PATHS + IMPORT_PATHS
ADD_PATHS = [CONTRACT, 'schemas/cell_address.schema.json',
    'COORDINATE_ADDRESS_CONVENTION.md', 'COORDINATE_ADDRESS_CONVENTION.zh-CN.md',
    'src/enterprise_math/_cell_slice_codec.py', 'src/enterprise_math/cell_address.py',
    'tools/validate_cell_address.py', 'tools/apply_coordinate_address_contract.py',
    'tests/test_cell_address_contract.py',
    'EnterpriseMath/CellAddress/ThreeRegionSlice.lean',
    'EnterpriseMath/CellAddress/Contract.lean']


def read(path: str) -> str:
    return (ROOT/path).read_text(encoding='utf-8')


def digest(data: bytes | str) -> str:
    return hashlib.sha256(data.encode() if isinstance(data,str) else data).hexdigest()


def objhash(value: object) -> str:
    return digest(json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False))


def link(path: str) -> str:
    return '../'*len(Path(path).parts[:-1]) + CONTRACT


def replace_section(text: str, start: str, end: str, replacement: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError('Current source section changed; explicit rebase needed: '+start)
    a,b = text.index(start),text.index(end)
    if a >= b:
        raise ValueError('Section order changed')
    return text[:a] + replacement.rstrip() + '\n\n' + text[b:]


def banner(path: str) -> str:
    route = link(path)
    if path.endswith('.zh-CN.md'):
        content = f'''## 晶包坐标接口约束（2026-09-13）

所有最终晶包地址遵循 [`{CONTRACT}`]({route})：六字段非负；未启用字段只在可恢复完整身份时置0；显示原点与轴线不参与晶包运算；跨区不强制加1。内部原始坐标、位移、反向操作与零位移分别保留，不能直接当作最终地址输出。已验证三分区实现仅覆盖固定两原生方向切片，不适用于任意完整六轴状态。旧文中的坐标零点为内部锚点，不是显示原点放置要求。'''
    else:
        content = f'''## Final Cell address interface (2026-09-13)

All final Cell addresses obey [`{CONTRACT}`]({route}): six nonnegative integer fields; inactive zero only without identity loss; display origin/axes are nonoperational; crossing does not force +1. Existing signed raw charts, displacements, inverse actions and their zero remain separately typed internal mathematics, not final address output. The verified three-region codec covers only a fixed two-generator slice, not arbitrary full X6. Existing coordinate-zero statements below concern RAW_CHART_ZERO, not display-origin placement.'''
    if path.endswith('00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md'):
        content = f'''## Public address typing only (2026-09-13)

Before exporting a final Cell address, apply [`{CONTRACT}`]({route}): six nonnegative fields; inactive fields may be zero only losslessly; no operational display origin and no automatic boundary increment. This is an interface constraint, not a new discovery prior or an instruction to load theorem/result catalogs. Preserve this router's information firewall and all original P000 premises. Raw signed proof coordinates remain separate from final public addresses.'''
    return MARK+'\n'+content+'\n<!-- END_EM_FINAL_CELL_ADDRESS_CONTRACT_V1 -->\n'


EN_CORE = '''## 1. Current spatial and display types

The exact native X6 spatial model is routed through
`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` and P000.
Six native spatial axis labels and existing forward/reverse operations are unchanged.
Raw signed charts are internal mathematical carriers. Their zero labels a chosen
Cell anchor; it does not prescribe a physical global center or the display origin.
A display origin may lie in a gap and display axes need not pass through Cell
centers. Neither is a Cell, path vertex or operational source.

## 2. Current coordinates and length

The mandatory final address contract is `coordinate_address_contract.json`.
Final Cell addresses have six nonnegative integer fields, a registered codec,
version and explicit fixed frame. Inactive zero is allowed only losslessly.
Unknown or omitted spatial information is not zero. Public digits are addresses,
not automatically raw components whose difference defines distance.

The registered `three_region_slice_v1` covers a fixed two-generator slice only.
Its forms are `(0,b,c,0,0,0)`, `(a,0,c,0,0,0)`, `(a,b,0,0,0,0)`, with
positive active values. No complete full-X6 codec is asserted. Other inputs must
be rejected or await a verified registered codec, never silently projected.

## 3. Current line and point-to-point structure

Preserve the native signed displacement metric and primitive adjacency. Evaluate
metrics on decoded Cells, not raw address digits. Crossing a display boundary
neither adds a vertex nor imposes +1; the verified boundary table includes both
equal-value transfer and adjusted-value cases. Preserve actual edge identity,
ordered paths, BRC multiplicity, ports, weights, boundaries and initial conditions.
Path-letter count and native component length remain different quantities.
The current signed metric is reversal symmetric; historical directed min-zero
gauges are lower-information observer readouts, not a replacement native metric.
'''
ZH_CORE = '''## 1. 当前空间与显示参照

原生六轴晶包结构以 `p000_reality_foundation.json` 和
`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` 为准。
六条原生轴及既有正向、反向操作保持不变。原始有符号坐标属于内部数学表示；
其零坐标标记一个选定晶包锚点，不规定物理全局中心或显示原点。
显示原点可以位于空隙，显示轴线不必经过晶包中心；二者不是晶包、路径节点或运算起点。

## 2. 当前坐标与长度

所有最终晶包地址统一遵循 `coordinate_address_contract.json`：六个非负整数字段，
明确编码版本及固定参照系。不参与表达的字段只有在完整身份不丢失时才可置0；
未知、隐藏或省略的信息不等于0。地址数字不能未经解码直接当作位移或距离。

已登记实现 `three_region_slice_v1` 仅覆盖固定两原生方向切片，形式为
`(0,b,c,0,0,0)`、`(a,0,c,0,0,0)`、`(a,b,0,0,0,0)`，启用字段为正整数。
这不是完整六轴通用编码。其他输入必须使用另行验证登记的编码；不支持时明确拒绝，
不得偷偷清零其他分量后套用切片。

## 3. 当前线与点到点结构

原生有符号位移、距离、邻接规则保留。距离基于解码后的晶包，不基于地址数字的差。
跨显示分界不增加节点，也不强制加1；当前已证明的边界表同时包含等值换栏和调整字段。
实际边身份、路径先后、BRC 重复度、端口、权重、边界及初态均需保留。
步数与原生分量长度仍须区别。当前原生有符号距离具有反向对称性；历史有向 min-zero
数值仅是信息较少的观察读数，不再作为当前原生点到点距离。
'''


def patch_md(path: str, text: str) -> str:
    if MARK in text:
        return text
    if path == 'PROJECT_DEFINITION.md':
        text = replace_section(text,'## 1. Current Enterprise plane','## 4. BRC',EN_CORE)
        text = text.replace('THREE-POSITIVE-AXIS ENTERPRISE COORDINATES','NONNEGATIVE CELL ADDRESSES OVER TYPED NATIVE RELATIONS')
    elif path == 'PROJECT_DEFINITION.zh-CN.md':
        text = replace_section(text,'## 1. 当前进取平面','## 4. BRC',ZH_CORE)
        text = text.replace('THREE-POSITIVE-AXIS ENTERPRISE COORDINATES','NONNEGATIVE CELL ADDRESSES OVER TYPED NATIVE RELATIONS')
    elif path == 'GEOMETRIC_TOOL_REFOUNDATION_POLICY.md':
        text = replace_section(text,'## Current native-plane authority','## Geometry layers','''## Current native-plane authority

Use `definitions/00_CURRENT_NATIVE_FOUNDATION.md` and the exact X6/slice
definitions for native spatial mathematics. Use `coordinate_address_contract.json`
for final address and display-origin semantics. Native six-axis identity, signed
internal displacements and reverse operations are not twelve address fields.
The final address fields are nonnegative. A plotting origin is nonoperational;
old raw coordinate-zero Cells are retained. Circle footprints and their triple
incidences are classical carrier readouts, not a compulsory native origin.
The verified three-region codec is scoped to a fixed two-generator slice.
''')
        text = replace_section(text,'## Current line/distance boundary','## BRC boundary','''## Current line/distance boundary

Preserve the current signed component metric and path rules from the exact X6
and centered-slice definitions. Do not equate path-step count with component
length. Directed min-zero gauges and bidirectional spectra survive at their
historical observer scopes, not as current native metric restrictions. Final
address digits require a registered decoder; ordinary digit differences are not
a native distance formula. Boundary crossing does not force a numeric increment.
''')
        text = replace_section(text,'## Worldview boundary','## Stage-specific premise rule','''## Worldview boundary

The protected account worldview remains a separate directly user-controlled
source. This address-only migration does not edit it or promote a carrier
visualization into ontology. P000's current axioms and native dimension remain
unchanged. Older spatial summaries cannot override current exact X6 definitions
or the current final-address interface contract.
''')
    lines = text.splitlines(keepends=True)
    return lines[0]+'\n'+banner(path)+'\n'+''.join(lines[1:])


def patch_json(path: str, data: dict) -> dict:
    if data.get('coordinate_address_contract') == CONTRACT:
        return data
    d = copy.deepcopy(data)
    d['coordinate_address_contract'] = CONTRACT
    d['coordinate_address_scope'] = {
        'final_address': 'SIX_NONNEGATIVE_FIELDS_WITH_REGISTERED_LOSSLESS_CODEC',
        'raw_coordinate_and_displacement': 'EXISTING_SIGNED_INTERNAL_MATHEMATICS_UNCHANGED',
        'legacy_coordinate_zero_keys': 'RAW_CHART_ZERO_NOT_DISPLAY_ORIGIN',
        'display_origin_and_axes_operational': False,
        'crossing_forces_increment': False,
        'proof_scope': 'REGISTERED_FIXED_TWO_GENERATOR_SLICE_NOT_FULL_X6',
    }
    if path == 'p000_reality_foundation.json':
        original_axioms = copy.deepcopy(d['axioms'])
        d.setdefault('mandatory_companion_contracts', []).append({
            'contract_id':'FINAL_CELL_ADDRESS_CONSTRAINT', 'path':CONTRACT,
            'authority_kind':'DIRECT_USER_INTERFACE_CONSTRAINT',
            'scope':'ALL_FINAL_CELL_ADDRESS_OUTPUT_AND_INPUT',
            'load_policy':'BEFORE_INTERPRETING_OR_SERIALIZING_FINAL_CELL_ADDRESSES',
        })
        d['typed_semantics']['native_coordinate_origin']['scope'] = 'INTERNAL_RAW_CHART_ONLY_NOT_FINAL_DISPLAY_ORIGIN'
        d['typed_semantics']['final_cell_address'] = {'contract':CONTRACT,'negative_fields_allowed':False,'display_origin_is_cell':False,'native_zero_cell_preserved':True}
        d['machine_invariants'] += [
            'FINAL_CELL_ADDRESS_FIELD_DOMAIN=NONNEGATIVE_INTEGER',
            'FINAL_CELL_ADDRESS_FIELD_COUNT=6',
            'FINAL_CELL_ADDRESS!=RAW_SPATIAL_CHART',
            'DISPLAY_REFERENCE!=NATIVE_CELL',
            'DISPLAY_AXIS_OR_ORIGIN_AS_OPERATIONAL_NODE=FORBIDDEN',
            'ADDRESS_BOUNDARY_CROSSING_FORCED_INCREMENT=false',
            'INACTIVE_ZERO_REQUIRES_LOSSLESS_CODEC=true',
            'UNREGISTERED_FULL_X6_ADDRESS_CODEC=REJECT',
        ]
        assert d['axioms'] == original_axioms
    elif path == 'project_definition.json':
        d['current_native_plane'] = {
            'foundation':'definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md',
            'native_axis_count':6,'slice_model':'EXPLICIT_SELECTED_NATIVE_SUBSPACE',
            'raw_spatial_chart':'Z^6','raw_zero':'CHOSEN_CELL_ANCHOR',
            'display_origin_type':'NONOPERATIONAL_REFERENCE_MAY_LIE_IN_GAP',
            'carrier_circle_footprint_is_native_cell_identity':False,
        }
        d['current_coordinate_atlas'] = {
            'contract':CONTRACT, 'final_field_domain':'N_0^6_VALID_CODEC_IMAGE',
            'registered_codec':'three_region_slice_v1',
            'registered_scope':'FIXED_TWO_NATIVE_GENERATOR_SLICE',
            'full_x6_codec_registered':False,'crossing_forces_increment':False,
            'raw_signed_chart_is_final_address':False,
        }
        d['current_line_and_distance'] = {
            'foundation':'definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md',
            'native_metric':'SUM_OF_SIGNED_DISPLACEMENT_COMPONENT_SQUARES',
            'symmetric':True,'address_digits_are_metric_components':False,
            'path_and_component_length_distinct':True,
        }
        d['worldview_alignment'] = {
            'protected_source':'我眼中的世界.md',
            'modification_by_address_migration':False,
            'project_spatial_authority':'p000_reality_foundation.json',
        }
        d['canonical_stack'] = d['canonical_stack'].replace('THREE_POSITIVE_AXIS_ENTERPRISE_COORDINATES','NONNEGATIVE_CELL_ADDRESSES_OVER_NATIVE_RELATIONS')
    elif path.endswith('CENTERED_THREE_AXIS_SLICE_REBASE_20260905.json'):
        d['semantic_authority']['coordinate_zero_scope'] = 'RAW_INTERNAL_CHART'
        d['slice']['coordinate_carrier_scope'] = 'RAW_INTERNAL_CHART_NOT_PUBLIC_ADDRESS'
        d['machine_invariants'] += ['FINAL_ADDRESS_RULES=coordinate_address_contract.json',
            'RAW_SLICE_ZERO_CELL!=DISPLAY_REFERENCE',
            'FINAL_ADDRESS_NEGATIVE_FIELDS=FORBIDDEN']
    elif path.endswith('enterprise_coordinate_system_and_brc_bridge.json'):
        d['current_native_route'] = {
            'foundation':'definitions/00_CURRENT_NATIVE_FOUNDATION.md',
            'final_address_contract':CONTRACT,
            'historical_sections_are_current_authority':False,
        }
    return d


def patch_import(path: str, text: str) -> str:
    if path.endswith('.lean'):
        line='import EnterpriseMath.CellAddress.Contract'
        return text if line in text.splitlines() else line+'\n'+text
    marker='# Public nonnegative Cell address interface (2026-09-13).'
    if marker in text:
        return text
    return text.rstrip()+'''\n\n# Public nonnegative Cell address interface (2026-09-13).
from .cell_address import (
    FinalCellAddress,
    encode_raw_slice,
    decode_raw_slice,
    step_cell,
    cell_step_distance,
    cell_squared_distance,
    validate_cell_address,
)
__all__ += [
    "FinalCellAddress", "encode_raw_slice", "decode_raw_slice", "step_cell",
    "cell_step_distance", "cell_squared_distance", "validate_cell_address",
]
'''


def apply() -> None:
    prior = json.loads(read(MANIFEST)) if (ROOT/MANIFEST).exists() else None
    entries = {e['path']:e for e in prior['updated_surfaces']} if prior else {}
    axioms_before = objhash(json.loads(read('p000_reality_foundation.json'))['axioms'])
    for path in EDIT_PATHS:
        if not (ROOT/path).is_file():
            raise ValueError('Required authority surface missing: '+path)
        text=read(path)
        if path in JSON_PATHS:
            data=json.loads(text); changed=patch_json(path,data)
            new = text if changed == data else json.dumps(changed,ensure_ascii=False,indent=2)+'\n'
        elif path in MD_PATHS:
            new=patch_md(path,text)
        else:
            new=patch_import(path,text)
        if path not in entries:
            entries[path]={'path':path,'before_sha256':digest(text),'after_sha256':digest(new)}
        elif new != text:
            raise ValueError('Already migrated surface changed: manual rebase required '+path)
        if new != text:
            (ROOT/path).write_text(new,encoding='utf-8')
    axioms_after = objhash(json.loads(read('p000_reality_foundation.json'))['axioms'])
    if axioms_before != axioms_after:
        raise AssertionError('P000_AXIOMS_MUST_NOT_CHANGE')
    manifest = prior or {
        'schema':'ENTERPRISE_COORDINATE_CONTRACT_MIGRATION_V1',
        'source_main':'366a7517c3baf91ade267c972833fe722902519c',
        'semantic_scope':'FINAL_ADDRESS_CONSTRAINT_AND_TYPED_ROUTING_NOT_ONTOLOGY',
        'p000_axioms_sha256':axioms_before,
        'updated_surfaces':[],
        'new_surfaces':ADD_PATHS,
        'preserved':['HISTORICAL_THEOREMS_AND_RESEARCH_RECORDS','PROTECTED_WORLDVIEW',
            'P000_AXIOMS','EXISTING_NATIVE_SIGNED_OPERATIONS','SCALAR_ARITHMETIC_APIS'],
        'excluded_false_positive':['docs/ORIGIN.en.md','docs/ORIGIN.zh-CN.md'],
        'not_claimed':['FULL_X6_CODEC','ALL_APPLICATION_CALLER_MIGRATION','FULL_REPOSITORY_BUILD','NEW_FOUNDATION_THEOREM_ADMISSION'],
    }
    manifest['updated_surfaces']=[entries[p] for p in EDIT_PATHS]
    (ROOT/MANIFEST).write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    check(verify_manifest=True)


def check(verify_manifest: bool = False) -> None:
    for path in ADD_PATHS+[MANIFEST]+EDIT_PATHS:
        if not (ROOT/path).is_file():raise ValueError('Missing mandatory migration file: '+path)
    c=json.loads(read(CONTRACT))
    assert c['types']['FINAL_CELL_ADDRESS']['field_count']==6
    assert c['types']['FINAL_CELL_ADDRESS']['negative_fields_allowed'] is False
    assert c['crossing']['forced_increment'] is False
    assert c['crossing']['equal_value_transfer_allowed'] is True
    assert c['full_x6_codec']['fallback_to_slice'] is False
    assert list(c['registered_codecs'])==['three_region_slice_v1']
    for path in JSON_PATHS:
        obj=json.loads(read(path))
        assert obj['coordinate_address_contract']==CONTRACT,path
        assert patch_json(path,obj)==obj,path
    for path in MD_PATHS:
        text=read(path)
        assert text.count(MARK)==1,path
        assert patch_md(path,text)==text,path
    for path in IMPORT_PATHS:
        assert patch_import(path,read(path))==read(path),path
    for path in ['PROJECT_DEFINITION.md','PROJECT_DEFINITION.zh-CN.md','GEOMETRIC_TOOL_REFOUNDATION_POLICY.md']:
        text=read(path)
        assert 'O_E=0' not in text,path
        assert 'DIRECTED_NATIVE_LINE_GAUGE' not in text,path
    proof='EnterpriseMath/CellAddress/ThreeRegionSlice.lean'
    assert digest((ROOT/proof).read_bytes())==PROOF_HASH
    for path in [proof,'EnterpriseMath/CellAddress/Contract.lean']:
        assert not re.search(r'\b(sorry|admit|axiom|native_decide)\b',read(path)),path
    manifest=json.loads(read(MANIFEST))
    assert objhash(json.loads(read('p000_reality_foundation.json'))['axioms'])==manifest['p000_axioms_sha256']
    if verify_manifest:
        for item in manifest['updated_surfaces']:
            assert digest(read(item['path']))==item['after_sha256'],item['path']
    print(json.dumps({'status':'COORDINATE_CONTRACT_CHECK_PASSED',
        'updated_current_surfaces':len(EDIT_PATHS),'new_surfaces':len(ADD_PATHS),
        'p000_axioms_unchanged':True,'full_x6_codec_claimed':False},ensure_ascii=False))


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--apply',action='store_true')
    group.add_argument('--check',action='store_true')
    group.add_argument('--publish-paths',action='store_true')
    args=ap.parse_args()
    if args.apply: apply()
    elif args.check: check()
    else: print('\n'.join(EDIT_PATHS+[MANIFEST]))

if __name__=='__main__':main()
