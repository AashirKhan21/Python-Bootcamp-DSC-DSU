#A function that will print lyrics of given song with 1 second delay between each line.
#Use time.sleep()
#Use split() function of string

#So here we import time library inorder to get time 
import time

song = """   Tasveer By Asim Azhar   ,
    Chahein Deed Tere Naino Ki Adat Bure,
    Chahein Deed Tere Naino Ki Adat Bure,
    Tum The Wo Ajnabi Thay Samny Lapata,
    Jitna Milte Gaiy Hute Gaiy Tum Juda,
    Akhiyoun Ne Khincheen Koi Aur Tasveer Tere,
    Ranjheya Bholta Hai Aur Koi Heer Tere,
    Akhiyoun Ne Khincheen Koi Aur Tasveer Tere,
    Ranjheya Bholta Hai Aur Koi Heer Tere,
    Dard Ki Jheel Ka Paani Wo Kia Pee Lia,
    Jab Se Tera Nahi Dil Kesi Ka Nahi Raha,
    Palkain Chou Ke Gira Aanou Wo Mera,
    Bichara U Aansou Mera Lamha Ruk Wo Gaiya,
    Jis Pal Tha Wo Rubaru Dhouka Dil Tou Hua,
    Lagta Tha Tu Hubahu Akhiyoun Ne Khincheen Koi,
    Aur Tasveer Tere Ranjheya Bholta Hai,
    Aur Koi Heer Tere Dard Ki Jheel Ka,
    Paani Wo Kia Pee Lia Jab Se Tera Nahi,
    Dil Na Kisi Ka Raha Tune Zor Se Dharkaya Hai,
    Dil Aankhon Me Bhar Aya Hai Apna Pata Gum Kar Baithe,
    Dil Ne Bhatkaya Hai The Samne Lapata,
    Jitna Milte Gaiy Hute Gaiy Tum Juda,
    Dard Ki Jheel Ka Paani Wo Kia Pee Lia,
    Jab Se Tera Nahi Dil Na Kisi Ka Rah
    """
x = song.split(",")

for elements in x:
    time.sleep(1.2)
    print(elements)
