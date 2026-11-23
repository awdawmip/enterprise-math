#include <array>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;
using X=array<int,7>;using A=array<int,4>;
const int q=5,u=2;
int bit(int p,int i){return i?((p>>(i-1))&1):0;}
int last(int p,int i){for(int d=1;d<=4;++d){int e=(i-d+4)%4;if(bit(p,e)!=bit(p,(e+1)%4))return e;}return -1;}
struct Cut{int m0,m1,cost;};vector<Cut> cuts[4][4];
void init(){for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(j!=i&&j!=(i+1)%4){for(int U=0;U<256;U++){int a=0,b=0;for(int p=1;p<=7;p++){int E=(1<<last(p,i))|(1<<(4+last(p,j)));if(bit(p,i)!=bit(p,j)&&(U&E)==E)a|=1<<(p-1);if(bit(p,(i+1)%4)!=bit(p,j)&&(U&(1<<(4+last(p,j)))))b|=1<<(p-1);}int cost=q*__builtin_popcount((unsigned)U);bool seen=false;for(auto &c:cuts[i][j])if(c.m0==a&&c.m1==b){c.cost=min(c.cost,cost);seen=true;break;}if(!seen)cuts[i][j].push_back({a,b,cost});}}}
int sum(const X&x,int mask){int s=0;while(mask){int p=__builtin_ctz((unsigned)mask);s+=x[p];mask&=mask-1;}return s;}
X x{},s{};vector<int> p;int i;A a{};long long checks=0,nodes=0;unordered_map<int,bool> memo;
bool collision(){X w=x;for(int v:p)w[v]-=s[v];for(int j=0;j<4;j++)if(j!=i&&j!=(i+1)%4){checks++;bool sep=false;for(auto c:cuts[i][j])if(sum(w,c.m0)+sum(s,c.m1)>c.cost+2*u){sep=true;break;}if(!sep)return true;}return false;}
bool bad(int k,int rem){if(k==(int)p.size())return collision();int v=p[k];for(int o=0;o<=min(rem,a[k]);o++){s[v]=a[k]-o;if(bad(k+1,rem-o))return true;}return false;}
int key(){int z=0;for(int k=0;k<(int)p.size();k++)z=z*(x[p[k]]+1)+a[k];return z;}
bool path(){int z=key();if(auto it=memo.find(z);it!=memo.end())return it->second;nodes++;if(bad(0,q))return memo[z]=false;bool full=true;for(int k=0;k<(int)p.size();k++)if(a[k]<x[p[k]]){full=false;a[k]++;bool ok=path();a[k]--;if(ok)return memo[z]=true;}return memo[z]=full;}
int main(){init();int N=0,ok=0;int failed[4]={};while(cin>>x[0]>>x[1]>>x[2]>>x[3]>>x[4]>>x[5]>>x[6]){N++;bool works=true;for(i=0;i<4;i++){p.clear();a={};s={};memo.clear();for(int v=0;v<7;v++)if(x[v]&&bit(v+1,i)!=bit(v+1,(i+1)%4))p.push_back(v);if(!path()){failed[i]++;works=false;break;}}if(works){ok++;for(int v:x)cout<<v<<' ';cout<<'\n';}}cerr<<"candidates="<<N<<" survivors="<<ok<<" first_failed=";for(int v:failed)cerr<<v<<' ';cerr<<" nodes="<<nodes<<" cut_queries="<<checks<<'\n';}
