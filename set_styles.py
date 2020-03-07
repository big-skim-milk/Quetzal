font_pattern = "font: "
color_pattern = "color: "
IFS = """
"""


def setCustomStyles(f, c):
    try:
        to_write = []
        with open('customizable_styles.qss') as current_style:
            old_style = current_style.readlines()

        with open('customizable_styles.qss', 'w') as new_style:
            for line in old_style:
                if font_pattern in line:
                    to_write.append(line.replace(line.split(font_pattern)[
                                    1], "75 {} \"{}\";".format(f['size'], f['fam'])))
                elif color_pattern in line:
                    to_write.append(line.replace(
                        line.split(color_pattern)[1], c + ";"))
                else:
                    to_write.append(line)
            new_style.write(IFS.join(to_write).replace('\n\n', '\n'))
            return 'done'
    except KeyError:
        return 'failed'
