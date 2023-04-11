class Human:
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi!")
    def __str__(self):
        return f"STR fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")
#instance = sınıf içindeki nesneden örnek oluşturuldu.
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()

human2 = Human("Zeynep")
human2.talk("Selam")
human2.walk()
print(human2)


#değişkene atama yapılmadan kullanım:
Human("Zeynep").talk("Merhaba")