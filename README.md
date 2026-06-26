# Matrice — Application d'Algèbre Linéaire

A Python command-line application for performing matrix operations and linear algebra computations, with an interactive menu interface.

## Overview

This project provides a complete interactive console tool for working with matrices. Users enter matrices through guided prompts, then choose from a wide range of operations — from basic arithmetic to Gaussian elimination. Results are displayed step by step with formatted matrix output using Unicode bracket characters.

> ⚠️ **Platform note:** The application currently targets **Windows** (`os.system("cls")`, `msvcrt`). Minor changes are needed to run on Linux/macOS.

---

## Features

### Currently implemented
| # | Operation |
|---|-----------|
| 1 | Addition of two matrices |
| 2 | Subtraction of two matrices |
| 4 | Scalar multiplication |
| 5 | Transpose |
| 6 | Gaussian elimination (row echelon form) |
| 25 | Operation history |
| 0 | Quit |

### Planned (menu present, not yet implemented)
- Matrix multiplication (3)
- Gauss-Jordan reduction (7)
- Linear system solving (8)
- Rank (9), Determinant (10), Inverse (11), Trace (12)
- Eigenvalues / eigenvectors (16–17)
- Kernel / Image (18–19)
- LU decomposition (20), SVD (21)
- Random matrix generator (22)
- Save / Load (23–24)

---

## Project Structure

```
matrice/
├── main.py         # Entry point — menu loop and operation dispatch
├── matrice_io.py   # Matrix input, display, and swap utilities
├── gauss.py        # Gaussian elimination with step-by-step row operation log
├── operations.py   # Addition, subtraction, scalar multiplication, transpose
├── menu_txtes.py   # Menu rendering and title formatting
└── utils.py        # Windows-specific "press any key" pause utility
```

---

## Getting Started

### Prerequisites

- Python 3.x
- Windows OS (for `msvcrt` and `cls` commands)

### Run

```bash
python main.py
```

You will be greeted with a welcome screen, then a full menu. Enter the number of the operation you want:

```
=========================================================
          APPLICATION D'ALGÈBRE LINÉAIRE
=========================================================

[A] Opérations sur les matrices       [B] Réduction et résolution
    [1]. Addition                         [6]. Réduction de Gauss
    [2]. Soustraction                     ...
    [4]. Multiplication par scalaire
    [5]. Transposée
...
```

---

## Example — Gaussian Elimination (option 6)

```
Matrice initiale :
⎡ 0 2 1 ⎤
⎢ 3 1 4 ⎥
⎣ 6 0 2 ⎦

L1 ↔ L2
⎡ 3 1 4 ⎤
⎢ 0 2 1 ⎥
⎣ 6 0 2 ⎦

_________Opérations effectuées sur les lignes :_________

L3 ← 3L3 - 6L1

⎡ 3  1  4 ⎤
⎢ 0  2  1 ⎥
⎣ 0 -6 -18 ⎦
```

---

## Module Reference

### `matrice_io.py`
- **`prenant_matrice(nom)`** — prompts the user for matrix dimensions and integer values; returns a 2D list.
- **`affichage(matrice)`** — prints the matrix with Unicode bracket notation (`⎡ ⎢ ⎣ ⎤ ⎥ ⎦`).
- **`demander_matrice()`** — wraps `prenant_matrice` with error handling and a title prompt.

### `gauss.py`
- **`elimination_gauss(matrice, pivot)`** — performs one forward-elimination step for a given pivot column. Prints each row operation (`Lj ← pLj − aLi`) before applying it.

### `operations.py`
- **`addition(m1, m2)`** — element-wise addition; prints each computation.
- **`souetraction(m1, m2)`** — element-wise subtraction; prints each computation.
- **`multiplication_scalaire(matrice, scalaire)`** — multiplies every element by a scalar.
- **`Transpose(matrice)`** — returns the transposed matrix.

### `menu_txtes.py`
- **`menu()`** — prints the full operation menu.
- **`home()`** — prints the welcome screen.
- **`titre(text)`** — prints a centered section title surrounded by `=` separators.

### `utils.py`
- **`clear_avec_msg(msg)`** — displays a message, waits for a keypress (Windows `msvcrt`), then clears the screen.

---

## License

No license specified.