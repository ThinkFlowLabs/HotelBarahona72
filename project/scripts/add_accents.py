# -*- coding: utf-8 -*-
# Agrega tildes al texto visible del sitio, protegiendo estructura (CSS, JS, JSON-LD, href/src/id/class/style).
import io, re
P = r"C:/Users/JimAn/Desktop/ThinkFlowLabs/Websites Builder/Projects/Hotel Barahona 72/site/index.html"
s = io.open(P, encoding="utf-8").read(); orig = s

# ---- 1. PROTECT structural pieces ----
store = []
def prot(m):
    store.append(m.group(0)); return "\x01PH%d\x01" % (len(store)-1)
s = re.sub(r'<style[^>]*>.*?</style>', prot, s, flags=re.S)
s = re.sub(r'<script[^>]*>.*?</script>', prot, s, flags=re.S)
# protect structural attributes (values only kept intact) - NOT alt/aria-label/content/data-cap/title
s = re.sub(r'(?:href|src|srcset|data-full|data-group|data-f|id|class|style|viewBox|d|lang|rel|type|name|property)="[^"]*"', prot, s)

# ---- 2. DICTIONARY (whole-word, case-sensitive) ----
D = {
 # -cion / -sion nouns (singular only; plurals lose the accent)
 "Ubicacion":"Ubicación","ubicacion":"ubicación",
 "Habitacion":"Habitación","habitacion":"habitación",
 "Recepcion":"Recepción","recepcion":"recepción",
 "Television":"Televisión","television":"televisión",
 "Informacion":"Información","informacion":"información",
 "Atencion":"Atención","atencion":"atención",
 "Navegacion":"Navegación","navegacion":"navegación",
 "Calificacion":"Calificación","calificacion":"calificación",
 # otros sustantivos/adjetivos
 "telefono":"teléfono","Telefono":"Teléfono",
 "economico":"económico","Economico":"Económico",
 "comodo":"cómodo","Comodo":"Cómodo","comoda":"cómoda",
 "historico":"histórico","Historico":"Histórico",
 "corazon":"corazón",
 "salon":"salón","Salon":"Salón",
 "clinicas":"clínicas","clinica":"clínica",
 "medicas":"médicas","medica":"médica","medico":"médico","medicos":"médicos",
 "estadia":"estadía","Estadia":"Estadía",
 "vehiculo":"vehículo",
 "numero":"número","Numero":"Número",
 "cuadruple":"cuádruple","Cuadruple":"Cuádruple",
 "lavanderia":"lavandería","Lavanderia":"Lavandería",
 "mediodia":"mediodía",
 "huespedes":"huéspedes","Huesped":"Huésped","huesped":"huésped",
 "centrico":"céntrico",
 "area":"área","areas":"áreas",
 "facil":"fácil",
 "unico":"único","unica":"única",
 # adverbios
 "tambien":"también","segun":"según","aqui":"aquí","Aqui":"Aquí",
 "asi":"así","Asi":"Así","rapido":"rápido","Rapido":"Rápido",
 "despues":"después","ademas":"además","proximo":"próximo","proxima":"próxima",
 "mas":"más","super":"súper",
 # verbos que siempre llevan tilde
 "varia":"varía","varian":"varían","estan":"están","Estan":"Están",
 # dia / dias
 "dia":"día","dias":"días","Dia":"Día","Dias":"Días",
 # nombres propios
 "Atlantico":"Atlántico","Martinez":"Martínez","Tomas":"Tomás",
}
for plain, acc in D.items():
    s = re.sub(r'\b'+re.escape(plain)+r'\b', acc, s)

# ---- 3. context-specific fixes ----
specific = [
 ("&iquest;Cuanto","&iquest;Cuánto"),("&iquest;Cual","&iquest;Cuál"),
 ("&iquest;Que","&iquest;Qué"),("&iquest;Donde","&iquest;Dónde"),("&iquest;Como","&iquest;Cómo"),
 ("¿Cuanto","¿Cuánto"),("¿Cual","¿Cuál"),("¿Que","¿Qué"),("¿Donde","¿Dónde"),("¿Como","¿Cómo"),
 ("desayuno esta incluido","desayuno está incluido"),
 ("Cortissoz esta a unos","Cortissoz está a unos"),
 (">Si, ",">Sí, "),("<p>Si,","<p>Sí,"),
 ("Escribenos","Escríbenos"),("escribenos","escríbenos"),
 ("Avisanos","Avísanos"),
 ("Aseguralá","Asegúrala"),
 ("Como llegar","Cómo llegar"),
]
for a,b in specific:
    s = s.replace(a,b)

# ---- 4. RESTORE ----
for i,v in enumerate(store):
    s = s.replace("\x01PH%d\x01" % i, v)

io.open(P,"w",encoding="utf-8").write(s)
print("accents applied. delta chars", len(s)-len(orig))
# show any remaining bare 'esta'/'estan' verb-suspects for review
for mo in re.finditer(r'>[^<]*\b(esta)\b[^<]*<', s):
    seg = mo.group(0)[:80]
    if 'está' not in seg:
        print("REVIEW esta:", seg.strip())
