# FrameVM

Spoofax projects for the FrameVM and Racket compiler. Created as part of a master thesis.

## Using the project
To run this code [Spoofax](https://www.metaborg.org/en/latest/) needs to be installed.
In order to generate new tests based on the example Racket programs in `TinyRacket.example` [Python](https://www.python.org/) and [Racket](https://racket-lang.org/) also need to be installed.

## Projects
There are two Spoofax projects in this repository.

### Framed
All code belonging to the Framed language and the FrameVM, split in three folders
- `Framed` contains the definition and the interpreter
- `Framed.Example` can be used to write example Framed programs
- `Framed.test` contains all the tests for Framed and the FrameVM

### TinyRacket
All code belonging to the Racket implementation and its compiler, split in three folders
- `TinyRacket` contains the definition and the compiler
- `TinyRacket.Example` can be used to write example Racket programs
- `TinyRacket.test` contains all the tests, and all the code to generate tests
