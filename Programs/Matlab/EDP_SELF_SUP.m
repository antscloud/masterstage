N=50;
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
    
    V(1,1:70)= V(2,1:70);
    V(1,130:M)= V(2,130:M);
    
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
cont=contour(X,Y,V,'ShowText','on')
eq=streamline(X,Y,Ex,Ey,startx,starty)
set(eq,'linestyle','-')

hold on
h = zeros(1, 1);
h(1) = plot(NaN,NaN,'-b');
legend(h, 'Current Lines');