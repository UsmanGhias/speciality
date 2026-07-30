# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged("post_install", "-at_install")
class TestSpeciality(TransactionCase):
    """Odoo TransactionCase tests for speciality.speciality.

    These tests require an Odoo test environment. They are authored here for
    real coverage but may be marked as "not executed" when Odoo is unavailable
    on the local machine or CI runner.
    """

    def setUp(self):
        super().setUp()
        self.Speciality = self.env["speciality.speciality"]

    def test_create_speciality(self):
        record = self.Speciality.create(
            {
                "name": "Cardiology",
                "code": "CARDIO",
                "sequence": 5,
                "description": "Heart-related speciality",
            }
        )
        self.assertTrue(record.id)
        self.assertEqual(record.name, "Cardiology")
        self.assertEqual(record.code, "CARDIO")
        self.assertTrue(record.active)
        self.assertEqual(record.sequence, 5)

    def test_required_name(self):
        with self.assertRaises(Exception):
            self.Speciality.create({"code": "NO_NAME"})

    def test_unique_code_validation(self):
        self.Speciality.create({"name": "One", "code": "UNIQUE1"})
        with self.assertRaises(Exception):
            self.Speciality.create({"name": "Two", "code": "UNIQUE1"})

    def test_active_flag(self):
        record = self.Speciality.create({"name": "Archivable", "code": "ARCH1"})
        self.assertTrue(record.active)
        record.write({"active": False})
        self.assertFalse(record.active)

    def test_sequence_ordering(self):
        second = self.Speciality.create({"name": "B", "code": "B1", "sequence": 20})
        first = self.Speciality.create({"name": "A", "code": "A1", "sequence": 10})
        ordered = self.Speciality.search([("code", "in", ["A1", "B1"])])
        self.assertEqual(ordered[0].id, first.id)
        self.assertEqual(ordered[1].id, second.id)

    def test_update_behavior(self):
        record = self.Speciality.create({"name": " Old ", "code": " OLD "})
        self.assertEqual(record.name, "Old")
        self.assertEqual(record.code, "OLD")
        record.write({"name": " New ", "code": " NEW "})
        self.assertEqual(record.name, "New")
        self.assertEqual(record.code, "NEW")

    def test_duplicate_code_spaces_rejected(self):
        with self.assertRaises(ValidationError):
            self.Speciality.create({"name": "Bad", "code": "BAD CODE"})
