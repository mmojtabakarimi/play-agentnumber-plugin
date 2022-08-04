from wazo_confd.helpers.validator import Validator, ValidationGroup


class PlayagentnumberValidator(Validator):
    def validate(self, model):
        return


def build_playagentnumber_validator():
    playagentnumber_validator = PlayagentnumberValidator()
    return ValidationGroup(create=[playagentnumber_validator], edit=[playagentnumber_validator])
