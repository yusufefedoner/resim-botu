# Bu kod parçacığı bir metin dosyasının tamamını okumamızı sağlar
f = open('C:/Users/MEHTAP DÖNER/OneDrive/Masaüstü/kodland/m2l1/metin.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()
