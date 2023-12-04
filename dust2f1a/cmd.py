import getopt
import sys, os

from . import dust2f1a

class CommandLineInterface():

    def __init__(self, args) -> None:
        
        self.help = '''dust2f1a [options] <input files>

Options:
-h|--help\t\tShow this help message.
-o|--output\t\tSpecify output directory.
--version\t\tDisplay version.
'''

        self.input_files = []
        self.output_dir = None
        self.arg_opts = []

        if len(args) > 0:
            for a in args:
                if os.path.splitext(a)[1] == "vtu":
                    self.input_files.append(a)
                else:
                    self.arg_opts.append(a)
            if len(self.input_files) == 0:
                print("No .vtu input files detected\n")
                print(self.help)
                sys.exit(0)
        else:
            print("No .vtu input files detected\n")
            print(self.help)
            sys.exit(0)

        self.opts = self.get_options()


    def get_options(self):

        try:
            opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output=", "version"])
        except getopt.GetoptError as err:
            # print help information and exit:
            print(err)  # will print something like "option -a not recognized"
            print(self.help)
            sys.exit(2)
        for o, a in opts:
            if o in ("-h", "--help"):
                print(self.help)
                sys.exit()
            elif o in ("-o", "--output"):
                self.output_dir = a
                if os.path.isdir(self.output_dir):
                    raise ValueError("Specified output directory does not exist.")
            elif o in ("--version"):
                from .__init__ import __version__
                print(__version__)
                sys.exit(0)
            else:
                assert False, "unhandled option"

    def run(self):

        for input in self.input_files:
            dust2f1a.convert(input, self.output_dir)


def main():

    args = sys.argv[1:]

    CLI = CommandLineInterface(args)
    CLI.run()