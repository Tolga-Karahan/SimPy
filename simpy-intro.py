"""
	SimPy bir discrete-event simulasyon kutuphanesidir. Araclar, musteriler ve ya mesajlar
gibi aktif bilesenler processler ile modellenir. Tum processler bir ortamda(environment) bulunur.
Ortam ve birbirleri ile olaylar araciligiyla etkilesim kurarlar.

	Processler Python generatorleri ile tanimlanir. Yasam surecleri boyunca olaylari uretirler
ve yield ifadesi ile bu olaylarin tetiklenmesini beklerler. Bir process bir olayi yield
ettiginde susturulmalidir. SimPy olay olustugu zaman processi devam ettirir(olay tetiklenir).
Birden fazla process ayni olay icin bekleyebilir. SimPy bu processleri olaylari yield ettikleri
sira ile devam ettirir. Yani olayi ilk yield eden process(generator) ilk devam eden process olur.

	Onemli bir olay tipi Timeout'tur. Bu tipte olaylar belirli miktarda bir zaman gectikten sonra
tetiklenirler. Bu sayede process uyuyabilir ve ya belirli bir ssre icin durumunu koruyabilir. Bir
Timeout ve diger tum olaylar processin yasadigi Environment'in uygun metodu cagirilarak olusturulabilir.
"""

"""
	car processi yeni olaylar uretebilmek icin ortama(Environment) bir referans tutmalidir. car generator i
icerisinde bir arabanin davranisi tanimlanmistir. Generator icerisinde bir timeout olayi yield edilir ve kontrol
simulasyona gecer, yield edilen olay gerceklestiginde ise kontrol tekrar generator a gecer ve generator kaldigi
noktadan devam eder. 
""" 

import simpy

def car(env):
	while True:
		print('Start parking at %d' % env.now)
		parking_duration = 5
		yield env.timeout(parking_duration)

		print('Start driving at %d' % env.now)
		trip_duration = 2
		yield env.timeout(trip_duration)

def main():
	env = simpy.Environment()
	env.process(car(env))
	env.run(until=15)

if __name__ == '__main__':
	main()

