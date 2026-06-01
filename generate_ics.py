import datetime
import hashlib

# Datos de la rutina planificada (mayo 31 - julio 1, 2026)
seed = {
    '2026-05-31': [('CS50', 'study', '10:00', '13:00'), ('Repaso Facultad', 'study', '13:00', '16:00'), ('Tiempo de ocio libre', 'rest', '16:00', '24:00')],
    '2026-06-01': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Física 1 – Práctica', 'study', '17:00', '20:00'), ('Cocinar y cenar', 'eat', '20:00', '22:00'), ('Prob y Est – Repaso conceptual', 'study', '22:00', '24:00')],
    '2026-06-02': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Repaso previo: Prob y Est', 'study', '17:00', '19:00'), ('Cursada: Prob y Estadística', 'study', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-03': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Repaso previo: Costos', 'study', '17:00', '19:00'), ('Cursada: Costos Industriales', 'study', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-04': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Prob y Est – Parciales viejos', 'study', '17:00', '20:00'), ('Cocinar y cenar', 'eat', '20:00', '22:00'), ('Física 1 – Repaso', 'study', '22:00', '24:00')],
    '2026-06-05': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Repaso previo: Física 1', 'study', '17:00', '19:00'), ('Cursada: Física 1', 'study', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-06': [('Física 1 – Estudio fuerte', 'study', '10:00', '13:00'), ('Prob y Est – Estudio fuerte', 'study', '13:00', '16:00'), ('Tiempo de ocio libre', 'rest', '16:00', '24:00')],
    '2026-06-07': [('CS50', 'study', '10:00', '13:00'), ('Física 1 – Repaso', 'study', '13:00', '14:30'), ('Prob y Est – Repaso', 'study', '14:30', '16:00'), ('Tiempo de ocio libre', 'rest', '16:00', '24:00')],
    '2026-06-08': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Física 1 – Práctica', 'study', '17:00', '20:00'), ('Cocinar y cenar', 'eat', '20:00', '22:00'), ('Prob y Est – Repaso conceptual', 'study', '22:00', '24:00')],
    '2026-06-09': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Repaso previo: Prob y Est', 'study', '17:00', '19:00'), ('Cursada: Prob y Estadística', 'study', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-10': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Repaso previo: Costos', 'study', '17:00', '19:00'), ('Cursada: Costos Industriales', 'study', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-11': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Prob y Est – Parciales viejos', 'study', '17:00', '20:00'), ('Cocinar y cenar', 'eat', '20:00', '22:00'), ('Física 1 – Repaso', 'study', '22:00', '24:00')],
    '2026-06-12': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Repaso previo: Física 1', 'study', '17:00', '19:00'), ('Cursada: Física 1', 'study', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-13': [('Física 1 – Estudio fuerte', 'study', '10:00', '13:00'), ('Prob y Est – Estudio fuerte', 'study', '13:00', '16:00'), ('Tiempo de ocio libre', 'rest', '16:00', '24:00')],
    '2026-06-14': [('CS50', 'study', '10:00', '13:00'), ('Física 1 – Repaso', 'study', '13:00', '14:30'), ('Prob y Est – Repaso', 'study', '14:30', '16:00'), ('Tiempo de ocio libre', 'rest', '16:00', '24:00')],
    '2026-06-15': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('🔥 Prob y Est – INTENSIVO', 'study', '17:00', '20:00'), ('Cocinar y cenar', 'eat', '20:00', '22:00'), ('🔥 Prob y Est – FINAL', 'study', '22:00', '24:00')],
    '2026-06-16': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Repaso último momento', 'study', '17:00', '19:00'), ('📝 PARCIAL: Prob y Est', 'exam', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-17': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Física 1 – Repaso intensivo', 'study', '17:00', '19:00'), ('Cursada: Costos Industriales', 'study', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-18': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('🔥 Física 1 – INTENSIVO', 'study', '17:00', '20:00'), ('Cocinar y cenar', 'eat', '20:00', '22:00'), ('🔥 Física 1 – FINAL', 'study', '22:00', '24:00')],
    '2026-06-19': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Repaso último momento', 'study', '17:00', '19:00'), ('📝 PARCIAL ÚNICO: Física 1', 'exam', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-20': [('Costos – Inicio fase intensiva', 'study', '10:00', '16:00'), ('Tiempo de ocio libre', 'rest', '16:00', '24:00')],
    '2026-06-21': [('CS50', 'study', '10:00', '13:00'), ('Costos – Teoría', 'study', '13:00', '16:00'), ('Tiempo de ocio libre', 'rest', '16:00', '24:00')],
    '2026-06-22': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Costos – Ejercicios', 'study', '17:00', '20:00'), ('Cocinar y cenar', 'eat', '20:00', '22:00'), ('Costos – Teoría', 'study', '22:00', '24:00')],
    '2026-06-23': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Costos – Repaso', 'study', '17:00', '19:00'), ('Cursada: Prob y Estadística', 'study', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-24': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Costos – Repaso previo', 'study', '17:00', '19:00'), ('Cursada: Costos Industriales', 'study', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-25': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Costos – Ejercicios', 'study', '17:00', '20:00'), ('Cocinar y cenar', 'eat', '20:00', '22:00'), ('Costos – Presupuestos', 'study', '22:00', '24:00')],
    '2026-06-26': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Costos – Repaso', 'study', '17:00', '19:00'), ('Cursada: Física 1', 'study', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')],
    '2026-06-27': [('Costos – Simulacro de examen', 'study', '10:00', '16:00'), ('Tiempo de ocio libre', 'rest', '16:00', '24:00')],
    '2026-06-28': [('CS50', 'study', '10:00', '13:00'), ('Costos – Simulacro de examen', 'study', '13:00', '16:00'), ('Tiempo de ocio libre', 'rest', '16:00', '24:00')],
    '2026-06-29': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Costos – Repaso intensivo', 'study', '17:00', '20:00'), ('Cocinar y cenar', 'eat', '20:00', '22:00'), ('Costos – Repaso final', 'study', '22:00', '24:00')],
    '2026-06-30': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('🔥 Costos – Repaso FINAL', 'study', '17:00', '19:00'), ('Cursada: Prob y Estadística', 'study', '19:00', '22:00'), ('🔥 Costos – Último repaso', 'study', '22:00', '24:00')],
    '2026-07-01': [('Trabajo', 'work', '10:00', '16:00'), ('Viaje y despeje', 'travel', '16:00', '17:00'), ('Repaso último momento', 'study', '17:00', '19:00'), ('📝 PARCIAL: Costos Industriales', 'exam', '19:00', '22:00'), ('Cocinar y cenar', 'eat', '22:00', '24:00')]
}

def create_ics():
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Unidev Planner//NONSGML v1.0//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH"
    ]
    
    for date_str, events in seed.items():
        y, m, d = map(int, date_str.split('-'))
        for name, category, start, end in events:
            sh, sm = map(int, start.split(':'))
            if end == '24:00':
                eh, em = 23, 59
            else:
                eh, em = map(int, end.split(':'))
                
            start_dt = datetime.datetime(y, m, d, sh, sm)
            end_dt = datetime.datetime(y, m, d, eh, em)
            
            if end == '24:00':
                end_dt = end_dt + datetime.timedelta(minutes=1)
                
            # Formato ICS: YYYYMMDDTHHMMSS
            # Para Google Calendar es mejor usar hora local con zona horaria o UTC. 
            # Como estás en Buenos Aires, usaremos la TZ local.
            start_str = start_dt.strftime('%Y%m%dT%H%M%S')
            end_str = end_dt.strftime('%Y%m%dT%H%M%S')
            
            uid_hash = hashlib.md5(f"{name}{date_str}{start}{end}".encode('utf-8')).hexdigest()
            uid = f"{uid_hash}@unidev.planner"
            
            # Asignar emoji según categoría
            emoji = "📚"
            if category == "work": emoji = "💼"
            elif category == "travel": emoji = "🚗"
            elif category == "eat": emoji = "🍽️"
            elif category == "rest": emoji = "😴"
            elif category == "exam": emoji = "📝"
            
            title = f"{emoji} {name}"
            
            lines.extend([
                "BEGIN:VEVENT",
                f"UID:{uid}",
                f"DTSTAMP:{datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}",
                f"DTSTART;TZID=America/Argentina/Buenos_Aires:{start_str}",
                f"DTEND;TZID=America/Argentina/Buenos_Aires:{end_str}",
                f"SUMMARY:{title}",
                f"DESCRIPTION:Categoría original del plan: {category}",
                "STATUS:CONFIRMED",
                "END:VEVENT"
            ])
            
    lines.append("END:VCALENDAR")
    
    with open("unidev_routine.ics", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("unidev_routine.ics generado con éxito!")

if __name__ == "__main__":
    create_ics()
