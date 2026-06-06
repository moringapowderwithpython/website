from flask import Flask, request
import random
import os

app = Flask(__name__)

# --- 1. ANA SAYFA (ARILAR SIFIRDAN CSS İLE ÇİZİLDİ, ASLA KIRILMAZ!) ---
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
                50% { transform: translateY(-18px); }
                100% { transform: translateY(0px); }
            }
            @keyframes kanatÇırp {
                0% { transform: scaleY(1); }
                50% { transform: scaleY(0.3); }
                100% { transform: scaleY(1); }
            }
            
            .logo-python {
                width: 105px;
                animation: dansPython 3s ease-in-out infinite;
            }
            .logo-lua {
                width: 105px;
                animation: dansLua 2.5s ease-in-out infinite;
            }
            
            /* --- SIFIRDAN CSS ARILARIN ORTAK TABANI --- */
            .ari-konteyner {
                display: inline-block;
                position: relative;
                width: 120px;
                height: 100px;
                animation: ucusAri 3.5s ease-in-out infinite;
            }
            .ari-govde {
                width: 120px;
                height: 90px;
                border-radius: 12px;
                position: relative;
                box-shadow: 0 10px 20px rgba(0,0,0,0.5);
                overflow: hidden;
                border: 2px solid rgba(255,255,255,0.1);
            }
            .ari-goz {
                position: absolute;
                width: 14px;
                height: 14px;
                background-color: #000;
                border-radius: 50%;
                top: 25px;
            }
            .ari-goz-ici {
                position: absolute;
                width: 5px;
                height: 5px;
                background-color: #fff;
                border-radius: 50%;
                top: 2px;
                left: 2px;
            }
            .ari-kanat-sol {
                position: absolute;
                width: 35px;
                height: 20px;
                background-color: rgba(255, 255, 255, 0.7);
                border-radius: 50% 50% 0 0;
                top: -15px;
                left: 25px;
                transform-origin: bottom;
                animation: kanatÇırp 0.15s linear infinite;
            }
            .ari-kanat-sag {
                position: absolute;
                width: 35px;
                height: 20px;
                background-color: rgba(255, 255, 255, 0.7);
                border-radius: 50% 50% 0 0;
                top: -15px;
                right: 25px;
                transform-origin: bottom;
                animation: kanatÇırp 0.15s linear infinite;
            }

            /* --- TADPOLE BEE ÖZELLEŞTİRME (Mavi/Yeşil Kurbağa Temalı) --- */
            .tadpole-govde {
                background: linear-gradient(135deg, #1e3a8a 0%, #0d1b2a 100%);
            }
            .tadpole-cizgi {
                position: absolute;
                width: 25px;
                height: 100%;
                background-color: #10b981; /* Kurbağa Yeşili Çizgiler */
                left: 45px;
                opacity: 0.8;
            }
            .tadpole-detay {
                position: absolute;
                width: 16px;
                height: 16px;
                background-color: #34d399;
                border-radius: 4px;
                bottom: 15px;
                right: 20px;
            }

            /* --- BUOYANT BEE ÖZELLEŞTİRME (Açık Mavi/Balon Temalı) --- */
            .buoyant-govde {
                background: linear-gradient(135deg, #0ea5e9 0%, #0369a1 100%);
            }
            .buoyant-cizgi {
                position: absolute;
                width: 25px;
                height: 100%;
                background-color: #bae6fd; /* Açık Mavi Çizgiler */
                left: 45px;
                opacity: 0.7;
            }
            .buoyant-balon {
                position: absolute;
                width: 18px;
                height: 18px;
                background-color: #f43f5e; /* Pembe Balon Detayı */
                border-radius: 50%;
                top: 15px;
                right: 15px;
            }

            /* Alt Kısımdaki Sinsi Buton */
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
        </style>

        <h1>moringa'nın python sitesi 🐍</h1>
        
        <div style="display: flex; justify-content: center; align-items: center; gap: 160px; margin-top: 60px; flex-wrap: wrap; padding: 0 40px;">
            
            <div class="ari-konteyner" title="Tadpole Bee">
                <div class="ari-kanat-sol"></div><div class="ari-kanat-sag"></div>
                <div class="ari-govde tadpole-govde">
                    <div class="tadpole-cizgi"></div>
                    <div class="ari-goz" style="left: 15px;"><div class="ari-goz-ici"></div></div>
                    <div class="ari-goz" style="right: 15px;"><div class="ari-goz-ici"></div></div>
                    <div class="tadpole-detay"></div>
                </div>
                <div style="font-size: 12px; margin-top: 8px; color: #a7f3d0; font-weight: bold;">Tadpole Bee</div>
            </div>
            
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" class="logo-python" alt="Python">
            
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/lua/lua-original.svg" class="logo-lua" alt="Lua">
            
            <div class="ari-konteyner" title="Buoyant Bee">
                <div class="ari-kanat-sol"></div><div class="ari-kanat-sag"></div>
                <div class="ari-govde buoyant-govde">
                    <div class="buoyant-cizgi"></div>
                    <div class="ari-goz" style="left: 15px;"><div class="ari-goz-ici"></div></div>
                    <div class="ari-goz" style="right: 15px;"><div class="ari-goz-ici"></div></div>
                    <div class="buoyant-balon"></div>
                </div>
                <div style="font-size: 12px; margin-top: 8px; color: #bae6fd; font-weight: bold;">Buoyant Bee</div>
            </div>

        </div>

        <div class="butonlar">
            <br>
            <a href="/flappy"><button>Flappy Bird Oyna 🐦</button></a>
            <a href="/oyun"><button>Sayı Tahmin Oyunu 🎮</button></a>
        </div>

        <a href="/gizli-oda" class="gizli-buton">🚪 Gizli Giriş</a>
    </body>
    """

# --- 2. SAYI TAHMİN OYUNU ---
@app.route("/oyun", methods=["GET", "POST"])
def oyun():
    return """
    <body style="background-color: #0f172a; color: white; text-align: center; padding-top: 50px;">
        <h1>Sayı Tahmin</h1>
        <p>1 ile 50 arasında bir sayı tahmin et!</p>
        <form method="POST"><input type="number" name="tahmin"><button type="submit">Tahmin Et</button></form>
        <br><a href="/" style="color:white;">Ana Sayfa</a>
    </body>
    """

# --- 3. GİZLİ ODA ---
@app.route("/gizli-oda")
def gizli_oda():
    return """
    <body style="background-color: #312e81; color: white; text-align: center; padding-top: 50px;">
        <h1>Gizli Odaya Hoş Geldin! 🏆</h1>
        <img src="https://i.ibb.co/Zp6xv1Bs/image.png" style="width: 200px; border-radius: 50%; border: 5px solid white;">
        <br><br>
        <a href="https://www.tiktok.com/@rz4uy">
            <img src="https://resimlink.com/F7NBK0UuOfI" style="width: 120px; height: 120px; cursor: pointer;">
        </a>
        <br><br><a href="/" style="color:white;">Ana Sayfa</a>
    </body>
    """

# --- 4. FLAPPY BIRD ---
@app.route("/flappy")
def flappy():
    return """
    <body style="background-color: #222; text-align: center; padding-top: 20px;">
        <h2 style="color: white;">Flappy Bird 🐦</h2>
        <canvas id="canvas" width="320" height="480" style="background-color: #70c5ce; border: 4px solid white;"></canvas>
        <script>
        const canvas = document.getElementById("canvas");
        const ctx = canvas.getContext("2d");
        let y = 150, dy = 0, gravity = 0.25, jump = -5, gameRunning = true, score = 0;
        let pipes = [{x: 320, top: 150}];
        
        function drawBird(x, y) {
            ctx.fillStyle = "yellow"; ctx.fillRect(x, y, 30, 25);
            ctx.fillStyle = "white"; ctx.fillRect(x+15, y+5, 10, 10);
            ctx.fillStyle = "black"; ctx.fillRect(x+20, y+8, 4, 4);
            ctx.fillStyle = "orange"; ctx.fillRect(x+25, y+15, 10, 8);
        }
        
        function draw() {
            if(!gameRunning) return;
            ctx.clearRect(0, 0, 320, 480);
            dy += gravity; y += dy;
            drawBird(50, y);
            ctx.fillStyle = "#73BF2E";
            for(let p of pipes) {
                p.x -= 2;
                ctx.fillRect(p.x, 0, 50, p.top);
                ctx.fillRect(p.x - 5, p.top - 20, 60, 20);
                ctx.fillRect(p.x, p.top + 130, 50, 480);
                ctx.fillRect(p.x - 5, p.top + 130, 60, 20);
                if (50 < p.x + 50 && 50 + 30 > p.x && (y < p.top || y + 25 > p.top + 130)) {
                    gameRunning = false; alert('OYUN BİTTİ! Skor: ' + score);
                }
                if(p.x == 50) score++;
            }
            if(y > 480 || y < 0) gameRunning = false;
            if(pipes[pipes.length-1].x < 150) pipes.push({x: 320, top: Math.random()*200 + 50});
            requestAnimationFrame(draw);
        }
        window.addEventListener("mousedown", () => {if(gameRunning) dy = jump;});
        window.addEventListener("keydown", (e) => { if(e.code === "Space" && gameRunning) dy = jump; });
        draw();
        </script>
        <br><br><a href="/" style="color:white;">Ana Sayfa</a>
    </body>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
