# 🚀 OOP Assignment #1 - Python Principles

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Topic](https://img.shields.io/badge/Focus-OOP_Principles-green)

---

## 📝 Project Overview
This repository contains the implementation of the first assignment in the Object-Oriented Programming (OOP) course. Each directory demonstrates a core OOP principle: **Encapsulation**, **Inheritance**, and **Polymorphism**, using clean and modular Python code.

---

## 🛠️ Tasks & Implementation

### 🛡️ Task 1: Invoice System (Encapsulation)
* **Objective:** Developing a secure system for managing business invoices.
* **Key Features:**
    * **Data Hiding:** Implemented private attributes (using `__`) to prevent unauthorized access to sensitive data such as price and ID.
    * **Controlled Access:** Used the `@property` decorator to provide read access to internal attributes without exposing the internal state.
    * **Currency Formatting:** Integrated the `locale` module to ensure that financial data is displayed in a professional currency format.

---

### 🧬 Task 2: Securities Market (Inheritance)
* **Objective:** Modeling a financial market hierarchy to manage various investment types.
* **Key Features:**
    * **Class Hierarchy:** Created a base class `Security` to hold shared logic (Name, Symbol, Price).
    * **Specialization:** Implemented derived classes for `Stock`, `Bond`, and `Option`, each adding unique attributes and specific methods.
    * **Code Reusability:** Leveraged the `super()` function to initialize parent attributes, following the DRY (Don't Repeat Yourself) principle.

---

### 🎭 Task 3: Animal Sounds (Polymorphism)
* **Objective:** Implementing a universal interface to interact with different object types.
* **Key Features:**
    * **Abstract Base Classes:** Defined a template `Animal` class using the `ABC` module to enforce a "contract" for sub-classes.
    * **Polymorphic Execution:** Implemented `Dog` and `Cat` classes that provide their own specific version of the `speak()` method.
    * **Type Safety:** Used `isinstance()` checks within a shared loop to ensure robust execution before invoking methods.
    * **Duck Typing:** Demonstrated Python's ability to handle objects based on their behavior rather than their explicit type.

---

## 📂 Project Structure

| Folder | Concept | Key Files |
| :--- | :--- | :--- |
| **Seif1** | Encapsulation | `invoice.py`, `main.py` |
| **Seif2** | Inheritance | `securities.py`, `main.py` |
| **Seif3** | Polymorphism | `animals.py`, `main.py` |

---
*Created by Adi Saadon - 2026*
