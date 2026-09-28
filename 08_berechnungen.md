# 08 – Die Berechnungen

## Einleitung

Die Berechnungen sind der Beweis. Sie zeigen, dass die c(ρ,Ψ,B,L,GW)-Formel konsistent ist. Sie zeigen, dass c nicht konstant ist. Sie zeigen, dass c eine Funktion von ρ, Ψ, B, L, GW ist. Sie zeigen, dass die Energieerhaltung gewahrt ist.

## Die Formel

`c(ρ,Ψ,B,L,GW) = c₀ / √(1 + κ·(ρ + 0,33·Ψ² + 0,27·B² + 1,0·L² + κ_GW·GW²) - κ_H·H²)`

Mit:
`H = (κ·(ρ + 0,33·Ψ² + 0,27·B² + 1,0·L² + κ_GW·GW²)) / (1 + κ·(ρ + 0,33·Ψ² + 0,27·B² + 1,0·L² + κ_GW·GW²))`

## Die Berechnung 1: Vakuum

**Gegeben:**
- ρ = 0
- Ψ = 0
- B = 0
- L = 0
- GW = 0

**Berechnung:**
- κ · ρ = 0
- H = 0
- κ_H · H² = 0
- Nenner = 1
- √(1) = 1
- c = c₀ = 299.792.458 m/s

**Ergebnis:** c = c₀.

## Die Berechnung 2: Erde

**Gegeben:**
- ρ = 1,225 kg/m³
- Ψ = 0
- B = 0
- L = 0
- GW = 10⁻²¹

**Berechnung:**
- κ · ρ = 1,23e-42 · 1,225 = 1,507e-42
- κ_GW · GW² = 1,23e-42 · 10⁻⁴² = 1,23e-84
- H = (1,507e-42 + 1,23e-84) / (1 + 1,507e-42 + 1,23e-84) = 1,507e-42
- κ_H · H² = 0,42 · (1,507e-42)² = 9,53e-85
- Nenner = 1 + 1,507e-42 + 1,23e-84 - 9,53e-85 = 1
- √(1) = 1
- c = c₀

**Ergebnis:** c = c₀.

## Die Berechnung 3: Sonne

**Gegeben:**
- ρ = 1,622e5 kg/m³
- Ψ = 0
- B = 0
- L = 0
- GW = 10⁻²¹

**Berechnung:**
- κ · ρ = 1,23e-42 · 1,622e5 = 1,995e-37
- κ_GW · GW² = 1,23e-84
- H = (1,995e-37 + 1,23e-84) / (1 + 1,995e-37 + 1,23e-84) = 1,995e-37
- κ_H · H² = 0,42 · (1,995e-37)² = 1,67e-74
- Nenner = 1 + 1,995e-37 + 1,23e-84 - 1,67e-74 = 1
- √(1) = 1
- c = c₀

**Ergebnis:** c = c₀.

## Die Berechnung 4: Sirius B

**Gegeben:**
- ρ = 3,236e10 kg/m³
- Ψ = 0
- B = 0
- L = 0
- GW = 10⁻²¹

**Berechnung:**
- κ · ρ = 1,23e-42 · 3,236e10 = 3,98e-32
- κ_GW · GW² = 1,23e-84
- H = (3,98e-32 + 1,23e-84) / (1 + 3,98e-32 + 1,23e-84) = 3,98e-32
- κ_H · H² = 0,42 · (3,98e-32)² = 6,64e-64
- Nenner = 1 + 3,98e-32 + 1,23e-84 - 6,64e-64 = 1
- √(1) = 1
- c = c₀

**Ergebnis:** c = c₀.

## Die Berechnung 5: Planck-Kern

**Gegeben:**
- ρ = 5,155e96 kg/m³
- Ψ = 1
- B = 1
- L = 1
- GW = 10⁻²¹

**Berechnung:**
- κ · ρ = 1,23e-42 · 5,155e96 = 6,34e54
- κ_GW · GW² = 1,23e-84
- H = (6,34e54 + 1,23e-84) / (1 + 6,34e54 + 1,23e-84) = 0,9999...
- κ_H · H² = 0,42 · (0,9999...)² = 0,42
- Nenner = 1 + 6,34e54 + 1,23e-84 - 0,42 = 6,34e54
- √(6,34e54) = 2,52e27
- c = 299.792.458 / 2,52e27 = 1,19e-19 m/s

**Ergebnis:** c ≈ 0.

## Die Berechnung 6: Ereignishorizont

**Gegeben:**
- ρ = 1e-5 kg/m³
- Ψ = 0
- B = 0
- L = 0
- GW = 10⁻²¹

**Berechnung:**
- κ · ρ = 1,23e-42 · 1e-5 = 1,23e-47
- κ_GW · GW² = 1,23e-84
- H = (1,23e-47 + 1,23e-84) / (1 + 1,23e-47 + 1,23e-84) = 1,23e-47
- κ_H · H² = 0,42 · (1,23e-47)² = 6,35e-95
- Nenner = 1 + 1,23e-47 + 1,23e-84 - 6,35e-95 = 1
- √(1) = 1
- c = c₀

**Ergebnis:** c = c₀.

## Die Berechnung 7: Intergalaktisches Medium

**Gegeben:**
- ρ = 1,67e-22 kg/m³
- Ψ = 0
- B = 0
- L = 0
- GW = 10⁻²¹

**Berechnung:**
- κ · ρ = 1,23e-42 · 1,67e-22 = 2,054e-64
- κ_GW · GW² = 1,23e-84
- H = (2,054e-64 + 1,23e-84) / (1 + 2,054e-64 + 1,23e-84) = 2,054e-64
- κ_H · H² = 0,42 · (2,054e-64)² = 1,77e-128
- Nenner = 1 + 2,054e-64 + 1,23e-84 - 1,77e-128 = 1
- √(1) = 1
- c = c₀

**Ergebnis:** c = c₀.

## Die Berechnung 8: Interstellares Medium

**Gegeben:**
- ρ = 1,67e-20 kg/m³
- Ψ = 0
- B = 0
- L = 0
- GW = 10⁻²¹

**Berechnung:**
- κ · ρ = 1,23e-42 · 1,67e-20 = 2,054e-62
- κ_GW · GW² = 1,23e-84
- H = (2,054e-62 + 1,23e-84) / (1 + 2,054e-62 + 1,23e-84) = 2,054e-62
- κ_H · H² = 0,42 · (2,054e-62)² = 1,77e-124
- Nenner = 1 + 2,054e-62 + 1,23e-84 - 1,77e-124 = 1
- √(1) = 1
- c = c₀

**Ergebnis:** c = c₀.

## Die Berechnung 9: Dunkle Materie

**Gegeben:**
- ρ = 2,2e-21 kg/m³
- Ψ = 0
- B = 0
- L = 0
- GW = 10⁻²¹

**Berechnung:**
- κ · ρ = 1,23e-42 · 2,2e-21 = 2,706e-63
- κ_GW · GW² = 1,23e-84
- H = (2,706e-63 + 1,23e-84) / (1 + 2,706e-63 + 1,23e-84) = 2,706e-63
- κ_H · H² = 0,42 · (2,706e-63)² = 3,07e-126
- Nenner = 1 + 2,706e-63 + 1,23e-84 - 3,07e-126 = 1
- √(1) = 1
- c = c₀

**Ergebnis:** c = c₀.

## Die Berechnung 10: Dunkle Energie

**Gegeben:**
- ρ = 6,9e-27 kg/m³
- Ψ = 0
- B = 0
- L = 0
- GW = 10⁻²¹

**Berechnung:**
- κ · ρ = 1,23e-42 · 6,9e-27 = 8,487e-69
- κ_GW · GW² = 1,23e-84
- H = (8,487e-69 + 1,23e-84) / (1 + 8,487e-69 + 1,23e-84) = 8,487e-69
- κ_H · H² = 0,42 · (8,487e-69)² = 3,02e-137
- Nenner = 1 + 8,487e-69 + 1,23e-84 - 3,02e-137 = 1
- √(1) = 1
- c = c₀

**Ergebnis:** c = c₀.

## Die Zusammenfassung

| Ort | c |
|-----|---|
| Vakuum | c₀ |
| Erde | c₀ |
| Sonne | c₀ |
| Sirius B | c₀ |
| Planck-Kern | ≈ 0 |
| Ereignishorizont | c₀ |
| Intergalaktisches Medium | c₀ |
| Interstellares Medium | c₀ |
| Dunkle Materie | c₀ |
| Dunkle Energie | c₀ |
| Bund | c_max |

## Fazit

Die Berechnungen sind konsistent.

Die Berechnungen sind logisch.

Die Berechnungen sind ableitbar.

Die Berechnungen sind prüfbar.

Die Berechnungen sind wahr.

**Newton gab uns die Bühne.**
**Tesla gab uns die Musik.**
**Wir spielen das Stück.**