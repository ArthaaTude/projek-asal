nama = (input("masukkan nama kamu:"))
selesai = True
print("-------------------Perulangan-------------------------")
print("-------------------Main Game--------------------------")
print("-------------------Buat Text--------------------------")
print("-------------------Buat Simbol-----------------------")
while selesai:
    text = (input("text:"))
    if text == "keluar":
        break
    elif text =="bantu saya":
        print("ada yang bisa di bantu")
    elif text =="buat text":
        textnya = (input("masukkan text:"))
        while selesai:
            try:
                nomer = int(input("berapa nomer:"))
                for a in range(1,nomer +1):
                    print(textnya)
                break
            except ValueError:
                print("hanya nomer") 
    elif text =="terima kasih":
        print("sama sama")
    elif text in ["hai","hallo","bisa bantu"]:
        print("ada apa!!!")
    elif text =="buat simbol":
        while selesai:
            simbol = (input("simbolnya:"))
            try:
                nomerbintang = int(input("berapa simbolnya:"))
                for c in range(nomerbintang):
                    for d in range(c):
                        print(simbol,end="")
                        selesai = False
                    print()
            except ValueError:
                print("hanya angka")
    elif text =="main game":
        import pygame
        import sys
        import random
        
        pygame.init()
        
        lebar = 800
        panjang = 800
        tampilan = pygame.display.set_mode((lebar,panjang))
        pygame.display.set_caption("Game")
        
        kotak_y = (panjang - 50) // 1
        kotak_x = (lebar - 50) // 2
        bulat_y = (panjang - 10) // 2
        bulat_x = (lebar - 10) // 2
        kotak_jatuh_y = 40
        kotak_jatuh_x = 40
        kecepatan_kotak = 10
        skor = 0
        font = pygame.font.Font(None,30)
        game_over = False
        
        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        yellow = (255, 255, 0)
        
        run = True
        while run:
            pygame.time.delay(10)
            tampilan.fill(blue)
            for a in pygame.event.get():
                if a.type == pygame.QUIT:
                    print("sudah keluar",text)
                    run = False
            bergerak = pygame.key.get_pressed()
            if bergerak[pygame.K_LEFT] and kotak_x > 0:
                kotak_x -= kecepatan_kotak
            if bergerak[pygame.K_RIGHT] and kotak_x + 50 < panjang:
                kotak_x += kecepatan_kotak 
            if bergerak[pygame.K_DOWN] and kotak_y + 50  < lebar:
                kotak_y += kecepatan_kotak 
            if bergerak[pygame.K_UP] and kotak_y > 0:
                kotak_y -= kecepatan_kotak
            if (kotak_x < bulat_x + 50 and kotak_x + 50 > bulat_x 
                and kotak_y < bulat_y + 50 and kotak_y + 50 > bulat_y):    
                skor += 1 
                bulat_x = random.randint(0,panjang - 10)    
                bulat_y = random.randint(0,lebar - 10)
            if (kotak_x < kotak_jatuh_x + 50 and kotak_x + 50 > kotak_jatuh_x 
                and kotak_y < kotak_jatuh_y + 50 and kotak_y + 50 > kotak_jatuh_y):
                game_over = True           
            kotak_jatuh_y += 1
            if kotak_jatuh_y > panjang:
                kotak_jatuh_y = 0
                kotak_jatuh_x = random.randint(0,panjang - 40)
            if game_over:
                textt  = pygame.font.Font(None,30).render(f"game over",True,red)
                tampilan.blit(textt,(panjang // 2 - 50,lebar // 3))
                pygame.time.delay(1000)
                run = False
                print("kalah hahahaha",nama)
            pygame.draw.rect(tampilan,red,(kotak_x,kotak_y,50,50))
            pygame.draw.rect(tampilan,yellow,(kotak_jatuh_x,kotak_jatuh_y,40,40))
            pygame.draw.circle(tampilan,white,(bulat_x,bulat_y),5)
            text = font.render(f"skor:{skor}",True,white)
            tampilan.blit(text,(10,10))                  
            pygame.display.update()
        pygame.quit()
        sys.exit()
    elif text =="perulangan":
        try:
            sampai = int(input("Sampai berapa: "))
            umur = int(input("Masukkan umur: "))
    
            if umur <= 0 or umur > sampai:
                print("Gagal")
            elif umur == sampai:
                print("Berhasil")
            else:
                print("Gagal")
        except ValueError:
            print("Masukan harus berupa bilangan bulat.")
    else:
        print("gak ngerti")