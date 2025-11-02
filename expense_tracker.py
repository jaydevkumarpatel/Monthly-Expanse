#!/usr/bin/env python3
"""
Monthly Expense Tracker
A tool to analyze credit card statements and generate monthly expense reports.
"""

import csv
import os
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Tuple


class ExpenseTracker:
    """Main class for tracking and analyzing expenses."""
    
    # Common expense categories with keywords
    CATEGORIES = {
        'Food & Dining': ['restaurant', 'cafe', 'food', 'dining', 'pizza', 'burger', 'coffee', 'starbucks', 'mcdonald'],
        'Groceries': ['grocery', 'supermarket', 'walmart', 'target', 'whole foods', 'trader joe', 'costco', 'safeway'],
        'Transportation': ['gas', 'fuel', 'uber', 'lyft', 'taxi', 'parking', 'transit', 'metro', 'bus'],
        'Shopping': ['amazon', 'ebay', 'shop', 'store', 'mall', 'retail', 'clothing', 'fashion'],
        'Entertainment': ['movie', 'cinema', 'theater', 'netflix', 'spotify', 'gaming', 'entertainment', 'hulu'],
        'Utilities': ['electric', 'water', 'gas utility', 'internet', 'phone', 'mobile', 'cable', 'utility'],
        'Healthcare': ['pharmacy', 'doctor', 'hospital', 'medical', 'health', 'clinic', 'cvs', 'walgreens'],
        'Travel': ['hotel', 'airline', 'flight', 'airbnb', 'booking', 'travel', 'vacation'],
        'Bills & Fees': ['insurance', 'subscription', 'membership', 'fee', 'bill', 'payment'],
        'Other': []
    }
    
    def __init__(self):
        self.transactions = []
    
    def categorize_transaction(self, description: str) -> str:
        """Categorize a transaction based on its description."""
        description_lower = description.lower()
        
        for category, keywords in self.CATEGORIES.items():
            if category == 'Other':
                continue
            for keyword in keywords:
                if keyword in description_lower:
                    return category
        
        return 'Other'
    
    def load_csv(self, filepath: str) -> None:
        """
        Load transactions from a CSV file.
        Expected format: Date, Description, Amount
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Parse date (try multiple formats)
                    date_str = row['Date'].strip()
                    try:
                        date = datetime.strptime(date_str, '%Y-%m-%d')
                    except ValueError:
                        try:
                            date = datetime.strptime(date_str, '%m/%d/%Y')
                        except ValueError:
                            date = datetime.strptime(date_str, '%d/%m/%Y')
                    
                    description = row['Description'].strip()
                    amount = float(row['Amount'].replace('$', '').replace(',', '').strip())
                    
                    category = self.categorize_transaction(description)
                    
                    self.transactions.append({
                        'date': date,
                        'description': description,
                        'amount': amount,
                        'category': category
                    })
                except (ValueError, KeyError) as e:
                    print(f"Warning: Skipping invalid row: {row}. Error: {e}")
                    continue
    
    def get_monthly_report(self, year: int = None, month: int = None) -> Dict:
        """
        Generate a monthly expense report.
        If year/month not specified, uses current month.
        """
        if year is None or month is None:
            now = datetime.now()
            year = year or now.year
            month = month or now.month
        
        # Filter transactions for the specified month
        monthly_transactions = [
            t for t in self.transactions
            if t['date'].year == year and t['date'].month == month
        ]
        
        # Calculate totals by category
        category_totals = defaultdict(float)
        for transaction in monthly_transactions:
            category_totals[transaction['category']] += transaction['amount']
        
        # Calculate overall total
        total_spent = sum(category_totals.values())
        
        return {
            'year': year,
            'month': month,
            'transactions': monthly_transactions,
            'category_totals': dict(category_totals),
            'total_spent': total_spent,
            'transaction_count': len(monthly_transactions)
        }
    
    def get_all_months(self) -> List[Tuple[int, int]]:
        """Get all unique year-month combinations in the data."""
        months = set()
        for transaction in self.transactions:
            months.add((transaction['date'].year, transaction['date'].month))
        return sorted(list(months))
    
    def print_monthly_report(self, year: int = None, month: int = None) -> None:
        """Print a formatted monthly expense report."""
        report = self.get_monthly_report(year, month)
        
        month_name = datetime(report['year'], report['month'], 1).strftime('%B %Y')
        
        print("\n" + "=" * 60)
        print(f"MONTHLY EXPENSE REPORT - {month_name}".center(60))
        print("=" * 60)
        print()
        
        # Print category breakdown
        print("EXPENSE BREAKDOWN BY CATEGORY:")
        print("-" * 60)
        
        # Sort categories by amount spent (descending)
        sorted_categories = sorted(
            report['category_totals'].items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        for category, amount in sorted_categories:
            percentage = (amount / report['total_spent'] * 100) if report['total_spent'] > 0 else 0
            print(f"{category:<25} ${amount:>10.2f}  ({percentage:>5.1f}%)")
        
        print("-" * 60)
        print(f"{'TOTAL SPENT':<25} ${report['total_spent']:>10.2f}")
        print(f"{'Number of Transactions':<25} {report['transaction_count']:>10}")
        print("=" * 60)
        print()
    
    def export_report_to_csv(self, output_file: str, year: int = None, month: int = None) -> None:
        """Export monthly report to a CSV file."""
        report = self.get_monthly_report(year, month)
        
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write header
            month_name = datetime(report['year'], report['month'], 1).strftime('%B %Y')
            writer.writerow(['Monthly Expense Report', month_name])
            writer.writerow([])
            
            # Write category summary
            writer.writerow(['Category', 'Amount', 'Percentage'])
            sorted_categories = sorted(
                report['category_totals'].items(),
                key=lambda x: x[1],
                reverse=True
            )
            
            for category, amount in sorted_categories:
                percentage = (amount / report['total_spent'] * 100) if report['total_spent'] > 0 else 0
                writer.writerow([category, f"${amount:.2f}", f"{percentage:.1f}%"])
            
            writer.writerow([])
            writer.writerow(['Total Spent', f"${report['total_spent']:.2f}"])
            writer.writerow(['Number of Transactions', report['transaction_count']])
            writer.writerow([])
            
            # Write detailed transactions
            writer.writerow(['Detailed Transactions'])
            writer.writerow(['Date', 'Description', 'Category', 'Amount'])
            
            for transaction in sorted(report['transactions'], key=lambda x: x['date']):
                writer.writerow([
                    transaction['date'].strftime('%Y-%m-%d'),
                    transaction['description'],
                    transaction['category'],
                    f"${transaction['amount']:.2f}"
                ])
        
        print(f"Report exported to: {output_file}")


def main():
    """Main function to demonstrate usage."""
    import sys
    
    tracker = ExpenseTracker()
    
    # Check if a CSV file was provided as argument
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
        if not os.path.exists(csv_file):
            print(f"Error: File '{csv_file}' not found.")
            print("\nUsage: python expense_tracker.py [statement.csv]")
            sys.exit(1)
        
        print(f"Loading transactions from: {csv_file}")
        tracker.load_csv(csv_file)
        print(f"Loaded {len(tracker.transactions)} transactions.")
        
        # Generate reports for all months in the data
        months = tracker.get_all_months()
        
        if not months:
            print("No valid transactions found.")
            sys.exit(1)
        
        for year, month in months:
            tracker.print_monthly_report(year, month)
            
            # Export to CSV
            month_name = datetime(year, month, 1).strftime('%Y-%m')
            output_file = f"expense_report_{month_name}.csv"
            tracker.export_report_to_csv(output_file, year, month)
    else:
        print("Monthly Expense Tracker")
        print("\nUsage: python expense_tracker.py <statement.csv>")
        print("\nExpected CSV format:")
        print("Date,Description,Amount")
        print("2024-01-15,Starbucks Coffee,5.99")
        print("2024-01-16,Walmart Groceries,85.42")
        print("\nSee sample_statement.csv for an example.")


if __name__ == "__main__":
    main()
