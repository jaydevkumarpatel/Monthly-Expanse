#!/usr/bin/env python3
"""
Test script for the expense tracker
"""

import os
import sys
from datetime import datetime
from expense_tracker import ExpenseTracker


def test_categorization():
    """Test expense categorization."""
    tracker = ExpenseTracker()
    
    test_cases = [
        ("Starbucks Coffee", "Food & Dining"),
        ("Walmart Groceries", "Groceries"),
        ("Shell Gas", "Transportation"),
        ("Amazon Prime", "Shopping"),
        ("Netflix", "Entertainment"),
        ("Electric Company", "Utilities"),
        ("CVS Pharmacy", "Healthcare"),
        ("Delta Airlines", "Travel"),
        ("Insurance Payment", "Bills & Fees"),
        ("Unknown Merchant", "Other"),
    ]
    
    print("Testing categorization...")
    passed = 0
    failed = 0
    
    for description, expected_category in test_cases:
        result = tracker.categorize_transaction(description)
        if result == expected_category:
            print(f"✓ '{description}' -> {result}")
            passed += 1
        else:
            print(f"✗ '{description}' -> Expected: {expected_category}, Got: {result}")
            failed += 1
    
    print(f"\nCategorization Tests: {passed} passed, {failed} failed")
    return failed == 0


def test_csv_loading():
    """Test CSV loading functionality."""
    tracker = ExpenseTracker()
    
    print("\nTesting CSV loading...")
    tracker.load_csv('sample_statement.csv')
    
    if len(tracker.transactions) > 0:
        print(f"✓ Loaded {len(tracker.transactions)} transactions")
        return True
    else:
        print("✗ Failed to load transactions")
        return False


def test_monthly_report():
    """Test monthly report generation."""
    tracker = ExpenseTracker()
    tracker.load_csv('sample_statement.csv')
    
    print("\nTesting monthly report generation...")
    report = tracker.get_monthly_report(2024, 10)
    
    checks = [
        (report['year'] == 2024, "Year is correct"),
        (report['month'] == 10, "Month is correct"),
        (report['total_spent'] > 0, "Total spent is positive"),
        (report['transaction_count'] > 0, "Has transactions"),
        (len(report['category_totals']) > 0, "Has categories"),
    ]
    
    all_passed = True
    for check, description in checks:
        if check:
            print(f"✓ {description}")
        else:
            print(f"✗ {description}")
            all_passed = False
    
    return all_passed


def test_export():
    """Test CSV export functionality."""
    tracker = ExpenseTracker()
    tracker.load_csv('sample_statement.csv')
    
    print("\nTesting CSV export...")
    test_output = '/tmp/test_report.csv'
    tracker.export_report_to_csv(test_output, 2024, 10)
    
    if os.path.exists(test_output):
        print(f"✓ Report exported successfully")
        os.remove(test_output)
        return True
    else:
        print(f"✗ Failed to export report")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("EXPENSE TRACKER TEST SUITE")
    print("=" * 60)
    
    # Change to script directory
    os.chdir('/home/runner/work/Monthly-Expanse/Monthly-Expanse')
    
    results = []
    results.append(("Categorization", test_categorization()))
    results.append(("CSV Loading", test_csv_loading()))
    results.append(("Monthly Report", test_monthly_report()))
    results.append(("CSV Export", test_export()))
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "PASSED" if result else "FAILED"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {test_name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print("\n❌ Some tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
