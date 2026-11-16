import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Ring

theorem goldbach_parametric_identity (S K r m : Nat) :
    let C := K * S + r
    let N := 2 * C + 2
    let Q_m := 2 * (r + m * S) + 1
    let P_m := 2 * S * (K - m) + 1
    m <= K -> P_m + Q_m = N := by
  intro C N Q_m P_m h_le
  dsimp only [C, N, Q_m, P_m]
  omega

theorem cunningham_link_formula (A m : Nat) :
    2 * (2 ^ (m + 1) * A + (2 ^ m - 1)) + 1 = 2 ^ (m + 2) * A + (2 ^ (m + 1) - 1) := by
  have h1 : 1 <= 2 ^ m := Nat.one_le_two_pow
  have h2 : 1 <= 2 ^ (m + 1) := Nat.one_le_two_pow
  zify [h1, h2]
  ring
