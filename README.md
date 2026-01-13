# 🚀 OOP Assignment #1 - Python

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Topic](https://img.shields.io/badge/Focus-OOP_Principles-green)

---

## 📝 Project Overview
פרויקט זה מציג את היישום של עקרונות התכנות מונחה העצמים (OOP) שנלמדו בקורס. כל תיקייה מייצגת עקרון אחר ושואפת להדגים קוד נקי, בטוח ומאורגן.

---

## 🛠️ Tasks & Implementation

### 🛡️ Task 1: Invoice System (Encapsulation)
* **Goal:** Secure data management for business invoices.
* **Core Concepts:**
    * `Private Attributes`: Used `__` for data hiding.
    * `Properties`: Implemented `@property` and `@setter` for validation.
    * `Formatting`: Used `locale` for professional output.

> **Key Takeaway:** Encapsulation ensures that an invoice's price or ID cannot be changed to invalid values from outside the class.

---

### 🧬 Task 2: Securities System (Inheritance)
* **Goal:** Modeling a financial market hierarchy.
* **Core Concepts:**
    * `Base Class`: Shared logic in the `Security` class.
    * `Specialization`: Unique classes for `Stock`, `Bond`, and `Option`.
    * `DRY Principle`: Using `super()` to avoid code duplication.

---

### 🎭 Task 3: Animal Sounds (Polymorphism)
* **Goal:** Universal interface for different object types.
* **Core Concepts:**
    * `Abstract Base Classes`: Defining a "contract" using `ABC`.
    * `Duck Typing`: Pythonic approach to object behavior.
    * `Type Safety`: Validating objects with `isinstance()` before execution.

---

## 📂 Project Structure
| Section | Concept | Main Files |
| :--- | :--- | :--- |
| **Seif1** | Encapsulation | `invoice.py`, `main.py` |
| **Seif2** | Inheritance | `securities.py`, `main.py` |
| **Seif3** | Polymorphism | `animals.py`, `main.py` |

---
*Created by Adi Saadon - 2026*
