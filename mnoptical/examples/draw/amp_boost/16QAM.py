import matplotlib.pyplot as plt
# import numpy as np


bpsk = [0.0000000214557219648747,	5.761407673501742e-10,	3.739417393705592e-13	,4.924676701284285e-14]
qpsk = [5.356786256053086e-05,	8.387849566714112e-06,	1.9867147655802385e-07,	7.088881855670204e-08]
eight_psk = [0.007474674682	,0.003225440765704361	,0.0006017472374181713	,0.0003801483546026469]
# sixteen_psk = [0.2189248717	,0.2035275409545132	,0.17750642888253051,	0.17126273806132186]

gosnr = [15.006602,	18.524242,	25.707195,	27.698431]

plt.plot(gosnr, bpsk, marker='o',color='red', label="bpsk")
plt.plot(gosnr, qpsk, marker='o',color='blue', label="qpsk")
plt.plot(gosnr, eight_psk, marker='o',color='green', label="8psk")
# plt.plot(gosnr, sixteen_psk, marker='o',color='gray', label="16psk")

plt.legend(loc = 'upper right')

plt.xlabel('gosnr')
plt.title("gosnr and bit error rate in 16QAM")

plt.show()