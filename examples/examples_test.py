import filecmp
import os

from testfixtures import TempDirectory

import katana.clipper as clipper
from test.util_test import KatanaBaseTestCase


INPUT_DIR=os.path.realpath(os.path.dirname(__file__))

class ExamplesFunctionalTest(KatanaBaseTestCase):
    def test_examples(self):
        with TempDirectory() as temp_dir:
            output_dir = temp_dir.path
            input_bam = "chr10.pten.bam"
            output_bam = "chr10.pten.clipped.bam"
            output_bai = output_bam + ".bai"
            input_primer_filename = os.path.join(INPUT_DIR, "primers.txt")
            input_bam_filename = os.path.join(INPUT_DIR, input_bam)
            expect_bam_filename = os.path.join(INPUT_DIR, output_bam)
            expect_bai_filename = os.path.join(INPUT_DIR, output_bai)
            output_bam_filename = os.path.join(output_dir, output_bam)
            output_bai_filename = os.path.join(output_dir, output_bai)
            clipper.main(["program_name",
                          input_primer_filename,
                          input_bam_filename,
                          output_bam_filename])
            self.assertTrue(filecmp.cmp(expect_bam_filename,
                                        output_bam_filename),
                            "{} does not match expected".format(output_bam))
            bai_stat_info = os.stat(output_bai_filename)
            self.assertTrue(bai_stat_info.st_size > 0)

    def test_preserve_all_alignments(self):
        with TempDirectory() as temp_dir:
            output_dir = temp_dir.path
            input_bam = "chr10.pten.bam"
            output_bam = "chr10.pten.clipped-preserve_all_alignments.bam"
            output_bai = output_bam + ".bai"
            input_primer_filename = os.path.join(INPUT_DIR, "primers.txt")
            input_bam_filename = os.path.join(INPUT_DIR, input_bam)
            expect_bam_filename = os.path.join(INPUT_DIR, output_bam)
            expect_bai_filename = os.path.join(INPUT_DIR, output_bai)
            output_bam_filename = os.path.join(output_dir, output_bam)
            output_bai_filename = os.path.join(output_dir, output_bai)
            clipper.main(["program_name",
                          "--preserve_all_alignments",
                          input_primer_filename,
                          input_bam_filename,
                          output_bam_filename])
            msg = "{} does not match expected"
            self.assertTrue(filecmp.cmp(expect_bam_filename,
                                        output_bam_filename),
                            msg.format(output_bam))
            bai_stat_info = os.stat(output_bai_filename)
            self.assertTrue(bai_stat_info.st_size > 0)
