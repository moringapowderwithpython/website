from flask import Flask, request
import random
import os

app = Flask(__name__)

# --- 1. ANA SAYFA (ARILAR DOĞRU YERLERİNE YERLEŞTİRİLDİ VE KORUNDU) ---
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
            
            /* Orijinal Arıların Boyut ve Uçuş Ayarları */
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
            
            <img src="data:image/jpeg;base64,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" class="ari-stil" alt="Tadpole Bee">
            
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" class="logo-python" alt="Python">
            
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/lua/lua-original.svg" class="logo-lua" alt="Lua">
            
            <img src="data:image/png;base64,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" class="ari-stil" alt="Buoyant Bee">
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

# --- 3. GİZLİ ODA (RESİM VE TİKTOK BUTONU KORUNDU) ---
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
