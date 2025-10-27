class Paciente:
    orden = 0
    def __init__(self, id, codigo_paciente, nivel_emergencia):
        Paciente.orden += 1
        self.id = id
        self.codigo_paciente = codigo_paciente
        self.nivel_emergencia: int = nivel_emergencia
        self.orden_llegada = Paciente.orden

    def __str__(self):
        return f"{self.id}, {self.orden_llegada}"

