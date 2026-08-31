"""
We are building Floating License Pool, a back-end system that manages a shared pool of floating software licenses used by an internal engineering tools team.

Definitions:
* A "license" is an object representing one floating software license in the shared pool. A license has:
  - license_id
  - status
  - assigned_user_id
  - checked_out_at (the time a license was assigned to a user)
  - last_heartbeat_at (the most recent time the checked-out client confirmed it's still actively using the license)

* A license's status can be one of:
  - AVAILABLE
  - IN_USE

The LicensePoolManager class manages the pool of licenses.

To begin with, we present you with two tasks:

1-1) Read through and understand the code below. Feel free to run it.
1-2) The test for LicensePoolManager is not passing due to a bug in the code. Make the necessary changes to LicensePoolManager to fix the bug.
"""



"""
We are extending Floating License Pool to let users check out and return licenses. This lets an engineer get a license when they need one, and free it up for someone else when they're done.

Add two functions to the LicensePoolManager class.

2-1) checkout_license

The checkout_license function takes a user ID and the current time. It should assign an available license to that user, following these rules:
- A user may hold at most one license at a time; ignore the request if the user already holds one.
- When more than one license is available, assign the one with the lowest license_id.
- Set the license status to IN_USE, store the assigned user, and set both the checkout time and heartbeat time to the given current time.

Return the assigned license_id, or None if no license is available or the user already holds one.

2-2) return_license

The return_license function takes a user ID. It should find the license currently held by that user, set its status to AVAILABLE, and clear the assigned user, checkout time, and heartbeat time.

Return true when a license is returned, and false if the user does not hold a license.

Example:
- Licenses 2 and 4 are AVAILABLE.
- Checking out a license for U-1 at time 100 assigns license 2, the lowest available id.
- If U-1 tries to check out again at time 150, the request returns None, since they already hold a license.
"""

import unittest


class License:
    def __init__(
        self,
        license_id,
        status,
        assigned_user_id=None,
        checked_out_at=None,
        last_heartbeat_at=None
    ):
        """Represents a single floating license and its current checkout state."""
        self.license_id = license_id
        self.status = status
        self.assigned_user_id = assigned_user_id
        self.checked_out_at = checked_out_at
        self.last_heartbeat_at = last_heartbeat_at


class WaitingRequest:
    def __init__(self, request_id, user_id, requested_at, status):
        self.request_id = request_id
        self.user_id = user_id
        self.requested_at = requested_at
        self.status = status


class LicensePoolManager:
    def __init__(self):
        """Manages the pool of licenses, keyed by license ID."""
        self.licenses = {}
        self.waiting_requests = []

    def is_license_available(self, license):
        return (
            license.status == "AVAILABLE"
            and license.assigned_user_id is None
        )

    def checkout_license(self, user_ID, current_time):
        # First check whether this user already holds a license.
        for license in self.licenses.values():
            if (
                license.status == "IN_USE"
                and license.assigned_user_id == user_ID
            ):
                return None

        # Find the lowest-ID available license.
        available_licenses = [
            license
            for license in self.licenses.values()
            if self.is_license_available(license)
        ]

        if not available_licenses:
            return None

        license = min(
            available_licenses,
            key=lambda license: license.license_id
        )

        # Assign the license.
        license.status = "IN_USE"
        license.assigned_user_id = user_ID
        license.checked_out_at = current_time
        license.last_heartbeat_at = current_time

        return license.license_id

    def return_license(self, user_ID):
        # Find the license currently held by this user.
        for license in self.licenses.values():
            if (
                license.status == "IN_USE"
                and license.assigned_user_id == user_ID
            ):
                license.status = "AVAILABLE"
                license.assigned_user_id = None
                license.checked_out_at = None
                license.last_heartbeat_at = None

                return True

        return False

            

class TestSuite(unittest.TestCase):
    def test_is_license_available_1(self):
        """Test is_license_available for AVAILABLE, unassigned licenses."""
        print("Running test_is_license_available_1")

        manager = LicensePoolManager()

        # Available, unassigned license using default (omitted) assigned_user_id
        license_default = License(1, "AVAILABLE")
        self.assertTrue(manager.is_license_available(license_default))

        # Available license with explicit null fields
        license_explicit_null = License(
            2, "AVAILABLE", assigned_user_id=None, checked_out_at=None, last_heartbeat_at=None
        )
        self.assertTrue(manager.is_license_available(license_explicit_null))

    def test_is_license_available_2(self):
        """Test is_license_available for IN_USE licenses, both assigned and unassigned."""
        print("Running test_is_license_available_2")

        manager = LicensePoolManager()

        # In-use license that is assigned to a user
        license_assigned = License(
            1, "IN_USE", assigned_user_id="U-1", checked_out_at=10, last_heartbeat_at=10
        )
        self.assertFalse(manager.is_license_available(license_assigned))

        # IN_USE license with no assigned user.
        license_unassigned = License(3, "IN_USE", assigned_user_id=None)
        self.assertFalse(manager.is_license_available(license_unassigned))

    def test_is_license_available_3(self):
        """Test is_license_available for AVAILABLE licenses with an assigned user."""
        print("Running test_is_license_available_3")

        manager = LicensePoolManager()

        # Available license that still has an assigned user
        license_with_user = License(4, "AVAILABLE", assigned_user_id="U-2")
        self.assertFalse(manager.is_license_available(license_with_user))

        # AVAILABLE license with an empty string assigned user.
        license_empty_user = License(5, "AVAILABLE", assigned_user_id="")
        self.assertFalse(manager.is_license_available(license_empty_user))

    def test_is_license_available_4(self):
        """Test is_license_available across a pool with mixed statuses and assignments."""
        print("Running test_is_license_available_4")

        manager = LicensePoolManager()
        manager.licenses[1] = License(1, "AVAILABLE")
        manager.licenses[2] = License(
            2, "IN_USE", assigned_user_id="U-1", checked_out_at=10, last_heartbeat_at=10
        )
        manager.licenses[3] = License(3, "AVAILABLE")
        manager.licenses[4] = License(
            4, "IN_USE", assigned_user_id="U-2", checked_out_at=20, last_heartbeat_at=20
        )

        available_ids = [
            license.license_id
            for license in manager.licenses.values()
            if manager.is_license_available(license)
        ]

        self.assertEqual([1, 3], sorted(available_ids))

    def test_checkout_license_1(self):
        """Test that checkout_license assigns an available license and sets all of its fields."""
        print("Running test_checkout_license_1")

        manager = LicensePoolManager()
        manager.licenses[1] = License(1, "AVAILABLE")

        license_id = manager.checkout_license("U-1", 100)

        self.assertEqual(1, license_id)
        license = manager.licenses[1]
        self.assertEqual("IN_USE", license.status)
        self.assertEqual("U-1", license.assigned_user_id)
        self.assertEqual(100, license.checked_out_at)
        self.assertEqual(100, license.last_heartbeat_at)

    def test_checkout_license_2(self):
        """Test checkout_license when multiple licenses are available."""
        print("Running test_checkout_license_2")

        manager = LicensePoolManager()
        manager.licenses[5] = License(5, "AVAILABLE")
        manager.licenses[2] = License(2, "AVAILABLE")

        license_id = manager.checkout_license("U-1", 100)

        # Multiple licenses available.
        self.assertEqual(2, license_id)

    def test_checkout_license_3(self):
        """Test that checkout_license returns None whenever there is nothing to assign: the user already holds a license, no license is available, or the pool is empty."""
        print("Running test_checkout_license_3")

        # No license available: the only license in the pool is already IN_USE.
        manager = LicensePoolManager()
        manager.licenses[1] = License(1, "IN_USE", assigned_user_id="U-2")

        license_id = manager.checkout_license("U-1", 100)

        self.assertIsNone(license_id)

        # User already holds a license, and another license is available.
        manager = LicensePoolManager()
        manager.licenses[1] = License(1, "IN_USE", assigned_user_id="U-1")
        manager.licenses[2] = License(2, "AVAILABLE")

        license_id = manager.checkout_license("U-1", 100)

        self.assertIsNone(license_id)
        # The available license must remain untouched.
        self.assertEqual("AVAILABLE", manager.licenses[2].status)

        # Empty pool: there are no licenses at all.
        manager = LicensePoolManager()

        license_id = manager.checkout_license("U-1", 100)

        self.assertIsNone(license_id)

    def test_checkout_license_4(self):
        """Test that checkout_license skips a lower-id license already IN_USE and held by a
        different user, assigning the available higher-id license instead."""
        print("Running test_checkout_license_4")

        manager = LicensePoolManager()
        manager.licenses[1] = License(1, "IN_USE", assigned_user_id="U-1")
        manager.licenses[2] = License(2, "AVAILABLE")

        license_id = manager.checkout_license("U-3", 200)

        self.assertEqual(2, license_id)
        license2 = manager.licenses[2]
        self.assertEqual("IN_USE", license2.status)
        self.assertEqual("U-3", license2.assigned_user_id)
        self.assertEqual(200, license2.checked_out_at)
        self.assertEqual(200, license2.last_heartbeat_at)

        # The lower-id license, held by a different user, must remain untouched.
        license1 = manager.licenses[1]
        self.assertEqual("IN_USE", license1.status)
        self.assertEqual("U-1", license1.assigned_user_id)

    def test_return_license_1(self):
        """Test that return_license clears an in-use license's fields and makes it available."""
        print("Running test_return_license_1")

        manager = LicensePoolManager()
        manager.licenses[1] = License(
            1, "IN_USE", assigned_user_id="U-1", checked_out_at=100, last_heartbeat_at=150
        )

        result = manager.return_license("U-1")

        self.assertTrue(result)
        license = manager.licenses[1]
        self.assertEqual("AVAILABLE", license.status)
        self.assertIsNone(license.assigned_user_id)
        self.assertIsNone(license.checked_out_at)
        self.assertIsNone(license.last_heartbeat_at)

    def test_return_license_2(self):
        """Test that return_license returns false when the user does not hold a license."""
        print("Running test_return_license_2")

        manager = LicensePoolManager()
        manager.licenses[1] = License(1, "AVAILABLE")

        result = manager.return_license("U-1")

        self.assertFalse(result)

    def test_return_license_3(self):
        """Test that a license freed by return_license can immediately be checked out by another user."""
        print("Running test_return_license_3")

        manager = LicensePoolManager()
        manager.licenses[1] = License(1, "IN_USE", assigned_user_id="U-1")

        manager.return_license("U-1")
        license_id = manager.checkout_license("U-2", 200)

        self.assertEqual(1, license_id)
        self.assertEqual("U-2", manager.licenses[1].assigned_user_id)

    def test_return_license_4(self):
        """Test return_license with an unrelated license present, followed by a checkout_license call."""
        print("Running test_return_license_4")

        manager = LicensePoolManager()
        manager.licenses[5] = License(
            5, "IN_USE", assigned_user_id="U-1", checked_out_at=100, last_heartbeat_at=150
        )
        manager.licenses[2] = License(2, "AVAILABLE")

        result = manager.return_license("U-1")

        self.assertTrue(result)
        license5 = manager.licenses[5]
        self.assertEqual("AVAILABLE", license5.status)
        self.assertIsNone(license5.assigned_user_id)
        self.assertIsNone(license5.checked_out_at)
        self.assertIsNone(license5.last_heartbeat_at)

        # Unrelated license present.
        license2 = manager.licenses[2]
        self.assertEqual("AVAILABLE", license2.status)
        self.assertIsNone(license2.assigned_user_id)
        self.assertIsNone(license2.checked_out_at)
        self.assertIsNone(license2.last_heartbeat_at)

        # Checkout after return.
        license_id = manager.checkout_license("U-2", 200)

        self.assertEqual(2, license_id)
        self.assertEqual("AVAILABLE", manager.licenses[5].status)

if __name__ == "__main__":
    unittest.main()
