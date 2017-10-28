import unittest
import os

from octoscat import (
    shannon_entropy,
    find_suspicious_strings,
    B64_CHARS,
    HEX_CHARS,
)

SAMPLE_TEXT = '''This is a test to see how this thing actually works. First I'll write a normal
sentence, and then I'll write some weird base64 strings like VGhpcyB0ZXN0IHN0cmluZyBzaG91bGQgdHJpZ2dlcgo==
and maybe even some hex strings like 1234567890abcdefABCDEF'''  # noqa

class TestOctoScat(unittest.TestCase):
    def setUp(self):
        base_path = os.path.join(os.getcwd(), os.path.dirname(__file__))
        self.fixtures_path = os.path.join(base_path, 'fixtures.txt')

    def test_shannon_entropy(self):
        b64_string = "VGhpcyB0ZXN0IHN0cmluZyBzaG91bGQgdHJpZ2dlcgo="
        hex_string = "882413967d2daa61eae1e3c989f369ef0752154b"
        self.assertGreater(shannon_entropy(b64_string), 4.5)
        self.assertGreater(shannon_entropy(hex_string), 3)

    def test_b64_suspicious_strings(self):
        exp_strings = [
            'VGhpcyB0ZXN0IHN0cmluZyBzaG91bGQgdHJpZ2dlcgo==',
            '1234567890abcdefABCDEF'
        ]
        actual_strings = find_suspicious_strings(SAMPLE_TEXT, B64_CHARS)
        self.assertEqual(actual_strings, exp_strings)

    def test_hex_suspicious_strings(self):
        exp_strings = ['1234567890abcdefABCDEF']
        actual_strings = find_suspicious_strings(SAMPLE_TEXT, HEX_CHARS)
        self.assertEqual(actual_strings, exp_strings)

if __name__ == '__main__':
    unittest.main()
