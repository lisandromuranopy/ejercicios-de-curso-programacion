personaje_jugador = {"nombre": "Guerrero Valiente", "hp": 100, "ataque": 15}
personaje_enemigo = {"nombre": "Orco Feroz", "hp": 80, "ataque": 10}
def ejecutar_ataque(atacante, defensor):
  nombre_atacante = atacante.get("nombre")
  nombre_defensor = defensor.get("nombre")
  daño_por_ataque = atacante.get("ataque")
  defensa_por_ataque = defensor.get("hp")
  restar_hp = defensa_por_ataque - daño_por_ataque
  return (
    f"el {nombre_atacante} ataca al {nombre_defensor} "
    f"y le causa {daño_por_ataque} de daño, al {nombre_defensor} le queda {restar_hp} de hp")
def iniciar_batalla(jugador, enemigo):
  while jugador["hp"] > 0 or enemigo["hp"] > 0:
    turno_jugador = ejecutar_ataque(jugador, enemigo)
    turno_enemigo = ejecutar_ataque(enemigo, jugador)
  if jugador["hp"] > 0:
    ganador = jugador
    return f" el ganador es {ganador}"
  else:
    ganador = enemigo
    return f" el ganador es {ganador}"
iniciar_batalla(personaje_jugador,personaje_enemigo)
