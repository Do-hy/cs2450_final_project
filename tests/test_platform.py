# tests/test_platform.py

import unittest
from src.platform import PlatformManager
from src.brands import Brand


class TestPlatformManager(unittest.TestCase):
    def setUp(self):
        # reset singleton for tests (simple way: create new instance via "private" trick)
        PlatformManager._instance = None  # type: ignore[attr-defined]
        self.platform = PlatformManager.get_instance()

    def test_singleton(self):
        other = PlatformManager.get_instance()
        self.assertIs(self.platform, other)

    def test_brand_approval_flow(self):
        admin = self.platform.create_admin("Admin", "admin@example.com")
        owner = self.platform.register_brand_owner("Owner", "owner@example.com")
        brand = self.platform.request_brand(owner.user_id, "Test Brand")
        self.assertFalse(brand.approved)

        self.platform.approve_brand(admin.user_id, brand.brand_id)
        self.assertTrue(self.platform.brands[brand.brand_id].approved)


if __name__ == "__main__":
    unittest.main()
