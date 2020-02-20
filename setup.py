from cx_Freeze import setup, Executable
base = None

executables = [Executable("gf_db.py", base=base)]

packages = ["pandas", "tkinter"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name='magic',
    version='0.1',
    packages=[''],
    url='https://github.com/s3nt3nz4/magic',
    license='',
    author='s3nt3nz4',
    author_email='',
    description='convert mtg goldfish > deckbox'
)
