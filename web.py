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
            
            <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw8NDw8NDQ0NDw0NDw0NDw0NDg8NDQ0NFREWFhURFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMsNygtLisBCgoKDg0OGBAQGisdHh0tLS0tKystLS0tLSstLS0tLSstLSstLSstLS0tKy0tLS0rLS0rLS0tLSsrKysrKystK//AABEIAMEBBQMBIgACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAABQYDBAcCAQj/xAA4EAACAQIEAquFFv8BAQAAAAAAAQIDEQQFITEGEkETIlFhcYEykaEGscHwFBUjQmJyM4KyNJKi/8ve" class="ari-stil" alt="Buoyant Bee">
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
