"""
Quiz 1 (Minggu 1) — Konsep Dasar Probabilitas

Isi fungsi-fungsi di bawah. Semua fungsi harus *pure* (tidak print),
dan mengembalikan nilai agar bisa diuji otomatis.

Catatan:
- Untuk float, gunakan operasi biasa; test memakai toleransi.
- Anda boleh import modul standar Python.
"""

from __future__ import annotations

from typing import Iterable, List, Sequence, Tuple


def q1_sample_space_binary_3() -> List[Tuple[int, int, int]]:
    """
    Mengembalikan seluruh ruang sampel untuk 3 kali pengiriman sinyal biner (0/1).

    Return:
        list of tuple, misalnya [(0,0,0), (0,0,1), ..., (1,1,1)]
    """
    # TODO: implement
    raise NotImplementedError


def q2_union_probability(p_a: float, p_b: float, p_a_and_b: float) -> float:
    """Menghitung P(A ∪ B) = P(A) + P(B) - P(A ∩ B)."""
    # TODO: implement
    raise NotImplementedError


def q3_complement_probability(p_event: float) -> float:
    """Menghitung probabilitas komplemen: P(A^c) = 1 - P(A)."""
    # TODO: implement
    raise NotImplementedError


def q4_is_mutually_exclusive_possible(probs: Sequence[float]) -> tuple[bool, float]:
    """
    Mengecek apakah sekumpulan kejadian bisa mutually exclusive dalam satu ruang sampel.
    Kriteria sederhana (sesuai soal): sum(P_i) <= 1.

    Return:
        (is_possible, total_prob)
    """
    # TODO: implement
    raise NotImplementedError


def q5_joint_probability(count_joint: int, total: int) -> float:
    """Probabilitas joint = count_joint / total."""
    # TODO: implement
    raise NotImplementedError


def q6_marginal_probability(counts: Sequence[int], total: int) -> float:
    """
    Probabilitas marginal = (sum counts) / total.

    Contoh:
        counts = [9, 5], total=100 => 0.14
    """
    # TODO: implement
    raise NotImplementedError


def q7_demorgan_notA_and_notB(p_a_union_b: float) -> float:
    """Dengan De Morgan: P(A^c ∩ B^c) = 1 - P(A ∪ B)."""
    # TODO: implement
    raise NotImplementedError


def q8_conditional_probability(n_a_and_b: int, n_a: int) -> float:
    """Probabilitas kondisional sederhana: P(B|A) = n(A ∩ B) / n(A)."""
    # TODO: implement
    raise NotImplementedError


def q9_total_sample_points_board_test(num_defect_types: int) -> int:
    """
    Hasil uji papan sirkuit:
    - 1 outcome untuk 'Lolos'
    - Jika gagal, ada `num_defect_types` jenis cacat (outcome terpisah)

    Total = 1 + num_defect_types
    """
    # TODO: implement
    raise NotImplementedError


def q10_empirical_probability_greater_than(data: Sequence[float], threshold: float) -> float:
    """
    Probabilitas empiris = frekuensi relatif data > threshold.
    """
    # TODO: implement
    raise NotImplementedError
