import matplotlib.pyplot as plt
# import numpy as np


# ber = {
#     'bpsk': {1.0429943153521592e-10, 1.043000556527073e-10},
#     'qpsk': {},
#     '8psk': {},
#     '16psk': {}
# }

bpsk = [1.0429943153521592e-10, 5.02E-06, 0.0004720935884, 0.000472093801]
qpsk = [3.5018865940475577e-06, 0.000895729, 0.009689610262,0.009689612576]
eight_psk = [0.0021758635440927826, 0.027279614, 0.08389873445, 0.08389874408]
# sixteen_psk = [0.19691649217521787, 0.247034104, 0.2778365728, 0.3294061356]

gosnr = [20.192206, 9.741003, 5.466968, 1.170099]

plt.plot(gosnr, bpsk, marker='o',color='red', label="bpsk")
plt.plot(gosnr, qpsk, marker='o',color='blue', label="qpsk")
plt.plot(gosnr, eight_psk, marker='o',color='green', label="8psk")
# plt.plot(gosnr, sixteen_psk, marker='o',color='gray', label="16psk")

plt.legend(loc = 'upper right')

plt.xlabel('gosnr')
plt.title("gosnr and bit error rate in 16QAM")

plt.show()