const canvas = document.getElementById('girasolCanvas');
const ctx = canvas.getContext('2d');
const centerX = canvas.width / 2;
const centerY = canvas.height / 2;

// Función para dibujar un círculo
function drawCircle(x, y, radius, color) {
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, 2 * Math.PI);
    ctx.fillStyle = color;
    ctx.fill();
}

// Función para dibujar los pétalos del girasol
function drawPetals() {
    ctx.strokeStyle = '#FFA216';
    for (let i = 0; i < 16; i++) {
        for (let j = 0; j < 18; j++) {
            ctx.save();
            ctx.translate(centerX, centerY);
            ctx.rotate(i * Math.PI / 8);
            ctx.beginPath();
            ctx.moveTo(0, 0);
            ctx.lineTo(0, -150 + j * 6);
            ctx.stroke();
            ctx.restore();
        }
    }
}

// Función para dibujar el centro del girasol con un corazón
function drawCenter() {
    const goldenAngle = 137.508 * (Math.PI / 180);
    for (let i = 0; i < 140; i++) {
        const r = 4 * Math.sqrt(i);
        const theta = i * goldenAngle;
        const x = centerX + r * Math.cos(theta);
        const y = centerY + r * Math.sin(theta);
        drawCircle(x, y, 2, '#8B4513');
    }
}

// Función para dibujar un corazón en el centro
function drawHeart(x, y) {
    ctx.fillStyle = '#FF0000';
    ctx.beginPath();
    ctx.moveTo(x, y + 5);
    ctx.bezierCurveTo(x, y, x - 10, y - 10, x - 20, y - 10);
    ctx.bezierCurveTo(x - 40, y - 10, x - 40, y + 15, x - 40, y + 15);
    ctx.bezierCurveTo(x - 40, y + 35, x - 20, y + 55, x, y + 75);
    ctx.bezierCurveTo(x + 20, y + 55, x + 40, y + 35, x + 40, y + 15);
    ctx.bezierCurveTo(x + 40, y + 15, x + 40, y - 10, x + 20, y - 10);
    ctx.bezierCurveTo(x + 10, y - 10, x, y, x, y + 5);
    ctx.closePath();
    ctx.fill();
}

// Función para animar el dibujo del girasol
function animateSunflower() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPetals();
    drawCenter();
    drawHeart(centerX, centerY);
}

animateSunflower();
