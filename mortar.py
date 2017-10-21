'''
Mortar Attack Lab - OS3307
The Dream Team:
	Erin Ward
	Justin Goodwin
	Elizabeth Wanic
DATE - 1 June 2017

to be run with Python version 3.6.0 
'''

import random
import math 


## Testing with the center (0,0) as the target 
i = 0
success = 0
failure = 0 
hitBothTotal = 0
hitBoth = 0 
hitsCount = []

while i < 500:
	hitA = False
	hitB = False
	hitHospital = False

	for s in range(0,5):
		x = random.gauss(0, 20)
		y = random.gauss(0, 25)

		if (-12 <= x <= 12) and (-600 <= y <= 600):
			hitA = True
		if (-600 <= x <= 600) and (-12 <= y <= 12):
			hitB = True
		if (-12 <= x <= 12) and (-12 <= y <= 12):
			hitBoth += 1
			hitBothTotal += 1

		xDist = (x+65)*(x+65)
		yDist = (y-65)*(y-65)
		if math.sqrt(xDist + yDist) <= 50:
			hitHospital = True 

	if hitA and hitB and not hitHospital:
		success += 1
	else:
		failure += 1

	hitsCount.append(hitBoth)
	hitBoth = 0

	i += 1

# Confidence interval for number of successes per volley
phat = success/500

confidenceLow = (phat - 1.96*(math.sqrt(phat*(1-phat)/500)))
confidenceHigh = (phat + 1.96*(math.sqrt(phat*(1-phat)/500)))

# Confidence interval for number of double hits per round
meanHits = hitBothTotal/500
diffsSquared = 0 

#Calculate the standard deviation of the sample
for x in range(0,500):
	diffsSquared += (hitsCount[x] - meanHits) * (hitsCount[x] - meanHits)

sd1 = math.sqrt((1/500)*(diffsSquared))

#Compute the confidence intervals
confidenceLow2 = (meanHits - 2.576* (sd1/math.sqrt(500)))
confidenceHigh2 = (meanHits + 2.576*(sd1/math.sqrt(500)))

print("\n\nTest aiming at center (0,0)\n")
print("     Success means both runways were hit and the hospital was not.")
print("     Successful volleys (out of 500) = ",success)
print("\n     How many times did we hit both runways in one shot?")
print("     Number of rounds that hit the center target (out of 2500) = ",hitBothTotal)

print("\n     Task 1")
print("        95% Confidence Interval for success with aimpoint (0, 0):")
print("            ", confidenceLow, " - ", confidenceHigh, "\n")

print("     Task 2")
print("        Average number of hits on center target per volley (out of 5):")
print("            ", meanHits)
print("        99% Confidence Interval for hitting both runways in one shot (per volley):")
print("            ", confidenceLow2, " - ", confidenceHigh2, "\n")

## Testing with the (12,-12) as the target 
i = 0
success = 0
failure = 0 
hitBothTotal = 0
hitBoth = 0 
hitsCount = []

while i < 500:
	hitA = False
	hitB = False
	hitHospital = False

	for s in range(0,5):
		x = random.gauss(12, 20)
		y = random.gauss(-12, 25)

		if (-12 <= x <= 12) and (-600 <= y <= 600):
			hitA = True
		if (-600 <= x <= 600) and (-12 <= y <= 12):
			hitB = True
		if (-12 <= x <= 12) and (-12 <= y <= 12):
			hitBoth += 1
			hitBothTotal += 1

		xDist = (x+65)*(x+65)
		yDist = (y-65)*(y-65)
		if math.sqrt(xDist + yDist) <= 50:
			hitHospital = True 

	if hitA and hitB and not hitHospital:
		success += 1
	else:
		failure += 1

	hitsCount.append(hitBoth)
	hitBoth = 0

	i += 1

# Confidence interval for successes per volley
phat3 = success/500

confidenceLow3 = (phat3 - 1.96* (math.sqrt(phat3*(1-phat3)/500)))
confidenceHigh3 = (phat3 + 1.96*(math.sqrt(phat3*(1-phat3)/500)))

# Confidence interval for number of double hits per round
meanHits2 = hitBothTotal/500
diffsSquared = 0 

#Calculate the standard deviation of the sample
for x in range(0,500):
	diffsSquared += (hitsCount[x] - meanHits2) * (hitsCount[x] - meanHits2)

sd2 = math.sqrt((1/500)*(diffsSquared))

#Compute the confidence intervals
confidenceLow4 = (meanHits2 - 2.576* (sd2/math.sqrt(500)))
confidenceHigh4 = (meanHits2 + 2.576*(sd2/math.sqrt(500)))

#Should we reject the null?  Is one better than the other at hitting both runways?  
#Test if (0,0) is better.  Null hypothesis is (0,0). Alternative is (12,-12) is greater.
reject12 = False
t = (meanHits2-meanHits)/(sd2/math.sqrt(500))
if t > 1.645:
	reject12 = True

#Test if (12,-12) is better. Null is (12,-12). Alternative is (0,0) is greater.
reject0 = False
t2 = (meanHits-meanHits2)/(sd1/math.sqrt(500))
if t2 > 1.645:
	reject0 = True

#Format output statements
#If we rejected the null of (0,0) to say that (12,-12) was better
if reject12 == True:
	test = "aimpoint (12, -12)"
	other = "aimpoint (0, 0)"
	answer = "can"
#If we rejected the null of (12,-12) to say that (0,0) was better
elif reject0 == True:
	test = "aimpoint (0, 0)"
	other = "aimpoint (12, -12)"
	answer = "can"
#If neither null hypothesis was rejected
else:
	answer = "cannot"
	other = "the other"
	test = "one"


print("Test aiming at (12, -12)\n")
print("     Success means both runways were hit and the hospital was not.")
print("     Successful volleys (out of 500) = ",success)
print("\n     How many times did we hit both runways in one shot?")
print("     Number of rounds that hit the center target (out of 2500) = ",hitBothTotal)

print("\n     Task 3")
print("        95% Confidence Interval for success with aimpoint (12, -12):")
print("            ", confidenceLow3, " - ", confidenceHigh3, "\n")

print("     Task 4")
print("        Average number of hits on center target per volley (out of 5):")
print("            ", meanHits2)
print("        99% Confidence Interval for hitting both runways in one shot (per volley):")
print("            ", confidenceLow4, " - ", confidenceHigh4, "\n")

print("     Task 5")
print("     Which aimpoint has more rounds hitting the center target?")
print("        Do we reject the null and say that (12,-12) is better than (0, 0)? ", reject12)
print("        Do we reject the null and say that (0, 0) is better than (12, -12)? ", reject0)
print("        We",answer,"say that", test, "is better than", other, "\n\n")




