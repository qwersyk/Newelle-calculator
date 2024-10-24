import math

from .extensions import NewelleExtension

class CalculatorExtension(NewelleExtension):
    id = "calculator"
    name = "Basic Calculator"

    def get_replace_codeblocks_langs(self) -> list:
        return ["calculator"]

    def get_additional_prompts(self) -> list:
        return [
            {
                "key": "calculator",
                "setting_name": "calculator",
                "title": "Calculator",
                "description": "Enable basic calculator",
                "editable": True,
                "show_in_settings": True,
                "default": True,
                "text": "Use \n```calculator\nexpression\n```\nto evaluate basic mathematical expressions.\n"
                        "Note: Please use standard Python mathematical syntax for correct evaluation."
            }
        ]

    def get_answer(self, codeblock: str, lang: str) -> str | None:
        try:
            result = eval(codeblock, {"__builtins__": None}, {
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "sqrt": math.sqrt,
                "log": math.log,
                "abs": abs,
                "pi": math.pi,
                "e": math.e
            })

            return str(result)
        except Exception as e:
            return f"Error evaluating expression: {e}"
