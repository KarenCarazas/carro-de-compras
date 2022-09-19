<!DOCTYPE html>
<html>
<title>Curriculum Vitae</title>

<head>
    <h1>
        <center>Curriculum Vitae Form</center>
    </h1>
</head>
<form action="cv.html" method="post">

    <div class="elem-group"> <label for="name">Nombres y Apellidos</label>
        <br>
        <input type="text" id="name" name="visitor_name" size='40' placeholder="Nombres y apellidos" required> </div>
    <br>

    <div class="elem-group"> <label for="born">Fecha de nacimiento</label>
        <br>
        <input type="date" id="born" name="visitor_born" required> </div>
    <br>

    <div class="elem-group"> <label for="ocupation">Ocupación</label>
        <br>
        <input type="text" id="ocupation" name="visitor_ocupation" placeholder="Ocupacion" required></div>
    <br>

    <div class="elem-group"> <label for="number">Telefono</label>
        <br>
        <input type="tel" id="number" name="visitor_number" placeholder="Numero de telefono" required> </div>
    <br>

    <div class="elem-group"> <label for="mail">Correo electrónico</label>
        <br>
        <input type="email" id="mail" name="visitor_mail" size='25' placeholder="ejemplo@gmail.com" required> </div>
    <br>

    <div class="elem-group"> <label for="nation">Nacionalidad</label>
        <br>
        <select id="nation" name='visitor_nation' required>
        <option value="0">...</option>
        <option value="1">Perú</option>
        <option value="2">Chile</option>
        <option value="3">Bolivia</option>
        <option value="4">Argentina</option>
        </select>
    </div>
    <br>

    <div class="elem-group"> <label for="english">Nivel de inglés</label>
        <required>
            <br>
            <input type="radio" name="bif" value="b" required> Básico
            <input type="radio" name="bif" value="i" required> Intermedio
            <input type="radio" name="bif" value="f" required> Fluido
    </div>
    <br>

    <div class="elem-group"> <label for="program">Lenguajes de programación</label>
        <br>
        <input type="radio" name="python" value="p" required> Python
        <br>
        <input type="radio" name="c++" value="c" required> C++
        <br>
        <input type="radio" name="javascript" value="j" required> JavaScript
    </div>
    <br>

    <div class="elem-group"> <label for="aptituds">Aptitudes</label>
        <br>
        <input list="aptituds" required>
        <datalist id="aptituds">
        <option value="Inteligencia emocional">
        <option value="Creatividad">
        <option value="Trabajo en equipo">
    </datalist>
    </div>
    <br>

    <div class="elem-group"> <label for="ability">Habilidades</label>
        <br>
        <input type="checkbox" name="casilla" required>Liderazgo
        <br>
        <input type="checkbox" name="casilla" required>Ética de trabajo
        <br>
        <input type="checkbox" name="casilla" required>Capacidad de análisis
        <br>
        <input type="checkbox" name="casilla" required>Iniciativa
        <br>
        <input type="checkbox" name="casilla" required>Comunicación verbal
    </div>
    <br>

    <div class="elem-group"> <label for="message">Perfil</label>
        <br>
        <textarea id="message" name="visitor_message" placeholder="Escribe tu mensaje aquí." required></textarea> </div>
    <br>

</html>