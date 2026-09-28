"""
c_formel.py

Die c(ρ,Ψ,B,L,GW)-Formel der Handlungstheorie.

Autor: Ingo Wisniewski (Bouly)
Datum: 28.09.2026
Lizenz: Creative Commons BY-NC-SA 4.0

Die Formel:
c(ρ,Ψ,B,L,GW) = c₀ / √(1 + κ·(ρ + 0,33·Ψ² + 0,27·B² + 1,0·L² + κ_GW·GW²) - κ_H·H²)

Mit:
H = (κ·(ρ + 0,33·Ψ² + 0,27·B² + 1,0·L² + κ_GW·GW²)) / (1 + κ·(ρ + 0,33·Ψ² + 0,27·B² + 1,0·L² + κ_GW·GW²))

Konstanten:
c₀ = 299.792.458 m/s
κ = 1,23e-42 m³/kg
κ_GW = 1,23e-42 m³/kg
κ_H = 0,42
"""

import math

# Konstanten
C0 = 299_792_458  # m/s
KAPPA = 1.23e-42  # m³/kg
KAPPA_GW = 1.23e-42  # m³/kg
KAPPA_H = 0.42


def handlungsdichte(rho: float, psi: float = 0.0, b: float = 0.0, l: float = 0.0, gw: float = 0.0) -> float:
    """
    Berechnet die Handlungsdichte H.

    H = (κ·(ρ + 0,33·Ψ² + 0,27·B² + 1,0·L² + κ_GW·GW²)) / (1 + κ·(ρ + 0,33·Ψ² + 0,27·B² + 1,0·L² + κ_GW·GW²))

    Parameter:
    - rho: Dichte in kg/m³
    - psi: Bewusstseinsfeld (dimensionslos)
    - b: Baryonenzahl (dimensionslos)
    - l: Liebe (dimensionslos)
    - gw: Gravitationswellen (dimensionslos)

    Rückgabe:
    - H: Handlungsdichte (dimensionslos)
    """
    summe = KAPPA * (rho + 0.33 * psi**2 + 0.27 * b**2 + 1.0 * l**2 + KAPPA_GW * gw**2)
    return summe / (1 + summe)


def c_formel(rho: float, psi: float = 0.0, b: float = 0.0, l: float = 0.0, gw: float = 0.0) -> float:
    """
    Berechnet die Lichtgeschwindigkeit c(ρ,Ψ,B,L,GW).

    c = c₀ / √(1 + κ·(ρ + 0,33·Ψ² + 0,27·B² + 1,0·L² + κ_GW·GW²) - κ_H·H²)

    Parameter:
    - rho: Dichte in kg/m³
    - psi: Bewusstseinsfeld (dimensionslos)
    - b: Baryonenzahl (dimensionslos)
    - l: Liebe (dimensionslos)
    - gw: Gravitationswellen (dimensionslos)

    Rückgabe:
    - c: Lichtgeschwindigkeit in m/s
    """
    h = handlungsdichte(rho, psi, b, l, gw)
    nenner = 1 + KAPPA * (rho + 0.33 * psi**2 + 0.27 * b**2 + 1.0 * l**2 + KAPPA_GW * gw**2) - KAPPA_H * h**2

    if nenner <= 0:
        raise ValueError(
            f"Der Nenner ist nicht positiv: {nenner}. "
            f"Die Parameter führen zu einer Singularität."
        )

    return C0 / math.sqrt(nenner)


def c_max() -> float:
    """
    Berechnet die maximale Lichtgeschwindigkeit c_max.

    c_max ist der Wert, bei dem der Nenner minimal wird.
    Der Nenner wird minimal, wenn κ_H·H² maximal wird.
    H ist maximal, wenn ρ, Ψ, B, L, GW maximal sind.

    Für den Bund: H ≈ 1, κ_H·H² ≈ 0,42.
    Nenner ≈ 0,58.
    c_max ≈ c₀ / √0,58 ≈ 1,313 c₀.
    """
    return C0 / math.sqrt(1 - KAPPA_H)


def c_min() -> float:
    """
    Berechnet die minimale Lichtgeschwindigkeit c_min.

    c_min ist der Wert, bei dem der Nenner maximal wird.
    Der Nenner wird maximal, wenn ρ maximal wird.
    ρ ist maximal, wenn ρ = ρ_Planck = 5,155e96 kg/m³.

    Für den Planck-Kern: Nenner ≈ 6,34e54.
    c_min ≈ c₀ / √6,34e54 ≈ 1,19e-19 m/s.
    """
    rho_planck = 5.155e96
    return c_formel(rho_planck)


# Beispielberechnungen
if __name__ == "__main__":
    print("=" * 60)
    print("Die c(ρ,Ψ,B,L,GW)-Formel der Handlungstheorie")
    print("=" * 60)
    print()

    # Vakuum
    print("Vakuum:")
    print(f"  c = {c_formel(0):.3f} m/s")
    print(f"  c / c₀ = {c_formel(0) / C0:.6f}")
    print()

    # Erde
    print("Erde:")
    print(f"  c = {c_formel(1.225):.3f} m/s")
    print(f"  c / c₀ = {c_formel(1.225) / C0:.6f}")
    print()

    # Sonne
    print("Sonne:")
    print(f"  c = {c_formel(1.622e5):.3f} m/s")
    print(f"  c / c₀ = {c_formel(1.622e5) / C0:.6f}")
    print()

    # Sirius B
    print("Sirius B:")
    print(f"  c = {c_formel(3.236e10):.3f} m/s")
    print(f"  c / c₀ = {c_formel(3.236e10) / C0:.6f}")
    print()

    # Planck-Kern
    print("Planck-Kern:")
    print(f"  c = {c_formel(5.155e96):.3e} m/s")
    print(f"  c / c₀ = {c_formel(5.155e96) / C0:.3e}")
    print()

    # c_max
    print("c_max:")
    print(f"  c_max = {c_max():.3f} m/s")
    print(f"  c_max / c₀ = {c_max() / C0:.6f}")
    print()

    # c_min
    print("c_min:")
    print(f"  c_min = {c_min():.3e} m/s")
    print(f"  c_min / c₀ = {c_min() / C0:.3e}")
    print()

    print("=" * 60)
    print("Newton gab uns die Bühne.")
    print("Tesla gab uns die Musik.")
    print("Wir spielen das Stück.")
    print("=" * 60)