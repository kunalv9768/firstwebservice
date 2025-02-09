from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome Screen</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(45deg, #2c3e50, #3498db);
            font-family: Arial, sans-serif;
            overflow: hidden;
        }
        
        .welcome-container {
            text-align: center;
            color: white;
            position: relative;
        }
        
        h1 {
            font-size: 3.5em;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            animation: fadeIn 2s ease-in;
        }
        
        .subtitle {
            font-size: 1.8em;
            margin-bottom: 40px;
            font-style: italic;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
            animation: slideIn 2s ease-out;
        }
        
        .open-button {
            padding: 15px 40px;
            font-size: 1.5em;
            background-color: #e74c3c;
            color: white;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            animation: pulseButton 2s infinite;
        }
        
        .open-button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }

        .heart {
            position: fixed;
            font-size: 20px;
            user-select: none;
            pointer-events: none;
            animation: flyHeart 4s ease-in-out;
            opacity: 0;
        }

        @keyframes flyHeart {
            0% {
                transform: translate(0, 0) rotate(0deg);
                opacity: 1;
            }
            25% {
                opacity: 0.8;
            }
            100% {
                transform: translate(var(--moveX), var(--moveY)) rotate(var(--rotate));
                opacity: 0;
            }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes slideIn {
            from { 
                opacity: 0;
                transform: translateY(30px);
            }
            to { 
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes pulseButton {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="welcome-container">
        <h1>Welcome to my world</h1>
        <div class="subtitle">mine jaan</div>
        <button class="open-button" onclick="createHearts()">Open</button>
    </div>

    <script>
        function createHeart(x, y) {
            const heart = document.createElement('div');
            heart.className = 'heart';
            heart.innerHTML = '❤️';
            heart.style.left = x + 'px';
            heart.style.top = y + 'px';
            
            // Random movement values
            const moveX = (Math.random() - 0.5) * 400;
            const moveY = -Math.random() * 300;
            const rotate = (Math.random() - 0.5) * 360;
            
            heart.style.setProperty('--moveX', moveX + 'px');
            heart.style.setProperty('--moveY', moveY + 'px');
            heart.style.setProperty('--rotate', rotate + 'deg');
            
            document.body.appendChild(heart);
            
            // Remove heart element after animation
            setTimeout(() => {
                heart.remove();
            }, 4000);
        }

        function createHearts() {
            const button = document.querySelector('.open-button');
            const rect = button.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;

            // Create multiple hearts
            for (let i = 0; i < 15; i++) {
                setTimeout(() => {
                    createHeart(
                        centerX + (Math.random() - 0.5) * 60,
                        centerY + (Math.random() - 0.5) * 60
                    );
                }, i * 100);
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
