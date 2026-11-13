// Usage: compile with g++ -O3 -std=c++17 (unsigned __int128 required); ./extend [node_cap_per_slice] < seeds.txt. UNKNOWN is never an exclusion.
#include <cstdio>
#include <cstring>
#include <cstdint>
#include <algorithm>
#include <array>
#include <vector>
using namespace std; using U=unsigned long long; struct U2{int bad0=0;};
using B=__uint128_t;
int nodeLimit=300000,stable=0;long long nodes=0,total=0;
bool cutoff=false;
int a[125],line[75][5],posL[125][3],atL[125],lcount[75][3],linesD[75];B lb[75],neigh[125][3],clr[3],all=(((B)1<<125)-1);
struct C{B part; unsigned char col;};
vector<B> cons[125];int nodsig[125],pi[125],MP[6][6][6];
struct Log{int p,c;B old[3];}; Log stk[125];int ptr=0,deltaL;
int bit(B x){return (x&((U)-1))?__builtin_ctzll(x):64+__builtin_ctzll(x>>64);}
int ct(B x){return __builtin_popcountll(x)+__builtin_popcountll(x>>64);}
void prep(){int w=0;for(int i=0;i<3;i++)for(int x=0;x<5;x++)for(int y=0;y<5;y++){int k=w++;for(int j=0;j<5;j++){int v=i==0?25*j+5*x+y:(i==1?25*x+5*j+y:25*x+5*y+j);posL[v][atL[v]++]=k;line[k][j]=v;lb[k]|=(B)1<<v;}}
for(int a=0;a<=5;a++)for(int b=0;b<=5-a;b++)for(int c=0;c<=5-a-b;c++){int u=5-a-b-c,best=2;for(int x=0;x<=u;x++)for(int y=0;y<=u-x;y++){int two=(a+x==1)+(b+y==1)+(c+u-x-y==1);best=min(best,2-two);}MP[a][b][c]=best;}
for(int v=0;v<125;v++){for(int j=0;j<3;j++)neigh[v][j]=lb[posL[v][j]]^((B)1<<v);}
}
int rad(B m){for(int i=0;i<8;i++)if(((m>>i)&(m>>(i^1))&(m>>(i^2))&(m>>(i^4)))&1)return 1;return 0;}
void hyper(){for(int i=0;i<5;i++)for(int j=0;j<i;j++)for(int k=0;k<5;k++)for(int l=0;l<k;l++)for(int m=0;m<5;m++)for(int n=0;n<m;n++){
int r[3][2]={{i,j},{k,l},{m,n}};int v[8];for(int b=0;b<8;b++)v[b]=25*r[0][b/4]+5*r[1][b/2%2]+r[2][b%2];
for(int b=1;b<256;b++){int count=__builtin_popcount(b);if(count!=5||rad(b))continue;B mask=0;for(int s=0;s<8;s++)if(b>>s&1)mask|=(B)1<<v[s];for(int s=0;s<8;s++)if(b>>s&1)cons[v[s]].push_back(mask^((B)1<<v[s]));}
}}
inline int minD(int j){auto&r=lcount[j];return MP[r[0]][r[1]][r[2]];}
bool add(int v,int c,B F[3]){Log&s=stk[ptr++];s.p=v;s.c=c;B p=(B)1<<v;a[v]=c;for(int j=0;j<3;j++){s.old[j]=F[j];if(j!=c)F[j]|=p;}
clr[c]|=p;for(auto l:posL[v]){deltaL-=minD(l);lcount[l][c]++;deltaL+=minD(l);}if(deltaL>25){return false;}
B block=F[c],neg=~clr[c];for(B m:cons[v]){B av=m&neg;if(!av)return false;if(!(av&(av-1)))block|=av;}
// A center color with same-color neighbors in 2 directions forbids this color in third direction; with 3 invalid.
B cand=clr[c]&(lb[posL[v][0]]|lb[posL[v][1]]|lb[posL[v][2]]);while(cand){int u=bit(cand);cand&=cand-1;
int cnt=0,none=0;for(int t=0;t<3;t++)if(neigh[u][t]&clr[c])cnt++;else none=t;if(cnt==3)return false;if(cnt==2)block|=neigh[u][none];}
F[c]=block;return !(F[0]&F[1]&F[2]);}
void undo(B F[3],unsigned to){while(ptr>(int)to){auto&s=stk[--ptr];int c=s.c,v=s.p;a[v]=-1;clr[c]^=(B)1<<v;for(auto l:posL[v]){deltaL-=minD(l);lcount[l][c]--;deltaL+=minD(l);}for(int j=0;j<3;j++)F[j]=s.old[j];}}
int score(int v){int tot=0;for(auto l:posL[v])for(auto c:lcount[l])tot+=c;return tot;}
bool dfs(B F[3]){if(++nodes>nodeLimit){cutoff=true;return false;}int base=ptr;B free=all&~(clr[0]|clr[1]|clr[2]);
while(free){B forced=free&((F[0]&F[1])|(F[1]&F[2])|(F[2]&F[0]));if(!forced)break;int v=bit(forced),c=0;while(c<3&&(F[c]>>v&1))c++;if(c==3||!add(v,c,F)){undo(F,base);return false;}free^=(B)1<<v;}
if(!free){for(int v:a)printf("%d",v);printf("\n");fflush(stdout);return true;}B cand=free&(F[0]|F[1]|F[2]);if(!cand)cand=free;
int v=-1,max=-1;while(cand){int j=bit(cand);cand&=cand-1;int sc=score(j);if(sc>max){v=j;max=sc;}}
int k=ptr;for(int c=0;c<3;c++)if(!(F[c]>>v&1)){if(add(v,c,F)&&dfs(F))return true;undo(F,k);if(cutoff)break;}undo(F,base);return false;}
int main(int argc,char**argv){if(argc>1)nodeLimit=atoi(argv[1]);prep();hyper();U z,seed;while(scanf("%llu",&seed)==1){memset(lcount,0,sizeof(lcount));for(auto&c:clr)c=0;fill(a,a+125,-1);B F[3]={};nodes=ptr=deltaL=0;cutoff=false;z=seed;bool ok=true;for(int i=24;i>=0;i--){int c=z%3;z/=3;if((F[c]>>i&1)||!add(i,c,F)){ok=false;break;}}
bool sat=ok&&dfs(F);printf("%llu %s %lld\n",seed,sat?"SAT":cutoff?"UNKNOWN":"UNSAT",nodes);fflush(stdout);if(sat)break;}}
