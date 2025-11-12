"""
Bengkel AutoCare - Automotive Workshop Booking System
Entry point — see bengkel/, core/, booking/, payment/ packages for actual implementation.

This file now serves as a reference to the refactored Django project structure.
Run: python manage.py runserver to start the project.
"""

from pathlib import Path

ROOT = Path(__file__).parent

if __name__ == '__main__':
    print("✓ Bengkel AutoCare project structure is ready!")
    print(f"  Root directory: {ROOT}")
    print("  Run 'python manage.py runserver' to start the development server.")

