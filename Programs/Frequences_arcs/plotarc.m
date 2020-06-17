%Distance 1 

V1=[11 13 15 17 19 21];
F1=[22.9945 34.6851 38.2447 38.5363 48.8804 56.4524];
Var1=[9.1520 34.4936 178.84 49.17 15.7764 29.43];
[f,r]=fit(V1',F1','poly1');
Coef=coeffvalues(f)
fit1=Coef(1)*V1+Coef(2)

%Distance 2
V2=[11 13 15 17 19 21];
F2=[17.2270 35.6860 47.4886 46.3466 48.0147 56.1002];
Var2=[3.1745 29.5706 245.9577 729.4383 15.2353 24.3238];

%Distance 3
V3=[7 9 11 13 15 17 19];
F3=[10.4589 28.2917 37.0128 54.6802  68.2510 94.6627 90.2340];
Var3= [15.8088 5.0035 7.4171 23.1632 23.4109 879.2597 938.9789];

%plot
plot(V1,F1,'-x',V2,F2,'-o',V3,F3,'-*')
legend('0.92 mm','1mm','0.5mm')
xlim([0,30])
xlabel('Voltage (kV)')
ylabel('Frequence des arcs (Hz)')
%errorbar(V1,F1,Var1)
A=num2str(Coef(1))
B=num2str(Coef(2))
Legend=strcat('Fit : ',A,'x',B)
plot(V1,F1,'-x',V1,fit1)
xlabel('Voltage (kV)')
ylabel('Frequence des arcs (Hz)')
legend('0.92cm',Legend)