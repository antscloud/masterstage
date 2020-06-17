clear all
Npre = 1000; Nplot = 1000;
Values=1:0.01:3.999;
Steps=100; % Nombre de diagrammes à moyenner proportionnel au spot
StockPoints=zeros(Steps,length(Values));
for k=1:1:Steps
    x = zeros(Nplot,1);
    Points=zeros(length(Values),1);
    i=1;
    for r = Values
        x(1) = 0.5;
        for n = 1:Npre
        x(1) = r.*x(1).*(1 -x(1));
        end
    for n = 1:Nplot-1
        x(n+1) = r.*x(n).*(1 - x(n));
    end
    Points(i)=x(randi(numel(1:1:length(x))));
    %plot(r, x(randi(numel(1:1:length(x)))), '.-', 'markersize', 5);
    %hold on;
    i=i+1;
    end
    StockPoints(k,:)=Points'; %Chaque ligne contient les valeurs d'un graphe de bifurcation
end

%Sommes directs
PointsSum=0;
for k=1:1:Steps
   PointsSum=PointsSum+StockPoints(k,:);
end
PointsSum=PointsSum/Steps;


%Inverse des sommes 
PointsSumInv=0;
for k=1:1:Steps
   PointsSumInv=PointsSumInv+(1./StockPoints(k,:));
end
PointsSumInv=1./PointsSumInv;

%Moyenne géométrique
PointsSumGeo=1;
for k=1:1:Steps
   PointsSumGeo=PointsSumGeo.*(StockPoints(k,:));
end
PointsSumGeo=PointsSumGeo.^(1/Steps);


title('Bifurcation diagram of the logistic map');
xlabel('r');  ylabel('x_n');
legend()
plot(Values,PointsSum)
hold on
%plot(Values,PointsSumInv)
hold on
%plot(Values.^4,PointsSumGeo)
legend('Moyenne arithmétique','Inverse de la somme des inverses','Moyenne géométrique')

%plot d'un seul chemin
plot(Values,Points)