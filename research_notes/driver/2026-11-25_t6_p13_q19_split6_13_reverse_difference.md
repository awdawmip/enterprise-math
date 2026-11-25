# T6 p13 q19 split(6,13): full reverse-difference exclusion

2026-11-25, existing Driver lane EM-DVR-DEBB5E, own scientific contribution, NOT_REVIEWED. Retain the valuation-one, cancellation-normalized H0..H6 necessary-residue domain of the [previous q20 proof](https://github.com/awdawmip/enterprise-math/blob/f95a357f39459396d06972facdc1e34cba5dc41b/research_notes/driver/2026-11-25_t6_p13_q20_split10_10_symmetric_injection.md). The other actor r182 is advancing q12, backlog r490 retains DCMP11; no competing owner work identified in those checkpoints. No protected claim or new Result.

Each multiset consists of 13-smooth positive u=13j+r, 1<=r<=12, sum j=Q, sum w=13r-1 <= B=2331-169Q. Separate vertical atoms j>0 and horizontal j=0. Let G be the four residues k=4,5,6,1 with moduli 13^k. Necessity is G(P)+G(H)=G(T). For Q=6, B=1317; Q=13, B=134. The smallest vertical weight for Q6 is 24, hence every admissible H has w<=1293. Index all exact differences G(T)-G(P) over the 9798 Q6 vertical profiles and all 5775 Q13 targets. Enumerate every horizontal profile up to 1293, deliberately relaxing the individual mass constraint. No match even in this superset proves the whole split excluded. The exact 61-bit key uses nonoverlapping fields; bitmap only filters, open addressing stores the complete key plus one, collisions resolved by linear probing. Recursion uses nondecreasing atom indices and visits each multiset once. Independent JS BigInt unbounded coin DP by ascending j,r (separate vertical and horizontal arrays) gives Q6 full 223166422312, Q13 full 5775, P6=9798, P13=1368, H6 at cap1293=220398388; recursive counts agree. No Cartesian pair count is presented as actually enumerated.

Actual local g++ -O3 -std=c++17 -march=native reverse.cpp -o reverse; /usr/bin/time -v ./reverse:
```
band=0/1 P=9798 minP=24 Hcap=1293 target=5775 TESTED=56583450 unique=47292026
H=220398388 FILTER=9495836 HIT_H=0
LEGAL4=0
User 28.36s; system 0.30s; elapsed 28.74s; peak RSS 1181692 KiB; exit status 0.
```
Earlier forward horizontal-key sort attempt timed out after enumerating H=220398388, with no match test completed; no exclusion credit for it. Reverse method completed all queries and H profiles. This yields q19(6,13) only. Independent BigInt DP gives remaining side counts Q7=106764960310, Q8=37377606512, Q9=8963595909, Q10=1328547997, Q11=100750914, Q12=2583672. Next q19(7,12), (8,11), (9,10); adapt reverse lookup or additional residue constraints. No independent review, native Result, Task, parent closure.

Reproduction source (executed):
```cpp
#include <bits/stdc++.h>
using namespace std; using U=uint64_t; using S=array<int,4>; constexpr int M[]={28561,371293,4826809,13};
S add(S a,S b){for(int i=0;i<4;i++) a[i]=(a[i]+b[i])%M[i];return a;}
S sub(S a,S b){for(int i=0;i<4;i++) a[i]=(a[i]-b[i]+M[i])%M[i];return a;}
U key(S a){return U(a[0])|(U(a[1])<<15)|(U(a[2])<<34)|(U(a[3])<<57);}
U hash64(U k){k^=k>>30;k*=0xbf58476d1ce4e5b9ULL;k^=k>>27;k*=0x94d049bb133111ebULL;return k^(k>>31);}
bool smooth(int n){for(int p:{2,3,5,7,11,13})while(n%p==0)n/=p;return n==1;}
int inv(int a,int m){long x=0,y=1;int b=m;while(a){int t=b/a,z=b-t*a;b=a;a=z;long u=x-t*y;x=y;y=u;}assert(b==1);return (x%m+m)%m;}
struct Atom{int j,w;S s;}; struct Row{int w;S s;};
vector<Atom> atoms(int Q){vector<Atom>a;for(int j=0;j<=Q;j++)for(int r=1;r<=12;r++)if(smooth(13*j+r)){Atom t{j,13*r-1,{}};for(int i=0;i<4;i++){long v=inv(13*j+r,M[i]),z=1;for(int n=0;n<(i==3?1:i+4);n++)z=z*v%M[i];t.s[i]=z;}a.push_back(t);}return a;}
void vertical(const vector<Atom>&a,int i,int q,int w,int B,S s,vector<Row>&out){if(!q){out.push_back({w,s});return;}for(int k=i;k<(int)a.size();k++)if(a[k].j&&a[k].j<=q&&w+a[k].w<=B)vertical(a,k,q-a[k].j,w+a[k].w,B,add(s,a[k].s),out);}
template<class F>void horizontal(const vector<Atom>&a,int i,int w,int B,S s,F& f){f(w,s);for(int k=i;k<(int)a.size()&&a[k].j==0;k++)if(w+a[k].w<=B)horizontal(a,k,w+a[k].w,B,add(s,a[k].s),f);}
int main(int argc,char**argv){int band=argc>1?atoi(argv[1]):0,K=argc>2?atoi(argv[2]):1;auto a=atoms(6),b=atoms(13);vector<Row>p,tv,targets;vertical(a,0,6,0,1317,{},p);vertical(b,0,13,0,134,{},tv);for(auto t:tv){auto f=[&](int w,S s){targets.push_back({w+t.w,add(t.s,s)});};horizontal(b,0,0,134-t.w,{},f);}assert(p.size()==9798&&tv.size()==1368&&targets.size()==5775);int mn=INT_MAX;U nP=0;for(int i=band;i<(int)p.size();i+=K){mn=min(mn,p[i].w);nP++;}int cap=1317-mn;int lg=1;while((1ULL<<lg)<2*nP*targets.size())lg++;vector<U> ht(1ULL<<lg);U mask=ht.size()-1;constexpr int bits=30;vector<U> bm(1ULL<<(bits-6));U tested=0,unique=0;for(int i=band;i<(int)p.size();i+=K)for(auto t:targets){U k=key(sub(t.s,p[i].s)),v=k+1,h=hash64(k),j=h&mask,bi=h>>(64-bits);bm[bi>>6]|=1ULL<<(bi&63);while(ht[j]&&ht[j]!=v)j=(j+1)&mask;if(!ht[j]){ht[j]=v;unique++;}tested++;}assert(tested==nP*targets.size());cout<<"band="<<band<<"/"<<K<<" P="<<nP<<" minP="<<mn<<" Hcap="<<cap<<" target="<<targets.size()<<" TESTED="<<tested<<" unique="<<unique<<endl;U n=0,bh=0,hits=0;vector<pair<U,int>>match;auto f=[&](int w,S s){n++;U k=key(s),h=hash64(k),bi=h>>(64-bits);if(!(bm[bi>>6]>>(bi&63)&1))return;bh++;U v=k+1,j=h&mask;while(ht[j]&&ht[j]!=v)j=(j+1)&mask;if(ht[j]==v){hits++;match.emplace_back(k,w);}};horizontal(a,0,0,cap,{},f);cout<<"H="<<n<<" FILTER="<<bh<<" HIT_H="<<hits<<endl;U legal=0;if(hits){unordered_map<U,vector<int>>m;for(auto [k,w]:match)m[k].push_back(w);for(int i=band;i<(int)p.size();i+=K)for(int j=0;j<(int)targets.size();j++){auto it=m.find(key(sub(targets[j].s,p[i].s)));if(it!=m.end())for(int w:it->second)if(w+p[i].w<=1317){legal++;cout<<"LEGAL4 i="<<i<<" j="<<j<<" w="<<w<<endl;}}}cout<<"LEGAL4="<<legal<<endl;return legal?2:0;}
```
