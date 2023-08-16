import os


def title_box(text, delimiter):
    """Accepts a string, and center aligns it in an ascii box.
    text = str()"""
    try:
        max_len = 0
        for line in text.split(delimiter):
            if max_len <= len(line):
                max_len = len(line)
        print('+-' + ('-' * max_len) + '-+')
        for line in text.split(delimiter):
            diff = (max_len - len(line)) // 2
            if (max_len - len(line)) % 2 == 1:
                print('| ' + (' ' * diff) + line + (' ' * diff) + '  |')
            else:
                print('| ' + (' ' * diff) + line + (' ' * diff) + ' |')
        print('+-' + ('-' * max_len) + '-+')
    except AttributeError:
        print("Invalid ascii.center_box input: 'text' and 'delimiter' need to be strings!")


def clear():  # Clear the Windows CMD line
    os.system("cls")


if __name__ == '__main__':  # This code is not run on import
    pass
