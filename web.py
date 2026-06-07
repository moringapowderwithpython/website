from flask import Flask, request, session
import random
import os

app = Flask(__name__)
app.secret_key = "moringa_python_site_ozel_keyi" # Oyun hafızası için şifreleyici

# --- 1. ANA SAYFA (EFSANE ARKA PLAN GÖRSELİ ENTEGRE EDİLDİ) ---
@app.route("/")
def ana_sayfa():
    return """
    <body style="
        background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('https://www.image2url.com/r2/default/images/1780847286056-2c37b288-aa4c-4835-a0e0-655452756c6c.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white; 
        font-family: sans-serif; 
        text-align: center; 
        padding-top: 30px; 
        overflow-x: hidden;
    ">
        
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
            
            /* Tadpole Bee Görsel Ayarları */
            .ari-tadpole {
                width: 135px; 
                height: auto;
                animation: ucusAri 3.5s ease-in-out infinite;
            }

            /* Buoyant Bee Görsel Ayarları */
            .ari-buoyant {
                width: 135px; 
                height: auto;
                animation: ucusAri 3.2s ease-in-out infinite;
            }
            
            .butonlar {
                margin-top: 50px;
            }
            button {
                padding: 15px 25px; 
                margin: 10px; 
                cursor: pointer; 
                font-weight: bold; 
                border-radius: 8px; 
                border: none; 
                background-color: rgba(30, 41, 59, 0.85); /* Arka plan göründüğü için butonları hafif şeffaf yaptık, çok şık durdu! */
                color: white; 
                font-size: 16px;
                transition: 0.2s;
                backdrop-filter: blur(5px);
            }
            button:hover {
                background-color: #38bdf8;
                color: black;
                transform: scale(1.05);
            }
        </style>

        <h1 style="text-shadow: 2px 2px 8px rgba(0,0,0,0.8);">moringa'nın python sitesi 🐍</h1>
        
        <div style="display: flex; justify-content: center; align-items: center; gap: 120px; margin-top: 50px; flex-wrap: wrap; padding: 0 40px;">
            
            <img src="https://www.image2url.com/r2/default/images/1780846534135-ed934fd6-a009-4bde-973f-fc0ebd230ec7.jpg" class="ari-tadpole" alt="Tadpole Bee" style="border-radius: 15px; box-shadow: 0px 4px 15px rgba(0,0,0,0.5);">
            
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" class="logo-python" alt="Python">
            
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/lua/lua-original.svg" class="logo-lua" alt="Lua">
            
            <img src="https://www.image2url.com/r2/default/images/1780843955524-5bf7cf96-7c1c-4cd4-bdbe-8b114691263c.jpg" class="ari-buoyant" alt="Buoyant Bee" style="border-radius: 15px; box-shadow: 0px 4px 15px rgba(0,0,0,0.5);">
        </div>

        <div class="butonlar">
            <br>
            <a href="/flappy"><button>Flappy Bird Oyna 🐦</button></a>
            <a href="/oyun"><button>Sayı Tahmin Oyunu 🎮</button></a>
        </div>

        <a href="/gizli-oda" style="position: fixed; bottom: 10px; right: 10px; padding: 6px 10px; font-size: 11px; background-color: rgba(26, 26, 26, 0.7); color: #ccc; border: 1px solid #444; border-radius: 4px; text-decoration: none; backdrop-filter: blur(3px);">🚪 Gizli Giriş</a>
    </body>
    """

# --- 2. SAYI TAHMİN OYUNU ---
@app.route("/oyun", methods=["GET", "POST"])
def oyun():
    if 'gizy_sayi' not in session: # Minik değişken ismi güvenliği
        session['gizli_sayi'] = random.randint(1, 50)
        session['tahmin_sayisi'] = 0

    mesaj = "1 ile 50 arasında bir sayı tahmin et!"
    if request.method == "POST":
        try:
            tahmin = int(request.form.get("tahmin", 0))
            session['tahmin_sayisi'] += 1
            if tahmin == session['gizli_sayi']:
                mesaj = f"🎉 TEBRİKLER! {session['tahmin_sayisi']}. denemede bildin! Sayı: {session['gizli_sayi']}"
                session.pop('gizli_sayi', None)
            elif tahmin < session['gizli_sayi']:
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

# --- 3. GİZLİ ODA ---
@app.route("/gizli-oda")
def gizli_oda():
    return """
    <body style="background-color: #312e81; color: white; font-family: sans-serif; text-align: center; padding-top: 50px;">
        <h1>Gizli Odaya Hoş Geldin! 🏆</h1>
        <br>
        <img src="https://i.ibb.co/Zp6xv1Bs/image.png" style="width: 200px; border-radius: 50%; border: 5px solid white;">
        <br><br><br>
        
        <a href="https://www.tiktok.com/@rz4uy" target="_blank">
            <img src="https://www.image2url.com/r2/default/images/1780846803888-dcb8074e-a946-4b21-8a9a-92b9eeabca78.jpg" style="width: 120px; height: auto; cursor: pointer; border-radius: 20px; transition: 0.2s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        </a>
        
        <br><br><br>
        <a href="/" style="color: #c7d2fe; text-decoration: none;">← Ana Sayfaya Dön</a>
    </body>
    """

# --- 4. FLAPPY BIRD ---
@app.route("/flappy")
def flappy():
    return """
    <body style="background-color: #222; font-family: sans-serif; text-align: center; padding-top: 20px; margin: 0; overflow: hidden;">
        <h2 style="color: white; margin-bottom: 10px;">Flappy Bird 🐦</h2>
        <canvas id="canvas" width="320" height="480" style="background-color: #70c5ce; border: 4px solid white; border-radius: 8px;"></canvas>
        <br><br>
        <a href="/" style="color: #aaa; text-decoration: none; font-weight: bold;">← Ana Sayfaya Dön</a>

        <script>
        const canvas = document.getElementById("canvas");
        const ctx = canvas.getContext("2d");
        let y = 150, dy = 0, gravity = 0.25, jump = -5.3, gameRunning = true, score = 0;
        let pipes = [{x: 320, top: 150}];

        function drawBird(x, y) {
            ctx.fillStyle = "yellow"; ctx.fillRect(x, y, 30, 25);
            ctx.fillStyle = "white"; ctx.fillRect(x + 16, y + 4, 9, 9);
            ctx.fillStyle = "black"; ctx.fillRect(x + 21, y + 7, 4, 4);
            ctx.fillStyle = "orange"; ctx.fillRect(x + 26, y + 12, 10, 8);
        }

        function draw() {
            if (!gameRunning) return;
            ctx.clearRect(0, 0, 320, 480);
            dy += gravity; y += dy;
            drawBird(50, y);
            ctx.fillStyle = "#73BF2E";
            for (let i = 0; i < pipes.length; i++) {
                let p = pipes[i]; p.x -= 2;
                ctx.fillRect(p.x, 0, 50, p.top);
                ctx.fillRect(p.x, p.top + 130, 50, 480);
                if (50 < p.x + 50 && 50 + 30 > p.x && (y < p.top || y + 25 > p.top + 130)) {
                    gameRunning = false; alert('Oyun Bitti! Skorun: ' + score); location.reload();
                }
                if (p.x === 50) score++;
            }
            if (y > 480 || y < 0) { gameRunning = false; alert('Oyun Bitti! Skorun: ' + score); location.reload(); }
            if (pipes[pipes.length - 1].x < 160) pipes.push({ x: 320, top: Math.floor(Math.random() * 200) + 60 });
            ctx.fillStyle = "white"; ctx.font = "bold 24px sans-serif"; ctx.fillText("Skor: " + score, 15, 35);
            requestAnimationFrame(draw);
        }
        window.addEventListener("mousedown", () => { if (gameRunning) dy = jump; });
        window.addEventListener("keydown", (e) => { if (e.code === "Space" && gameRunning) { e.preventDefault(); dy = jump; } });
        draw();
        </script>
    </body>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
