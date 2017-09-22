import pandas as pd
import rerata

data = pd.read_csv('data.csv')
print "jumlah data"
print len(data)
#print data
data_kelahiran = data[data.tahun == 2009]
data_kelahiran = data_kelahiran[data_kelahiran.nama_provinsi == 'Prov. Jawa Tengah']
data_kelahiran.to_csv('jawa_tengah.csv', sep='\t')
kelahiran_nasional = data_kelahiran['persen_kelahiran'].tolist()
nama_kabkota = data_kelahiran['nama_kabkota'].tolist()


print kelahiran_nasional

print "jumlah data"
print len(kelahiran_nasional)
print "data terendah"
data_new = sorted(kelahiran_nasional)
print data_new[0]

print "data tertinggi"
print data_new[-1]

# print kelahiran_jogja
print "rerata kelahiran : "
print rerata.mean(kelahiran_nasional)

print "modus :"
print rerata.mode(kelahiran_nasional)

print "median :"
print rerata.median(kelahiran_nasional)

print "varience :"
print rerata.variance(kelahiran_nasional)

print "standar deviasi :"
print rerata.standard_deviation(kelahiran_nasional)

print "quartil 1"
q_1 = rerata.quartile_1(kelahiran_nasional)
q_1_r = q_1 - data_new[0]
print "range quartil 1"
print q_1_r
print "quartil 3"
q_3 = rerata.quartile_3(kelahiran_nasional)
q_3_r = q_3 - data_new[0]
print "range quartil 3"
print q_3_r
print "range"
print rerata.range(kelahiran_nasional)
# kurang range dan interquartile range

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = tuple(nama_kabkota)
y_pos = np.arange(len(objects))
performance = kelahiran_nasional
 
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Presentase')
plt.title('Kelahiran tertolong oleh tenaga kesehatan terlatih')
 
plt.show()