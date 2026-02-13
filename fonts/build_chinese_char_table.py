import akshare as ak  # pip install --upgrade akshare termcolor
import string
from termcolor import colored


def main():
    with open("common_3500_cn_char.txt", 'r') as f2:
        base_3500 = f2.read()

    charset_filename = "char_set.txt"
    with open(charset_filename, "w") as f:
        f.write(string.printable)
        f.write("\n")
        f.write("沪深")
        f.write("↓↑")
        f.write("\n")

        f.write(base_3500)
        f.write("\n")

        full_overview = ak.stock_info_a_code_name()
        stock_list = []
        for _, row, in full_overview.iterrows():
            name = str(row["name"]).replace(" ", "")
            stock_list.append(name)

        for x in sorted(stock_list):
            f.write(x + " ")
        f.write("\n")

    print("all characters written to {}".format(
        colored(charset_filename, "red")))
    print()

    fullsize_fontfile = "SarasaTermSlabSC-Regular.woff2"
    subset_fontfile = "SarasaTermSlabSC-subset.woff2"

    command = \
    '''
pyftsubset {} \\
    --text-file={} \\
    --flavor=woff2 \\
    --output-file={} \\
    --layout-features='*' \\
    --glyph-names
    '''.format(fullsize_fontfile, charset_filename,subset_fontfile)

    print(command)


if __name__ == "__main__":
    main()
