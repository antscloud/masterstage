% N=5 # Nombre de ligne 
% M=200 # Nombre de colonne 
% V=np.zeros([N+1,M+1]) #Initialisation du réseau. 
% #V[1:99,1:99]=0.25*(V[2:100,1:99]+V[0:98,1:99]+V[1:99,2:100]+V[1:99,0:98])
% #V[1:N-1,1:N-1]=0.25*(V[2:N,1:N-1]+V[0:N-2,1:N-1]+V[1:N-1,2:N]+V[1:N-1,0:N-2])
% 
% ParMaille=1#(N/M)**2
% Eps= 1e-10
% Ecart=1.0
% i=np.arange(1,8)
% Size=np.zeros(len(i))
% Field=np.zeros(len(i))
% while Ecart>Eps:
%     Vprec=V.copy()
%     V[N,:]=100 # Toutes les colonnes, et la ligne 99
%     V[:,0]=V[:,1] #Bord Gauche
%     V[:,M]=V[:,M-1] #Bord Droit 
%     
%     V[1:N,1:M]=(1/(2*(ParMaille+1)))*(ParMaille*(V[2:N+1,1:M]+V[0:N-1,1:M])+V[1:N,2:M+1]+V[1:N,0:M-1])
%     
%     V[0,0:70]= V[1,0:70]
%     V[0,130:M]= V[1,130:M]
%     Ecart = np.max(np.abs(V-Vprec))
% 
% x = np.arange(0,M+1,1)
% y = np.arange(0,N+1,1)
% X,Y = np.meshgrid(x,y)
% 
% A=np.linspace(1,M,40)
% B = (N-1)*np.ones(len(A))
% seed_points = np.array([A,B])
% 
% 
% Ey,Ex = gradient(V)
% 
% Ey=-Ey
% Ex=-Ex
% plt.figure(figsize=(8,5))
% plt.contour(X,Y,V,20,colors='b')
% plt.streamplot(X, Y, Ex, Ey,linewidth=1,arrowstyle='->',density=10,start_points=seed_points.T,color='orange')

N=80;
M=200;
V=zeros([N,M]);
ParMaille=1 ;%(N/M)**2
Eps= 1*10^(-20);
Ecart=1.0;
    V(41,1:70)= V(42,1:70);
    V(41,130:M)= V(42,130:M);
    V(39,1:70)= V(38,1:70);
    V(39,130:M)= V(38,130:M);
while Ecart>Eps
    Vprec=V;
    V(N,:)=100;
    
    V(:,1)=V(:,2);
    V(:,M)=V(:,M-1);
    %V(2:N-1,2:M-1)=(1/(2*(ParMaille+1)))*(ParMaille*(V(3:N,2:M-1)+V(1:N-2,2:M-1))+V(2:N-1,3:M)+V(2:N-1,1:M-2));
    V(2:N-1,2:M-1)=(4/20)*(V(3:N,2:M-1)+V(1:N-2,2:M-1)+V(2:N-1,3:M)+V(2:N-1,1:M-2))+(1/20)*(V(1:N-2,3:M)+V(1:N-2,1:M-2)+V(3:N,3:M)+V(3:N,1:M-2));
    
    V(41,1:70)= V(42,1:70);
    V(41,130:M)= V(42,130:M);
    V(39,1:70)= V(38,1:70);
    V(39,130:M)= V(38,130:M);
    
    Ecart = max(abs(V-Vprec));
end

x=1:1:N;
y=1:1:M;
[X,Y] = meshgrid(y,x)
[Ex,Ey] = gradient(V);
Ex=-Ex
Ey=-Ey
display("fini")
startx = linspace(0,200,50);
starty = (N)*ones(size(startx));
contour(X,Y,V,'ShowText','on')
eq=streamline(X,Y,Ex,Ey,startx,starty)
set(eq,'linestyle','-')