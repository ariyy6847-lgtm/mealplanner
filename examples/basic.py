"""Minimal example for MealPlanner."""

from mealplanner import mealplanner


def main():
 runner = mealplanner({"name": "MealPlanner", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()