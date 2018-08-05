"""
	Elektrikli arac tamamen sarj olana dek beklemek istemedigimizi dusunelim. Boylece charge() processini
interrupt ederek tekrar driving() processi ile devam ederiz. Kosan bir process interrupt() metodu ile
kesilebilir.
"""

import simpy

def driver(env, car):
	print('Driver process')
	yield env.timeout(3)
	car.action.interrupt()

class Car(object):
	def __init__(self, env):
		self.env 		=	env
		self.action 	=	env.process(self.run())

	def run(self):
		while True:
			print('Start parking at %d' % self.env.now)
			charge_duration = 5
			# charge() processi kesilmek istenebilir
			try:
				yield self.env.process(self.charge(charge_duration))
			except simpy.Interrupt:
				# Kesme alindiginda charging durumundan driving
				# durumuna gecilir
				print('Was interrupted. Hope, the battery is full enough...')

			print('Start driving at %d' % self.env.now)
			trip_duration = 2
			yield self.env.timeout(trip_duration)

	def charge(self, duration):
		yield self.env.timeout(duration)

def main():
	env = simpy.Environment()
	car = Car(env)
	env.process(driver(env, car))
	env.run(until=15)

if __name__ == '__main__':
	main()				
						