import random
dongu = 0
deniz = []
sayac = 0
yapılanatıs = 0

while dongu == 0 :
   büyüklük = int(input("oyun alanının büyükülüğünü giriniz :"))
   if(büyüklük < 10):
      print("oyunu alanını çok küçük girdiniz!")
      break
  toplamhak = int((büyüklük*büyüklük)/3)
   for i in range(büyüklük):
     deniz.append(["?"]*büyüklük)
   def deniz_yazdir(deniz):
      for satir in deniz:
          print(" ".join(satir))

   deniz_yazdir(deniz)





   gemi_satir = random.randint(0, büyüklük-1)
   gemi_sutun = random.randint(0, büyüklük-1)
   gemi1_satir = random.randint(0, büyüklük-1)
   gemi1_sutun = random.randint(0, büyüklük-1)
   gemi2_satir =  random.randint(0, büyüklük-1)
   gemi2_sutun =  random.randint(0, büyüklük-1)
   gemi3_satir = random.randint(0, büyüklük-1)
   gemi3_sutun = random.randint(0, büyüklük-1)
   kontrol = 0
   while kontrol == 0 :

       if (gemi_satir == gemi1_satir and gemi_sutun == gemi1_sutun):
          gemi1_satir = random.randint(0, büyüklük-1)
          gemi1_sutun = random.randint(0, büyüklük-1)
          continue
       elif (gemi_satir == gemi2_satir and gemi_sutun == gemi2_sutun):
          gemi2_satir = random.randint(0, büyüklük-1)
          gemi2_sutun = random.randint(0, büyüklük-1)
          continue
       elif (gemi1_satir == gemi2_satir and gemi1_sutun == gemi2_sutun):
          gemi2_satir = random.randint(0, büyüklük-1)
          gemi2_sutun = random.randint(0, büyüklük-1)
          continue

       elif (gemi_satir == gemi3_satir and gemi_sutun == gemi3_sutun):
           gemi3_satir = random.randint(0, büyüklük-1)
           gemi3_sutun = random.randint(0, büyüklük-1)
           continue

       elif(gemi1_sutun == gemi3_sutun and gemi1_satir == gemi3_satir):
          gemi3_sutun = random.randint(0, büyüklük-1)
          gemi3_satir = random.randint(0, büyüklük-1)
          continue

       else:
           print("-" * 35)
           tahmin_satir = int(input("Satır giriniz: "))
           tahmin_sutun = int(input("Sütun giriniz: "))

           if (tahmin_satir == gemi_satir and tahmin_sutun == gemi_sutun) \
                  or (tahmin_satir == gemi1_satir and tahmin_sutun == gemi1_sutun) \
                  or (tahmin_satir == gemi2_satir and tahmin_sutun == gemi2_sutun):
              if deniz[tahmin_satir - 1][tahmin_sutun - 1] == "*":
                 print("-" * 35)
                 print("Zaten tahmin ettiniz")
                 print("-" * 35)
                 puan = toplamhak-yapılanatıs
                 print(puan)
                 deniz_yazdır(deniz)
                 yapılanatıs += 1
              else:
                 print("-" * 35)
                 print("Tebrikler gemiyi batırdınız!")
                 deniz[tahmin_satir - 1][tahmin_sutun - 1] = "X"
                 print("-" * 35)
                 puan = toplamhak-yapılanatıs
                 print(puan)
                 deniz_yazdir(deniz)
                 sayac += 1
                 yapılanatıs += 1


           else:
              if (tahmin_satir < 0 or tahmin_sutun < 0) or (tahmin_satir > büyüklük or tahmin_sutun > büyüklük):
                 print("-" * 35)
                 print("Alan sınırları dışında değer girdiniz")

              elif deniz[tahmin_satir - 1][tahmin_sutun - 1] == "*":
                 print("-" * 35)
                 print("Zaten tahmin ettiniz")
                 print("-" * 35)
                 yapılanatıs += 1
                 puan = toplamhak-yapılanatıs
                 print(puan)
                 deniz_yazdir(deniz)
              else:
                 print("-" * 35)
                 print("Vuramadınız")
                 deniz[tahmin_satir - 1][tahmin_sutun - 1] = "*"
                 print("-" * 35)
                 yapılanatıs += 1
                 puan = toplamhak-yapılanatıs
                 print(puan)
                 deniz_yazdir(deniz)


              if sayac == 3:
                 print("-" * 35)
                 print("Tebrikler bütün gemileri batırdınız ve oyunu kazandınız")
                 print("-" * 35)
                 puan = toplamhak-yapılanatıs
                 print(puan)
                 break



