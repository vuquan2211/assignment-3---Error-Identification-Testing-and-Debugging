import unittest
from io import StringIO
from unittest.mock import patch

from BuggyCode_Fixed import Order


class TestOrderManagement(unittest.TestCase):

    # Unit Test 1 - Bug 3
    def test_01_calculate_total_returns_correct_total(self):
        print("\n=== START test_01_calculate_total ===")
        results = []
        failed_cases = []

        for case_num in range(1, 4):
            print(f"\n[Test 1 - Case {case_num}]")

            qty_book = int(input("Enter Book quantity: "))
            qty_pen = int(input("Enter Pen quantity: "))

            order = Order("Alice", [
                ("Book", qty_book, 15.00),
                ("Pen", qty_pen, 1.50)
            ])

            expected_total = (qty_book * 15.00) + (qty_pen * 1.50)
            actual_total = order.calculate_total()

            status = "PASS" if actual_total == expected_total else "FAIL"
            results.append((case_num, qty_book, qty_pen, expected_total, actual_total, status))

            if status == "FAIL":
                failed_cases.append(
                    f"Case {case_num}: expected {expected_total}, got {actual_total}"
                )

        print("\n===== SUMMARY TABLE =====")
        print(f"{'Case':<6}{'Book':<8}{'Pen':<8}{'Expected':<12}{'Actual':<12}{'Status':<8}")

        for case_num, book, pen, expected, actual, status in results:
            print(f"{case_num:<6}{book:<8}{pen:<8}{expected:<12}{actual:<12}{status:<8}")

        print("=== END test_01 ===")

        if failed_cases:
            self.fail(" ; ".join(failed_cases))

    # Unit Test 2 - Bug 4
    def test_02_apply_discount_returns_correct_values(self):
        print("\n=== START test_02_apply_discount ===")

        test_cases = [
            ("SAVE10", 0.1),
            ("SAVE20", 0.2),
            ("SAVE30", 0),
            ("INVALID", 0),
            ("", 0)
        ]

        results = []
        failed_cases = []

        order = Order("Alice", [])

        for case_num, (code, expected) in enumerate(test_cases, start=1):
            actual = order.apply_discount(code)

            if actual == expected:
                display_actual = actual
                status = "PASS"
            else:
                display_actual = "ERROR"
                status = "FAIL"
                failed_cases.append(f"{code}: expected {expected}, got {actual}")

            results.append((case_num, code, expected, display_actual, status))

        print("\n===== DISCOUNT TEST TABLE =====")
        print(f"{'Case':<6}{'Code':<10}{'Expected':<12}{'Actual':<12}{'Status':<8}")

        for case_num, code, expected, actual, status in results:
            print(f"{case_num:<6}{code:<10}{expected:<12}{actual:<12}{status:<8}")

        print("=== END test_02 ===")

        if failed_cases:
            self.fail(" ; ".join(failed_cases))

    # Integration Test
    def test_03_order_flow_integration(self):
        print("\n=== START test_03_order_flow_integration ===")

        order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
        results = []
        failed_steps = []

        # Step 1: Check initial total
        expected_initial = 37.5
        actual_initial = order.calculate_total()
        status = "PASS" if actual_initial == expected_initial else "FAIL"
        results.append(("Initial total", expected_initial, actual_initial, status))

        if status == "FAIL":
            failed_steps.append(
                f"Initial total: expected {expected_initial}, got {actual_initial}"
            )

        # Step 2: Add item
        order.add_item("Notebook", 3, 5.00)
        expected_after_add = 52.5
        actual_after_add = order.calculate_total()
        status = "PASS" if actual_after_add == expected_after_add else "FAIL"
        results.append(("After add_item", expected_after_add, actual_after_add, status))

        if status == "FAIL":
            failed_steps.append(
                f"After add_item: expected {expected_after_add}, got {actual_after_add}"
            )

        # Step 3: Remove item
        order.remove_item("Pen")
        expected_after_remove = 45.0
        actual_after_remove = order.calculate_total()
        status = "PASS" if actual_after_remove == expected_after_remove else "FAIL"
        results.append(("After remove_item", expected_after_remove, actual_after_remove, status))

        if status == "FAIL":
            failed_steps.append(
                f"After remove_item: expected {expected_after_remove}, got {actual_after_remove}"
            )

        # Step 4: Check printed summary
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            order.print_summary()
            output = mock_stdout.getvalue()

        summary_ok = (
            "Order Summary for Alice" in output and
            "2 x Book @ $15.00" in output and
            "3 x Notebook @ $5.00" in output and
            "Total: $ 45.0" in output
        )

        status = "PASS" if summary_ok else "FAIL"
        results.append(("Print summary", "Correct output", "Correct output" if summary_ok else "Incorrect output", status))

        if status == "FAIL":
            failed_steps.append("Print summary: output did not match expected content")

        print("\n===== INTEGRATION TEST TABLE =====")
        print(f"{'Step':<20}{'Expected':<18}{'Actual':<18}{'Status':<8}")

        for step, expected, actual, status in results:
            print(f"{step:<20}{str(expected):<18}{str(actual):<18}{status:<8}")

        print("=== END test_03 ===")

        if failed_steps:
            self.fail(" ; ".join(failed_steps))


if __name__ == "__main__":
    unittest.main(verbosity=2)