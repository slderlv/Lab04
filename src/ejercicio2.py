import numpy as np

file = open("src/UNI_CORR_500_01.txt","r")
coordenates = [coord.strip("\n").split("\t")[2:] for coord in file.readlines()[4:]]
XList = []
YList = []
ZList = []
for coor in coordenates:
  XList.append(coor[0])
  YList.append(coor[1])
  ZList.append(coor[2])

uniqueX, Xfrequency = np.unique(XList,return_counts=True)
uniqueY, Yfrequency = np.unique(YList,return_counts=True)
uniqueZ, Zfrequency = np.unique(ZList,return_counts=True)

print("Las coordenadas X que más se repiten:",uniqueX[Xfrequency==max(Xfrequency)],"con un recuento de",max(Xfrequency))
print("Las coordenadas Y que más se repiten:",uniqueY[Yfrequency==max(Yfrequency)],"con un recuento de",max(Yfrequency))
print("Las coordenadas Z que más se repiten:",uniqueZ[Zfrequency==max(Zfrequency)],"con un recuento de",max(Zfrequency))