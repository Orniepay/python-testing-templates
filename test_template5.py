# NOTE: pip install rich
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from time import sleep

from calculator import square  # Import your function here

console = Console()

# Define test functions for each case
def test_square_2():
    assert square(2) == 4, f"Expected 4, got {square(2)}"

def test_square_3():
    assert square(3) == 9, f"Expected 9, got {square(3)}"

def test_square_4():
    assert square(4) == 16, f"Expected 16, got {square(4)}"

def test_square_5():
    assert square(5) == 25, f"Expected 25, got {square(5)}"

def test_square_6():
    assert square(6) == 36, f"Expected 36, got {square(6)}"

# List of (name, function) test cases
tests = [
    ("test_square_2", test_square_2),
    ("test_square_3", test_square_3),
    ("test_square_4", test_square_4),
    ("test_square_5", test_square_5),
    ("test_square_6", test_square_6),
]

# Run tests with a progress bar and spinner
progress = Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(bar_width=None),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%")
)
with progress:
    task = progress.add_task("Running tests...", total=len(tests))
    results = []
    for name, func in tests:
        try:
            func()
            results.append((name, True))
        except AssertionError as e:
            results.append((name, False, str(e)))
        progress.advance(task)

# Display results summary
table = Table(show_header=True, header_style="bold")
table.add_column("Test")
table.add_column("Result")
table.add_column("Details")
for result in results:
    if result[1]:
        table.add_row(result[0], "[green]✅ PASS", "")
    else:
        table.add_row(result[0], "[red]❌ FAIL", result[2])
console.print(table)
