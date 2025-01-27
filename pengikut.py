import os

selesai = True
orang = ["Christy","Marsha","Zee","Telah Di Ikuti"]
os.system("cls")
while selesai:
    nama = (input("nama:"))
    
    if len(nama) == 15:
        print("Gagal")
    else:
        print("1.christy\n2.marsha\n3.zee")
        while selesai:
            try:
                pilihan = int(input("mengikuti:"))
                
                os.system("cls")
                if pilihan == 1:
                    print(orang[0],orang[-1])
                    pesan = f"{orang[0]} yakin:"
                    oshi = orang[0]
                elif pilihan == 2:
                    print(orang[1],orang[-1])
                    pesan = f"{orang[1]} yakin:"
                    oshi = orang[1]
                elif pilihan == 3:
                    print(orang[2],orang[-1])
                    pesan = f"{orang[2]} yakin:"
                    oshi = orang[2]
                else:
                    print("Pilihan tidak ada")
                while selesai:
                    yakin = input(pesan)
                    if yakin == "y":
                        os.system("cls")
                        import pygame
                        import sys
                        pygame.init()

                        lebar = 800
                        panjang = 800
                        tampilan = pygame.display.set_mode((lebar,panjang))

                        font = pygame.font.Font(None,35)
                        font_1 = pygame.font.Font(None,35)

                        run = True
                        while run:
                            for a in pygame.event.get():
                                if a.type == pygame.QUIT:
                                    run = False
                            text = font.render(f"Anda Mengikuti {oshi} {orang[-1]}",True,((255,255,255)))
                            text_1 = font_1.render(f"nama:{nama}",True,((0, 0, 255)))
                            tampilan.blit(text,(panjang // 4,lebar // 2))
                            tampilan.blit(text_1,(10,10))
                            pygame.display.update()
                        pygame.quit()
                        sys.exit()
                    elif yakin == "t":
                        break
                    else:
                        print("tidak ada")
            except ValueError:
                print("Angka")