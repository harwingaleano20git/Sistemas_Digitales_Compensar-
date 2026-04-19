# Juego en OLED con Arduino 🎮

## Descripción
Este proyecto implementa un juego interactivo en una pantalla OLED usando Arduino UNO. El jugador controla un objeto para evitar obstáculos y acumular puntaje.

## Materiales
- Arduino UNO
- Pantalla OLED SSD1306 (I2C)
- Pulsador
- Protoboard
- Cables

## Conexiones
- VCC → 5V  
- GND → GND  
- SDA → A4  
- SCL → A5  
- Botón → Pin 2 y GND (INPUT_PULLUP)

## Funcionamiento
El jugador se mueve verticalmente usando un botón. Un obstáculo se desplaza horizontalmente y el objetivo es evitar colisiones.

## Librerías usadas
- Adafruit GFX
- Adafruit SSD1306

## Autor
Harwin Galeano
