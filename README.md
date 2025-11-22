# Gilded Rose Refactoring Exercise

## Objective
Refactor legacy code while maintaining functionality through comprehensive unit testing.

## Background
The Gilded Rose is an inventory management system that updates item quality based on special rules. The existing code in `template/gilded_rose.py` works but is deeply nested and hard to maintain.

## Item Rules
- **Normal items**: Quality decreases by 1 per day, by 2 after sell-by date
- **Aged Brie**: Quality increases by 1 per day, by 2 after sell-by date
- **Sulfuras**: Legendary item - never changes quality or sell_in date
- **Conjured items**: Quality decreases by 2 per day, by 4 after sell-by date. Aged Brie and Sulfuras cannot be conjured.
- **Quality constraints**: Never negative, never exceeds 50 (except Sulfuras at 80)

## Task

### Part 1: Write Tests
Create comprehensive unit tests in `test_gilded_rose.py` that verify:
- Normal item degradation (before and after expiry)
- Aged Brie quality increases
- Sulfuras remains constant
- Conjured items degrade twice as fast
- Quality boundaries (0-50 cap)

### Part 2: Refactor
Refactor `gilded_rose.py` to improve:
- Reduce nesting and complexity
- Extract helper functions
- Improve readability
- Ensure all tests still pass

## Running Tests
```bash
python -m unittest test_gilded_rose.py
```

## Success Criteria
- All tests pass before refactoring
- All tests pass after refactoring
- Code is more maintainable and readable
- No functionality changes
