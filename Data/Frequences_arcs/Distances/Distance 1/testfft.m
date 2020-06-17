t=0:ST:1;
y=sin(2*pi*1000*t)

Fs = 44100;            % Sampling frequency                    
ST = 1/Fs;             % Sampling period       
L = length(y);        % Length of signal
t = (0:L-1)*ST;         % Time vector

Y = fft(y);
P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
plot(f,P1) 
title('Single-Sided Amplitude Spectrum of X(t)')
xlabel('f (Hz)')
ylabel('|P1(f)|')