"""
	Bir Environment instance i olusturularak car generatorina gecirilir ve Environment.process() metodu ile process 
generator ortama eklenir. process() tarafindan dondurulen process, process etkilesimleri icin kullanilabilir. Bunun
en yaygin iki ornegi diger processin sonlanmasini beklemek ve diger process bir olay icin beklerken interrupt etmektir.
"""

""" 
	Bir SimPy processi bir olay gibi kullanilabilir. yield edildiginde process bittigi zaman devam edilir. Ornegin
elektrikle calisan bir arac dusunelim. Aracin tekrar harekete gecebilmesi icin bataryasinin sarj olmasini beklemesi
gerekir. Bu olay ilave bir charge() processi ile modellenebilir. 
"""

import simpy

class Car(object):
	def __init__(self, env):
		self.env 	=	env
		self.action =   env.process(self.run())

	def run(self):
		while True:
			print('Start parking and charging at %d' % self.env.now)
			charge_duration = 5
			# process() metodunun dondurdugu process yield edilir
			# ve processin tamamlanmasi beklenir
			yield self.env.process(self.charge(charge_duration))

			# charge process bittiginde tekrar drive process baslatilabilir
			print('Start driving at %d' %self.env.now)
			trip_duration = 2
			yield self.env.timeout(trip_duration)

	def charge(self, duration):
		yield self.env.timeout(duration)		

def main():
	env = simpy.Environment()
	car = Car(env)
	env.run(until=15)

if __name__ == '__main__':
	main()	
