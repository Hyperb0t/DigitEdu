from django.contrib.auth.models import User
from main.models import Student, Group, PointList, Subject, AdditionalEduResource, ResourceToStudent, Lesson
import random

names = ["Nikita", "Tagmir", "YAkov", "Aleksandr", "Alina", "Damir", "Anastasiya", "Igor'", "Еgor", "Al'bina", "Muhammad", "Anzhela", "Dmitrij", "Filipp", "Dmitrij", "Samat", "Daniyal", "Artur", "Artem", "Anna", "Nuriya", "Dmitrij", "Dmitrij", "David", "Ravil'", "Farit", "Aleksandra", "Bulat", "Alteya", "Almaz", "Maksim", "Ajdar", "Kadyr", "Dinara", "Aida", "Bogdan", "Mihail ", "Bulat", "Remir", "Samat", "Aleksandr", "Nikita", "Еkaterina", "Rajnur", "Aliya", "Ruslan", "Maksim", "Il'ya", "Artem", "Radel' ", "Dinar", "Ajnur", "Askar", "Timur", "Gul'naz ", "Adel'", "Roman", "Al'sina", "Arslan", "Diana", "Damir", "Angelina", "Aleksej", "Maksim", "Mihail", "Dmitrij", "Kamil'", "Regina", "Salavat", "Ural", "Bulat", "Marat", "Danil", "Marsel'", "Renat", "Viktoriya", "Daniil", "Vladislav", "Alina", "Daniil", "Adelya", "Ajnur", "Ajrat", "Bulat", "Sergej", "Aleksandr", "Anastasiya", "Artyom", "Ruslan", "Rinat", "Danila", "Evelina", "Amir", "Semyon", "Ruslan", "Al'bert", "Niyaz", "Sergej", "Dmitrij", "Alena", "Almaz", "Ayaz", "Stepan", "Ruslan", "Pavel", "Dzhalil", "Dmitrij", "Bulat", "El'dar", "Nail'", "Mark", "Roman", "Roman", "Azat", "Kamilla", "Artur", "Ajdar", "Dinar", "Marat", "Rinat", "Timur", "Azat", "Il'ya ", "Sabina", "Konstantin", "Vitalij", "Syumbel'", "Aleksandr", "Alina", "Aleksandra", "Aleksandra", "Ramil'", "Ravil'", "Damir", "Artem", "Rajnur", "Dar'ya", "Tat'yana", "Timur", "Еkaterina", "Linar", "Il'ya", "Il'ya", "Rasim", "Zagir", "Timur", "Regina", "Aleksej", "Dzhejhun", "Sandzhar", "Vadim", "Ibrahim", "Ernest", "Muhsin", "Azat", "Damir", "Niyaz", "Il'dar", "Ala-Еddin", "Kseniya", "Matvej", "Aretm", "Ernest", "Il'yas", "Il'sur", "Ibragim", "Adeliya", "Ruslan", "Andrej", "Il'ya", "Al'fred", "Anastasiya", "Veronika", "Alina", "Haosyuan'", "Dzhengizkhan Emil'", "El'za", "Nikita", "Rustamdzhon", "Kirill", "Rustem", "Adel'", "Bulat", "Bulat", "Otabek", "Emil'", "Anna", "Daniil", "Pavel", "Karim", "Maksim", "Magamed", "Artyom", "Kirill", "Timofej", "Valerij", "Kamila", "Nikita", "Emin", "Taliya", "Artem", "Arkadij", "Askar", "Dmitrij", "Bulat", "Azat", "Edgar", "Il'naz", "Anastasiya", "Ramis", "Vadim", "Alsu", "Dmitrij", "Emil'", "Aliya", "Niyaz", "Rimma", "Sergej", "Alina", "Almas", "Artem", "Polina", "Azat", "Isabek", "Diana", "Azaliya", "Ruslan", "Regina", "Dina", "Selim", "Nikita", "Kamilla", "Al'bert", "Dinis", "Alsu", "Alsu", "Kirill", "Rodion", "Еvgenij", "Nikita", "Danil", "Amir", "Emil'", "Maksim", "Bogdan", "Еgor", "Sergej", "Robert", "Roman", "Il'shat", "Amirhan", "Marsel'", "Stanislav", "Radimir", "YUliya", "Nikita", "Izida", "El'vina", "Almaz", "Gul'naz", "Bogdan", "Kamil'", "Danis", "Viktoriya", "Vladislav", "Aleksandr", "Nikita", "Iskander", "Daniyar", "Ajnur", "Aleksej", "Mihail", "Еgor", "Il'naz", "Alina"]
surnames = ["Arhipov", "Gilyazov", "Grigor'ev", "Dzhunushaliev", "Еfimova", "Zakirov", "Indienkova", "Kvasnikov", "Malyshkin", "Minahmetova", "Mukiev", "Mustafina", "Orlov", "Palutin", "Podlevskih", "Rahimov", "Salahov", "Sattarov", "Solov'ev", "Fedorova", "Hamidullina", "CHegodaev", "CHemkin", "SHapiro", "SHarafeev", "SHamardanov", "Aver'yanova", "Askarova", "Bady", "Bekmuratov", "Budnikov", "Gabdrahmanov", "Gabdrahmanov", "Gabdullina", "Galimova", "Goncharenko", "Dmitriev", "Zagidullin ", "Ziyatdinov", "Kadyrov", "Kazakov", "Kalashkin", "Miroshihina", "Muhamed'yanov", "Muhutdinova", "Pashin", "Petrov", "Plotnikov", "Primachenko ", "Sagdeev", "Sirazetdinov", "Sultanov", "Hajbullin", "Hamidullin", "SHakirova", "SHamsutdinov", "SHirokov", "Abdrashitova", "Arifullin", "Gil'mullina", "Gusinnikov", "Еlanskaya", "Zapadnov", "Ilalov", "Kilin", "Leont'ev", "Mazitov", "Mirzayanova", "Nizamov", "Ozbayan", "Haliullin", "Zabirov S.", "Abdullin", "Apsadikov", "Ahmetov", "Blinov", "Bogacheva", "Bogomolov", "Buzanov", "Valinurova", "Vdovinov", "Garieva", "Gatin", "Gatin", "Gimazov", "Gordeev", "Grishin", "Еgorova", "Еlin", "Zajnullin", "Zakirov", "Isaichkin", "Karimova", "Karimullin", "Kon'kov", "Korchenov", "Manahov", "Mannapov", "Miheev", "Mokshin", "Murzina", "Musin", "Muhametov", "Ponomarev", "Potapov", "Prokop'ev", "Rahimov", "Ryabov", "Sajdashev", "Sakaev", "Salimov", "Safin", "Soldatov", "Syunyakov", "Faskhutdinov", "Hajrullina", "Hisamov", "SHajdullin", "SHakurov", "SHigabutdinov", "SHigapov", "YAkubenko", "YAmanaev", "Azin", "Alikilichova", "Valitov", "Groshev", "Еnikeeva", "Еrmakov", "Ibragimova", "Kalinina", "Mel'nikova", "Minyukov", "Nasybullin", "Nafikov", "Hakimov", "Hasanov", "CHerbaeva", "Berendakova", "Bikmullin", "ZHeleznova", "Zagidullin", "Malov", "Samigullin", "Hasanov", "Dingizbaev", "Agleev", "Akramova", "Ahmatyanov", "Ahmedov", "Ayubov", "Ayupov", "Baryshan", "Gareev ", "Gench", "Valiullin", "Gabdulhakov", "Ganeev", "Davlet'yarov", "Duak", "Еdkova", "Kazancev", "Maksimov", "Migranov", "Mustaev", "Muhamethanov", "Muhtarov", "Nazipova", "Nazirov", "Naumov", "Pravdivcev", "Safiullin", "Smyshlyaeva", "Sockova", "Suhova", "Syuj", "Sanlyer ", "Timergalieva", "Treskov", "Usmonov", "Ushakov ", "Habibrahmanov", "Hadiev", "Haziev", "Hajbullin", "Hamdamov", "Harisov", "Hishchenko", "CHekanin  ", "CHeremisin", "SHarafutdinov ", "SHumilov", "Halilov ", "Ivanov", "Kononov", "Mironchuk", "Myrzin", "Hammatova", "CHernigov", "Aliev", "Arsembekova", "Artem'ev", "Asanov", "Ahmetov", "Belyakov", "Bilalov", "Valiev", "Gataullin", "Gil'mutdinov", "Gribanova", "Gubajdullin", "Gur'yanov", "Davletgareeva", "Danilov", "Zamaldinov", "Ziangirova", "Muhitov", "Nurieva", "Ryzhakov", "Saetova", "Sajfutdinov", "Semakin", "Senyukova", "Sultanov", "Uezbaev", "Fedotova", "Hismatova", "SHagaliev", "SHakirova", "SHafeeva", "Erdogan", "Afanas'ev", "Bulanova", "Vagmanov", "Gabdrashitov", "Giniyatullina", "Gubaeva", "Korolev", "Kubyshkin", "Kuz'min", "Luzhbin", "Malyshev", "Mardanov", "Mubarakov", "Myalicin", "Soshnikov", "Stroev", "SHabel'nik", "SHamsiev", "SHurkin", "Gataullin", "Gizzatullin", "Gimadiev", "Lavrent'ev", "Mamedov", "Mihajlova", "Surkov", "Hayaleeva", "SHajdullina", "SHangareev", "Amirhanova", "Bukarev", "Gatin", "Gil'fanov", "Gorskaya", "Konstantinov", "Kochedykov", "Levchenko", "Musin", "Sadykov", "Samigulov ", "Strelov", "Schastlivcev", "Fineev", "SHarifullin", "SHaronova"]
groups = ["11-801", "11-802", "11-803", "11-804", "11-805", "11-806", "11-807", "11-808", "11-809", "11-810"]
subjects = ["Algebra", "Matanaliz", "Diskretnaya matematika", "Informatika", "Algoritmy i struktury dannyh",
            "Vvedenie v proektnuyu deyatel'nost'", "Russkij yazyk i kul'tura rechi"]
st_groups = ["11-808", "11-809", "11-809", "11-808", "11-811", "11-809", "11-809", "11-810", "11-809", "11-808", "11-808", "11-808", "11-808", "11-809", "11-808", "11-808", "11-808", "11-809", "11-808", "11-809", "11-809", "11-808", "11-810", "11-810", "11-808", "11-808", "11-801", "11-807", "11-810", "11-811", "11-804", "11-809", "11-806", "11-809", "11-808", "11-809", "11-805", "11-811", "11-804", "11-805", "11-809", "11-810", "11-810", "11-810", "11-805", "11-801", "11-811", "11-808", "11-808", "11-808", "11-811", "11-810", "11-810", "11-808", "11-806", "11-810", "11-810", "11-807", "11-804", "11-807", "11-810", "11-801", "11-806", "11-806", "11-801", "11-801", "11-804", "11-807", "11-805", "11-809", "11-808", "11-803", "11-806", "11-803", "11-805", "11-802", "11-802", "11-803", "11-801", "11-802", "11-802", "11-806", "11-802", "11-805", "11-805", "11-802", "11-805", "11-804", "11-807", "11-803", "11-802", "11-802", "11-807", "11-801", "11-805", "11-806", "11-801", "11-803", "11-803", "11-806", "11-802", "11-804", "11-803", "11-807", "11-807", "11-806", "11-802", "11-803", "11-802", "11-802", "11-802", "11-803", "11-807", "11-806", "11-802", "11-802", "11-802", "11-803", "11-805", "11-803", "11-803", "11-802", "11-802", "11-803", "11-810", "11-804", "11-801", "11-804", "11-803", "11-801", "11-806", "11-804", "11-809", "11-802", "11-805", "11-809", "11-805", "11-804", "11-801", "11-808", "11-804", "11-810", "11-805", "11-804", "11-804", "11-808", "11-803", "11-809", "11-811", "11-811", "11-806", "11-811", "11-810", "11-811", "11-806", "11-803", "11-807", "11-808", "11-811", "11-801", "11-811", "11-811", "11-810", "11-809", "11-809", "11-811", "11-806", "11-804", "11-803", "11-806", "11-810", "11-803", "11-802", "11-810", "11-811", "11-811", "11-806", "11-809", "11-811", "11-801", "11-811", "11-806", "11-806", "11-808", "11-811", "11-805", "11-810", "11-811", "11-809", "11-804", "11-801", "11-811", "11-805", "11-809", "11-803", "11-810", "11-810", "11-806", "11-805", "11-804", "11-803", "11-806", "11-808", "11-807", "11-807", "11-807", "11-805", "11-805", "11-803", "11-805", "11-804", "11-801", "11-802", "11-803", "11-802", "11-806", "11-802", "11-801", "11-801", "11-807", "11-811", "11-804", "11-807", "11-811", "11-801", "11-811", "11-806", "11-802", "11-803", "11-811 ", "11-805", "11-805", "11-809", "11-808", "11-807", "11-810", "11-807", "11-801", "11-803", "11-811", "11-811", "11-806", "11-804", "11-805", "11-804", "11-807", "11-811", "11-809", "11-801", "11-807", "11-809", "11-810", "11-807", "11-805", "11-806", "11-806", "11-804", "11-804", "11-802", "11-807", "11-801", "11-805", "11-807", "11-801", "11-810", "11-801", "11-803", "11-804", "11-804", "11-807", "11-807", "11-804", "11-801", "11-801", "11-803"]
ress = ["stepik", "youtube", "matprofi"]
maxSem = 6
print("started generating groups")
for gr in groups:
    g = Group(name=gr)
    g.save()
print("groups generated")
print("started generating subjects")
for sb in subjects:
    s = Subject(name=sb)
    s.save()
print("subjects generated")
print("started generating res")
for re in ress:
    r = AdditionalEduResource(name=re, url="somesite.com")
    r.save()
i = 0
print("res generated")
print("started generating users")
while i < len(surnames):
    user = User.objects.create_user(username=surnames[i]+str(i), password=surnames[i]+surnames[i])
    user.save()
    i+=1
print("users generated")
print("started generating students")
i = 0
while i < len(names):
    stud = Student(name=names[i], surname=surnames[i],
                   group=Group.objects.filter(name=st_groups[i])[0],
                   user=User.objects.all()[i])
    stud.save()
    i+=1
print("students generated")
print("started generating resToStud")
i = 0
while i < len(names):
    rts = ResourceToStudent(student=Student.objects.all()[i],
                            resource=AdditionalEduResource.objects.all()[i%len(ress)])
    rts.save()
    i+=1
print("resToStudGenerated")
print("started generating PointLists")
i = 0
while i < maxSem:
    for stud in Student.objects.all():
        for sub in Subject.objects.all():
            pl = PointList(student=stud, subject=sub, semester=i, point=50+random.random()*50)
            pl.save()
    i+=1
print("PointLists generated")
print("started generating lessons")
for gr in Group.objects.all():
    for sb in Subject.objects.all():
        ls = Lesson(group=gr, subject=sb, total=random.randint(20, 50),
                    passed=random.randint(0, 50))
        ls.save()
print("lessons generated")