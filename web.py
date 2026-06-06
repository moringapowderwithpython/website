from flask import Flask, request
import random

app = Flask(__name__)

# --- 1. ANA SAYFA ---
@app.route("/")
def ana_sayfa():
    return """
    <body style="background-color: #121212; color: white; font-family: sans-serif; text-align: center; padding-top: 50px;">
        <h1>Yazılımcı Dünyasına Hoş Geldin! ⚡</h1>
        <br>
        <a href="/flappy"><button style="padding: 15px; margin: 10px;">Flappy Bird Oyna 🐦</button></a>
        <a href="/oyun"><button style="padding: 15px; margin: 10px;">Sayı Tahmin Oyunu 🎮</button></a>
        <a href="/gizli-oda"><button style="padding: 15px; margin: 10px;">Gizli Odaya Gir 🚪</button></a>
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

# --- 3. GİZLİ ODA (Kendi resmin ve yeni logon) ---
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
    app.run(host="0.0.0.0", port=5000)
