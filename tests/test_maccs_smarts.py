"""Test if SMARTS patterns are valid."""

import unittest

from molshap.maccs_smarts import MACCS_KEYS
from rdkit import Chem


class TestSMARTSPattern(unittest.TestCase):
    def test_validity(self) -> None:
        """Test is SMARTS are valid."""
        for key, smarts in MACCS_KEYS.items():
            with self.subTest(f"Testing key: {key}"):
                smarts_obj = Chem.MolFromSmarts(smarts)
                self.assertIsNotNone(smarts_obj)


if __name__ == '__main__':
    unittest.main()
