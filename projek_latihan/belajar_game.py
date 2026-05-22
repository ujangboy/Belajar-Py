import pygame
import sys

# --- INISIALISASI ---
pygame.init()

# Pengaturan Layar dan Waktu
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Belajar Game Loop")
clock = pygame.time.Clock()
FPS = 60 # Kita atur agar loop berjalan 60 kali per detik

# --- VARIABEL GAME STATE ---
# (Ini adalah data yang akan kita "Update" dan "Render")
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5
player_size = 50
player_color = (0, 200, 100) # Warna hijau kebiruan
bg_color = (30, 30, 30)      # Warna latar gelap

# Flag untuk mengontrol siklus game
running = True

print("Game dimulai! Gunakan tombol W, A, S, D atau Panah untuk bergerak.")

# ==========================================
#             THE GAME LOOP
# ==========================================
# Selama 'running' bernilai True, siklus ini akan terus berputar
while running:
    
    # ---------------------------------------------------------
    # FASE 1: EVENT HANDLING (Mengecek Input & Interaksi)
    # ---------------------------------------------------------
    for event in pygame.event.get():
        # Mengecek apakah pemain menekan tombol "X" di ujung jendela
        if event.type == pygame.QUIT:
            running = False
    
    # Menangkap input keyboard yang sedang ditahan (continuous press)
    keys = pygame.key.get_pressed()

    # ---------------------------------------------------------
    # FASE 2: UPDATE STATE (Memperbarui Logika & Data)
    # ---------------------------------------------------------
    # Memperbarui posisi karakter (X dan Y) berdasarkan input dari Fase 1
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += player_speed

    # Mencegah karakter keluar dari batas layar (Logika dasar)
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    # ---------------------------------------------------------
    # FASE 3: RENDER / DRAW (Menggambar Ulang ke Layar)
    # ---------------------------------------------------------
    # a. Bersihkan layar dari frame sebelumnya (Wajib!)
    # Jika tidak dibersihkan, pergerakan karakter akan meninggalkan "jejak"
    screen.fill(bg_color)

    # b. Gambar ulang state terbaru (Karakter kita di posisi yang baru)
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # c. Tampilkan hasil gambaran dari memory (backbuffer) ke monitor pemain
    pygame.display.flip()

    # ---------------------------------------------------------
    # KONTROL WAKTU (Framerate)
    # ---------------------------------------------------------
    # Menahan loop agar tidak berjalan lebih cepat dari 60 Frame Per Second
    clock.tick(FPS)

# --- CLEANUP ---
# Jika loop selesai (running = False), matikan mesin gamenya
pygame.quit()
sys.exit()