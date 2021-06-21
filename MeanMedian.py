import pandas as pd

data = pd.read_csv("SOCR-HeightWeight.csv")
height = data["Height(Inches)"].tolist()
count = 0
mean = 0

#Mean of the Data
for i in height:
    count = count + i
    mean = count/len(height)

print("Mean of the data: " + str(mean))


#Median of the data
height.sort()

if len(height)%2 == 0:
    print("The number of data is even")
    Median1 = float(height[len(height)//2])
    Median2 = float(height[len(height)//2-1])
    Median = (Median1 + Median2)/2
    print("The median of the data is: " + str(Median))
else:
    print("The number of data is odd")
    Median = float(height[len(height)//2])
    print("The median of the data is: " + str(Median))

