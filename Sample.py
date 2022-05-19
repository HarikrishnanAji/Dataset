import csv

with open("records.csv",'r') as file:
	datas = csv.reader(file)
	value = [data for data in datas]

res = []

for i in range(1, len(value)):

	slope = float(value[i][0])
	vib = float(value[i][1])
	moist = float(value[i][2])

	if (slope < 8):
		if (moist < 25):
			if (vib < 0.039):
				res.append([slope, vib, moist, 1])
			elif (0.040< vib < 0.092):
				res.append([slope, vib, moist, 1])
			else:
				res.append([slope, vib, moist, 1])

		elif(26 <moist < 75):
			if (vib < 0.039):
				res.append([slope, vib, moist, 1])
			elif (0.039< vib < 0.092):
				res.append([slope, vib, moist, 1])
			else:
				res.append([slope, vib, moist, 0])
		else:
			if (vib < 0.039):
				res.append([slope, vib, moist, 1])
			elif (0.039< vib < 0.092):
				res.append([slope, vib, moist, 1])
			else:
				res.append([slope, vib, moist, 0])
	elif(9 < slope < 35):
		if (moist < 25):
			if (vib < 0.039):
				res.append([slope, vib, moist, 1])
			elif (0.040< vib < 0.092):
				res.append([slope, vib, moist, 1])
			else:
				res.append([slope, vib, moist, 0])

		elif(26 <moist < 75):
			if (vib < 0.039):
				res.append([slope, vib, moist, 0])
			elif (0.039< vib < 0.092):
				res.append([slope, vib, moist, 0])
			else:
				res.append([slope, vib, moist, 0])
		else:
			if (vib < 0.039):
				res.append([slope, vib, moist, 0])
			elif (0.039< vib < 0.092):
				res.append([slope, vib, moist, 0])
			else:
				res.append([slope, vib, moist, 0])
	else:
		if (moist < 25):
			if (vib < 0.039):
				res.append([slope, vib, moist, 1])
			elif (0.040< vib < 0.092):
				res.append([slope, vib, moist, 0])
			else:
				res.append([slope, vib, moist, 0])

		elif(26 <moist < 75):
			if (vib < 0.039):
				res.append([slope, vib, moist, 0])
			elif (0.039< vib < 0.092):
				res.append([slope, vib, moist, 0])
			else:
				res.append([slope, vib, moist, 0])
		else:
			if (vib < 0.039):
				res.append([slope, vib, moist, 0])
			elif (0.039< vib < 0.092):
				res.append([slope, vib, moist, 0])
			else:
				res.append([slope, vib, moist, 0])

with open("test.csv", "w",newline='') as f:
	cw = csv.writer(f)
	cw.writerow(["slope", "vibration", "moisture", "status"])
	cw.writerows(res)