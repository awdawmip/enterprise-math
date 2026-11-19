"""Run pinned stock and instrumented OpenFOAM v1912 pressure solves. See pressure.md."""
import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import statistics
import subprocess
import tempfile
from time import perf_counter_ns

HERE=Path(__file__).resolve().parent
SOURCE_HASH='3e750df925c1f905178d2fe50e12c8bd105274f805e050bf48b1381d47c51cd0'
PROGRAM_PINS={
    'openfoam/usr/bin/blockMesh':'2a92e36ccfbfee209acc2f4dc61fe7c2690597c4bc7be1b63c6223a17fe53702',
    'openfoam/usr/bin/potentialFoam':'4dbc855fdca4988cbb7d00f1515eb53f2f52108e21bca7e4c7efaaf6ba170eb5',
    'libopenfoam/usr/lib/libfiniteVolume.so':'5f806491488e220f08162c0597257822064de8309d5120b04f1260b937b3a196',
    'libopenfoam/usr/lib/libOpenFOAM.so':'be8b5a0399ef105d0f47fc16d97e3a0668f2b26806d72ded023b31bce3c53ca0'}
METHODS=['GAMG','Schur','Thomas','port_cache']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compile_bench(src,lib,tmp,cxx):
    solver=src/'applications/solvers/basic/potentialFoam'
    source=solver/'potentialFoam.C'
    assert sha(source)==SOURCE_HASH
    text=source.read_text()
    site='            pEqn.solve();'
    assert text.count(site)==1 and text.count('int main(int argc')==1
    patched=text.replace('int main(int argc','#include <memory>\n#include "pressure_bench.H"\nint main(int argc')
    patched=patched.replace(site,'            pressureStudy::bench(pEqn,p);\n'+site)
    (tmp/'bench.C').write_text(patched)
    include=[]
    for name in ['finiteVolume','meshTools','sampling','OpenFOAM','OSspecific/POSIX']:
        target=tmp/name.replace('/','_');target.mkdir()
        for p in sorted((src/'src'/name).rglob('*')):
            if p.is_file() and p.suffix in ('.C','.H','.c','.h','.I','.T') and 'lnInclude' not in p.parts:
                out=target/p.name
                if not out.exists():out.symlink_to(p)
        include+=['-I'+str(target)]
    exe=tmp/'pressure-comparison'
    args=[cxx,'-std=c++11','-DWM_DP','-DWM_LABEL_SIZE=32','-DNoRepository','-DOPENFOAM=1912',
          '-O2','-Wno-deprecated-declarations','-I'+str(HERE),'-I'+str(solver),*include,
          str(tmp/'bench.C'),'-L'+str(lib),'-Wl,-rpath-link,'+str(lib),
          '-lfiniteVolume','-lmeshTools','-lsampling','-lOpenFOAM','-lPstream','-ldl','-o',str(exe)]
    subprocess.run(args,check=True)
    return exe


def write_case(root,n,left=1,right=0,neumann=False,driven=False):
    def put(rel,kind,body):
        path=root/rel
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text('FoamFile {version 2.0; format ascii; class '+kind+'; object '+path.name+';}\n'+body+'\n')
    put('system/blockMeshDict','dictionary','''scale 1;
vertices ((0 0 0)(1 0 0)(1 1 0)(0 1 0)(0 0 1)(1 0 1)(1 1 1)(0 1 1));
blocks (hex (0 1 2 3 4 5 6 7) ('''+str(n)+''' 1 1) simpleGrading (1 1 1)); edges ();
boundary (left {type patch; faces ((0 4 7 3));} right {type patch; faces ((1 2 6 5));}
 sides {type wall; faces ((0 1 5 4)(3 7 6 2)(0 3 2 1)(4 5 6 7));}); mergePatchPairs ();''')
    put('system/controlDict','dictionary','''application potentialFoam; startFrom startTime; startTime 0;
stopAt endTime; endTime 1; deltaT 1; writeControl timeStep; writeInterval 1; writeFormat ascii;
writePrecision 16; writeCompression off; timeFormat general; timePrecision 6; runTimeModifiable false;''')
    put('system/fvSchemes','dictionary','''ddtSchemes {default steadyState;} gradSchemes {default Gauss linear;}
divSchemes {default Gauss linear;} laplacianSchemes {default Gauss linear corrected;}
interpolationSchemes {default linear;} snGradSchemes {default corrected;}''')
    put('system/fvSolution','dictionary','''solvers {"(p|Phi)" {solver GAMG; tolerance 1e-12; relTol 0;
smoother GaussSeidel; nCellsInCoarsestLevel 3; agglomerator faceAreaPair; cacheAgglomeration false;}}
potentialFlow {nNonOrthogonalCorrectors 0; pRefCell 0; pRefValue 2;}''')
    (root/'constant').mkdir(exist_ok=True)
    def field(name,kind,dim,internal,ends):
        put('0/'+name,kind,'dimensions ['+dim+']; internalField uniform '+internal+
            '; boundaryField {'+ends+' sides {type zeroGradient;}}')
    def bounds(l,r):
        return 'left {type fixedValue; value uniform '+str(l)+';} right {type fixedValue; value uniform '+str(r)+';}'
    gradients='left {type zeroGradient;} right {type zeroGradient;}'
    field('p','volScalarField','0 2 -2 0 0 0 0','0',gradients if neumann else bounds(left,right))
    field('Phi','volScalarField','0 2 -1 0 0 0 0','0',bounds(0,1))
    velocity='left {type fixedValue; value uniform (2 0 0);} right {type zeroGradient;}' if driven else gradients
    field('U','volVectorField','0 1 -1 0 0 0 0','(0 0 0)',velocity)


def execute(args,env):
    start=perf_counter_ns()
    p=subprocess.run(list(map(str,args)),env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    elapsed=perf_counter_ns()-start
    if p.returncode: raise RuntimeError(p.stdout[-3500:])
    return p.stdout,elapsed


def field_values(path,n):
    txt=path.read_text()
    values=re.search(r'internalField\s+nonuniform List<scalar>\s+(\d+)\s*\(([^)]*)\)',txt)
    if values:
        assert int(values[1])==n
        return list(map(float,values[2].split()))
    val=re.search(r'internalField\s+uniform\s+([0-9eE.+-]+);',txt)
    return [float(val[1])]*n


def stock_row(root,n,l,r,apps,env,neumann=False,driven=False,body=None):
    write_case(root,n,l,r,neumann,driven)
    _,mesh_time=execute([apps/'blockMesh','-case',root],env)
    log,total=execute([apps/'potentialFoam','-writep','-case',root],env)
    it=re.search(r'GAMG:  Solving for p, Initial residual = ([^,]+), Final residual = ([^,]+), No Iterations (\d+)',log)
    assert it and float(it[2])<=1e-12
    v=field_values(root/'0/p',n)
    ans=[2 if neumann else l+(r-l)*(i+.5)/n for i in range(n)]
    if body:
        for i in range(n):
            xi=(i+.5)/n
            ans[i]+=sum(min(xi,(j+.5)/n)*(1-max(xi,(j+.5)/n))*f for j,f in enumerate(body))
    err=max(abs(a-b) for a,b in zip(v,ans))
    assert err<5e-7
    return v,dict(iterations=int(it[3]),initial_residual=float(it[1]),final_residual=float(it[2]),
                  max_field_error=err,mesh_ns=mesh_time,process_ns=total)


def instrument(case,n,b,exe,apps,env,driven=False):
    write_case(case,n,driven=driven)
    _,mesh_ns=execute([apps/'blockMesh','-case',case],env)
    receipt=case/'bench.txt'
    log,process_ns=execute([exe,'-writep','-case',case],dict(env,EM_PRESSURE_BLOCK=str(b),
                                        EM_PRESSURE_RECEIPT=str(receipt)))
    levels=[]; runs=defaultdict(list); geometry=None
    for line in receipt.read_text().splitlines():
        tag,*parts=line.split()
        if tag=='SOURCE':
            body=list(map(float,parts));assert len(body)==n
        elif tag=='GEOMETRY':
            geometry=list(map(float,parts));assert geometry[:4]==[n,b,2*n,2*n]
        elif tag=='LEVELS':
            levels=[list(map(int,s.split(':'))) for s in parts]
        elif tag=='RUN':
            trial,method,setup,solves=map(int,parts[:4])
            resid,err,flux=map(float,parts[4:7])
            imin,imax,isum=map(int,parts[7:10])
            native=float(parts[10])
            assert resid<1e-5 and err<1e-6 and flux<1e-4 and native<=1e-12
            runs[METHODS[method]].append(dict(trial=trial,setup_ns=setup,all_24_solve_ns=solves,
                max_integrated_residual=resid,max_field_error=err,max_flux_error=flux,
                min_iterations=imin,max_iterations=imax,total_iterations=isum,max_normalised_residual=native))
    assert geometry and levels and len(runs)==4 and all(len(rows)==5 for rows in runs.values())
    deterministic={}
    for name,rows in runs.items():
        item=lambda x:[x['min_iterations'],x['max_iterations'],x['total_iterations']]
        assert all(item(x)==item(rows[0]) for x in rows)
        deterministic[name]=item(rows[0])
    stable=dict(cells=n,block_length=b,ports=n//b,coarse_cells_and_internal_faces=levels,
                velocity_boundary='left-fixed-2' if driven else 'both-zero-gradient',fine_packed_symmetric_scalars=2*n-1,coarse_packed_symmetric_scalars=sum(c+f for c,f in levels),
                Schur_retained_factor_bytes=n*int(geometry[-1]),Thomas_retained_factor_bytes=8*(2*n-1),
                cache_retained_vector_bytes=24*n,native_iterations_per_batch=deterministic['GAMG'],
                trials=5,rhs_per_trial=24,all_original_operator_and_flux_checks=True)
    raw=dict(cells=n,block_length=b,velocity_boundary=stable["velocity_boundary"],body_source_linf=geometry[4],runs=runs,mesh_ns=mesh_ns,
             instrumented_process_ns=process_ns)
    return stable,raw,field_values(case/'0/p',n),body


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--foam-root',type=Path,required=True,help='parent of unpacked openfoam/ and libopenfoam/')
    p.add_argument('--source',type=Path,required=True,help='unpacked OpenFOAM-v1912.200626 source')
    p.add_argument('--timings',type=Path,help='save hardware-dependent times, residuals and field errors')
    p.add_argument('--cxx',default='g++')
    args=p.parse_args()
    base=args.foam_root.resolve()
    for f,h in PROGRAM_PINS.items():
        assert sha(base/f)==h,f
    apps=base/'openfoam/usr/bin'
    lib=base/'libopenfoam/usr/lib'
    env=dict(os.environ,LD_LIBRARY_PATH=str(lib)+':'+str(lib/'dummy')+':'+os.environ.get('LD_LIBRARY_PATH',''),
             WM_PROJECT_DIR=str(base/'openfoam/usr/share/openfoam'))
    summary=[];raw_cases=[];stock=[];counts={}
    with tempfile.TemporaryDirectory(prefix='pressure-native-') as tmp:
        tmp=Path(tmp)
        exe=compile_bench(args.source.resolve(),lib,tmp,args.cxx)
        for n in (32,128,512):
            initial=None
            for j,(l,r) in enumerate(((1,0),(0,1),(3,-1))):
                vals,row=stock_row(tmp/f'stock{n}-{j}',n,l,r,apps,env)
                stock.append(dict(cells=n,left=l,right=r,**row))
                counts[f'{n}:{l}:{r}']=row['iterations']
                if j==0: initial=vals
            for b in (8,16):
                s,raw,v,_=instrument(tmp/f'case{n}-{b}',n,b,exe,apps,env)
                assert max(abs(x-y) for x,y in zip(initial,v))<1e-11
                summary.append(s);raw_cases.append(raw)
        s,raw,driven_p,body=instrument(tmp/'driven',32,8,exe,apps,env,driven=True)
        assert max(map(abs,body))>0.1
        raw['actual_integrated_body_source']=body
        for j,(l,r) in enumerate(((1,0),(0,1),(3,-1))):
            v,row=stock_row(tmp/f'driven-stock{j}',32,l,r,apps,env,driven=True,body=body)
            stock.append(dict(cells=32,left=l,right=r,velocity_boundary='left-fixed-2',**row))
            counts[f'driven32:{l}:{r}']=row['iterations']
            if j==0: assert max(abs(x-y) for x,y in zip(v,driven_p))<1e-11
        summary.append(s);raw_cases.append(raw)
        _,nr=stock_row(tmp/'neumann',32,0,0,apps,env,neumann=True)
    if args.timings:
        cpu=next((s.split(':',1)[1].strip() for s in Path('/proc/cpuinfo').read_text().splitlines()
                  if s.startswith('model name')),'unspecified')
        measured=dict(cpu=cpu,system=platform.system()+' '+platform.machine(),compiler=subprocess.check_output(
            [args.cxx,'--version'],text=True).splitlines()[0],stock=stock,neumann_reference=nr,cases=raw_cases)
        args.timings.write_text(json.dumps(measured,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(potential_source_sha256=SOURCE_HASH,pinned_binaries=PROGRAM_PINS,
            cases=summary,stock_iterations=counts,neumann_32_reference_value=2,
            neumann_iterations=nr['iterations']),indent=2,sort_keys=True))


if __name__=='__main__':
    main()
