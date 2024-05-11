def euclidean_distance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

x1 = float(input("Birinci noktanın x koordinatını girin: "))
y1 = float(input("Birinci noktanın y koordinatını girin: "))
x2 = float(input("İkinci noktanın x koordinatını girin: "))
y2 = float(input("İkinci noktanın y koordinatını girin: "))

nokta1 = (x1, y1)
nokta2 = (x2, y2)

print("Öklid uzaklığı:", euclidean_distance(nokta1, nokta2))