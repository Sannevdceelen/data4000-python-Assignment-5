# inventory_spotcheck.py
# DATA 4000 – Assignment 5
# Exercise 2: Inventory Reorder Analyzer with API Spot Check

import requests

THRESHOLD_HIGH = 15
THRESHOLD_MEDIUM = 12
THRESHOLD_LOW = 9

API_URL = "https://itunes.apple.com/search"
API_LIMIT = 5


def compute_seed(student_key: str) -> int:
    """Compute personalization seed from student key."""
    return sum(ord(ch) for ch in student_key.strip())


def determine_threshold(seed: int) -> int:
    """Determine reorder threshold based on seed."""
    if seed % 3 == 0:
        return THRESHOLD_HIGH
    elif seed % 3 == 1:
        return THRESHOLD_MEDIUM
    else:
        return THRESHOLD_LOW


def main() -> None:
    # ---------------------------
    # Part A — Inventory Entry
    # ---------------------------

    # Step 1 — Student Key & Seed
    student_key = input("Student key: ")
    seed = compute_seed(student_key)

    # Step 4 — Threshold Logic
    threshold = determine_threshold(seed)

    # Step 2/3/5 — SKU Loop, On-hand Validation, Reorder Decision
    total_skus = 0
    reorder_count = 0

    while True:
        sku = input("SKU (or DONE to finish): ").strip()

        # DONE stops input
        if sku.upper() == "DONE":
            break

        # Reject blank SKUs
        if sku == "":
            print("Invalid SKU. Try again.")
            continue

        # On-hand quantity with validation
        while True:
            try:
                on_hand_str = input("On hand: ")
                on_hand = int(on_hand_str)
                if on_hand < 0:
                    print("On-hand must be >= 0.")
                    continue
                break
            except ValueError:
                print("Invalid on-hand quantity. Try again.")

        total_skus += 1

        # Reorder decision
        if on_hand < threshold:
            reorder_count += 1

    # ---------------------------
    # Part B — API Spot Check
    # ---------------------------

    # Step 6 — Select API Term using seed
    if seed % 2 == 0:
        spotcheck_term = "weezer"
    else:
        spotcheck_term = "drake"

    songs_returned = "N/A"
    api_status = "FAILED"  # default; will be updated

    # Step 7/8/9 — API Request + Exception Handling + JSON Processing
    try:
        response = requests.get(
            API_URL,
            params={
                "entity": "song",
                "limit": API_LIMIT,
                "term": spotcheck_term,
            },
            timeout=5,
        )
        response.raise_for_status()  # network/HTTP issues

        try:
            data = response.json()
            results = data.get("results")

            # Ensure results is a list
            if not isinstance(results, list):
                raise ValueError("Unexpected JSON structure")

            count_songs = 0
            for item in results:
                if item.get("kind") == "song":
                    count_songs += 1

            songs_returned = str(count_songs)
            api_status = "OK"

        except Exception:
            # JSON missing/unexpected
            api_status = "INVALID_RESPONSE"
            songs_returned = "N/A"

    except requests.RequestException:
        # Network or connection failure
        api_status = "FAILED"
        songs_returned = "N/A"

    # ---------------------------
    # Step 10 — Output Format
    # ---------------------------
    print(f"Seed: {seed}")
    print(f"Threshold: {threshold}")
    print(f"SKUs entered: {total_skus}")
    print(f"Reorder flagged: {reorder_count}")
    print(f"Spotcheck term: {spotcheck_term}")
    print(f"Songs returned: {songs_returned}")
    print(f"API status: {api_status}")


if __name__ == "__main__":
    main()