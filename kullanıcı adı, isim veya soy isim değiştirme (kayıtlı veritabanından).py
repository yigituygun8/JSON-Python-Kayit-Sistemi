# Bu program ile sisteme kayıt yaptırıp bilgileri "userslist.json" dosyasına yazdırıp veritabanınna kaydedebiliyorsunuz.
# Ayrıca, kullanıcı adı, isim, soy isim gibi bilgileri, veritabanındaki bilgi ile uyuştuğu takdirde, değiştirebiliyorsunuz.

import json


createUser = str(input("Kullanıcı Adı Oluştur: "))
createName = str(input("İsminiz: "))
createSurname = str(input("Soy isminiz: "))


addUser = {
        "userName": createUser,
        "firstName": createName,
        "lastName": createSurname
}

with open("userslist.json") as file:
    users = json.load(file)


users.append(addUser)


with open("userslist.json", "w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)

with open("userslist.json") as file:
    users = json.load(file)


change = int(input("Ne Değişmek İstiyorsunuz?: (1- Kullanıcı Adı / 2- İsim / 3-Soy İsim) "))
if change == 1:
    eski1 = str(input("Eski Kullanıcı Adınız: "))
    for addUser in users:
        if addUser["userName"] == eski1:
            newUser = str(input("Yeni Kullanıcı Adınız: "))
            addUser["userName"] = newUser
            

if change == 2:
    eski2 = str(input("Eski İsminiz: "))
    for addUser in users:
        if addUser["firstName"] == eski2:
            newName = str(input("Yeni İsminiz: "))
            addUser["firstName"] = newName
        
    

if change == 3:
    eski3 = str(input("Eski Soy İsminiz: "))
    for addUser in users:
        if addUser["lastName"] == eski3:
            newSurname = str(input("Yeni Soy İsminiz: "))
            addUser["lastName"] = newSurname

        
            


with open("userslist.json", "w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)

