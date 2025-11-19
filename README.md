# FireAnneal – Feueranimation mit Simulated Annealing

## Projektbeschreibung
FireAnneal erzeugt eine dynamische Feueranimation mithilfe von Simulated Annealing.  
Das System verwaltet eine zweidimensionale Temperaturkarte, deren Werte sich kontinuierlich verändern.  
Über Mutationen und eine Bewertungsfunktion wird entschieden, ob ein neuer Zustand realistischer wirkt.  
Simulated Annealing akzeptiert schlechtere Zustände abhängig von einer abkühlenden Temperatur.  
So entsteht ein organisch wirkendes Feuerbild, das sich über die Zeit stabilisiert.

## Ziele
- Umsetzung eines naturanalogen Optimierungsverfahrens in einem visuellen Kontext  
- Generierung eines animierten Feuerbildes  
- Demonstration des Simulated-Annealing-Prinzips  
- Erweiterbar für interaktive oder modellbasierte Feuersimulationen

## Funktionsprinzip (kurz)
1. Ein 2D-Array speichert Temperaturwerte (z. B. 0–255).  
2. Eine Mutation verändert einzelne Pixel oder Pixelgruppen.  
3. Eine Cost-Funktion bewertet, wie feuerähnlich der Zustand ist.  
4. Simulated Annealing entscheidet, ob der neue Zustand übernommen wird.  
5. Durch das Abkühlen des Algorithmus wird das Verhalten zunehmend stabiler.  
6. Die Temperaturwerte werden zu Farben gemappt und visualisiert.
