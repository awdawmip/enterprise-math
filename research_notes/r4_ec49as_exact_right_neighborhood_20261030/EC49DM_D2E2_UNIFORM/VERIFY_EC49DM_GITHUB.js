/* EC49DM: native six-axis ordered signed paths, BRC dual positive products, exact modular certificate.
   Run: node VERIFY_EC49DM_GITHUB.js. Analytic general-h theorem: README_EC49DM.md. */
'use strict';
const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3]};
const SPLIT=[
[-2,1,-2,2,2,2,2,-1],[-2,1,1,-1,2,2,2,-1],[-1,1,1,1,-1,2,2,-1],
[-2,-2,2,1,-1,2,2,2],[-2,-1,2,1,1,-1,2,2],[-1,-1,2,1,1,1,-1,2],
[-2,-2,1,2,2,2,2,-1],[-2,-1,1,1,2,2,2,-1],[-1,-1,1,1,1,2,2,-1],
[-2,-2,-1,2,1,2,2,2],[-2,-1,-1,1,2,1,2,2],[-1,-1,-1,1,1,2,1,2],
[-2,-2,2,2,2,2,-1,1],[-2,-1,2,2,2,-1,1,1],[-1,-1,2,2,-1,1,1,1],
[-2,-2,1,-1,2,2,2,2],[-2,-1,1,1,-1,2,2,2],[-1,-1,1,1,1,-1,2,2]];
const EQUAL_PAIR=[
[-2,1,-2,2,2,2,2,-1],[-3,-2,1,-1,2,2,2,3],[-3,-3,-1,1,3,2,2,3],
[-2,-2,2,1,-1,2,2,2],[-3,-2,-1,2,1,3,2,2],[-3,-3,-1,2,1,3,2,3],
[-2,-2,1,2,2,2,2,-1],[-3,-2,-1,1,2,2,2,3],[-3,-3,-1,1,2,2,3,3],
[-2,-2,-1,2,1,2,2,2],[-3,-2,-1,2,1,2,2,3],[-3,-3,-1,2,1,2,3,3],
[-2,-2,2,2,2,2,-1,1],[-3,-2,-1,2,2,2,3,1],[-3,-3,-1,2,2,3,3,1],
[-2,-2,1,-1,2,2,2,2],[-3,-2,-1,1,3,2,2,2],[-3,-3,-1,1,3,2,3,2]];
const CONSTANT=[[-6,2,2,6],[2,1,-1,2],[1,2,2,-1],[-1,2,1,2],[2,2,-1,1],[-6,2,6,2]];
const SPEC={
even_h2:'bc:2 bc:3 bd:1 cb:2 db:1',
odd_h3:'abe:0 abe:1 abe:2 abe:3 cbc:2 dbd:1',
cumulative_h2:'b:0 b:1 b:2 b:3 cb:2 db:1'};
const EXPECT={
split:[[53525,843759],[451119,205744],[118997,259205]],
equal_pair:[[446329,835875],[797806,613518],[102102,795162]],
constant:[[1,1],[1000002,1000032],[1000002,1000032]]};
function end6(word){let v=[0,0,0,0,0,0];for(const z of word)v[Math.abs(z)-1]+=Math.sign(z);return v;}
function tag(word){let t=0;for(let j=1;j<word.length;j++){if(word[j-1]===1&&word[j]===2)t|=2;if(word[j-1]===2&&word[j]===1)t|=1;}return t;}
function history(word){let t=tag(word),a=[0,0,0,0];a[t]=1;a.push(+( !(t&2) && word[word.length-1]===1),+( !(t&1) && word[word.length-1]===2));return a;}
function weight(word,x,y){let u=1n,v=1n;for(const z of word)if(z>0){u*=BigInt(x[z-1]);v*=BigInt(y[z-1]);}return [u,v,1n];}
function columns(name,constant){let ans=[];for(const sp of SPEC[name].split(' ')){let parts=sp.split(':');for(const ch of (constant?[2]:[0,1,2]))ans.push({s:parts[0],t:Number(parts[1]),ch});}return ans;}
function observation(path,coord,x,y){let word=path.slice();for(const op of coord.s)word.push(...OPS[op]);return tag(word)===coord.t?weight(word,x,y)[coord.ch]:0n;}
function power(a,n,p){let out=1;for(;n>0;n=Math.floor(n/2),a=a*a%p)if(n%2)out=out*a%p;return out;}
function detP(rows,p){let m=rows.map(row=>row.map(q=>Number(q%BigInt(p)))),det=1,sign=1,n=m.length;for(let j=0;j<n;j++){let pivot=j;while(pivot<n&&m[pivot][j]===0)pivot++;if(pivot===n)return 0;if(pivot!==j){[m[pivot],m[j]]=[m[j],m[pivot]];sign*=-1;}let v=m[j][j],inv=power(v,p-2,p);det=det*v%p;for(let k=j+1;k<n;k++){let fac=m[k][j]*inv%p;for(let l=j;l<n;l++)m[k][l]=((m[k][l]-fac*m[j][l])%p+p)%p;}}return det*(sign===1?1:p-1)%p;}
function check(group,paths,x,y){let constant=group==='constant',out={};for(const w of paths)if(w.length!==(constant?4:8)||end6(w).join(',')!=='0,2,0,0,0,0')throw Error('not a D=+2E2 native path');
if(!constant){const basis=['1,0,0,0,0,0','0,1,0,0,0,0','0,0,1,0,0,0','0,0,0,1,0,0','1,0,0,0,1,0','1,0,0,0,0,1'];for(let i=0;i<18;i++)if(history(paths[i]).join(',')!==basis[Math.floor(i/3)])throw Error(group+' invalid history at '+i);}
let names=Object.keys(SPEC);for(let q=0;q<names.length;q++){let name=names[q],cols=columns(name,constant);let idx=name==='even_h2'?(constant?[0,1,2,4,5]:[0,1,2,3,4,5,6,7,8,12,13,14,15,16,17]):paths.map((_,i)=>i);
let mat=idx.map(i=>cols.map(z=>observation(paths[i],z,x,y))),mod=[1000003,1000033].map(p=>detP(mat,p));if(mod.some((r,j)=>r!==EXPECT[group][q][j]))throw Error(group+' '+name+': '+mod.join(','));out[name]={rank_lower:mat.length,mod_1000003:mod[0],mod_1000033:mod[1]};}return out;}
function main(){return {status:'PASS',native_path_count:42,nonzero_modular_minors:9,split:check('split',SPLIT,[2,3,1,2,3,4],[5,7,3,5,7,9]),equal_pair:check('equal_pair',EQUAL_PAIR,[2,2,5,2,2,2],[5,5,11,5,5,5]),constant:check('constant',CONSTANT,[2,2,2,2,2,2],[5,5,5,5,5,5])};}
if(require.main===module)console.log(JSON.stringify(main(),null,2));
module.exports={main};
