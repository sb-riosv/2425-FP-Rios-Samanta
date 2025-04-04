# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (4 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Machala
        [   # Semana 1
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 95}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 36}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 20}
        ],
      [   # Semana 3
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 25}
        ],
     [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 25}
        ],
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 23}
        ],
      [   # Semana 3
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 23}
        ],
      [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 24}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Machala", "Guayaquil", "Quito", "Cuenca"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")
