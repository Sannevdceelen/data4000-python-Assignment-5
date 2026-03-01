# DATA 4000 – Assignment 5  
Conditionals, Loops, Exceptions, and Libraries

This repository contains solutions for Assignment 5 of DATA 4000.

Programs included:

- `pos_checkout.py` – Point-of-Sale Checkout System  
- `inventory_spotcheck.py` – Inventory Reorder Analyzer with API Spot Check  

---

## Installation

This project requires Python 3.x and the `requests` library.

Install the required dependency:

```bash
pip install requests
```

---

## How to Run

Open a terminal in the repository folder and run the programs using:

### Exercise 1 – Point-of-Sale Checkout

```bash
python pos_checkout.py
```

### Exercise 2 – Inventory Reorder Analyzer

```bash
python inventory_spotcheck.py
```

---

## Example Run – Exercise 1

```
Student key: 1
Enter item name (or DONE to finish): dress
Enter unit price: 25
Enter quantity: 2
Enter item name (or DONE to finish): skirt
Enter unit price: 20
Enter quantity: 1
Enter item name (or DONE to finish): done
Seed: 49
Units: 3
Subtotal: $70.00
Discount: 0%
Perk applied: YES
Total: $67.00
```

---

## Example Run – Exercise 2

```
Student key: 2
SKU (or DONE to finish): 45
On hand: 3
SKU (or DONE to finish): 678
On hand: 67
SKU (or DONE to finish): done
Seed: 50
Threshold: 9
SKUs entered: 2
Reorder flagged: 1
Spotcheck term: weezer
Songs returned: 5
API status: OK
```

---

## Notes

- Both programs compute a personalization seed using the student key.
- Input validation ensures programs do not crash due to invalid input.
- The API spot check uses the iTunes Search API.
