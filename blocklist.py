"""
blocklist.py
This file contains a set that acts as a blocklist for JWT tokens.
it will be imported and used in app.py
and the logout resource so that tockens can be added to it when users log out
and checked against it when users try to access protected resources.
"""

BLOCKLIST = set()
