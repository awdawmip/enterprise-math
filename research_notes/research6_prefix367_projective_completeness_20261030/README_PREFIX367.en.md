# PREFIX-367 — Projective completeness of five-port elimination: 8 = 1 + 6 + 1

Status: AUTHOR_SIDE_EXACT_SYMBOLIC, LOCAL_VERIFIED, UNREVIEWED, NOT_ADMITTED (2026-10-30). Frozen input: GLOBAL_KNOWLEDGE_V1 main@fc04681d8785f58ea45f82edf20fca1b4b9ec6ea; Enterprise Math main@f05844fa7a1ed5fa3e75fc98eecd757949bcb3f2. Native owner query yielded CONTROL_QUOTA and no formal claim or review was acquired. This is a static auxiliary complex 3D five-port statement, not an X6/Heartbeat theorem.

Fix A=[[4,4,0],[0,-4,4],[-5+3i,0,-3+i],[-2-2i,4+4i,2+2i],[-2,0,5+2i]], Q=(34000+204144t,3200+56336t,58250+1286t,46600+12936t,31525+28011t), 0<=t<=1/4. After fixing overall phase y1>0 and setting u=y2/y1, v=y3/y1, the last two relative measurement rows are B=[[5/2+9i/2,3/2+7i/2,4i],[11/4+15i/8,11/4+15i/8,5/4+9i/4]]. For row (a_j,b_j,c_j), let F_j=(a_j+b_j u+c_jv)(conj(a_j)Q1uv+conj(b_j)Q2v+conj(c_j)Q3u)-Q_juv, j=4,5. A general complex solution of F4=F5=0 need not obey the physical modulus constraints.

**Theorem.** For every t in [0,1/4], the two bihomogenized curves have bidegree (2,2), no common component, and total complex projective intersection length 8. Exactly two universal simple basepoints are present: (u,v)=(0,0) and (infinity,infinity). No other boundary intersection occurs. Consequently there are exactly SIX intersections in (C*)², counted with multiplicity, for every t.

The complex Jacobians at the basepoints are exact:
J0=(3699/2-1313i/2)(643t+29125)(3521t+200) != 0;
Jinfty=(14796+5252i)(12759t+2125)^2 != 0.
At v=infinity with u finite, the leading-v coefficient equations have determinant 7/8-37i/8 != 0; at u=infinity with v finite their leading-u equations have determinant 1/2-i/4 != 0. The same determinants exclude nonzero common axis points. In the reciprocal chart p=1/u,q=1/v the local polynomials are (a_jpq+b_jq+c_jp)(conj(a_j)Q1+conj(b_j)Q2p+conj(c_j)Q3q)-Q_jpq.

Direct exact algebra establishes Res_v(F4,F5)=u P_t(u), deg_u P=6, with
LC(P)=(252404-3550672i)(12759t+2125)^3(643t+29125),
P_t(0)=(252404+3550672i)(3521t+200)^3(643t+29125).
Both are nonzero in the interval, hence there is no common affine component. No projective boundary line is a component. For fiber classes H_u,H_v on P¹×P¹, H_u²=H_v²=0 and H_u H_v=1, so (2H_u+2H_v)^2=8. Subtract two transversal basepoints to get six. This invokes standard intersection theory: The Stacks Project, Chow rings, Tag 0B0G, https://stacks.math.columbia.edu/tag/0B0G .

Physical sources also obey |u|²=(3521t+200)/(12759t+2125) increasing, and |v|²=(643t+29125)/(8(12759t+2125)) decreasing, yielding
8/85 <= |u|² <= 4321/21259 and 117143/170072 <= |v|² <= 233/136.
Thus physical sources cannot escape through zero/infinity. SIX complex algebraic intersections with multiplicity does **not** mean six physically admissible U(1) source orbits; the earlier 6/4/2 real-source classification remains separately dependent on physical filtering and H3/H12 certificates, and is not independently reproved here.

The exact SymPy 1.14.0 checker actually returned PASS_PREFIX367_PROJECTIVE_8_EQUALS_1_PLUS_6_PLUS_1. The checker tests the concrete algebraic identities, not the standard Chow-ring theorem nor any physical/X6 mapping. BRC REUSE_APPLIED retains (u,v), port and source identity, distinguishing algebraic intersection multiplicity from physical observer fibers.

Next PREFIX-368: independently certify the physical-real-form filtering of the six complex solutions over parameter intervals, then specify a scope-limited native X6 Cell/3D-slice third-component/ordered-path/port observation bridge, without prematurely asserting Heartbeat time dynamics.
