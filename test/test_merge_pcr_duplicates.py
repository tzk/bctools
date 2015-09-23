import re
from filecmp import cmp
from scripttest import TestFileEnvironment

bindir = "bin/"
datadir = "test/data/"
testdir = "test/testenv_merge_pcr_dupes/"
env = TestFileEnvironment(testdir)
# relative to test file environment
bindir_rel = "../../" + bindir
datadir_rel = "../../" + datadir


def test_call_without_parameters():
    "Call merge_pcr_duplicates.py withouth any additional parameters."
    run = env.run(
        bindir_rel + "merge_pcr_duplicates.py",
        expect_error=True
    )
    assert(re.search("too few arguments", run.stderr))


def test_call_fileout():
    "Call merge_pcr_duplicates.py with infile and outfile."
    infile = "pcr_dupes.bed"
    outfile = "merged_pcr_dupes.bed"
    env.run(
        bindir_rel + "merge_pcr_duplicates.py",
        datadir_rel + infile,
        "--outfile", outfile
    )
    assert(cmp(
        testdir + outfile,
        datadir + "merged_pcr_dupes.bed"
    ))


def test_call_stdout():
    "Call merge_pcr_duplicates.py with infile."
    infile = "pcr_dupes.bed"
    outfile = "stdout_merged_pcr_dupes.bed"
    run = env.run(
        bindir_rel + "merge_pcr_duplicates.py",
        datadir_rel + infile
    )
    with open(testdir + outfile, "w") as b:
        b.write(run.stdout)
    assert(cmp(
        testdir + outfile,
        datadir + "merged_pcr_dupes.bed"
    ))
