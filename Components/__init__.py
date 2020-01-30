from .checkbox import CheckBoxComponent
from .choice import ChoiceComponent
from .option import OptionComponent
from .range import RangeComponent
from .text import TextComponent

__all__ = [
    "CheckboxComponent",
    "ChoiceComponent",
    "OptionComponent",
    "RangeComponent",
    "TextComponent",
]

valid_type = [
    "text",
    "option",
    "range",
    "checkbox",
    "choice"
]

valid_component = [
    CheckBoxComponent,
    ChoiceComponent,
    OptionComponent,
    RangeComponent,
    TextComponent,
]
