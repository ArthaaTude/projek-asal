print("Bermain Game")
while True:
    try:
        umur =int(input("umur:"))
        
        if umur <= 0:
            print(umur,"tidak ada!!!")
        elif umur <= 17:
            print(umur,"tidak boleh")
            break
        elif umur <= 100:
            nama = (input("nama:"))
            
            if not nama.isalpha():
                print("tidak boleh")
            else:
                import pygame
                import sys
                
                pygame.init()
                
                lebar = 800
                panjang = 600
                tampilkan_layar = pygame.display.set_mode((lebar,panjang))
                pygame.display.set_caption("Game")
                
                warna_putih = (255,255,255)
                warna_hitam  = (0,0,0)
                
                kotak_y = 50
                kotak_x = 50
                x = (kotak_x)
                y = (kotak_y)
                kecepatan = 10
                
                jalankan =  True
                while jalankan:
                    pygame.time.delay(10)
                    for a in pygame.event.get():
                        if a.type == pygame.QUIT:
                            print("keluar")
                            jalankan = False
                    kunci = pygame.key.get_pressed()
                    if kunci[pygame.K_LEFT] and kotak_x > 0:
                        kotak_x -= kecepatan 
                    if kunci[pygame.K_RIGHT]:
                        kotak_x += kecepatan
                    if kunci[pygame.K_DOWN]:
                        kotak_y += kecepatan
                    if kunci[pygame.K_UP] and kotak_y > 0:
                        kotak_y -= kecepatan                       
                    pygame.draw.rect(tampilkan_layar,warna_hitam,(kotak_x,kotak_y,x,y))
                    pygame.display.flip()
                    pygame.display.update()
                    tampilkan_layar.fill(warna_putih)
                pygame.quit()
                sys.exit()          
        else:
            print("lebih")
    except ValueError:
        print("anya angka!!!")