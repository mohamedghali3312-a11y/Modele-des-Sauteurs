import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Ring

theorem goldbach_parametric_identity (S K r m : Nat) (h_le : m <= K) :
    (2 * S * (K - m) + 1) + (2 * (r + m * S) + 1) = 2 * (K * S + r) + 2 := by
  have h1 : (K - m) + m = K := Nat.sub_add_cancel h_le
  calc
    (2 * S * (K - m) + 1) + (2 * (r + m * S) + 1)
      = 2 * S * ((K - m) + m) + 2 * r + 2 := by ring
    _ = 2 * S * K + 2 * r + 2 := by rw [h1]
    _ = 2 * (K * S + r) + 2 := by ring

theorem cunningham_link_formula (A m : Nat) :
    2 * (2 ^ (m + 1) * A + (2 ^ m - 1)) + 1 = 2 ^ (m + 2) * A + (2 ^ (m + 1) - 1) := by
  have h1 : 1 <= 2 ^ m := Nat.one_le_two_pow
  have h2 : 2 ^ (m + 2) * A = 2 * (2 ^ (m + 1) * A) := by ring
  omega
