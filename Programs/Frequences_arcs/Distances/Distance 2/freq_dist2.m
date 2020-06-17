[f1,f2]=audioread('C:/Users/antoi/Desktop/Frequences_arcs/Distances/Distance 2/V=21kV.flac');

y=f1(:,1)*1000; % Permet de lire et d'amplifier le signal 
Fs = 44100;            % Sampling frequency                    
ST = 1/Fs;             % Sampling period       
L = length(y);         % Length of signal
t = (0:L-1)*ST;         % Time vector

%Transformé de fourier 
% Y = fft(y);
% P2 = abs(Y/L);
% P1 = P2(1:L/2+1);
% P1(2:end-1) = 2*P1(2:end-1);
% f = Fs*(0:(L/2))/L;
% plot(f,P1) 
% title('Single-Sided Amplitude Spectrum of X(t)')
% xlabel('f (Hz)')
% ylabel('|P1(f)|')
MinPeakProminence=60;
MinPeakDistance=500;
findpeaks(y,'MinPeakProminence',MinPeakProminence,'MinPeakDistance',MinPeakDistance);
[pks,locs]=findpeaks(y,'MinPeakProminence',MinPeakProminence,'MinPeakDistance',MinPeakDistance) ;% Trouve tout les pics
locs=locs.*(ST); % Met le resultat en seconde (Localise tout les pics en seconde)
Frequence=1./diff(locs);

FMean=mean(Frequence);
var(Frequence)
