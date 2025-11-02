# Monthly Expense Tracker

A Python application to analyze credit card statements and generate detailed monthly expense reports.

## Features

- 📊 Parse credit card statements from CSV files
- 🏷️ Automatic expense categorization
- 📈 Monthly expense reports with category breakdowns
- 💾 Export reports to CSV format
- 📅 Support for multiple date formats
- 🎯 Percentage-based spending analysis

## Categories

The application automatically categorizes expenses into:

- **Food & Dining** - Restaurants, cafes, fast food
- **Groceries** - Supermarkets and grocery stores
- **Transportation** - Gas, Uber, Lyft, parking
- **Shopping** - Amazon, retail stores, clothing
- **Entertainment** - Movies, streaming services, gaming
- **Utilities** - Electric, water, internet, phone
- **Healthcare** - Pharmacy, doctors, medical
- **Travel** - Hotels, airlines, bookings
- **Bills & Fees** - Insurance, subscriptions, memberships
- **Other** - Uncategorized expenses

## Installation

No external dependencies required! Uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/jaydevkumarpatel/Monthly-Expanse.git
cd Monthly-Expanse

# Run with Python 3.6 or higher
python3 expense_tracker.py sample_statement.csv
```

## Usage

### Basic Usage

```bash
python expense_tracker.py your_statement.csv
```

### CSV File Format

Your credit card statement CSV should have the following format:

```csv
Date,Description,Amount
2024-10-01,Starbucks Coffee,6.75
2024-10-02,Walmart Groceries,124.50
2024-10-03,Shell Gas Station,45.00
```

**Supported date formats:**
- `YYYY-MM-DD` (2024-10-01)
- `MM/DD/YYYY` (10/01/2024)
- `DD/MM/YYYY` (01/10/2024)

### Example Output

```
============================================================
        MONTHLY EXPENSE REPORT - October 2024
============================================================

EXPENSE BREAKDOWN BY CATEGORY:
------------------------------------------------------------
Travel                        $534.00  ( 35.2%)
Groceries                     $266.45  ( 17.6%)
Shopping                      $227.08  ( 15.0%)
Utilities                     $170.50  ( 11.2%)
Transportation                $122.50  (  8.1%)
...
------------------------------------------------------------
TOTAL SPENT                  $1516.15
Number of Transactions             20
============================================================
```

### Generated Files

The application generates CSV reports for each month found in your data:
- `expense_report_2024-10.csv`
- `expense_report_2024-11.csv`

Each report includes:
- Category summary with amounts and percentages
- Total spent
- Transaction count
- Detailed transaction list

## Sample Data

A sample credit card statement (`sample_statement.csv`) is included in the repository. Try it out:

```bash
python expense_tracker.py sample_statement.csv
```

## Customization

### Adding Custom Categories

Edit the `CATEGORIES` dictionary in `expense_tracker.py`:

```python
CATEGORIES = {
    'Your Category': ['keyword1', 'keyword2', 'keyword3'],
    # ... other categories
}
```

### Date Format

The application supports multiple date formats automatically. If you need to add a new format, modify the `load_csv` method.

## Use Cases

- 📝 Monthly budgeting
- 💰 Expense tracking
- 📊 Financial analysis
- 🎯 Spending pattern identification
- 💳 Credit card statement analysis

## Requirements

- Python 3.6 or higher
- No external dependencies

## Contributing

Contributions are welcome! Feel free to:
- Add new expense categories
- Improve categorization algorithms
- Add new report formats
- Enhance documentation

## License

MIT License - feel free to use this for personal or commercial projects.

## Tips

1. **Regular Updates**: Import your credit card statements monthly for best tracking
2. **Category Customization**: Adjust keywords to match your spending patterns
3. **Multiple Cards**: Combine statements from different cards into one CSV
4. **Data Privacy**: All processing is local - your financial data stays on your machine

## Troubleshooting

**Issue**: "File not found" error  
**Solution**: Make sure the CSV file path is correct

**Issue**: Transactions not categorizing correctly  
**Solution**: Add custom keywords to the category definitions

**Issue**: Date parsing errors  
**Solution**: Ensure your dates are in YYYY-MM-DD, MM/DD/YYYY, or DD/MM/YYYY format

## Example Workflow

1. Export your credit card statement as CSV
2. Format it to match the required structure (Date, Description, Amount)
3. Run the tracker: `python expense_tracker.py statement.csv`
4. Review the console output for quick insights
5. Open the generated CSV files for detailed analysis
6. Use the reports for budgeting and financial planning

---

**Happy tracking! 💰📊**