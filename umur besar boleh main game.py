while True:
    try:
        umur = int(input("umur:"))
        
        if umur <= 0:
            print(umur,"gagal")
        elif umur <= 17:
            print("bocil")
        elif umur <= 1000:
            nama = (input("nama pertama:"))
            if not nama.isalpha():
                print("gagal")
            else:
                nama_kedua = (input("nama kedua:"))
                if not nama.isalpha():
                    print("gagal")
                else:
                    import pygame
                    import random
                    import sys
                    
                    pygame.init()
                    
                    lebar = 800        
                    panjang = 700
                    tampilan = pygame.display.set_mode((lebar,panjang))
                    pygame.display.set_caption("Game")
                    
                    kotak_pertama_y = (lebar - 50) // 2   
                    kotak_pertama_x = (panjang - 50) // 2
                    kotak_kedua_y = (lebar- 50) // 2
                    kotak_kedua_x = (panjang - 50) // 4
                    
                    red = (255, 0, 0)
                    green = (0, 255, 0)
                    blue = (0, 0, 255)
                    
                    kecepatan = 30
                    skor = 0
                    font = pygame.font.Font(None,30)
                    
                    jalankan = True
                    while jalankan:
                        pygame.time.delay(10)
                        for a in pygame.event.get():
                            if a.type == pygame.QUIT:
                                print("Keluar")
                                jalankan = False        
                        kotak_berjalan = pygame.key.get_pressed()
                        if kotak_berjalan[pygame.K_LEFT] and kotak_pertama_x > 0:
                            kotak_pertama_x -= kecepatan
                        if kotak_berjalan[pygame.K_RIGHT] and kotak_pertama_x + 50 < lebar:
                            kotak_pertama_x += kecepatan
                        if kotak_berjalan[pygame.K_DOWN] and kotak_pertama_y + 50 < panjang:
                            kotak_pertama_y += kecepatan
                        if kotak_berjalan[pygame.K_UP] and kotak_pertama_y > 0:
                            kotak_pertama_y -= kecepatan
                        if (kotak_pertama_x < kotak_kedua_x + 50 and kotak_pertama_x + 50 > kotak_kedua_x and
                            kotak_pertama_y < kotak_kedua_y + 50 and kotak_pertama_y + 50 > kotak_kedua_y):    
                            skor += 1
                            kotak_kedua_y = random.randint(0,panjang - 50)                        
                            kotak_kedua_x = random.randint(0,lebar - 50) 
                        tampilan.fill(blue)
                        pygame.draw.rect(tampilan,red,(kotak_pertama_x,kotak_pertama_y,50,50))
                        pygame.draw.rect(tampilan,green,(kotak_kedua_x,kotak_kedua_y,50,50))
                        text = font.render("skor:"+ str(skor),True,red) 
                        tampilan.blit(text,(10,10)) 
                        pygame.display.update()
                    pygame.quit()
                    sys.exit()
        else:
            break
    except ValueError:
        print("hanya angka")      