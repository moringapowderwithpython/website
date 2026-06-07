from flask import Flask, request
import random
import os

app = Flask(__name__)

# --- 1. ANA SAYFA (ARILAR VE LOGOLAR KUSURSUZ GENİŞ DÜZENDE) ---
@app.route("/")
def ana_sayfa():
    return """
    <body style="background-color: #121212; color: white; font-family: sans-serif; text-align: center; padding-top: 30px; overflow-x: hidden;">
        
        <style>
            @keyframes dansPython {
                0% { transform: translateY(0px) rotate(0deg); }
                50% { transform: translateY(-20px) rotate(5deg); }
                100% { transform: translateY(0px) rotate(0deg); }
            }
            @keyframes dansLua {
                0% { transform: translateY(0px) rotate(0deg); }
                50% { transform: translateY(-25px) rotate(-8deg); }
                100% { transform: translateY(0px) rotate(0deg); }
            }
            @keyframes ucusAri {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-15px); }
                100% { transform: translateY(0px); }
            }
            .logo-python {
                width: 105px;
                animation: dansPython 3s ease-in-out infinite;
            }
            .logo-lua {
                width: 105px;
                animation: dansLua 2.5s ease-in-out infinite;
            }
            
            /* Arıların Boyut ve Uçuş Ayarları */
            .ari-stil {
                width: 125px; 
                height: auto;
                animation: ucusAri 3.5s ease-in-out infinite;
            }
            
            .butonlar {
                margin-top: 50px;
            }
            button {
                padding: 15px; 
                margin: 10px; 
                cursor: pointer; 
                font-weight: bold; 
                border-radius: 8px; 
                border: none; 
                background-color: #1e293b; 
                color: white; 
                transition: 0.2s;
            }
            button:hover {
                background-color: #334155;
                transform: scale(1.05);
            }
            
            /* Sağ Alt Köşedeki Gizli Giriş Butonu */
            .gizli-buton {
                position: fixed;
                bottom: 10px;
                right: 10px;
                padding: 6px 10px;
                font-size: 11px;
                background-color: #1a1a1a; 
                color: #555; 
                border: 1px solid #222;
                border-radius: 4px;
                cursor: pointer;
                text-decoration: none;
                transition: 0.3s;
                font-weight: normal;
            }
            .gizli-buton:hover {
                color: #ff007f; 
                border-color: #ff007f;
                background-color: #26121f;
            }
        </style>

        <h1>moringa'nın python sitesi 🐍</h1>
        
        <div style="display: flex; justify-content: center; align-items: center; gap: 120px; margin-top: 50px; flex-wrap: wrap; padding: 0 40px;">
            
            <img src="https://i.ibb.co/wZ1j8F6/tadpole.png" class="ari-stil" alt="Tadpole Bee">
            
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" class="logo-python" alt="Python">
            
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/lua/lua-original.svg" class="logo-lua" alt="Lua">
            
            <img src="https://www.image2url.com/r2/default/images/1780770391252-e0bd5937-54f6-4110-8d12-ba5bb9c851ae.jpg" class="ari-stil" alt="Buoyant Bee">
        </div>

        <div class="butonlar">
            <br>
            <a href="/flappy"><button>Flappy Bird Oyna 🐦</button></a>
            <a href="/oyun"><button>Sayı Tahmin Oyunu 🎮</button></a>
        </div>

        <a href="/gizli-oda" class="gizli-buton">🚪 Gizli Giriş</a>
    </body>
    """

# --- 2. SAYI TAHMİN OYUNU (TAM SÜRÜM) ---
@app.route("/oyun", methods=["GET", "POST"])
def oyun():
    if 'gizli_sayi' not in session:
        from flask import session
        # Eğer session kullanmak istemiyorsan basit tutalım, her girişte rastgele seçsin ya da statik olsun:
        pass
        
    mesaj = "1 ile 50 arasında bir sayı tahmin et!"
    if request.method == "POST":
        try:
            tahmin = int(request.form.get("tahmin", 0))
            # Basit bir mantık: Her tahminde heyecan olsun diye 25'i bulmaya çalışsınlar veya random üretsin
            if tahmin == 25:
                mesaj = "🎉 TEBRİKLER! Doğru tahmin ettin!"
            elif tahmin < 25:
                mesaj = "📈 Daha BÜYÜK bir sayı dene!"
            else:
                mesaj = "📉 Daha KÜÇÜK bir sayı dene!"
        except:
            mesaj = "Lütfen geçerli bir sayı gir!"

    return f"""
    <body style="background-color: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 50px;">
        <h1>Sayı Tahmin Oyunu 🎮</h1>
        <p style="font-size: 18px; color: #cbd5e1;">{mesaj}</p>
        <form method="POST" style="margin-top: 30px;">
            <input type="number" name="tahmin" style="padding: 10px; font-size: 16px; border-radius: 5px; border: none; width: 150px; text-align: center;" required>
            <br><br>
            <button type="submit" style="padding: 10px 20px; font-weight: bold; background-color: #38bdf8; color: black; border: none; border-radius: 5px; cursor: pointer;">Tahmin Et</button>
        </form>
        <br><br>
        <a href="/" style="color: #94a3b8; text-decoration: none;">← Ana Sayfaya Dön</a>
    </body>
    """

# --- 3. GİZLİ ODA (ORİJİNAL TÜM MEDYALAR DAHİL) ---
@app.route("/gizli-oda")
def gizli_oda():
    return """
    <body style="background-color: #312e81; color: white; font-family: sans-serif; text-align: center; padding-top: 50px;">
        <h1>Gizli Odaya Hoş Geldin! 🏆</h1>
        <p style="color: #eef2f6;">Buraya sadece gerçek geliştiriciler girebilir.</p>
        <br>
        <img src="https://i.ibb.co/Zp6xv1Bs/image.png" style="width: 200px; border-radius: 50%; border: 5px solid white; box-shadow: 0 0 20px rgba(255,255,255,0.3);">
        <br><br><br>
        <a href="https://www.tiktok.com/@rz4uy" target="_blank">
            <img src="https://resimlink.com/F7NBK0UuOfI" style="width: 120px; height: 120px; cursor: pointer; transition: 0.3s; border-radius: 20px;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        </a>
        <br><br><br>
        <a href="/" style="color: #c7d2fe; text-decoration: none;">← Ana Sayfaya Dön</a>
    </body>
    """

# --- 4. FLAPPY BIRD (ORİJİNAL, TAM VE KESİNTİSİZ JAVASCRIPT KODU) ---
@app.route("/flappy")
def flappy():
    return """
    <body style="background-color: #222; font-family: sans-serif; text-align: center; padding-top: 20px; margin: 0; overflow: hidden;">
        <h2 style="color: white; margin-bottom: 10px;">Flappy Bird 🐦</h2>
        <p style="color: #aaa; margin: 0 0 15px 0; font-size: 14px;">Zıplamak için <b>BOŞLUK (SPACE)</b> tuşuna bas veya ekrana <b>TIKLA</b>!</p>
        
        <canvas id="canvas" width="320" height="480" style="background-color: #70c5ce; border: 4px solid white; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); cursor: pointer;"></canvas>
        
        <br><br>
        <a href="/" style="color: #aaa; text-decoration: none; font-weight: bold;">← Ana Sayfaya Dön</a>

        <script>
        const canvas = document.getElementById("canvas");
        const ctx = canvas.getContext("2d");

        // Oyun Değişkenleri
        let y = 150;
        let dy = 0;
        let gravity = 0.25;
        let jump = -5.3;
        let gameRunning = true;
        let score = 0;
        let pipes = [{x: 320, top: 150}];

        // Kuş Çizimi (Klasik Detaylı Flappy Görünümü)
        function drawBird(x, y) {
            ctx.fillStyle = "yellow"; 
            ctx.fillRect(x, y, 30, 25);
            // Gözü
            ctx.fillStyle = "white"; 
            ctx.fillRect(x + 16, y + 4, 9, 9);
            ctx.fillStyle = "black"; 
            ctx.fillRect(x + 21, y + 7, 4, 4);
            // Gagası
            ctx.fillStyle = "orange"; 
            ctx.fillRect(x + 26, y + 12, 10, 8);
            // Kanadı
            ctx.fillStyle = "#d4af37"; 
            ctx.fillRect(x + 4, y + 10, 12, 8);
        }

        // Ana Oyun Döngüsü
        function draw() {
            if (!gameRunning) return;

            // Arka planı temizle
            ctx.clearRect(0, 0, 320, 480);

            // Yerçekimi Fiziği
            dy += gravity;
            y += dy;

            // Kuşu Çiz
            drawBird(50, y);

            // Boruları Çiz ve Hareket Ettir
            ctx.fillStyle = "#73BF2E";
            for (let i = 0; i < pipes.length; i++) {
                let p = pipes[i];
                p.x -= 2; // Boru hızı

                // Üst Boru
                ctx.fillRect(p.x, 0, 50, p.top);
                ctx.fillRect(p.x - 5, p.top - 20, 60, 20); // Boru ağzı

                // Alt Boru (Boşluk: 130px)
                ctx.fillRect(p.x, p.top + 130, 50, 480);
                ctx.fillRect(p.x - 5, p.top + 130, 60, 20); // Boru ağzı

                // Çarpışma Testi (Hitbox Kontrolü)
                if (50 < p.x + 50 && 50 + 30 > p.x && (y < p.top || y + 25 > p.top + 130)) {
                    gameRunning = false;
                    alert('OYUN BİTTİ! \\nSkorun: ' + score + '\\nYeniden başlamak için sayfayı yenile!');
                    location.reload();
                }

                // Skor Ekleme
                if (p.x === 50) {
                    score++;
                }
            }

            // Ekran dışına çıkma kontrolü
            if (y > 480 || y < 0) {
                gameRunning = false;
                alert('OYUN BİTTİ! \\nSkorun: ' + score + '\\nYeniden başlamak için sayfayı yenile!');
                location.reload();
            }

            // Yeni Boru Ekleme Dengesi
            if (pipes[pipes.length - 1].x < 160) {
                pipes.push({
                    x: 320,
                    top: Math.floor(Math.random() * 200) + 60
                });
            }

            // Skor Tablosu Yazısı
            ctx.fillStyle = "white";
            ctx.font = "bold 24px sans-serif";
            ctx.strokeStyle = "black";
            ctx.lineWidth = 4;
            ctx.strokeText("Skor: " + score, 15, 35);
            ctx.fillText("Skor: " + score, 15, 35);

            requestAnimationFrame(draw);
        }

        // Zıplama Tetikleyicileri (Hem Tıklama Hem Boşluk Tuşu)
        window.addEventListener("mousedown", () => {
            if (gameRunning) dy = jump;
        });

        window.addEventListener("keydown", (e) => {
            if (e.code === "Space" && gameRunning) {
                e.preventDefault(); // Sayfanın aşağı kaymasını önler
                dy = jump;
            }
        });

        // Oyunu Başlat
        draw();
        </script>
    </body>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
