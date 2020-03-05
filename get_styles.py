IFS = """
"""


def STYLES():
    with open('style.qss') as main_styles:
        with open('customizable_styles.qss') as custom_styles:
            all_styles = main_styles.read() + IFS + custom_styles.read()
            return all_styles
