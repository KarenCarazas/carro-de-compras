<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Formulario</title>
    <h1>
        <center>Curriculum Vitae Form</center>
    </h1>
    <style>
        .btn {
            border-radius: 5px;
            display: inline-block;
            padding: 5px 15px;

        }

        .btn-silver {
            color: white;
            background-color: silver;
        }

        .btn-silver:hover {
            background-color: silver
        }

        .btn-silver:active {
            background-color: silver;
        }
body {
            font-family: Arial;
            background-color: silver;
        }

        form {
            background-color: white;
            color: black;
            font-size: 15px;
            padding: 40px;
            margin: 25px auto;
            width: 300px;
        }

        .field {
            border: solid 1px silver;
            padding: 10px;
        }

        .field:focus {
            border-color: black;
        }

        .center-content {
            text-align: center;
        }
    </style>
</head>

<body>
    <form action="cvforms" method="post">
        <p>Nombres y Apellidos:</p>
        <input class="field" type="text" size="35" required> <br />

        <p>Fecha de nacimiento:</p>
        <input class="field" type="date" required> <br />

        <p>Ocupación:</p>
        <input type="text" class="field" size="35"> <br />

        <p>Teléfono:</p>
        <input type="tel" class="field" size="35" required> <br />

        <p>Correo electrónico:</p>
        <input type="email" class="field" size="35" required> <br />

        <p>Nacionalidad:</p>
        <select class="field" required> <br />
            <option value="0">...</option>
            <option value="1">Perú</option>
            <option value="2">Chile</option>
            <option value="3">Bolivia</option>
            <option value="4">Argentina</option>
        </select>
        <br />

        <p>Nivel de inglés:</p>
        <input type="radio" name="ingles" value="b"> Básico
        <input type="radio" name="ingles" value="i"> Intermedio
        <input type="radio" name="ingles" value="f"> Fluido
        <br />

        <p>Lenguajes de programación:</p>
        <input type="radio" name="leng" value="p"> Python
        <br />
        <input type="radio" name="leng" value="c"> C++
        <br />
        <input type="radio" name="leng" value="j"> Java
        <br />

        <p>Aptitudes:</p>
        <input class="field" list="aptitudes" id="aps" name="aps" required>
        <datalist id="aptitudes">
            <option value="Inteligencia emocional">
            <option value="Espíritu crítico">
            <option value="Trabajo en equipo">
            <option value="Capacidad analítica">
            <option value="Habilidades físicas">
        </datalist>
        <br />

        <p>Habilidades:</p>
        <input type="checkbox" name="casilla" value="l">Liderazgo
        <br>
        <input type="checkbox" name="casilla" value="e">Ética de trabajo
        <br>
        <input type="checkbox" name="casilla" value="c">Capacidad de análisis
        <br>
        <input type="checkbox" name="casilla" value="i">Iniciativa
        <br>
        <input type="checkbox" name="casilla" value="v">Comunicación verbal

        <p>Perfil:</p>
        <textarea class="field" cols="35"></textarea> <br />

        <p class="center-content">
            <input type="submit" class="btn btn-silver" value="Enviar Datos">
        </p>

    </form>
</body>

</html>
