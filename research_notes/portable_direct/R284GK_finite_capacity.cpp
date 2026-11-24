#include <array>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;
using X=array<int,7>; using A=array<int,4>;
int q,u,n;
int bit(int p,int i){return i?((p>>(i-1))&1):0;}
int last(int p,int i){for(int d=1;d<=4;++d){int e=(i-d+4)%4;if(bit(p,e)!=bit(p,(e+1)%4))return e;}return -1;}
struct Cut{int m0,m1,cost;}; vector<Cut> cuts[4][4],stablecuts[4][4];
int adj[4][4]={}; X x{},s{}; vector<int> p; int i; A a{}; long long checks=0,nodes=0,ge=0,stable=0,nonheavy=0,leaves=0,pruned=0,survivors=0,failed[4]={}; unordered_map<int,bool> memo;
int sum(const X&x,int mask){int s=0;while(mask){int p=__builtin_ctz((unsigned)mask);s+=x[p];mask&=mask-1;}return s;}
void init(){for(int i=0;i<4;i++){for(int p=1;p<=7;p++)if(bit(p,i)!=bit(p,(i+1)%4))adj[i][last(p,i)]|=1<<(p-1);for(int j=0;j<4;j++)if(j!=i){for(int U=0;U<256;U++){int a=0,b=0;for(int p=1;p<=7;p++){int E=(1<<last(p,i))|(1<<(4+last(p,j)));if(bit(p,i)!=bit(p,j)&&(U&E)==E)a|=1<<(p-1);if(bit(p,(i+1)%4)!=bit(p,j)&&(U&(1<<(4+last(p,j)))))b|=1<<(p-1);}int cost=q*__builtin_popcount((unsigned)U);auto add=[&](vector<Cut>&v,int b){for(auto &c:v)if(c.m0==a&&c.m1==b){c.cost=min(c.cost,cost);return;}v.push_back({a,b,cost});};add(cuts[i][j],b);if(i<j)add(stablecuts[i][j],0);}}}}
bool collision(){X w=x;for(int v:p)w[v]-=s[v];for(int j=0;j<4;j++)if(j!=i&&j!=(i+1)%4){checks++;bool sep=false;for(auto c:cuts[i][j])if(sum(w,c.m0)+sum(s,c.m1)>c.cost+2*u){sep=true;break;}if(!sep)return true;}return false;}
bool bad(int k,int rem){if(k==(int)p.size())return collision();int v=p[k];for(int o=0;o<=min(rem,a[k]);o++){s[v]=a[k]-o;if(bad(k+1,rem-o))return true;}return false;}
int key(){int z=0;for(int k=0;k<(int)p.size();k++)z=z*(x[p[k]]+1)+a[k];return z;}
bool path(){int z=key();if(auto it=memo.find(z);it!=memo.end())return it->second;nodes++;if(bad(0,q))return memo[z]=false;bool full=true;for(int k=0;k<(int)p.size();k++)if(a[k]<x[p[k]]){full=false;a[k]++;bool ok=path();a[k]--;if(ok)return memo[z]=true;}return memo[z]=full;}
void test(){leaves++;ge++;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){bool ok=false;for(auto c:stablecuts[i][j])if(sum(x,c.m0)>c.cost+2*u){ok=true;break;}if(!ok)return;}stable++;nonheavy+=((x[2]>=2*q+2*u)+(x[4]>=2*q+2*u)+(x[5]>=2*q+2*u))<2;for(i=0;i<4;i++){p.clear();a={};s={};memo.clear();for(int v=0;v<7;v++)if(x[v]&&bit(v+1,i)!=bit(v+1,(i+1)%4))p.push_back(v);if(!path()){failed[i]++;return;}}survivors++;cout<<"survivor: ";for(int v:x)cout<<v<<' ';cout<<endl;}
// Upper bound on adjacent overflow with at most rem unassigned columns.
// Convexity: maximum is achieved by allocating all rem to one eligible group (or none).
int order[]={2,4,5,0,3,1,6};
int future[8];
void gen(int k,int rem){for(int e=0;e<4;e++){int total=0,best=0;for(int m:adj[e]){int z=sum(x,m),v=max(0,z-q);total+=v;if(m&future[k])best=max(best,max(0,z+rem-q)-v);}if(total+best<q+4*u+1){pruned++;return;}}if(k==7){test();return;}int j=order[k];for(int v=0;v<=rem;v++){x[j]=v;gen(k+1,rem-v);}x[j]=0;}
int main(int argc,char**argv){if(argc!=3)return 1;q=stoi(argv[1]);u=stoi(argv[2]);n=4*q+8*u+1;init();for(int k=6;k>=0;k--)future[k]=future[k+1]|(1<<order[k]);gen(0,n);cerr<<"q="<<q<<" u="<<u<<" n="<<n<<" ge="<<ge<<" stable="<<stable<<" nonheavy="<<nonheavy<<" survivors="<<survivors<<" first_failed=";for(auto v:failed)cerr<<v<<' ';cerr<<" nodes="<<nodes<<" cut_queries="<<checks<<" pruned_subtrees="<<pruned<<endl;}
