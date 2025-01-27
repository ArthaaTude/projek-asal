import random
while True:
    nama = (input("Nama Anda:").upper())
    
    if nama.isdigit():
        print("Tidak Boleh Angka")
    else:   
        if not nama.isalpha():
            print("Maaf, Nama Tidak Valid") 
        elif len(nama) >= 6:
            print("Lebih Dari 6")
            hasil_nama = len(nama)
            print("Jumblah Nama kamu:",hasil_nama)
        else:
            jumlah_nama = len(nama)
            print("Jumblah Nama Anda",jumlah_nama)
            print("Perhatikan Ini Di Mana Hewan Ini Sembunyi:")
            bentuk = "|__|"
            hasil = [bentuk] * 4

            hasil[1] = "-__-"
            print(hasil)
            kesalahan = 0
            while True:
                try:
                    nomer = int(input("Nomer:"))
                    nomer_acak = random.randint(1,7)
                    if nomer <= 0:
                        print("Tidak Ada")
                    elif nomer >= 8:
                        print("Lebih Dari 7")
                    else:
                        if nomer == nomer_acak:
                            print("Benar")
                            print("Kesalahan Anda:",kesalahan)
                            import pygame
                            import sys
                            
                            pygame.init()
                            
                            lebar = 800
                            panjang = 800
                            tampilan = pygame.display.set_mode((lebar,panjang))
                            pygame.display.set_caption("Tebak Nomer")
                            
                            skor = 0
                            font = pygame.font.Font(None,30)
                            red =  (255, 0, 0)
                            blue = (0, 0, 255)
                            
                            kotak_jatuh_y = 50
                            kotak_jatuh_x = 50
                            kotak_keatas_y = 50
                            kotak_keatas_x = 50
                            
                            run = True
                            while run:
                                tampilan.fill((255,255,255))
                                for a in pygame.event.get():
                                    if a.type == pygame.QUIT:
                                        print("Sudah Keluar")
                                        run = False
                                    elif a.type == pygame.KEYDOWN:
                                        run = False
                                        print("Sudah Keluar Pencet Tombol")
                                kotak_jatuh_y += 1
                                if kotak_jatuh_y > panjang:
                                    kotak_jatuh_y = 50   
                                    kotak_jatuh_x = random.randint(0,panjang - 40)
                                kotak_keatas_y -= 1
                                if kotak_keatas_y < - 40:
                                    kotak_keatas_y = panjang
                                    kotak_keatas_x = random.randint(0,panjang - 40)     
                                skor += 1
                                pygame.draw.rect(tampilan,blue,(kotak_jatuh_x,kotak_jatuh_y,50,50))
                                pygame.draw.rect(tampilan,blue,(kotak_keatas_x,kotak_keatas_y,50,50))
                                text_nama = pygame.font.Font(None,50).render(f"Selamat Kamu Menang:{nama}",True,(0,0,0))
                                text_kesalahan = pygame.font.Font(None,23).render(f"Kesalahan Kamu:{kesalahan}",True,red)
                                text_skor = font.render(f"skor:{skor}",True,blue)
                                tampilan.blit(text_nama,(lebar // 5,panjang // 2))
                                tampilan.blit(text_kesalahan,(10,28))
                                tampilan.blit(text_skor,(10,10))
                                pygame.display.update()      
                            pygame.quit()
                            sys.exit()
                        else:
                            kesalahan += 1
                            print("Salah Berada Di Nomer",nomer_acak)       
                except ValueError:
                    print("Hanya Angka")