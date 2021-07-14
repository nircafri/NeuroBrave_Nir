clear all; close all;
%% Question 3
%% A:
% Sampling
fs = 50000;     % Sampling rate [Hz]
Ts = 1/fs;     % Sampling period [s]
fNy = fs / 5;  % Nyquist frequency [Hz]
duration = 1; % Duration [s]
t = 0 : Ts : duration-Ts; % Time vector
% Original signal
x = sin(pi*200* t);
% Harmonics
x1 = sin(2 .* pi .* 200 .* t);
x2 = sin(2 .* pi .* 2000 .* t);
x3 = sin(2 .* pi .* 5000 .* t);
% Contaminated signal
xn = x + x1 + x2 + x3;


noSamples = length(t);    % Number of samples
% Frequency analysis
f = 0 : fs/noSamples : fs - fs/noSamples; % Frequency vector
% FFT

x_fft = abs(fft(x));
xn_fft = abs(fft(xn));
%Cut half of amplituds for non-symmentry harmonies
xn_fft=xn_fft(1:length(xn_fft)/2);
x= x((1:length(x)/2));
xn=xn(1:length(xn)/2);
x_fft=x_fft(1:length(x_fft)/2);
t=t((1:length(t)/2));
f=f((1:length(f)/2));

%% Plot
figure(1);
subplot(2,2,1);
plot(t, x);
title("X")
ylabel('Amplitude')
xlabel('Times[Sec]')

subplot(2,2,2);
plot(t, xn);
title("Xn")
ylabel('Amplitude')
xlabel('Times[Sec]')

subplot(2,2,3);
plot(f,x_fft);
title("X FFT")
ylabel('Power Spectrom')
xlabel('Frequency[Hz]')
xlim([0 fNy]);

subplot(2,2,4);
plot(f,xn_fft);
title("Xn FFT")
ylabel('Power Spectrom')
xlabel('Frequency[Hz]')
xlim([0 fNy]);
%% B:
freqlowpass = 300; % low pass [Hz]
xnfftlowpass = lowpass(xn,freqlowpass,fs);
%Plot
figure()
pspectrum(xnfftlowpass,fs)
ylabel('Power Spectrom')
xlabel('Frequency[KHz]')
title("Low pass, freq: " + freqlowpass +"[Hz]")
%% C:
for order = 1:3
    xnfftlowpass = lowpass(xnfftlowpass,freqlowpass,fs);
    %Plot
    figure()
    pspectrum(xnfftlowpass,fs)
    ylabel('Power Spectrom')
    xlabel('Frequency[KHz]')
    title("Low pass, freq: " + freqlowpass +"[Hz]" + "order: " + (order+1))
end