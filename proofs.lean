import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Ring

theorem goldbach_parametric_identity (S K r m : Nat) (h_le : m <= K) :
    (2 * S * (K - m) + 1) + (2 * (r + m * S) + 1) = 2 * (K * S + r) + 2 := by
  have h1 : (K - m) + m = K := Nat.sub_add_cancel h_le
  have h2 : 2 * S * (K - m) + 2 * (m * S) = 2 * S * ((K - m) + m) := by ring
  rw [h1] at h2
  omega

theorem cunningham_link_formula (A m : Nat) :
    2 * (2 ^ (m + 1) * A + (2 ^ m - 1)) + 1 = 2 ^ (m + 2) * A + (2 ^ (m + 1) - 1) := by
  have h1 : 1 <= 2 ^ m := Nat.one_le_two_pow
  have h2 : 2 ^ (m + 2) * A = 2 * (2 ^ (m + 1) * A) := by ring
  omega
