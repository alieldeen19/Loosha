import subprocess
import unittest


def run_demo_command() -> str:
    completed = subprocess.run(
        "echo scan-demo",
        shell=True,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


class TestScanSample(unittest.TestCase):
    def test_run_demo_command(self) -> None:
        self.assertEqual(run_demo_command(), "scan-demo")
