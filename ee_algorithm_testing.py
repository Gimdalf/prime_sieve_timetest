from time import time
import numpy as np
import gc

from math import ceil, sqrt
def timed_esieve(n):
	tyms = []
	tymin = time() 

	prime_list = [True if i%2 ==1 else False1 for i in range(n-2)]
	i = 1

	tyms.append(time() - tymin)
	tymin = time()

	while (i+2)**2 <= n:
		if prime_list[i]:
			for j in range(3, int(ceil(n/(i+2))), 2):
				prime_list[(i+2)*j-2]=False
		i+=2

	tyms.append(time() - tymin)
	tymin = time()

	rawprimelist = []
	for i in range(len(prime_list)):
		if prime_list[i] == True:
			rawprimelist.append(i+2)
	tyms.append(time() - tymin)
	#has 3 time markers
	return tyms

def timed_atkin(nmax):
	tyms = []
	tymin = time()

	rlist = [2,3,5]
	slist = [False for i in range(nmax)]

	tyms.append(time() - tymin)
	tymin = time()

	# fp = lambda x, y: True if (4*x**2 + y**2) % 60 in (1,13,17,29,37,41,49,53) else False
	# tp = lambda x, y: True if (3*x**2 + y**2) % 60 in (7,19,31,43) else False
	# tm = lambda x, y: True if (3*x**2 - y**2) % 60 in (11,23,47,59) else False
	for x in range(int((sqrt(nmax)+1))):
		for y in range(int(sqrt(nmax)+1)):
			n = 4*x**2 + y**2
			if (4*x**2 + y**2) % 60 in (1,13,17,29,37,41,49,53) and n < nmax:
				slist[n] = not slist[n]
			n = 3*x**2 + y**2
			if (3*x**2 + y**2) % 60 in (7,19,31,43) and n < nmax:
				slist[n] = not slist[n]
			n = 3*x**2 - y**2
			if y < x and (3*x**2 - y**2) % 60 in (11,23,47,59) and n < nmax:
				slist[n] = not slist[n]

	tyms.append(time() - tymin)
	tymin = time()

	for i in range(6, len(slist)):
		if slist[i] == True:
			count = 1
			while count*i**2 < nmax:
				slist[count*i**2] = False
				count += 1
			rlist.append(i)
	tyms.append(time() - tymin)
	tymin = time()
	return tyms

def timed_ssieve(inp):
	tyms = []
	tymin = time()
	n = int((inp-1)/2)
	
	primelist = [True for i in range(n+1)]
	# print("Primelist length: {:d}".format(len(primelist)))

	tyms.append(time() - tymin)
	tymin = time()

	for i in range(1, int((sqrt(2*n+2)-1/2))):
		j = i
		while i + j + 2*i*j <= n:
			primelist[i+j+2*i*j] = False
			j += 1
	tyms.append(time() - tymin)
	tymin = time()

	rawprimelist = [2]
	for i in range(1, len(primelist)):
		if primelist[i]:
			rawprimelist.append((2*i)+1)
	tyms.append(time() - tymin)
	return tyms

for j in range(1,6):
	test_runtime = time()
	erast_times = open("erast{}.txt".format(j), "w")
	sunda_times = open("sunda{}.txt".format(j), "w")
	atkin_times = open("atkin{}.txt".format(j), "w")
	rang = [i**2 for i in range(3, 2000)]
	for i in rang:
		tyms = []
		tymin = time()
		for alg, file in ((timed_esieve, erast_times), (timed_ssieve, sunda_times), (timed_atkin, atkin_times)):
			timinz = alg(i)
			file.write("\n {} ".format(i)+" ".join(list(map(lambda x: str(x), timinz))))
			gc.collect
	print("Trial: {} completed, time taken: {}".format(j, time() - test_runtime))