import simpy

# Elektrikli arac orneginden yola cikarak araclarin sarj olmak icin bir istasyona
# gittigini ve iki adet olan slotlari paylastigini dusunelim

def car(env, name, bcs, driving_time, charge_duration):
	# Aracin istasyona gitmesi
	yield env.timeout(driving_time)

	# Kaynaklardan(sarj slotu) birine istekte bulunmasi
	print('%s arriving at %d' % (name, env.now))
	with bcs.request() as req:
		yield req

		# Sarj edilmesi
		print('%s starting to charge at %s' % (name, env.now))
		yield env.timeout(charge_duration)
		print('%s leaving the bcs at %s' % (name, env.now))

# Ortam ve paylasilacak kaynagin uretilmesi
env = simpy.Environment()
bcs = simpy.Resource(env, capacity=2)

# Elektrikli araclarin davranisini simule eden processler
for i in range(4):
	env.process(car(env, 'car %d' % i, bcs, i*2, 5))

env.run()	
