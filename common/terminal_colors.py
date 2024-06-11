class TerminalColors:
    RESET = "\033[0m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"

    @staticmethod
    def color_text(text, color):
        return f"{color}{text}{TerminalColors.RESET}"