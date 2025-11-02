#!/usr/bin/env python3
"""
Example script showing how to use the ExpenseTracker programmatically.
This demonstrates using the tracker as a library in your own scripts.
"""

from expense_tracker import ExpenseTracker
from datetime import datetime


def example_usage():
    """Demonstrate various ways to use the ExpenseTracker."""
    
    # Create an instance of the tracker
    tracker = ExpenseTracker()
    
    # Load transactions from a CSV file
    print("Loading transactions from sample_statement.csv...")
    tracker.load_csv('sample_statement.csv')
    print(f"Loaded {len(tracker.transactions)} transactions\n")
    
    # Get all available months in the data
    print("Available months in the data:")
    months = tracker.get_all_months()
    for year, month in months:
        month_name = datetime(year, month, 1).strftime('%B %Y')
        print(f"  - {month_name}")
    print()
    
    # Get a specific month's report
    print("Getting October 2024 report...")
    oct_report = tracker.get_monthly_report(2024, 10)
    
    # Access report data programmatically
    print(f"Total spent in October: ${oct_report['total_spent']:.2f}")
    print(f"Number of transactions: {oct_report['transaction_count']}")
    print()
    
    # Analyze spending by category
    print("Top 3 spending categories in October:")
    sorted_categories = sorted(
        oct_report['category_totals'].items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    for i, (category, amount) in enumerate(sorted_categories[:3], 1):
        percentage = (amount / oct_report['total_spent'] * 100)
        print(f"  {i}. {category}: ${amount:.2f} ({percentage:.1f}%)")
    print()
    
    # Print formatted report to console
    print("Full formatted report:")
    tracker.print_monthly_report(2024, 10)
    
    # Export to CSV for further analysis
    print("Exporting to CSV...")
    tracker.export_report_to_csv('my_october_report.csv', 2024, 10)
    
    # Example: Find all transactions in a specific category
    print("\nAll Travel expenses in October:")
    for transaction in oct_report['transactions']:
        if transaction['category'] == 'Travel':
            print(f"  {transaction['date'].strftime('%Y-%m-%d')}: "
                  f"{transaction['description']} - ${transaction['amount']:.2f}")
    
    # Example: Calculate average transaction amount
    if oct_report['transaction_count'] > 0:
        avg_transaction = oct_report['total_spent'] / oct_report['transaction_count']
        print(f"\nAverage transaction amount: ${avg_transaction:.2f}")


def compare_months():
    """Example: Compare spending across multiple months."""
    tracker = ExpenseTracker()
    tracker.load_csv('sample_statement.csv')
    
    print("\n" + "=" * 60)
    print("MONTH-TO-MONTH COMPARISON")
    print("=" * 60)
    
    months = tracker.get_all_months()
    
    for year, month in months:
        report = tracker.get_monthly_report(year, month)
        month_name = datetime(year, month, 1).strftime('%B %Y')
        print(f"{month_name}: ${report['total_spent']:.2f} "
              f"({report['transaction_count']} transactions)")


def analyze_spending_trends():
    """Example: Analyze spending trends by category."""
    tracker = ExpenseTracker()
    tracker.load_csv('sample_statement.csv')
    
    print("\n" + "=" * 60)
    print("CATEGORY SPENDING TRENDS")
    print("=" * 60)
    
    months = tracker.get_all_months()
    
    # Track spending by category across months
    category_trends = {}
    
    for year, month in months:
        report = tracker.get_monthly_report(year, month)
        month_name = datetime(year, month, 1).strftime('%b %Y')
        
        for category, amount in report['category_totals'].items():
            if category not in category_trends:
                category_trends[category] = {}
            category_trends[category][month_name] = amount
    
    # Display trends
    for category in sorted(category_trends.keys()):
        print(f"\n{category}:")
        for month, amount in category_trends[category].items():
            print(f"  {month}: ${amount:.2f}")


if __name__ == "__main__":
    # Run the examples
    example_usage()
    compare_months()
    analyze_spending_trends()
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
